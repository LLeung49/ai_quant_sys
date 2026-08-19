"""Tests for trend_features: relative returns, persistence, ER/ADX, alpha strength."""

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.stock_alpha.trend_features import (
    calc_adx14,
    calc_alpha_persistence,
    calc_kama_er,
    calc_relative_return,
    calc_relative_returns,
    calc_volatility,
    score_alpha_strength,
    score_trend_quality,
    sector_local_percentile,
)


def test_positive_stock_return_can_have_negative_sector_alpha() -> None:
    assert calc_relative_return(stock_ret=0.08, sector_ret=0.10) == pytest.approx(-0.02)


def test_calc_relative_returns_aligns_on_common_dates() -> None:
    dates = [date(2026, 8, 13) + timedelta(days=i) for i in range(6)]
    stock = pd.Series([1.00, 1.02, 1.05, 1.06, 1.08, 1.10], index=dates)
    sector = pd.Series([1.00, 1.05, 1.05, 1.04, 1.04, 1.05], index=dates)
    out = calc_relative_returns(stock, sector, windows=(5,))
    assert out == {"rr_5": pytest.approx(0.05)}


def test_calc_relative_returns_uses_window_span() -> None:
    dates = [date(2026, 8, 15) + timedelta(days=i) for i in range(3)]
    stock = pd.Series([1.00, 1.02, 1.05], index=dates)
    sector = pd.Series([1.00, 1.05, 1.05], index=dates)
    out = calc_relative_returns(stock, sector, windows=(5,))
    assert out == {"rr_5": None}


def test_calc_relative_returns_handles_missing_alignment() -> None:
    stock = pd.Series([1.00, 1.02], index=[date(2026, 8, 16), date(2026, 8, 17)])
    sector = pd.Series([1.00, 1.02], index=[date(2026, 8, 13), date(2026, 8, 14)])
    out = calc_relative_returns(stock, sector, windows=(5,))
    assert out == {"rr_5": None}


def test_sector_local_percentile_isolates_between_sectors() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 4,
        "sector_name": ["Bank", "Bank", "Tech", "Tech"],
        "rr_5": [-0.05, 0.10, -0.20, 0.05],
    })
    out = sector_local_percentile(frame, "rr_5")
    assert out.iloc[0] == pytest.approx(-0.5)
    assert out.iloc[1] == pytest.approx(0.5)
    assert out.iloc[2] == pytest.approx(-0.5)
    assert out.iloc[3] == pytest.approx(0.5)


def test_sector_local_percentile_assigns_zero_for_single_member_groups() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 3,
        "sector_name": ["Bank", "Tech", "Tech"],
        "rr_5": [0.10, 0.05, 0.20],
    })
    out = sector_local_percentile(frame, "rr_5")
    assert out.iloc[0] == pytest.approx(0.0)
    assert out.iloc[1] == pytest.approx(-0.5)
    assert out.iloc[2] == pytest.approx(0.5)


def test_sector_local_percentile_propagates_nans() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 3,
        "sector_name": ["Bank", "Bank", "Bank"],
        "rr_5": [np.nan, 0.10, 0.05],
    })
    out = sector_local_percentile(frame, "rr_5")
    assert pd.isna(out.iloc[0])
    assert out.iloc[1] == pytest.approx(0.5)
    assert out.iloc[2] == pytest.approx(-0.5)


def test_sector_local_percentile_maps_extremes_to_half_for_size_three() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 3,
        "sector_name": ["Bank", "Bank", "Bank"],
        "rr_5": [0.01, 0.05, 0.10],
    })
    out = sector_local_percentile(frame, "rr_5")
    assert out.iloc[0] == pytest.approx(-0.5)
    assert out.iloc[2] == pytest.approx(0.5)


def test_score_alpha_strength_renormalizes_on_missing_windows() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 2,
        "sector_name": ["Bank", "Bank"],
        "rr_5": [0.10, 0.20],
        "rr_10": [np.nan, np.nan],
        "rr_20": [np.nan, np.nan],
    })
    out = score_alpha_strength(frame, windows=(5, 10, 20), alpha_weights=(0.5, 0.3, 0.2), min_alpha_weight=0.60)
    assert out["alpha_strength"].isna().all()


def test_score_alpha_strength_uses_partial_window_when_floor_met() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 2,
        "sector_name": ["Bank", "Bank"],
        "rr_5": [0.10, 0.20],
        "rr_10": [0.05, 0.15],
        "rr_20": [np.nan, np.nan],
    })
    out = score_alpha_strength(frame, windows=(5, 10, 20), alpha_weights=(0.5, 0.3, 0.2), min_alpha_weight=0.60)
    assert out.iloc[0]["alpha_strength"] == pytest.approx(-0.5)
    assert out.iloc[1]["alpha_strength"] == pytest.approx(0.5)


