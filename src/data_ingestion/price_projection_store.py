"""独立原始/前复权/后复权日线表的固定写入边界。

本模块把 QMT ``dividend_type`` 映射到唯一允许写入的三张新表，并集中维护其 UPSERT。
它刻意不知道旧 ``trade_stock_daily`` 的写入 SQL：即使新采集任务发生故障，也不会污染
正在使用的旧前复权链路。旧表只能由独立的、人工确认后的对账修复脚本写入。
"""

from datetime import date, datetime, timezone
import hashlib
import json

try:  # Package import for tests and application modules.
    from .db_config import execute_many, execute_query, get_connection
    from .market_row_validation import validate_market_row
except ImportError:  # Direct ``python 8-...py`` execution.
    from db_config import execute_many, execute_query, get_connection
    from market_row_validation import validate_market_row


TABLE_BY_DIVIDEND_TYPE = {
    # 该白名单同时是防误写保护：未知 QMT 模式不能拼接为任意表名。
    "none": "trade_stock_daily_raw",
    "front": "trade_stock_daily_qfq",
    "back": "trade_stock_daily_bfq",
}

RAW_INSERT_SQL = """
-- 原始行情是交易事实；重复下载同一日期时以供应商最新值幂等覆盖。
INSERT INTO trade_stock_daily_raw
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, pre_close, suspend_flag, data_source,
     rebuild_batch_id, rebuild_source, rebuild_fetched_at, rebuild_fingerprint,
     rebuild_validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'valid')
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    pre_close = VALUES(pre_close), suspend_flag = VALUES(suspend_flag),
    data_source = VALUES(data_source),
    rebuild_batch_id = VALUES(rebuild_batch_id),
    rebuild_source = VALUES(rebuild_source),
    rebuild_fetched_at = VALUES(rebuild_fetched_at),
    rebuild_fingerprint = VALUES(rebuild_fingerprint),
    rebuild_validation_status = VALUES(rebuild_validation_status),
    updated_at = CURRENT_TIMESTAMP
"""

QFQ_INSERT_SQL = """
-- 独立前复权投影；adjustment_asof 记录本行已包含到哪个权益事件版本。
INSERT INTO trade_stock_daily_qfq
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate, adjustment_asof,
     rebuild_batch_id, rebuild_source, rebuild_fetched_at, rebuild_fingerprint,
     rebuild_validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'valid')
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    turnover_rate = VALUES(turnover_rate),
    adjustment_asof = VALUES(adjustment_asof),
    rebuild_batch_id = VALUES(rebuild_batch_id),
    rebuild_source = VALUES(rebuild_source),
    rebuild_fetched_at = VALUES(rebuild_fetched_at),
    rebuild_fingerprint = VALUES(rebuild_fingerprint),
    rebuild_validation_status = VALUES(rebuild_validation_status),
    refreshed_at = CURRENT_TIMESTAMP
"""

BFQ_INSERT_SQL = """
-- 独立后复权投影；正常新增权益事件通常只需增量写入，历史修订才由任务表回补。
INSERT INTO trade_stock_daily_bfq
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate, adjustment_asof,
     rebuild_batch_id, rebuild_source, rebuild_fetched_at, rebuild_fingerprint,
     rebuild_validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'valid')
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    turnover_rate = VALUES(turnover_rate),
    adjustment_asof = VALUES(adjustment_asof),
    rebuild_batch_id = VALUES(rebuild_batch_id),
    rebuild_source = VALUES(rebuild_source),
    rebuild_fetched_at = VALUES(rebuild_fetched_at),
    rebuild_fingerprint = VALUES(rebuild_fingerprint),
    rebuild_validation_status = VALUES(rebuild_validation_status),
    refreshed_at = CURRENT_TIMESTAMP
"""

INSERT_SQL_BY_DIVIDEND_TYPE = {
    "none": RAW_INSERT_SQL,
    "front": QFQ_INSERT_SQL,
    "back": BFQ_INSERT_SQL,
}

DEFAULT_WRITE_CHUNK_SIZE = 10000

LATEST_DATE_SQL_BY_DIVIDEND_TYPE = {
    # 每个模式单独取游标，再由采集器选择最早日期以保证三张表日期对齐。
    "none": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_raw GROUP BY stock_code",
    "front": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_qfq GROUP BY stock_code",
    "back": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_bfq GROUP BY stock_code",
}


def _daily_metadata(
    row: dict,
    adjustment_asof: date | None,
    fetched_at: datetime,
) -> tuple[str, str, datetime, str]:
    source = str(row.get("data_source") or "akshare")
    batch_date = adjustment_asof or date.fromisoformat(str(row["trade_date"])[:10])
    batch_id = f"daily-{source}-{batch_date:%Y%m%d}"
    payload = {
        key: row.get(key)
        for key in (
            "stock_code", "trade_date", "open_price", "high_price", "low_price",
            "close_price", "volume", "amount", "pre_close", "suspend_flag",
            "turnover_rate", "data_source",
        )
    }
    payload["adjustment_asof"] = adjustment_asof
    fingerprint = hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return batch_id, f"{source}_daily", fetched_at, fingerprint


