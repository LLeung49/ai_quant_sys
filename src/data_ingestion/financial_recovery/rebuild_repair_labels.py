"""Rebuild forward labels for corrected Repair Alpha backfill snapshots by month."""

from __future__ import annotations

import argparse
from calendar import monthrange
from datetime import date, timedelta
import json
from pathlib import Path

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.research.evaluation.run_backfill import run
from morning_conference.sector_rotation2.research.status import SnapshotMode


LEDGER = Path("reports/financial-audit/repair-label-rebuild-20261020.jsonl")
START = date(2024, 2, 1)
END = date(2026, 9, 17)
CALENDAR_LIMIT = date(2026, 10, 19)


def completed_months() -> set[str]:
    if not LEDGER.exists():
        return set()
    return {
        row["month"] for line in LEDGER.read_text(encoding="utf-8").splitlines()
        if (row := json.loads(line)).get("status") == "succeeded"
    }


def months():
    year, month = START.year, START.month
    while (year, month) <= (END.year, END.month):
        first = max(START, date(year, month, 1))
        last = min(END, date(year, month, monthrange(year, month)[1]))
        yield f"{year:04d}-{month:02d}", first, last
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)


def completed_calendar_end(target: date) -> date:
    rows = execute_query(
        "SELECT MAX(trade_date) AS last_date FROM trade_sector_daily "
        "WHERE sector_level=2 AND trade_date<=%s", (target,),
    )
    last_date = rows[0]["last_date"] if rows else None
    if last_date is None:
        raise RuntimeError(f"no completed sector calendar through {target}")
    return last_date


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-month", default="2024-02")
    parser.add_argument("--end-month", default="2026-09")
    args = parser.parse_args()
    if args.start_month > args.end_month:
        raise ValueError("start-month must not exceed end-month")
    done = completed_months()
    for month, first, last in months():
        if month in done or not args.start_month <= month <= args.end_month:
            continue
        try:
            result = run(
                snapshot_mode=SnapshotMode.BACKFILL,
                start_date=first, end_date=last, sector_level=2,
                strategy_type="stock_repair",
                calendar_end_date=completed_calendar_end(min(last + timedelta(days=134), CALENDAR_LIMIT)),
            )
            entry = {"month": month, "status": "succeeded", **result}
        except Exception as exc:
            entry = {"month": month, "status": "failed", "error": f"{type(exc).__name__}: {exc}"}
        with LEDGER.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")
        print(json.dumps(entry, ensure_ascii=False, default=str), flush=True)
        if entry["status"] == "failed":
            raise RuntimeError(f"label recovery failed in {month}: {entry['error']}")


if __name__ == "__main__":
    main()
