import json
from datetime import date
from pathlib import Path

from data_ingestion.qmt_bootstrap_provider import QMTBootstrapProvider


codes = ["511920.SH", "511930.SH", "511950.SH", "511970.SH"]
batches = QMTBootstrapProvider().fetch_batches(
    codes, date(2015, 1, 1), date(2026, 10, 13)
)
summary = {}
for code, batch in batches.items():
    summary[code] = {
        "complete": batch.is_complete,
        "failures": batch.failures,
        "rows": {mode: len(rows) for mode, rows in batch.rows_by_mode.items()},
        "zero_price_rows": sum(
            1
            for rows in batch.rows_by_mode.values()
            for row in rows
            if any(row[field] == 0 for field in ("open_price", "high_price", "low_price", "close_price"))
        ),
        "gap_count": len(batch.gaps),
    }
output = Path("reports/market-rebuild/four-volume-codes-verification-20261015.json")
output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False))
print(f"report={output.resolve()}")
