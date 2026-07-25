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
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation

try:  # Package import for tests and application modules.
    from .db_config import execute_many, execute_query, execute_update
except ImportError:  # Direct script execution from src/data_ingestion.
    from db_config import execute_many, execute_query, execute_update


PRICE_TOLERANCE = Decimal("0.000001")
PRICE_COLUMNS = ("open_price", "high_price", "low_price", "close_price")
RECONCILE_REASON = "qfq_ohlc_mismatch"

SELECT_DATE_BOUNDS_SQL = """
SELECT MIN(trade_date) AS min_date, MAX(trade_date) AS max_date
FROM (
    SELECT trade_date FROM trade_stock_daily
    UNION ALL
    SELECT trade_date FROM trade_stock_daily_qfq
) AS all_dates
"""

SELECT_CODES_BATCH_SQL = """
SELECT stock_code
FROM (
    SELECT stock_code FROM trade_stock_daily
    WHERE trade_date BETWEEN %s AND %s
    UNION
    SELECT stock_code FROM trade_stock_daily_qfq
    WHERE trade_date BETWEEN %s AND %s
) AS codes
ORDER BY stock_code
"""

SELECT_DISCREPANCIES_BATCH_SQL = """
SELECT legacy.stock_code, legacy.trade_date,
       legacy.open_price AS old_open_price,
       legacy.high_price AS old_high_price,
       legacy.low_price AS old_low_price,
       legacy.close_price AS old_close_price,
       projected.open_price AS new_open_price,
       projected.high_price AS new_high_price,
       projected.low_price AS new_low_price,
       projected.close_price AS new_close_price,
       1 AS legacy_exists,
       CASE WHEN projected.stock_code IS NULL THEN 0 ELSE 1 END AS projected_exists
FROM trade_stock_daily AS legacy
LEFT JOIN trade_stock_daily_qfq AS projected
    ON projected.stock_code = legacy.stock_code
   AND projected.trade_date = legacy.trade_date
WHERE legacy.trade_date BETWEEN %s AND %s
  AND legacy.stock_code IN ({code_placeholders})
  AND (
      projected.stock_code IS NULL
      OR ABS(legacy.open_price - projected.open_price) > 0.000001
      OR ABS(legacy.high_price - projected.high_price) > 0.000001
      OR ABS(legacy.low_price - projected.low_price) > 0.000001
      OR ABS(legacy.close_price - projected.close_price) > 0.000001
  )
UNION ALL
SELECT projected.stock_code, projected.trade_date,
       NULL, NULL, NULL, NULL,
       projected.open_price, projected.high_price,
       projected.low_price, projected.close_price,
       0 AS legacy_exists, 1 AS projected_exists
FROM trade_stock_daily_qfq AS projected
LEFT JOIN trade_stock_daily AS legacy
    ON legacy.stock_code = projected.stock_code
   AND legacy.trade_date = projected.trade_date
WHERE projected.trade_date BETWEEN %s AND %s
  AND projected.stock_code IN ({code_placeholders})
  AND legacy.stock_code IS NULL
ORDER BY stock_code, trade_date
"""

SELECT_UNRESOLVED_LOGS_SQL = """
SELECT log.stock_code, log.trade_date,
       legacy.open_price AS old_open_price,
       legacy.high_price AS old_high_price,
       legacy.low_price AS old_low_price,
       legacy.close_price AS old_close_price,
       projected.open_price AS new_open_price,
       projected.high_price AS new_high_price,
       projected.low_price AS new_low_price,
       projected.close_price AS new_close_price,
       CASE WHEN legacy.stock_code IS NULL THEN 0 ELSE 1 END AS legacy_exists,
       CASE WHEN projected.stock_code IS NULL THEN 0 ELSE 1 END AS projected_exists
FROM trade_price_reconcile_log AS log
LEFT JOIN trade_stock_daily AS legacy
    ON legacy.stock_code = log.stock_code AND legacy.trade_date = log.trade_date
LEFT JOIN trade_stock_daily_qfq AS projected
    ON projected.stock_code = log.stock_code AND projected.trade_date = log.trade_date
WHERE log.price_mode = 'front'
  AND log.status IN ('pending', 'queued')
  AND log.trade_date BETWEEN %s AND %s
  AND log.stock_code IN ({code_placeholders})
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
WHERE price_mode = 'front'
  AND status = 'pending'
  AND diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
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
  AND diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
"""

