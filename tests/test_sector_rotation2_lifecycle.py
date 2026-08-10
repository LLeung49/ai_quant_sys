from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.lifecycle import apply_lifecycle_v0


def test_lifecycle_v0_prioritizes_exit_over_all_positive_signals():
    """防止下降加速的行业因排名或历史热度而仍被建议持有。"""
    frame = pd.DataFrame(
        {
            "score_eligible": [True],
            "phase_confirmed": ["accel_down"],
            "composite_rank": [1],
            "participation_score": [0.8],
            "rank_change_1d": [5],
            "top10_days_20": [20],
        },
        index=["A"],
    )

    result = apply_lifecycle_v0(frame)

    assert result.loc["A", "lifecycle_state"] == "exit"
    assert result.loc["A", "lifecycle_action"] == "exit_or_avoid"
    assert result.loc["A", "lifecycle_position_multiplier"] == 0.0


def test_lifecycle_v0_marks_fading_breadth_as_divergence_before_crowding():
    """防止强势降温且参与度恶化的行业被误判为仅需轻度降仓。"""
    frame = pd.DataFrame(
        {
            "score_eligible": [True],
            "phase_confirmed": ["decel_up"],
            "composite_rank": [3],
            "participation_score": [-0.25],
            "rank_change_1d": [-2],
            "top10_days_20": [16],
        },
        index=["A"],
    )

    result = apply_lifecycle_v0(frame)

    assert result.loc["A", "lifecycle_state"] == "divergence"
    assert result.loc["A", "lifecycle_action"] == "reduce"
    assert result.loc["A", "lifecycle_position_multiplier"] == 0.25


def test_lifecycle_v0_distinguishes_crowded_trending_repair_and_emerging_candidates():
    """防止生命周期状态丢失对可执行动作的区分。"""
    frame = pd.DataFrame(
        {
            "score_eligible": [True, True, True, True],
            "phase_raw": ["decel_up", "accel_up", "bottoming_candidate", "bottoming_candidate"],
            "phase_confirmed": ["decel_up", "accel_up", "neutral", "reversal_confirmed"],
            "composite_rank": [2, 4, 9, 8],
            "participation_score": [0.30, 0.40, 0.10, 0.25],
            "rank_change_1d": [0, 2, 3, 4],
            "top10_days_20": [15, 7, 0, 0],
        },
        index=["crowded", "trending", "repair", "emerging"],
    )

    result = apply_lifecycle_v0(frame)

    assert result.loc["crowded", "lifecycle_state"] == "crowded"
    assert result.loc["crowded", "lifecycle_action"] == "hold_or_trim"
    assert result.loc["trending", "lifecycle_state"] == "trending"
    assert result.loc["trending", "lifecycle_action"] == "hold_or_add"
    assert result.loc["repair", "lifecycle_state"] == "repair"
    assert result.loc["repair", "lifecycle_action"] == "watch_or_probe"
    assert result.loc["emerging", "lifecycle_state"] == "emerging"
    assert result.loc["emerging", "lifecycle_action"] == "hold_or_probe"


def test_lifecycle_v0_keeps_ineligible_sector_neutral():
    """防止数据覆盖不足的行业生成伪交易建议。"""
    frame = pd.DataFrame({"score_eligible": [False], "phase_confirmed": ["accel_up"]}, index=["A"])

    result = apply_lifecycle_v0(frame)

    assert result.loc["A", "lifecycle_state"] == "neutral"
    assert result.loc["A", "lifecycle_action"] == "observe"
    assert result.loc["A", "lifecycle_position_multiplier"] == 0.0


def test_lifecycle_v0_records_state_transition_and_age_from_prior_snapshot():
    """防止状态切换无法审计，或持续天数在每日重跑时被重置。"""
    frame = pd.DataFrame(
        {
            "score_eligible": [True, True],
            "phase_confirmed": ["accel_up", "accel_up"],
            "participation_score": [0.4, 0.4],
        },
        index=["changed", "continued"],
    )
    previous = pd.DataFrame(
        {
            "sector_name": ["changed", "continued"],
            "lifecycle_state": ["neutral", "trending"],
            "lifecycle_age": [5, 3],
        }
    )

    result = apply_lifecycle_v0(frame, previous)

    assert bool(result.loc["changed", "lifecycle_changed"]) is True
    assert result.loc["changed", "lifecycle_age"] == 1
    assert bool(result.loc["continued", "lifecycle_changed"]) is False
    assert result.loc["continued", "lifecycle_age"] == 4
