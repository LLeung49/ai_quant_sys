# -*- coding: utf-8 -*-
"""旧前复权与独立前复权的对账、人工确认和定向修复任务。

默认运行只读取两张价格表并维护差异审计日志，绝不修改旧 ``trade_stock_daily``。
只有操作员确认后显式传入 ``--queue-repairs``，才会生成修复任务；再传入
``--run-repairs`` 才会把独立前复权投影 UPSERT 回旧表。这是新链路唯一允许写旧表的入口。

``PRICE_TOLERANCE`` 是两张表六位小数精度中的最小单位。小于等于该值的差异是舍入噪声；
更大差异、以及任一侧缺行都会持久化为可审计记录。
"""

import argparse
import sys
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from uuid import uuid4

try:  # Package import for tests and application modules.
    from .db_config import execute_many, execute_query, execute_update, get_connection
except ImportError:  # Direct script execution from src/data_ingestion_qmt.
    from db_config import execute_many, execute_query, execute_update, get_connection


PRICE_TOLERANCE = Decimal("0.000001")  # 必须与两张价格表的 DECIMAL(..., 6) 精度一致。
PRICE_COLUMNS = ("open_price", "high_price", "low_price", "close_price")
RECONCILE_REASON = "qfq_ohlc_mismatch"

SELECT_DATE_BOUNDS_SQL = """
-- 用两表日期并集决定对账范围，使“仅一侧存在数据”的日期也不会遗漏。
SELECT MIN(trade_date) AS min_date, MAX(trade_date) AS max_date
FROM (
    SELECT trade_date FROM trade_stock_daily
    UNION ALL
    SELECT trade_date FROM trade_stock_daily_qfq
) AS all_dates
"""

SELECT_CODES_BATCH_SQL = """
-- 每个日期批次只枚举实际出现的代码，避免构造全市场笛卡尔扫描。
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
-- 第一半识别旧表存在但独立表缺失，或两侧 OHLC 超出容差的情况。
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
-- 第二半补齐“独立表存在但旧表缺失”；LEFT JOIN + UNION ALL 等价于受控的全外连接。
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
-- 仅复查已有未解决审计记录；已一致的正常行不做任何写入。
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
-- (代码, 日期, 模式) 唯一：重复对账更新最新观测值；已 resolved 后再次差异会重新 pending。
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
-- 只关闭仍待处理/已排队的记录，避免覆盖人工忽略等最终状态。
UPDATE trade_price_reconcile_log
SET status = 'resolved', resolved_at = CURRENT_TIMESTAMP
WHERE stock_code = %s
  AND trade_date = %s
  AND price_mode = 'front'
  AND status IN ('pending', 'queued')
"""

SELECT_PENDING_RANGES_SQL = """
-- 只有可由独立前复权补齐的差异才允许进入旧表修复队列；独立表缺行不能修复旧表。
SELECT stock_code, trade_date AS refresh_from, trade_date AS refresh_to
FROM trade_price_reconcile_log
WHERE price_mode = 'front'
  AND status = 'pending'
  AND diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
ORDER BY stock_code, trade_date
"""

UPSERT_LEGACY_REPAIR_TASK_SQL = """
-- 人工重复确认安全：相同修复任务复用；已完成/运行中任务重新置 pending 并清空认领令牌。
INSERT INTO trade_legacy_qfq_repair_task
    (stock_code, refresh_from, refresh_to, reason, status)
VALUES (%s, %s, %s, %s, 'pending')
ON DUPLICATE KEY UPDATE
    status = CASE
        WHEN status = 'done' THEN 'pending'
        WHEN status = 'running' THEN 'pending'
        ELSE status
    END,
    claim_token = NULL,
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
-- 进程异常退出留下的 running 任务超过租约后自动转 failed，供下一轮重试。
UPDATE trade_legacy_qfq_repair_task
SET status = 'failed',
    retry_count = retry_count + 1,
    last_error = 'Lease expired while task was running; reclaimed automatically',
    claim_token = NULL,
    updated_at = CURRENT_TIMESTAMP
WHERE status = 'running'
  AND updated_at < CURRENT_TIMESTAMP - INTERVAL %s MINUTE
"""

