from __future__ import annotations

from datetime import date
import json
from pathlib import Path

from data_ingestion.qmt_bootstrap_provider import QMTBootstrapProvider
from data_ingestion.price_projection_store import write_projection_batch


code = "689009.SH"
start_date = date(2026, 10, 14)
end_date = date(2026, 10, 16)
batch = QMTBootstrapProvider().fetch_batches([code], start_date, end_date)[code]
result = {
    "stock_code": code,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "complete": batch.is_complete,
    "failures": batch.failures,
    "rows": {mode: len(rows) for mode, rows in batch.rows_by_mode.items()},
    "zero_price_rows": sum(
        1
        for rows in batch.rows_by_mode.values()
        for row in rows
        if any(
            row[field] == 0
            for field in ("open_price", "high_price", "low_price", "close_price")
        )
    ),
}
if not batch.is_complete or result["zero_price_rows"]:
    raise RuntimeError(json.dumps(result, ensure_ascii=False, default=str))
result["written_rows"] = write_projection_batch(batch.rows_by_mode, end_date)
output = Path(__file__).with_name("daily-update-20261018") / "qmt-689009-recovery.json"
output.write_text(
    json.dumps(result, ensure_ascii=False, default=str, indent=2),
    encoding="utf-8",
)
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
