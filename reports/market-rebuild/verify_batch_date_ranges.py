import json
from pathlib import Path

from data_ingestion.db_config import execute_query


BATCH_ID = "market-full-qmt-20261014"
TABLES = (
    "trade_stock_daily_raw_rebuild",
    "trade_stock_daily_qfq_rebuild",
    "trade_stock_daily_bfq_rebuild",
)

invalid_windows = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.end_date, b.status,
           (x.stock_code IS NOT NULL) AS excluded
    FROM trade_market_rebuild_batch b
    LEFT JOIN trade_market_rebuild_excluded_code x
      ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
    WHERE b.batch_id=%s AND b.start_date>b.end_date
    ORDER BY b.stock_code
    """,
    (BATCH_ID,),
)
outside = {}
for table in TABLES:
    outside[table] = execute_query(
        f"""
        SELECT COUNT(*) AS n
        FROM {table} s
        JOIN trade_market_rebuild_batch b
          ON b.batch_id=s.rebuild_batch_id AND b.stock_code=s.stock_code
        LEFT JOIN trade_market_rebuild_excluded_code x
          ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
        WHERE s.rebuild_batch_id=%s AND b.status='complete'
          AND x.stock_code IS NULL
          AND (s.trade_date < b.start_date OR s.trade_date > b.end_date)
        """,
        (BATCH_ID,),
    )[0]["n"]

result = {
    "batch_id": BATCH_ID,
    "invalid_windows": invalid_windows,
    "nonexcluded_rows_outside_batch_range": outside,
}
path = Path("reports/market-rebuild/date-range-verification-20261016.json")
path.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
