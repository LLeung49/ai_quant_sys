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

result = {
    "status": execute_query(
        f"SELECT * FROM trade_stock_status WHERE stock_code IN ({placeholders}) "
        "ORDER BY stock_code",
        tuple(codes),
    ),
    "expected": execute_query(
        f"SELECT * FROM trade_market_rebuild_expected_code "
        f"WHERE stock_code IN ({placeholders}) ORDER BY stock_code",
        tuple(codes),
    ),
}
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
