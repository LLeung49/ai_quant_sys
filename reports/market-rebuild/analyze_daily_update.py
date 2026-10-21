from __future__ import annotations

import ast
from collections import Counter
import json
from pathlib import Path

from data_ingestion.db_config import execute_query


REPORT_DIR = Path(__file__).with_name("daily-update-20261018")
LOG_PATH = REPORT_DIR / "stdout.log"
OUTPUT_PATH = REPORT_DIR / "failure-analysis.json"


def category(failure: dict) -> str:
    detail = json.dumps(failure.get("details"), ensure_ascii=False)
    if "projection_volume_amount_mismatch" in detail:
        return "projection_mismatch"
    if "ProxyError" in detail or "RemoteDisconnected" in detail:
        return "transient_network"
    if "empty_response" in detail or "JSONDecodeError" in detail:
        return "empty_or_unsupported"
    return "other"


failures = []
for line in LOG_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
    if not line.startswith("[行情失败] "):
        continue
    failure = ast.literal_eval(line.split(" ", 1)[1])
    failure["category"] = category(failure)
    failures.append(failure)

tables = [
    "trade_stock_daily_raw",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
]
coverage = {}
for table in tables:
    coverage[table] = execute_query(
        f"""
        SELECT trade_date, COUNT(*) AS rows_count,
               SUM(open_price=0 OR high_price=0 OR low_price=0 OR close_price=0)
                   AS zero_rows
        FROM {table}
        WHERE trade_date BETWEEN %s AND %s
        GROUP BY trade_date ORDER BY trade_date
        """,
        ("2026-10-14", "2026-10-16"),
    )

failed_codes = [str(item["stock_code"]) for item in failures]
latest_by_code = {}
if failed_codes:
    placeholders = ",".join(["%s"] * len(failed_codes))
    for table in tables:
        rows = execute_query(
            f"SELECT stock_code, MAX(trade_date) AS latest FROM {table} "
            f"WHERE stock_code IN ({placeholders}) GROUP BY stock_code",
            tuple(failed_codes),
        )
        for row in rows:
            latest_by_code.setdefault(str(row["stock_code"]), {})[table] = row["latest"]

result = {
    "failure_count": len(failures),
    "category_counts": dict(Counter(item["category"] for item in failures)),
    "failed_codes": failed_codes,
    "failures": failures,
    "latest_by_failed_code": latest_by_code,
    "coverage": coverage,
}
OUTPUT_PATH.write_text(
    json.dumps(result, ensure_ascii=False, default=str, indent=2),
    encoding="utf-8",
)
print(json.dumps({
    "failure_count": result["failure_count"],
    "category_counts": result["category_counts"],
    "failed_codes": result["failed_codes"],
    "coverage": result["coverage"],
}, ensure_ascii=False, default=str, indent=2))
