"""Incrementally collect implemented stock corporate actions from AKShare."""

from __future__ import annotations

import argparse
from datetime import date
import json
from typing import Callable, Sequence

import akshare as ak

from .db_config import execute_query
from .price_corporate_actions import (
    DATA_SOURCE,
    SnapshotPlan,
    persist_snapshot_plan,
    normalize_akshare_market_stock_actions,
    plan_incremental_snapshot,
)


STORED_ACTIONS_SQL = """
SELECT stock_code, ex_date, cash_dividend_per_share,
       stock_bonus_per_share, stock_gift_per_share,
       rights_issue_per_share, rights_issue_price, share_reform_flag,
       qmt_dr_factor, event_status, data_source, source_payload
FROM trade_corporate_action
WHERE data_source = 'akshare'
ORDER BY stock_code, ex_date
"""


def _report_periods(as_of_date: date) -> tuple[str, ...]:
    year = as_of_date.year
    return (
        f"{year - 1}1231",
        f"{year}0331",
        f"{year}0630",
        f"{year}0930",
    )


def collect_market_stock_events(
    as_of_date: date,
    *,
    fetch_market: Callable[..., object] = ak.stock_fhps_em,
) -> list[dict]:
    """Fetch recent report periods once each and return implemented events."""

    by_key: dict[tuple[str, str], dict] = {}
    for period in _report_periods(as_of_date):
        for event in normalize_akshare_market_stock_actions(fetch_market(date=period)):
            if date.fromisoformat(event["ex_date"]) > as_of_date:
                continue
            by_key[(event["stock_code"], event["ex_date"])] = event
    return sorted(by_key.values(), key=lambda item: (item["ex_date"], item["stock_code"]))


def load_stored_akshare_actions() -> list[dict]:
    return list(execute_query(STORED_ACTIONS_SQL))


def run_collection(
    *,
    as_of_date: date,
    data_start: date,
    dry_run: bool,
    bootstrap: bool = False,
    collect_events: Callable[[date], Sequence[dict]] = collect_market_stock_events,
    load_stored: Callable[[], Sequence[dict]] = load_stored_akshare_actions,
    persist: Callable = persist_snapshot_plan,
) -> dict[str, int | bool | str]:
    current = list(collect_events(as_of_date))
    stored = list(load_stored())
    plan = (
        SnapshotPlan([], current, [], [])
        if bootstrap
        else plan_incremental_snapshot(current, stored, data_start)
    )
    if not dry_run:
        persist(plan)
    return {
        "provider": DATA_SOURCE,
        "as_of_date": as_of_date.isoformat(),
        "events": len(current),
        "changes": len(plan.changes),
        "new": sum(change.kind == "new" for change in plan.changes),
        "corrected": sum(change.kind == "corrected" for change in plan.changes),
        "cancelled": len(plan.events_to_cancel),
        "refresh_tasks": len(plan.refresh_tasks),
        "dry_run": dry_run,
        "bootstrap": bootstrap,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--data-start", type=date.fromisoformat, default=date(2015, 1, 1))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--bootstrap",
        action="store_true",
        help="persist initial AKShare facts without queuing price refresh tasks",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_collection(
        as_of_date=args.as_of_date,
        data_start=args.data_start,
        dry_run=args.dry_run,
        bootstrap=args.bootstrap,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
