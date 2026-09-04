"""Two-level selection: Pareto front and per-index product selection."""

from __future__ import annotations

import pytest

from asset_allocation.etf_adaptive.research.selection import (
    CandidateMetrics,
    ProductMetrics,
    dominates,
    pareto_front,
    select_best_product,
    select_products_by_index,
)


def _candidate(id: str, *, return_: float, drawdown: float, positive: float, cost: float) -> CandidateMetrics:
    return CandidateMetrics(
        candidate_id=id,
        annual_return=return_,
        max_drawdown_abs=drawdown,
        positive_window_share=positive,
        cost_ratio=cost,
    )


def test_dominates_returns_true_when_left_is_better_on_every_axis() -> None:
    left = _candidate("A", return_=0.20, drawdown=0.10, positive=0.80, cost=0.02)
    right = _candidate("B", return_=0.10, drawdown=0.20, positive=0.60, cost=0.04)

    assert dominates(left, right) is True
    assert dominates(right, left) is False


def test_dominates_returns_false_when_axes_mix_wins_and_losses() -> None:
    left = _candidate("A", return_=0.30, drawdown=0.10, positive=0.80, cost=0.02)
    right = _candidate("B", return_=0.20, drawdown=0.05, positive=0.80, cost=0.02)

    assert dominates(left, right) is False
    assert dominates(right, left) is False


def test_pareto_front_excludes_dominated_candidate() -> None:
    candidates = (
        _candidate("A", return_=0.20, drawdown=0.10, positive=0.80, cost=0.02),
        _candidate("B", return_=0.10, drawdown=0.20, positive=0.60, cost=0.04),
        _candidate("C", return_=0.15, drawdown=0.15, positive=0.70, cost=0.03),
    )

    front = pareto_front(candidates)

    ids = [item.candidate_id for item in front]
    assert ids[0] == "A"
    assert "B" not in ids


def test_pareto_front_keeps_non_dominated_pairs() -> None:
    candidates = (
        _candidate("A", return_=0.20, drawdown=0.10, positive=0.80, cost=0.04),
        _candidate("B", return_=0.10, drawdown=0.05, positive=0.60, cost=0.02),
    )

    front = pareto_front(candidates)

    ids = sorted(item.candidate_id for item in front)
    assert ids == ["A", "B"]


def test_select_best_product_picks_lowest_cost_sensitivity_with_history_floor() -> None:
    products = (
        ProductMetrics(
            product_id="510300.SH", tracking_index_code="000300.SH",
            history_confidence=0.95, average_amount=2e8, data_quality_score=0.98,
            cost_sensitivity=0.04, oos_evidence=0.20,
        ),
        ProductMetrics(
            product_id="510310.SH", tracking_index_code="000300.SH",
            history_confidence=0.90, average_amount=1.5e8, data_quality_score=0.95,
            cost_sensitivity=0.03, oos_evidence=0.18,
        ),
    )

    chosen = select_best_product(products)

    assert chosen.product_id == "510310.SH"


def test_select_products_by_index_groups_by_tracking_index_code() -> None:
    products = (
        ProductMetrics(
            product_id="510300.SH", tracking_index_code="000300.SH",
            history_confidence=0.95, average_amount=2e8, data_quality_score=0.98,
            cost_sensitivity=0.04, oos_evidence=0.20,
        ),
        ProductMetrics(
            product_id="510500.SH", tracking_index_code="000905.SH",
            history_confidence=0.92, average_amount=1e8, data_quality_score=0.97,
            cost_sensitivity=0.05, oos_evidence=0.18,
        ),
        ProductMetrics(
            product_id="510310.SH", tracking_index_code="000300.SH",
            history_confidence=0.90, average_amount=1.5e8, data_quality_score=0.95,
            cost_sensitivity=0.03, oos_evidence=0.18,
        ),
    )

    chosen = select_products_by_index(products)

    ids = tuple(item.product_id for item in chosen)
    assert ids == ("510310.SH", "510500.SH")
