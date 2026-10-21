import json

from data_ingestion.db_config import execute_query


batch_id = "market-full-qmt-20261014"
schema = execute_query("SHOW CREATE TABLE trade_market_rebuild_batch")[0]
missing_staging = execute_query(
    """SELECT
         COUNT(*) AS missing_codes,
         SUM(EXISTS(SELECT 1 FROM trade_stock_daily_raw_rebuild r
                    WHERE r.rebuild_batch_id=e.batch_id AND r.stock_code=e.stock_code)) AS raw_codes,
         SUM(EXISTS(SELECT 1 FROM trade_stock_daily_qfq_rebuild q
                    WHERE q.rebuild_batch_id=e.batch_id AND q.stock_code=e.stock_code)) AS qfq_codes,
         SUM(EXISTS(SELECT 1 FROM trade_stock_daily_bfq_rebuild h
                    WHERE h.rebuild_batch_id=e.batch_id AND h.stock_code=e.stock_code)) AS bfq_codes
       FROM trade_market_rebuild_expected_code e
       LEFT JOIN trade_market_rebuild_batch b
         ON b.batch_id=e.batch_id AND b.stock_code=e.stock_code
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
       WHERE e.batch_id=%s AND b.stock_code IS NULL AND x.stock_code IS NULL""",
    (batch_id,),
)[0]
other_status = execute_query(
    """SELECT b.batch_id, b.status, COUNT(*) AS row_count
       FROM trade_market_rebuild_batch b
       JOIN trade_market_rebuild_expected_code e ON e.stock_code=b.stock_code
       LEFT JOIN trade_market_rebuild_batch current
         ON current.batch_id=e.batch_id AND current.stock_code=e.stock_code
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
       WHERE e.batch_id=%s AND current.stock_code IS NULL AND x.stock_code IS NULL
       GROUP BY b.batch_id, b.status""",
    (batch_id,),
)
print(json.dumps({"schema": schema, "missing_staging": missing_staging, "other_status": other_status}, ensure_ascii=False, default=str, indent=2))
