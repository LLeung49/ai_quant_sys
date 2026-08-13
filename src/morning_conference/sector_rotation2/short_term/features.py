"""v2_short_term 短期原始特征的纯计算函数。

本模块只计算特征，不直接访问数据库；调用方需要在传入前准备好板块日 K 线
与对应成分股面板。算法定义与字段语义严格对齐
《sector_rotation2_short_term_v2_plan.md》第 4 节。
"""
from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from ..data_loader import build_market_benchmark, load_sector_panel, load_sector_stock_amounts


LOGGER = logging.getLogger(__name__)


# ----- 通用工具 -----------------------------------------------------------------


def _safe_float(value: object) -> float:
    """把 Pandas 标量安全转换为 ``float``，缺失返回 NaN。"""
    if value is None:
        return float("nan")
    try:
        result = float(value)
    except (TypeError, ValueError):
        return float("nan")
    return result


def _previous_value(series: pd.Series, lag: int) -> float:
    """读取序列倒数第 ``lag`` 个有效值；越界或缺失返回 NaN。"""
    if lag <= 0 or len(series) <= lag:
        return float("nan")
    return _safe_float(series.iloc[-lag - 1])


def _streak(flag_series: pd.Series | None, max_days: int) -> int:
    """从序列末尾向前数连续 ``True`` 的天数，上限 ``max_days``。

    入参允许为 ``None``、空 ``Series``、单值；非 ``Series`` 输入会被强制转换，
    避免调用方传错类型时崩溃。
    """
    if flag_series is None:
        return 0
    if not isinstance(flag_series, pd.Series):
        flag_series = pd.Series([bool(flag_series)])
    if flag_series.empty:
        return 0
    streak = 0
    for value in flag_series.iloc[::-1]:
        if bool(value):
            streak += 1
            if streak >= max_days:
                return max_days
        else:
            break
    return streak


def _breadth_up_series(extras: pd.DataFrame) -> pd.Series:
    """从板块日线的 rise/fall/flat 计算每日 ``breadth_up``，与 v1 口径一致。"""
    if extras is None or extras.empty:
        return pd.Series(dtype=float)
    rise = pd.to_numeric(extras.get("rise_count"), errors="coerce").fillna(0)
    fall = pd.to_numeric(extras.get("fall_count"), errors="coerce").fillna(0)
    flat = pd.to_numeric(extras.get("flat_count"), errors="coerce").fillna(0)
    denom = rise + fall + flat
    safe_denom = denom.where(denom > 0)
    return (rise / safe_denom).replace([np.inf, -np.inf], np.nan)


# ----- 板块层短期特征 -----------------------------------------------------------


