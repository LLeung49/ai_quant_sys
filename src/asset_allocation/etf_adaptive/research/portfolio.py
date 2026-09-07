"""2-4 ETF portfolio construction and risk decomposition."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from math import sqrt
from typing import TYPE_CHECKING, Mapping, Sequence

from ..contracts import SubLayerBudget

if TYPE_CHECKING:
    from .selection import ProductMetrics


DEFAULT_INVERSE_VOLATILITY_CAP: float = 0.50


@dataclass(frozen=True)
class PairwiseRisk:
    """Per-pair correlation, downside correlation, and drawdown overlap."""

    correlation: float
    downside_correlation: float
    drawdown_overlap: float


def _normalise_weights(weights: Mapping[str, float]) -> dict[str, float]:
    total = sum(max(value, 0.0) for value in weights.values())
    if total <= 0:
        raise ValueError("portfolio weights must be non-negative and sum positive")
    return {key: max(value, 0.0) / total for key, value in weights.items()}


def build_equal_weight(product_ids: Sequence[str]) -> dict[str, float]:
    """Return an equal-weight portfolio, normalised to 1.0."""

    if not product_ids:
        raise ValueError("build_equal_weight requires at least one product")
    unique = tuple(dict.fromkeys(product_ids))
    if len(unique) != len(product_ids):
        raise ValueError("build_equal_weight requires unique product ids")
    weight = 1.0 / len(unique)
    return {product_id: weight for product_id in unique}


def build_inverse_volatility(
    volatilities: Mapping[str, float],
    cap: float = DEFAULT_INVERSE_VOLATILITY_CAP,
) -> dict[str, float]:
    """Inverse-volatility weights with a per-product cap.

    Products with non-positive volatility are dropped. If the cap clips any
    product the residual weight is redistributed proportionally across the
    remaining products until the weights sum to 1.0 and no product exceeds
    the cap.
    """

    if not volatilities:
        raise ValueError("build_inverse_volatility requires at least one product")
    if not 0.0 < cap <= 1.0:
        raise ValueError("inverse volatility cap must be in (0, 1]")
    filtered = {key: float(value) for key, value in volatilities.items() if value > 0}
    if not filtered:
        raise ValueError("build_inverse_volatility requires at least one positive volatility")
    if len(filtered) * cap < 1.0 - 1e-12:
        raise ValueError("inverse volatility cap is infeasible for this basket")

    # Water-fill the inverse-volatility scores.  Unlike normalising a fully
    # clipped vector, this proves both conservation and the cap at every step.
    inverse = {key: 1.0 / value for key, value in filtered.items()}
    remaining = set(inverse)
    remaining_weight = 1.0
    weights: dict[str, float] = {}
    while remaining:
        total_inverse = sum(inverse[key] for key in remaining)
        provisional = {
            key: remaining_weight * inverse[key] / total_inverse for key in remaining
        }
        clipped = [key for key, value in provisional.items() if value > cap + 1e-12]
        if not clipped:
            weights.update(provisional)
            break
        for key in clipped:
            weights[key] = cap
            remaining.remove(key)
            remaining_weight -= cap
        if remaining_weight < -1e-12 or (
            remaining and len(remaining) * cap < remaining_weight - 1e-12
        ):
            raise ValueError("inverse volatility cap is infeasible for this basket")
    return weights


@dataclass(frozen=True)
class SubLayerPortfolio:
    """One fully-funded, cap-compliant weight construction."""

    weights: Mapping[str, float]
    allocations: Mapping[str, Decimal]


@dataclass(frozen=True)
class SubLayerPortfolioEvaluation:
    """Comparable equal-weight and capped inverse-volatility baskets."""

    equal_weight: SubLayerPortfolio
    capped_inverse_volatility: SubLayerPortfolio


def _validate_portfolio_inputs(
    products: Sequence[ProductMetrics],
    returns: Mapping[str, Sequence[float]],
    budget: SubLayerBudget,
    cap: float,
    minimum_tradable_budget: Decimal,
) -> tuple[str, ...]:
    if not isinstance(budget, SubLayerBudget):
        raise ValueError("budget must be a SubLayerBudget")
    if not 0.0 < cap <= 1.0:
        raise ValueError("per_product_cap must be in (0, 1]")
    if (
        not isinstance(minimum_tradable_budget, Decimal)
        or not minimum_tradable_budget.is_finite()
        or minimum_tradable_budget < 0
    ):
        raise ValueError("minimum_tradable_budget must be a non-negative finite Decimal")
    ids = tuple(product.product_id for product in products)
    if not ids:
        raise ValueError("evaluate_sub_layer_portfolios requires at least one product")
    if len(set(ids)) != len(ids):
        raise ValueError("evaluate_sub_layer_portfolios requires unique product ids")
    if any(product.sub_layer is not budget.sub_layer for product in products):
        raise ValueError("products must belong to the budget sub-layer")
    if len(ids) * cap < 1.0 - 1e-12:
        raise ValueError("per-product cap is infeasible for this basket")
    if any(product_id not in returns for product_id in ids):
        raise ValueError("returns must include every selected product")
    return ids


def _fund_portfolio(
    weights: Mapping[str, float],
    budget: Decimal,
    minimum_tradable_budget: Decimal,
) -> SubLayerPortfolio:
    if abs(sum(weights.values()) - 1.0) > 1e-10:
        raise ValueError("portfolio weights must conserve the sub-layer budget")
    allocations: dict[str, Decimal] = {}
    product_ids = tuple(weights)
    for product_id in product_ids[:-1]:
        allocations[product_id] = budget * Decimal(str(weights[product_id]))
    allocations[product_ids[-1]] = budget - sum(allocations.values(), Decimal("0"))
    if any(value < minimum_tradable_budget for value in allocations.values()):
        raise ValueError("basket cannot fund every product at the minimum tradable budget")
    return SubLayerPortfolio(weights=dict(weights), allocations=allocations)


def evaluate_sub_layer_portfolios(
    products: Sequence[ProductMetrics],
    returns: Mapping[str, Sequence[float]],
    budget: SubLayerBudget,
    *,
    per_product_cap: float = DEFAULT_INVERSE_VOLATILITY_CAP,
    minimum_tradable_budget: Decimal = Decimal("0"),
) -> SubLayerPortfolioEvaluation:
    """Build comparable, fully funded baskets for one selected sub-layer.

    No allocation is silently re-normalised above a cap.  Infeasible cap,
    volatility, return-series, or minimum-trade constraints fail explicitly so
    freezing can refuse an untradeable basket.
    """

    ids = _validate_portfolio_inputs(
        products, returns, budget, per_product_cap, minimum_tradable_budget
    )
    equal = build_equal_weight(ids)
    if max(equal.values()) > per_product_cap + 1e-12:
        raise ValueError("per-product cap is infeasible for equal-weight basket")
    volatilities = {product_id: _pop_std(returns[product_id]) for product_id in ids}
    if any(volatility <= 0 for volatility in volatilities.values()):
        raise ValueError("returns must produce positive volatility for every product")
    inverse = build_inverse_volatility(volatilities, cap=per_product_cap)
    return SubLayerPortfolioEvaluation(
        equal_weight=_fund_portfolio(equal, budget.budget, minimum_tradable_budget),
        capped_inverse_volatility=_fund_portfolio(
            inverse, budget.budget, minimum_tradable_budget
        ),
    )


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _pop_std(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    mean = _mean(values)
    return sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def correlation(series_a: Sequence[float], series_b: Sequence[float]) -> float:
    """Pearson correlation between two equal-length return series."""

    if len(series_a) != len(series_b):
        raise ValueError("correlation requires equal-length series")
    if len(series_a) < 2:
        return 0.0
    std_a = _pop_std(series_a)
    std_b = _pop_std(series_b)
    if std_a == 0.0 or std_b == 0.0:
        return 0.0
    mean_a = _mean(series_a)
    mean_b = _mean(series_b)
    return sum((a - mean_a) * (b - mean_b) for a, b in zip(series_a, series_b)) / (len(series_a) * std_a * std_b)


def downside_correlation(
    series_a: Sequence[float], series_b: Sequence[float], threshold: float = 0.0,
) -> float:
    """Correlation restricted to sessions where either return is below ``threshold``."""

    if len(series_a) != len(series_b):
        raise ValueError("downside_correlation requires equal-length series")
    filtered_a = [a for a, b in zip(series_a, series_b) if a < threshold or b < threshold]
    filtered_b = [b for a, b in zip(series_a, series_b) if a < threshold or b < threshold]
    if len(filtered_a) < 2:
        return 0.0
    return correlation(filtered_a, filtered_b)


def drawdown_overlap(nav_a: Sequence[float], nav_b: Sequence[float]) -> float:
    """Fraction of sessions where both products are simultaneously in drawdown."""

    if len(nav_a) != len(nav_b):
        raise ValueError("drawdown_overlap requires equal-length series")
    if not nav_a:
        return 0.0
    drawdown_a = _running_drawdown(nav_a)
    drawdown_b = _running_drawdown(nav_b)
    overlapping = sum(1 for da, db in zip(drawdown_a, drawdown_b) if da < 0.0 and db < 0.0)
    return overlapping / len(nav_a)


def _running_drawdown(nav: Sequence[float]) -> list[float]:
    peak = nav[0]
    out: list[float] = []
    for value in nav:
        if value > peak:
            peak = value
        out.append(value / peak - 1.0)
    return out


def pairwise_risk(
    series: Mapping[str, Sequence[float]], *, nav: Mapping[str, Sequence[float]] | None = None,
) -> dict[tuple[str, str], PairwiseRisk]:
    """Compute pairwise correlation/downside-correlation/drawdown-overlap."""

    keys = sorted(series)
    out: dict[tuple[str, str], PairwiseRisk] = {}
    for left in keys:
        for right in keys:
            if left == right:
                continue
            returns_left = series[left]
            returns_right = series[right]
            left_nav = (nav or {}).get(left, returns_left)
            right_nav = (nav or {}).get(right, returns_right)
            out[(left, right)] = PairwiseRisk(
                correlation=correlation(returns_left, returns_right),
                downside_correlation=downside_correlation(returns_left, returns_right),
                drawdown_overlap=drawdown_overlap(left_nav, right_nav),
            )
    return out
