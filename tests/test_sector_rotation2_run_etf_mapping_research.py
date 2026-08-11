from __future__ import annotations

import pandas as pd


def test_run_etf_mapping_research_writes_metrics_mapping_overlap_and_report(tmp_path):
    from morning_conference.sector_rotation2.run_etf_mapping_research import run_etf_mapping_research

    dates = pd.bdate_range("2026-01-01", periods=60)
    candidates = pd.DataFrame([{"sector_name": "A", "etf_code": "510000.SH", "average_turnover_20d": 20_000_000, "spread_bps": 3}])
    sector_returns = pd.DataFrame({"as_of_date": dates, "sector_name": "A", "return": range(60)})
    etf_returns = pd.DataFrame({"as_of_date": dates, "etf_code": "510000.SH", "return": range(60)})

    run_etf_mapping_research(candidates, sector_returns, etf_returns, dates[-1], tmp_path)

    assert (tmp_path / "etf_mapping_metrics.csv").exists()
    assert (tmp_path / "etf_mapping_snapshot.csv").exists()
    assert (tmp_path / "etf_mapping_overlap.csv").exists()
    assert "mapping_as_of_date" in (tmp_path / "etf_mapping_report.md").read_text(encoding="utf-8")


def test_runner_writes_holdings_evidence_and_only_verifies_with_exposure(tmp_path):
    from morning_conference.sector_rotation2.run_etf_mapping_research import run_etf_mapping_research

    dates = pd.bdate_range("2026-01-01", periods=60)
    candidates = pd.DataFrame([{"sector_name": "白酒", "etf_code": "512000.SH", "average_turnover_20d": 20_000_000, "spread_bps": 3}])
    sector_returns = pd.DataFrame({"as_of_date": dates, "sector_name": "白酒", "return": range(60)})
    etf_returns = pd.DataFrame({"as_of_date": dates, "etf_code": "512000.SH", "return": range(60)})
    holdings = pd.DataFrame({"etf_code": ["512000.SH"], "股票代码": ["600519"], "占净值比例": [10.0], "季度": ["2026年1季度股票投资明细"]})
    industries = pd.DataFrame({"stock_code": ["600519"], "sector_2": ["白酒"]})

    result = run_etf_mapping_research(candidates, sector_returns, etf_returns, dates[-1], tmp_path, holdings, industries)

    assert (tmp_path / "etf_holdings_evidence.csv").exists()
    assert set(result["mapping"]["mapping_status"]) == {"verified"}
