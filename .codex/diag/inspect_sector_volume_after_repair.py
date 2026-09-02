"""Read-only component inspection for a remaining sector-volume break."""

from data_ingestion.db_config import get_connection


connection = get_connection()
cursor = connection.cursor()
try:
    cursor.execute(
        """SELECT q.stock_code, s.stock_name,
                      MAX(CASE WHEN q.trade_date='2026-08-12' THEN q.volume END) AS volume_0812,
                      MAX(CASE WHEN q.trade_date='2026-08-13' THEN q.volume END) AS volume_0813,
                      MAX(CASE WHEN q.trade_date='2026-08-12' THEN q.amount/(q.volume*q.close_price) END) AS ratio_0812,
                      MAX(CASE WHEN q.trade_date='2026-08-13' THEN q.amount/(q.volume*q.close_price) END) AS ratio_0813
                 FROM trade_stock_daily_qfq AS q
                 JOIN trade_stock_status AS s ON s.stock_code=q.stock_code
                WHERE s.sector_2=%s AND q.trade_date IN ('2026-08-12','2026-08-13')
                GROUP BY q.stock_code, s.stock_name
                ORDER BY volume_0812 DESC""",
        ("白酒",),
    )
    for row in cursor.fetchall():
        print(row)
finally:
    cursor.close()
    connection.close()