def table_for_mode(dividend_type: str) -> str:
    """返回模式的固定目标表；拒绝未知模式，防止动态 SQL 表名注入/误写。"""
    try:
        return TABLE_BY_DIVIDEND_TYPE[dividend_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported dividend type: {dividend_type}") from exc


def _validate_rows(dividend_type: str, rows: list[dict]) -> None:
    """Reject the complete write when any row could corrupt persisted prices."""
    failures = []
    for row in rows:
        result = validate_market_row(
            row, allow_negative_price=(dividend_type == "front")
        )
        failures.extend(issue for issue in result.issues if issue.severity == "error")
    if failures:
        detail = "; ".join(
            f"{issue.stock_code}/{issue.trade_date}/{issue.field}: {issue.code}"
            for issue in failures[:10]
        )
        if len(failures) > 10:
            detail += f"; ... {len(failures) - 10} more"
        raise ValueError(f"market row validation failed: {detail}")


def get_existing_latest_dates(dividend_type: str) -> dict[str, str]:
    """取得一种模式中每个代码的最新落库日期，供上层决定增量起点。"""
    table_for_mode(dividend_type)
    rows = execute_query(LATEST_DATE_SQL_BY_DIVIDEND_TYPE[dividend_type])
    return {
        row["stock_code"]: row["max_date"].strftime("%Y%m%d")
        for row in rows
        if row["max_date"]
    }


def write_daily_rows(
    dividend_type: str, rows: list[dict], adjustment_asof: date | None,
) -> int:
    """将同一模式的一批行幂等写入其固定表，返回驱动报告的影响行数。

    原始数据和复权投影刻意使用不同列集：前者保留昨收/停牌事实，后者保留权益事件版本。
    空列表不发 SQL，避免调用方将无行情响应误记为成功写入。
    """
    if not rows:
        return 0
    table_for_mode(dividend_type)
    _validate_rows(dividend_type, rows)
    fetched_at = datetime.now(timezone.utc).replace(tzinfo=None)
    if dividend_type == "none":
        values = [
            (
                row["stock_code"], row["trade_date"], row["open_price"],
                row["high_price"], row["low_price"], row["close_price"],
                row["volume"], row["amount"], row.get("pre_close"),
                row.get("suspend_flag"), row.get("data_source", "akshare"),
                *_daily_metadata(row, adjustment_asof, fetched_at),
            )
            for row in rows
        ]
    else:
        values = [
            (
                row["stock_code"], row["trade_date"], row["open_price"],
                row["high_price"], row["low_price"], row["close_price"],
                row["volume"], row["amount"], row.get("turnover_rate"),
                adjustment_asof,
                *_daily_metadata(row, adjustment_asof, fetched_at),
            )
            for row in rows
        ]
    return execute_many(INSERT_SQL_BY_DIVIDEND_TYPE[dividend_type], values)


def write_projection_batch(rows_by_mode: dict[str, list[dict]], adjustment_asof: date) -> int:
    """Write one instrument's three validated projections atomically."""
    if set(rows_by_mode) != set(TABLE_BY_DIVIDEND_TYPE):
        raise ValueError("all three market projections are required")
    for mode, rows in rows_by_mode.items():
        table_for_mode(mode)
        if not rows:
            raise ValueError(f"empty {mode} market projection")
        _validate_rows(mode, rows)

    conn = get_connection()
    cursor = conn.cursor()
    affected = 0
    fetched_at = datetime.now(timezone.utc).replace(tzinfo=None)
    try:
        for mode in ("none", "front", "back"):
            rows = rows_by_mode[mode]
            if mode == "none":
                values = [(
                    row["stock_code"], row["trade_date"], row["open_price"],
                    row["high_price"], row["low_price"], row["close_price"],
                    row["volume"], row["amount"], row.get("pre_close"),
                    row.get("suspend_flag"), row.get("data_source", "akshare"),
                    *_daily_metadata(row, adjustment_asof, fetched_at),
                ) for row in rows]
            else:
                values = [(
                    row["stock_code"], row["trade_date"], row["open_price"],
                    row["high_price"], row["low_price"], row["close_price"],
                    row["volume"], row["amount"], row.get("turnover_rate"),
                    adjustment_asof,
                    *_daily_metadata(row, adjustment_asof, fetched_at),
                ) for row in rows]
            affected += cursor.executemany(INSERT_SQL_BY_DIVIDEND_TYPE[mode], values)
        conn.commit()
        return affected
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


def write_daily_rows_batch(
    dividend_type: str,
    rows: list[dict],
    adjustment_asofs: dict[str, date | None],
    chunk_size: int = DEFAULT_WRITE_CHUNK_SIZE,
) -> int:
    """批量 UPSERT 多只股票的一种价格模式。

    该函数仅供日常增量采集使用。每只股票的 ``adjustment_asof`` 可能不同，不能把
    整个批次误写成同一个权益版本；原始模式不使用该字段。单股票历史刷新仍使用
    :func:`write_daily_rows`，保持调用边界简单。
    """
    if not rows:
        return 0
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    table_for_mode(dividend_type)
    _validate_rows(dividend_type, rows)
    fetched_at = datetime.now(timezone.utc).replace(tzinfo=None)
    if dividend_type == "none":
        values = [
            (
                row["stock_code"], row["trade_date"], row["open_price"],
                row["high_price"], row["low_price"], row["close_price"],
                row["volume"], row["amount"], row.get("pre_close"),
                row.get("suspend_flag"), row.get("data_source", "akshare"),
                *_daily_metadata(
                    row, adjustment_asofs.get(row["stock_code"]), fetched_at
                ),
            )
            for row in rows
        ]
    else:
        values = [
            (
                row["stock_code"], row["trade_date"], row["open_price"],
                row["high_price"], row["low_price"], row["close_price"],
                row["volume"], row["amount"], row.get("turnover_rate"),
                adjustment_asofs.get(row["stock_code"]),
                *_daily_metadata(
                    row, adjustment_asofs.get(row["stock_code"]), fetched_at
                ),
            )
            for row in rows
        ]
    affected = 0
    for offset in range(0, len(values), chunk_size):
        chunk_affected = execute_many(
            INSERT_SQL_BY_DIVIDEND_TYPE[dividend_type],
            values[offset:offset + chunk_size],
        )
        affected += chunk_affected or 0
    return affected
