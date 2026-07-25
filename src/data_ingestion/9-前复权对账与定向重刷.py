# -*- coding: utf-8 -*-
"""Reconcile legacy and independent QMT front-adjusted daily prices.

The legacy collector remains untouched.  This script is the only new-path code
allowed to update ``trade_stock_daily`` and does so only after an operator
confirms a logged discrepancy with ``--queue-repairs``.

``PRICE_TOLERANCE`` is one unit at the six decimal places stored by both price
tables.  Differences at or below that amount are rounding noise; a larger
difference is persisted for review.
"""

import argparse
import sys
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

try:  # Package import for tests and application modules.
    from .db_config import execute_many, execute_query, execute_update
except ImportError:  # Direct script execution from src/data_ingestion.
    from db_config import execute_many, execute_query, execute_update


PRICE_TOLERANCE = Decimal("0.000001")
PRICE_COLUMNS = ("open_price", "high_price", "low_price", "close_price")
RECONCILE_REASON = "qfq_ohlc_mismatch"

SELECT_QFQ_ROWS_SQL = """
SELECT legacy.stock_code, legacy.trade_date,
       legacy.open_price AS old_open_price,
       legacy.high_price AS old_high_price,
       legacy.low_price AS old_low_price,
       legacy.close_price AS old_close_price,
       projected.open_price AS new_open_price,
       projected.high_price AS new_high_price,
       projected.low_price AS new_low_price,
       projected.close_price AS new_close_price
FROM trade_stock_daily AS legacy
INNER JOIN trade_stock_daily_qfq AS projected
    ON projected.stock_code = legacy.stock_code
   AND projected.trade_date = legacy.trade_date
ORDER BY legacy.stock_code, legacy.trade_date
"""

UPSERT_RECONCILE_LOG_SQL = """
INSERT INTO trade_price_reconcile_log
    (stock_code, trade_date, price_mode,
     old_open_price, old_high_price, old_low_price, old_close_price,
     new_open_price, new_high_price, new_low_price, new_close_price,
     diff_reason, status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'pending')
ON DUPLICATE KEY UPDATE
    old_open_price = VALUES(old_open_price),
    old_high_price = VALUES(old_high_price),
    old_low_price = VALUES(old_low_price),
    old_close_price = VALUES(old_close_price),
    new_open_price = VALUES(new_open_price),
    new_high_price = VALUES(new_high_price),
    new_low_price = VALUES(new_low_price),
    new_close_price = VALUES(new_close_price),
    diff_reason = VALUES(diff_reason),
    status = CASE WHEN status = 'resolved' THEN 'pending' ELSE status END,
    detected_at = CURRENT_TIMESTAMP,
    resolved_at = NULL
"""

MARK_RECONCILE_LOG_RESOLVED_SQL = """
UPDATE trade_price_reconcile_log
SET status = 'resolved', resolved_at = CURRENT_TIMESTAMP
WHERE stock_code = %s
  AND trade_date = %s
  AND price_mode = 'front'
  AND status IN ('pending', 'queued')
"""

SELECT_PENDING_RANGES_SQL = """
SELECT stock_code, MIN(trade_date) AS refresh_from, MAX(trade_date) AS refresh_to
FROM trade_price_reconcile_log
WHERE price_mode = 'front' AND status = 'pending'
GROUP BY stock_code
ORDER BY stock_code
"""

UPSERT_LEGACY_REPAIR_TASK_SQL = """
INSERT INTO trade_legacy_qfq_repair_task
    (stock_code, refresh_from, refresh_to, reason, status)
VALUES (%s, %s, %s, %s, 'pending')
ON DUPLICATE KEY UPDATE
    status = CASE WHEN status = 'done' THEN 'pending' ELSE status END,
    last_error = NULL,
    updated_at = CURRENT_TIMESTAMP
"""

MARK_LOG_RANGE_QUEUED_SQL = """
UPDATE trade_price_reconcile_log
SET status = 'queued'
WHERE stock_code = %s
  AND trade_date BETWEEN %s AND %s
  AND price_mode = 'front'
  AND status = 'pending'
"""

