from __future__ import annotations

import pandas as pd
import pytest


def test_attribution_reconciles_sector_expression_and_cost_to_net_return():
    from morning_conference.sector_rotation2.attribution import attribute_paper_portfolio

    simulation = {
        "daily": pd.DataFrame([{"as_of_date": "2026-07-01", "net_return": 0.071, "transaction_cost": 0.001}]),
        "holdings": pd.DataFrame([{"as_of_date": "2026-07-01", "sector_name": "A", "etf_code": "510000.SH", "weight": 0.6, "cash_weight": 0.4}]),
    }
    industry_returns = pd.DataFrame([{"as_of_date": "2026-07-01", "sector_name": "A", "return": 0.10}])
    etf_returns = pd.DataFrame([{"as_of_date": "2026-07-01", "etf_code": "510000.SH", "return": 0.12}])

    result = attribute_paper_portfolio(simulation, industry_returns, etf_returns)

    assert result.iloc[0]["sector_selection_return"] == pytest.approx(0.06)
    assert result.iloc[0]["etf_expression_return"] == pytest.approx(0.012)
    assert result.iloc[0]["reconciliation_error"] == pytest.approx(0.0)
