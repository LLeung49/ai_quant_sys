from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.sector_features import (
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