SELECT_PENDING_LEGACY_REPAIRS_SQL = """
SELECT id, stock_code, refresh_from, refresh_to, retry_count
FROM trade_legacy_qfq_repair_task
WHERE status IN ('pending', 'failed')
ORDER BY created_at, id
"""

RECLAIM_STALE_LEGACY_REPAIRS_SQL = """
UPDATE trade_legacy_qfq_repair_task
SET status = 'failed',
    retry_count = retry_count + 1,
    last_error = 'Lease expired while task was running; reclaimed automatically',
    updated_at = CURRENT_TIMESTAMP
WHERE status = 'running'
  AND updated_at < CURRENT_TIMESTAMP - INTERVAL %s MINUTE
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

UPSERT_LEGACY_FROM_QFQ_SQL = """
INSERT INTO trade_stock_daily
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate)
SELECT stock_code, trade_date, open_price, high_price, low_price, close_price,
       volume, amount, turnover_rate
FROM trade_stock_daily_qfq
WHERE stock_code = %s AND trade_date BETWEEN %s AND %s
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price),
    high_price = VALUES(high_price),
    low_price = VALUES(low_price),
    close_price = VALUES(close_price),
    volume = VALUES(volume),
    amount = VALUES(amount)
"""

COUNT_QFQ_REPAIR_ROWS_SQL = """
SELECT COUNT(*) AS row_count
FROM trade_stock_daily_qfq
WHERE stock_code = %s AND trade_date BETWEEN %s AND %s
"""

MARK_LOG_RANGE_RESOLVED_SQL = """
UPDATE trade_price_reconcile_log
SET status = 'resolved', resolved_at = CURRENT_TIMESTAMP
WHERE stock_code = %s
  AND trade_date BETWEEN %s AND %s
  AND price_mode = 'front'
  AND status IN ('pending', 'queued')
  AND diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
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
        legacy_exists = bool(row.get("legacy_exists", 1))
        projected_exists = bool(row.get("projected_exists", 1))
        old_values = [
            _decimal(row[f"old_{column}"]) if legacy_exists else None
            for column in PRICE_COLUMNS
        ]
        new_values = [
            _decimal(row[f"new_{column}"]) if projected_exists else None
            for column in PRICE_COLUMNS
        ]
        if not legacy_exists:
            reason = "legacy_qfq_missing"
        elif not projected_exists:
            reason = "projected_qfq_missing"
        elif all(
            abs(old - new) <= PRICE_TOLERANCE
            for old, new in zip(old_values, new_values)
        ):
            continue
        else:
            reason = RECONCILE_REASON
        discrepancy = {
            "stock_code": row["stock_code"],
            "trade_date": row["trade_date"],
            "price_mode": "front",
            "diff_reason": reason,
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


def _chunks(items: list, size: int):
    for offset in range(0, len(items), size):
        yield items[offset:offset + size]


def _batch_sql(template: str, code_count: int) -> str:
    return template.format(code_placeholders=", ".join(["%s"] * code_count))


def reconcile_qfq_prices(
    date_batch_days: int = 31,
    code_batch_size: int = 200,
) -> dict[str, int]:
    """Find missing/different rows in bounded date/code batches.

    Matching rows are never updated.  Only previously unresolved audit rows are
    checked for resolution, which avoids full-market no-op writes.
    """
    bounds = execute_query(SELECT_DATE_BOUNDS_SQL)
    if not bounds or not bounds[0]["min_date"]:
        return {"compared": 0, "discrepancies": 0, "upserted": 0, "resolved": 0}
    current = bounds[0]["min_date"]
    maximum = bounds[0]["max_date"]
    result = {"compared": 0, "discrepancies": 0, "upserted": 0, "resolved": 0}
    while current <= maximum:
        batch_end = min(maximum, current + timedelta(days=date_batch_days - 1))
        code_rows = execute_query(
            SELECT_CODES_BATCH_SQL,
            (current, batch_end, current, batch_end),
        )
        codes = [row["stock_code"] for row in code_rows]
        for code_batch in _chunks(codes, code_batch_size):
            if not code_batch:
                continue
            discrepancy_sql = _batch_sql(
                SELECT_DISCREPANCIES_BATCH_SQL,
                len(code_batch),
            )
            params = (
                current, batch_end, *code_batch,
                current, batch_end, *code_batch,
            )
            rows = execute_query(discrepancy_sql, params)
            discrepancies = find_qfq_discrepancies(rows)
            if discrepancies:
                execute_many(
                    UPSERT_RECONCILE_LOG_SQL,
                    [_log_values(item) for item in discrepancies],
                )
            result["compared"] += len(rows)
            result["discrepancies"] += len(discrepancies)
            result["upserted"] += len(discrepancies)

            unresolved_sql = _batch_sql(
                SELECT_UNRESOLVED_LOGS_SQL,
                len(code_batch),
            )
            unresolved = execute_query(
                unresolved_sql,
                (current, batch_end, *code_batch),
            )
            resolved_keys = [
                (row["stock_code"], row["trade_date"])
                for row in unresolved
                if not find_qfq_discrepancies([row])
            ]
            if resolved_keys:
                execute_many(MARK_RECONCILE_LOG_RESOLVED_SQL, resolved_keys)
                result["resolved"] += len(resolved_keys)
        current = batch_end + timedelta(days=1)
    return result


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


def refresh_legacy_qfq_range(stock_code: str, refresh_from: date, refresh_to: date) -> int:
    """UPSERT a confirmed range from the independent qfq projection."""
    params = (stock_code, refresh_from, refresh_to)
    rows = execute_query(COUNT_QFQ_REPAIR_ROWS_SQL, params)
    source_count = int(rows[0]["row_count"]) if rows else 0
    if not source_count:
        raise RuntimeError("independent qfq table returned no rows for repair range")
    execute_update(
        UPSERT_LEGACY_FROM_QFQ_SQL,
        params,
    )
    return source_count


def run_pending_legacy_repairs(lease_timeout_minutes: int = 60) -> dict[str, int]:
    """Execute durable legacy repairs; failures remain queued for another run."""
    reclaimed = execute_update(
        RECLAIM_STALE_LEGACY_REPAIRS_SQL,
        (lease_timeout_minutes,),
    )
    result = {
        "done": 0,
        "failed": 0,
        "updated_rows": 0,
        "retried": 0,
        "reclaimed": reclaimed,
    }
    for task in execute_query(SELECT_PENDING_LEGACY_REPAIRS_SQL):
        if task.get("retry_count", 0):
            result["retried"] += 1
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
            execute_update(
                MARK_LOG_RANGE_RESOLVED_SQL,
                (task["stock_code"], task["refresh_from"], task["refresh_to"]),
            )
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
        "[对账] 比较=%(compared)s 差异=%(discrepancies)s 写入=%(upserted)s "
        "已解决=%(resolved)s"
        % reconcile_result
    )
    if args.queue_repairs:
        queued = queue_confirmed_legacy_repairs()
        print("[重刷任务] 创建=%(tasks)s 标记已确认=%(queued_logs)s" % queued)
    if args.run_repairs:
        repaired = run_pending_legacy_repairs()
        print(
            "[重刷执行] 成功=%(done)s 失败=%(failed)s 更新=%(updated_rows)s "
            "重试=%(retried)s 回收=%(reclaimed)s"
            % repaired
        )
        return 1 if repaired["failed"] else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
