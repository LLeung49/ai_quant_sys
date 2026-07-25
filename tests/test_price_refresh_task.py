from datetime import date
from pathlib import Path
import sys


SRC_DIR = Path(__file__).parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from data_ingestion.price_refresh_tasks import (  # noqa: E402
    INSERT_REFRESH_TASK_SQL,
    MARK_TASK_DONE_SQL,
    MARK_TASK_FAILED_SQL,
    MARK_TASK_RUNNING_SQL,
    RECLAIM_STALE_TASKS_SQL,
    SELECT_PENDING_TASKS_SQL,
    merge_refresh_tasks,
)


def test_merge_refresh_tasks_keeps_earliest_date_for_same_task_key():
    merged = merge_refresh_tasks(
        [
            {
                "stock_code": "600519.SH",
                "price_mode": "front",
                "refresh_from": date(2015, 1, 1),
                "reason": "corporate_action_changed",
            },
            {
                "stock_code": "600519.SH",
                "price_mode": "front",
                "refresh_from": date(2018, 1, 1),
                "reason": "corporate_action_changed",
            },
        ]
    )

    assert merged == [
        {
            "stock_code": "600519.SH",
            "price_mode": "front",
            "refresh_from": date(2015, 1, 1),
            "reason": "corporate_action_changed",
        }
    ]


def test_merge_refresh_tasks_keeps_different_reasons_separate():
    merged = merge_refresh_tasks(
        [
            {
                "stock_code": "600519.SH",
                "price_mode": "back",
                "refresh_from": date(2024, 6, 1),
                "reason": "corporate_action_changed",
            },
            {
                "stock_code": "600519.SH",
                "price_mode": "back",
                "refresh_from": date(2024, 5, 1),
                "reason": "supplier_ohlc_corrected",
            },
        ]
    )

    assert len(merged) == 2


def test_refresh_task_sql_covers_lifecycle_and_retries():
    assert "ON DUPLICATE KEY UPDATE" in INSERT_REFRESH_TASK_SQL
    assert "LEAST(refresh_from, VALUES(refresh_from))" in INSERT_REFRESH_TASK_SQL
    assert "status IN ('pending', 'failed')" in SELECT_PENDING_TASKS_SQL
    assert "status = 'running'" in MARK_TASK_RUNNING_SQL
    assert "status = 'done'" in MARK_TASK_DONE_SQL
    assert "status = 'failed'" in MARK_TASK_FAILED_SQL
    assert "retry_count = retry_count + 1" in MARK_TASK_FAILED_SQL
    assert "status = 'running'" in RECLAIM_STALE_TASKS_SQL
    assert "retry_count = retry_count + 1" in RECLAIM_STALE_TASKS_SQL
    assert "WHEN status = 'running' THEN 'pending'" in INSERT_REFRESH_TASK_SQL
    assert "claim_token = NULL" in INSERT_REFRESH_TASK_SQL
    assert "claim_token = %s" in MARK_TASK_RUNNING_SQL
    assert "claim_token = %s" in MARK_TASK_DONE_SQL
    assert "claim_token = %s" in MARK_TASK_FAILED_SQL


def test_ddl_defines_all_dual_track_tables_and_refresh_task_uniqueness():
    ddl = (Path(__file__).parents[1] / "sql" / "2026-07-25-dual-track-market-data.sql").read_text(
        encoding="utf-8"
    )

    for table_name in (
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
        "trade_price_reconcile_log",
        "trade_price_refresh_task",
    ):
        assert f"CREATE TABLE IF NOT EXISTS {table_name}" in ddl
    assert "UNIQUE KEY uk_refresh_task (stock_code, price_mode, reason)" in ddl
    assert "trade_stock_daily_raw" in ddl
    assert "trade_corporate_action" in ddl
    assert "SIGNAL SQLSTATE '45000'" in ddl
    assert "claim_token CHAR(36) NULL" in ddl
