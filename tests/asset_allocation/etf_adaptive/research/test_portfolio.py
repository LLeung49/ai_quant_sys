"""2-4 ETF portfolio construction and risk decomposition."""

from __future__ import annotations

import pytest

from asset_allocation.etf_adaptive.research.portfolio import (
    PairwiseRisk,
    build_equal_weight,
    build_inverse_volatility,
    correlation,
    downside_correlation,
    drawdown_overlap,
    pairwise_risk,
)


def test_build_equal_weight_normalises_to_one() -> None:
    weights = build_equal_weight(("A", "B", "C"))

    assert sum(weights.values()) == pytest.approx(1.0)
    assert weights == {"A": pytest.approx(1 / 3), "B": pytest.approx(1 / 3), "C": pytest.approx(1 / 3)}


def test_build_equal_weight_rejects_empty_input() -> None:
    try:
        build_equal_weight(())
    except ValueError as exc:
        assert "at least one" in str(exc)
    else:
        raise AssertionError("expected ValueError for empty product ids")


def test_build_equal_weight_rejects_duplicates() -> None:
    try:
        build_equal_weight(("A", "A"))
    except ValueError as exc:
        assert "unique" in str(exc)
    else:
        raise AssertionError("expected ValueError for duplicate product ids")


def test_inverse_volatility_weights_respect_fifty_percent_cap() -> None:
    weights = build_inverse_volatility({"A": 0.05, "B": 0.20, "C": 0.25}, cap=0.50)

    assert sum(weights.values()) == pytest.approx(1.0)
    assert max(weights.values()) <= 0.50


def test_inverse_volatility_weights_inverse_to_volatility() -> None:
    weights = build_inverse_volatility({"A": 0.10, "B": 0.20, "C": 0.30}, cap=1.0)

    assert weights["A"] > weights["B"] > weights["C"]
    assert sum(weights.values()) == pytest.approx(1.0)


def test_inverse_volatility_drops_zero_volatility_products() -> None:
    weights = build_inverse_volatility({"A": 0.10, "B": 0.0, "C": 0.30}, cap=1.0)

    assert "B" not in weights
    assert sum(weights.values()) == pytest.approx(1.0)


def test_inverse_volatility_rejects_invalid_cap() -> None:
    try:
        build_inverse_volatility({"A": 0.10}, cap=0.0)
    except ValueError as exc:
        assert "cap" in str(exc)
    else:
        raise AssertionError("expected ValueError for zero cap")


def test_correlation_matches_expectation_for_lockstep_series() -> None:
    series = (0.01, -0.02, 0.03, -0.01)

    assert correlation(series, series) == pytest.approx(1.0)


def test_correlation_is_negative_one_for_perfectly_anti_correlated_series() -> None:
    series_a = (0.01, 0.02, 0.03, 0.04)
    series_b = (0.04, 0.03, 0.02, 0.01)

    assert correlation(series_a, series_b) == pytest.approx(-1.0)


def test_correlation_is_zero_for_constant_series() -> None:
    series_a = (0.0, 0.0, 0.0, 0.0)
    series_b = (0.01, -0.02, 0.03, -0.01)

    assert correlation(series_a, series_b) == 0.0


def test_downside_correlation_focuses_on_negative_returns() -> None:
    series_a = (0.10, -0.20, 0.10, -0.30, 0.10)
    series_b = (0.10, -0.20, 0.10, -0.30, 0.10)

    assert downside_correlation(series_a, series_b) == pytest.approx(1.0)


def test_downside_correlation_returns_zero_for_all_positive_series() -> None:
    series_a = (0.01, 0.02, 0.03)
    series_b = (0.04, 0.05, 0.06)

    assert downside_correlation(series_a, series_b) == 0.0


def test_drawdown_overlap_counts_simultaneous_drawdown_sessions() -> None:
    nav_a = (1.0, 0.9, 0.95, 1.0, 0.85, 0.90)
    nav_b = (1.0, 0.92, 0.93, 0.96, 0.80, 0.95)

    overlap = drawdown_overlap(nav_a, nav_b)

    assert overlap > 0.0
    assert overlap < 1.0


def test_pairwise_risk_returns_metrics_for_every_ordered_pair() -> None:
    returns = {
        "A": (0.01, -0.02, 0.03, -0.01),
        "B": (0.02, -0.01, 0.02, -0.02),
    }
    risk = pairwise_risk(returns)

    assert ("A", "B") in risk
    assert ("B", "A") in risk
    assert isinstance(risk[("A", "B")], PairwiseRisk)
    assert risk[("A", "B")].drawdown_overlap == pytest.approx(
        risk[("B", "A")].drawdown_overlap,
    )
