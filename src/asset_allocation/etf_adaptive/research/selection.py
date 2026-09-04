"""Two-level selection: Pareto front of stitched-OOS candidates and per-index
product selection. The selection layer never reaches back into the
backtest engine; it only consumes pre-aggregated metrics so the research
report can be regenerated deterministically from the artifact manifest.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence


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


@dataclass(frozen=True)
class PortfolioMetrics:
    """Aggregated risk metrics for one candidate portfolio."""

    product_ids: tuple[str, ...]
    weights: Mapping[str, float]
    correlation: Mapping[tuple[str, str], float]
    downside_correlation: Mapping[tuple[str, str], float]
    drawdown_overlap: Mapping[tuple[str, str], float]
    notes: tuple[str, ...] = field(default_factory=tuple)
