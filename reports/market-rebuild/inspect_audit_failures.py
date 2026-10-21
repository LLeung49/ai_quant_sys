import json

from data_ingestion.db_config import execute_query


BATCH_ID = "market-full-qmt-20261014"

zero_rows = execute_query(
    """
    SELECT 'raw' AS mode, stock_code, trade_date, open_price, high_price,
           low_price, close_price, rebuild_source
      FROM trade_stock_daily_raw_rebuild
     WHERE rebuild_batch_id=%s
       AND (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
    UNION ALL
    SELECT 'qfq', stock_code, trade_date, open_price, high_price,
           low_price, close_price, rebuild_source
      FROM trade_stock_daily_qfq_rebuild
     WHERE rebuild_batch_id=%s
       AND (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
    UNION ALL
    SELECT 'bfq', stock_code, trade_date, open_price, high_price,
           low_price, close_price, rebuild_source
      FROM trade_stock_daily_bfq_rebuild
     WHERE rebuild_batch_id=%s
       AND (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
    ORDER BY stock_code, trade_date, mode
    """,
    (BATCH_ID, BATCH_ID, BATCH_ID),
)

gaps = execute_query(
    """
    SELECT g.stock_code, g.price_mode, g.reason, g.first_trade_date,
           g.last_trade_date, g.gap_count, b.start_date, b.end_date
      FROM trade_market_rebuild_gap g
      JOIN trade_market_rebuild_batch b
        ON b.batch_id=g.batch_id AND b.stock_code=g.stock_code
      LEFT JOIN trade_market_rebuild_excluded_code x
        ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
     WHERE g.batch_id=%s AND b.status='complete' AND x.stock_code IS NULL
       AND NOT (g.reason='zero_price_fill'
                AND (g.last_trade_date < b.start_date
                     OR g.first_trade_date > b.end_date))
     ORDER BY g.gap_count DESC, g.stock_code, g.price_mode
    """,
    (BATCH_ID,),
)

report = {"zero_rows": zero_rows, "unresolved_gaps": gaps}
print(json.dumps(report, ensure_ascii=False, default=str, indent=2))
