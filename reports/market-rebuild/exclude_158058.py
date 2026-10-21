from data_ingestion.db_config import execute_query
from data_ingestion.market_rebuild_store import RebuildStore


BATCH_ID = "market-full-qmt-20261014"
STOCK_CODE = "158058.SZ"


before = execute_query(
    """
    SELECT b.stock_code, b.start_date, b.end_date, b.status,
      (SELECT COUNT(*) FROM trade_stock_daily_raw_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS raw_rows,
      (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS qfq_rows,
      (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS hfq_rows
    FROM trade_market_rebuild_batch b
    WHERE b.batch_id=%s AND b.stock_code=%s
    """,
    (BATCH_ID, STOCK_CODE),
)
if len(before) != 1:
    raise RuntimeError(f"expected one batch row, found {len(before)}")
row = before[0]
if str(row["start_date"]) != "2026-10-14" or str(row["end_date"]) != "2026-10-13":
    raise RuntimeError(f"unexpected date evidence: {row}")

RebuildStore(batch_id=BATCH_ID).replace_with_exclusion(
    STOCK_CODE,
    reason="listed_after_rebuild_end",
    evidence={
        "open_date": "2026-10-14",
        "rebuild_end_date": "2026-10-13",
        "qmt_actual_range": "2015-01-05..2026-10-13",
        "qmt_constant_close": 1.004,
        "qmt_rows_per_projection": 2859,
        "akshare_rows_through_rebuild_end": 0,
        "diagnostic": "reports/market-rebuild/inspect_158058.py",
    },
)

after = execute_query(
    """
    SELECT b.status, b.raw_rows, b.qfq_rows, b.hfq_rows, x.reason,
      JSON_LENGTH(x.evidence) AS evidence_fields,
      (SELECT COUNT(*) FROM trade_stock_daily_raw_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS raw_rows_actual,
      (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS qfq_rows_actual,
      (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild s
       WHERE s.rebuild_batch_id=b.batch_id AND s.stock_code=b.stock_code) AS hfq_rows_actual
    FROM trade_market_rebuild_batch b
    JOIN trade_market_rebuild_excluded_code x
      ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
    WHERE b.batch_id=%s AND b.stock_code=%s
    """,
    (BATCH_ID, STOCK_CODE),
)
print({"before": before, "after": after})
