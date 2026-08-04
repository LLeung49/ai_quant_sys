# 参考并改造自 sector_rotation/sector_loader.py。
# 差异：构建基准前先校验板块数据，且绝不导入旧包。
"""sector_rotation2 的只读数据加载与数据质量检查。

这里的 SQL 均为只读；调用方可以记录异常板块原因，但异常历史不会进入
横截面基准和可排名样本。
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import pandas as pd

from data_ingestion.db_config import execute_query


@dataclass(frozen=True)
class FrameValidation:
    valid: bool
    reasons: tuple[str, ...]


def validate_sector_frame(frame: pd.DataFrame) -> FrameValidation:
    """校验板块进入排名前必须满足的最小数据不变量。"""
    reasons: list[str] = []
    required = {"close", "amount"}
    missing = required.difference(frame.columns)
    if missing:
        reasons.append("missing_required_columns")
    if not isinstance(frame.index, pd.DatetimeIndex):
        reasons.append("invalid_trade_date_index")
    else:
        if frame.index.has_duplicates:
            reasons.append("duplicate_trade_date")
        if not frame.index.is_monotonic_increasing:
            reasons.append("unsorted_trade_date")
    if "close" in frame and (pd.to_numeric(frame["close"], errors="coerce") <= 0).any():
        reasons.append("nonpositive_close")
    if "amount" in frame and (pd.to_numeric(frame["amount"], errors="coerce") < 0).any():
        reasons.append("negative_amount")
    return FrameValidation(valid=not reasons, reasons=tuple(reasons))


def build_market_benchmark(sector_panel: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """仅以有效板块构建等权价格、成交额求和的市场基准。

每个板块收盘先归一到自身首个有效观察值，消除合成指数点位差异；
成交额按市场实际规模求和而非平均。
"""
    eligible = {name: frame for name, frame in sector_panel.items() if validate_sector_frame(frame).valid}
    if not eligible:
        return pd.DataFrame(columns=["close", "amount", "eligible_sector_count"])
    normalized = [frame["close"] / frame["close"].iloc[0] for frame in eligible.values()]
    amounts = [frame["amount"] for frame in eligible.values()]
    return pd.DataFrame({
        "close": pd.concat(normalized, axis=1).mean(axis=1) * 1000.0,
        "amount": pd.concat(amounts, axis=1).sum(axis=1),
        "eligible_sector_count": len(eligible),
    })


def load_sector_panel(
    level: int,
    start_date: str | None = None,
    end_date: str | None = None,
    min_history_days: int = 60,
) -> dict[str, pd.DataFrame]:
    """从 ``trade_sector_daily`` 只读加载板块历史面板。

日期筛选先在 SQL 完成以减少载入量；随后按板块独立校验，因此单个异常历史
不会污染市场基准或可排名样本集合。
"""
    conditions = ["sector_level = %s"]
    params: list[object] = [level]
    if start_date:
        conditions.append("trade_date >= %s")
        params.append(start_date)
    if end_date:
        conditions.append("trade_date <= %s")
        params.append(end_date)
    sql = f"""
        SELECT sector_name, trade_date, close_idx AS close, total_amount AS amount,
               stock_count, kline_stock_count, rise_count, fall_count, flat_count,
               limit_up, limit_down
        FROM trade_sector_daily
        WHERE {' AND '.join(conditions)}
        ORDER BY sector_name ASC, trade_date ASC
    """
    rows = execute_query(sql, params)
    if not rows:
        return {}
    frame = pd.DataFrame(rows)
    frame["trade_date"] = pd.to_datetime(frame["trade_date"])
    panel: dict[str, pd.DataFrame] = {}
    for sector_name, group in frame.groupby("sector_name", sort=True):
        sector_frame = group.drop(columns="sector_name").set_index("trade_date").sort_index()
        if len(sector_frame) >= min_history_days and validate_sector_frame(sector_frame).valid:
            panel[str(sector_name)] = sector_frame
    return panel


def load_sector_stock_amounts(
    sector_name: str,
    level: int,
    trade_dates: list[str],
) -> pd.DataFrame:
    """加载当前行业成员的只读日成交额/收盘面板，用于广度计算。

v1 明确使用当前行业映射，这是回测口径限制；返回结果因此逐行标记
``membership_asof_mode=current_mapping``，供快照与报告披露。
"""
    if not trade_dates:
        return pd.DataFrame(columns=["stock_code", "trade_date", "amount", "close", "membership_asof_mode"])
    field = "sector_1" if level == 1 else "sector_2"
    placeholders = ", ".join(["%s"] * len(trade_dates))
    sql = f"""
        SELECT daily.stock_code, daily.trade_date, daily.amount, daily.close_price AS close
        FROM trade_stock_daily_qfq AS daily
        INNER JOIN trade_stock_status AS status ON status.stock_code = daily.stock_code
        WHERE status.{field} = %s AND daily.trade_date IN ({placeholders})
        ORDER BY daily.trade_date ASC, daily.stock_code ASC
    """
    rows = execute_query(sql, [sector_name, *trade_dates])
    result = pd.DataFrame(rows, columns=["stock_code", "trade_date", "amount", "close"])
    if not result.empty:
        result["trade_date"] = pd.to_datetime(result["trade_date"])
    result["membership_asof_mode"] = "current_mapping"
    return result


def load_market_aggregates(sector_panel: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """从有效板块历史聚合涨跌停、成交额和上涨广度中位数。

上涨广度取板块中位数，避免超大板块主导市场状态信号；涨跌停家数与成交额
仍按市场总量求和。
"""
    eligible = [frame for frame in sector_panel.values() if validate_sector_frame(frame).valid]
    if not eligible:
        return pd.DataFrame(columns=["amount", "limit_up", "limit_down", "breadth_up_median"])
    combined = pd.concat(eligible, keys=range(len(eligible)), names=["sector", "trade_date"])
    combined["breadth_up"] = combined["rise_count"] / (
        combined["rise_count"] + combined["fall_count"] + combined["flat_count"]
    )
    return combined.groupby(level="trade_date").agg(
        amount=("amount", "sum"), limit_up=("limit_up", "sum"),
        limit_down=("limit_down", "sum"), breadth_up_median=("breadth_up", "median"),
    )
