"""Capital uses both change and announcement dates for visibility."""

from datetime import date

import pytest

from data_ingestion.financial_recovery.publish_native_capital import prepare_capital


def _row():
    return {"stock_code": "600000.SH", "report_date": "2015-06-30",
            "announcement_date": "2015-05-01", "first_usable_date": "2015-06-30",
            "total_shares": 1000., "circulating_shares": 800.,
            "source_hash": "a" * 64}


def test_capital_preserves_advance_announcement_but_waits_for_change_date():
    prepared = prepare_capital(_row(), as_of_date=date(2026, 10, 20))
    assert prepared["announcement_date"] == "2015-05-01"
    assert prepared["first_usable_date"] == "2015-06-30"


def test_zero_circulating_shares_are_missing_not_a_real_zero():
    prepared = prepare_capital(dict(_row(), circulating_shares=0.),
                               as_of_date=date(2026, 10, 20))
    assert prepared["total_shares"] == 1000.
    assert prepared["circulating_shares"] is None


@pytest.mark.parametrize("change", [
    {"total_shares": 0.},
    {"circulating_shares": 1200.},
    {"circulating_shares": -1.},
    {"first_usable_date": "2015-05-01"},
])
def test_invalid_capital_rejected(change):
    with pytest.raises(ValueError):
        prepare_capital(dict(_row(), **change), as_of_date=date(2026, 10, 20))
