"""Publication gates must reject bad finance without inventing zero values."""

from datetime import date

import pytest

from data_ingestion.financial_recovery.publish_native_pit import prepare_candidate


def _candidate():
    return {"stock_code": "600000.SH", "report_date": "2015-03-31",
            "announcement_date": "2015-04-30", "source_hash": "a" * 64,
            "revenue": 0., "net_profit": -2., "total_assets": 200.,
            "total_equity": 80., "operating_cashflow": -5.,
            "eps": 1.2, "roe": -2000., "gross_margin": 31.,
            "metric_available_at": "2015-04-30", "lineage": {}}


def test_prepare_preserves_real_zero_and_negative_profit_but_quarantines_metric_outlier():
    result = prepare_candidate(_candidate(), as_of_date=date(2026, 10, 20))
    assert result["revenue"] == 0.
    assert result["net_profit"] == -2.
    assert result["operating_cash_flow"] == -5.
    assert result["roe"] is None
    assert result["eps"] == 1.2
    assert result["metric_quality_flags"] == ["roe_outlier"]


@pytest.mark.parametrize("change", [
    {"total_assets": 0},
    {"announcement_date": "2015-03-01"},
    {"announcement_date": "2026-10-21"},
    {"net_profit": None},
])
def test_prepare_rejects_invalid_core_or_dates(change):
    with pytest.raises(ValueError):
        prepare_candidate(dict(_candidate(), **change), as_of_date=date(2026, 10, 20))
