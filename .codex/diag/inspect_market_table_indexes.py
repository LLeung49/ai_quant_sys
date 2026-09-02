"""Read-only schema inspection for safe full-market volume-unit scanning."""

from data_ingestion.db_config import get_connection


connection = get_connection()
cursor = connection.cursor()
try:
    for table_name in (
        "trade_stock_daily",
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
    ):
        cursor.execute(f"SHOW INDEX FROM {table_name}")
        print(f"[{table_name}]")
        for row in cursor.fetchall():
            print(row)
finally:
    cursor.close()
    connection.close()
