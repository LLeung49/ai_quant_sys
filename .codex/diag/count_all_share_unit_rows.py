"""Read-only database-side count of all apparent share-unit daily rows."""

from data_ingestion.db_config import get_connection


connection = get_connection()
cursor = connection.cursor()
try:
    for table_name in (
        "trade_stock_daily",
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
    ):
        cursor.execute(
            f"""SELECT COUNT(*), COUNT(DISTINCT stock_code),
                       MIN(trade_date), MAX(trade_date)
                  FROM {table_name}
                 WHERE volume > 0 AND amount > 0 AND close_price > 0
                   AND amount / (volume * close_price) BETWEEN 0.5 AND 2"""
        )
        print(table_name, cursor.fetchone())
finally:
    cursor.close()
    connection.close()