def calculate_sector_short_term_features(
    close: pd.Series,
    benchmark_close: pd.Series,
    amount: pd.Series,
    benchmark_amount: pd.Series,
    member_amount_history: pd.DataFrame | None,
    config,
    sector_daily_extras: pd.DataFrame | None = None,
) -> dict[str, float]:
    """计算单个板块的短期原始特征。

    参数:
        close: 按交易日升序的板块收盘指数序列。
        benchmark_close: 同期市场基准收盘序列。
        amount: 板块成交额序列。
        benchmark_amount: 市场基准成交额序列。
        member_amount_history: 含 ``stock_code``、``trade_date``、``amount``、``close``
            （可选 high/low）的个股面板；缺省时 ``breadth_above_ma5`` 等需要个股的字段返回 NaN。
        config: ``ModelConfigShortTerm`` 实例。
        sector_daily_extras: 板块日线的扩展列，至少含 ``limit_up``、``limit_down``、
            ``rise_count``、``fall_count``、``flat_count``；缺省时涨跌停与上涨广度返回 NaN。
    返回:
        与计划文档 §4 对齐的字段字典；任何窗口不足时对应字段为 NaN。
    """
    streak_cap = int(config.streak_max_days)
    ret_1 = _safe_float(close.iloc[-1] / _previous_value(close, 1) - 1.0) if len(close) >= 2 else float("nan")
    ret_2 = _safe_float(close.iloc[-1] / _previous_value(close, 2) - 1.0) if len(close) >= 3 else float("nan")
    ret_3 = _safe_float(close.iloc[-1] / _previous_value(close, 3) - 1.0) if len(close) >= 4 else float("nan")

    # 相对强度：板块 ret_n 减去基准 ret_n；n 取 1、2。
    rs_1 = float("nan")
    rs_2 = float("nan")
    if len(close) >= 2 and len(benchmark_close) >= 2:
        bench_ret_1 = _safe_float(
            benchmark_close.iloc[-1] / _previous_value(benchmark_close, 1) - 1.0
        )
        if not np.isnan(bench_ret_1):
            rs_1 = ret_1 - bench_ret_1
    if len(close) >= 3 and len(benchmark_close) >= 3:
        bench_ret_2 = _safe_float(
            benchmark_close.iloc[-1] / _previous_value(benchmark_close, 2) - 1.0
        )
        if not np.isnan(bench_ret_2):
            rs_2 = ret_2 - bench_ret_2

    # 5 日相对强度的 1 日变化：rs_5 当日 - rs_5 昨日。
    rs5_accel_1d = float("nan")
    if len(close) >= 6 and len(benchmark_close) >= 6:
        def _rs5(window_close: pd.Series, window_bench: pd.Series) -> float:
            if len(window_close) < 6 or len(window_bench) < 6:
                return float("nan")
            sector_ret = window_close.iloc[-1] / window_close.iloc[-6] - 1.0
            bench_ret = window_bench.iloc[-1] / window_bench.iloc[-6] - 1.0
            return _safe_float(sector_ret - bench_ret)

        rs5_accel_1d = _rs5(close, benchmark_close) - _rs5(close.iloc[:-1], benchmark_close.iloc[:-1])

    # ma5_slope：MA5 末日 - 前一日值。
    ma5 = close.rolling(5, min_periods=5).mean() if len(close) >= 5 else pd.Series(dtype=float)
    ma5_slope = _safe_float(ma5.iloc[-1] - ma5.iloc[-2]) if len(ma5) >= 2 else float("nan")

    # 量能与份额脉冲。
    rvol_1_20 = float("nan")
    rvol_1_60 = float("nan")
    amount_share_today = float("nan")
    share_impulse_1d = float("nan")
    if len(amount) >= 20 and len(benchmark_amount) >= 20:
        baseline_20 = amount.iloc[-20:].mean()
        if pd.notna(baseline_20) and baseline_20 > 0:
            rvol_1_20 = _safe_float(amount.iloc[-1] / baseline_20)
        market_baseline_20 = benchmark_amount.iloc[-20:].mean()
        if pd.notna(market_baseline_20) and market_baseline_20 > 0:
            amount_share_today = _safe_float(amount.iloc[-1] / market_baseline_20)
    if len(amount) >= 21 and len(benchmark_amount) >= 21:
        # share_impulse_1d：当日份额 / 昨日份额。
        today_share = _safe_float(amount.iloc[-1] / benchmark_amount.iloc[-1])
        yesterday_share = _safe_float(amount.iloc[-2] / benchmark_amount.iloc[-2])
        if today_share > 0 and yesterday_share > 0:
            share_impulse_1d = _safe_float(today_share / yesterday_share)
    if len(amount) >= 60 and len(benchmark_amount) >= 60:
        baseline_60 = amount.iloc[-60:].mean()
        if pd.notna(baseline_60) and baseline_60 > 0:
            rvol_1_60 = _safe_float(amount.iloc[-1] / baseline_60)

    # 连续性：ret_1 > 0 连续天数（基于板块收盘）。``pct_change`` 首日是 NaN，
    # 从 idx=1 开始看，避免首日把 streak 截断。
    if len(close) >= 2:
        ret_series = close.pct_change().iloc[1:]
        streak_pos_ret = _streak(ret_series > 0, streak_cap)
    else:
        streak_pos_ret = 0

    # —— 板块日线扩展字段：涨跌停占比、上涨广度、连续涨停天数 ——————————
    limit_up_ratio = float("nan")
    limit_down_ratio = float("nan")
    streak_top_limit_up = 0
    breadth_up = float("nan")
    streak_high_breadth = 0
    if sector_daily_extras is not None and not sector_daily_extras.empty:
        latest = sector_daily_extras.iloc[-1]
        total_house = (
            float(latest.get("rise_count", 0) or 0)
            + float(latest.get("fall_count", 0) or 0)
            + float(latest.get("flat_count", 0) or 0)
        )
        if total_house > 0:
            limit_up = float(latest.get("limit_up", 0) or 0)
            limit_down = float(latest.get("limit_down", 0) or 0)
            limit_up_ratio = _safe_float(limit_up / total_house)
            limit_down_ratio = _safe_float(limit_down / total_house)
        streak_top_limit_up = _streak(
            pd.to_numeric(sector_daily_extras.get("limit_up"), errors="coerce").fillna(0) >= 1,
            streak_cap,
        )
        breadth_up_series = _breadth_up_series(sector_daily_extras)
        if not breadth_up_series.empty:
            last_value = breadth_up_series.iloc[-1]
            breadth_up = _safe_float(last_value)
        streak_high_breadth = _streak(breadth_up_series.dropna() > 0.5, streak_cap)

    # —— 个股层面广度（来自 ``member_amount_history``） ————————————————————
    breadth_features = _calculate_member_breadth_features(
        member_amount_history,
        streak_cap,
        int(config.min_member_samples),
    )

    features = {
        "ret_1": ret_1,
        "ret_2": ret_2,
        "ret_3": ret_3,
        "rs_1": rs_1,
        "rs_2": rs_2,
        "rs5_accel_1d": rs5_accel_1d,
        "ma5_slope": ma5_slope,
        "rvol_1_20": rvol_1_20,
        "rvol_1_60": rvol_1_60,
        "amount_share_today": amount_share_today,
        "share_impulse_1d": share_impulse_1d,
        "breadth_up": breadth_up,
        "limit_up_ratio": limit_up_ratio,
        "limit_down_ratio": limit_down_ratio,
        "streak_pos_ret": int(streak_pos_ret),
        "streak_high_breadth": int(streak_high_breadth),
        "streak_top_limit_up": int(streak_top_limit_up),
    }
    features.update(breadth_features)
    return features


