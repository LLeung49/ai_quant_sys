"""板块原始特征的纯计算函数。

本模块只计算特征，不访问数据库；数据加载与每日特征面板编排将在调用层完成。
"""
from __future__ import annotations

import pandas as pd


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
