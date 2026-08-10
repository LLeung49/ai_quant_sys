"""板块原始特征的纯计算函数。

本模块只计算特征，不访问数据库；数据加载与每日特征面板编排将在调用层完成。
"""
from __future__ import annotations

import logging
import pandas as pd

from .derivatives import macd_hist, ma_slope, relative_strength, rs_acceleration
from .data_loader import (
    build_market_benchmark,
    load_historical_sector_panel,
    load_historical_sector_stock_panel,
    load_sector_panel,
    load_sector_stock_amounts,
)


LOGGER = logging.getLogger(__name__)


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


def calculate_sector_features(
    sector_frame: pd.DataFrame,
    benchmark_frame: pd.DataFrame,
    market_amount: float,
    amount_share_history: pd.Series,
) -> dict[str, float]:
    """组合单板块价格、趋势和量能原始特征。

    参数:
        sector_frame: 含 close、amount 列且按交易日升序排列的板块历史表。
        benchmark_frame: 含 close 列的同期市场基准历史表。
        market_amount: 当前交易日全部有效板块成交额之和。
        amount_share_history: 当前日前的板块成交额份额历史序列。
    返回:
        可直接进入每日横截面评分的原始特征字典；窗口不足的指标保持 NaN。
    异常:
        KeyError: 任一输入表缺少必要的 close 或 amount 列时抛出。
    """
    if "close" not in sector_frame or "amount" not in sector_frame or "close" not in benchmark_frame:
        raise KeyError("sector_frame requires close/amount and benchmark_frame requires close")
    close = sector_frame["close"]
    amount = sector_frame["amount"]
    current_amount = amount.iloc[-1] if not amount.empty else float("nan")
    amount_share = calculate_amount_share(float(current_amount), market_amount)
    features = calculate_sector_price_features(close, benchmark_frame["close"])
    features.update(calculate_sector_trend_features(close, benchmark_frame["close"]))
    features.update({
        "rvol_5_20": calculate_rvol(amount, 5, 20),
        "rvol_5_60": calculate_rvol(amount, 5, 60),
        "amount_share": amount_share,
        "share_impulse": calculate_share_impulse(amount_share, amount_share_history),
    })
    return features


def calculate_historical_sector_features(sector_frame: pd.DataFrame, benchmark_frame: pd.DataFrame) -> pd.DataFrame:
    """一次滚动计算单行业全历史的价格、趋势和量能特征。"""
    close, amount = sector_frame["close"], sector_frame["amount"]
    benchmark_close, benchmark_amount = benchmark_frame["close"], benchmark_frame["amount"]
    ma20, ma60 = close.rolling(20, min_periods=20).mean(), close.rolling(60, min_periods=60).mean()
    rs5, rs20, rs60 = relative_strength(close, benchmark_close, 5), relative_strength(close, benchmark_close, 20), relative_strength(close, benchmark_close, 60)
    slope = ma_slope(close)
    share = amount / benchmark_amount.reindex(amount.index)
    return pd.DataFrame({
        "ret_5": close / close.shift(5) - 1.0,
        "ret_20": close / close.shift(20) - 1.0,
        "rs_5": rs5, "rs_20": rs20, "rs_60": rs60,
        "distance_ma20": close / ma20 - 1.0, "distance_ma60": close / ma60 - 1.0,
        "ma20_slope": slope, "rs20_accel": rs_acceleration(rs20, lag=5),
        "ma20_accel": slope - slope.shift(5), "macd_hist": macd_hist(close),
        "macd_hist_delta": macd_hist(close).diff(),
        "rvol_5_20": amount.rolling(5).mean() / amount.rolling(20).mean(),
        "rvol_5_60": amount.rolling(5).mean() / amount.rolling(60).mean(),
        "amount_share": share, "share_impulse": share / share.shift(1).rolling(20).mean(),
    }, index=close.index)


