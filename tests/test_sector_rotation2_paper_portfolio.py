from __future__ import annotations

import pandas as pd


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
