"""Repair Alpha scoring and classification.

The Repair Alpha pipeline combines:

- Valuation dislocation (PE / PB / PS / P-OCF vs sector percentiles)
- Quality fundamentals (margin stability, ROE, debt safety, earnings momentum)
- Technical repair evidence (MACD bottom divergence + bullish patterns)
- Value-trap penalty (negative earnings momentum + high debt + restated)

The candidate status is one of:
- ``repair_value``     (high valuation dislocation only)
- ``repair_turnaround`` (valuation + quality)
- ``repair_full``       (valuation + quality + technical)
- ``value_trap``        (rejected by quality/value-trap penalty)

Default weights:
    valuation:    35%
    quality:       25%
    technical:     20%
    momentum:      10%
    risk:          10% (subtracted as penalty)

The four positive components (valuation + quality + technical + momentum)
sum to 0.90; risk is always subtracted as a penalty so the total
contribution can dip below 0.90 depending on fundamentals.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Optional

import numpy as np

from ..financial.quality import QualityComponents
from ..financial.valuation import ValuationSnapshot
from .pattern_adapter import BottomDivergenceResult, BullishPatternHit


CANDIDATE_VALUE = "repair_value"
CANDIDATE_TURNAROUND = "repair_turnaround"
CANDIDATE_FULL = "repair_full"
CANDIDATE_TRAP = "value_trap"

CANDIDATE_VALUES = frozenset({
    CANDIDATE_VALUE, CANDIDATE_TURNAROUND, CANDIDATE_FULL, CANDIDATE_TRAP,
})


@dataclass(frozen=True)
class RepairScoreWeights:
    """Configurable weights for the Repair score composition."""

    valuation: float = 0.35
    quality: float = 0.25
    technical: float = 0.20
    momentum: float = 0.10
    risk: float = 0.10


def _zscore(value: float, mean: float, std: float) -> float:
    if std is None or std <= 0:
        return 0.0
    return (float(value) - float(mean)) / float(std)


def compute_valuation_rank(
    snapshot: ValuationSnapshot,
    sector_pe_median: float,
    sector_pe_std: float,
    sector_pb_median: float,
    sector_pb_std: float,
    *,
    prefer_low_pe: bool = True,
) -> float:
    """Return a sector-normalized valuation dislocation score.

    A positive score means the stock is "cheaper than the sector median"
    by ``n`` standard deviations.  The score is averaged over the
    *valid* dimensions (PE/PB) so a missing ratio does not drag the
    average toward zero.  Financial-sector stocks skip PB.
    """

    is_financial = snapshot.sector_name in {"\u94f6\u884c", "\u91d1\u878d"}
    pe_z = 0.0
    pb_z = 0.0
    n_components = 0
    if snapshot.pe is not None:
        pe_z = _zscore(snapshot.pe, sector_pe_median, sector_pe_std)
        n_components += 1
    if snapshot.pb is not None and not is_financial:
        pb_z = _zscore(snapshot.pb, sector_pb_median, sector_pb_std)
        n_components += 1
    if n_components == 0:
        return 0.0
    avg = (pe_z + pb_z) / n_components
    return -avg if prefer_low_pe else avg


def score_technical(
    divergence: Optional[BottomDivergenceResult],
    bullish_patterns: list[BullishPatternHit],
) -> float:
    """Score the technical repair evidence in ``[0, 1]``."""

    score = 0.0
    if divergence is not None and divergence.has_divergence:
        score += 0.6
    for hit in bullish_patterns:
        if hit.signal_strength >= 200:
            score += 0.2
        else:
            score += 0.1
    return min(1.0, score)


def compute_momentum_score(
    quality: QualityComponents,
) -> float:
    """Convert earnings momentum into a [-1, 1] score."""

    if quality.earnings_momentum is None:
        return 0.0
    mom = float(quality.earnings_momentum)
    if mom >= 0:
        return min(1.0, mom / 0.5)
    return max(-1.0, mom / 0.5)


def compute_value_trap_penalty(quality: QualityComponents) -> float:
    """Penalty in ``[0, 1]`` for likely value-trap risk."""

    if quality.earnings_momentum is None or quality.debt_safety is None or quality.roe is None:
        return 0.0
    penalty = 0.0
    if quality.earnings_momentum is not None and quality.earnings_momentum < 0:
        penalty += 0.4
    if quality.debt_safety is not None and quality.debt_safety < 0.3:
        penalty += 0.3
    if quality.roe is not None and quality.roe < 0:
        penalty += 0.3
    return min(1.0, penalty)


def score_repair_candidate(
    *,
    valuation_rank: Optional[float],
    quality: QualityComponents,
    divergence: Optional[BottomDivergenceResult],
    bullish_patterns: list[BullishPatternHit],
    weights: RepairScoreWeights | None = None,
    technical_threshold: float = 0.5,
) -> "RepairScore":
    """Compute the final Repair score and candidate status."""

    weights = weights or RepairScoreWeights()
    positive_total = (
        weights.valuation + weights.quality + weights.technical + weights.momentum
    )
    if abs(positive_total - 0.90) > 1e-9:
        raise ValueError(
            "Repair positive weights must sum to 0.90 (35+25+20+10); "
            "risk is a separate penalty"
        )

    val = float(valuation_rank) if valuation_rank is not None else 0.0
    val_component = max(0.0, min(1.0, (val + 1.0) / 2.0))
    quality_component = 0.5
    if quality.roe is not None:
        quality_component = max(0.0, min(1.0, (quality.roe + 0.2) / 0.4))
    technical_component = score_technical(divergence, bullish_patterns)
    momentum_component = (compute_momentum_score(quality) + 1.0) / 2.0
    risk_penalty = compute_value_trap_penalty(quality)

    raw = (
        weights.valuation * val_component
        + weights.quality * quality_component
        + weights.technical * technical_component
        + weights.momentum * momentum_component
        - weights.risk * risk_penalty
    )
    score = max(0.0, min(1.0, raw))

    has_tech = technical_component >= technical_threshold
    has_quality = (quality.roe is not None) and (quality.roe > 0)
    has_value = valuation_rank is not None and valuation_rank > 0.0

    if risk_penalty >= 0.6:
        status = CANDIDATE_TRAP
    elif has_value and has_quality and has_tech:
        status = CANDIDATE_FULL
    elif has_value and has_quality:
        status = CANDIDATE_TURNAROUND
    elif has_value:
        status = CANDIDATE_VALUE
    else:
        status = CANDIDATE_TRAP

    attribution = {
        "valuation_component": val_component,
        "quality_component": quality_component,
        "technical_component": technical_component,
        "momentum_component": momentum_component,
        "risk_penalty": risk_penalty,
        "valuation_rank": val,
    }
    return RepairScore(
        stock_code="",
        sector_name=None,
        candidate_score=score,
        candidate_status=status,
        valuation_rank=valuation_rank,
        quality_score=quality.roe,
        technical_score=technical_component,
        momentum_score=quality.earnings_momentum,
        risk_penalty=risk_penalty,
        attribution=attribution,
        quality_flags=quality.quality_flags,
    )


@dataclass(frozen=True)
class RepairScore:
    """One Repair Alpha score row."""

    stock_code: str
    sector_name: Optional[str]
    candidate_score: float
    candidate_status: str
    valuation_rank: Optional[float]
    quality_score: Optional[float]
    technical_score: float
    momentum_score: Optional[float]
    risk_penalty: float
    attribution: dict
    quality_flags: tuple


__all__ = [
    "CANDIDATE_FULL",
    "CANDIDATE_TRAP",
    "CANDIDATE_TURNAROUND",
    "CANDIDATE_VALUE",
    "CANDIDATE_VALUES",
    "RepairScore",
    "RepairScoreWeights",
    "compute_momentum_score",
    "compute_valuation_rank",
    "compute_value_trap_penalty",
    "score_repair_candidate",
    "score_technical",
]

