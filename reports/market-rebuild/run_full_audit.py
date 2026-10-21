import json
from dataclasses import asdict
from pathlib import Path

from data_ingestion.market_rebuild_audit import audit_rebuild


BATCH_ID = "market-full-qmt-20261014"
output = Path("reports/market-rebuild/full-audit-20261015.json")
report = asdict(audit_rebuild(BATCH_ID))
output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
