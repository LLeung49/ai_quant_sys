import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import sys

from data_ingestion.db_config import execute_query


TRADE_DATES = [
    str(row["trade_date"])
    for row in execute_query(
        """
        SELECT DISTINCT trade_date FROM trade_stock_daily_qfq
        WHERE trade_date BETWEEN '2026-09-18' AND '2026-10-13'
        ORDER BY trade_date
        """
    )
]
COMPLETED_DATES = {
    str(row["as_of_date"])
    for row in execute_query(
        """
        SELECT as_of_date
        FROM sector_rotation_short_term_daily_snapshot
        WHERE as_of_date BETWEEN '2026-09-18' AND '2026-10-13'
          AND sector_level=1 AND model_version='v2_short_term'
        GROUP BY as_of_date HAVING COUNT(*)=30
        """
    )
}
DATES = [item for item in TRADE_DATES if item not in COMPLETED_DATES]
LOG_DIR = Path("reports/market-rebuild/short-term-level1-logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


def run_one(as_of_date: str) -> dict:
    command = [
        sys.executable,
        "-m", "morning_conference.sector_rotation2.short_term.run_daily",
        "--level", "1", "--as-of-date", as_of_date,
    ]
    env = dict(os.environ)
    env["PYTHONPATH"] = "src"
    completed = subprocess.run(
        command,
        cwd=Path.cwd(),
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    log_path = LOG_DIR / f"{as_of_date}.log"
    log_path.write_text(completed.stdout, encoding="utf-8")
    result = {"date": as_of_date, "returncode": completed.returncode, "log": str(log_path)}
    print(json.dumps(result, ensure_ascii=False), flush=True)
    return result


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(run_one, DATES))

report_path = Path("reports/market-rebuild/short-term-level1-backfill-20261016.json")
report = {
    "trade_dates": TRADE_DATES,
    "already_complete": sorted(COMPLETED_DATES),
    "requested_dates": DATES,
    "results": results,
}
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
if any(item["returncode"] for item in results):
    raise SystemExit(1)
