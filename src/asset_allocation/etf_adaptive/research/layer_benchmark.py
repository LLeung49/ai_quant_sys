"""Fixed strategic-weight aggregation and layer-level benchmark gates."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import asdict, dataclass, replace
from decimal import Decimal

from ..contracts import AssetLayer, SubLayer
from .baselines import BaselineKind
from .benchmark_contracts import (
    BenchmarkSeries,
    PortfolioGate,
    StrategicPortfolio,
    evaluate_layer_research_decision,
    evaluate_portfolio_gate,
)
from .bluechip_execution import BlueChipBasketEvidence
from .decision import DecisionSummary, ResearchConclusion
from .execution_evidence import (
    ExecutionCostTurnover,
    StitchedNavPoint,
    TargetEvidence,
)

LayerEvidence = TargetEvidence | BlueChipBasketEvidence
from .metrics import PerformanceMetrics, calculate_performance


@dataclass(frozen=True)
class LayerBenchmarkResult:
    portfolio: StrategicPortfolio
    strategy_nav: tuple[float, ...]
    benchmark_nav: tuple[float, ...]
    strategy_metrics: PerformanceMetrics
    benchmark_metrics: PerformanceMetrics
    gate: PortfolioGate
    decision: DecisionSummary
    marginal_excess_contribution: Mapping[SubLayer, float]
    bluechip_member_contribution: Mapping[str, float] | None = None


def _path(evidence: LayerEvidence, kind: BaselineKind) -> tuple[StitchedNavPoint, ...]:
    path = evidence.stitched_paths.get(kind)
    if not path:
        raise ValueError(f"missing stitched {kind.value} evidence")
    return path


def _aligned_paths(
    portfolio: StrategicPortfolio,
    evidence_by_exposure: Mapping[SubLayer, LayerEvidence],
) -> tuple[dict[SubLayer, tuple[StitchedNavPoint, ...]], dict[SubLayer, tuple[StitchedNavPoint, ...]]]:
    if set(evidence_by_exposure) != set(portfolio.weights):
        raise ValueError("evidence must exactly cover portfolio weights")
    strategy: dict[SubLayer, tuple[StitchedNavPoint, ...]] = {}
    benchmark: dict[SubLayer, tuple[StitchedNavPoint, ...]] = {}
    reference_dates = None
    reference_windows = None
    for sub_layer in portfolio.weights:
        evidence = evidence_by_exposure[sub_layer]
        evidence_sub_layer = (
            evidence.entry.sub_layer
            if isinstance(evidence, TargetEvidence)
            else SubLayer.DEFENSIVE_BLUE_CHIP
        )
        if evidence_sub_layer is not sub_layer:
            raise ValueError("evidence sub-layer does not match portfolio weight")
        strategy[sub_layer] = _path(evidence, BaselineKind.FULL_ADAPTIVE)
        benchmark[sub_layer] = _path(evidence, BaselineKind.BUY_AND_HOLD)
        dates = tuple(point.nav_date for point in strategy[sub_layer])
        if dates != tuple(point.nav_date for point in benchmark[sub_layer]):
            raise ValueError("strategy and benchmark evidence must be aligned")
        window_ids = tuple(point.window_id for point in strategy[sub_layer])
        if window_ids != tuple(point.window_id for point in benchmark[sub_layer]):
            raise ValueError("strategy and benchmark window boundaries must be aligned")
        if reference_dates is None:
            reference_dates = dates
            reference_windows = window_ids
        elif dates != reference_dates:
            raise ValueError("all exposure evidence must be aligned")
        elif window_ids != reference_windows:
            raise ValueError("all exposure window boundaries must be aligned")
    return strategy, benchmark


def _weighted_nav(
    weights: Mapping[SubLayer, float], paths: Mapping[SubLayer, tuple[StitchedNavPoint, ...]]
) -> tuple[float, ...]:
    count = len(next(iter(paths.values())))
    return tuple(
        sum(weights[sub_layer] * paths[sub_layer][index].nav_total for sub_layer in weights)
        for index in range(count)
    )


def _window_excess_returns(
    strategy_nav: tuple[float, ...],
    benchmark_nav: tuple[float, ...],
    paths: Mapping[SubLayer, tuple[StitchedNavPoint, ...]],
) -> tuple[float, ...]:
    """Return one aligned strategy-minus-B&H return for each OOS window."""

    reference = next(iter(paths.values()))
    grouped: list[tuple[str, list[int]]] = []
    for index, point in enumerate(reference):
        if not grouped or grouped[-1][0] != point.window_id:
            if any(window_id == point.window_id for window_id, _ in grouped):
                raise ValueError("OOS window boundaries must not repeat")
            grouped.append((point.window_id, []))
        grouped[-1][1].append(index)
    if not grouped:
        raise ValueError("layer evidence must contain at least one OOS observation")
    strategy_basis = strategy_nav[0]
    benchmark_basis = benchmark_nav[0]
    excess_returns: list[float] = []
    for _, indexes in grouped:
        strategy_end = strategy_nav[indexes[-1]]
        benchmark_end = benchmark_nav[indexes[-1]]
        excess_returns.append(
            (strategy_end / strategy_basis - 1.0)
            - (benchmark_end / benchmark_basis - 1.0)
        )
        strategy_basis = strategy_end
        benchmark_basis = benchmark_end
    return tuple(excess_returns)


def _initial_cash(evidence: LayerEvidence) -> Decimal:
    initial_cash = (
        evidence.initial_cash
        if isinstance(evidence, TargetEvidence)
        else evidence.initial_cash
    )
    if (
        not isinstance(initial_cash, Decimal)
        or not initial_cash.is_finite()
        or initial_cash <= 0
    ):
        raise ValueError("layer execution evidence requires positive initial_cash")
    return initial_cash


def _recorded_execution_evidence(
    portfolio: StrategicPortfolio,
    evidence_by_exposure: Mapping[SubLayer, LayerEvidence],
    kind: BaselineKind,
) -> ExecutionCostTurnover:
    total_cost = 0.0
    turnover = 0.0
    for sub_layer, weight in portfolio.weights.items():
        recorded = evidence_by_exposure[sub_layer].execution_evidence.get(kind)
        if not isinstance(recorded, ExecutionCostTurnover):
            raise ValueError(f"missing recorded execution evidence for {kind.value}")
        total_cost += weight * recorded.total_cost
        turnover += weight * recorded.turnover
    return ExecutionCostTurnover(total_cost, turnover)


def aggregate_layer_evidence(
    portfolio: StrategicPortfolio,
    evidence_by_exposure: Mapping[SubLayer, LayerEvidence],
) -> LayerBenchmarkResult:
    """Aggregate fixed layer weights and evaluate the approved layer gate."""

    if not isinstance(portfolio, StrategicPortfolio):
        raise ValueError("portfolio must be a StrategicPortfolio")
    strategy_paths, benchmark_paths = _aligned_paths(portfolio, evidence_by_exposure)
    strategy_nav = _weighted_nav(portfolio.weights, strategy_paths)
    benchmark_nav = _weighted_nav(portfolio.weights, benchmark_paths)
    initial_cash_values = {_initial_cash(evidence) for evidence in evidence_by_exposure.values()}
    if len(initial_cash_values) != 1:
        raise ValueError("layer evidence must share one initial_cash basis")
    initial_cash = float(initial_cash_values.pop())
    strategy_execution = _recorded_execution_evidence(
        portfolio, evidence_by_exposure, BaselineKind.FULL_ADAPTIVE,
    )
    benchmark_execution = _recorded_execution_evidence(
        portfolio, evidence_by_exposure, BaselineKind.BUY_AND_HOLD,
    )
    strategy_metrics = replace(
        calculate_performance(
            tuple(nav * initial_cash for nav in strategy_nav), (),
        ),
        total_cost=strategy_execution.total_cost,
        turnover=strategy_execution.turnover,
    )
    benchmark_metrics = replace(
        calculate_performance(
            tuple(nav * initial_cash for nav in benchmark_nav), (),
        ),
        total_cost=benchmark_execution.total_cost,
        turnover=benchmark_execution.turnover,
    )
    window_excess_returns = _window_excess_returns(
        strategy_nav, benchmark_nav, strategy_paths,
    )
    gate = evaluate_portfolio_gate(
        BenchmarkSeries("full_adaptive", strategy_metrics.annual_return, strategy_metrics.max_drawdown),
        BenchmarkSeries("buy_and_hold", benchmark_metrics.annual_return, benchmark_metrics.max_drawdown),
        window_excess_returns,
    )
    decision = evaluate_layer_research_decision(
        gate=gate,
        strategy_metrics=strategy_metrics,
        benchmark_metrics=benchmark_metrics,
        initial_oos_nav=strategy_nav[0] * initial_cash,
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
        strategy_metrics=strategy_metrics,
        benchmark_metrics=benchmark_metrics,
        gate=gate,
        decision=decision,
        marginal_excess_contribution=contribution,
    )


def aggregate_defensive_evidence(
    dividend: TargetEvidence,
    bluechip: BlueChipBasketEvidence,
) -> LayerBenchmarkResult:
    """Aggregate the approved defensive ETF plus historical blue-chip basket."""

    if not isinstance(dividend, TargetEvidence):
        raise ValueError("dividend must be TargetEvidence")
    if dividend.entry.sub_layer is not SubLayer.DEFENSIVE_DIVIDEND_ETF:
        raise ValueError("dividend evidence must be defensive dividend ETF")
    if not isinstance(bluechip, BlueChipBasketEvidence):
        raise ValueError("bluechip must be BlueChipBasketEvidence")
    result = aggregate_layer_evidence(
        StrategicPortfolio(
            "defensive_strategy",
            AssetLayer.DEFENSIVE,
            {
                SubLayer.DEFENSIVE_DIVIDEND_ETF: 0.6429,
                SubLayer.DEFENSIVE_BLUE_CHIP: 0.3571,
            },
        ),
        {
            SubLayer.DEFENSIVE_DIVIDEND_ETF: dividend,
            SubLayer.DEFENSIVE_BLUE_CHIP: bluechip,
        },
    )
    contribution = {
        code: 0.3571
        * (
            value
            - bluechip.paths[BaselineKind.BUY_AND_HOLD].member_contribution[code]
        )
        for code, value in bluechip.paths[
            BaselineKind.FULL_ADAPTIVE
        ].member_contribution.items()
    }
    return LayerBenchmarkResult(
        portfolio=result.portfolio,
        strategy_nav=result.strategy_nav,
        benchmark_nav=result.benchmark_nav,
        strategy_metrics=result.strategy_metrics,
        benchmark_metrics=result.benchmark_metrics,
        gate=result.gate,
        decision=result.decision,
        marginal_excess_contribution=result.marginal_excess_contribution,
        bluechip_member_contribution=contribution,
    )


def layer_benchmark_artifact(result: LayerBenchmarkResult) -> dict[str, object]:
    """Return the deterministic report/freeze payload for one layer result."""

    if not isinstance(result, LayerBenchmarkResult):
        raise ValueError("result must be a LayerBenchmarkResult")
    artifact = {
        "passed": result.decision.conclusion is ResearchConclusion.PASSED,
        "return_passed": result.gate.return_passed,
        "drawdown_passed": result.gate.drawdown_passed,
        "majority_windows_passed": result.gate.majority_windows_passed,
        "strategy_metrics": asdict(result.strategy_metrics),
        "benchmark_metrics": asdict(result.benchmark_metrics),
        "decision": {
            "conclusion": result.decision.conclusion.value,
            "blockers": list(result.decision.blockers),
        },
        "strategy_nav": result.strategy_nav,
        "benchmark_nav": result.benchmark_nav,
        "marginal_excess_contribution": {
            sub_layer.value: result.marginal_excess_contribution[sub_layer]
            for sub_layer in sorted(result.marginal_excess_contribution, key=lambda item: item.value)
        },
    }
    if result.bluechip_member_contribution is not None:
        artifact["bluechip_member_contribution"] = {
            stock_code: result.bluechip_member_contribution[stock_code]
            for stock_code in sorted(result.bluechip_member_contribution)
        }
    return artifact


__all__ = [
    "LayerBenchmarkResult",
    "aggregate_defensive_evidence",
    "aggregate_layer_evidence",
    "layer_benchmark_artifact",
]
