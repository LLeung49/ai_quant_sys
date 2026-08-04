# 参考并改造自 sector_rotation/derivatives.py。
# 差异：本模块不依赖旧包，新增相对强度加速度和多周期加速度。
"""sector_rotation2 使用的纯时间序列指标。"""
from __future__ import annotations

import pandas as pd


def ma_slope(
    close: pd.Series,
    ma_window: int = 20,
    slope_window: int = 10,
) -> pd.Series:
    """计算移动均线的滚动最小二乘斜率。"""
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
    """按既有系统的 HIST×2 约定计算 MACD 柱。"""
    fast_ema = close.ewm(span=fast, adjust=False).mean()
    slow_ema = close.ewm(span=slow, adjust=False).mean()
    dif = fast_ema - slow_ema
    dea = dif.ewm(span=signal, adjust=False).mean()
    return (dif - dea) * 2.0


def relative_strength(sector: pd.Series, benchmark: pd.Series, periods: int) -> pd.Series:
    """在共同交易日上计算板块收益减基准收益。"""
    aligned_sector, aligned_benchmark = sector.align(benchmark, join="inner")
    return aligned_sector.pct_change(periods) - aligned_benchmark.pct_change(periods)


def rs_acceleration(relative_strength_series: pd.Series, lag: int = 5) -> pd.Series:
    """计算固定交易日滞后下的相对强度变化。"""
    return relative_strength_series - relative_strength_series.shift(lag)


def multi_horizon_acceleration(rs_5: pd.Series, rs_20: pd.Series) -> pd.Series:
    """比较近期相对强度与中期平均速度，用于诊断多周期加速度。"""
    aligned_rs5, aligned_rs20 = rs_5.align(rs_20, join="inner")
    return aligned_rs5 - 0.25 * aligned_rs20
