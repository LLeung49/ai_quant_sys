import math
from datetime import date

import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.etf_core.return_exposure import (
    assess_return_exposure,
)


def _close_from_returns(returns):
    values = [100.0]
    for value in returns:
        values.append(values[-1] * (1.0 + value))
    return pd.Series(values)


def test_assess_return_exposure_returns_qualified_regression_result():
    sector_returns = [0.01 if i % 2 == 0 else -0.005 for i in range(60)]
    sector = _close_from_returns(sector_returns)
    etf = _close_from_returns([2.0 * value for value in sector_returns])

    results, failures = assess_return_exposure({"510300.SH": etf}, sector)

    assert failures == []
    result = results[0]
    assert result.etf_code == "510300.SH"
    assert result.beta == pytest.approx(2.0)
    assert result.corr == pytest.approx(1.0)
    assert result.r_squared == pytest.approx(1.0)
    assert result.residual_vol == pytest.approx(0.0)
    assert result.sector_fit_score == pytest.approx(2.0)
    assert result.sample_count == 60
    assert result.confidence_status == "qualified"


def test_assess_return_exposure_keeps_low_confidence_result():
    sector_returns = [0.01 if i % 2 == 0 else -0.005 for i in range(60)]
    etf_returns = [0.001 if i % 3 == 0 else -0.001 for i in range(60)]
    results, failures = assess_return_exposure(
        {"LOW": _close_from_returns(etf_returns)}, _close_from_returns(sector_returns)
    )

    assert failures == []
    assert results[0].confidence_status == "low_confidence"
    assert results[0].sample_count == 60


def test_assess_return_exposure_rejects_insufficient_common_returns():
    results, failures = assess_return_exposure(
        {"SHORT": _close_from_returns([0.01] * 10)}, _close_from_returns([0.01] * 10)
    )

    assert results == []
    assert failures[0].etf_code == "SHORT"
    assert failures[0].failure_reason == "insufficient_common_returns"


def test_assess_return_exposure_orders_by_score_then_r_squared_then_code():
    sector_returns = [0.01 if i % 2 == 0 else -0.005 for i in range(60)]
    sector = _close_from_returns(sector_returns)
    closes = {
        "B": _close_from_returns([1.0 * value for value in sector_returns]),
        "A": _close_from_returns([1.0 * value for value in sector_returns]),
        "C": _close_from_returns([0.5 * value for value in sector_returns]),
    }

    results, _ = assess_return_exposure(closes, sector)

    assert [result.etf_code for result in results] == ["A", "B", "C"]


def test_assess_return_exposure_rejects_nonfinite_data_and_zero_sector_variance():
    invalid = pd.Series([100.0] * 60 + [math.nan])
    _, invalid_failures = assess_return_exposure({"BAD": invalid}, _close_from_returns([0.01] * 60))
    _, variance_failures = assess_return_exposure(
        {"FLAT": _close_from_returns([0.01] * 60)}, pd.Series([100.0] * 61)
    )

    assert invalid_failures[0].failure_reason == "nonfinite_close_data"
    assert variance_failures[0].failure_reason == "zero_sector_return_variance"


def test_assess_return_exposure_enforces_hard_minimum_even_when_caller_lowers_minimum():
    closes = _close_from_returns([0.01 if i % 2 else -0.005 for i in range(10)])
    results, failures = assess_return_exposure(
        {"SHORT_MIN": closes}, closes, min_samples=2
    )

    assert results == []
    assert failures[0].failure_reason == "insufficient_common_returns"


def test_assess_return_exposure_rejects_infinite_return_from_zero_close():
    sector = _close_from_returns([0.01] * 60)
    etf = pd.Series([100.0] * 30 + [0.0] + [100.0] * 30)

    results, failures = assess_return_exposure({"ZERO": etf}, sector)

    assert results == []
    assert failures[0].failure_reason == "nonfinite_return_data"


def test_assess_return_exposure_rejects_missing_date_instead_of_mixing_return_intervals():
    dates = pd.bdate_range("2026-05-25", periods=61)
    sector_returns = [0.01 if index % 2 == 0 else -0.005 for index in range(60)]
    sector = pd.Series(_close_from_returns(sector_returns).to_numpy(), index=dates)
    etf = pd.Series(
        _close_from_returns([2.0 * value for value in sector_returns]).to_numpy(),
        index=dates,
    ).drop(dates[30])

    results, failures = assess_return_exposure({"510300.SH": etf}, sector)

    assert results == []
    assert len(failures) == 1
    assert failures[0].etf_code == "510300.SH"
    assert failures[0].failure_reason == "insufficient_consecutive_common_returns"


def test_assess_return_exposure_rejects_stale_etf_with_auditable_failure():
    dates = pd.bdate_range("2026-05-25", periods=61)
    returns = [0.01 if index % 2 == 0 else -0.005 for index in range(60)]
    sector = pd.Series(_close_from_returns(returns).to_numpy(), index=dates)
    stale_etf = pd.Series(_close_from_returns(returns).to_numpy()[:-1], index=dates[:-1])

    results, failures = assess_return_exposure({"510300.SH": stale_etf}, sector)

    assert results == []
    assert failures[0].etf_code == "510300.SH"
    assert failures[0].failure_reason == "stale_price_data"


def test_assess_return_exposure_records_each_etfs_actual_aligned_price_window():
    dates = pd.bdate_range("2026-05-25", periods=61)
    returns = [0.01 if index % 2 == 0 else -0.005 for index in range(60)]
    sector = pd.Series(_close_from_returns(returns).to_numpy(), index=dates)
    etf = pd.Series(
        _close_from_returns(returns[10:]).to_numpy(),
        index=dates[10:],
    )

    results, failures = assess_return_exposure({"159995.SZ": etf}, sector)

    assert failures == []
    assert results[0].sample_count == 50
    assert results[0].window_start_date == date(2026, 6, 8)
    assert results[0].window_end_date == dates[-1].date()
    assert results[0].price_as_of_date == dates[-1].date()
