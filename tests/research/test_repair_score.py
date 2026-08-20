"""Tests for the Repair scoring module."""

import pytest

from datetime import date

from morning_conference.sector_rotation2.research.financial.quality import QualityComponents
from morning_conference.sector_rotation2.research.financial.valuation import ValuationSnapshot
from morning_conference.sector_rotation2.research.stock_alpha.pattern_adapter import (
    BottomDivergenceResult,
    BullishPatternHit,
)
from morning_conference.sector_rotation2.research.stock_alpha.repair import (
    CANDIDATE_FULL,
    CANDIDATE_TRAP,
    CANDIDATE_TURNAROUND,
    CANDIDATE_VALUE,
    RepairScoreWeights,
    compute_momentum_score,
    compute_valuation_rank,
    compute_value_trap_penalty,
    score_repair_candidate,
    score_technical,
)


def _quality(**overrides) -> QualityComponents:
    base = dict(
        margin_stability=0.10,
        roe=0.20,
        debt_safety=0.40,
        earnings_momentum=0.25,
        quality_flags=(),
    )
    base.update(overrides)
    return QualityComponents(**base)


def _valuation(**overrides) -> ValuationSnapshot:
    base = dict(
        as_of_date=date(2026, 8, 17),
        stock_code="600000",
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e",
        pe=10.0,
        pb=1.0,
        ps=2.0,
        p_ocf=8.0,
        market_cap=1000.0,
        ttm_revenue=500.0,
        ttm_net_profit=50.0,
        pit_status="pit_exact",
        quality_flags=(),
        raw_close=10.0,
    )
    base.update(overrides)
    return ValuationSnapshot(**base)


def test_compute_valuation_rank_prefers_low_pe() -> None:
    # PE = 5 (z = -2.5), PB = 1 (z = -2.0); prefer_low -> positive score.
    # (2.5 + 2.0) / 2 = 2.25
    rank = compute_valuation_rank(
        _valuation(pe=5.0, pb=1.0), sector_pe_median=10.0, sector_pe_std=2.0,
        sector_pb_median=2.0, sector_pb_std=0.5,
    )
    assert rank == pytest.approx(2.25)


def test_compute_valuation_rank_skips_missing_pb_for_financial() -> None:
    rank = compute_valuation_rank(
        _valuation(sector_name="\u94f6\u884c", pe=5.0, pb=None),
        sector_pe_median=10.0, sector_pe_std=2.0,
        sector_pb_median=2.0, sector_pb_std=0.5,
    )
    assert rank == pytest.approx(2.5)


def test_compute_valuation_rank_handles_missing_pe() -> None:
    rank = compute_valuation_rank(
        _valuation(pe=None, pb=0.5),
        sector_pe_median=10.0, sector_pe_std=2.0,
        sector_pb_median=2.0, sector_pb_std=0.5,
    )
    assert rank == pytest.approx(3.0)


def test_score_technical_full_on_divergence_plus_strong_pattern() -> None:
    div = BottomDivergenceResult(has_divergence=True)
    patterns = [BullishPatternHit(chinese_name="\u767e\u53d1\u4e0a\u5347", function_name="CDL3WHITESOLDIERS", signal_strength=200)]
    assert score_technical(div, patterns) == pytest.approx(0.8)


def test_score_technical_no_signals() -> None:
    assert score_technical(None, []) == 0.0


def test_compute_momentum_score_saturates_at_one() -> None:
    assert compute_momentum_score(_quality(earnings_momentum=2.0)) == 1.0


def test_compute_momentum_score_negative_saturates_at_minus_one() -> None:
    assert compute_momentum_score(_quality(earnings_momentum=-1.0)) == -1.0


def test_compute_momentum_score_zero_for_missing() -> None:
    assert compute_momentum_score(_quality(earnings_momentum=None)) == 0.0


def test_value_trap_penalty_accumulates_with_evidence() -> None:
    penalty = compute_value_trap_penalty(_quality(
        earnings_momentum=-0.10,
        debt_safety=0.20,
        roe=-0.05,
    ))
    assert penalty == 1.0


def test_value_trap_penalty_zero_when_healthy() -> None:
    assert compute_value_trap_penalty(_quality()) == 0.0


def test_score_repair_candidate_assigns_full_when_value_quality_tech() -> None:
    div = BottomDivergenceResult(has_divergence=True)
    patterns = [BullishPatternHit(chinese_name="\u4e00", function_name="CDLHAMMER", signal_strength=200)]
    score = score_repair_candidate(
        valuation_rank=0.5,
        quality=_quality(),
        divergence=div,
        bullish_patterns=patterns,
    )
    assert score.candidate_status == CANDIDATE_FULL


def test_score_repair_candidate_assigns_trap_when_risk_high() -> None:
    score = score_repair_candidate(
        valuation_rank=0.5,
        quality=_quality(roe=0.05, debt_safety=0.20, earnings_momentum=-0.30),
        divergence=None,
        bullish_patterns=[],
    )
    assert score.candidate_status == CANDIDATE_TRAP


def test_score_repair_candidate_value_only_path() -> None:
    score = score_repair_candidate(
        valuation_rank=0.5,
        quality=_quality(roe=None, debt_safety=None, earnings_momentum=None),
        divergence=None,
        bullish_patterns=[],
    )
    assert score.candidate_status == CANDIDATE_VALUE


def test_score_repair_candidate_rejects_invalid_weight_sum() -> None:
    bad = RepairScoreWeights(valuation=0.5, quality=0.5, technical=0.5, momentum=0.5)
    with pytest.raises(ValueError, match="must sum to 0.90"):
        score_repair_candidate(
            valuation_rank=0.0,
            quality=_quality(),
            divergence=None,
            bullish_patterns=[],
            weights=bad,
        )


def test_score_repair_candidate_clipping() -> None:
    div = BottomDivergenceResult(has_divergence=True)
    patterns = [
        BullishPatternHit(chinese_name="a", function_name="f1", signal_strength=200),
        BullishPatternHit(chinese_name="b", function_name="f2", signal_strength=200),
        BullishPatternHit(chinese_name="c", function_name="f3", signal_strength=200),
    ]
    score = score_repair_candidate(
        valuation_rank=2.0,
        quality=_quality(roe=0.30, debt_safety=0.8, earnings_momentum=0.5),
        divergence=div,
        bullish_patterns=patterns,
    )
    assert 0.0 <= score.candidate_score <= 1.0


def test_score_repair_candidate_attribution_keys() -> None:
    score = score_repair_candidate(
        valuation_rank=0.0,
        quality=_quality(),
        divergence=None,
        bullish_patterns=[],
    )
    for key in (
        "valuation_component", "quality_component", "technical_component",
        "momentum_component", "risk_penalty", "valuation_rank",
    ):
        assert key in score.attribution


def test_score_repair_candidate_turnaround_when_no_tech() -> None:
    score = score_repair_candidate(
        valuation_rank=0.5,
        quality=_quality(),
        divergence=None,
        bullish_patterns=[],
    )
    assert score.candidate_status == CANDIDATE_TURNAROUND


def test_score_repair_candidate_returns_clean_attribution_keys() -> None:
    """Each row exposes the same five-attribution JSON shape."""

    score = score_repair_candidate(
        valuation_rank=0.0,
        quality=_quality(roe=0.20, debt_safety=0.4, earnings_momentum=0.25),
        divergence=None,
        bullish_patterns=[],
    )
    assert set(score.attribution) == {
        "valuation_component", "quality_component", "technical_component",
        "momentum_component", "risk_penalty", "valuation_rank",
    }
