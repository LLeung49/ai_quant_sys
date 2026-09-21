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

from data_ingestion_qmt.db_config import execute_query


@dataclass(frozen=True)
class FrameValidation:
    valid: bool
    reasons: tuple[str, ...]


def validate_sector_frame(frame: pd.DataFrame) -> FrameValidation:
    """校验板块进入排名前必须满足的最小数据不变量。

    参数:
        frame: 索引为交易日，至少包含 close 和 amount 列的板块历史 DataFrame。
    返回:
        含 valid 布尔值和全部失败原因的 FrameValidation 对象。
    """
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

    参数:
        sector_panel: 板块名到历史 DataFrame 的映射。
    返回:
        含 close、amount、eligible_sector_count 的市场基准 DataFrame；无有效板块时为空表。
    """
    eligible = {name: frame for name, frame in sector_panel.items() if validate_sector_frame(frame).valid}
    if not eligible:
        return pd.DataFrame(columns=["close", "amount", "eligible_sector_count"])
    # 归一到自身首个有效观察值，消除合成指数点位差异(frame["close"].iloc[0] 是当前这个板块历史 DataFrame 中，close 列的第一条有效收盘指数值)
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

    参数:
        level: 申万行业层级，1 为一级、2 为二级。
        start_date: 可选起始交易日，格式 YYYY-MM-DD。
        end_date: 可选截止交易日，格式 YYYY-MM-DD。
        min_history_days: 每个板块入选面板所需的最少历史行数。
    返回:
        板块名到按 trade_date 升序索引的有效历史 DataFrame 映射。
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
    # MySQL DECIMAL 通常以 decimal.Decimal 返回；在数据边界统一转为 float，
    # 避免后续 Pandas 收益率、均线和横截面运算与 float 基准混算时报类型错误。
    numeric_columns = [column for column in frame.columns if column not in {"sector_name", "trade_date"}]
    frame[numeric_columns] = frame[numeric_columns].apply(pd.to_numeric, errors="coerce")
    panel: dict[str, pd.DataFrame] = {}
    for sector_name, group in frame.groupby("sector_name", sort=True):
        sector_frame = group.drop(columns="sector_name").set_index("trade_date").sort_index()
        if len(sector_frame) >= min_history_days and validate_sector_frame(sector_frame).valid:
            panel[str(sector_name)] = sector_frame
    return panel


def load_historical_sector_panel(level: int, start_date: str, end_date: str, warmup_days: int = 90) -> dict[str, pd.DataFrame]:
    """一次读取目标区间及预热日的全部有效行业历史面板。"""
    sql = """
        WITH selected_dates AS (
            SELECT DISTINCT trade_date FROM trade_sector_daily
            WHERE sector_level = %s AND trade_date BETWEEN %s AND %s
            UNION
            SELECT trade_date FROM (
                SELECT DISTINCT trade_date FROM trade_sector_daily
                WHERE sector_level = %s AND trade_date < %s
                ORDER BY trade_date DESC LIMIT %s
            ) warmup
        )
        SELECT sector_name, trade_date, close_idx AS close, total_amount AS amount,
               stock_count, kline_stock_count, rise_count, fall_count, flat_count, limit_up, limit_down
        FROM trade_sector_daily
        WHERE sector_level = %s AND trade_date IN (SELECT trade_date FROM selected_dates)
        ORDER BY sector_name, trade_date
    """
    rows = execute_query(sql, (level, start_date, end_date, level, start_date, warmup_days, level))
    frame = pd.DataFrame(rows)
    if frame.empty:
        return {}
    frame["trade_date"] = pd.to_datetime(frame["trade_date"])
    numeric_columns = [column for column in frame.columns if column not in {"sector_name", "trade_date"}]
    frame[numeric_columns] = frame[numeric_columns].apply(pd.to_numeric, errors="coerce")
    return {
        str(name): group.drop(columns="sector_name").set_index("trade_date").sort_index()
        for name, group in frame.groupby("sector_name", sort=True)
    }


def load_historical_sector_stock_panel(level: int, start_date: str, end_date: str, warmup_days: int = 20) -> pd.DataFrame:
    """一次读取所有当前行业成员的目标区间及预热个股历史。"""
    field = "sector_1" if level == 1 else "sector_2"
    sql = f"""
        WITH selected_dates AS (
            SELECT DISTINCT trade_date FROM trade_sector_daily
            WHERE sector_level = %s AND trade_date BETWEEN %s AND %s
            UNION
            SELECT trade_date FROM (
                SELECT DISTINCT trade_date FROM trade_sector_daily
                WHERE sector_level = %s AND trade_date < %s
                ORDER BY trade_date DESC LIMIT %s
            ) warmup
        )
        SELECT status.{field} AS sector_name, daily.stock_code, daily.trade_date,
               daily.amount, daily.close_price AS close
        FROM trade_stock_daily_qfq AS daily
        INNER JOIN trade_stock_status AS status ON status.stock_code = daily.stock_code
        WHERE status.{field} IS NOT NULL AND daily.trade_date IN (SELECT trade_date FROM selected_dates)
        ORDER BY status.{field}, daily.stock_code, daily.trade_date
    """
    rows = execute_query(sql, (level, start_date, end_date, level, start_date, warmup_days))
    frame = pd.DataFrame(rows, columns=["sector_name", "stock_code", "trade_date", "amount", "close"])
    if not frame.empty:
        frame["trade_date"] = pd.to_datetime(frame["trade_date"])
        frame[["amount", "close"]] = frame[["amount", "close"]].apply(pd.to_numeric, errors="coerce")
    frame["membership_asof_mode"] = "current_mapping"
    return frame


def load_sector_stock_amounts(
    sector_name: str,
    level: int,
    trade_dates: list[str],
) -> pd.DataFrame:
    """加载当前行业成员的只读日成交额/收盘面板，用于广度计算。

v1 明确使用当前行业映射，这是回测口径限制；返回结果因此逐行标记
``membership_asof_mode=current_mapping``，供快照与报告披露。

    参数:
        sector_name: 待查询的行业名称。
        level: 申万行业层级，用于选择 sector_1 或 sector_2 映射列。
        trade_dates: 需要查询的交易日字符串列表。
    返回:
        含 stock_code、trade_date、amount、close、membership_asof_mode 的 DataFrame。
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
        result[["amount", "close"]] = result[["amount", "close"]].apply(pd.to_numeric, errors="coerce")
    result["membership_asof_mode"] = "current_mapping"
    return result


def load_market_aggregates(sector_panel: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """从有效板块历史聚合涨跌停、成交额和上涨广度中位数。

上涨广度取板块中位数，避免超大板块主导市场状态信号；涨跌停家数与成交额
仍按市场总量求和。

    参数:
        sector_panel: 板块名到历史 DataFrame 的映射，仅有效板块参与聚合。
    返回:
        以交易日为索引、含 amount、limit_up、limit_down、breadth_up_median 的 DataFrame。
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

