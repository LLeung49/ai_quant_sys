"""Tests for trend_risk and trend (scoring, classification)."""

from datetime import date

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.stock_alpha.config import TrendAlphaConfig
from morning_conference.sector_rotation2.research.stock_alpha.trend import (
    classify_candidate,
    score_trend_candidates,
)
from morning_conference.sector_rotation2.research.stock_alpha.trend_risk import (
    calc_extension_penalty,
    calc_hot_leader_bonus,
    calc_stock_liquidity,
    calc_volatility_penalty,
    total_risk_penalty,
)


def test_calc_extension_penalty_zero_below_start() -> None:
    assert calc_extension_penalty(0.10, start=0.20) == 0.0
    assert calc_extension_penalty(0.20, start=0.20) == 0.0


def test_calc_extension_penalty_max_at_or_above_end() -> None:
    assert calc_extension_penalty(1.00, start=0.20, end=1.00, max_penalty=0.40) == 0.40
    assert calc_extension_penalty(2.00, start=0.20, end=1.00, max_penalty=0.40) == 0.40


def test_calc_extension_penalty_linear_between() -> None:
    assert calc_extension_penalty(0.60, start=0.20, end=1.00, max_penalty=0.40) == pytest.approx(0.20)


def test_calc_extension_penalty_returns_none_for_missing() -> None:
    assert calc_extension_penalty(None) is None
    assert calc_extension_penalty(float("nan")) is None


def test_calc_extension_penalty_rejects_invalid_curve() -> None:
    with pytest.raises(ValueError, match="extension_start must be < extension_end"):
        calc_extension_penalty(0.5, start=1.0, end=0.5)


def test_calc_hot_leader_bonus_zero_below_threshold() -> None:
    bonus, unavailable = calc_hot_leader_bonus(streak=1, source="limit_up_history")
    assert bonus == 0.0
    assert unavailable is False


def test_calc_hot_leader_bonus_capped_at_five_percent() -> None:
    bonus, unavailable = calc_hot_leader_bonus(streak=3, source="limit_up_history")
    assert bonus == pytest.approx(0.05)
    assert unavailable is False


def test_calc_hot_leader_bonus_unavailable_source_returns_zero_with_flag() -> None:
    bonus, unavailable = calc_hot_leader_bonus(streak=10, source="unavailable")
    assert bonus == 0.0
    assert unavailable is True


def test_calc_hot_leader_bonus_rejects_invalid_cap() -> None:
    with pytest.raises(ValueError, match="cap must be in"):
        calc_hot_leader_bonus(streak=2, source="limit_up_history", cap=1.5)


def test_calc_hot_leader_bonus_rejects_non_positive_streak_threshold() -> None:
    with pytest.raises(ValueError, match="streak_threshold must be positive"):
        calc_hot_leader_bonus(streak=2, source="limit_up_history", streak_threshold=0)


def test_calc_stock_liquidity_returns_signed_percentile() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 4,
        "sector_name": ["Bank", "Bank", "Tech", "Tech"],
        "amount_20d_median": [1e6, 2e6, 5e5, 1.5e6],
    })
    out = calc_stock_liquidity(frame)
    assert out.iloc[0] == pytest.approx(-0.5)
    assert out.iloc[1] == pytest.approx(0.5)
    assert out.iloc[2] == pytest.approx(-0.5)
    assert out.iloc[3] == pytest.approx(0.5)


def test_calc_volatility_penalty_returns_signed_percentile() -> None:
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 3,
        "sector_name": ["Bank", "Bank", "Bank"],
        "volatility_20d": [0.10, 0.20, 0.40],
    })
    out = calc_volatility_penalty(frame)
    assert out.iloc[0] == pytest.approx(-0.5)
    assert out.iloc[2] == pytest.approx(0.5)


def test_total_risk_penalty_combines_components() -> None:
    assert total_risk_penalty(0.20, 0.10) == pytest.approx(0.15)


def test_total_risk_penalty_handles_missing_components() -> None:
    assert total_risk_penalty(None, 0.10) == pytest.approx(0.10)
    assert total_risk_penalty(0.20, None) == pytest.approx(0.20)
    assert total_risk_penalty(None, None) == 0.0


def test_total_risk_penalty_clamps_negative_volatility_to_zero() -> None:
    assert total_risk_penalty(0.10, -0.30) == pytest.approx(0.05)


def _scoring_frame() -> pd.DataFrame:
    return pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)] * 4,
        "sector_name": ["Bank", "Bank", "Bank", "Tech"],
        "alpha_strength": [0.30, 0.20, np.nan, 0.10],
        "persistence": [0.20, 0.10, 0.05, 0.0],
        "trend_quality": [0.20, 0.15, np.nan, 0.05],
        "structure": [0.10, 0.10, 0.10, 0.10],
        "liquidity": [0.10, 0.10, 0.05, 0.0],
        "hot_leader_bonus": [0.0, 0.0, 0.0, 0.0],
        "risk_penalty": [0.05, 0.10, 0.0, 0.0],
    })


