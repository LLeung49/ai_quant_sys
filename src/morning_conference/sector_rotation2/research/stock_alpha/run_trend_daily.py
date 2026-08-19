"""Daily/backfill runner for SHADOW Trend Alpha stock candidates.

CLI modes
=========

``--as-of-date <YYYY-MM-DD>``
    Default ``LIVE_SHADOW`` mode.  Allowed only when the date equals today;
    historical dates must use ``--mode backfill`` to avoid clobbering today's
    live snapshots.

``--as-of-date <YYYY-MM-DD> --mode backfill``
    Persist a reproducible ``BACKFILL`` snapshot for any historical date.

``--backfill-start <YYYY-MM-DD> [--backfill-end <YYYY-MM-DD>] [--mode ...]``
    Walk every available sector-opportunity BACKFILL date in the window and
    persist Trend Alpha BACKFILL snapshots for each.

The CLI is self-bootstrapping: ``ensure_research_schema()`` is invoked once
before running so that idempotent migrations for
``research_candidate_snapshot`` and ``trade_stock_status`` are applied
automatically (even in ``--dry-run`` mode).  Use ``--skip-migrations`` to
bypass the bootstrap in debug scenarios.

``--sector <NAME>`` filters the run to a single upstream sector-opportunity
sector name (the Chinese sector stored in ``trade_stock_status.sector_2``);
useful for fast smoke-testing one sector at a time.  ``--workers`` controls
the thread-pool size for per-sector processing (default 4).

``--force-replace`` deletes any existing ``stock_trend`` snapshots for the
target date before persisting.  Default is "fail on conflict" (immutable
behavior).  Use this flag only when you are certain the previous run is
stale (e.g. a config change or a JSON bug fix).
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from uuid import uuid4
from typing import Any, Callable

from data_ingestion.db_config import execute_query, execute_update

from ...snapshot_store import create_run, mark_run_failed, mark_run_succeeded
from ..config_hash import build_config_hash
from ..orchestrator.store import MySQLSnapshotStore
from ..status import SnapshotMode
from .common import (
    load_sector_close_series,
    load_stock_close_series,
    load_stock_universe,
)
from .config import TrendAlphaConfig
from .service import (
    SectorTrendContext,
    assemble_features_frame,
    build_trend_candidate,
    load_trend_follow_sectors,
    persist_trend_candidates,
    score_features_frame,
)
from .store import ensure_research_schema


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build SHADOW Trend Alpha stock candidates")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument(
        "--mode",
        choices=("live_shadow", "backfill"),
        help="Override the snapshot mode.  LIVE_SHADOW requires today's date unless --today is supplied.",
    )
    parser.add_argument(
        "--today",
        help="ISO date to treat as 'today' for the LIVE_SHADOW gate.  Useful for replaying yesterday's run.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build the candidate snapshot in memory and print a one-line summary; do not persist.",
    )
    parser.add_argument(
        "--skip-migrations",
        action="store_true",
        help="Skip the auto-bootstrap idempotent migrations (debug only).",
    )
    parser.add_argument(
        "--sector",
        help="Limit to one upstream sector name (matches feature_json playbook=trend_follow AND sector_name).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers for per-sector processing. 1 = serial.",
    )
    parser.add_argument(
        "--force-replace",
        action="store_true",
        help=(
            "Delete any existing stock_trend snapshots for the target date and "
            "level before persisting.  Required to re-run the same date after a "
            "code or config change; off by default to preserve immutability."
        ),
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
               AND strategy_type='sector_opportunity' AND snapshot_mode=%s
             ORDER BY as_of_date""",
        (start_date, end_date, level, SnapshotMode.BACKFILL.value),
    )
    return [str(row["as_of_date"]) for row in rows]


