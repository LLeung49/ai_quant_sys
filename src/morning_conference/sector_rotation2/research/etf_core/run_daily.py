"""Daily/backfill runner consuming only effective exposure-derived ETF maps."""

import argparse
from datetime import date
from uuid import uuid4

from data_ingestion.db_config import execute_query

from ..orchestrator.store import MySQLSnapshotStore
from ..status import SnapshotMode
from .macd_adapter import load_etf_macd_evidence
from .mapping import load_effective_etfs
from .service import build_etf_candidate, persist_etf_candidate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build ETF Core SHADOW candidates from exposure-derived mappings")
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--as-of-date")
    date_group.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
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


def run_one_date(as_of_date: str, level: int, mode: SnapshotMode = SnapshotMode.LIVE_SHADOW) -> int:
    target = date.fromisoformat(as_of_date)
    validate_mode_for_date(target, mode)
    store = MySQLSnapshotStore()
    store.ensure_schema()
    run_id = str(uuid4())
    sectors = load_sector_rows(as_of_date, level, mode)
    count = 0
    for sector in sectors:
        allowed = sector["candidate_status"] not in {"avoid", "risk_reduce"}
        for mapping in load_effective_etfs(str(sector["sector_name"]), level, target):
            code = str(mapping["etf_code"])
            snapshot = build_etf_candidate(
                as_of_date=target, sector_level=level, sector_name=str(sector["sector_name"]), etf_code=code,
                sector_allowed=allowed, liquid=True, macd_evidence=load_etf_macd_evidence(code, target),
                extended=False, run_id=run_id, snapshot_mode=mode,
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
            persist_etf_candidate(store, snapshot)
            count += 1
    print(f"{as_of_date}: processed {count} {mode.value} ETF candidates")
    return count


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
