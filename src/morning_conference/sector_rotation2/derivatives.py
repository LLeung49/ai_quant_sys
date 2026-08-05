# 参考并改造自 sector_rotation/derivatives.py。
# 差异：本模块不依赖旧包，新增相对强度加速度和多周期加速度。
"""sector_rotation2 使用的纯时间序列指标。"""
from __future__ import annotations

import pandas as pd
from scipy.stats import linregress


def ma_slope(
    close: pd.Series,
    ma_window: int = 20,
    slope_window: int = 10,
) -> pd.Series:
    """计算移动均线的滚动最小二乘斜率。

    参数:
        close: 按交易日升序排列的收盘价序列。
        ma_window: 先计算简单移动均线的交易日窗口。
        slope_window: 对均线拟合线性斜率的交易日窗口。
    返回:
        与 close 索引一致的斜率序列；历史不足处为 NaN。
    """
    ma = close.rolling(ma_window, min_periods=ma_window).mean()
    def slope(values: pd.Series) -> float:
        """拟合单个均线窗口并返回 scipy 标准最小二乘斜率。

        参数:
            values: rolling 窗口内的均线观测值。
        返回:
            线性回归斜率；窗口含缺失值时返回 NaN。
        """
        if values.isna().any():
            return float("nan")
        return float(linregress(range(len(values)), values.to_numpy()).slope)

    return ma.rolling(slope_window, min_periods=slope_window).apply(slope, raw=False)


def macd_hist(
    close: pd.Series,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
) -> pd.Series:
    """按既有系统的 HIST×2 约定计算 MACD 柱。

    参数:
        close: 按交易日升序排列的收盘价序列。
        fast: 快速 EMA 周期，默认 12。
        slow: 慢速 EMA 周期，默认 26。
        signal: DIF 信号线 EMA 周期，默认 9。
    返回:
        与 close 索引一致的 MACD HIST 序列。
    """
    fast_ema = close.ewm(span=fast, adjust=False).mean()
    slow_ema = close.ewm(span=slow, adjust=False).mean()
    dif = fast_ema - slow_ema
    dea = dif.ewm(span=signal, adjust=False).mean()
    return (dif - dea) * 2.0


def relative_strength(sector: pd.Series, benchmark: pd.Series, periods: int) -> pd.Series:
    """在共同交易日上计算板块收益减基准收益。

    参数:
        sector: 板块收盘价序列。
        benchmark: 市场基准收盘价序列。
        periods: 计算收益率使用的交易日滞后期。
    返回:
        仅保留双方共同日期的相对强度序列；历史不足处为 NaN。
    """
    aligned_sector, aligned_benchmark = sector.align(benchmark, join="inner")
    return aligned_sector.pct_change(periods) - aligned_benchmark.pct_change(periods)


def rs_acceleration(relative_strength_series: pd.Series, lag: int = 5) -> pd.Series:
    """计算固定交易日滞后下的相对强度变化。

    参数:
        relative_strength_series: 已计算好的相对强度时间序列。
        lag: 比较当前相对强度与过去值的交易日滞后数。
    返回:
        与输入索引一致的相对强度加速度序列。
    """
    return relative_strength_series - relative_strength_series.shift(lag)


def multi_horizon_acceleration(rs_5: pd.Series, rs_20: pd.Series) -> pd.Series:
    """比较近期相对强度与中期平均速度，用于诊断多周期加速度。

    参数:
        rs_5: 5 日相对强度序列。
        rs_20: 20 日相对强度序列。
    返回:
        双方共同日期上的 rs_5 - 0.25 * rs_20 序列。
    """
    aligned_rs5, aligned_rs20 = rs_5.align(rs_20, join="inner")
    return aligned_rs5 - 0.25 * aligned_rs20