def calculate_stock_participation_features(stock_history: pd.DataFrame) -> dict[str, float]:
    """计算成分股层面的量能和价格参与度。

    参数:
        stock_history: 含 stock_code、trade_date、amount、close 的历史表；每只股票按日期计算 20 日指标。
    返回:
        含 median_stock_rvol、breadth_rvol、breadth_above_ma20、breadth_new_high_20 的字典；
        无足够有效成分股时对应字段为 NaN。
    异常:
        KeyError: 缺少必要列时抛出。
    """
    empty_result = {key: float("nan") for key in ("median_stock_rvol", "breadth_rvol", "breadth_above_ma20", "breadth_new_high_20")}
    # 个股数据源无返回行时，参与度不可计算但不能阻断板块价格特征输出。
    if stock_history.empty:
        return empty_result
    required = {"stock_code", "trade_date", "amount", "close"}
    missing = required.difference(stock_history.columns)
    if missing:
        raise KeyError(f"stock_history missing columns: {sorted(missing)}")
    latest_rows: list[dict[str, float]] = []
    for _, group in stock_history.sort_values(["stock_code", "trade_date"]).groupby("stock_code", sort=False):
        if len(group) < 20:
            continue
        amount_ma20 = group["amount"].rolling(20, min_periods=20).mean().iloc[-1]
        close_ma20 = group["close"].rolling(20, min_periods=20).mean().iloc[-1]
        high20 = group["close"].rolling(20, min_periods=20).max().iloc[-1]
        current_amount, current_close = group["amount"].iloc[-1], group["close"].iloc[-1]
        latest_rows.append({
            "stock_rvol": current_amount / amount_ma20 if amount_ma20 > 0 else float("nan"),
            "above_ma20": float(current_close > close_ma20) if pd.notna(close_ma20) else float("nan"),
            "new_high_20": float(current_close >= high20) if pd.notna(high20) else float("nan"),
        })
    latest = pd.DataFrame(latest_rows)
    if latest.empty:
        return empty_result
    return {
        "median_stock_rvol": float(latest["stock_rvol"].median()),
        "breadth_rvol": calculate_breadth_rvol(latest["stock_rvol"]),
        "breadth_above_ma20": float(latest["above_ma20"].mean()),
        "breadth_new_high_20": float(latest["new_high_20"].mean()),
    }


def calculate_historical_stock_participation(stock_history: pd.DataFrame) -> pd.DataFrame:
    """一次计算所有个股滚动指标，并按行业和交易日聚合参与度。"""
    columns = ["sector_name", "trade_date", "median_stock_rvol", "breadth_rvol", "breadth_above_ma20", "breadth_new_high_20"]
    if stock_history.empty:
        return pd.DataFrame(columns=columns)
    ordered = stock_history.sort_values(["stock_code", "trade_date"]).copy()
    groups = ordered.groupby("stock_code", sort=False)
    amount_ma20 = groups["amount"].transform(lambda values: values.rolling(20, min_periods=20).mean())
    close_ma20 = groups["close"].transform(lambda values: values.rolling(20, min_periods=20).mean())
    high20 = groups["close"].transform(lambda values: values.rolling(20, min_periods=20).max())
    valid = amount_ma20.notna() & close_ma20.notna() & high20.notna()
    enriched = ordered.loc[valid, ["sector_name", "trade_date"]].copy()
    enriched["stock_rvol"] = ordered.loc[valid, "amount"] / amount_ma20.loc[valid]
    enriched["above_ma20"] = (ordered.loc[valid, "close"] > close_ma20.loc[valid]).astype(float)
    enriched["new_high_20"] = (ordered.loc[valid, "close"] >= high20.loc[valid]).astype(float)
    if enriched.empty:
        return pd.DataFrame(columns=columns)
    return enriched.groupby(["sector_name", "trade_date"], as_index=False).agg(
        median_stock_rvol=("stock_rvol", "median"),
        breadth_rvol=("stock_rvol", lambda values: float((values > 1.0).mean())),
        breadth_above_ma20=("above_ma20", "mean"),
        breadth_new_high_20=("new_high_20", "mean"),
    )


