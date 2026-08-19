"""Tests for trend_structure: MA stack, breakout, strong pullback, structure score."""

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.stock_alpha.trend_structure import (
    calc_breakout_flags,
    calc_ma,
    calc_ma_slope,
    calc_ma_stack,
    calc_prev_high,
    calc_strong_pullback,
    score_trend_structure,
)


def test_calc_ma_stack_requires_positive_slope() -> None:
    close = pd.Series([10, 11, 12, 13, 14])
    ma20 = pd.Series([9, 10, 11, 12, 13])
    ma60 = pd.Series([8, 9, 10, 11, 12])
    slope = pd.Series([0.01, 0.02, 0.03, 0.04, 0.05])
    assert calc_ma_stack(close, ma20, ma60, slope) is True


def test_calc_ma_stack_rejects_negative_slope() -> None:
    close = pd.Series([10, 11, 12, 13, 14])
    ma20 = pd.Series([9, 10, 11, 12, 13])
    ma60 = pd.Series([8, 9, 10, 11, 12])
    slope = pd.Series([0.01, 0.02, -0.01, -0.02, -0.05])
    assert calc_ma_stack(close, ma20, ma60, slope) is False


def test_calc_ma_stack_rejects_inverted_stack() -> None:
    close = pd.Series([10, 9, 8, 7, 6])
    ma20 = pd.Series([11, 10, 9, 8, 7])
    ma60 = pd.Series([12, 11, 10, 9, 8])
    slope = pd.Series([0.01] * 5)
    assert calc_ma_stack(close, ma20, ma60, slope) is False


def test_calc_ma_stack_returns_false_when_last_value_is_nan() -> None:
    close = pd.Series([10.0, 11.0, np.nan])
    ma20 = pd.Series([9.0, 10.0, 11.0])
    ma60 = pd.Series([8.0, 9.0, 10.0])
    slope = pd.Series([0.01, 0.02, 0.03])
    assert calc_ma_stack(close, ma20, ma60, slope) is False


def test_breakout_uses_shifted_history_only() -> None:
    dates = pd.date_range("2026-08-01", periods=22, freq="D")
    highs = pd.Series([10.0] * 21 + [15.0], index=dates)
    prev_high_20 = calc_prev_high(highs, window=20)
    breakout20, _ = calc_breakout_flags(highs, prev_high_20, prev_high_20.copy())
    assert breakout20 is True
    expected = float(highs.iloc[:-1].tail(20).max())
    assert float(prev_high_20.iloc[-1]) == expected


def test_breakout_returns_false_when_not_exceeding_prior_high() -> None:
    dates = pd.date_range("2026-08-01", periods=22, freq="D")
    highs = pd.Series([10.0, 11.0, 12.0, 13.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0] + [10.0] * 12, index=dates)
    prev_high_20 = calc_prev_high(highs, window=20)
    breakout20, _ = calc_breakout_flags(highs, prev_high_20, prev_high_20.copy())
    assert breakout20 is False


def test_breakout_returns_false_when_last_value_is_nan() -> None:
    highs = pd.Series([10.0, 11.0, np.nan])
    prev_high = pd.Series([9.0, 10.0, 11.0])
    breakout20, breakout60 = calc_breakout_flags(highs, prev_high, prev_high.copy())
    assert breakout20 is False
    assert breakout60 is False


def test_calc_prev_high_rejects_non_positive_window() -> None:
    with pytest.raises(ValueError, match="window must be positive"):
        calc_prev_high(pd.Series([1.0]), window=0)


def test_calc_ma_returns_simple_moving_average() -> None:
    series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    ma = calc_ma(series, window=3)
    assert float(ma.iloc[-1]) == pytest.approx(4.0)


def test_calc_ma_rejects_non_positive_window() -> None:
    with pytest.raises(ValueError, match="window must be positive"):
        calc_ma(pd.Series([1.0]), window=0)


def test_calc_ma_slope_returns_positive_ratio_for_uptrend() -> None:
    series = pd.Series([10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 14.0, 15.0, 16.0])
    slope = calc_ma_slope(series, window=5)
    last_value = float(slope.iloc[-1])
    assert last_value > 0


def test_calc_ma_slope_rejects_non_positive_window() -> None:
    with pytest.raises(ValueError, match="window must be positive"):
        calc_ma_slope(pd.Series([1.0]), window=0)