SELECT_PENDING_LEGACY_REPAIRS_SQL = """
SELECT id, stock_code, refresh_from, refresh_to, retry_count
FROM trade_legacy_qfq_repair_task
WHERE status IN ('pending', 'failed')
ORDER BY created_at, id
"""

MARK_LEGACY_REPAIR_RUNNING_SQL = """
UPDATE trade_legacy_qfq_repair_task
SET status = 'running', last_error = NULL, updated_at = CURRENT_TIMESTAMP
WHERE id = %s AND status IN ('pending', 'failed')
"""

MARK_LEGACY_REPAIR_DONE_SQL = """
UPDATE trade_legacy_qfq_repair_task
SET status = 'done', last_error = NULL, updated_at = CURRENT_TIMESTAMP
WHERE id = %s
"""

MARK_LEGACY_REPAIR_FAILED_SQL = """
UPDATE trade_legacy_qfq_repair_task
SET status = 'failed', retry_count = retry_count + 1, last_error = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE id = %s
"""

UPDATE_LEGACY_QFQ_OHLC_SQL = """
UPDATE trade_stock_daily
SET open_price = %s, high_price = %s, low_price = %s, close_price = %s
WHERE stock_code = %s AND trade_date = %s
"""


def _decimal(value) -> Decimal:
    """Convert a database number without binary-floating-point comparisons."""
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid price value: {value!r}") from exc


def find_qfq_discrepancies(rows: list[dict]) -> list[dict]:
    """Return OHLC rows whose old/new prices differ by more than the tolerance."""
    discrepancies = []
    for row in rows:
        old_values = [_decimal(row[f"old_{column}"]) for column in PRICE_COLUMNS]
        new_values = [_decimal(row[f"new_{column}"]) for column in PRICE_COLUMNS]
        if all(abs(old - new) <= PRICE_TOLERANCE for old, new in zip(old_values, new_values)):
            continue
        discrepancy = {
            "stock_code": row["stock_code"],
            "trade_date": row["trade_date"],
            "price_mode": "front",
            "diff_reason": RECONCILE_REASON,
        }
        for column, old_value, new_value in zip(PRICE_COLUMNS, old_values, new_values):
            discrepancy[f"old_{column}"] = old_value
            discrepancy[f"new_{column}"] = new_value
        discrepancies.append(discrepancy)
    return discrepancies


def _log_values(discrepancy: dict) -> tuple:
    return (
        discrepancy["stock_code"],
        discrepancy["trade_date"],
        discrepancy["price_mode"],
        *(discrepancy[f"old_{column}"] for column in PRICE_COLUMNS),
        *(discrepancy[f"new_{column}"] for column in PRICE_COLUMNS),
        discrepancy["diff_reason"],
    )


def reconcile_qfq_prices() -> dict[str, int]:
    """Compare all overlapping qfq rows and idempotently persist differences."""
    rows = execute_query(SELECT_QFQ_ROWS_SQL)
    discrepancies = find_qfq_discrepancies(rows)
    if discrepancies:
        execute_many(UPSERT_RECONCILE_LOG_SQL, [_log_values(item) for item in discrepancies])
    discrepancy_keys = {(item["stock_code"], item["trade_date"]) for item in discrepancies}
    resolved_keys = [
        (row["stock_code"], row["trade_date"])
        for row in rows
        if (row["stock_code"], row["trade_date"]) not in discrepancy_keys
    ]
    if resolved_keys:
        execute_many(MARK_RECONCILE_LOG_RESOLVED_SQL, resolved_keys)
    return {
        "compared": len(rows),
        "discrepancies": len(discrepancies),
        "upserted": len(discrepancies),
    }


