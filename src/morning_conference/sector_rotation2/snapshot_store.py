"""版本化板块轮动日快照的事务持久化。

上游源表始终只读。本模块只操作已批准的派生表；任一行写入失败时，
会明确回滚整批快照，避免留下半成品数据。
"""
from __future__ import annotations

from typing import Any
from datetime import datetime

import pandas as pd

from data_ingestion.db_config import get_connection
from data_ingestion.db_config import execute_query


SNAPSHOT_COLUMNS = (
    "as_of_date", "sector_level", "sector_name", "model_version", "run_id",
    "membership_asof_mode", "coverage_ratio", "rs_5", "rs_20", "rs_60", "distance_ma20", "distance_ma60",
    "ma20_slope", "rs20_accel", "ma20_accel", "macd_hist_delta", "rvol_5_20", "share_impulse",
    "breadth_up", "breadth_above_ma20", "breadth_new_high_20", "breadth_rvol", "score_eligible",
    "trend_level_score", "velocity_score", "acceleration_score", "volume_score", "participation_score", "base_score",
    "composite_score", "composite_rank", "phase_raw", "phase_confirmed",
    "phase_age", "phase_changed", "phase_confidence", "market_regime",
    "regime_multiplier", "rank_change_1d", "rank_change_5d", "top10_days_20",
)
# 同日同版本重跑需覆盖所有计算结果；唯一键标识列不可更新。
SNAPSHOT_UPDATE_COLUMNS = tuple(column for column in SNAPSHOT_COLUMNS if column not in {
    "as_of_date", "sector_level", "sector_name", "model_version",
})


def _mysql_nullable(value: Any) -> Any:
    """将 Pandas 缺失值转换为 PyMySQL 可绑定的 SQL NULL。

    参数:
        value: 即将写入数据库的单个标量值，可能是 float NaN、pd.NA 或 pd.NaT。
    返回:
        缺失值返回 None；其他值原样返回。
    """
    if value is None:
        return None
    missing = pd.isna(value)
    return None if isinstance(missing, bool) and missing else value


def _execute_update(sql: str, params: tuple[Any, ...]) -> int:
    """执行一条运行审计写操作，并由本函数明确负责提交或回滚。

    参数:
        sql: 使用 %s 参数占位符的单条审计 SQL。
        params: 与 SQL 占位符一一对应的参数元组。
    返回:
        数据库受影响行数。
    异常:
        Exception: 数据库执行失败时先回滚，再原样抛出。
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, params)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def create_run(
    run_id: str,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    config_hash: str,
    source_max_trade_date: str,
) -> int:
    """在每日快照持久化前创建可追溯的 running 审计记录。

    参数:
        run_id: 本次运行的唯一 UUID。
        as_of_date: 计算所对应的交易日。
        sector_level: 申万行业层级，当前支持 1 或 2。
        model_version: 评分模型版本。
        config_hash: 本次模型配置的确定性哈希。
        source_max_trade_date: 上游源表可用的最大交易日。
    返回:
        数据库受影响行数，正常为 1。
    """
    return _execute_update(
        """
        INSERT INTO sector_rotation_run_log
            (run_id, as_of_date, sector_level, model_version, config_hash,
             source_max_trade_date, status, started_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (run_id, as_of_date, sector_level, model_version, config_hash,
         source_max_trade_date, "running", datetime.now()),
    )


def mark_run_failed(run_id: str, error_summary: str) -> int:
    """在数据事务回滚后，将已有审计记录标记为 failed 并写入错误摘要。

    参数:
        run_id: 需要更新状态的运行唯一标识。
        error_summary: 可供排障和报告展示的错误摘要。
    返回:
        数据库受影响行数。
    """
    return _execute_update(
        """
        UPDATE sector_rotation_run_log
        SET status = %s, error_summary = %s, finished_at = NOW()
        WHERE run_id = %s
        """,
        ("failed", error_summary, run_id),
    )


def mark_run_succeeded(run_id: str, eligible_sector_count: int, skipped_sector_count: int) -> int:
    """将运行审计更新为成功，并记录本次有效/跳过板块数量。

    参数:
        run_id: 已完成持久化的运行唯一标识。
        eligible_sector_count: 有综合排名的板块数量。
        skipped_sector_count: 因覆盖或评分证据不足而跳过的板块数量。
    返回:
        数据库受影响行数。
    """
    return _execute_update(
        """
        UPDATE sector_rotation_run_log
        SET status = %s, eligible_sector_count = %s, skipped_sector_count = %s, finished_at = NOW()
        WHERE run_id = %s
        """,
        ("succeeded", eligible_sector_count, skipped_sector_count, run_id),
    )


