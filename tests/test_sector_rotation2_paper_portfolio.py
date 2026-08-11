from __future__ import annotations

import pandas as pd
import pytest


def _policy():
    from morning_conference.sector_rotation2.paper_portfolio import ResearchPolicy

    return ResearchPolicy(
        max_single_etf_weight=0.6,
        max_sector_weight=0.6,
        max_cluster_weight=0.8,
        max_turnover=1.0,
        min_average_turnover=1_000_000,
        cost_bps=10,
        rebalance_frequency=1,
    )


def test_build_targets_rejects_unvalidated_p1_intent():
    from morning_conference.sector_rotation2.paper_portfolio import build_etf_targets

    intent = pd.DataFrame([{"as_of_date": "2026-06-30", "sector_name": "A", "target_weight": 0.5, "source_label": "p1_unvalidated"}])
    mapping = pd.DataFrame([{"sector_name": "A", "etf_code": "510000.SH", "mapping_status": "expressible", "expression_rank": 1, "average_turnover_20d": 20_000_000}])

    targets, issues = build_etf_targets(intent, mapping, _policy())

    assert targets.empty
    assert issues.iloc[0]["reason"] == "unvalidated_signal_source"


def test_build_targets_records_unallocated_cash_for_unmapped_sector():
    from morning_conference.sector_rotation2.paper_portfolio import build_etf_targets

    intent = pd.DataFrame([{"as_of_date": "2026-06-30", "sector_name": "A", "target_weight": 0.5, "source_label": "manual_scenario"}])
    mapping = pd.DataFrame([{"sector_name": "A", "etf_code": None, "mapping_status": "no_qualified_etf", "expression_rank": None, "average_turnover_20d": None}])

    targets, issues = build_etf_targets(intent, mapping, _policy())

    assert targets.empty
    assert issues.iloc[0]["reason"] == "no_qualified_etf"
    assert issues.iloc[0]["unallocated_cash_weight"] == 0.5


def test_simulator_charges_turnover_cost_and_carries_cash():
    from morning_conference.sector_rotation2.paper_portfolio import simulate_paper_portfolio

    targets = pd.DataFrame([{"as_of_date": "2026-06-30", "sector_name": "A", "etf_code": "510000.SH", "target_weight": 0.6}])
    prices = pd.DataFrame([{"as_of_date": "2026-06-30", "etf_code": "510000.SH", "close": 10.0}])

    result = simulate_paper_portfolio(targets, prices, _policy())

    assert result["daily"].iloc[0]["transaction_cost"] > 0
    assert result["holdings"].iloc[0]["cash_weight"] == 0.4


def test_simulator_applies_next_day_etf_return_to_prior_holding():
    from morning_conference.sector_rotation2.paper_portfolio import simulate_paper_portfolio

    targets = pd.DataFrame([
        {"as_of_date": "2026-06-30", "sector_name": "A", "etf_code": "510000.SH", "target_weight": 0.6},
        {"as_of_date": "2026-07-01", "sector_name": "A", "etf_code": "510000.SH", "target_weight": 0.6},
    ])
    prices = pd.DataFrame([
        {"as_of_date": "2026-06-30", "etf_code": "510000.SH", "close": 10.0},
        {"as_of_date": "2026-07-01", "etf_code": "510000.SH", "close": 11.0},
    ])

    result = simulate_paper_portfolio(targets, prices, _policy())

    assert result["daily"].iloc[1]["gross_return"] == pytest.approx(0.06)
