from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.config import ModelConfig
from morning_conference.sector_rotation2.market_regime import classify_market_regime
from morning_conference.sector_rotation2.scoring import apply_phase_history, score_feature_panel


def test_score_feature_panel_builds_continuous_scores_and_rank_without_phase_bonus():
    panel = pd.DataFrame(
        {
            "rs_20": [0.03, 0.01, -0.01],
            "rs_60": [0.05, 0.02, -0.02],
            "distance_ma20": [0.02, 0.00, -0.02],
            "distance_ma60": [0.03, 0.00, -0.03],
            "rs_5": [0.02, 0.00, -0.02],
            "ma20_slope": [2.0, 0.0, -2.0],
            "rs20_accel": [0.01, 0.00, -0.01],
            "ma20_accel": [1.0, 0.0, -1.0],
            "macd_hist_delta": [0.5, 0.0, -0.5],
            "rvol_5_20": [1.5, 1.0, 0.8],
            "share_impulse": [1.4, 1.0, 0.9],
            "breadth_up": [0.8, 0.5, 0.2],
            "breadth_above_ma20": [0.8, 0.5, 0.2],
            "breadth_new_high_20": [0.5, 0.2, 0.0],
            "breadth_rvol": [0.7, 0.5, 0.3],
        },
        index=["强势", "中性", "弱势"],
    )
    config = ModelConfig(min_cross_section=3)

    result = score_feature_panel(panel, config)

    assert result.loc["强势", "trend_level_score"] > result.loc["中性", "trend_level_score"]
    assert result.loc["强势", "composite_rank"] == 1
    assert result.loc["弱势", "composite_rank"] == 3
    assert "phase_bonus" not in result.columns


def test_score_feature_panel_marks_row_ineligible_when_available_weight_is_too_low():
    panel = pd.DataFrame({"rs_20": [0.01, 0.00, -0.01], "rs_60": [0.01, 0.00, -0.01]})
    config = ModelConfig(min_cross_section=3)

    result = score_feature_panel(panel, config)

    assert result["score_eligible"].eq(False).all()
    assert result["composite_rank"].isna().all()


def test_phase_requires_two_of_last_three_candidate_days():
    """当前候选与最近两日中一次相同，满足三日两次后才确认状态。"""
    current = pd.DataFrame(
        {"velocity_score": [0.30], "acceleration_score": [0.30], "participation_score": [0.20]},
        index=["A"],
    )
    previous = pd.DataFrame(
        {
            "sector_name": ["A", "A"],
            "as_of_date": pd.to_datetime(["2026-07-30", "2026-07-31"]),
            "phase_raw": ["neutral", "accel_up"],
            "phase_confirmed": ["neutral", "neutral"],
            "phase_age": [3, 4],
        }
    )

    result = apply_phase_history(current, previous, ModelConfig())

    assert result.loc["A", "phase_raw"] == "accel_up"
    assert result.loc["A", "phase_confirmed"] == "accel_up"
    assert result.loc["A", "phase_age"] == 1


def test_bottoming_needs_two_reversal_conditions():
    """筑底候选同时满足两项反转证据时才提升为确认反转。"""
    current = pd.DataFrame(
        {
            "velocity_score": [-0.4], "acceleration_score": [0.4], "participation_score": [0.2],
            "rs_5": [0.01], "distance_ma20": [0.01], "breadth_up": [0.45],
            "share_impulse": [0.9], "composite_rank": [4],
        },
        index=["A"],
    )

    result = apply_phase_history(current, None, ModelConfig())

    assert result.loc["A", "phase_raw"] == "bottoming_candidate"
    assert result.loc["A", "phase_confirmed"] == "reversal_confirmed"


def test_phase_uses_lower_hold_threshold_after_accel_up_is_confirmed():
    """已经确认向上加速时，分数回落至进入阈值以内仍可按保持阈值延续。"""
    current = pd.DataFrame(
        {"velocity_score": [0.15], "acceleration_score": [0.15], "participation_score": [0.20]}, index=["A"]
    )
    previous = pd.DataFrame(
        {
            "sector_name": ["A", "A"],
            "as_of_date": pd.to_datetime(["2026-07-30", "2026-07-31"]),
            "phase_raw": ["accel_up", "accel_up"],
            "phase_confirmed": ["accel_up", "accel_up"],
            "phase_age": [2, 3],
        }
    )

    result = apply_phase_history(current, previous, ModelConfig())

    assert result.loc["A", "phase_raw"] == "accel_up"
    assert result.loc["A", "phase_confirmed"] == "accel_up"
    assert result.loc["A", "phase_age"] == 4


def test_phase_history_derives_rank_changes_and_top10_duration():
    """排名变动只使用历史快照，Top10 持续天数在重新进入时从 1 开始。"""
    current = pd.DataFrame(
        {"velocity_score": [0.3], "acceleration_score": [0.3], "participation_score": [0.2], "composite_rank": [8]},
        index=["A"],
    )
    previous = pd.DataFrame(
        {
            "sector_name": ["A"] * 5,
            "as_of_date": pd.date_range("2026-07-27", periods=5, freq="B"),
            "phase_raw": ["neutral"] * 5,
            "phase_confirmed": ["neutral"] * 5,
            "phase_age": [1, 2, 3, 4, 5],
            "composite_rank": [15, 14, 12, 10, 9],
            "top10_days_20": [0, 0, 0, 1, 2],
        }
    )

    result = apply_phase_history(current, previous, ModelConfig())

    assert result.loc["A", "rank_change_1d"] == 1
    assert result.loc["A", "rank_change_5d"] == 7
    assert result.loc["A", "top10_days_20"] == 3


def test_risk_off_takes_priority_over_high_volatility():
    """同时命中多个条件时，状态应遵循规格规定的优先级。"""
    benchmark = pd.DataFrame(
        {"close": [100.0] * 60 + [90.0], "amount": [100.0] * 61},
        index=pd.date_range("2026-05-01", periods=61, freq="B"),
    )
    breadth = pd.Series([0.40, 0.42, 0.43], index=benchmark.index[-3:])
    aggregates = pd.DataFrame({"limit_up": [10], "limit_down": [12]}, index=benchmark.index[-1:])

    result = classify_market_regime(benchmark, breadth, aggregates, benchmark.index[-1])

    assert result.market_regime == "risk_off"
    assert result.regime_multiplier == 0.70


def test_risk_on_regime_does_not_change_composite_rank():
    """市场状态只提供共享的风险暴露缩放，不能修改板块横截面排序。"""
    benchmark = pd.DataFrame(
        {"close": [100.0 + 0.25 * day for day in range(61)], "amount": [100.0] * 60 + [150.0]},
        index=pd.date_range("2026-05-01", periods=61, freq="B"),
    )
    breadth = pd.Series([0.60, 0.65, 0.70], index=benchmark.index[-3:])
    aggregates = pd.DataFrame({"limit_up": [12], "limit_down": [3]}, index=benchmark.index[-1:])

    result = classify_market_regime(benchmark, breadth, aggregates, benchmark.index[-1])

    assert result.market_regime == "risk_on"
    assert result.regime_multiplier == 1.00
