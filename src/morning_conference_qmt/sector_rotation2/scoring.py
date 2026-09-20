"""将板块原始特征转换为连续、可解释的横截面评分。"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .config import ModelConfig
from .normalizers import signed_percentile, weighted_available_mean


def _score_group(frame: pd.DataFrame, columns: list[str], minimum_count: int) -> pd.Series:
    """对一组原始指标做当日百分位标准化后等权合成。

    参数:
        frame: 行为板块的当日横截面原始特征。
        columns: 允许进入本评分组的特征列，缺失列自动排除。
        minimum_count: 每一原始列计算百分位所需的最少有效板块数量。
    返回:
        评分范围为 [-1, 1] 的 Series；少于两项可用证据的行返回 NaN。
    """
    available = [column for column in columns if column in frame]
    if not available:
        return pd.Series(float("nan"), index=frame.index)
    normalized = pd.DataFrame({column: signed_percentile(frame[column], minimum_count) for column in available})
    return normalized.mean(axis=1, skipna=True).where(normalized.notna().sum(axis=1) >= 2)


def score_feature_panel(panel: pd.DataFrame, config: ModelConfig) -> pd.DataFrame:
    """计算五类连续评分、主评分和横截面排名。

    参数:
        panel: 行为板块、列为 Task 5 原始特征的同日横截面 DataFrame。
        config: 含最低截面数量、最低可用权重和主评分权重的模型配置。
    返回:
        复制原始列并增加各类 score、score_eligible、component rank、base_score 和 composite_rank 的 DataFrame。
    """
    result = panel.copy()
    minimum = config.min_cross_section
    result["trend_level_score"] = _score_group(result, ["rs_20", "rs_60", "distance_ma20", "distance_ma60"], minimum)
    result["strength_score"] = result["trend_level_score"]
    result["velocity_score"] = _score_group(result, ["rs_5", "rs_20", "ma20_slope"], minimum)
    result["acceleration_score"] = _score_group(result, ["rs20_accel", "ma20_accel", "macd_hist_delta"], minimum)

    # 量能输入先取对数，减弱极端放量板块对截面排名的影响。
    for source, target in (("rvol_5_20", "_log_rvol_5_20"), ("share_impulse", "_log_share_impulse")):
        result[target] = np.log(result[source].where(result[source] > 0)) if source in result else np.nan
    result["volume_score"] = _score_group(result, ["_log_rvol_5_20", "_log_share_impulse"], minimum)
    result["participation_score"] = _score_group(
        result, ["breadth_up", "breadth_above_ma20", "breadth_new_high_20", "breadth_rvol"], minimum
    )

    component_columns = list(config.score_weights)
    result["base_score"] = weighted_available_mean(result, config.score_weights, config.score_minimum_weight)
    result["composite_score"] = result["base_score"]
    result["score_eligible"] = result["base_score"].notna()
    for column in component_columns:
        result[f"{column.removesuffix('_score')}_rank"] = result[column].rank(ascending=False, method="min").where(result[column].notna())
    eligible = result["score_eligible"]
    result["composite_rank"] = result.loc[eligible, "base_score"].rank(ascending=False, method="min")
    return result.drop(columns=["_log_rvol_5_20", "_log_share_impulse"])


def _phase_raw(row: pd.Series, previous_confirmed: str | None, config: ModelConfig) -> str:
    """根据连续速度/加速度及迟滞阈值得到未确认的阶段候选。

    参数:
        row: 单一板块当日评分与特征。
        previous_confirmed: 前一已确认阶段；同方向保持时使用较低阈值。
        config: 包含进入和保持阈值的模型配置。
    返回:
        ``accel_up``、``decel_up``、``accel_down``、``bottoming_candidate``
        或 ``neutral``。
    """
    velocity = row.get("velocity_score")
    acceleration = row.get("acceleration_score")
    if pd.isna(velocity) or pd.isna(acceleration):
        return "neutral"
    positive_direction = previous_confirmed in {"accel_up", "decel_up"}
    negative_direction = previous_confirmed in {"accel_down", "bottoming_candidate", "reversal_confirmed"}
    threshold = config.phase_hold_threshold if positive_direction or negative_direction else config.phase_enter_threshold
    if velocity >= threshold and acceleration >= threshold:
        return "accel_up"
    if velocity >= threshold and acceleration <= -threshold:
        return "decel_up"
    if velocity <= -threshold and acceleration <= -threshold:
        return "accel_down"
    if velocity <= -threshold and acceleration >= threshold:
        return "bottoming_candidate"
    return "neutral"


def _history_for_sector(previous: pd.DataFrame | None, sector_name: object) -> pd.DataFrame:
    """提取一个板块最多二十日的状态记录，并兼容索引或列保存板块名的调用方。

    参数:
        previous: 历史快照行；应含 ``phase_raw``，可选 ``as_of_date``、
            ``phase_confirmed``、``phase_age``。
        sector_name: 当前评分行所对应的板块标识。
    返回:
        按日期升序排列且最多二十行的该板块历史 DataFrame。
    """
    if previous is None or previous.empty:
        return pd.DataFrame()
    history = previous.copy()
    if "sector_name" in history:
        history = history.loc[history["sector_name"] == sector_name]
    elif sector_name in history.index:
        history = history.loc[[sector_name]]
    else:
        return pd.DataFrame()
    if "as_of_date" in history:
        history = history.sort_values("as_of_date")
    return history.tail(20)


def _phase_confidence(row: pd.Series, phase_age: int) -> float:
    """按规格合成阶段置信度，并对缺失参与度重新归一化。

    参数:
        row: 当前板块的速度、加速度和参与度评分。
        phase_age: 本次确认状态已持续的交易日数。
    返回:
        [0, 1] 内的置信度；速度或加速度缺失时返回 NaN。
    """
    velocity, acceleration = row.get("velocity_score"), row.get("acceleration_score")
    if pd.isna(velocity) or pd.isna(acceleration):
        return float("nan")
    parts = [0.35 * abs(velocity), 0.35 * abs(acceleration), 0.10 * min(phase_age / 3.0, 1.0)]
    weights = [0.35, 0.35, 0.10]
    participation = row.get("participation_score")
    if not pd.isna(participation):
        parts.append(0.20 * max(participation, 0.0))
        weights.append(0.20)
    return min(1.0, sum(parts) / sum(weights))


def _is_reversal_confirmed(row: pd.Series, history: pd.DataFrame) -> bool:
    """判断筑底候选是否同时具备至少两项反转确认信号。

    参数:
        row: 当前板块的原始特征、分数及排名。
        history: 当前板块此前快照，若存在则用于速度穿零与排名连续改善。
    返回:
        至少两项规格定义的反转条件命中时为 True。
    """
    conditions = [
        row.get("rs_5", float("nan")) > 0,
        row.get("distance_ma20", float("nan")) > 0,
        row.get("breadth_up", float("nan")) > 0.50,
        row.get("share_impulse", float("nan")) > 1.0,
    ]
    if not history.empty:
        prior_velocity = history.iloc[-1].get("velocity_score", float("nan"))
        conditions.append(prior_velocity <= 0 < row.get("velocity_score", float("nan")))
        if len(history) >= 2:
            prior_ranks = history["composite_rank"].tail(2).tolist()
            conditions.append(prior_ranks[1] < prior_ranks[0] and row.get("composite_rank", float("nan")) < prior_ranks[1])
    return sum(bool(condition) for condition in conditions) >= 2


def apply_phase_history(scored: pd.DataFrame, previous: pd.DataFrame | None, config: ModelConfig) -> pd.DataFrame:
    """依据最近快照确认阶段、持续天数和置信度，不干预综合分或排名。

    ``previous`` 是该日以前的历史快照明细（最多使用每个板块最近两日），因而
    回填时不会读取未来记录。候选阶段须在“当前加最近两日”中至少出现两次；
    筑底候选在具备两项反转证据时输出 ``reversal_confirmed``。

    参数:
        scored: ``score_feature_panel`` 的当日结果，索引为板块名。
        previous: 可为空的历史快照，支持 ``sector_name`` 列或板块索引。
        config: 含 phase 进入/保持阈值的模型配置。
    返回:
        在输入副本上增加 ``phase_raw``、``phase_confirmed``、``phase_age``、
        ``phase_changed``、``phase_confidence`` 的 DataFrame。
    """
    result = scored.copy()
    for sector_name, row in result.iterrows():
        history = _history_for_sector(previous, sector_name)
        prior_confirmed = history.iloc[-1].get("phase_confirmed", "neutral") if not history.empty else "neutral"
        raw = _phase_raw(row, prior_confirmed, config)
        recent_raw = history.get("phase_raw", pd.Series(dtype=object)).tail(2).tolist() + [raw]
        is_confirmed_candidate = raw != "neutral" and recent_raw.count(raw) >= 2
        if raw == "bottoming_candidate" and _is_reversal_confirmed(row, history):
            confirmed = "reversal_confirmed"
        elif is_confirmed_candidate:
            confirmed = raw
        else:
            confirmed = prior_confirmed if prior_confirmed else "neutral"
        prior_age = history.iloc[-1].get("phase_age", 0) if not history.empty else 0
        changed = confirmed != prior_confirmed
        age = 1 if changed else int(prior_age or 0) + 1
        result.loc[sector_name, "phase_raw"] = raw
        result.loc[sector_name, "phase_confirmed"] = confirmed
        result.loc[sector_name, "phase_age"] = age
        result.loc[sector_name, "phase_changed"] = changed
        result.loc[sector_name, "phase_confidence"] = _phase_confidence(row, age)
        current_rank = row.get("composite_rank", float("nan"))
        prior_ranks = history.get("composite_rank", pd.Series(dtype=float)).dropna()
        # 名次数字越小代表排名越好，因此“昨日名次 - 今日名次”为正即排名上升。
        result.loc[sector_name, "rank_change_1d"] = (
            prior_ranks.iloc[-1] - current_rank if len(prior_ranks) >= 1 and not pd.isna(current_rank) else float("nan")
        )
        result.loc[sector_name, "rank_change_5d"] = (
            prior_ranks.iloc[-5] - current_rank if len(prior_ranks) >= 5 and not pd.isna(current_rank) else float("nan")
        )
        was_top10 = not pd.isna(current_rank) and current_rank <= 10
        # 字段语义是“最近 20 个交易日累计在 Top10 的天数”，不是连续在榜天数；
        # 历史最多保留 20 行，因此取最近 19 日再加当前日，避免窗口超长。
        prior_top10_count = int((prior_ranks.tail(19) <= 10).sum())
        result.loc[sector_name, "top10_days_20"] = prior_top10_count + int(was_top10)
    return result

