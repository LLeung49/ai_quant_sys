from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.sector_features import (
    calculate_rvol,
    calculate_simple_return,
    calculate_amount_share,
    calculate_breadth_rvol,
    calculate_share_impulse,
)


def test_amount_share_is_sector_amount_divided_by_same_day_market_amount():
    assert calculate_amount_share(200.0, 1_000.0) == pytest.approx(0.20)


def test_amount_share_is_nan_when_market_amount_is_not_positive():
    assert pd.isna(calculate_amount_share(200.0, 0.0))


def test_share_impulse_compares_current_share_with_twenty_day_average():
    history = pd.Series([0.10] * 20)
    assert calculate_share_impulse(0.20, history) == pytest.approx(2.0)


def test_breadth_rvol_is_fraction_of_valid_stocks_above_one():
    stock_rvol = pd.Series([1.2, 0.8, float("nan"), 1.0])
    assert calculate_breadth_rvol(stock_rvol) == pytest.approx(1 / 3)


def test_simple_return_uses_requested_trading_day_lag():
    close = pd.Series([100.0, 105.0, 110.0])
    assert calculate_simple_return(close, periods=2) == pytest.approx(0.10)


def test_rvol_divides_recent_average_by_long_average():
    amount = pd.Series([10.0] * 20 + [20.0] * 5)
    # 基准窗口包含最近 5 日，20 日均额为 (15*10 + 5*20) / 20 = 12.5。
    assert calculate_rvol(amount, recent_window=5, baseline_window=20) == pytest.approx(1.6)


def test_rvol_returns_nan_when_history_is_too_short():
    assert pd.isna(calculate_rvol(pd.Series([10.0] * 5), recent_window=5, baseline_window=20))