def load_previous_snapshots(as_of_date: str, sector_level: int, model_version: str) -> pd.DataFrame:
    """读取目标日前最近二十日快照，供 phase 和排名历史计算使用。

    参数:
        as_of_date: 当前待运行交易日；查询严格使用小于号，避免同日重跑读取自身。
        sector_level: 行业层级。
        model_version: 模型版本，防止混用不同评分口径的历史。
    返回:
        每板块最多二十条、按日期升序的历史快照 DataFrame；无数据时为空表。
    """
    sql = """
        SELECT as_of_date, sector_name, phase_raw, phase_confirmed, phase_age,
               velocity_score, composite_rank, top10_days_20
        FROM sector_rotation_sector_daily_snapshot
        WHERE as_of_date < %s AND sector_level = %s AND model_version = %s
        ORDER BY as_of_date DESC
    """
    # 既有 data_ingestion.execute_query 契约是“字典列表/元组”，不是 DataFrame。
    # 在持久化边界立即转换，避免调用方误将 tuple 当作 DataFrame 使用。
    history = pd.DataFrame(execute_query(sql, (as_of_date, sector_level, model_version)))
    if history.empty:
        return history
    history["as_of_date"] = pd.to_datetime(history["as_of_date"])
    return history.sort_values("as_of_date")


def persist_daily_snapshot(
    frame: pd.DataFrame,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    run_id: str,
) -> int:
    """在一个数据库事务中 upsert 某日的全部板块快照。

唯一键为日期、层级、板块名和模型版本；同一模型同日重跑时更新数值和
run_id，而不是新增重复快照。

    参数:
        frame: 每行一个板块的评分/状态 DataFrame；sector_name 可为列或索引。
        as_of_date: 快照归属交易日。
        sector_level: 申万行业层级。
        model_version: 模型版本，属于快照唯一键的一部分。
        run_id: 写入本批快照的运行审计 ID。
    返回:
        成功 upsert 的受影响行数；空 DataFrame 返回 0。
    异常:
        Exception: 任意写入失败时整批回滚后原样抛出。
    """
    rows: list[tuple[Any, ...]] = []
    for sector_name, row in frame.iterrows():
        name = row.get("sector_name", sector_name)
        row_values = (
            as_of_date, sector_level, name, model_version, run_id,
            row.get("membership_asof_mode", "current_mapping"), row.get("coverage_ratio"),
            row.get("rs_5"), row.get("rs_20"), row.get("rs_60"), row.get("distance_ma20"), row.get("distance_ma60"),
            row.get("ma20_slope"), row.get("rs20_accel"), row.get("ma20_accel"), row.get("macd_hist_delta"),
            row.get("rvol_5_20"), row.get("share_impulse"), row.get("breadth_up"), row.get("breadth_above_ma20"),
            row.get("breadth_new_high_20"), row.get("breadth_rvol"),
            bool(row.get("score_eligible", False)), row.get("trend_level_score"), row.get("velocity_score"),
            row.get("acceleration_score"), row.get("volume_score"), row.get("participation_score"), row.get("base_score"),
            row.get("composite_score"), row.get("composite_rank"), row.get("phase_raw"),
            row.get("phase_confirmed"), row.get("phase_age"), row.get("phase_changed"),
            row.get("phase_confidence"), row.get("market_regime"), row.get("regime_multiplier"),
            row.get("rank_change_1d"), row.get("rank_change_5d"), row.get("top10_days_20"),
        )
        # MySQL 的 DECIMAL/日期可为空；PyMySQL 不接受 float('nan')，必须显式传 None。
        rows.append(tuple(_mysql_nullable(value) for value in row_values))
    if not rows:
        return 0

    # 列名来自内部固定常量；所有运行时数据值都使用参数化占位符，避免拼接 SQL 值。
    placeholders = ", ".join(["%s"] * len(SNAPSHOT_COLUMNS))
    sql = f"""
        INSERT INTO sector_rotation_sector_daily_snapshot ({", ".join(SNAPSHOT_COLUMNS)})
        VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE
            {", ".join(f"{column} = VALUES({column})" for column in SNAPSHOT_UPDATE_COLUMNS)}
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, rows)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def persist_forward_returns(frame: pd.DataFrame, sector_level: int) -> int:
    """参数化 upsert 已成熟的前瞻收益标签。

    参数:
        frame: ``build_forward_return_labels`` 生成的标签 DataFrame。
        sector_level: 标签对应的行业层级。
    返回:
        数据库受影响行数；空表返回 0。
    """
    if frame.empty:
        return 0
    columns = ("as_of_date", "sector_level", "sector_name", "horizon", "target_date", "sector_return", "benchmark_return", "excess_return", "label_ready_at")
    rows = [
        (row.as_of_date, sector_level, row.sector_name, row.horizon, row.target_date,
         row.sector_return, row.benchmark_return, row.excess_return, datetime.now())
        for row in frame.itertuples(index=False)
    ]
    sql = f"""
        INSERT INTO sector_rotation_sector_forward_return ({", ".join(columns)})
        VALUES ({", ".join(["%s"] * len(columns))})
        ON DUPLICATE KEY UPDATE target_date = VALUES(target_date), sector_return = VALUES(sector_return),
            benchmark_return = VALUES(benchmark_return), excess_return = VALUES(excess_return),
            label_ready_at = VALUES(label_ready_at)
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, rows)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
