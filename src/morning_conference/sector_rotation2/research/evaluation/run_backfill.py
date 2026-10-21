"""Run real forward-label backfill against immutable research snapshots.

This command is deliberately explicit about snapshot mode.  It creates only
evaluation tables/rows and never updates ``research_candidate_snapshot``.
"""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from uuid import uuid4

from data_ingestion.db_config import execute_query, get_connection

from ..contracts import CandidateSnapshot, ResearchContext
from ..orchestrator.store import _snapshot_from_row
from ..status import SnapshotMode
from .calendar import TradingCalendar
from .config import DEFAULT_EVALUATION_CONFIG
from .prices import MySQLPriceBarProvider, load_authoritative_market_calendar
from .service import backfill_forward_labels
from .store import ensure_evaluation_tables, persist_forward_labels


class CachingProvider(MySQLPriceBarProvider):
    """Cache each entity's requested date range during a single run."""

    def __init__(self, query, start_date: date, end_date: date) -> None:
        super().__init__(query)
        self._start_date = start_date
        self._end_date = end_date
        self._cache: dict[tuple[str, str], dict] = {}

    def load_bars(self, entity_type: str, entity_code: str, start_date: date, end_date: date):
        key = (entity_type, entity_code)
        if key not in self._cache:
            self._cache[key] = dict(super().load_bars(entity_type, entity_code, self._start_date, self._end_date))
        return {day: bar for day, bar in self._cache[key].items() if start_date <= day <= end_date}


def run(
    *, snapshot_mode: SnapshotMode, start_date: date, end_date: date, sector_level: int,
    strategy_type: str | None = None, calendar_end_date: date | None = None,
) -> dict[str, object]:
    query = (
        "SELECT * FROM research_candidate_snapshot WHERE snapshot_mode=%s AND sector_level=%s "
        "AND as_of_date BETWEEN %s AND %s "
        "AND NOT (strategy_type='stock_repair' AND validation_status='rejected') "
    )
    params: tuple[object, ...] = (snapshot_mode.value, sector_level, start_date, end_date)
    if strategy_type is not None:
        query += "AND strategy_type=%s "
        params += (strategy_type,)
    rows = execute_query(query + "ORDER BY as_of_date, id", params)
    snapshots: list[CandidateSnapshot] = []
    for row in rows:
        for field in ("feature_json", "reasons_json", "risk_flags_json"):
            if isinstance(row.get(field), str):
                row[field] = json.loads(row[field])
        snapshots.append(_snapshot_from_row(row))
    if not snapshots:
        return {"snapshot_mode": snapshot_mode.value, "snapshot_count": 0, "label_count": 0}

    calendar_end = _calendar_end_date(snapshots, end_date)
    if calendar_end_date is not None:
        if calendar_end_date < end_date:
            raise ValueError("calendar_end_date cannot precede end_date")
        calendar_end = calendar_end_date
    calendar_dates = load_authoritative_market_calendar(start_date, calendar_end, execute_query, sector_level=sector_level)
    if not calendar_dates:
        raise RuntimeError("authoritative market calendar returned no dates")
    calendar = TradingCalendar(calendar_dates)
    provider = CachingProvider(execute_query, start_date, calendar_end)
    context = ResearchContext(
        as_of_date=max(snapshot.as_of_date for snapshot in snapshots),
        sector_level=sector_level,
        model_version="evaluation_forward_label_v1",
        config_hash="evaluation-forward-label-v1",
        run_id=f"forward-backfill-{snapshot_mode.value}-{uuid4().hex[:12]}",
    )
    labels = backfill_forward_labels(
        snapshots=snapshots, calendar=calendar, provider=provider, context=context,
        horizons=DEFAULT_EVALUATION_CONFIG.horizons,
    )
    connection = get_connection()
    try:
        ensure_evaluation_tables(connection)
        affected = persist_forward_labels(connection, labels, context)
    finally:
        connection.close()
    counts: dict[str, int] = {}
    for label in labels:
        counts[label.return_status.value] = counts.get(label.return_status.value, 0) + 1
    return {
        "snapshot_mode": snapshot_mode.value, "snapshot_count": len(snapshots), "label_count": len(labels),
        "affected_rows": affected, "calendar_start": calendar_dates[0].isoformat(),
        "calendar_end": calendar_dates[-1].isoformat(), "status_counts": counts, "run_id": context.run_id,
    }


def _calendar_end_date(snapshots: list[CandidateSnapshot], requested_end: date) -> date:
    """Include delayed execution and the longest configured daily-bar horizon."""
    latest_input = max(
        [requested_end, *(snapshot.as_of_date for snapshot in snapshots), *(
            snapshot.run_at.date() for snapshot in snapshots
            if snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW and snapshot.run_at is not None
        )],
    )
    max_horizon = max(horizon for horizons in DEFAULT_EVALUATION_CONFIG.horizons.values() for horizon in horizons)
    # Three calendar days per trading day covers weekends and the longest
    # mainland-market holiday while still retaining a deterministic query bound.
    return latest_input + timedelta(days=max_horizon * 3 + 14)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-mode", choices=[mode.value for mode in SnapshotMode if mode in (SnapshotMode.BACKFILL, SnapshotMode.LIVE_SHADOW, SnapshotMode.DELAYED_SHADOW)], required=True)
    parser.add_argument("--start-date", required=True, type=date.fromisoformat)
    parser.add_argument("--end-date", required=True, type=date.fromisoformat)
    parser.add_argument("--sector-level", type=int, default=2)
    parser.add_argument("--strategy-type")
    parser.add_argument("--calendar-end-date", type=date.fromisoformat)
    args = parser.parse_args()
    print(json.dumps(run(
        snapshot_mode=SnapshotMode(args.snapshot_mode), start_date=args.start_date,
        end_date=args.end_date, sector_level=args.sector_level,
        strategy_type=args.strategy_type, calendar_end_date=args.calendar_end_date,
    ), ensure_ascii=False, default=str, indent=2))


if __name__ == "__main__":
    main()
