import json

from data_ingestion.db_config import execute_query


batch_id = "market-full-qmt-20261014"
row_estimate = execute_query(
    """SELECT
         SUM((SELECT COUNT(*) FROM trade_stock_daily_raw r WHERE r.stock_code=e.stock_code)) raw_rows,
         SUM((SELECT COUNT(*) FROM trade_stock_daily_qfq q WHERE q.stock_code=e.stock_code)) qfq_rows,
         SUM((SELECT COUNT(*) FROM trade_stock_daily_bfq h WHERE h.stock_code=e.stock_code)) bfq_rows
       FROM trade_market_rebuild_expected_code e
       LEFT JOIN trade_market_rebuild_batch b
         ON b.batch_id=e.batch_id AND b.stock_code=e.stock_code
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
       WHERE e.batch_id=%s AND b.stock_code IS NULL AND x.stock_code IS NULL""",
    (batch_id,),
)[0]
sizes = execute_query(
    """SELECT table_name, table_rows, data_length, index_length
       FROM information_schema.tables
       WHERE table_schema=DATABASE() AND table_name IN
         ('trade_stock_daily_raw_rebuild','trade_stock_daily_qfq_rebuild','trade_stock_daily_bfq_rebuild')"""
)
print(json.dumps({"production_row_estimate": row_estimate, "staging_sizes": sizes}, default=str, indent=2))