def _process_sector(
    sector: dict,
    *,
    as_of_date: str,
    level: int,
    mode: SnapshotMode,
    config: TrendAlphaConfig,
    run_id: str,
    store: Any,
    query: Callable,
) -> list:
    """Build and persist candidate snapshots for a single sector."""

    sector_name = str(sector["sector_name"])
    target = date.fromisoformat(as_of_date)
    universe = load_stock_universe(
        as_of_date=target,
        sector_names={sector_name},
        sector_level=level,
        config=config,
        query=query,
    )
    if not universe:
        return []
    sector_close_series = load_sector_close_series(
        {sector_name}, level, target, query,
    ).get(sector_name, {})
    stock_close_series = load_stock_close_series(
        [row.stock_code for row in universe], target, query,
    )
    feature_frame = assemble_features_frame(
        as_of_date=target,
        sector_level=level,
        sector_name=sector_name,
        universe=universe,
        sector_close_series=sector_close_series,
        stock_close_series=stock_close_series,
        config=config,
    )
    if feature_frame.empty:
        return []
    scored = score_features_frame(feature_frame, config=config)
    sector_ctx = SectorTrendContext(
        as_of_date=target,
        sector_level=level,
        sector_name=sector_name,
        model_version=str(sector.get("model_version") or config.model_version),
        config_hash=str(sector.get("config_hash") or ""),
        snapshot_mode=mode,
    )
    snapshots = [
        build_trend_candidate(
            row=row,
            sector_context=sector_ctx,
            config=config,
            run_id=run_id,
        )
        for _, row in scored.iterrows()
    ]
    if store is not None:
        persist_trend_candidates(store, snapshots)
    return snapshots


def _delete_existing_trend_snapshots(
    as_of_date: str, level: int, query=execute_query, update=execute_update,
) -> int:
    """Delete existing stock_trend snapshots for ``as_of_date``/``level``."""

    count_row = query(
        "SELECT COUNT(*) AS c FROM research_candidate_snapshot "
        "WHERE as_of_date=%s AND sector_level=%s AND strategy_type='stock_trend'",
        (as_of_date, level),
    )
    deleted = int(count_row[0]["c"]) if count_row else 0
    if deleted == 0:
        return 0
    update(
        "DELETE FROM research_candidate_snapshot "
        "WHERE as_of_date=%s AND sector_level=%s AND strategy_type='stock_trend'",
        (as_of_date, level),
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
) -> int:
    """Build and persist Trend Alpha SHADOW candidates for ``as_of_date``."""

    target = date.fromisoformat(as_of_date)
    validate_mode_for_date(target, mode, today=today)
    config = config or TrendAlphaConfig()
    if not skip_migrations:
        ensure_research_schema()
    run_id = "dry-run" if dry_run else str(uuid4())
    store = None if dry_run else MySQLSnapshotStore()
    if store is not None:
        if force_replace:
            deleted = _delete_existing_trend_snapshots(as_of_date, level)
            if deleted:
                print(f"{as_of_date}: --force-replace deleted {deleted} existing stock_trend rows")
        store.ensure_schema()
        create_run(
            run_id, as_of_date, level, config.model_version,
            build_config_hash({"model_version": config.model_version, "sector_level": level}), as_of_date,
        )
    try:
        sectors = load_trend_follow_sectors(as_of_date, level, mode, query)
        if sector_filter:
            sectors = [s for s in sectors if str(s.get("sector_name")) == sector_filter]
        snapshots: list = []
        if workers <= 1:
            for sector in sectors:
                snapshots.extend(_process_sector(
                    sector, as_of_date=as_of_date, level=level, mode=mode,
                    config=config, run_id=run_id, store=store, query=query,
                ))
        else:
            with ThreadPoolExecutor(max_workers=workers) as pool:
                futures = [
                    pool.submit(
                        _process_sector, sector,
                        as_of_date=as_of_date, level=level, mode=mode,
                        config=config, run_id=run_id, store=store, query=query,
                    )
                    for sector in sectors
                ]
                for future in as_completed(futures):
                    snapshots.extend(future.result())
    except Exception as exc:
        if store is not None:
            mark_run_failed(run_id, str(exc))
        raise
    if store is not None:
        mark_run_succeeded(run_id, len(snapshots), 0)
    persist_label = "dry-run" if dry_run else f"persisted {len(snapshots)}"
    print(f"{as_of_date}: {persist_label} {mode.value} trend candidates across {len(sectors)} sectors")
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
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