MARK_LEGACY_REPAIR_RUNNING_SQL = """
-- 条件认领：只有 pending/failed 状态可进入 running，claim_token 用于防并发覆盖。
UPDATE trade_legacy_qfq_repair_task
SET status = 'running', claim_token = %s, last_error = NULL,
    updated_at = CURRENT_TIMESTAMP
WHERE id = %s AND status IN ('pending', 'failed')
"""

MARK_LEGACY_REPAIR_DONE_SQL = """
-- 同一事务中完成任务并关闭它覆盖范围内的 queued 差异日志，二者不可只成功其一。
UPDATE trade_legacy_qfq_repair_task AS task
INNER JOIN trade_price_reconcile_log AS log
    ON log.stock_code = task.stock_code
   AND log.trade_date BETWEEN task.refresh_from AND task.refresh_to
   AND log.price_mode = 'front'
   AND log.status = 'queued'
   AND log.diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
SET task.status = 'done',
    task.claim_token = NULL,
    task.last_error = NULL,
    task.updated_at = CURRENT_TIMESTAMP,
    log.status = 'resolved',
    log.resolved_at = CURRENT_TIMESTAMP
WHERE task.claim_token = %s AND task.id = %s AND task.status = 'running'
"""

MARK_LEGACY_REPAIR_FAILED_SQL = """
UPDATE trade_legacy_qfq_repair_task
SET status = 'failed', retry_count = retry_count + 1, last_error = %s,
    claim_token = NULL, updated_at = CURRENT_TIMESTAMP
WHERE claim_token = %s AND id = %s AND status = 'running'
"""

UPSERT_LEGACY_FROM_QFQ_SQL = """
-- 唯一写入旧 trade_stock_daily 的 SQL：只复制已 queued 且已人工确认的独立投影行。
INSERT INTO trade_stock_daily
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate)
SELECT projected.stock_code, projected.trade_date,
       projected.open_price, projected.high_price,
       projected.low_price, projected.close_price,
       projected.volume, projected.amount, projected.turnover_rate
FROM trade_stock_daily_qfq AS projected
INNER JOIN trade_price_reconcile_log AS log
    ON log.stock_code = projected.stock_code
   AND log.trade_date = projected.trade_date
   AND log.price_mode = 'front'
WHERE projected.stock_code = %s
  AND projected.trade_date BETWEEN %s AND %s
  AND log.status = 'queued'
  AND log.diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price),
    high_price = VALUES(high_price),
    low_price = VALUES(low_price),
    close_price = VALUES(close_price),
    volume = VALUES(volume),
    amount = VALUES(amount)
"""

COUNT_QFQ_REPAIR_ROWS_SQL = """
-- 写旧表前先验证存在可复制的源行；零行意味着不应把任务误标为成功。
SELECT COUNT(*) AS row_count
FROM trade_stock_daily_qfq AS projected
INNER JOIN trade_price_reconcile_log AS log
    ON log.stock_code = projected.stock_code
   AND log.trade_date = projected.trade_date
   AND log.price_mode = 'front'
WHERE projected.stock_code = %s
  AND projected.trade_date BETWEEN %s AND %s
  AND log.status = 'queued'
  AND log.diff_reason IN ('qfq_ohlc_mismatch', 'legacy_qfq_missing')
"""

def _decimal(value) -> Decimal:
    """把数据库数值转为 Decimal，避免 float 二进制误差制造虚假的价格差异。"""
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid price value: {value!r}") from exc


