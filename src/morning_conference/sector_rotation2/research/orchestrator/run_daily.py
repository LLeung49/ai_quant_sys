"""Daily/backfill entry point for immutable Sector Opportunity snapshots."""

import argparse
from datetime import date
from uuid import uuid4

from data_ingestion.db_config import execute_query

from ..status import SnapshotMode
from .service import build_sector_opportunity_snapshots
from .store import MySQLSnapshotStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build SHADOW Sector Opportunity snapshots")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    return parser


def load_v1_rows(as_of_date: str, level: int) -> list[dict[str, object]]:
    return execute_query(
        """SELECT sector_name, score_eligible, lifecycle_state, phase_confirmed, phase_confidence,
                  participation_score, rank_change_5d, composite_score
             FROM sector_rotation_sector_daily_snapshot
             WHERE as_of_date=%s AND sector_level=%s AND model_version='v1'""",
        (as_of_date, level),
    )


def load_v2_rows(as_of_date: str, level: int) -> list[dict[str, object]]:
    return execute_query(
        """SELECT sector_name, short_term_labels
             FROM sector_rotation_short_term_daily_snapshot
             WHERE as_of_date=%s AND sector_level=%s AND model_version='v2_short_term'""",
        (as_of_date, level),
    )


def _backfill_dates(start_date: str, end_date: str, level: int) -> list[str]:
    rows = execute_query(
        """SELECT DISTINCT as_of_date FROM sector_rotation_sector_daily_snapshot
             WHERE as_of_date BETWEEN %s AND %s AND sector_level=%s AND model_version='v1'
             ORDER BY as_of_date""",
        (start_date, end_date, level),
    )
    return [str(row["as_of_date"]) for row in rows]


def run_one_date(as_of_date: str, level: int, mode: SnapshotMode) -> int:
    store = MySQLSnapshotStore()
    store.ensure_schema()
    snapshots = build_sector_opportunity_snapshots(
        store, load_v1_rows(as_of_date, level), load_v2_rows(as_of_date, level),
        date.fromisoformat(as_of_date), level, str(uuid4()), snapshot_mode=mode,
    )
    return len(snapshots)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.as_of_date:
        run_one_date(args.as_of_date, args.level, SnapshotMode.LIVE_SHADOW)
        return 0
    if not args.backfill_end:
        raise SystemExit("--backfill-end is required with --backfill-start")
    for as_of_date in _backfill_dates(args.backfill_start, args.backfill_end, args.level):
        run_one_date(as_of_date, args.level, SnapshotMode.BACKFILL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
