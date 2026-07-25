"""Fixed SQL storage for the independent raw and adjusted daily-price tables.

This module deliberately knows only the three derived-price tables.  It never
writes the legacy ``trade_stock_daily`` table, which keeps the new collection
path safe to run beside the existing collector.
"""

from datetime import date

try:  # Package import for tests and application modules.
    from .db_config import execute_many, execute_query
except ImportError:  # Direct ``python 8-...py`` execution.
    from db_config import execute_many, execute_query


TABLE_BY_DIVIDEND_TYPE = {
    "none": "trade_stock_daily_raw",
    "front": "trade_stock_daily_qfq",
    "back": "trade_stock_daily_bfq",
}

RAW_INSERT_SQL = """
INSERT INTO trade_stock_daily_raw
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, pre_close, suspend_flag)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    pre_close = VALUES(pre_close), suspend_flag = VALUES(suspend_flag),
    updated_at = CURRENT_TIMESTAMP
"""

QFQ_INSERT_SQL = """
INSERT INTO trade_stock_daily_qfq
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate, adjustment_asof)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    turnover_rate = VALUES(turnover_rate),
    adjustment_asof = VALUES(adjustment_asof), refreshed_at = CURRENT_TIMESTAMP
"""

BFQ_INSERT_SQL = """
INSERT INTO trade_stock_daily_bfq
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate, adjustment_asof)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    open_price = VALUES(open_price), high_price = VALUES(high_price),
    low_price = VALUES(low_price), close_price = VALUES(close_price),
    volume = VALUES(volume), amount = VALUES(amount),
    turnover_rate = VALUES(turnover_rate),
    adjustment_asof = VALUES(adjustment_asof), refreshed_at = CURRENT_TIMESTAMP
"""

INSERT_SQL_BY_DIVIDEND_TYPE = {
    "none": RAW_INSERT_SQL,
    "front": QFQ_INSERT_SQL,
    "back": BFQ_INSERT_SQL,
}

LATEST_DATE_SQL_BY_DIVIDEND_TYPE = {
    "none": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_raw GROUP BY stock_code",
    "front": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_qfq GROUP BY stock_code",
    "back": "SELECT stock_code, MAX(trade_date) AS max_date FROM trade_stock_daily_bfq GROUP BY stock_code",
}


def table_for_mode(dividend_type: str) -> str:
    """Return the fixed destination table for a QMT dividend type."""
    try:
        return TABLE_BY_DIVIDEND_TYPE[dividend_type]
    except KeyError as exc:
        raise ValueError(f"Unsupported dividend type: {dividend_type}") from exc


def get_existing_latest_dates(dividend_type: str) -> dict[str, str]:
    """Return each code's latest saved date for one independent price mode."""
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
    """Upsert rows for exactly one price mode using its fixed SQL statement."""
    if not rows:
        return 0
    table_for_mode(dividend_type)
    if dividend_type == "none":
        values = [
            (
                row["stock_code"], row["trade_date"], row["open_price"],
                row["high_price"], row["low_price"], row["close_price"],
                row["volume"], row["amount"], row.get("pre_close"),
                row.get("suspend_flag"),
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
            )
            for row in rows
        ]
    return execute_many(INSERT_SQL_BY_DIVIDEND_TYPE[dividend_type], values)