def _pullback_fixture(drawdown: float = 0.05, vol_ratio: float = 0.70) -> tuple:
    """Return a 30-day fixture with healthy uptrend, MA20 pullback, low volume."""
    n = 30
    base = pd.Series(np.linspace(10.0, 20.0, n))
    high = base + 0.5
    ma20 = base.rolling(20, min_periods=20).mean()
    volume = pd.Series([100.0] * n)
    volume.iloc[-3:] = vol_ratio * 100.0
    vol_3 = volume.rolling(3, min_periods=3).mean()
    vol_20 = volume.rolling(20, min_periods=20).mean()
    close = base.copy()
    high_10 = float(high.iloc[-11:].max())
    close.iloc[-1] = high_10 * (1.0 - drawdown)
    return close, high, ma20, vol_3, vol_20


def test_calc_strong_pullback_requires_all_four_conditions() -> None:
    close, high, ma20, vol_3, vol_20 = _pullback_fixture(drawdown=0.05, vol_ratio=0.70)
    assert calc_strong_pullback(close, high, ma20, vol_3, vol_20) is True


def test_calc_strong_pullback_rejects_excessive_drawdown() -> None:
    close, high, ma20, vol_3, vol_20 = _pullback_fixture(drawdown=0.15, vol_ratio=0.70)
    assert calc_strong_pullback(close, high, ma20, vol_3, vol_20) is False


def test_calc_strong_pullback_rejects_volume_expansion() -> None:
    close, high, ma20, vol_3, vol_20 = _pullback_fixture(drawdown=0.05, vol_ratio=1.50)
    assert calc_strong_pullback(close, high, ma20, vol_3, vol_20) is False


def test_calc_strong_pullback_rejects_close_below_recent_ma20() -> None:
    close, high, ma20, vol_3, vol_20 = _pullback_fixture(drawdown=0.05, vol_ratio=0.70)
    close.iloc[-2] = ma20.iloc[-2] - 1.0
    assert calc_strong_pullback(close, high, ma20, vol_3, vol_20) is False


def test_calc_strong_pullback_rejects_short_history() -> None:
    close = pd.Series([10.0] * 5)
    high = pd.Series([10.5] * 5)
    ma20 = pd.Series([9.5] * 5)
    vol = pd.Series([100.0] * 5)
    assert calc_strong_pullback(close, high, ma20, vol, vol) is False


def test_score_trend_structure_renormalizes_missing_components() -> None:
    frame = pd.DataFrame({
        "ma_stack": [True, True],
        "breakout20": [np.nan, False],
        "breakout60": [False, np.nan],
        "strong_pullback": [False, True],
    })
    out = score_trend_structure(frame)
    # Row 0: ma_stack True (.35), breakout20 NaN (skip weight),
    # breakout60 False (.20 * 0 = 0), strong_pullback False (.20 * 0 = 0).
    # Total weight = 0.35 + 0.20 + 0.20 = 0.75; weighted = 0.35; score = 0.4667.
    assert out.iloc[0]["trend_structure"] == pytest.approx(0.35 / 0.75)
    # Row 1: ma_stack True (.35), breakout20 False (.25*0), breakout60 NaN (skip),
    # strong_pullback True (.20). Total weight = 0.80; weighted = 0.55.
    assert out.iloc[1]["trend_structure"] == pytest.approx(0.55 / 0.80)


def test_score_trend_structure_all_components_score_one() -> None:
    frame = pd.DataFrame({
        "ma_stack": [True],
        "breakout20": [True],
        "breakout60": [True],
        "strong_pullback": [True],
    })
    out = score_trend_structure(frame)
    assert out.iloc[0]["trend_structure"] == pytest.approx(1.0)


def test_score_trend_structure_returns_nan_when_no_components() -> None:
    frame = pd.DataFrame({
        "ma_stack": [np.nan],
        "breakout20": [np.nan],
        "breakout60": [np.nan],
        "strong_pullback": [np.nan],
    })
    out = score_trend_structure(frame)
    assert pd.isna(out.iloc[0]["trend_structure"])


def test_score_trend_structure_validates_weight_sum() -> None:
    with pytest.raises(ValueError, match="structure_weights must sum to 1.0"):
        score_trend_structure(
            pd.DataFrame({
                "ma_stack": [True], "breakout20": [False], "breakout60": [False], "strong_pullback": [False],
            }),
            weights={"ma_stack": 0.5, "breakout20": 0.3, "breakout60": 0.3, "strong_pullback": 0.1},
        )
