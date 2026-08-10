from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.etf_mapping import evaluate_etf_expression


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
