"""Fail-closed decisions for risk-adjusted ETF research evidence."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite


class ResearchConclusion(str, Enum):
    """Permitted outcomes for research; none authorizes live trading."""

    PASSED = "passed"
    CONTINUE_PARAMETER_OPTIMIZATION = "continue_parameter_optimization"
    EVALUATE_STRUCTURAL_CHANGE = "evaluate_structural_change"
    DO_NOT_TRADE = "do_not_trade"


@dataclass(frozen=True)
class ResearchEvidence:
    """Comparable out-of-sample evidence for one strategy configuration."""

    data_valid: bool
    oos_window_count: int
    oos_non_lagging_share: float
    stable_parameter_region: bool
    annual_excess: float
    drawdown_improvement: float
    sharpe_excess: float
    sortino_excess: float
    calmar_excess: float
    cvar5_improvement: float
    exposure_ratio: float
    turnover: float
    total_cost: float


@dataclass(frozen=True)
class DecisionSummary:
    """A conclusion and the evidence fields that prevented a stronger result."""

    conclusion: ResearchConclusion
    blockers: tuple[str, ...]


_NUMERIC_FIELDS = (
    "oos_window_count",
    "oos_non_lagging_share",
    "annual_excess",
    "drawdown_improvement",
    "sharpe_excess",
    "sortino_excess",
    "calmar_excess",
    "cvar5_improvement",
    "exposure_ratio",
    "turnover",
    "total_cost",
)
_RISK_ADJUSTED_FIELDS = (
    "drawdown_improvement",
    "sharpe_excess",
    "sortino_excess",
    "calmar_excess",
    "cvar5_improvement",
)
_MIN_OOS_WINDOWS = 3
_MIN_NON_LAGGING_SHARE = 0.60
_BOUNDED_RETURN_LAG = -0.002
_MATERIAL_DRAWDOWN_IMPROVEMENT = 0.10
_MATERIAL_CVAR5_IMPROVEMENT = 0.01


def _is_finite_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and isfinite(value)


def _invalid_evidence_blockers(evidence: ResearchEvidence) -> tuple[str, ...]:
    blockers: list[str] = []
    for field in _NUMERIC_FIELDS:
        if not _is_finite_number(getattr(evidence, field, None)):
            blockers.append(field)
    for field in ("data_valid", "stable_parameter_region"):
        if not isinstance(getattr(evidence, field, None), bool):
            blockers.append(field)
    if evidence.data_valid is not True:
        blockers.append("data_valid")
    if _is_finite_number(evidence.oos_non_lagging_share) and not 0.0 <= evidence.oos_non_lagging_share <= 1.0:
        blockers.append("oos_non_lagging_share")
    if _is_finite_number(evidence.exposure_ratio) and not 0.0 <= evidence.exposure_ratio <= 1.0:
        blockers.append("exposure_ratio")
    if _is_finite_number(evidence.turnover) and evidence.turnover < 0.0:
        blockers.append("turnover")
    if _is_finite_number(evidence.total_cost) and evidence.total_cost < 0.0:
        blockers.append("total_cost")
    return tuple(dict.fromkeys(blockers))


def _has_positive_risk_adjusted_evidence(evidence: ResearchEvidence) -> bool:
    return all(getattr(evidence, field) > 0.0 for field in _RISK_ADJUSTED_FIELDS)


def _has_material_defensive_improvement(evidence: ResearchEvidence) -> bool:
    return (
        evidence.drawdown_improvement >= _MATERIAL_DRAWDOWN_IMPROVEMENT
        and evidence.cvar5_improvement >= _MATERIAL_CVAR5_IMPROVEMENT
    )


def evaluate_research_decision(evidence: ResearchEvidence) -> DecisionSummary:
    """Classify research evidence without aggregating it into a weighted score."""

    invalid_blockers = _invalid_evidence_blockers(evidence)
    if invalid_blockers:
        return DecisionSummary(ResearchConclusion.DO_NOT_TRADE, invalid_blockers)

    if not evidence.stable_parameter_region:
        return DecisionSummary(ResearchConclusion.DO_NOT_TRADE, ("stable_parameter_region",))

    adequate_oos = (
        evidence.oos_window_count >= _MIN_OOS_WINDOWS
        and evidence.oos_non_lagging_share >= _MIN_NON_LAGGING_SHARE
    )
    positive_risk_adjusted = _has_positive_risk_adjusted_evidence(evidence)

    if (
        evidence.annual_excess <= -0.01
        and all(getattr(evidence, field) <= 0.0 for field in _RISK_ADJUSTED_FIELDS)
    ):
        return DecisionSummary(ResearchConclusion.EVALUATE_STRUCTURAL_CHANGE, ())

    pass_return_gate = evidence.annual_excess > 0.0 or (
        evidence.annual_excess >= _BOUNDED_RETURN_LAG
        and _has_material_defensive_improvement(evidence)
    )
    if adequate_oos and positive_risk_adjusted and pass_return_gate:
        return DecisionSummary(ResearchConclusion.PASSED, ())

    if positive_risk_adjusted and _has_material_defensive_improvement(evidence):
        blockers: list[str] = []
        if not adequate_oos:
            blockers.append("oos_evidence")
        if not pass_return_gate:
            blockers.append("annual_excess")
        return DecisionSummary(
            ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION,
            tuple(blockers),
        )

    return DecisionSummary(ResearchConclusion.EVALUATE_STRUCTURAL_CHANGE, ())
