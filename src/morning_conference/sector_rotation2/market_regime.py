"""依据市场基准、广度和成交数据标注当日市场状态。

市场状态用于下游控制风险暴露，而不是改变板块间的相对排名。该模块完全由
传入的历史 DataFrame 计算，便于每日运行和回填使用相同逻辑。
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class MarketRegime:
    """一次市场状态判断的不可变结果。

    属性:
        market_regime: 规格定义的 ``risk_off``、``high_volatility``、
            ``risk_on`` 或 ``range`` 状态名。
        regime_multiplier: 仅供风险暴露缩放的公共乘数，不能参与板块排序。
    """

    market_regime: str
    regime_multiplier: float


def _as_of_row(frame: pd.DataFrame, as_of_date: pd.Timestamp) -> pd.Series:
    """取得不晚于指定日期的最后一行数据。

    参数:
        frame: 日期索引已转换为 ``DatetimeIndex`` 的历史数据。
        as_of_date: 目标交易日。
    返回:
        目标日或此前最近一个交易日的行。
    异常:
        ValueError: 没有不晚于目标日的可用历史时抛出。
    """
    eligible = frame.loc[frame.index <= as_of_date]
    if eligible.empty:
        raise ValueError("市场状态缺少不晚于 as_of_date 的历史数据")
    return eligible.iloc[-1]


def classify_market_regime(
    benchmark: pd.DataFrame,
    breadth_history: pd.Series,
    market_aggregates: pd.DataFrame,
    as_of_date: pd.Timestamp,
) -> MarketRegime:
    """按固定优先级为目标交易日分类市场状态。

    ``risk_off``、``high_volatility``、``risk_on`` 和 ``range`` 的判断次序与
    规格一致。数据窗口不足以计算某个条件时，该条件视为不命中，最终安全地
    回落至 ``range``；因此函数不会用未来数据补齐历史窗口。

    参数:
        benchmark: 以交易日为索引，至少包含 ``close`` 和 ``amount`` 的市场基准历史。
        breadth_history: 目标日前各交易日横截面 ``breadth_up`` 中位数。
        market_aggregates: 以交易日为索引，包含 ``limit_up``、``limit_down`` 的全市场聚合。
        as_of_date: 待标注的交易日。
    返回:
        包含状态名称和风险暴露乘数的 ``MarketRegime``。
    """
    normalized_date = pd.Timestamp(as_of_date)
    history = benchmark.copy()
    history.index = pd.to_datetime(history.index)
    history = history.loc[history.index <= normalized_date].sort_index()
    if history.empty or "close" not in history or "amount" not in history:
        return MarketRegime("range", 0.90)

    close = history["close"].astype(float)
    amount = history["amount"].astype(float)
    current_close = close.iloc[-1]
    ma20 = close.rolling(20, min_periods=20).mean().iloc[-1]
    ma60 = close.rolling(60, min_periods=60).mean().iloc[-1]

    breadth = breadth_history.copy()
    breadth.index = pd.to_datetime(breadth.index)
    current_breadth = breadth.loc[breadth.index <= normalized_date].tail(1)
    median_breadth = current_breadth.iloc[0] if not current_breadth.empty else float("nan")

    aggregates = market_aggregates.copy()
    aggregates.index = pd.to_datetime(aggregates.index)
    try:
        aggregate_row = _as_of_row(aggregates, normalized_date)
        limit_up = float(aggregate_row.get("limit_up", float("nan")))
        limit_down = float(aggregate_row.get("limit_down", float("nan")))
    except ValueError:
        limit_up = limit_down = float("nan")

    # 第一优先级：弱趋势、弱广度与限跌占优必须同时满足，避免单一指标误报。
    if current_close < ma60 and median_breadth < 0.45 and limit_down > limit_up:
        return MarketRegime("risk_off", 0.70)

    ret20 = close.pct_change(20).iloc[-1] if len(close) >= 21 else float("nan")
    rolling_vol = close.pct_change().rolling(20, min_periods=20).std()
    current_vol = rolling_vol.iloc[-1]
    vol_reference = rolling_vol.dropna().tail(252)
    vol_threshold = vol_reference.quantile(0.80) if not vol_reference.empty else float("nan")
    if abs(ret20) >= 0.08 or current_vol >= vol_threshold:
        return MarketRegime("high_volatility", 0.85)

    amount_ma20 = amount.rolling(20, min_periods=20).mean().iloc[-1]
    if current_close > ma20 > ma60 and median_breadth >= 0.55 and amount.iloc[-1] > amount_ma20:
        return MarketRegime("risk_on", 1.00)
    return MarketRegime("range", 0.90)
