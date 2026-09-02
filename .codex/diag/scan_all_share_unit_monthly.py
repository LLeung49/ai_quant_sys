"""Read-only, index-range monthly scan for residual share-unit rows."""

from datetime import date

from data_ingestion.db_config import get_connection


TABLES = (
    ("trade_stock_daily", "idx_stock_daily_date"),
    ("trade_stock_daily_qfq", "idx_qfq_trade_date"),
    ("trade_stock_daily_bfq", "idx_bfq_trade_date"),
)


def next_month(value: date) -> date:
    return date(value.year + (value.month == 12), value.month % 12 + 1, 1)


connection = get_connection()
cursor = connection.cursor()
try:
    for table_name, index_name in TABLES:
        current = date(2015, 1, 1)
        total = 0
        while current <= date(2026, 8, 31):
            end = next_month(current)
            cursor.execute(
                f"""SELECT COUNT(*), COUNT(DISTINCT stock_code)
                    FROM {table_name} FORCE INDEX ({index_name})
                   WHERE trade_date >= %s AND trade_date < %s
                     AND volume > 0 AND amount > 0 AND close_price > 0
                     AND amount / (volume * close_price) BETWEEN 0.5 AND 2""",
                (current, end),
            )
            rows, codes = cursor.fetchone()
            if rows:
                print(f"[share-unit] table={table_name} month={current:%Y-%m} rows={rows} codes={codes}", flush=True)
                total += rows
            current = end
        print(f"[share-unit-total] table={table_name} rows={total}", flush=True)
finally:
    cursor.close()
    connection.close()
