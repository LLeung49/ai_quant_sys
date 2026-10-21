import json
from datetime import date

from data_ingestion.akshare_market_provider import AKShareMarketProvider
from data_ingestion.db_config import execute_query
from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway


CODE = "158040.SZ"
BATCH_ID = "market-full-qmt-20261014"
summary = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.end_date, b.source, b.raw_rows,
           b.qfq_rows, b.hfq_rows,
           MIN(r.trade_date) AS actual_start, MAX(r.trade_date) AS actual_end,
           MIN(r.close_price) AS min_close, MAX(r.close_price) AS max_close
      FROM trade_market_rebuild_batch b
      JOIN trade_stock_daily_raw_rebuild r
        ON r.rebuild_batch_id=b.batch_id AND r.stock_code=b.stock_code
     WHERE b.batch_id=%s AND b.stock_code=%s
     GROUP BY b.stock_code, b.start_date, b.end_date, b.source, b.raw_rows,
              b.qfq_rows, b.hfq_rows
    """,
    (BATCH_ID, CODE),
)
detail = QMTDataGateway.from_env().get_instrument_detail([CODE], iscomplete=True)
batch = AKShareMarketProvider(max_attempts=2, request_timeout=20).fetch_batch(
    CODE, date(2026, 9, 1), date(2026, 10, 13)
)
print(json.dumps({
    "database": summary,
    "qmt_detail": detail,
    "akshare": {
        "rows": {mode: len(rows) for mode, rows in batch.rows_by_mode.items()},
        "failures": batch.failures,
        "interfaces": batch.provenance["interfaces"],
    },
}, ensure_ascii=False, default=str, indent=2))
