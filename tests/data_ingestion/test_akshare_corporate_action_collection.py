from datetime import date
from decimal import Decimal

import pandas as pd

from data_ingestion.akshare_corporate_action_collection import (
    collect_market_stock_events,
    run_collection,
)


def test_market_collection_fetches_recent_report_periods_and_filters_future_events():
    calls = []

    def fetch_market(*, date):
        calls.append(date)
        return pd.DataFrame([{
            "代码": "600519",
            "除权除息日": (
                date_value := (
                    __import__("datetime").date(2026, 6, 26)
                    if date == "20251231"
                    else __import__("datetime").date(2026, 12, 1)
                )
            ),
            "现金分红-现金分红比例": Decimal("10"),
            "送转股份-送转比例": None,
            "送转股份-转股比例": None,
            "方案进度": "实施分配",
        }])

    events = collect_market_stock_events(
        as_of_date=date(2026, 10, 19), fetch_market=fetch_market
    )

    assert calls == ["20251231", "20260331", "20260630", "20260930"]
    assert len(events) == 1
    assert events[0]["ex_date"] == "2026-06-26"


def test_collection_builds_incremental_plan_without_cancelling_history():
    current = {
        "stock_code": "600519.SH",
        "ex_date": "2026-06-26",
        "cash_dividend_per_share": "1.00000000",
        "stock_bonus_per_share": "0.00000000",
        "stock_gift_per_share": "0.00000000",
        "rights_issue_per_share": "0.00000000",
        "rights_issue_price": None,
        "share_reform_flag": 0,
        "qmt_dr_factor": None,
        "event_status": "effective",
        "data_source": "akshare",
        "source_payload": {},
    }
    older = {**current, "ex_date": date(2025, 6, 27)}
    persisted = []

    result = run_collection(
        as_of_date=date(2026, 10, 19),
        data_start=date(2015, 1, 1),
        dry_run=False,
        collect_events=lambda _as_of: [current],
        load_stored=lambda: [older],
        persist=lambda plan: persisted.append(plan),
    )

    assert result["events"] == 1
    assert result["changes"] == 1
    assert result["cancelled"] == 0
    assert len(persisted) == 1
    assert persisted[0].events_to_cancel == []


def test_bootstrap_persists_facts_without_enqueuing_projection_refreshes():
    current = {
        "stock_code": "600519.SH",
        "ex_date": "2026-06-26",
        "cash_dividend_per_share": "28.02423000",
        "stock_bonus_per_share": "0.00000000",
        "stock_gift_per_share": "0.00000000",
        "rights_issue_per_share": "0.00000000",
        "rights_issue_price": None,
        "share_reform_flag": 0,
        "qmt_dr_factor": None,
        "event_status": "effective",
        "data_source": "akshare",
        "source_payload": {},
    }
    persisted = []

    result = run_collection(
        as_of_date=date(2026, 10, 19),
        data_start=date(2015, 1, 1),
        dry_run=False,
        bootstrap=True,
        collect_events=lambda _as_of: [current],
        load_stored=lambda: [],
        persist=lambda plan: persisted.append(plan),
    )

    assert result["events"] == 1
    assert result["refresh_tasks"] == 0
    assert persisted[0].events_to_upsert == [current]
    assert persisted[0].changes == []
