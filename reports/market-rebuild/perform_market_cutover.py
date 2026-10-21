import json
from pathlib import Path

import pymysql

from data_ingestion.db_config import get_connection


BATCH_ID = "market-full-qmt-20261014"
AUDIT_PATH = Path("reports/market-rebuild/full-audit-20261015.json")
COMPARISON_PATH = Path("reports/market-rebuild/source-comparison-20261015.json")
SQL_PATH = Path("sql/20261014_market_rebuild_cutover.sql")
OUTPUT_PATH = Path("reports/market-rebuild/cutover-result-20261016.json")

audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
comparison = json.loads(COMPARISON_PATH.read_text(encoding="utf-8"))
if not audit.get("can_cutover") or audit.get("hard_failures"):
    raise RuntimeError(f"full audit does not permit cutover: {audit}")
combined = comparison.get("combined_assessment", {})
if not combined.get("can_cutover") or combined.get("hard_failures"):
    raise RuntimeError(f"source comparison does not permit cutover: {combined}")

sql_text = "\n".join(
    line for line in SQL_PATH.read_text(encoding="utf-8").splitlines()
    if not line.strip().upper().startswith("DELIMITER")
)
statements = [part.strip() for part in sql_text.split("$$") if part.strip()]

conn = get_connection()
cursor = conn.cursor(pymysql.cursors.DictCursor)
try:
    for statement in statements:
        cursor.execute(statement)
    cursor.execute("CALL cutover_market_rebuild(%s)", (BATCH_ID,))
    while cursor.nextset():
        pass

    cursor.execute(
        """
        SELECT table_name FROM information_schema.tables
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
    tables = [
        row.get("table_name") or row.get("TABLE_NAME")
        for row in cursor.fetchall()
    ]
    table_metrics = {}
    for table in (
        "trade_stock_daily_raw",
        "trade_stock_daily_qfq",
        "trade_stock_daily_bfq",
    ):
        cursor.execute(
            f"""
            SELECT COUNT(*) AS row_count, COUNT(DISTINCT stock_code) AS code_count,
                   MIN(trade_date) AS first_date, MAX(trade_date) AS last_date,
                   SUM(open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
                     AS zero_price_rows,
                   SUM(rebuild_batch_id<>%s OR rebuild_batch_id IS NULL) AS foreign_rows
            FROM {table}
            """,
            (BATCH_ID,),
        )
        table_metrics[table] = cursor.fetchone()
finally:
    cursor.close()
    conn.close()

expected_tables = {
    "trade_stock_daily_raw", "trade_stock_daily_qfq", "trade_stock_daily_bfq",
    "trade_stock_daily_raw_rollback_20261014",
    "trade_stock_daily_qfq_rollback_20261014",
    "trade_stock_daily_bfq_rollback_20261014",
}
if set(tables) != expected_tables:
    raise RuntimeError(f"unexpected post-cutover table set: {tables}")
for table, metrics in table_metrics.items():
    if int(metrics["zero_price_rows"] or 0) or int(metrics["foreign_rows"] or 0):
        raise RuntimeError(f"post-cutover integrity failure in {table}: {metrics}")

report = {
    "batch_id": BATCH_ID,
    "cutover": "complete",
    "tables": tables,
    "production_metrics": table_metrics,
    "rollback_procedure": "rollback_market_rebuild()",
}
OUTPUT_PATH.write_text(
    json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
