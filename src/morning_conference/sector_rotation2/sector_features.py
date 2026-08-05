"""板块原始特征的纯计算函数。

本模块只计算特征，不访问数据库；数据加载与每日特征面板编排将在调用层完成。
"""
from __future__ import annotations

import pandas as pd

from .derivatives import macd_hist, ma_slope, relative_strength, rs_acceleration


def calculate_simple_return(close: pd.Series, periods: int) -> float:
    """计算序列末日相对指定交易日滞后的简单收益率。

    参数:
        close: 按交易日升序的收盘价序列。
        periods: 当前日与比较日之间的交易日间隔。
    返回:
        close[-1] / close[-periods-1] - 1；历史不足或比较价格非正时返回 NaN。
    """
    if len(close) <= periods:
        return float("nan")
    base = close.iloc[-periods - 1]
    return float(close.iloc[-1] / base - 1.0) if pd.notna(base) and base > 0 else float("nan")


def calculate_rvol(amount: pd.Series, recent_window: int, baseline_window: int) -> float:
    """计算近期平均成交额相对较长基准窗口平均成交额的量比。

    参数:
        amount: 按交易日升序的成交额序列。
        recent_window: 近期均值窗口，例如 5 日。
        baseline_window: 历史基准均值窗口，例如 20 或 60 日。
    返回:
        最近 recent_window 日均额 / 最近 baseline_window 日均额；样本不足或基准非正时返回 NaN。
    """
    if len(amount) < baseline_window:
        return float("nan")
    recent_mean = amount.iloc[-recent_window:].mean()
    baseline_mean = amount.iloc[-baseline_window:].mean()
    return float(recent_mean / baseline_mean) if pd.notna(baseline_mean) and baseline_mean > 0 else float("nan")


def calculate_sector_price_features(close: pd.Series, benchmark_close: pd.Series) -> dict[str, float]:
    """计算单板块的收益、相对强度和均线位置原始特征。

    参数:
        close: 按交易日升序排列的板块收盘指数序列。
        benchmark_close: 同期市场基准收盘序列。
    返回:
        含 ret_5/20、rs_5/20/60、distance_ma20、distance_ma60 的字典；
        任何窗口历史不足时对应字段为 NaN。
    """
    rs_5 = relative_strength(close, benchmark_close, 5)
    rs_20 = relative_strength(close, benchmark_close, 20)
    rs_60 = relative_strength(close, benchmark_close, 60)
    ma20 = close.rolling(20, min_periods=20).mean()
    ma60 = close.rolling(60, min_periods=60).mean()
    latest = close.iloc[-1] if not close.empty else float("nan")

    def latest_value(series: pd.Series) -> float:
        return float(series.iloc[-1]) if not series.empty and pd.notna(series.iloc[-1]) else float("nan")

    ma20_last, ma60_last = latest_value(ma20), latest_value(ma60)
    return {
        "ret_5": calculate_simple_return(close, 5),
        "ret_20": calculate_simple_return(close, 20),
        "rs_5": latest_value(rs_5),
        "rs_20": latest_value(rs_20),
        "rs_60": latest_value(rs_60),
        "distance_ma20": float(latest / ma20_last - 1.0) if ma20_last > 0 else float("nan"),
        "distance_ma60": float(latest / ma60_last - 1.0) if ma60_last > 0 else float("nan"),
    }


def calculate_sector_trend_features(close: pd.Series, benchmark_close: pd.Series) -> dict[str, float]:
    """计算趋势速度和加速度层所需的单板块原始指标。

    参数:
        close: 按交易日升序排列的板块收盘指数序列。
        benchmark_close: 同期市场基准收盘序列。
    返回:
        含 MA20 斜率、RS20 加速度、MA20 斜率加速度、MACD 柱及其单日变化的字典；
        所需窗口历史不足时对应字段为 NaN。
    """
    slope = ma_slope(close)
    relative_strength_20 = relative_strength(close, benchmark_close, 20)
    rs20_accel = rs_acceleration(relative_strength_20, lag=5)
    slope_accel = slope - slope.shift(5)
    hist = macd_hist(close)

    def latest_value(series: pd.Series) -> float:
        return float(series.iloc[-1]) if not series.empty and pd.notna(series.iloc[-1]) else float("nan")

    return {
        "ma20_slope": latest_value(slope),
        "rs20_accel": latest_value(rs20_accel),
        "ma20_accel": latest_value(slope_accel),
        "macd_hist": latest_value(hist),
        "macd_hist_delta": latest_value(hist.diff()),
    }


def calculate_amount_share(sector_amount: float, market_amount: float) -> float:
    """计算板块成交额占同日有效市场成交额的比例。

    参数:
        sector_amount: 单板块当日成交额。
        market_amount: 同层级全部有效板块当日成交额之和。
    返回:
        板块成交额份额；市场成交额非正时返回 NaN。
    """
    return sector_amount / market_amount if market_amount > 0 else float("nan")


def calculate_share_impulse(current_share: float, share_history: pd.Series) -> float:
    """计算当前资金份额相对于过去 20 日平均份额的冲量。

    参数:
        current_share: 当前交易日的板块成交额份额。
        share_history: 截止当前日前的历史成交额份额序列。
    返回:
        current_share / 最近 20 日平均份额；历史不足、均值非正时返回 NaN。
    """
    baseline = share_history.tail(20).mean()
    return current_share / baseline if pd.notna(baseline) and baseline > 0 else float("nan")


def calculate_breadth_rvol(stock_rvol: pd.Series) -> float:
    """计算有效成分股中个股 RVOL 严格大于 1 的比例。

    参数:
        stock_rvol: 每只成分股的成交额相对量比序列。
    返回:
        放量股票占有效股票的比例；无有效股票时返回 NaN。
    """
    valid = stock_rvol.dropna()
    return float((valid > 1.0).mean()) if not valid.empty else float("nan")
