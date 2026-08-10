"""构建交易日前瞻标签并评估板块横截面因子。"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from .data_loader import build_market_benchmark, load_sector_panel


DEFAULT_ALPHA_DECAY_HORIZONS = (1, 2, 3, 5, 10, 20, 40)


def evaluate_lifecycle_states(snapshots: pd.DataFrame, labels: pd.DataFrame, horizon: int) -> pd.DataFrame:
    """按 Lifecycle 状态统计同一 Score 快照日可得的成熟前瞻超额收益。"""
    selected = labels.loc[labels["horizon"] == horizon, ["as_of_date", "sector_name", "excess_return"]]
    merged = snapshots[["as_of_date", "sector_name", "lifecycle_state"]].merge(
        selected, on=["as_of_date", "sector_name"], how="inner"
    ).dropna(subset=["lifecycle_state", "excess_return"])
    if merged.empty:
        return pd.DataFrame(columns=["lifecycle_state", "mean_excess_return", "sample_count"])
    return merged.groupby("lifecycle_state", as_index=False).agg(
        mean_excess_return=("excess_return", "mean"), sample_count=("excess_return", "size")
    )


def evaluate_lifecycle_score_buckets(snapshots: pd.DataFrame, labels: pd.DataFrame, horizon: int) -> pd.DataFrame:
    """在每日 Score 五分位内统计 Lifecycle 的成熟前瞻超额收益。"""
    required_snapshot_columns = {"as_of_date", "sector_name", "composite_score", "lifecycle_state"}
    if not required_snapshot_columns.issubset(snapshots):
        raise ValueError("快照缺少 Lifecycle 条件收益所需列")
    selected = labels.loc[labels["horizon"] == horizon, ["as_of_date", "sector_name", "excess_return"]].copy()
    _validate_unique(snapshots, "快照")
    _validate_unique(selected, "标签")
    merged = snapshots[["as_of_date", "sector_name", "composite_score", "lifecycle_state"]].merge(
        selected, on=["as_of_date", "sector_name"], how="inner"
    ).dropna(subset=["lifecycle_state", "composite_score", "excess_return"])
    merged["composite_score"] = pd.to_numeric(merged["composite_score"], errors="coerce")
    merged["excess_return"] = pd.to_numeric(merged["excess_return"], errors="coerce")
    merged = merged.dropna(subset=["composite_score", "excess_return"])
    if merged.empty:
        return pd.DataFrame(columns=["score_bucket", "lifecycle_state", "mean_excess_return", "sample_count"])

    def assign_quintiles(group: pd.DataFrame) -> pd.DataFrame:
        group = group.copy()
        if group["composite_score"].nunique() < 5:
            group["score_bucket"] = np.nan
        else:
            group["score_bucket"] = pd.qcut(group["composite_score"], 5, labels=False, duplicates="drop") + 1
        return group

    bucketed = merged.groupby("as_of_date", group_keys=False).apply(assign_quintiles, include_groups=False)
    bucketed = bucketed.dropna(subset=["score_bucket"])
    return bucketed.groupby(["score_bucket", "lifecycle_state"], as_index=False).agg(
        mean_excess_return=("excess_return", "mean"), sample_count=("excess_return", "size")
    )


def evaluate_lifecycle_score_bucket_oos(
    snapshots: pd.DataFrame,
    labels: pd.DataFrame,
    horizon: int,
    windows: list[dict[str, pd.Timestamp]],
) -> pd.DataFrame:
    """仅在每个滚动窗口的验证日期内统计受控 Lifecycle 条件收益。"""
    dated_snapshots = snapshots.copy()
    dated_snapshots["as_of_date"] = pd.to_datetime(dated_snapshots["as_of_date"])
    rows: list[pd.DataFrame] = []
    for index, window in enumerate(windows, start=1):
        validation = dated_snapshots.loc[
            dated_snapshots["as_of_date"].between(window["validation_start"], window["validation_end"])
        ]
        result = evaluate_lifecycle_score_buckets(validation, labels, horizon)
        if not result.empty:
            rows.append(result.assign(window_name=f"oos_{index:03d}", horizon=horizon, **window))
    if not rows:
        return pd.DataFrame(columns=[
            "score_bucket", "lifecycle_state", "mean_excess_return", "sample_count",
            "window_name", "horizon", "train_start", "train_end", "validation_start", "validation_end",
        ])
    return pd.concat(rows, ignore_index=True)


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


def build_forward_return_labels(
    level: int,
    start_date: str,
    end_date: str,
    horizons: tuple[int, ...] = DEFAULT_ALPHA_DECAY_HORIZONS,
) -> pd.DataFrame:
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


def rolling_oos_windows(trade_dates: pd.DatetimeIndex, train_days: int = 252, validation_days: int = 63, step_days: int = 21) -> list[dict[str, pd.Timestamp]]:
    """按固定训练、验证和步长生成不重叠未来验证区间的滚动窗口。

    参数:
        trade_dates: 已去重的交易日序列。
        train_days: 每个训练窗口的交易日数量。
        validation_days: 紧随训练窗口的样本外验证日数量。
        step_days: 相邻窗口起点的推进交易日数。
    返回:
        含训练/验证起止日期的窗口字典列表；历史不足时返回空列表。
    """
    dates = pd.DatetimeIndex(trade_dates).drop_duplicates().sort_values()
    windows = []
    for start in range(0, len(dates) - train_days - validation_days + 1, step_days):
        windows.append({
            "train_start": dates[start], "train_end": dates[start + train_days - 1],
            "validation_start": dates[start + train_days], "validation_end": dates[start + train_days + validation_days - 1],
        })
    return windows


def evaluate_rolling_oos(
    snapshots: pd.DataFrame,
    labels: pd.DataFrame,
    factor: str,
    horizon: int,
    windows: list[dict[str, pd.Timestamp]],
) -> pd.DataFrame:
    """仅在每个滚动窗口的验证期计算已冻结因子的研究指标。"""
    rows = []
    dated_snapshots = snapshots.copy()
    dated_snapshots["as_of_date"] = pd.to_datetime(dated_snapshots["as_of_date"])
    for index, window in enumerate(windows, start=1):
        validation = dated_snapshots.loc[
            dated_snapshots["as_of_date"].between(window["validation_start"], window["validation_end"])
        ]
        metrics = evaluate_factor(validation, labels, factor, horizon)
        rows.append({
            **window,
            "window_name": f"oos_{index:03d}",
            "factor": factor,
            "horizon": horizon,
            **metrics,
        })
    return pd.DataFrame(rows)


def simulate_top_group_strategy(
    snapshots: pd.DataFrame,
    one_day_labels: pd.DataFrame,
    factor: str,
    rebalance_every: int,
    cost_bps: float,
) -> dict[str, float]:
    """用前一交易日 Score 选择 Top 五分位，并模拟下一交易日的成本后收益。"""
    if rebalance_every <= 0:
        raise ValueError("rebalance_every 必须为正整数")
    if cost_bps < 0:
        raise ValueError("cost_bps 不能为负数")
    _validate_unique(snapshots, "快照")
    if factor not in snapshots:
        raise ValueError(f"快照缺少因子列: {factor}")

    signals = snapshots[["as_of_date", "sector_name", factor]].copy()
    signals["as_of_date"] = pd.to_datetime(signals["as_of_date"])
    signals[factor] = pd.to_numeric(signals[factor], errors="coerce")
    signals = signals.dropna(subset=[factor])
    labels = one_day_labels.loc[one_day_labels["horizon"] == 1, ["as_of_date", "sector_name", "excess_return"]].copy()
    _validate_unique(labels, "标签")
    labels["as_of_date"] = pd.to_datetime(labels["as_of_date"])
    labels["excess_return"] = pd.to_numeric(labels["excess_return"], errors="coerce")
    labels = labels.dropna(subset=["excess_return"])
    signal_dates = pd.DatetimeIndex(signals["as_of_date"].unique()).sort_values()
    active_members: set[str] = set()
    gross_returns: list[float] = []
    net_returns: list[float] = []
    turnover_values: list[float] = []
    transaction_cost = 0.0

    for execution_index, execution_date in enumerate(sorted(labels["as_of_date"].unique())):
        prior_dates = signal_dates[signal_dates < execution_date]
        if prior_dates.empty:
            continue
        if execution_index % rebalance_every == 0 or not active_members:
            signal = signals.loc[signals["as_of_date"] == prior_dates[-1]]
            if signal[factor].nunique() < 5:
                continue
            buckets = pd.qcut(signal[factor], 5, labels=False, duplicates="drop")
            next_members = set(signal.loc[buckets == buckets.max(), "sector_name"])
            turnover = 1.0 if not active_members else 1.0 - len(active_members & next_members) / len(active_members | next_members)
            active_members = next_members
        else:
            turnover = 0.0
        day_labels = labels.loc[(labels["as_of_date"] == execution_date) & labels["sector_name"].isin(active_members)]
        if day_labels.empty:
            continue
        gross_return = float(day_labels["excess_return"].mean())
        cost = turnover * cost_bps / 10_000
        gross_returns.append(gross_return)
        net_returns.append(gross_return - cost)
        turnover_values.append(turnover)
        transaction_cost += cost

    if not net_returns:
        return {
            "gross_return": np.nan, "net_return": np.nan, "average_turnover": np.nan,
            "transaction_cost": np.nan, "max_drawdown": np.nan, "downside_volatility": np.nan, "cvar_5": np.nan,
        }
    gross_nav = pd.Series(gross_returns).add(1.0).cumprod()
    net_nav = pd.Series(net_returns).add(1.0).cumprod()
    drawdown = net_nav / net_nav.cummax() - 1.0
    net_array = np.asarray(net_returns, dtype=float)
    downside = np.minimum(net_array, 0.0)
    cvar_cutoff = np.quantile(net_array, 0.05)
    return {
        "gross_return": float(gross_nav.iloc[-1] - 1.0),
        "net_return": float(net_nav.iloc[-1] - 1.0),
        "average_turnover": float(np.mean(turnover_values)),
        "transaction_cost": float(transaction_cost),
        "max_drawdown": float(drawdown.min()),
        "downside_volatility": float(np.std(downside, ddof=0) * np.sqrt(252)),
        "cvar_5": float(net_array[net_array <= cvar_cutoff].mean()),
    }


def evaluate_by_regime(snapshots: pd.DataFrame, labels: pd.DataFrame, factor: str, horizon: int) -> pd.DataFrame:
    """按市场状态分桶执行同口径因子评估。

    参数:
        snapshots: 含 ``market_regime`` 的日快照。
        labels: 前瞻收益标签。
        factor: 待评估因子列。
        horizon: 标签期限。
    返回:
        每个市场状态一行的评估结果 DataFrame。
    """
    if "market_regime" not in snapshots:
        return pd.DataFrame()
    rows = []
    for regime, group in snapshots.dropna(subset=["market_regime"]).groupby("market_regime"):
        result = evaluate_factor(group, labels, factor, horizon)
        result["market_regime"] = regime
        rows.append(result)
    return pd.DataFrame(rows)


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
    if factor not in snapshots:
        raise ValueError(f"快照缺少因子列: {factor}")
    selected = labels.loc[labels["horizon"] == horizon].copy()
    _validate_unique(selected, "标签")
    if (pd.to_datetime(selected["target_date"]) <= pd.to_datetime(selected["as_of_date"])).any():
        raise ValueError("标签 target_date 必须晚于 as_of_date")
    merged = snapshots[["as_of_date", "sector_name", factor]].merge(
        selected[["as_of_date", "sector_name", "excess_return"]], on=["as_of_date", "sector_name"], how="inner"
    ).dropna()
    merged[factor] = pd.to_numeric(merged[factor], errors="coerce")
    merged["excess_return"] = pd.to_numeric(merged["excess_return"], errors="coerce")
    merged = merged.dropna(subset=[factor, "excess_return"])
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
    top_members: list[set[str]] = []
    for _, group in merged.groupby("as_of_date"):
        if group[factor].nunique() < 5:
            continue
        quantile = pd.qcut(group[factor], 5, labels=False, duplicates="drop")
        top_group = group.loc[quantile == quantile.max()]
        group_returns.append((top_group["excess_return"].mean(), group.loc[quantile == quantile.min(), "excess_return"].mean()))
        top_members.append(set(top_group["sector_name"]))
    top = float(np.mean([item[0] for item in group_returns])) if group_returns else np.nan
    bottom = float(np.mean([item[1] for item in group_returns])) if group_returns else np.nan
    top_returns = [item[0] for item in group_returns]
    cumulative = pd.Series(top_returns).add(1.0).cumprod() if top_returns else pd.Series(dtype=float)
    drawdown = cumulative / cumulative.cummax() - 1.0 if not cumulative.empty else pd.Series(dtype=float)
    turnover = [1.0 - len(left & right) / max(1, len(left | right)) for left, right in zip(top_members, top_members[1:])]
    return {"ic_mean": daily_ic.mean(), "rank_ic_mean": daily_rank_ic.mean(),
            "icir": daily_ic.mean() / daily_ic.std(ddof=1) if len(daily_ic) > 1 and daily_ic.std(ddof=1) else np.nan,
            "top_group_return": top, "bottom_group_return": bottom, "top_bottom_return": top - bottom,
            "top_group_win_rate": float(np.mean(np.array(top_returns) > 0)) if top_returns else np.nan,
            "top_group_max_drawdown": float(drawdown.min()) if not drawdown.empty else np.nan,
            "top_group_turnover": float(np.mean(turnover)) if turnover else 0.0,
            "sample_count": int(len(merged))}
