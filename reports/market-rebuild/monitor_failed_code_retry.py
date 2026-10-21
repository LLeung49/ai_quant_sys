from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query


report = json.loads(
    Path(__file__).with_name("daily-update-20261018")
    .joinpath("failure-analysis.json")
    .read_text(encoding="utf-8")
)
codes = report["failed_codes"]
placeholders = ",".join(["%s"] * len(codes))
tables = (
    "trade_stock_daily_raw",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
)
result = {}
for table in tables:
    rows = execute_query(
        f"SELECT stock_code, MAX(trade_date) AS latest FROM {table} "
        f"WHERE stock_code IN ({placeholders}) GROUP BY stock_code",
        tuple(codes),
    )
    latest = {str(row["stock_code"]): str(row["latest"]) for row in rows}
    result[table] = {
        "latest_2026_10_16": sum(value == "2026-10-16" for value in latest.values()),
        "still_before_2026_10_14": sorted(
            code for code in codes if latest.get(code, "") < "2026-10-14"
        ),
    }
print(json.dumps(result, ensure_ascii=False, indent=2))
