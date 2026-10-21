import json

from data_ingestion.db_config import execute_query


parts = []
for mode, table in (
    ("raw", "trade_stock_daily_raw"),
    ("qfq", "trade_stock_daily_qfq"),
    ("bfq", "trade_stock_daily_bfq"),
):
    parts.append(
        f"""
        SELECT '{mode}' AS mode,
               MIN(trade_date) AS min_date,
               MAX(trade_date) AS max_date,
               COUNT(*) AS rows_count,
               SUM(CASE WHEN open_price <= 0 OR high_price <= 0
                             OR low_price <= 0 OR close_price <= 0
                        THEN 1 ELSE 0 END) AS bad
          FROM {table}
         WHERE stock_code = '560650.SH'
        """
    )

print(json.dumps(execute_query(" UNION ALL ".join(parts)), ensure_ascii=False, default=str, indent=2))
