"""Event-sourced attribution for adaptive ETF research outputs."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from types import MappingProxyType
from typing import Mapping, Sequence

from ..state import BacktestEvent, BacktestResult, DailyNav, DailyStrategyObservation, Regime


@dataclass(frozen=True)
class TradePoint:
    event_date: object
    kind: str
    reason: str
    shares: int | None
    raw_price: float | None


@dataclass(frozen=True)
class ReasonAttribution:
    reason: str
    fill_count: int
    shares: int
    traded_value: Decimal


@dataclass(frozen=True)
class ResultAttribution:
    window_id: str
    trade_points: tuple[TradePoint, ...]
    by_reason: Mapping[str, ReasonAttribution]
    invested_sessions: int
    cash_sessions: int
    rejected_order_count: int


@dataclass(frozen=True)
class ExcessAttribution:
    grid_return: float
    trend_return: float
    transition_return: float
    cash_opportunity_cost: float
    execution_cost: float
    reconciliation_error: float


def build_result_attribution(window_id: str, result: BacktestResult) -> ResultAttribution:
    """Summarize only persisted events and NAV; never regenerate strategy signals."""
    if not window_id:
        raise ValueError("window_id must be non-empty")
    points: list[TradePoint] = []
    counts: dict[str, list[Decimal | int]] = {}
    rejected = 0
    for event in result.events:
        payload = dict(event.payload)
        if event.kind == "rejected_order":
            rejected += 1
            points.append(TradePoint(event.event_date, event.kind, payload.get("reason", "unknown"), None, None))
            continue
        if event.kind != "fill":
            continue
        reason = payload.get("reason", "unknown")
        shares = int(payload["shares"]) if "shares" in payload else 0
        raw_price = float(payload["raw_price"]) if "raw_price" in payload else None
        points.append(TradePoint(event.event_date, event.kind, reason, shares, raw_price))
        aggregate = counts.setdefault(reason, [0, 0, Decimal("0")])
        aggregate[0] = int(aggregate[0]) + 1
        aggregate[1] = int(aggregate[1]) + shares
        aggregate[2] = Decimal(aggregate[2]) + Decimal(str(raw_price or 0.0)) * shares
    by_reason = {
        reason: ReasonAttribution(reason, int(values[0]), int(values[1]), Decimal(values[2]))
        for reason, values in counts.items()
    }
    invested = sum(point.market_value > 0 for point in result.nav)
    return ResultAttribution(
        window_id, tuple(points), MappingProxyType(by_reason), invested,
        len(result.nav) - invested, rejected,
    )


def build_excess_attribution(
    strategy_nav: Sequence[DailyNav],
    benchmark_nav: Sequence[DailyNav],
    observations: Sequence[DailyStrategyObservation],
    strategy_events: Sequence[BacktestEvent] = (),
    *,
    execution_cost: float | None = None,
) -> ExcessAttribution:
    """Reconcile recorded net strategy excess without replaying strategy logic.

    All return contributions are simple daily strategy-minus-benchmark returns.
    Costs are already embedded in the recorded strategy NAV, so the optional
    execution-cost diagnostic is intentionally excluded from reconciliation.
    """

    _require_aligned_nav(strategy_nav, benchmark_nav)
    ordered_observations = _require_observations_for_nav(strategy_nav, observations)

    grid = 0.0
    trend = 0.0
    transition = 0.0
    cash = 0.0
    total_excess = 0.0
    previous_regime = ordered_observations[0].regime
    transition_pending = False
    liquidation_dates = _recorded_liquidation_dates(strategy_events)
    for previous_strategy, current_strategy, previous_benchmark, current_benchmark, previous_observation, observation in zip(
        strategy_nav,
        strategy_nav[1:],
        benchmark_nav,
        benchmark_nav[1:],
        ordered_observations,
        ordered_observations[1:],
    ):
        strategy_return = _daily_return(previous_strategy, current_strategy, "strategy")
        benchmark_return = _daily_return(previous_benchmark, current_benchmark, "benchmark")
        excess = strategy_return - benchmark_return
        total_excess += excess
        transition_pending = transition_pending or (
            previous_regime is not None and observation.regime is not previous_regime
        )
        liquidated = (
            previous_observation.actual_exposure > 0.0
            and observation.actual_exposure <= 0.0
            and current_strategy.nav_date in liquidation_dates
        )
        if observation.actual_exposure <= 0.0 and not liquidated:
            cash -= benchmark_return
        elif transition_pending:
            transition += excess
            transition_pending = False
        elif observation.regime is Regime.GRID:
            grid += excess
        elif observation.regime is Regime.TREND:
            trend += excess
        else:
            raise ValueError("invested observation requires a regime")
        previous_regime = observation.regime

    components = grid + trend + transition + cash
    reconciliation_error = components - total_excess
    if abs(reconciliation_error) > 1e-9:
        raise ValueError("excess attribution does not reconcile to recorded NAV")
    diagnostic_cost = (
        _recorded_execution_cost(strategy_events)
        if execution_cost is None
        else float(execution_cost)
    )
    return ExcessAttribution(grid, trend, transition, cash, diagnostic_cost, reconciliation_error)


def _require_aligned_nav(strategy_nav: Sequence[DailyNav], benchmark_nav: Sequence[DailyNav]) -> None:
    strategy_dates = tuple(point.nav_date for point in strategy_nav)
    benchmark_dates = tuple(point.nav_date for point in benchmark_nav)
    if not strategy_nav or strategy_dates != benchmark_dates:
        raise ValueError("strategy and benchmark NAV dates must align")
    if len(set(strategy_dates)) != len(strategy_dates):
        raise ValueError("recorded NAV dates must be unique")


def _require_observations_for_nav(
    nav: Sequence[DailyNav], observations: Sequence[DailyStrategyObservation],
) -> tuple[DailyStrategyObservation, ...]:
    by_date = {item.nav_date: item for item in observations}
    nav_dates = tuple(point.nav_date for point in nav)
    if len(by_date) != len(observations) or set(by_date) != set(nav_dates):
        raise ValueError("observation date must align with recorded NAV")
    return tuple(by_date[nav_date] for nav_date in nav_dates)


def _daily_return(previous: DailyNav, current: DailyNav, series_name: str) -> float:
    if previous.total <= 0:
        raise ValueError(f"{series_name} NAV must be positive")
    return float(current.total / previous.total - 1)


def _recorded_execution_cost(events: Sequence[BacktestEvent]) -> float:
    total = Decimal("0")
    for event in events:
        if event.kind != "fill":
            continue
        payload = dict(event.payload)
        total += Decimal(payload.get("commission", "0"))
        total += Decimal(payload.get("slippage_cost", "0"))
    return float(total)


def _recorded_liquidation_dates(events: Sequence[BacktestEvent]) -> frozenset:
    return frozenset(
        event.event_date
        for event in events
        if event.kind == "fill" and dict(event.payload).get("side") == "sell"
    )
