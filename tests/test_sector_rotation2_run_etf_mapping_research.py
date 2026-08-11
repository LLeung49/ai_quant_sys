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

    dates = pd.bdate_range("2026-01-01", periods=61)
    candidates = pd.DataFrame([{"sector_name": "白酒", "etf_code": "512000.SH", "average_turnover_20d": 20_000_000, "spread_bps": 3}])
    sector_returns = pd.DataFrame({"as_of_date": dates, "sector_name": "白酒", "return": range(61)})
    etf_returns = pd.DataFrame({"as_of_date": dates, "etf_code": "512000.SH", "return": range(61)})
    holdings = pd.DataFrame({"etf_code": ["512000.SH"], "股票代码": ["600519"], "占净值比例": [10.0], "季度": ["2026年1季度股票投资明细"]})
    industries = pd.DataFrame({"stock_code": ["600519"], "sector_2": ["白酒"]})

    result = run_etf_mapping_research(candidates, sector_returns, etf_returns, dates[-1], tmp_path, holdings, industries)

    assert (tmp_path / "etf_holdings_evidence.csv").exists()
    assert set(result["mapping"]["mapping_status"]) == {"verified"}


def test_source_backed_runner_caps_universe_before_market_research(monkeypatch, tmp_path):
    from morning_conference.sector_rotation2 import run_etf_mapping_research as module

    dates = pd.bdate_range("2026-01-01", periods=60)
    universe = pd.DataFrame({"代码": ["512000", "512001"], "名称": ["白酒ETF", "食品ETF"]})
    qfq = pd.DataFrame({
        "stock_code": ["512000.SH"] * 60 + ["512001.SH"] * 60,
        "trade_date": list(dates) * 2,
        "close_price": list(range(1, 61)) * 2,
        "amount": [20_000_000] * 60 + [1_000_000] * 60,
    })
    monkeypatch.setattr(module, "load_qfq_etf_panel", lambda *_: qfq)
    sectors = pd.DataFrame({"as_of_date": dates, "sector_name": "白酒", "return": range(60)})

    result = module.run_qfq_two_stage_etf_mapping_research(sectors, "2026-01-01", "2026-03-25", tmp_path, lambda: universe, lambda _: pd.DataFrame(), max_universe=1)

    assert result["universe"]["etf_code"].tolist() == ["512000.SH"]


def test_source_backed_runner_fetches_holdings_only_for_market_shortlist(monkeypatch, tmp_path):
    from morning_conference.sector_rotation2 import run_etf_mapping_research as module

    dates = pd.bdate_range("2026-01-01", periods=61)
    universe = pd.DataFrame({"代码": ["512000", "512001"], "名称": ["白酒ETF", "食品ETF"]})
    returns = [0.001 * (index + 1) for index in range(61)]
    prices = (100 * (1 + pd.Series(returns)).cumprod()).tolist()
    qfq = pd.DataFrame({"stock_code": ["512000.SH"] * 61 + ["512001.SH"] * 61, "trade_date": list(dates) * 2, "close_price": prices * 2, "amount": [20_000_000] * 61 + [1_000_000] * 61})
    monkeypatch.setattr(module, "load_qfq_etf_panel", lambda *_: qfq)
    monkeypatch.setattr(module, "load_current_stock_industries", lambda *_: pd.DataFrame({"stock_code": ["600519"], "sector_2": ["白酒"]}))
    called: list[str] = []
    def holdings(code: str) -> pd.DataFrame:
        called.append(code)
        return pd.DataFrame({"股票代码": ["600519"], "占净值比例": [10.0], "季度": ["2026年1季度股票投资明细"]})
    sectors = pd.DataFrame({"as_of_date": dates, "sector_name": "白酒", "return": returns})

    result = module.run_qfq_two_stage_etf_mapping_research(sectors, "2026-01-01", dates[-1].strftime("%Y-%m-%d"), tmp_path, lambda: universe, holdings, max_universe=1)

    assert called == ["512000"]
    assert set(result["mapping"]["mapping_status"]) == {"verified"}
