import json
from pathlib import Path

from data_ingestion.db_config import execute_query


BATCH_ID = "market-full-qmt-20261014"
names = execute_query(
    """
    SELECT table_name AS name FROM information_schema.tables
    WHERE table_schema=DATABASE() AND table_name IN (
      'trade_stock_daily_raw', 'trade_stock_daily_qfq', 'trade_stock_daily_bfq',
      'trade_stock_daily_raw_rebuild', 'trade_stock_daily_qfq_rebuild',
      'trade_stock_daily_bfq_rebuild',
      'trade_stock_daily_raw_rollback_20261014',
      'trade_stock_daily_qfq_rollback_20261014',
      'trade_stock_daily_bfq_rollback_20261014'
    ) ORDER BY table_name
    """
)
tables = [row.get("name") or row.get("NAME") for row in names]
metrics = {}
for table in (
    "trade_stock_daily_raw", "trade_stock_daily_qfq", "trade_stock_daily_bfq"
):
    metrics[table] = execute_query(
        f"""
        SELECT COUNT(*) AS row_count, COUNT(DISTINCT stock_code) AS code_count,
               MIN(trade_date) AS first_date, MAX(trade_date) AS last_date,
               SUM(open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
                 AS zero_price_rows,
               SUM(rebuild_batch_id<>%s OR rebuild_batch_id IS NULL) AS foreign_rows
        FROM {table}
        """,
        (BATCH_ID,),
    )[0]

expected = {
    "trade_stock_daily_raw", "trade_stock_daily_qfq", "trade_stock_daily_bfq",
    "trade_stock_daily_raw_rollback_20261014",
    "trade_stock_daily_qfq_rollback_20261014",
    "trade_stock_daily_bfq_rollback_20261014",
}
if set(tables) != expected:
    raise RuntimeError(f"cutover table set is incomplete: {tables}")
for table, row in metrics.items():
    if int(row["zero_price_rows"] or 0) or int(row["foreign_rows"] or 0):
        raise RuntimeError(f"post-cutover integrity failure in {table}: {row}")

report = {
    "batch_id": BATCH_ID,
    "cutover": "complete",
    "tables": tables,
    "production_metrics": metrics,
    "rollback_procedure": "rollback_market_rebuild()",
}
Path("reports/market-rebuild/cutover-result-20261016.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
