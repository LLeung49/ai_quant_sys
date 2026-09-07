"""Two-level selection: Pareto front and per-index product selection."""

from __future__ import annotations

from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import SubLayer, SubLayerBudget
from asset_allocation.etf_adaptive.research.portfolio import PairwiseRisk
from asset_allocation.etf_adaptive.research.selection import (
    CandidateMetrics,
    ProductMetrics,
    SubLayerSelectionEvidence,
    dominates,
    pareto_front,
    select_best_product,
    select_products_by_index,
    select_sub_layer_products,
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


def _sub_layer_product(
    product_id: str,
    index_code: str,
    *,
    oos_evidence: float = 0.12,
    cost_sensitivity: float = 0.03,
    sub_layer: SubLayer = SubLayer.DEFENSIVE_DIVIDEND_ETF,
) -> ProductMetrics:
    return ProductMetrics(
        product_id=product_id,
        tracking_index_code=index_code,
        history_confidence=0.95,
        average_amount=200_000_000.0,
        data_quality_score=0.98,
        cost_sensitivity=cost_sensitivity,
        oos_evidence=oos_evidence,
        sub_layer=sub_layer,
    )


def _evidence(
    *product_ids: str,
    risk: dict[tuple[str, str], PairwiseRisk] | None = None,
    budget: Decimal = Decimal("100000"),
    minimum_tradable_budget: Decimal = Decimal("10000"),
) -> SubLayerSelectionEvidence:
    return SubLayerSelectionEvidence(
        budget=SubLayerBudget(SubLayer.DEFENSIVE_DIVIDEND_ETF, budget),
        pareto_product_ids=frozenset(product_ids),
        maximum_cost_sensitivity=0.05,
        minimum_tradable_budget=minimum_tradable_budget,
        per_product_cap=0.60,
        minimum_diversification_gain=0.30,
        pairwise_risk=risk or {},
    )


def test_select_sub_layer_products_returns_no_products_without_positive_oos_evidence() -> None:
    products = (_sub_layer_product("negative", "dividend", oos_evidence=0.0),)

    chosen = select_sub_layer_products(products, _evidence("negative"))

    assert chosen == ()


def test_select_sub_layer_products_returns_one_qualifying_product() -> None:
    product = _sub_layer_product("dividend_etf", "dividend")

    chosen = select_sub_layer_products((product,), _evidence("dividend_etf"))

    assert tuple(item.product_id for item in chosen) == ("dividend_etf",)


def test_select_sub_layer_products_keeps_diversifying_products_and_rejects_duplicate_index() -> None:
    products = (
        _sub_layer_product("dividend_etf", "dividend", cost_sensitivity=0.02),
        _sub_layer_product("duplicate_dividend_etf", "dividend", cost_sensitivity=0.04),
        _sub_layer_product("bank_stock", "bank"),
        _sub_layer_product("correlated_value", "value"),
    )
    risk = {
        ("bank_stock", "dividend_etf"): PairwiseRisk(0.30, 0.30, 0.30),
        ("correlated_value", "dividend_etf"): PairwiseRisk(0.95, 0.95, 0.95),
        ("correlated_value", "bank_stock"): PairwiseRisk(0.95, 0.95, 0.95),
    }

    chosen = select_sub_layer_products(
        products,
        _evidence(
            "dividend_etf", "duplicate_dividend_etf", "bank_stock", "correlated_value",
            risk=risk,
        ),
    )

    assert tuple(item.product_id for item in chosen) == ("dividend_etf", "bank_stock")


def test_select_sub_layer_products_rejects_a_product_that_cannot_receive_minimum_trade_budget() -> None:
    product = _sub_layer_product("dividend_etf", "dividend")

    chosen = select_sub_layer_products(
        (product,),
        _evidence("dividend_etf", budget=Decimal("10000"), minimum_tradable_budget=Decimal("7000")),
    )

    assert chosen == ()