def _calculate_member_breadth_features(
    member_amount_history: pd.DataFrame | None,
    streak_cap: int,
    min_member_samples: int,
) -> dict[str, float]:
    """从个股面板计算 ``breadth_above_ma5``、``breadth_new_high_5`` 等需要个股的字段。

    注意：``breadth_up`` 与 ``streak_high_breadth`` 已从板块日线计算（与 v1 口径一致），
    本函数不重复计算。
    """
    empty = {
        "breadth_above_ma5": float("nan"),
        "breadth_new_high_5": float("nan"),
        "breadth_strong_1d": float("nan"),
        "breadth_weak_1d": float("nan"),
        "breadth_rvol_1d": float("nan"),
        "intraday_range": float("nan"),
        "ret_dispersion": float("nan"),
    }
    if member_amount_history is None or member_amount_history.empty:
        return empty
    if "close" not in member_amount_history.columns:
        return empty

    history = member_amount_history.copy()
    history["trade_date"] = pd.to_datetime(history["trade_date"])
    history = history.sort_values(["stock_code", "trade_date"])

    latest_date = history["trade_date"].max()
    today = history[history["trade_date"] == latest_date].dropna(subset=["close"])
    today_count = len(today)
    if today_count < min_member_samples:
        result = {key: float("nan") for key in (
            "breadth_above_ma5", "breadth_new_high_5",
            "breadth_strong_1d", "breadth_weak_1d", "breadth_rvol_1d",
        )}
    else:
        # 按个股计算 ret_1、MA5、5 日新高、MA20 量能。
        history["ret_1"] = history.groupby("stock_code")["close"].pct_change()
        today = today.copy()
        today["ret_1"] = today["close"].pct_change()
        ma5 = today["close"].rolling(5, min_periods=5).mean()
        new_high5 = today["close"].rolling(5, min_periods=5).max()
        amount_ma20 = today["amount"].rolling(20, min_periods=5).mean()
        result = {
            "breadth_above_ma5": _safe_float((today["close"] > ma5).sum() / today_count),
            "breadth_new_high_5": _safe_float((today["close"] >= new_high5).sum() / today_count),
            "breadth_strong_1d": _safe_float((today["ret_1"] > 0.05).sum() / today_count),
            "breadth_weak_1d": _safe_float((today["ret_1"] < -0.05).sum() / today_count),
            "breadth_rvol_1d": _safe_float((today["amount"] / amount_ma20 > 1.5).sum() / today_count),
        }

    intraday_range = float("nan")
    if {"high_price", "low_price"}.issubset(history.columns):
        latest_day = history[history["trade_date"] == latest_date].dropna(subset=["close", "high_price", "low_price"])
        if len(latest_day) >= min_member_samples:
            intraday_range = _safe_float(((latest_day["high_price"] - latest_day["low_price"]) / latest_day["close"]).mean())

    ret_dispersion = float("nan")
    today_ret = today.get("ret_1") if today_count >= min_member_samples else None
    if today_ret is not None and today_ret.notna().any():
        ret_dispersion = _safe_float(today_ret.std())

    result.update({
        "intraday_range": intraday_range,
        "ret_dispersion": ret_dispersion,
    })
    return result


