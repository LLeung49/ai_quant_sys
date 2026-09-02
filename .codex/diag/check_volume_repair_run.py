"""Read-only status check for a market-volume repair run id."""

import sys

from data_ingestion.db_config import get_connection


run_id = sys.argv[1]
connection = get_connection()
cursor = connection.cursor()
try:
    cursor.execute(
        """SELECT table_name, COUNT(*)
             FROM trade_market_volume_repair_audit
            WHERE run_id=%s GROUP BY table_name ORDER BY table_name""",
        (run_id,),
    )
    print("[audit_rows]", cursor.fetchall())
    cursor.execute(
        """SELECT audit.table_name, COUNT(*) AS mismatches
             FROM trade_market_volume_repair_audit AS audit
             LEFT JOIN trade_stock_daily AS legacy
               ON audit.table_name='trade_stock_daily'
              AND legacy.stock_code=audit.stock_code AND legacy.trade_date=audit.trade_date
             LEFT JOIN trade_stock_daily_qfq AS qfq
               ON audit.table_name='trade_stock_daily_qfq'
              AND qfq.stock_code=audit.stock_code AND qfq.trade_date=audit.trade_date
             LEFT JOIN trade_stock_daily_bfq AS bfq
               ON audit.table_name='trade_stock_daily_bfq'
              AND bfq.stock_code=audit.stock_code AND bfq.trade_date=audit.trade_date
            WHERE audit.run_id=%s
              AND COALESCE(legacy.volume, qfq.volume, bfq.volume) <> audit.normalized_volume
            GROUP BY audit.table_name""",
        (run_id,),
    )
    print("[audit_value_mismatches]", cursor.fetchall())
    cursor.execute(
        """SELECT COUNT(*) FROM trade_stock_daily AS legacy
             JOIN trade_stock_daily_raw AS raw
               ON raw.stock_code=legacy.stock_code AND raw.trade_date=legacy.trade_date
            WHERE legacy.trade_date='2026-08-12'
              AND legacy.volume / NULLIF(raw.volume, 0) BETWEEN 50 AND 150"""
    )
    print("[legacy_share_unit_stocks_0812]", cursor.fetchone()[0])
finally:
    cursor.close()
    connection.close()
