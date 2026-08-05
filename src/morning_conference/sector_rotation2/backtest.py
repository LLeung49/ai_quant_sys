"""构建交易日前瞻标签并评估板块横截面因子。"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from .data_loader import build_market_benchmark, load_sector_panel


def make_forward_labels(close: pd.Series, horizon: int, benchmark_close: pd.Series | None = None) -> pd.DataFrame:
    """用索引中的未来第 N 个交易日生成收益标签。

    参数:
        close: 日期索引的单板块收盘序列。
        horizon: 向后推进的交易日数量，必须为正整数。
        benchmark_close: 可选的同日期市场基准收盘序列；提供后计算超额收益。
    返回:
        索引为起始交易日，含 target_date、sector_return、benchmark_return、
        excess_return 的标签 DataFrame；尾部未成熟样本自动丢弃。
    """
    if horizon <= 0:
        raise ValueError("horizon 必须为正整数")
    series = close.dropna().sort_index()
    rows = []
    for position in range(len(series) - horizon):
        as_of_date, target_date = series.index[position], series.index[position + horizon]
        sector_return = series.iloc[position + horizon] / series.iloc[position] - 1.0
        benchmark_return = np.nan
        if benchmark_close is not None and as_of_date in benchmark_close.index and target_date in benchmark_close.index:
            benchmark_return = benchmark_close.loc[target_date] / benchmark_close.loc[as_of_date] - 1.0
        rows.append((as_of_date, target_date, sector_return, benchmark_return, sector_return - benchmark_return))
    return pd.DataFrame(rows, columns=["as_of_date", "target_date", "sector_return", "benchmark_return", "excess_return"]).set_index("as_of_date")


def build_forward_return_labels(level: int, start_date: str, end_date: str, horizons: tuple[int, ...] = (5, 10)) -> pd.DataFrame:
    """从只读板块历史构建指定区间内所有已成熟的前瞻收益标签。

    参数:
        level: 申万行业层级。
        start_date: 标签起始交易日。
        end_date: 标签起始交易日结束边界。
        horizons: 以交易日计的预测周期元组。
    返回:
        包含板块、起始日、目标日、周期、板块/基准/超额收益的标签 DataFrame。
    """
    panel = load_sector_panel(level=level, start_date=start_date, end_date=None, min_history_days=1)
    benchmark = build_market_benchmark(panel)
    rows: list[pd.DataFrame] = []
    for sector_name, frame in panel.items():
        for horizon in horizons:
            labels = make_forward_labels(frame["close"], horizon, benchmark.get("close"))
            labels = labels.loc[(labels.index >= pd.Timestamp(start_date)) & (labels.index <= pd.Timestamp(end_date))].copy()
            labels["sector_name"] = sector_name
            labels["horizon"] = horizon
            rows.append(labels.reset_index())
    if not rows:
        return pd.DataFrame(columns=["as_of_date", "sector_name", "horizon", "target_date", "sector_return", "benchmark_return", "excess_return"])
    return pd.concat(rows, ignore_index=True).sort_values(["as_of_date", "sector_name", "horizon"])


def _validate_unique(frame: pd.DataFrame, name: str) -> None:
    """验证评估输入按日期和板块唯一。

    参数:
        frame: 待验证的快照或标签表。
        name: 供异常信息使用的数据集名称。
    返回:
        无；不重复时正常返回。
    异常:
        ValueError: 缺少键列或出现重复键时抛出。
    """
    keys = ["as_of_date", "sector_name"]
    if not set(keys).issubset(frame):
        raise ValueError(f"{name} 缺少唯一键列")
    if frame.duplicated(keys).any():
        raise ValueError(f"{name} 存在重复日期/板块键")


def evaluate_factor(snapshots: pd.DataFrame, labels: pd.DataFrame, factor: str, horizon: int) -> dict[str, float]:
    """计算因子与指定期限超额收益的截面 IC 和五分组结果。

    参数:
        snapshots: 含日期、板块和待评估因子的日快照。
        labels: 含日期、板块、目标日期、期限和超额收益的前瞻标签。
        factor: 快照中作为因子的数值列名。
        horizon: 要评估的标签交易日周期。
    返回:
        包含 Pearson/Rank IC 均值、ICIR、五分组收益、Top-Bottom、样本数的字典。
    """
    _validate_unique(snapshots, "快照")
    _validate_unique(labels, "标签")
    if factor not in snapshots:
        raise ValueError(f"快照缺少因子列: {factor}")
    selected = labels.loc[labels["horizon"] == horizon].copy()
    if (pd.to_datetime(selected["target_date"]) <= pd.to_datetime(selected["as_of_date"])).any():
        raise ValueError("标签 target_date 必须晚于 as_of_date")
    merged = snapshots[["as_of_date", "sector_name", factor]].merge(
        selected[["as_of_date", "sector_name", "excess_return"]], on=["as_of_date", "sector_name"], how="inner"
    ).dropna()
    if merged.empty:
        return {"ic_mean": np.nan, "rank_ic_mean": np.nan, "icir": np.nan, "top_group_return": np.nan,
                "bottom_group_return": np.nan, "top_bottom_return": np.nan, "sample_count": 0}
    daily_ic = merged.groupby("as_of_date").apply(lambda group: group[factor].corr(group["excess_return"]), include_groups=False)
    # 采用 scipy 的标准 Spearman 实现；常数截面会返回 NaN，随后由均值计算自然忽略。
    daily_rank_ic = merged.groupby("as_of_date").apply(
        lambda group: spearmanr(group[factor], group["excess_return"]).statistic,
        include_groups=False,
    )
    group_returns = []
    for _, group in merged.groupby("as_of_date"):
        if group[factor].nunique() < 5:
            continue
        quantile = pd.qcut(group[factor], 5, labels=False, duplicates="drop")
        group_returns.append((group.loc[quantile == quantile.max(), "excess_return"].mean(), group.loc[quantile == quantile.min(), "excess_return"].mean()))
    top = float(np.mean([item[0] for item in group_returns])) if group_returns else np.nan
    bottom = float(np.mean([item[1] for item in group_returns])) if group_returns else np.nan
    return {"ic_mean": daily_ic.mean(), "rank_ic_mean": daily_rank_ic.mean(),
            "icir": daily_ic.mean() / daily_ic.std(ddof=1) if len(daily_ic) > 1 and daily_ic.std(ddof=1) else np.nan,
            "top_group_return": top, "bottom_group_return": bottom, "top_bottom_return": top - bottom,
            "sample_count": int(len(merged))}
