"""Read-only check of sector-builder inputs after volume correction."""

from data_ingestion.db_config import get_connection


connection = get_connection()
cursor = connection.cursor()
try:
    cursor.execute("SELECT COUNT(*) FROM trade_stock_daily_qfq")
    print("[qfq_rows]", cursor.fetchone()[0])
    cursor.execute(
        """SELECT COUNT(*) FROM trade_stock_daily_qfq AS q
             JOIN trade_stock_status AS s ON s.stock_code=q.stock_code
            WHERE s.sector_1=%s""",
        ("交通运输",),
    )
    print("[transport_qfq_rows]", cursor.fetchone()[0])
    cursor.execute(
        "SELECT COUNT(*) FROM trade_stock_status WHERE sector_1=%s",
        ("交通运输",),
    )
    print("[transport_members]", cursor.fetchone()[0])
finally:
    cursor.close()
    connection.close()
