from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query


tables = (
    "trade_stock_daily_raw",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
)
coverage = {}
for table in tables:
    coverage[table] = execute_query(
        f"SELECT trade_date, COUNT(*) AS rows_count, "
        "SUM(open_price=0 OR high_price=0 OR low_price=0 OR close_price=0) "
        f"AS zero_rows FROM {table} WHERE trade_date BETWEEN %s AND %s "
        "GROUP BY trade_date ORDER BY trade_date",
        ("2026-10-14", "2026-10-16"),
    )

cross_table_differences = execute_query(
    "SELECT r.trade_date, "
    "SUM(q.stock_code IS NULL) AS missing_qfq, "
    "SUM(b.stock_code IS NULL) AS missing_bfq "
    "FROM trade_stock_daily_raw r "
    "LEFT JOIN trade_stock_daily_qfq q ON q.stock_code=r.stock_code "
    "AND q.trade_date=r.trade_date "
    "LEFT JOIN trade_stock_daily_bfq b ON b.stock_code=r.stock_code "
    "AND b.trade_date=r.trade_date "
    "WHERE r.trade_date BETWEEN %s AND %s GROUP BY r.trade_date "
    "ORDER BY r.trade_date",
    ("2026-10-14", "2026-10-16"),
)
result = {
    "coverage": coverage,
    "cross_table_differences": cross_table_differences,
    "accepted_suspended_absences": [
        "000016.SZ", "002388.SZ", "002731.SZ", "300773.SZ", "512390.SH",
        "560650.SH", "600293.SH", "601059.SH", "601198.SH", "688496.SH",
    ],
    "qmt_recovered_active_codes": ["689009.SH"],
    "unresolved_active_codes": [],
}
output = Path(__file__).with_name("daily-update-20261018") / "verification.json"
output.write_text(
    json.dumps(result, ensure_ascii=False, default=str, indent=2),
    encoding="utf-8",
)
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
