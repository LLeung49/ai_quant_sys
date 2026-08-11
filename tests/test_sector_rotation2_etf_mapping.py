from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.etf_mapping import (
    calculate_etf_expression_metrics,
    calculate_etf_overlap,
    evaluate_etf_expression,
    select_etf_mapping,
    shortlist_market_candidates,
    verify_etf_mapping,
)


def test_metrics_calculates_60d_correlation_and_beta_without_future_rows():
    dates = pd.bdate_range("2026-01-01", periods=62)
    sector_returns = pd.DataFrame({
        "as_of_date": dates,
        "sector_name": "A",
        "return": [index / 10_000 for index in range(62)],
    })
    etf_returns = pd.DataFrame({
        "as_of_date": dates,
        "etf_code": "510000.SH",
        "return": [index / 10_000 for index in range(61)] + [-0.9],
    })
    candidates = pd.DataFrame([{"sector_name": "A", "etf_code": "510000.SH"}])

    result = calculate_etf_expression_metrics(sector_returns, etf_returns, candidates, dates[60])

    assert result.loc[0, "return_correlation_60d"] == pytest.approx(1.0)
    assert result.loc[0, "beta_60d"] == pytest.approx(1.0)


def test_missing_required_metric_is_insufficient_data():
    result = evaluate_etf_expression(pd.DataFrame([{"sector_name": "A", "etf_code": "510000.SH"}]))

    assert result.loc[0, "expression_status"] == "insufficient_data"


def test_etf_mapping_marks_high_correlation_liquid_candidate_expressible():
    candidates = pd.DataFrame([{
        "sector_name": "A", "etf_code": "510000.SH", "return_correlation_60d": 0.92,
        "tracking_error_60d": 0.03, "average_turnover_20d": 20_000_000, "spread_bps": 3,
    }])

    result = evaluate_etf_expression(candidates)

    assert result.loc[0, "expression_status"] == "expressible"


def test_etf_mapping_ranks_expressible_candidate_before_unusable_one():
    candidates = pd.DataFrame([
        {"sector_name": "A", "etf_code": "510000.SH", "return_correlation_60d": 0.91, "tracking_error_60d": 0.04, "average_turnover_20d": 20_000_000, "spread_bps": 3},
        {"sector_name": "A", "etf_code": "510001.SH", "return_correlation_60d": 0.50, "tracking_error_60d": 0.15, "average_turnover_20d": 100_000, "spread_bps": 30},
    ])

    result = evaluate_etf_expression(candidates)

    assert result.sort_values("expression_rank").iloc[0]["etf_code"] == "510000.SH"


def test_select_mapping_adds_no_qualified_etf_for_unexpressible_sector():
    metrics = pd.DataFrame([
        {"sector_name": "A", "etf_code": "510000.SH", "expression_status": "expressible", "expression_rank": 1},
        {"sector_name": "B", "etf_code": "510001.SH", "expression_status": "not_recommended", "expression_rank": 1},
    ])

    mapping = select_etf_mapping(metrics, "2026-06-30")

    assert set(mapping.loc[mapping["sector_name"] == "B", "mapping_status"]) == {"no_qualified_etf"}
    assert mapping.loc[mapping["sector_name"] == "A", "mapping_status"].iloc[0] == "expressible"


def test_overlap_reports_pairwise_60d_return_correlation():
    dates = pd.bdate_range("2026-01-01", periods=60)
    returns = pd.DataFrame({
        "as_of_date": list(dates) * 2,
        "etf_code": ["510000.SH"] * 60 + ["510001.SH"] * 60,
        "return": list(range(60)) * 2,
    })

    overlap = calculate_etf_overlap(returns)

    assert overlap.loc[0, "return_correlation_60d"] == pytest.approx(1.0)
    assert {overlap.loc[0, "left_etf_code"], overlap.loc[0, "right_etf_code"]} == {"510000.SH", "510001.SH"}


def test_shortlist_keeps_three_best_expressible_candidates_per_sector():
    evaluated = pd.DataFrame([
        {"sector_name": "A", "etf_code": f"51000{i}.SH", "expression_status": "expressible", "expression_rank": i}
        for i in range(1, 5)
    ])

    result = shortlist_market_candidates(evaluated)

    assert result["etf_code"].tolist() == ["510001.SH", "510002.SH", "510003.SH"]
    assert set(result["mapping_status"]) == {"market_only"}


def test_verify_etf_mapping_requires_target_sector_exposure():
    shortlist = pd.DataFrame([
        {"sector_name": "A", "etf_code": "510001.SH"},
        {"sector_name": "A", "etf_code": "510002.SH"},
    ])
    exposure = pd.DataFrame([
        {"sector_name": "A", "etf_code": "510001.SH", "industry_exposure": 0.60},
        {"sector_name": "A", "etf_code": "510002.SH", "industry_exposure": 0.40},
    ])

    result = verify_etf_mapping(shortlist, exposure)

    assert result.set_index("etf_code").loc["510001.SH", "mapping_status"] == "verified"
    assert result.set_index("etf_code").loc["510002.SH", "mapping_status"] == "rejected"
