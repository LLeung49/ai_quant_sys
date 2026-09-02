"""Daily/backfill runner for SHADOW Repair Alpha stock candidates.

Reads only the upstream sector_opportunity snapshots whose playbook is
``repair_probe`` or ``early_repair``.  All downstream rows are persisted
to ``research_candidate_snapshot`` with ``strategy_type='stock_repair'``.

CLI flags mirror the Phase 3 trend runner:
  --mode {live_shadow,delayed_shadow,backfill}
  --today <ISO date>     override LIVE_SHADOW today gate
  --dry-run              in-memory build, no persist
  --sector <NAME>        single-sector smoke test
  --workers N            thread-pool size
  --skip-migrations      debug only
  --allow-estimated-pit  include PIT_ESTIMATED rows (off by default)
  --force-replace        delete + rewrite stock_repair for the date

The Repair pipeline does not auto-provision the financial PIT tables
(schemas live in ``sql/20260820_create_repair_alpha_persistence_tables.sql``).
The runner assumes the operator has already applied that migration.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import replace
from datetime import date, datetime, timedelta
from typing import Any, Callable
from uuid import uuid4

from data_ingestion.db_config import execute_query, execute_update

from ...snapshot_store import create_run, mark_run_failed, mark_run_succeeded
from ..config_hash import build_config_hash
from ..availability import AvailabilityBasis, AvailabilityMetadata, as_shanghai_naive, resolve_availability
from ..calendar import TradingCalendar
from ..evaluation.prices import load_authoritative_market_calendar as load_trading_calendar
from ..orchestrator.store import MySQLSnapshotStore
from ..status import SnapshotMode
from ..financial.service import (
    RepairSectorContext,
    build_repair_candidate,
    load_repair_sectors,
    persist_repair_candidates,
    score_repair_sector,
)
from .config import TrendAlphaConfig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build SHADOW Repair Alpha stock candidates")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument(
        "--mode",
        choices=("live_shadow", "delayed_shadow", "backfill"),
        help="Override the snapshot mode.  LIVE_SHADOW requires today's date unless --today is supplied.",
    )
    parser.add_argument("--today", help="ISO date for the LIVE_SHADOW gate.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-migrations", action="store_true")
    parser.add_argument("--sector", help="Limit to one upstream sector name.")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--force-replace",
        action="store_true",
        help="Delete existing stock_repair snapshots for the target date and level before persisting.",
    )
    parser.add_argument(
        "--allow-estimated-pit",
        action="store_true",
        help="Include PIT_ESTIMATED rows.  Off by default (strict historical mode).",
    )
    return parser


def parse_today(value: str | None) -> date | None:
    if value is None:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        try:
            return datetime.fromisoformat(value).date()
        except ValueError as exc:
            raise SystemExit(f"invalid --today value: {value!r}") from exc


def resolve_mode(args: argparse.Namespace) -> SnapshotMode:
    if args.mode:
        return SnapshotMode(args.mode)
    if args.backfill_start:
        return SnapshotMode.BACKFILL
    return SnapshotMode.LIVE_SHADOW


def validate_mode_for_date(
    as_of_date: date, mode: SnapshotMode, *, today: date | None = None,
) -> None:
    if mode is SnapshotMode.LIVE_SHADOW and as_of_date != (today or date.today()):
        raise ValueError("non-today --as-of-date requires BACKFILL mode (use --mode backfill)")


def _backfill_dates(start_date: str, end_date: str, level: int, query: Callable = execute_query) -> list[str]:
    rows = query(
        """SELECT DISTINCT as_of_date FROM research_candidate_snapshot
             WHERE as_of_date BETWEEN %s AND %s AND sector_level=%s
               AND strategy_type='sector_opportunity'
             ORDER BY as_of_date""",
        (start_date, end_date, level),
    )
    return [str(row["as_of_date"]) for row in rows]


def _delayed_availability(target: date, level: int, run_at: datetime, query: Callable) -> AvailabilityMetadata:
    dates = load_trading_calendar(target, run_at.date() + timedelta(days=14), query, sector_level=level)
    return resolve_availability(target, AvailabilityBasis.MARKET_CLOSE_1800, TradingCalendar(dates), run_at)


def _delete_existing_repair_snapshots(
    as_of_date: str, level: int, mode: SnapshotMode, query=execute_query, update=execute_update,
) -> int:
    count_row = query(
        "SELECT COUNT(*) AS c FROM research_candidate_snapshot "
        "WHERE as_of_date=%s AND sector_level=%s AND strategy_type='stock_repair' AND snapshot_mode=%s",
        (as_of_date, level, mode.value),
    )
    deleted = int(count_row[0]["c"]) if count_row else 0
    if deleted == 0:
        return 0
    update(
        "DELETE FROM research_candidate_snapshot "
        "WHERE as_of_date=%s AND sector_level=%s AND strategy_type='stock_repair' AND snapshot_mode=%s",
        (as_of_date, level, mode.value),
    )
    return deleted


def run_one_date(
    as_of_date: str,
    level: int,
    mode: SnapshotMode,
    *,
    config: TrendAlphaConfig | None = None,
    today: date | None = None,
    query: Callable = execute_query,
    dry_run: bool = False,
    skip_migrations: bool = False,
    workers: int = 1,
    sector_filter: str | None = None,
    force_replace: bool = False,
    allow_estimated_pit: bool = False,
    now: datetime | None = None,
) -> int:
    """Build and persist Repair Alpha SHADOW candidates for ``as_of_date``."""

    target = date.fromisoformat(as_of_date)
    validate_mode_for_date(target, mode, today=today)
    config = config or TrendAlphaConfig()
    run_id = "dry-run" if dry_run else str(uuid4())
    store = None if dry_run else MySQLSnapshotStore()
    if store is not None:
        if force_replace:
            deleted = _delete_existing_repair_snapshots(as_of_date, level, mode)
            if deleted:
                print(f"{as_of_date}: --force-replace deleted {deleted} stock_repair rows")
        store.ensure_schema()
        create_run(
            run_id, as_of_date, level, config.model_version,
            build_config_hash({"model_version": config.model_version, "sector_level": level}), as_of_date,
        )
    try:
        sectors = load_repair_sectors(as_of_date, level, mode, query)
        if sector_filter:
            sectors = [s for s in sectors if str(s.get("sector_name")) == sector_filter]
        snapshots: list = []
        if workers <= 1:
            for sector in sectors:
                snapshots.extend(score_repair_sector(
                    sector, as_of_date=as_of_date, level=level, mode=mode,
                    config=config, run_id=run_id, store=None, query=query,
                    allow_estimated_pit=allow_estimated_pit,
                ))
        else:
            with ThreadPoolExecutor(max_workers=workers) as pool:
                futures = [
                    pool.submit(
                        score_repair_sector, sector,
                        as_of_date=as_of_date, level=level, mode=mode,
                        config=config, run_id=run_id, store=None, query=query,
                        allow_estimated_pit=allow_estimated_pit,
                    )
                    for sector in sectors
                ]
                for future in as_completed(futures):
                    snapshots.extend(future.result())
    except Exception as exc:
        if store is not None:
            mark_run_failed(run_id, str(exc))
        raise
    if snapshots and mode is SnapshotMode.DELAYED_SHADOW:
        availability = _delayed_availability(target, level, as_shanghai_naive(now), query)
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
    if store is not None:
        persist_repair_candidates(store, snapshots)
    if store is not None:
        mark_run_succeeded(run_id, len(snapshots), 0)
    persist_label = "dry-run" if dry_run else f"persisted {len(snapshots)}"
    print(f"{as_of_date}: {persist_label} {mode.value} repair candidates across {len(sectors)} sectors")
    return len(snapshots)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    today = parse_today(args.today)
    mode = resolve_mode(args)
    if args.as_of_date:
        run_one_date(
            args.as_of_date, args.level, mode, today=today,
            dry_run=args.dry_run, skip_migrations=args.skip_migrations,
            workers=args.workers, sector_filter=args.sector,
            force_replace=args.force_replace,
            allow_estimated_pit=args.allow_estimated_pit,
        )
        return 0
    if not args.backfill_end:
        raise SystemExit("--backfill-end is required with --backfill-start")
    for as_of_date in _backfill_dates(args.backfill_start, args.backfill_end, args.level):
        run_one_date(
            as_of_date, args.level, mode, today=today,
            dry_run=args.dry_run, skip_migrations=args.skip_migrations,
            workers=args.workers, sector_filter=args.sector,
            force_replace=args.force_replace,
            allow_estimated_pit=args.allow_estimated_pit,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
