"""Read-only acceptance checks for audited volume-unit correction."""

from data_ingestion.db_config import get_connection


run_id = "e2b0c8c9-ec41-4911-b343-3916a78430a7"
connection = get_connection()
cursor = connection.cursor()
try:
    cursor.execute(
        """SELECT table_name, COUNT(*) FROM trade_market_volume_repair_audit
             WHERE run_id=%s GROUP BY table_name ORDER BY table_name""",
        (run_id,),
    )
    print("[audit]", cursor.fetchall())
    for table_name in ("trade_stock_daily", "trade_stock_daily_qfq", "trade_stock_daily_bfq"):
        cursor.execute(
            f"""SELECT COUNT(*) FROM {table_name} AS fact
                 JOIN trade_market_volume_repair_audit AS audit
                   ON audit.table_name=%s AND audit.stock_code=fact.stock_code
                  AND audit.trade_date=fact.trade_date
                WHERE audit.run_id=%s AND fact.volume<>audit.normalized_volume""",
            (table_name, run_id),
        )
        print(f"[mismatch] {table_name}", cursor.fetchone()[0])
    for sector_name in ("煤炭开采", "白酒", "电池", "水泥"):
        cursor.execute(
            """SELECT trade_date, total_volume, total_amount
                 FROM trade_sector_daily
                WHERE sector_name=%s AND sector_level=2
                  AND trade_date IN ('2026-08-12','2026-08-13')
                ORDER BY trade_date""",
            (sector_name,),
        )
        print(f"[sector] {sector_name}", cursor.fetchall())
finally:
    cursor.close()
    connection.close()
