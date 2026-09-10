"""Tests for fail-closed risk-adjusted research decisions."""

from __future__ import annotations

from math import inf

from asset_allocation.etf_adaptive.research.decision import (
    ResearchConclusion,
    ResearchEvidence,
    evaluate_research_decision,
)


def _evidence(**overrides: object) -> ResearchEvidence:
    values: dict[str, object] = {
        "data_valid": True,
        "oos_window_count": 4,
        "oos_non_lagging_share": 0.75,
        "stable_parameter_region": True,
        "annual_excess": 0.02,
        "drawdown_improvement": 0.12,
        "sharpe_excess": 0.35,
        "sortino_excess": 0.40,
        "calmar_excess": 0.20,
        "cvar5_improvement": 0.01,
        "exposure_ratio": 0.80,
        "turnover": 1.0,
        "total_cost": 100.0,
    }
    values.update(overrides)
    return ResearchEvidence(**values)  # type: ignore[arg-type]


def test_defensive_evidence_with_small_return_lag_continues_parameter_optimization() -> None:
    """A regression to the pass gate must not promote this defensive result."""

    summary = evaluate_research_decision(
        _evidence(annual_excess=-0.004)
    )

    assert summary.conclusion is ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION
    assert summary.blockers == ("annual_excess",)


def test_positive_return_and_risk_adjusted_evidence_passes() -> None:
    """Dropping a pass criterion must not approve incomplete research evidence."""

    summary = evaluate_research_decision(_evidence())

    assert summary.conclusion is ResearchConclusion.PASSED
    assert summary.blockers == ()


def test_invalid_data_fails_closed_with_data_valid_blocker() -> None:
    """Removing the validity gate must never allow research evidence through."""

    summary = evaluate_research_decision(_evidence(data_valid=False))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "data_valid" in summary.blockers


def test_nonfinite_numeric_evidence_fails_closed() -> None:
    """Replacing finite checks with ordinary comparisons must not accept infinity."""

    summary = evaluate_research_decision(_evidence(sharpe_excess=inf))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "sharpe_excess" in summary.blockers


def test_boolean_numeric_evidence_fails_closed() -> None:
    """Replacing strict numeric validation with isinstance(value, int) is unsafe."""

    summary = evaluate_research_decision(_evidence(turnover=True))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "turnover" in summary.blockers


def test_incomplete_numeric_evidence_fails_closed() -> None:
    """A missing metric must become a trade blocker instead of raising or passing."""

    summary = evaluate_research_decision(_evidence(total_cost=None))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "total_cost" in summary.blockers


def test_persistent_negative_return_and_risk_adjusted_evidence_needs_structural_change() -> None:
    """A strategy with no return or defensive support must be escalated, not tuned."""

    summary = evaluate_research_decision(
        _evidence(
            annual_excess=-0.03,
            drawdown_improvement=-0.01,
            sharpe_excess=-0.10,
            sortino_excess=-0.10,
            calmar_excess=-0.10,
            cvar5_improvement=-0.01,
        )
    )

    assert summary.conclusion is ResearchConclusion.EVALUATE_STRUCTURAL_CHANGE
