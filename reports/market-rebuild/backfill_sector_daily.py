import json
import sys
from pathlib import Path


module_dir = Path("src/morning_conference/sector_rotation").resolve()
sys.path.insert(0, str(module_dir))
from sector_index_builder import rebuild_all_sectors  # noqa: E402


START_DATE = "20260918"
results = {
    str(level): rebuild_all_sectors(
        level=level, full=True, start_date=START_DATE
    )
    for level in (2, 1)
}
report = {"start_date": START_DATE, "rows_written": results}
Path("reports/market-rebuild/sector-backfill-20261016.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False, indent=2))
