"""Daily/backfill entry point for immutable Sector Opportunity snapshots."""

import argparse
from dataclasses import replace
from datetime import date, datetime, timedelta
from uuid import uuid4

from data_ingestion_qmt.db_config import execute_query

from ...snapshot_store import create_run, mark_run_failed, mark_run_succeeded
from ..config_hash import build_config_hash
from ..availability import AvailabilityBasis, AvailabilityMetadata, as_shanghai_naive, resolve_availability
from ..calendar import TradingCalendar
from ..evaluation.prices import load_authoritative_market_calendar as load_trading_calendar
from ..status import SnapshotMode
from .service import build_sector_opportunity_snapshots
from .store import MySQLSnapshotStore, persist_sector_opportunity


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build SHADOW Sector Opportunity snapshots")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument(
        "--mode", choices=("live_shadow", "delayed_shadow", "backfill"),
        help="Snapshot mode; delayed_shadow creates same-mode roots for next-day child runs.",
    )
    parser.add_argument("--today", help="ISO date to treat as today for LIVE_SHADOW validation")
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


def _delayed_availability(target: date, level: int, run_at: datetime) -> AvailabilityMetadata:
    dates = load_trading_calendar(target, run_at.date() + timedelta(days=14), execute_query, sector_level=level)
    return resolve_availability(target, AvailabilityBasis.MARKET_CLOSE_1800, TradingCalendar(dates), run_at)


def validate_mode_for_date(as_of_date: date, mode: SnapshotMode, *, today: date | None = None) -> None:
    """Prevent historical root snapshots from being labelled as live runs."""

    if mode is SnapshotMode.LIVE_SHADOW and as_of_date != (today or date.today()):
        raise ValueError("non-today --as-of-date requires BACKFILL mode")


def run_one_date(as_of_date: str, level: int, mode: SnapshotMode, *, today: date | None = None, now: datetime | None = None) -> int:
    target = date.fromisoformat(as_of_date)
    validate_mode_for_date(target, mode, today=today)
    store = MySQLSnapshotStore()
    store.ensure_schema()
    run_id = str(uuid4())
    model_version = "sector_opportunity_v1"
    create_run(
        run_id, as_of_date, level, model_version,
        build_config_hash({"model_version": model_version, "sector_level": level}), as_of_date,
    )
    try:
        v1_rows = load_v1_rows(as_of_date, level)
        v2_rows = load_v2_rows(as_of_date, level)
        snapshots = build_sector_opportunity_snapshots(
            store, v1_rows, v2_rows, target, level, run_id,
            model_version=model_version, snapshot_mode=mode, persist=False,
        )
        if snapshots and mode is SnapshotMode.DELAYED_SHADOW:
            availability = _delayed_availability(target, level, as_shanghai_naive(now))
            snapshots = [
                replace(
                    snapshot,
                    data_available_at=availability.data_available_at,
                    run_at=availability.run_at,
                    execution_eligible_at=availability.execution_eligible_at,
                    availability_basis=availability.availability_basis,
                )
                for snapshot in snapshots
            ]
        snapshots = [persist_sector_opportunity(store, snapshot) for snapshot in snapshots]
    except Exception as exc:
        mark_run_failed(run_id, str(exc))
        raise
    mark_run_succeeded(run_id, len(snapshots), len(v1_rows) - len(snapshots))
    return len(snapshots)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else None
    mode = SnapshotMode(args.mode) if args.mode else (SnapshotMode.BACKFILL if args.backfill_start else SnapshotMode.LIVE_SHADOW)
    if args.as_of_date:
        count = run_one_date(args.as_of_date, args.level, mode, today=today)
        print(f"{args.as_of_date}: persisted {count} {mode.value} sector opportunities")
        return 0
    if not args.backfill_end:
        raise SystemExit("--backfill-end is required with --backfill-start")
    for as_of_date in _backfill_dates(args.backfill_start, args.backfill_end, args.level):
        count = run_one_date(as_of_date, args.level, mode, today=today)
        print(f"{as_of_date}: persisted {count} {mode.value} sector opportunities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

