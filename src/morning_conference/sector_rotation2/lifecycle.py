"""板块轮动 Lifecycle V0：基于既有快照的研究型状态与人工执行建议。"""
from __future__ import annotations

import pandas as pd


_LIFECYCLE_FIELDS = (
    "lifecycle_state",
    "lifecycle_action",
    "lifecycle_position_multiplier",
    "lifecycle_reason",
)


def _state_for_row(row: pd.Series) -> tuple[str, str, float, str]:
    """按风险优先级为单个行业给出生命周期状态，不修改 Score 或排名。"""
    if not bool(row.get("score_eligible", False)):
        return "neutral", "observe", 0.0, "score_ineligible"

    phase = row.get("phase_confirmed", "neutral")
    raw_phase = row.get("phase_raw", "neutral")
    participation = row.get("participation_score", float("nan"))
    rank_change = row.get("rank_change_1d", float("nan"))
    top10_days = row.get("top10_days_20", 0)

    if phase == "accel_down":
        return "exit", "exit_or_avoid", 0.0, "phase_accel_down"
    if phase == "decel_up" and (participation < 0 or rank_change < 0):
        return "divergence", "reduce", 0.25, "decel_up_with_fading_breadth_or_rank"
    if phase == "decel_up" and top10_days >= 15:
        return "crowded", "hold_or_trim", 0.5, "decel_up_with_extended_top10_duration"
    if phase == "accel_up":
        return "trending", "hold_or_add", 1.0, "phase_accel_up"
    if phase == "reversal_confirmed":
        return "emerging", "hold_or_probe", 0.5, "reversal_confirmed"
    if raw_phase == "bottoming_candidate":
        return "repair", "watch_or_probe", 0.25, "repair_phase"
    if phase == "decel_up":
        return "emerging", "hold_or_probe", 0.5, "decel_up_without_warning"
    return "neutral", "observe", 0.0, "no_lifecycle_signal"


def _prior_lifecycle(previous: pd.DataFrame | None, sector_name: object) -> tuple[str, int]:
    """提取一个行业最近一日的 Lifecycle 状态和持续天数。"""
    if previous is None or previous.empty or "lifecycle_state" not in previous:
        return "neutral", 0
    history = previous.loc[previous["sector_name"] == sector_name] if "sector_name" in previous else pd.DataFrame()
    if history.empty:
        return "neutral", 0
    if "as_of_date" in history:
        history = history.sort_values("as_of_date")
    latest = history.iloc[-1]
    return str(latest.get("lifecycle_state") or "neutral"), int(latest.get("lifecycle_age") or 0)


def apply_lifecycle_v0(frame: pd.DataFrame, previous: pd.DataFrame | None = None) -> pd.DataFrame:
    """为已有评分快照附加 Lifecycle V0 的状态、人工动作和研究仓位乘数。

    输出仅是研究与人工决策辅助：Risk Engine 和 Sector Score 仍具有更高优先级，
    本函数不会改变 ``base_score``、``composite_score`` 或 ``composite_rank``。
    """
    result = frame.copy()
    values = result.apply(_state_for_row, axis=1, result_type="expand")
    values.columns = _LIFECYCLE_FIELDS
    result = result.join(values)
    for sector_name, row in result.iterrows():
        prior_state, prior_age = _prior_lifecycle(previous, sector_name)
        changed = row["lifecycle_state"] != prior_state
        result.loc[sector_name, "lifecycle_changed"] = changed
        result.loc[sector_name, "lifecycle_age"] = 1 if changed else prior_age + 1
    return result
