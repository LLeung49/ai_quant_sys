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