def test_score_trend_candidates_computes_35_20_20_10_10_5_minus_risk() -> None:
    config = TrendAlphaConfig()
    out = score_trend_candidates(_scoring_frame(), config=config)
    assert out.iloc[0]["candidate_score"] == pytest.approx(0.0775)


def test_score_trend_candidates_clips_to_unit_interval() -> None:
    config = TrendAlphaConfig()
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)],
        "sector_name": ["Bank"],
        "alpha_strength": [1.0],
        "persistence": [1.0],
        "trend_quality": [1.0],
        "structure": [1.0],
        "liquidity": [1.0],
        "hot_leader_bonus": [1.0],
        "risk_penalty": [0.0],
    })
    out = score_trend_candidates(frame, config=config)
    assert out.iloc[0]["candidate_score"] == pytest.approx(0.5)


def test_score_trend_candidates_produces_sector_local_rank() -> None:
    config = TrendAlphaConfig()
    out = score_trend_candidates(_scoring_frame(), config=config)
    bank_rows = out[out["sector_name"] == "Bank"].copy()
    assert set(bank_rows["rank_in_sector"].dropna().tolist()) <= {1.0, 2.0, 3.0}
    tech_rows = out[out["sector_name"] == "Tech"]
    assert tech_rows["rank_in_sector"].iloc[0] == 1


def test_score_trend_candidates_zeros_when_only_risk_penalty_present() -> None:
    config = TrendAlphaConfig()
    frame = pd.DataFrame({
        "as_of_date": [date(2026, 8, 17)],
        "sector_name": ["Bank"],
        "alpha_strength": [np.nan],
        "persistence": [np.nan],
        "trend_quality": [np.nan],
        "structure": [np.nan],
        "liquidity": [np.nan],
        "hot_leader_bonus": [np.nan],
        "risk_penalty": [0.0],
    })
    out = score_trend_candidates(frame, config=config)
    # All features missing; risk_penalty is zero; weighted_sum=0 / total_weight>0 -> 0.
    assert out.iloc[0]["candidate_score"] == 0.0


def test_classify_candidate_priority_risk_first() -> None:
    config = TrendAlphaConfig()
    features = {"risk_penalty": 0.50, "candidate_score": 0.50}
    assert classify_candidate(features, config=config) == "risk_watch"


def test_classify_candidate_hot_leader_when_streak_safe_and_strong() -> None:
    config = TrendAlphaConfig()
    features = {
        "candidate_score": 0.40,
        "alpha_strength": 0.30,
        "limit_up_streak": 2,
        "hot_leader_source": "limit_up_history",
    }
    assert classify_candidate(features, config=config) == "hot_leader"


def test_classify_candidate_skips_hot_leader_when_source_unavailable() -> None:
    config = TrendAlphaConfig()
    features = {
        "candidate_score": 0.40,
        "alpha_strength": 0.30,
        "limit_up_streak": 3,
        "hot_leader_source": "unavailable",
    }
    assert classify_candidate(features, config=config) != "hot_leader"


def test_classify_candidate_trend_pullback_when_flag_set() -> None:
    config = TrendAlphaConfig()
    features = {
        "candidate_score": 0.20,
        "alpha_strength": 0.10,
        "strong_pullback": True,
        "breakout20": False,
        "breakout60": False,
    }
    assert classify_candidate(features, config=config) == "trend_pullback"


def test_classify_candidate_trend_leader_requires_alpha_and_breakout() -> None:
    config = TrendAlphaConfig()
    assert classify_candidate(
        {"candidate_score": 0.50, "alpha_strength": 0.30, "breakout20": False, "breakout60": False},
        config=config,
    ) == "risk_watch"
    assert classify_candidate(
        {"candidate_score": 0.50, "alpha_strength": 0.30, "breakout20": True, "breakout60": False},
        config=config,
    ) == "trend_leader"
    assert classify_candidate(
        {"candidate_score": 0.50, "alpha_strength": -0.10, "breakout20": True, "breakout60": False},
        config=config,
    ) == "risk_watch"
    config_low = TrendAlphaConfig(min_score_for_leader=0.60)
    assert classify_candidate(
        {"candidate_score": 0.10, "alpha_strength": 0.30, "breakout20": True, "breakout60": False},
        config=config_low,
    ) == "risk_watch"


def test_classify_candidate_handles_missing_score_as_risk_watch() -> None:
    config = TrendAlphaConfig()
    assert classify_candidate({"risk_penalty": 0.0}, config=config) == "risk_watch"