def test_alpha_persistence_top_8_of_10_yields_0_6() -> None:
    history = {"code": [0.80] * 8 + [0.10, 0.10]}
    assert calc_alpha_persistence(history) == pytest.approx(2 * 8 / 10 - 1)


def test_alpha_persistence_returns_none_when_fewer_than_min_dates() -> None:
    history = {"code": [0.80, 0.85, 0.90, 0.91, 0.92]}
    assert calc_alpha_persistence(history, min_dates=6) is None


def test_alpha_persistence_ignores_none_values_in_history() -> None:
    history = {"code": [None, None, 0.80, 0.85, 0.90, 0.91, 0.92, 0.93]}
    assert calc_alpha_persistence(history) == pytest.approx(2 * 6 / 6 - 1)


def test_alpha_persistence_returns_negative_when_below_top_threshold() -> None:
    history = {"code": [0.10] * 10}
    assert calc_alpha_persistence(history) == pytest.approx(-1.0)


def test_kama_er_one_for_monotonic_series() -> None:
    series = pd.Series([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])
    assert calc_kama_er(series, window=10) == pytest.approx(1.0)


def test_kama_er_near_zero_for_alternating_series() -> None:
    series = pd.Series([1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0, 1.1, 1.0])
    assert calc_kama_er(series, window=10) == pytest.approx(0.0)


def test_kama_er_returns_none_when_history_short() -> None:
    series = pd.Series([1.0, 1.1])
    assert calc_kama_er(series, window=10) is None


def _adx_fixture() -> tuple:
    n = 60
    base = np.linspace(100, 130, n)
    high = base + 1
    low = base - 1
    close = base
    return pd.Series(high), pd.Series(low), pd.Series(close)


def test_adx14_trending_series_positive() -> None:
    high, low, close = _adx_fixture()
    value = calc_adx14(high, low, close)
    assert value is not None and value > 0


def test_adx14_returns_none_when_history_too_short() -> None:
    high = pd.Series([1, 2, 3])
    low = pd.Series([1, 1, 1])
    close = pd.Series([1, 2, 3])
    assert calc_adx14(high, low, close) is None


def test_score_trend_quality_combines_er_and_adx() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 3,
        "sector_name": ["Bank", "Bank", "Bank"],
        "er": [0.1, 0.5, 0.9],
        "adx": [10.0, 20.0, 30.0],
    })
    out = score_trend_quality(frame)
    assert out.iloc[0]["trend_quality"] == pytest.approx(-0.5)
    assert out.iloc[1]["trend_quality"] == pytest.approx(0.0)
    assert out.iloc[2]["trend_quality"] == pytest.approx(0.5)


def test_score_trend_quality_handles_missing_components() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 2,
        "sector_name": ["Bank", "Bank"],
        "er": [np.nan, 0.5],
        "adx": [20.0, 30.0],
    })
    out = score_trend_quality(frame)
    # Row 0: er_pct = NaN, adx_pct = -0.5 -> only adx contributes.
    assert out.iloc[0]["trend_quality"] == pytest.approx(-0.5)
    # Row 1: er_pct = 0.0 (single valid), adx_pct = +0.5 -> 0.5*0 + 0.5*0.5 = 0.25.
    assert out.iloc[1]["trend_quality"] == pytest.approx(0.25)


def test_calc_volatility_uses_annualization_factor() -> None:
    series = pd.Series([0.01] * 19 + [0.02])
    value = calc_volatility(series, window=20)
    # std(ddof=0) = sqrt(mean((x - mean)^2)). Mean = (19*0.01 + 0.02) / 20 = 0.0105.
    # Variance = (19*(0.0105-0.01)^2 + (0.0105-0.02)^2) / 20 = (19*2.5e-7 + 9.025e-5) / 20.
    expected_std = float(np.std([0.01] * 19 + [0.02], ddof=0))
    assert value == pytest.approx(expected_std * (252 ** 0.5))


def test_calc_volatility_returns_none_for_short_history() -> None:
    series = pd.Series([0.01] * 10)
    assert calc_volatility(series, window=20) is None


def test_calc_volatility_returns_none_when_history_has_nan() -> None:
    series = pd.Series([0.01] * 19 + [np.nan])
    assert calc_volatility(series, window=20) is None


def test_sector_local_percentile_rejects_missing_column() -> None:
    frame = pd.DataFrame({"x": [1]})
    with pytest.raises(ValueError, match="missing column"):
        sector_local_percentile(frame, "rr_5")