def find_qfq_discrepancies(rows: list[dict]) -> list[dict]:
    """识别 OHLC 差异及双向缺失，并生成可直接写入审计表的字典。

    ``legacy_qfq_missing`` 可以由独立投影修复；``projected_qfq_missing`` 只记录告警，
    因为没有可信源行可回写旧表。两侧均存在时才应用六位小数容差比较。
    """
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
    """将代码集合拆为受控批次，限制 SQL IN 参数数量和单次查询内存。"""
    for offset in range(0, len(items), size):
        yield items[offset:offset + size]


def _batch_sql(template: str, code_count: int) -> str:
    """为固定模板生成参数化 IN 占位符；代码值始终通过参数传递而非字符串拼接。"""
    return template.format(code_placeholders=", ".join(["%s"] * code_count))


def reconcile_qfq_prices(
    date_batch_days: int = 31,
    code_batch_size: int = 200,
) -> dict[str, int]:
    """按日期和代码分批找出差异/缺行，并只更新审计日志。

    正常一致行从不写库。每个批次在登记新差异后，只复查此前未解决的日志是否已自然一致，
    因而可每日运行且不会产生全市场无意义 UPDATE。
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
    """把确认可修复的 pending 日志转成可重试的旧表修复任务。

    该函数代表操作员的显式确认边界；它不会处理 ``projected_qfq_missing``，也不会直接写旧表。
    """
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
    """从独立前复权表 UPSERT 一个已确认范围到旧表；零源行直接失败而非静默完成。"""
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


def complete_legacy_qfq_repair(
    task: dict,
    claim_token: str,
    connection_factory=None,
) -> int:
    """原子复制已确认投影行，并完成由当前 ``claim_token`` 认领的任务。

    复制、标记任务完成、关闭日志必须在同一事务内：任一步失败即回滚，避免旧表已更新但
    任务仍显示失败，或任务完成但差异日志未关闭。
    """
    connection_factory = connection_factory or get_connection
    connection = connection_factory()
    cursor = connection.cursor()
    params = (task["stock_code"], task["refresh_from"], task["refresh_to"])
    try:
        cursor.execute(COUNT_QFQ_REPAIR_ROWS_SQL, params)
        count_row = cursor.fetchone()
        source_count = int(count_row[0]) if count_row else 0
        if not source_count:
            raise RuntimeError("independent qfq table returned no queued rows")
        cursor.execute(UPSERT_LEGACY_FROM_QFQ_SQL, params)
        cursor.execute(MARK_LEGACY_REPAIR_DONE_SQL, (claim_token, task["id"]))
        if not cursor.rowcount:
            raise RuntimeError("legacy repair claim was superseded")
        connection.commit()
        return source_count
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def run_pending_legacy_repairs(lease_timeout_minutes: int = 60) -> dict[str, int]:
    """执行持久旧表修复任务；失败任务保留错误与重试次数供下一轮恢复。"""
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
        "superseded": 0,
    }
    for task in execute_query(SELECT_PENDING_LEGACY_REPAIRS_SQL):
        if task.get("retry_count", 0):
            result["retried"] += 1
        # 令牌绑定本次执行，防止被回收并重新认领的任务接受旧进程的完成/失败结果。
        claim_token = str(uuid4())
        if not execute_update(
            MARK_LEGACY_REPAIR_RUNNING_SQL,
            (claim_token, task["id"]),
        ):
            continue
        try:
            updated_rows = complete_legacy_qfq_repair(
                task,
                claim_token,
            )
        except Exception as exc:
            failed = execute_update(
                MARK_LEGACY_REPAIR_FAILED_SQL,
                (
                    f"{type(exc).__name__}: {exc}"[:1000],
                    claim_token,
                    task["id"],
                ),
            )
            result["failed"] += int(bool(failed))
            result["superseded"] += int(not failed)
        else:
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
            "重试=%(retried)s 回收=%(reclaimed)s "
            "已被新任务取代=%(superseded)s"
            % repaired
        )
        return 1 if repaired["failed"] else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

