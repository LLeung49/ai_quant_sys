"""v2_short_term 短期原始特征的单元测试：覆盖 ``rs_5`` 与 ``rs5_accel_1d`` 的新实现。"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.short_term.config import DEFAULT_SHORT_TERM_CONFIG
from morning_conference.sector_rotation2.short_term.features import (
    _relative_strength,
    calculate_sector_short_term_features,
)


def _date_index(days: int) -> pd.DatetimeIndex:
    return pd.date_range(end="2026-08-14", periods=days, freq="B")


def test_relative_strength_subtracts_benchmark_for_arbitrary_lookback():
    close = pd.Series([100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 110.0])
    benchmark = pd.Series([100.0, 100.5, 101.0, 101.5, 102.0, 102.5, 103.0, 105.0])

    rs_1 = _relative_strength(close, benchmark, lookback=1)
    rs_2 = _relative_strength(close, benchmark, lookback=2)
    rs_5 = _relative_strength(close, benchmark, lookback=5)

    # lookback=1：1 日累计 → t/prev - 1
    expected_rs_1 = (110.0 / 106.0 - 1.0) - (105.0 / 103.0 - 1.0)
    # lookback=2：2 日累计 → t/prev2 - 1
    expected_rs_2 = (110.0 / 105.0 - 1.0) - (105.0 / 102.5 - 1.0)
    # lookback=5：5 日累计 → t/prev5 - 1
    expected_rs_5 = (110.0 / 102.0 - 1.0) - (105.0 / 101.0 - 1.0)

    assert rs_1 == pytest.approx(expected_rs_1)
    assert rs_2 == pytest.approx(expected_rs_2)
    assert rs_5 == pytest.approx(expected_rs_5)


def test_relative_strength_returns_nan_when_history_too_short():
    close = pd.Series([100.0, 101.0, 102.0])
    benchmark = pd.Series([100.0, 100.5, 101.0])
    assert np.isnan(_relative_strength(close, benchmark, lookback=5))


def test_calculate_sector_short_term_features_emits_rs5():
    days = 70
    dates = _date_index(days)
    close = pd.Series(np.linspace(100.0, 110.0, days), index=dates)
    benchmark = pd.Series(np.linspace(100.0, 105.0, days), index=dates)
    amount = pd.Series(np.full(days, 100.0), index=dates)
    benchmark_amount = pd.Series(np.full(days, 1_000.0), index=dates)

    result = calculate_sector_short_term_features(
        close=close,
        benchmark_close=benchmark,
        amount=amount,
        benchmark_amount=benchmark_amount,
        member_amount_history=None,
        config=DEFAULT_SHORT_TERM_CONFIG,
    )

    assert "rs_5" in result
    expected_rs_5 = (
        close.iloc[-1] / close.iloc[-6] - 1.0
        - (benchmark.iloc[-1] / benchmark.iloc[-6] - 1.0)
    )
    assert result["rs_5"] == pytest.approx(expected_rs_5)
    # rs_5 与 rs_1 / rs_2 都共享同一口径（基准来自 build_market_benchmark 的归一化）。
    assert np.isfinite(result["rs_1"])
    assert np.isfinite(result["rs_2"])
    # rs5_accel_1d 应当等于 rs_5 当日 - rs_5 昨日。
    rs5_today = (
        close.iloc[-1] / close.iloc[-6] - 1.0
        - (benchmark.iloc[-1] / benchmark.iloc[-6] - 1.0)
    )
    rs5_yesterday = (
        close.iloc[-2] / close.iloc[-7] - 1.0
        - (benchmark.iloc[-2] / benchmark.iloc[-7] - 1.0)
    )
    assert result["rs5_accel_1d"] == pytest.approx(rs5_today - rs5_yesterday)


def test_calculate_sector_short_term_features_returns_nan_when_history_is_short():
    days = 4
    dates = _date_index(days)
    close = pd.Series([100.0, 101.0, 102.0, 103.0], index=dates)
    benchmark = pd.Series([100.0, 100.5, 101.0, 101.5], index=dates)
    amount = pd.Series([100.0] * days, index=dates)
    benchmark_amount = pd.Series([1_000.0] * days, index=dates)

    result = calculate_sector_short_term_features(
        close=close,
        benchmark_close=benchmark,
        amount=amount,
        benchmark_amount=benchmark_amount,
        member_amount_history=None,
        config=DEFAULT_SHORT_TERM_CONFIG,
    )

    assert np.isnan(result["rs_5"])
    assert np.isnan(result["rs5_accel_1d"])
