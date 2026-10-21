import json

from data_ingestion.db_config import execute_query


batch_id = "market-full-qmt-20261014"
status = execute_query(
    """SELECT status, COUNT(*) AS row_count
       FROM trade_market_rebuild_batch
       WHERE batch_id=%s
       GROUP BY status""",
    (batch_id,),
)
excluded = execute_query(
    """SELECT reason, COUNT(*) AS row_count
       FROM trade_market_rebuild_excluded_code
       WHERE batch_id=%s
       GROUP BY reason""",
    (batch_id,),
)
unresolved = execute_query(
    """SELECT b.stock_code, b.error_detail
       FROM trade_market_rebuild_batch b
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
       WHERE b.batch_id=%s AND b.status<>'complete' AND x.stock_code IS NULL
       ORDER BY b.stock_code""",
    (batch_id,),
)
manifest = execute_query(
    """SELECT COUNT(*) AS expected_count
       FROM trade_market_rebuild_expected_code
       WHERE batch_id=%s""",
    (batch_id,),
)[0]
missing = execute_query(
    """SELECT e.stock_code
       FROM trade_market_rebuild_expected_code e
       LEFT JOIN trade_market_rebuild_batch b
         ON b.batch_id=e.batch_id AND b.stock_code=e.stock_code
       LEFT JOIN trade_market_rebuild_excluded_code x
         ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
       WHERE e.batch_id=%s AND b.stock_code IS NULL AND x.stock_code IS NULL
       ORDER BY e.stock_code""",
    (batch_id,),
)
result = {
    "batch_id": batch_id,
    "expected_count": manifest["expected_count"],
    "status": status,
    "excluded": excluded,
    "unresolved_count": len(unresolved),
    "unresolved_codes": [row["stock_code"] for row in unresolved],
    "missing_state_count": len(missing),
    "missing_state_sample": [row["stock_code"] for row in missing[:30]],
}
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
