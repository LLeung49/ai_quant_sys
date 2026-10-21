"""Read-only check that scanner exports use bars from the labelled date."""

import csv
import json
from pathlib import Path

from data_ingestion.db_config import execute_query


root = Path(__file__).resolve().parents[3]
date = "2026-10-16"
out = {}
for name in (f"候选池_{date}.csv", f"MACD动能趋势股票池_{date}.csv"):
    with (root / "outputs" / name).open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    codes = sorted({row["代码"] for row in rows})
    latest = {}
    for offset in range(0, len(codes), 200):
        chunk = codes[offset:offset + 200]
        placeholders = ",".join(["%s"] * len(chunk))
        for row in execute_query(
            f"SELECT stock_code, MAX(trade_date) AS latest FROM trade_stock_daily_qfq WHERE stock_code IN ({placeholders}) GROUP BY stock_code",
            tuple(chunk),
        ):
            latest[row["stock_code"]] = str(row["latest"])
    stale = {code: latest.get(code) for code in codes if latest.get(code) != date}
    out[name] = {"rows": len(rows), "distinct_codes": len(codes), "stale_count": len(stale), "stale_examples": dict(list(stale.items())[:20])}
print(json.dumps(out, ensure_ascii=False, indent=2))
