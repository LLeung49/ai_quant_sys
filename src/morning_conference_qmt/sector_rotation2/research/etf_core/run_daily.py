"""Daily/backfill runner consuming only effective return-derived ETF maps."""

import argparse
from dataclasses import replace
from datetime import date, datetime, timedelta
from uuid import uuid4

from data_ingestion_qmt.db_config import execute_query

from ..orchestrator.store import MySQLSnapshotStore
from ..availability import AvailabilityBasis, AvailabilityMetadata, as_shanghai_naive, resolve_availability
from ..calendar import TradingCalendar
from ..evaluation.prices import load_authoritative_market_calendar as load_trading_calendar
from ..status import SnapshotMode
from .execution_evidence import load_etf_execution_evidence
from .macd_adapter import load_etf_macd_evidence
from .mapping import load_effective_return_etfs
from .service import build_etf_candidate, persist_etf_candidate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build ETF Core SHADOW candidates from exposure-derived mappings")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument("--today", help="ISO date to treat as today for LIVE_SHADOW validation")
    parser.add_argument(
        "--mode", choices=[mode.value for mode in (SnapshotMode.LIVE_SHADOW, SnapshotMode.DELAYED_SHADOW, SnapshotMode.BACKFILL)],
        help="Snapshot mode; delayed_shadow records next-day operational availability for historical closes.",
    )
    return parser


def validate_mode_for_date(as_of_date: date, mode: SnapshotMode, *, today: date | None = None) -> None:
    """Historical dates are reproducible BACKFILL runs, never live snapshots."""

    if mode is SnapshotMode.LIVE_SHADOW and as_of_date != (today or date.today()):
        raise ValueError("non-today --as-of-date requires BACKFILL mode")


def load_sector_rows(
    as_of_date: str,
    level: int,
    mode: SnapshotMode,
    query=execute_query,
) -> list[dict[str, object]]:
    """Return one canonical upstream sector snapshot per sector and its identity."""

    return query(
        """SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode
             FROM (
                SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode,
                       ROW_NUMBER() OVER (
                           PARTITION BY sector_name ORDER BY created_at DESC, id DESC
                       ) AS canonical_rank
                FROM research_candidate_snapshot
                WHERE as_of_date=%s AND sector_level=%s AND entity_type='sector'
                  AND strategy_type='sector_opportunity' AND snapshot_mode=%s
             ) AS canonical_sector_snapshot
             WHERE canonical_rank=1
             ORDER BY sector_name ASC""",
        (as_of_date, level, mode.value),
    )


def _backfill_dates(start_date: str, end_date: str, level: int) -> list[str]:
    rows = execute_query(
        """SELECT DISTINCT as_of_date FROM research_candidate_snapshot
             WHERE as_of_date BETWEEN %s AND %s AND sector_level=%s
               AND strategy_type='sector_opportunity' AND snapshot_mode=%s
             ORDER BY as_of_date""",
        (start_date, end_date, level, SnapshotMode.BACKFILL.value),
    )
    return [str(row["as_of_date"]) for row in rows]


def _delayed_availability(target: date, level: int, run_at: datetime, query=execute_query) -> AvailabilityMetadata:
    dates = load_trading_calendar(target, run_at.date() + timedelta(days=14), query, sector_level=level)
    return resolve_availability(target, AvailabilityBasis.MARKET_CLOSE_1800, TradingCalendar(dates), run_at)


def run_one_date(as_of_date: str, level: int, mode: SnapshotMode = SnapshotMode.LIVE_SHADOW, *, today: date | None = None, now: datetime | None = None) -> int:
    target = date.fromisoformat(as_of_date)
    validate_mode_for_date(target, mode, today=today)
    store = MySQLSnapshotStore()
    store.ensure_schema()
    run_id = str(uuid4())
    sectors = load_sector_rows(as_of_date, level, mode)
    snapshots = []
    for sector in sectors:
        allowed = sector["candidate_status"] not in {"avoid", "risk_reduce"}
        for mapping in load_effective_return_etfs(str(sector["sector_name"]), level, target):
            code = str(mapping["etf_code"])
            execution_evidence = load_etf_execution_evidence(code, target)
            snapshot = build_etf_candidate(
                as_of_date=target, sector_level=level, sector_name=str(sector["sector_name"]), etf_code=code,
                sector_allowed=allowed,
                liquid=execution_evidence.get("liquid") if execution_evidence else None,
                macd_evidence=load_etf_macd_evidence(code, target),
                extended=execution_evidence.get("extended") if execution_evidence else None,
                execution_evidence=execution_evidence,
                run_id=run_id, snapshot_mode=mode,
                mapping_metadata={
                    **mapping,
                    "upstream_sector_snapshot": {
                        "as_of_date": as_of_date,
                        "entity_type": "sector",
                        "entity_code": str(sector["sector_name"]),
                        "strategy_type": "sector_opportunity",
                        "model_version": sector.get("model_version"),
                        "config_hash": sector.get("config_hash"),
                        "snapshot_mode": sector.get("snapshot_mode"),
                    },
                },
            )
            snapshots.append(snapshot)
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
    for snapshot in snapshots:
        persist_etf_candidate(store, snapshot)
    count = len(snapshots)
    print(f"{as_of_date}: processed {count} {mode.value} ETF candidates")
    return count


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else None
    mode = SnapshotMode(args.mode) if args.mode else (SnapshotMode.BACKFILL if args.backfill_start else SnapshotMode.LIVE_SHADOW)
    if args.as_of_date:
        run_one_date(args.as_of_date, args.level, mode, today=today)
        return 0
    if not args.backfill_end:
        raise SystemExit("--backfill-end is required with --backfill-start")
    for as_of_date in _backfill_dates(args.backfill_start, args.backfill_end, args.level):
        run_one_date(as_of_date, args.level, mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

