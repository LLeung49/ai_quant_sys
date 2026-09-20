"""一次性回填脚本：把历史 ``sector_rotation_short_term_daily_snapshot`` 的 ``rs_5`` 与
``short_term_labels`` 写满。

设计要点
=========

1. v1 快照表 ``sector_rotation_sector_daily_snapshot`` 已经持久化 ``rs_5`` 字段；
   v1 与 v2_short_term 都使用 ``build_market_benchmark(panel)`` 构造归一化基准，
   因此两套快照的 5 日相对强度口径一致，直接以 v1 为主键 JOIN 即可回填。
2. 仅回填指定区间、``v2_short_term`` 模型；遇到 v1 没有 ``rs_5`` 的板块（窗口不足
   或被剔除）会保留 NULL，不强行写 0。
3. 回填 ``rs_5`` 后，按日重新调用 ``classify_short_term_labels`` 写回
   ``short_term_labels`` / ``short_term_intensity``，让 ``short_rebound_candidate`` 与
   ``short_breakdown_candidate`` 与新 ``rs_5`` 对齐。
4. 不修改 ``short_term_composite``、``short_term_composite_rank`` 或 ``score_eligible``，
   避免影响既有 v1 排名与综合分；只动 ``rs_5`` + 标签两个字段。
"""
from __future__ import annotations

import argparse
import logging
from datetime import date

import pandas as pd
import pymysql

from data_ingestion_qmt.db_config import get_connection

from .config import DEFAULT_SHORT_TERM_CONFIG
from .labels import classify_short_term_labels


LOGGER = logging.getLogger(__name__)


DEFAULT_START = date(2026, 8, 1)
DEFAULT_END = date(2026, 8, 14)
DEFAULT_LEVEL = 2
DEFAULT_MODEL = "v2_short_term"
V1_MODEL = "v1"

# 与 ``labels.classify_short_term_labels`` 对齐的最小列。
_LABEL_INPUT_COLUMNS = (
    "sector_name", "score_eligible",
    "rs_1", "rs_5",
    "breadth_up",
    "rvol_1_20", "share_impulse_1d",
    "limit_up_ratio", "limit_down_ratio",
    "ret_1",
    "pulse_score", "volume_spike_score",
)


def _backfill_rs5(start: date, end: date, level: int, model_version: str) -> int:
    """从 v1 快照回填 v2_short_term 的 ``rs_5``。"""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            UPDATE sector_rotation_short_term_daily_snapshot t
              JOIN sector_rotation_sector_daily_snapshot v
                ON v.as_of_date = t.as_of_date
               AND v.sector_level = t.sector_level
               AND v.sector_name = t.sector_name
               AND v.model_version = %s
               SET t.rs_5 = v.rs_5
             WHERE t.model_version = %s
               AND t.sector_level = %s
               AND t.as_of_date BETWEEN %s AND %s
               AND v.rs_5 IS NOT NULL
            """,
            (V1_MODEL, model_version, level, start, end),
        )
        affected = cur.rowcount
        conn.commit()
        LOGGER.info("回填 rs_5 完成：%s 行（%s 至 %s, level=%s）", affected, start, end, level)
        return affected
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def _list_trading_dates(start: date, end: date, level: int, model_version: str) -> list[date]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT DISTINCT as_of_date
          FROM sector_rotation_short_term_daily_snapshot
         WHERE model_version = %s AND sector_level = %s
           AND as_of_date BETWEEN %s AND %s
         ORDER BY as_of_date
        """,
        (model_version, level, start, end),
    )
    dates = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return dates


def _load_label_input_rows(trading_date: date, level: int, model_version: str) -> pd.DataFrame:
    """读取指定日期 ``classify_short_term_labels`` 需要的全部字段。"""
    select_sql = (
        "SELECT sector_name, score_eligible, rs_1, rs_5, breadth_up, "
        "rvol_1_20, share_impulse_1d, limit_up_ratio, limit_down_ratio, "
        "ret_1, pulse_score, volume_spike_score "
        "FROM sector_rotation_short_term_daily_snapshot "
        "WHERE model_version = %s AND sector_level = %s AND as_of_date = %s"
    )
    conn = get_connection()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(select_sql, (model_version, level, trading_date))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        return pd.DataFrame(columns=_LABEL_INPUT_COLUMNS)
    frame = pd.DataFrame(rows)
    for col in ("score_eligible",):
        if col in frame.columns:
            frame[col] = frame[col].astype(bool)
    return frame


def _reload_labels(trading_date: date, level: int, model_version: str) -> int:
    """基于新的 ``rs_5`` 重新生成 ``short_term_labels`` / ``short_term_intensity``。"""
    frame = _load_label_input_rows(trading_date, level, model_version)
    if frame.empty:
        return 0
    conn = get_connection()
    cur = conn.cursor()
    try:
        updated = 0
        for _, row in frame.iterrows():
            labels, intensity = classify_short_term_labels(row, DEFAULT_SHORT_TERM_CONFIG)
            cur.execute(
                """
                UPDATE sector_rotation_short_term_daily_snapshot
                   SET short_term_labels = %s,
                       short_term_intensity = %s
                 WHERE model_version = %s
                   AND sector_level = %s
                   AND as_of_date = %s
                   AND sector_name = %s
                """,
                (labels, intensity, model_version, level, trading_date, row["sector_name"]),
            )
            updated += cur.rowcount
        conn.commit()
        return updated
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="回填 sector_rotation_short_term_daily_snapshot 的 rs_5 与短期标签")
    parser.add_argument("--start", type=str, default=DEFAULT_START.isoformat(), help="起始日期")
    parser.add_argument("--end", type=str, default=DEFAULT_END.isoformat(), help="结束日期")
    parser.add_argument("--level", type=int, default=DEFAULT_LEVEL, help="申万层级 1 或 2")
    parser.add_argument("--model-version", type=str, default=DEFAULT_MODEL, help="模型版本")
    parser.add_argument("--skip-reload-labels", action="store_true", help="仅回填 rs_5，不重算短期标签")
    args = parser.parse_args()

    start = date.fromisoformat(args.start)
    end = date.fromisoformat(args.end)

    affected = _backfill_rs5(start, end, level=args.level, model_version=args.model_version)
    LOGGER.info("rs_5 回填完成，共 %s 行", affected)
    if args.skip_reload_labels:
        return
    total_updated = 0
    for trading_date in _list_trading_dates(start, end, args.level, args.model_version):
        updated = _reload_labels(trading_date, args.level, args.model_version)
        LOGGER.info("重算 %s 的标签：%s 行", trading_date, updated)
        total_updated += updated
    LOGGER.info("短期标签重算完成，共 %s 行", total_updated)


if __name__ == "__main__":
    main()

