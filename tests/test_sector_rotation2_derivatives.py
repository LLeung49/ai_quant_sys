from __future__ import annotations

from decimal import Decimal

import pandas as pd
import pytest

from morning_conference.sector_rotation2.derivatives import (
    macd_hist,
    multi_horizon_acceleration,
    relative_strength,
    rs_acceleration,
)


def test_relative_strength_subtracts_benchmark_return():
    sector = pd.Series([100.0, 110.0, 121.0])
    benchmark = pd.Series([100.0, 105.0, 110.0])

    result = relative_strength(sector, benchmark, periods=2)

    assert result.iloc[-1] == pytest.approx(0.11)


def test_relative_strength_aligns_on_common_dates():
    sector = pd.Series([100.0, 110.0, 121.0], index=pd.date_range("2026-01-01", periods=3))
    benchmark = pd.Series([100.0, 105.0, 110.0], index=pd.date_range("2026-01-02", periods=3))

    result = relative_strength(sector, benchmark, periods=1)

    assert result.index.tolist() == list(pd.date_range("2026-01-02", periods=2))


def test_relative_strength_accepts_mysql_decimal_close_values():
    """MySQL DECIMAL 收盘价与 float 基准相减前必须统一为浮点数。"""
    sector = pd.Series([Decimal("100.00"), Decimal("110.00"), Decimal("121.00")])
    benchmark = pd.Series([100.0, 105.0, 110.0])

    result = relative_strength(sector, benchmark, periods=2)

    assert result.iloc[-1] == pytest.approx(0.11)


def test_rs_acceleration_uses_relative_strength_series():
    result = rs_acceleration(pd.Series([0.01, 0.02, 0.05]), lag=2)

    assert result.iloc[-1] == pytest.approx(0.04)


def test_multi_horizon_acceleration_compares_short_and_medium_speed():
    result = multi_horizon_acceleration(
        pd.Series([0.03]),
        pd.Series([0.04]),
    )

    assert result.iloc[0] == pytest.approx(0.02)


def test_macd_hist_and_its_change_are_distinct_series():
    close = pd.Series(range(1, 50), dtype="float64")

    hist = macd_hist(close)

    assert hist.iloc[-1] != hist.diff().iloc[-1]