# ----- 横截面编排 ---------------------------------------------------------------


def build_short_term_features(level: int, as_of_date: str, config, *, panel: dict[str, pd.DataFrame] | None = None) -> pd.DataFrame:
    """构建指定交易日全板块的短期原始特征横截面。

    参数:
        level: 申万行业层级，1 或 2。
        as_of_date: 目标交易日。
        config: ``ModelConfigShortTerm`` 实例。
        panel: 可选的预加载板块面板；若为 ``None`` 则按 ``level`` 与 ``as_of_date`` 自动加载。
    返回:
        以 ``sector_name`` 为索引的原始特征 DataFrame；无有效板块时返回空表。
    """
    if panel is None:
        # 复用 v1 的面板加载，但额外多取 60 个交易日以满足 ``rvol_1_60`` 窗口。
        panel = load_sector_panel(level=level, end_date=as_of_date, min_history_days=70)
    benchmark = build_market_benchmark(panel)
    if not panel or benchmark.empty:
        return pd.DataFrame()
    rows: dict[str, dict[str, float]] = {}
    total = len(panel)
    for index, (sector_name, frame) in enumerate(panel.items(), start=1):
        LOGGER.info("短期特征进度 %s/%s：%s", index, total, sector_name)
        date_strings = [d.strftime("%Y-%m-%d") for d in frame.index]
        stock_history = load_sector_stock_amounts(sector_name, level, date_strings)
        rows[sector_name] = calculate_sector_short_term_features(
            close=frame["close"],
            benchmark_close=benchmark["close"],
            amount=frame["amount"],
            benchmark_amount=benchmark["amount"],
            member_amount_history=stock_history,
            sector_daily_extras=frame,
            config=config,
        )
    LOGGER.info("短期特征计算完成：%s 个板块", len(rows))
    return pd.DataFrame.from_dict(rows, orient="index")


def calculate_stock_short_term_features(stock_history: pd.DataFrame, config) -> dict[str, float]:
    """在已知个股面板的前提下计算板块短期个股层面指标。

    此函数是 ``build_short_term_features`` 的辅助接口，主要为单元测试与
    回放场景提供确定性输入，避免依赖数据库。

    注：``breadth_up`` 与 ``streak_high_breadth`` 需要板块日线扩展字段
    （``rise_count`` 等），因此本函数返回 NaN。
    """
    return _calculate_member_breadth_features(
        stock_history,
        int(config.streak_max_days),
        int(config.min_member_samples),
    )