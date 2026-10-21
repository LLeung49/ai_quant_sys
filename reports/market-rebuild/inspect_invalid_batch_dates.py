from data_ingestion.db_config import execute_query
from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway


BATCH_ID = "market-full-qmt-20261014"
CODES = ["158040.SZ", "688001.SH", "688031.SH", "688981.SH", "600519.SH"]

details = QMTDataGateway.from_env().get_instrument_detail(CODES, iscomplete=True)
rows = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.end_date, b.status,
           MIN(s.trade_date) AS actual_start, MAX(s.trade_date) AS actual_end,
           COUNT(*) AS actual_rows
    FROM trade_market_rebuild_batch b
    LEFT JOIN trade_stock_daily_raw_rebuild s
      ON s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code
    WHERE b.batch_id=%s AND b.stock_code IN (%s, %s, %s, %s, %s)
    GROUP BY b.stock_code, b.start_date, b.end_date, b.status
    ORDER BY b.stock_code
    """,
    (BATCH_ID, *CODES),
)
for code in CODES:
    detail = details.get(code) or {}
    print(code, {key: detail.get(key) for key in ("OpenDate", "ExpireDate", "TradingDay", "InstrumentName")})
print(rows)