def build_historical_feature_panels(level: int, start_date: str, end_date: str) -> dict[str, pd.DataFrame]:
    """用一次批量读取预计算目标区间每日特征面板。"""
    panel = load_historical_sector_panel(level, start_date, end_date)
    stock_panel = load_historical_sector_stock_panel(level, start_date, end_date)
    stock_participation = calculate_historical_stock_participation(stock_panel)
    benchmark = build_market_benchmark(panel)
    sector_features = {name: calculate_historical_sector_features(frame, benchmark) for name, frame in panel.items()}
    target_dates = benchmark.loc[(benchmark.index >= pd.Timestamp(start_date)) & (benchmark.index <= pd.Timestamp(end_date))].index
    result: dict[str, pd.DataFrame] = {}
    for target_date in target_dates:
        rows = {}
        for sector_name, frame in panel.items():
            history = frame.loc[:target_date]
            if len(history) < 90:
                continue
            features = sector_features[sector_name].loc[target_date].to_dict()
            participation = stock_participation.loc[
                (stock_participation["sector_name"] == sector_name) & (stock_participation["trade_date"] == target_date)
            ]
            if participation.empty:
                features.update({key: float("nan") for key in ("median_stock_rvol", "breadth_rvol", "breadth_above_ma20", "breadth_new_high_20")})
            else:
                features.update(participation.iloc[0].drop(labels=["sector_name", "trade_date"]).to_dict())
            latest = history.iloc[-1]
            denominator = latest.get("rise_count", 0) + latest.get("fall_count", 0) + latest.get("flat_count", 0)
            features.update({
                "coverage_ratio": float(latest.get("kline_stock_count") / latest.get("stock_count")) if latest.get("stock_count", 0) > 0 else float("nan"),
                "breadth_up": float(latest.get("rise_count", 0) / denominator) if denominator > 0 else float("nan"),
                "membership_asof_mode": "current_mapping",
            })
            rows[sector_name] = features
        result[target_date.strftime("%Y-%m-%d")] = pd.DataFrame.from_dict(rows, orient="index")
    return result


def build_daily_feature_panel(level: int, as_of_date: str, min_history_days: int = 90) -> pd.DataFrame:
    """构建指定交易日全部有效板块的原始特征横截面。

    参数:
        level: 申万行业层级。
        as_of_date: 特征计算截止交易日，格式 YYYY-MM-DD。
        min_history_days: 板块进入特征面板所需的最少历史行数。
    返回:
        以 sector_name 为索引的原始特征 DataFrame；无有效板块时返回空表。
    """
    panel = load_sector_panel(level=level, end_date=as_of_date, min_history_days=min_history_days)
    LOGGER.info("特征数据：已加载 %s 个有效板块，开始构建市场基准", len(panel))
    benchmark = build_market_benchmark(panel)
    if not panel or benchmark.empty:
        return pd.DataFrame()
    rows: dict[str, dict[str, float]] = {}
    date_strings = [date.strftime("%Y-%m-%d") for date in benchmark.index]
    total_sectors = len(panel)
    for position, (sector_name, frame) in enumerate(panel.items(), start=1):
        LOGGER.info("特征进度 %s/%s：%s（加载成分股历史并计算特征）", position, total_sectors, sector_name)
        share_history = frame["amount"].div(benchmark["amount"].reindex(frame.index))
        features = calculate_sector_features(frame, benchmark, float(benchmark["amount"].iloc[-1]), share_history.iloc[:-1])
        stock_history = load_sector_stock_amounts(sector_name, level, date_strings)
        features.update(calculate_stock_participation_features(stock_history))
        latest = frame.iloc[-1]
        stock_count = latest.get("stock_count", float("nan"))
        kline_count = latest.get("kline_stock_count", float("nan"))
        denominator = latest.get("rise_count", 0) + latest.get("fall_count", 0) + latest.get("flat_count", 0)
        features.update({
            "coverage_ratio": float(kline_count / stock_count) if pd.notna(stock_count) and stock_count > 0 else float("nan"),
            "breadth_up": float(latest.get("rise_count", 0) / denominator) if denominator > 0 else float("nan"),
            "membership_asof_mode": "current_mapping",
        })
        rows[sector_name] = features
    LOGGER.info("特征计算完成：已生成 %s 个板块的特征记录", len(rows))
    return pd.DataFrame.from_dict(rows, orient="index")


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
