from __future__ import annotations

import pandas as pd


def test_runner_writes_paper_portfolio_outputs(tmp_path):
    from morning_conference.sector_rotation2.paper_portfolio import ResearchPolicy
    from morning_conference.sector_rotation2.run_paper_portfolio import run_paper_portfolio

    policy = ResearchPolicy(0.6, 0.6, 0.8, 1.0, 1_000_000, 10, 1)
    intent = pd.DataFrame([{"as_of_date": "2026-06-30", "sector_name": "A", "target_weight": 0.6, "source_label": "manual_scenario"}])
    mapping = pd.DataFrame([{"sector_name": "A", "etf_code": "510000.SH", "mapping_status": "expressible", "expression_rank": 1, "average_turnover_20d": 20_000_000}])
    prices = pd.DataFrame([{"as_of_date": "2026-06-30", "etf_code": "510000.SH", "close": 10.0}])
    industry_returns = pd.DataFrame([{"as_of_date": "2026-06-30", "sector_name": "A", "return": 0.0}])
    etf_returns = pd.DataFrame([{"as_of_date": "2026-06-30", "etf_code": "510000.SH", "return": 0.0}])

    run_paper_portfolio(intent, mapping, prices, industry_returns, etf_returns, policy, tmp_path)

    assert (tmp_path / "paper_portfolio_daily.csv").exists()
    assert (tmp_path / "paper_portfolio_attribution.csv").exists()
