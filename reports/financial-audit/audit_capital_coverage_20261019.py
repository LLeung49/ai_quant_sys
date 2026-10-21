import json

from data_ingestion.db_config import execute_query


rows = execute_query(
    """SELECT data_source, COUNT(*) AS rows_count,
              COUNT(DISTINCT stock_code) AS code_count,
              MIN(report_date) AS first_date, MAX(report_date) AS last_date
         FROM trade_stock_capital_pit
        GROUP BY data_source ORDER BY data_source"""
)
print(json.dumps(rows, ensure_ascii=False, default=str, indent=2))
