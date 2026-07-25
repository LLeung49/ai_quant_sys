"""Persistent refresh-task SQL and small, database-free task helpers."""

from collections.abc import Iterable
from datetime import date


INSERT_REFRESH_TASK_SQL = """
INSERT INTO trade_price_refresh_task
    (stock_code, price_mode, refresh_from, reason, status)
VALUES (%s, %s, %s, %s, 'pending')
ON DUPLICATE KEY UPDATE
    refresh_from = LEAST(refresh_from, VALUES(refresh_from)),
    status = CASE WHEN status = 'done' THEN 'pending' ELSE status END,
    last_error = NULL,
    updated_at = CURRENT_TIMESTAMP
"""

SELECT_PENDING_TASKS_SQL = """
SELECT id, stock_code, price_mode, refresh_from, reason, retry_count
FROM trade_price_refresh_task
WHERE status IN ('pending', 'failed')
ORDER BY created_at, id
"""

RECLAIM_STALE_TASKS_SQL = """
UPDATE trade_price_refresh_task
SET status = 'failed',
    retry_count = retry_count + 1,
    last_error = 'Lease expired while task was running; reclaimed automatically',
    updated_at = CURRENT_TIMESTAMP
WHERE status = 'running'
  AND updated_at < CURRENT_TIMESTAMP - INTERVAL %s MINUTE
"""

MARK_TASK_RUNNING_SQL = """
UPDATE trade_price_refresh_task
SET status = 'running', last_error = NULL, updated_at = CURRENT_TIMESTAMP
WHERE id = %s AND status IN ('pending', 'failed')
"""

MARK_TASK_DONE_SQL = """
UPDATE trade_price_refresh_task
SET status = 'done', last_error = NULL, updated_at = CURRENT_TIMESTAMP
WHERE id = %s
"""

MARK_TASK_FAILED_SQL = """
UPDATE trade_price_refresh_task
SET status = 'failed', retry_count = retry_count + 1, last_error = %s,
    updated_at = CURRENT_TIMESTAMP
WHERE id = %s
"""


def merge_refresh_tasks(tasks: Iterable[dict]) -> list[dict]:
    """Merge duplicate refresh requests and keep their earliest start date.

    A task is identified by stock, adjustment mode, and reason.  Ordering follows
    its first appearance so daily logs and database writes remain predictable.
    """
    merged: dict[tuple[str, str, str], dict] = {}
    for task in tasks:
        key = (task["stock_code"], task["price_mode"], task["reason"])
        refresh_from = task["refresh_from"]
        if not isinstance(refresh_from, date):
            raise TypeError("refresh_from must be a datetime.date")
        current = merged.get(key)
        if current is None or refresh_from < current["refresh_from"]:
            merged[key] = dict(task)
    return list(merged.values())
