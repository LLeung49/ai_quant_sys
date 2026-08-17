"""v2_short_term 短期快照的事务持久化。

独立表 ``sector_rotation_short_term_daily_snapshot`` 不会触碰 v1 快照。
所有写入均在同一事务内批量 upsert；任意一行失败时整批回滚。
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

import pandas as pd

from data_ingestion.db_config import get_connection


# 与文档 §7.1 DDL 对齐的列顺序；任何字段重命名必须同步修改表结构。
SHORT_TERM_SNAPSHOT_COLUMNS: tuple[str, ...] = (
    "as_of_date", "sector_level", "sector_name", "model_version", "run_id",
    "coverage_ratio",
    "ret_1", "ret_2", "ret_3",
    "rs_1", "rs_2", "rs_5", "rs5_accel_1d", "ma5_slope",
    "rvol_1_20", "rvol_1_60",
    "amount_share_today", "share_impulse_1d",
    "breadth_up", "breadth_above_ma5", "breadth_new_high_5",
    "breadth_strong_1d", "breadth_weak_1d", "breadth_rvol_1d",
    "limit_up_ratio", "limit_down_ratio",
    "intraday_range", "ret_dispersion",
    "streak_pos_ret", "streak_high_breadth", "streak_top_limit_up",
    "score_eligible",
    "pulse_score", "volume_spike_score", "breadth_spike_score",
    "limit_score", "momentum_shift_score",
    "short_term_composite", "short_term_composite_rank",
    "short_term_labels", "short_term_intensity",
    "eligible_member_count", "valid_member_count",
)
SHORT_TERM_SNAPSHOT_UPDATE_COLUMNS: tuple[str, ...] = tuple(
    column for column in SHORT_TERM_SNAPSHOT_COLUMNS
    if column not in {"as_of_date", "sector_level", "sector_name", "model_version"}
)


def _mysql_nullable(value: Any) -> Any:
    """将 Pandas 缺失值转换为 PyMySQL 可绑定的 SQL NULL。"""
    if value is None:
        return None
    missing = pd.isna(value)
    return None if isinstance(missing, bool) and missing else value


def _execute_many(sql: str, rows: list[tuple[Any, ...]]) -> int:
    """在同一数据库连接中执行批量 upsert，失败回滚整批。"""
    if not rows:
        return 0
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


def persist_short_term_snapshot(
    frame: pd.DataFrame,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    run_id: str,
) -> int:
    """把单个交易日的短期快照 upsert 到独立表。

    参数:
        frame: 每行一个板块的短期特征 + 评分 + 标签 DataFrame。
        as_of_date: 快照归属交易日。
        sector_level: 申万行业层级。
        model_version: 模型版本，写入到唯一键中以便将来与 v1 并存。
        run_id: 关联 ``sector_rotation_run_log`` 的运行 UUID。
    返回:
        成功 upsert 的受影响行数。
    """
    rows: list[tuple[Any, ...]] = []
    for sector_name, row in frame.iterrows():
        name = row.get("sector_name", sector_name)
        values = (
            as_of_date, sector_level, name, model_version, run_id,
            row.get("coverage_ratio"),
            row.get("ret_1"), row.get("ret_2"), row.get("ret_3"),
            row.get("rs_1"), row.get("rs_2"), row.get("rs_5"),
            row.get("rs5_accel_1d"), row.get("ma5_slope"),
            row.get("rvol_1_20"), row.get("rvol_1_60"),
            row.get("amount_share_today"), row.get("share_impulse_1d"),
            row.get("breadth_up"), row.get("breadth_above_ma5"), row.get("breadth_new_high_5"),
            row.get("breadth_strong_1d"), row.get("breadth_weak_1d"), row.get("breadth_rvol_1d"),
            row.get("limit_up_ratio"), row.get("limit_down_ratio"),
            row.get("intraday_range"), row.get("ret_dispersion"),
            row.get("streak_pos_ret"), row.get("streak_high_breadth"), row.get("streak_top_limit_up"),
            bool(row.get("score_eligible", False)),
            row.get("pulse_score"), row.get("volume_spike_score"), row.get("breadth_spike_score"),
            row.get("limit_score"), row.get("momentum_shift_score"),
            row.get("short_term_composite"), row.get("short_term_composite_rank"),
            row.get("short_term_labels"), row.get("short_term_intensity"),
            row.get("eligible_member_count"), row.get("valid_member_count"),
        )
        rows.append(tuple(_mysql_nullable(v) for v in values))
    if not rows:
        return 0

    placeholders = ", ".join(["%s"] * len(SHORT_TERM_SNAPSHOT_COLUMNS))
    sql = f"""
        INSERT INTO sector_rotation_short_term_daily_snapshot
            ({", ".join(SHORT_TERM_SNAPSHOT_COLUMNS)})
        VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE
            {", ".join(f"{col} = VALUES({col})" for col in SHORT_TERM_SNAPSHOT_UPDATE_COLUMNS)}
    """
    return _execute_many(sql, rows)


def create_short_term_run(
    run_id: str,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    config_hash: str,
    source_max_trade_date: str,
) -> int:
    """在事务内插入 ``running`` 审计行，与 v1 共用 ``sector_rotation_run_log`` 表。"""
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO sector_rotation_run_log
                (run_id, as_of_date, sector_level, model_version, config_hash,
                 source_max_trade_date, status, started_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (run_id, as_of_date, sector_level, model_version, config_hash,
             source_max_trade_date, "running", datetime.now()),
        )
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def mark_short_term_run_succeeded(
    run_id: str,
    eligible_sector_count: int,
    skipped_sector_count: int,
) -> int:
    """把审计行标记为 ``succeeded`` 并写入有效 / 跳过的板块计数。

    与 v1 ``mark_run_succeeded`` 共用同一份 ``sector_rotation_run_log`` 表；
    仅通过 ``model_version LIKE 'v2_%'`` 限定短期运行行，避免误更新 v1 审计行。
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            UPDATE sector_rotation_run_log
               SET status = 'succeeded',
                   finished_at = %s,
                   eligible_sector_count = %s,
                   skipped_sector_count = %s
             WHERE run_id = %s
               AND model_version LIKE %s
            """,
            (datetime.now(), eligible_sector_count, skipped_sector_count, run_id, 'v2_%'),
        )
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def mark_short_term_run_failed(run_id: str, reason: str) -> int:
    """把审计行标记为 ``failed`` 并写入 ``error_summary``（与 v1 共用列名）。

    ``error_summary`` 是 ``sector_rotation_run_log`` 表里既有的 TEXT 列；
    不存在 ``error_message`` 列，使用旧名会导致 ``Unknown column`` 报错。
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            UPDATE sector_rotation_run_log
               SET status = 'failed',
                   finished_at = %s,
                   error_summary = %s
             WHERE run_id = %s
               AND model_version LIKE %s
            """,
            (datetime.now(), reason, run_id, 'v2_%'),
        )
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


