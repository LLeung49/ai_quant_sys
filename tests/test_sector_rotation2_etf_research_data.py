from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2 import etf_research_data
from morning_conference.sector_rotation2.etf_research_data import calculate_holdings_industry_exposure, load_current_stock_industries, load_qfq_etf_panel


def test_calculate_holdings_industry_exposure_reports_target_and_unmapped_weight():
    holdings = pd.DataFrame({
        "etf_code": ["512000.SH", "512000.SH"],
        "股票代码": ["600519", "000001"],
        "占净值比例": [15.0, 5.0],
        "季度": ["2026年1季度股票投资明细"] * 2,
    })
    industries = pd.DataFrame({"stock_code": ["600519"], "sector_2": ["白酒"]})

    result = calculate_holdings_industry_exposure(holdings, industries, level=2)

    assert result.loc[0, "industry_exposure"] == pytest.approx(0.75)
    assert result.loc[0, "unmapped_weight"] == pytest.approx(0.25)
    assert result.loc[0, "membership_asof_mode"] == "current_mapping"


def test_load_qfq_etf_panel_uses_qfq_table_and_cutoff(monkeypatch):
    captured: dict[str, object] = {}
    monkeypatch.setattr(etf_research_data, "execute_query", lambda sql, params: captured.update(sql=sql, params=params) or [])

    result = load_qfq_etf_panel(["512000.SH"], "2026-01-01", "2026-06-30")

    assert result.empty
    assert "trade_stock_daily_qfq" in str(captured["sql"])
    assert captured["params"][-1] == "2026-06-30"


def test_load_current_stock_industries_marks_current_mapping(monkeypatch):
    monkeypatch.setattr(etf_research_data, "execute_query", lambda *_: [{"stock_code": "600519", "sector_2": "白酒"}])

    result = load_current_stock_industries(["600519"], level=2)

    assert result.loc[0, "sector_2"] == "白酒"
    assert result.loc[0, "membership_asof_mode"] == "current_mapping"
