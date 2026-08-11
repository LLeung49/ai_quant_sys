from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.etf_mapping import calculate_etf_expression_metrics, evaluate_etf_expression


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