def queue_confirmed_legacy_repairs() -> dict[str, int]:
    """Turn reviewed pending logs into idempotent, stock-specific date-range tasks."""
    ranges = execute_query(SELECT_PENDING_RANGES_SQL)
    if not ranges:
        return {"tasks": 0, "queued_logs": 0}
    task_values = [
        (row["stock_code"], row["refresh_from"], row["refresh_to"], RECONCILE_REASON)
        for row in ranges
    ]
    execute_many(UPSERT_LEGACY_REPAIR_TASK_SQL, task_values)
    queued_logs = 0
    for row in ranges:
        queued_logs += execute_update(
            MARK_LOG_RANGE_QUEUED_SQL,
            (row["stock_code"], row["refresh_from"], row["refresh_to"]),
        )
    return {"tasks": len(ranges), "queued_logs": queued_logs}


def _qmt_date(value: date) -> str:
    return value.strftime("%Y%m%d")


def _legacy_ohlc_rows(stock_code: str, dataframe) -> list[tuple]:
    rows = []
    for index_value, row in dataframe.iterrows():
        digits = str(index_value)[:8]
        trade_date = datetime.strptime(digits, "%Y%m%d").date()
        rows.append((
            _decimal(row["open"]), _decimal(row["high"]),
            _decimal(row["low"]), _decimal(row["close"]), stock_code, trade_date,
        ))
    return rows


def refresh_legacy_qfq_range(stock_code: str, refresh_from: date, refresh_to: date) -> int:
    """Fetch one confirmed range and update only legacy qfq OHLC values."""
    from xtquant import xtdata

    xtdata.download_history_data(stock_code, "1d", start_time=_qmt_date(refresh_from))
    market_data = xtdata.get_market_data_ex(
        field_list=["open", "high", "low", "close"],
        stock_list=[stock_code],
        period="1d",
        start_time=_qmt_date(refresh_from),
        end_time=_qmt_date(refresh_to),
        dividend_type="front",
    )
    dataframe = market_data.get(stock_code) if market_data else None
    if dataframe is None or len(dataframe) == 0:
        raise RuntimeError("empty QMT front-adjusted market response")
    rows = _legacy_ohlc_rows(stock_code, dataframe)
    if not rows:
        raise RuntimeError("QMT returned no valid daily rows")
    execute_many(UPDATE_LEGACY_QFQ_OHLC_SQL, rows)
    return len(rows)


def run_pending_legacy_repairs() -> dict[str, int]:
    """Execute durable legacy repairs; failures remain queued for another run."""
    result = {"done": 0, "failed": 0, "updated_rows": 0}
    for task in execute_query(SELECT_PENDING_LEGACY_REPAIRS_SQL):
        if not execute_update(MARK_LEGACY_REPAIR_RUNNING_SQL, (task["id"],)):
            continue
        try:
            updated_rows = refresh_legacy_qfq_range(
                task["stock_code"], task["refresh_from"], task["refresh_to"],
            )
        except Exception as exc:
            execute_update(
                MARK_LEGACY_REPAIR_FAILED_SQL,
                (f"{type(exc).__name__}: {exc}"[:1000], task["id"]),
            )
            result["failed"] += 1
        else:
            execute_update(MARK_LEGACY_REPAIR_DONE_SQL, (task["id"],))
            result["done"] += 1
            result["updated_rows"] += updated_rows
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="对账旧版与独立前复权行情，并按确认结果定向重刷旧表")
    parser.add_argument("--queue-repairs", action="store_true", help="确认并创建旧表定向重刷任务")
    parser.add_argument("--run-repairs", action="store_true", help="执行已确认的旧表重刷任务")
    args = parser.parse_args(argv)

    reconcile_result = reconcile_qfq_prices()
    print(
        "[对账] 比较=%(compared)s 差异=%(discrepancies)s 写入=%(upserted)s"
        % reconcile_result
    )
    if args.queue_repairs:
        queued = queue_confirmed_legacy_repairs()
        print("[重刷任务] 创建=%(tasks)s 标记已确认=%(queued_logs)s" % queued)
    if args.run_repairs:
        repaired = run_pending_legacy_repairs()
        print("[重刷执行] 成功=%(done)s 失败=%(failed)s 更新=%(updated_rows)s" % repaired)
        return 1 if repaired["failed"] else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
