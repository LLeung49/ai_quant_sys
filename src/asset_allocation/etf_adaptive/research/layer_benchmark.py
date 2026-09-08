"""Fixed strategic-weight aggregation and layer-level benchmark gates."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from ..contracts import SubLayer
from .baselines import BaselineKind
from .benchmark_contracts import BenchmarkSeries, PortfolioGate, StrategicPortfolio, evaluate_portfolio_gate
from .execution_evidence import StitchedNavPoint, TargetEvidence
from .metrics import calculate_performance


@dataclass(frozen=True)
class LayerBenchmarkResult:
    portfolio: StrategicPortfolio
    strategy_nav: tuple[float, ...]
    benchmark_nav: tuple[float, ...]
    gate: PortfolioGate
    marginal_excess_contribution: Mapping[SubLayer, float]


def _path(evidence: TargetEvidence, kind: BaselineKind) -> tuple[StitchedNavPoint, ...]:
    path = evidence.stitched_paths.get(kind)
    if not path:
        raise ValueError(f"missing stitched {kind.value} evidence")
    return path


def _aligned_paths(
    portfolio: StrategicPortfolio,
    evidence_by_exposure: Mapping[SubLayer, TargetEvidence],
) -> tuple[dict[SubLayer, tuple[StitchedNavPoint, ...]], dict[SubLayer, tuple[StitchedNavPoint, ...]]]:
    if set(evidence_by_exposure) != set(portfolio.weights):
        raise ValueError("evidence must exactly cover portfolio weights")
    strategy: dict[SubLayer, tuple[StitchedNavPoint, ...]] = {}
    benchmark: dict[SubLayer, tuple[StitchedNavPoint, ...]] = {}
    reference_dates = None
    for sub_layer in portfolio.weights:
        evidence = evidence_by_exposure[sub_layer]
        if evidence.entry.sub_layer is not sub_layer:
            raise ValueError("evidence sub-layer does not match portfolio weight")
        strategy[sub_layer] = _path(evidence, BaselineKind.FULL_ADAPTIVE)
        benchmark[sub_layer] = _path(evidence, BaselineKind.BUY_AND_HOLD)
        dates = tuple(point.nav_date for point in strategy[sub_layer])
        if dates != tuple(point.nav_date for point in benchmark[sub_layer]):
            raise ValueError("strategy and benchmark evidence must be aligned")
        if reference_dates is None:
            reference_dates = dates
        elif dates != reference_dates:
            raise ValueError("all exposure evidence must be aligned")
    return strategy, benchmark


def _weighted_nav(
    weights: Mapping[SubLayer, float], paths: Mapping[SubLayer, tuple[StitchedNavPoint, ...]]
) -> tuple[float, ...]:
    count = len(next(iter(paths.values())))
    return tuple(
        sum(weights[sub_layer] * paths[sub_layer][index].nav_total for sub_layer in weights)
        for index in range(count)
    )


def aggregate_layer_evidence(
    portfolio: StrategicPortfolio,
    evidence_by_exposure: Mapping[SubLayer, TargetEvidence],
) -> LayerBenchmarkResult:
    """Aggregate fixed layer weights and evaluate the approved layer gate."""

    if not isinstance(portfolio, StrategicPortfolio):
        raise ValueError("portfolio must be a StrategicPortfolio")
    strategy_paths, benchmark_paths = _aligned_paths(portfolio, evidence_by_exposure)
    strategy_nav = _weighted_nav(portfolio.weights, strategy_paths)
    benchmark_nav = _weighted_nav(portfolio.weights, benchmark_paths)
    strategy_metrics = calculate_performance(strategy_nav, ())
    benchmark_metrics = calculate_performance(benchmark_nav, ())
    excess = (strategy_nav[-1] / strategy_nav[0] - 1.0) - (
        benchmark_nav[-1] / benchmark_nav[0] - 1.0
    )
    gate = evaluate_portfolio_gate(
        BenchmarkSeries("full_adaptive", strategy_metrics.annual_return, strategy_metrics.max_drawdown),
        BenchmarkSeries("buy_and_hold", benchmark_metrics.annual_return, benchmark_metrics.max_drawdown),
        (excess,),
    )
    contribution = {
        sub_layer: portfolio.weights[sub_layer]
        * (strategy_paths[sub_layer][-1].nav_total - benchmark_paths[sub_layer][-1].nav_total)
        for sub_layer in portfolio.weights
    }
    return LayerBenchmarkResult(
        portfolio=portfolio,
        strategy_nav=strategy_nav,
        benchmark_nav=benchmark_nav,
        gate=gate,
        marginal_excess_contribution=contribution,
    )


__all__ = ["LayerBenchmarkResult", "aggregate_layer_evidence"]
