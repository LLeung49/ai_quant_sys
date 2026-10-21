import json
from datetime import datetime, timezone
from pathlib import Path

from data_ingestion.market_rebuild_store import RebuildStore


BATCH_ID = "market-full-qmt-20261014"
source = Path("reports/market-rebuild/remaining-failure-evidence-20261015.json")
report = json.loads(source.read_text(encoding="utf-8"))
zero_only = set(report["old_zero_only_codes"])
records = {row["stock_code"]: row for row in report["records"]}
reviewed_at = datetime.now(timezone.utc).isoformat()
exclusions = {
    code: {
        "reason": "invalid_legacy_zero_only_code",
        "evidence": {
            "reviewed_at": reviewed_at,
            "old_table": records[code]["old_table"],
            "qmt_failure": "all three projections contain only zero-price fill rows",
            "instrument_detail": records[code]["instrument_detail"],
            "source_report": str(source),
        },
    }
    for code in sorted(zero_only)
}
RebuildStore(batch_id=BATCH_ID).record_exclusions(exclusions)
print(json.dumps({"batch_id": BATCH_ID, "recorded_exclusions": len(exclusions)}, ensure_ascii=False))
