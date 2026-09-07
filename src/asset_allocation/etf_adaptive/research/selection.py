"""Two-level selection: Pareto front of stitched-OOS candidates and per-index
product selection. The selection layer never reaches back into the
backtest engine; it only consumes pre-aggregated metrics so the research
report can be regenerated deterministically from the artifact manifest.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
import math
from typing import Iterable, Mapping, Sequence

from ..contracts import SubLayer, SubLayerBudget
from .portfolio import PairwiseRisk


@dataclass(frozen=True)
class CandidateMetrics:
    """Point-in-time metrics for one stitched-OOS candidate configuration."""

    candidate_id: str
    annual_return: float
    max_drawdown_abs: float
    positive_window_share: float
    cost_ratio: float


def dominates(left: CandidateMetrics, right: CandidateMetrics) -> bool:
    """Return True when ``left`` dominates ``right`` on every metric."""

    if left.candidate_id == right.candidate_id:
        return False
    no_worse = (
        left.annual_return >= right.annual_return
        and left.max_drawdown_abs <= right.max_drawdown_abs
        and left.positive_window_share >= right.positive_window_share
        and left.cost_ratio <= right.cost_ratio
    )
    strictly_better = (
        left.annual_return > right.annual_return
        or left.max_drawdown_abs < right.max_drawdown_abs
        or left.positive_window_share > right.positive_window_share
        or left.cost_ratio < right.cost_ratio
    )
    return no_worse and strictly_better


def pareto_front(candidates: Iterable[CandidateMetrics]) -> tuple[CandidateMetrics, ...]:
    """Return the subset of ``candidates`` that are not dominated by another."""

    seen: list[CandidateMetrics] = list(candidates)
    front: list[CandidateMetrics] = []
    for candidate in seen:
        is_dominated = any(
            dominates(other, candidate) for other in seen if other is not candidate
        )
        if is_dominated:
            continue
        if any(existing.candidate_id == candidate.candidate_id for existing in front):
            continue
        front.append(candidate)
    front.sort(key=lambda item: (-item.annual_return, item.max_drawdown_abs, item.candidate_id))
    return tuple(front)


@dataclass(frozen=True)
class ProductMetrics:
    """Metrics describing one ETF product for product-selection purposes."""

    product_id: str
    tracking_index_code: str
    history_confidence: float
    average_amount: float
    data_quality_score: float
    cost_sensitivity: float
    oos_evidence: float
    sub_layer: SubLayer | None = None


def _normalise_history_confidence(value: float) -> float:
    if value < 0:
        return 0.0
    if value > 1:
        return 1.0
    return value


def select_best_product(products: Sequence[ProductMetrics]) -> ProductMetrics:
    """Select the best product for one tracking-index group.

    Lower cost sensitivity wins first, with higher history confidence as a
    secondary requirement to avoid picking cheap but thinly-traded products.
    """

    if not products:
        raise ValueError("select_best_product requires at least one product")

    def score(product: ProductMetrics) -> tuple[float, float, float, float, float, str]:
        history = _normalise_history_confidence(product.history_confidence)
        quality = product.data_quality_score
        return (
            product.cost_sensitivity,
            -history,
            -quality,
            -product.average_amount,
            -product.oos_evidence,
            product.product_id,
        )

    return min(products, key=score)


def select_products_by_index(
    products: Iterable[ProductMetrics],
) -> tuple[ProductMetrics, ...]:
    """Group ``products`` by tracking index and pick the best executable product per group."""

    grouped: dict[str, list[ProductMetrics]] = {}
    for product in products:
        grouped.setdefault(product.tracking_index_code, []).append(product)
    if not grouped:
        raise ValueError("select_products_by_index requires at least one product")
    selected: list[ProductMetrics] = []
    for index_code in sorted(grouped):
        selected.append(select_best_product(grouped[index_code]))
    selected.sort(key=lambda item: item.product_id)
    return tuple(selected)


def _normalise_products_by_id(
    products: Iterable[ProductMetrics],
) -> tuple[ProductMetrics, ...]:
    """Choose one deterministic record per tradable product identity.

    Provider metadata can be corrected or duplicated independently of the
    exchange-traded product id. Product identity therefore takes precedence
    over index metadata before index-level representative selection.
    """

    grouped: dict[str, list[ProductMetrics]] = {}
    for product in products:
        grouped.setdefault(product.product_id, []).append(product)
    return tuple(
        select_best_product(grouped[product_id]) for product_id in sorted(grouped)
    )


@dataclass(frozen=True)
class SubLayerSelectionEvidence:
    """Selection gates and pairwise evidence for one approved sub-layer.

    The evidence is deliberately pre-aggregated: selection is deterministic and
    cannot accidentally look ahead into the backtest engine.  ``pareto_product_ids``
    records the surviving cost-adjusted Pareto configurations, while positive
    ``ProductMetrics.oos_evidence`` is the independent stitched-OOS gate.
    """

    budget: SubLayerBudget
    pareto_product_ids: frozenset[str]
    maximum_cost_sensitivity: float
    minimum_tradable_budget: Decimal
    per_product_cap: float
    minimum_diversification_gain: float
    pairwise_risk: Mapping[tuple[str, str], PairwiseRisk] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        if not isinstance(self.budget, SubLayerBudget):
            raise ValueError("budget must be a SubLayerBudget")
        if not isinstance(self.pareto_product_ids, frozenset) or not all(
            isinstance(item, str) and item for item in self.pareto_product_ids
        ):
            raise ValueError("pareto_product_ids must be a frozenset of product ids")
        if (
            not isinstance(self.maximum_cost_sensitivity, (int, float))
            or isinstance(self.maximum_cost_sensitivity, bool)
            or not math.isfinite(self.maximum_cost_sensitivity)
            or self.maximum_cost_sensitivity < 0
        ):
            raise ValueError("maximum_cost_sensitivity must be a non-negative finite number")
        if (
            not isinstance(self.minimum_tradable_budget, Decimal)
            or not self.minimum_tradable_budget.is_finite()
            or self.minimum_tradable_budget < 0
        ):
            raise ValueError("minimum_tradable_budget must be a non-negative finite Decimal")
        if (
            not isinstance(self.per_product_cap, (int, float))
            or isinstance(self.per_product_cap, bool)
            or not math.isfinite(self.per_product_cap)
            or not 0 < self.per_product_cap <= 1
        ):
            raise ValueError("per_product_cap must be in (0, 1]")
        if (
            not isinstance(self.minimum_diversification_gain, (int, float))
            or isinstance(self.minimum_diversification_gain, bool)
            or not math.isfinite(self.minimum_diversification_gain)
        ):
            raise ValueError("minimum_diversification_gain must be a finite number")
        if not all(
            isinstance(pair, tuple)
            and len(pair) == 2
            and all(isinstance(product_id, str) and product_id for product_id in pair)
            and isinstance(risk, PairwiseRisk)
            for pair, risk in self.pairwise_risk.items()
        ):
            raise ValueError("pairwise_risk must map product-id pairs to PairwiseRisk")


def _pairwise_diversification_gain(
    candidate_id: str,
    selected_ids: Sequence[str],
    pairwise: Mapping[tuple[str, str], PairwiseRisk],
) -> float | None:
    """Return average diversification gain, or ``None`` without all evidence."""

    risks: list[PairwiseRisk] = []
    for selected_id in selected_ids:
        risk = pairwise.get((candidate_id, selected_id)) or pairwise.get(
            (selected_id, candidate_id)
        )
        if risk is None:
            return None
        risks.append(risk)
    if not risks:
        return 1.0
    average_overlap = sum(
        (risk.correlation + risk.downside_correlation + risk.drawdown_overlap) / 3
        for risk in risks
    ) / len(risks)
    return 1.0 - average_overlap


def select_sub_layer_products(
    products: Iterable[ProductMetrics], evidence: SubLayerSelectionEvidence
) -> tuple[ProductMetrics, ...]:
    """Return every evidence-supported product for a single sub-layer.

    This routine intentionally has no product-count target.  It filters to
    positive OOS, cost-sensitive Pareto survivors, de-duplicates products that
    track the same index, then adds only candidates with demonstrated
    correlation/downside/drawdown diversification.  A candidate must also be
    capable of receiving the configured minimum tradable allocation at its cap.
    """

    if not isinstance(evidence, SubLayerSelectionEvidence):
        raise ValueError("evidence must be a SubLayerSelectionEvidence")

    cap_budget = evidence.budget.budget * Decimal(str(evidence.per_product_cap))
    eligible = [
        product
        for product in products
        if product.sub_layer is evidence.budget.sub_layer
        and product.product_id in evidence.pareto_product_ids
        and product.oos_evidence > 0
        and product.cost_sensitivity <= evidence.maximum_cost_sensitivity
        and cap_budget >= evidence.minimum_tradable_budget
    ]
    if not eligible:
        return ()

    # De-duplicate only after evidence filters: an ineligible cheap tracker
    # cannot exclude a qualifying alternative for the same index.
    unique_products = _normalise_products_by_id(eligible)
    representatives = select_products_by_index(unique_products)
    ordered = sorted(
        representatives,
        key=lambda product: (
            product.cost_sensitivity,
            -product.oos_evidence,
            product.product_id,
        ),
    )
    selected: list[ProductMetrics] = []
    for candidate in ordered:
        minimum_required = evidence.minimum_tradable_budget * Decimal(
            len(selected) + 1
        )
        if minimum_required > evidence.budget.budget:
            continue
        gain = _pairwise_diversification_gain(
            candidate.product_id,
            [product.product_id for product in selected],
            evidence.pairwise_risk,
        )
        if gain is not None and gain >= evidence.minimum_diversification_gain:
            selected.append(candidate)
    if len(selected) * evidence.per_product_cap < 1.0 - 1e-12:
        return ()
    return tuple(selected)


@dataclass(frozen=True)
class PortfolioMetrics:
    """Aggregated risk metrics for one candidate portfolio."""

    product_ids: tuple[str, ...]
    weights: Mapping[str, float]
    correlation: Mapping[tuple[str, str], float]
    downside_correlation: Mapping[tuple[str, str], float]
    drawdown_overlap: Mapping[tuple[str, str], float]
    notes: tuple[str, ...] = field(default_factory=tuple)
