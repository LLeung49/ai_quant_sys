# Copied/adapted from sector_rotation/derivatives.py.
# Differences: this module has no dependency on the old package and adds
# relative-strength acceleration plus multi-horizon acceleration.
"""Pure time-series indicators used by sector_rotation2."""
from __future__ import annotations

import pandas as pd


def ma_slope(
    close: pd.Series,
    ma_window: int = 20,
    slope_window: int = 10,
) -> pd.Series:
    """Return the rolling least-squares slope of a moving average."""
    ma = close.rolling(ma_window, min_periods=ma_window).mean()
    x = pd.Series(range(slope_window), dtype="float64")

    def slope(values: pd.Series) -> float:
        if values.isna().any():
            return float("nan")
        centered_x = x - x.mean()
        return float((centered_x * (values.reset_index(drop=True) - values.mean())).sum() / (centered_x**2).sum())

    return ma.rolling(slope_window, min_periods=slope_window).apply(slope, raw=False)


def macd_hist(
    close: pd.Series,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
) -> pd.Series:
    """Return the MACD histogram using the existing system's 2x convention."""
    fast_ema = close.ewm(span=fast, adjust=False).mean()
    slow_ema = close.ewm(span=slow, adjust=False).mean()
    dif = fast_ema - slow_ema
    dea = dif.ewm(span=signal, adjust=False).mean()
    return (dif - dea) * 2.0


def relative_strength(sector: pd.Series, benchmark: pd.Series, periods: int) -> pd.Series:
    """Return sector return less benchmark return on their common trade dates."""
    aligned_sector, aligned_benchmark = sector.align(benchmark, join="inner")
    return aligned_sector.pct_change(periods) - aligned_benchmark.pct_change(periods)


def rs_acceleration(relative_strength_series: pd.Series, lag: int = 5) -> pd.Series:
    """Return the change in relative strength over a fixed trading-day lag."""
    return relative_strength_series - relative_strength_series.shift(lag)


def multi_horizon_acceleration(rs_5: pd.Series, rs_20: pd.Series) -> pd.Series:
    """Compare recent relative strength with its medium-horizon average speed."""
    aligned_rs5, aligned_rs20 = rs_5.align(rs_20, join="inner")
    return aligned_rs5 - 0.25 * aligned_rs20
