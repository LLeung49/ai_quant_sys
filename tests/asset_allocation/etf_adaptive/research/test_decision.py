"""Tests for fail-closed risk-adjusted research decisions."""

from __future__ import annotations

from math import inf

import pytest

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
        "initial_oos_nav": 10_000.0,
        "cost_drag": 0.01,
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


@pytest.mark.parametrize("oos_window_count", (0, 3.5))
def test_nonpositive_or_fractional_oos_window_count_fails_closed(
    oos_window_count: object,
) -> None:
    """A count validation regression must not accept invalid OOS windows."""

    summary = evaluate_research_decision(_evidence(oos_window_count=oos_window_count))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "oos_window_count" in summary.blockers


def test_excessive_cost_drag_fails_closed() -> None:
    """Removing execution-cost bounds must not promote an uneconomic result."""

    summary = evaluate_research_decision(_evidence(cost_drag=0.03))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "cost_drag" in summary.blockers


def test_fabricated_cost_drag_fails_closed() -> None:
    """Trusting a supplied drag value must not conceal recorded execution cost."""

    summary = evaluate_research_decision(_evidence(cost_drag=0.005))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "cost_drag" in summary.blockers


@pytest.mark.parametrize("initial_oos_nav", (0.0, inf))
def test_zero_or_nonfinite_initial_oos_nav_fails_closed(
    initial_oos_nav: float,
) -> None:
    """Cost validation must not divide by an absent or unusable OOS NAV."""

    summary = evaluate_research_decision(_evidence(initial_oos_nav=initial_oos_nav))

    assert summary.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "initial_oos_nav" in summary.blockers


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
            persistent_failure_windows=4,
        )
    )

    assert summary.conclusion is ResearchConclusion.EVALUATE_STRUCTURAL_CHANGE


@pytest.mark.parametrize("count", (1, 2))
def test_insufficient_oos_blocks_even_positive_evidence(count) -> None:
    result = evaluate_research_decision(_evidence(oos_window_count=count))
    assert result.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "oos_evidence" in result.blockers


def test_aggregate_negative_metrics_do_not_prove_persistent_failure() -> None:
    result = evaluate_research_decision(_evidence(
        annual_excess=-0.03, drawdown_improvement=-0.01, sharpe_excess=-0.1,
        sortino_excess=-0.1, calmar_excess=-0.1, cvar5_improvement=-0.01,
    ))
    assert result.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert "persistent_failure_evidence" in result.blockers
