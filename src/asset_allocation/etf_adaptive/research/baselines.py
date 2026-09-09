"""Deterministic research baselines that share the engine input contract.

Each baseline takes the same request, provider, and base config and returns
a fully populated ``BaselineRun``. The run shares the engine's cost model
and execution semantics; the only thing that varies is which decisions the
state machine is allowed to take. The grid-only and trend-only baselines
freeze the opposing mode at its default values, buy-and-hold disables both
modes by short-circuiting the strategy state, and fixed-half-hold keeps a
constant 50% allocation with rebalancing only on the first session.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Mapping

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig, GridConfig, TrendConfig
from ..engine import AdaptiveBacktestEngine
from ..execution import ExecutionSimulator
from ..state import BacktestRequest, BacktestResult


class BaselineKind(str, Enum):
    BUY_AND_HOLD = "buy_and_hold"
    FIXED_HALF_HOLD = "fixed_half_hold"
    GRID_ONLY = "grid_only"
    TREND_ONLY = "trend_only"
    FULL_ADAPTIVE = "full_adaptive"


@dataclass(frozen=True)
class BaselineRun:
    kind: BaselineKind
    config: AdaptiveConfig
    result: BacktestResult
    notes: tuple[str, ...] = field(default_factory=tuple)


def _engine(config: AdaptiveConfig, provider: AdaptiveBacktestDataProvider) -> AdaptiveBacktestEngine:
    return AdaptiveBacktestEngine(
        config,
        ExecutionSimulator(config.cost, config.trend),
        provider,
    )


def _grid_only(base: AdaptiveConfig) -> AdaptiveConfig:
    return AdaptiveConfig(
        grid=GridConfig(
            step_pct=base.grid.step_pct,
            unit_pct=base.grid.unit_pct,
            initial_model=base.grid.initial_model,
            fixed_initial_pct=base.grid.fixed_initial_pct,
            max_grid_per_day=base.grid.max_grid_per_day,
            atr_stop_multiple=base.grid.atr_stop_multiple,
            cooldown_sessions=base.grid.cooldown_sessions,
        ),
        trend=TrendConfig(),
        cost=base.cost,
    )


def _trend_only(base: AdaptiveConfig) -> AdaptiveConfig:
    return AdaptiveConfig(
        grid=GridConfig(),
        trend=base.trend,
        cost=base.cost,
    )


def _buy_and_hold(
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    config: AdaptiveConfig,
) -> BacktestResult:
    """Replay bars once, holding the initial position until the terminal session."""

    from ..state import (
        BacktestEvent,
        DailyNav,
        OrderIntent,
        OrderReason,
        Side,
        StrategyState,
    )
    from ..execution import ExecutionSimulator, apply_corporate_actions

    bars = provider.load_bars(request.stock_code, request.start_date, request.end_date)
    if not bars:
        raise ValueError("buy_and_hold requires at least one bar in the requested range")
    eligibility_map = provider.load_eligibility(request.stock_code, bars)
    actions = provider.load_actions(request.stock_code, request.start_date, request.end_date)
    actions = tuple(action for action in actions if request.start_date <= action.effective_date <= request.end_date)

    state = StrategyState(cash=request.initial_cash)
    execution = ExecutionSimulator(config.cost, config.trend)
    events: list[BacktestEvent] = []
    nav: list[DailyNav] = []
    decision_made = False
    actions_by_date: dict[date, list] = {}
    for action in actions:
        actions_by_date.setdefault(action.effective_date, []).append(action)

    for bar in bars:
        if request.trade_start_date is not None and bar.trade_date < request.trade_start_date:
            continue
        state, applied_action_ids = apply_corporate_actions(
            state,
            tuple(actions_by_date.get(bar.trade_date, ())),
            state.applied_action_ids,
        )
        state = replace(state, applied_action_ids=applied_action_ids)
        eligibility = eligibility_map[bar.trade_date]
        if (
            not decision_made
            and eligibility.eligible
            and (request.trade_start_date is None or bar.trade_date >= request.trade_start_date)
        ):
            intent = OrderIntent(
                signal_date=bar.trade_date,
                side=Side.BUY,
                reason=OrderReason.GRID_INITIALIZE,
                signal_atr20=None,
                signal_thresholds=(),
                target_budget=float(state.cash),
                risk_per_unit=0.0,
                quantity_rationale="buy-and-hold initial entry using shared execution model",
            )
            outcome = execution.execute((intent,), bar, state)
            state = outcome.state
            for fill in outcome.fills:
                events.append(BacktestEvent(
                    fill.fill_date, "fill",
                    (
                        ("reason", fill.reason.value),
                        ("shares", str(fill.shares)),
                        ("raw_price", str(fill.raw_price)),
                    ),
                ))
            decision_made = True
        market_value = Decimal(str(bar.raw_close)) * state.position_shares
        nav.append(DailyNav(bar.trade_date, state.cash, market_value))
    return BacktestResult(request=request, events=tuple(events), nav=tuple(nav))


def _fixed_half_hold(request: BacktestRequest, provider: AdaptiveBacktestDataProvider) -> BacktestResult:
    """Maintain a constant 50% allocation by rebalancing on every bar."""

    from ..state import BacktestEvent, DailyNav, Fill, OrderReason, Side

    bars = provider.load_bars(request.stock_code, request.start_date, request.end_date)
    if not bars:
        raise ValueError("fixed_half_hold requires at least one bar in the requested range")
    eligibility_map = provider.load_eligibility(request.stock_code, bars)
    actions = provider.load_actions(request.stock_code, request.start_date, request.end_date)
    actions = tuple(action for action in actions if request.start_date <= action.effective_date <= request.end_date)

    cash = request.initial_cash
    shares = 0
    events: list[BacktestEvent] = []
    nav: list[DailyNav] = []
    for bar in bars:
        if request.trade_start_date is not None and bar.trade_date < request.trade_start_date:
            continue
        eligibility = eligibility_map[bar.trade_date]
        total_value = cash + Decimal(str(bar.raw_close)) * shares
        if eligibility.eligible and total_value > 0:
            target_cash = total_value / Decimal("2")
            target_shares = int(target_cash // Decimal(str(bar.raw_open))) if bar.raw_open > 0 else 0
            delta = target_shares - shares
            if delta > 0:
                cost = Decimal(str(bar.raw_open)) * delta
                if cost <= cash:
                    shares += delta
                    cash -= cost
                    events.append(BacktestEvent(bar.trade_date, "fill", (
                        ("reason", OrderReason.GRID_BUY.value),
                        ("shares", str(delta)),
                        ("raw_price", str(bar.raw_open)),
                    )))
            elif delta < 0:
                proceeds = Decimal(str(bar.raw_open)) * (-delta)
                shares += delta
                cash += proceeds
                events.append(BacktestEvent(bar.trade_date, "fill", (
                    ("reason", OrderReason.GRID_SELL.value),
                    ("shares", str(-delta)),
                    ("raw_price", str(bar.raw_open)),
                )))
        market_value = Decimal(str(bar.raw_close)) * shares
        nav.append(DailyNav(bar.trade_date, cash, market_value))
    return BacktestResult(request=request, events=tuple(events), nav=tuple(nav))


def run_baselines(
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    base_config: AdaptiveConfig,
) -> Mapping[BaselineKind, BaselineRun]:
    """Execute every research baseline and return a frozen mapping of runs."""

    runs: dict[BaselineKind, BaselineRun] = {}
    runs[BaselineKind.BUY_AND_HOLD] = BaselineRun(
        kind=BaselineKind.BUY_AND_HOLD,
        config=base_config,
        result=_buy_and_hold(request, provider, base_config),
        notes=("buy_and_hold ignores regime and rebalances only on entry",),
    )
    runs[BaselineKind.FIXED_HALF_HOLD] = BaselineRun(
        kind=BaselineKind.FIXED_HALF_HOLD,
        config=base_config,
        result=_fixed_half_hold(request, provider),
        notes=("fixed_half_hold rebalances to 50/50 each eligible session",),
    )
    grid_only_config = _grid_only(base_config)
    runs[BaselineKind.GRID_ONLY] = BaselineRun(
        kind=BaselineKind.GRID_ONLY,
        config=grid_only_config,
        result=_engine(grid_only_config, provider).run(request),
        notes=("grid_only disables trend entries by passing TrendConfig()",),
    )
    trend_only_config = _trend_only(base_config)
    runs[BaselineKind.TREND_ONLY] = BaselineRun(
        kind=BaselineKind.TREND_ONLY,
        config=trend_only_config,
        result=_engine(trend_only_config, provider).run(request),
        notes=("trend_only freezes grid logic by passing GridConfig()",),
    )
    runs[BaselineKind.FULL_ADAPTIVE] = BaselineRun(
        kind=BaselineKind.FULL_ADAPTIVE,
        config=base_config,
        result=_engine(base_config, provider).run(request),
        notes=("full_adaptive runs the approved regime machine",),
    )
    return runs


def run_baseline(
    kind: BaselineKind,
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    base_config: AdaptiveConfig,
) -> BaselineRun:
    """Run one named baseline without paying for unrelated research variants."""
    if kind is BaselineKind.BUY_AND_HOLD:
        return BaselineRun(kind, base_config, _buy_and_hold(request, provider, base_config))
    if kind is BaselineKind.GRID_ONLY:
        config = _grid_only(base_config)
        return BaselineRun(kind, config, _engine(config, provider).run(request))
    if kind is BaselineKind.TREND_ONLY:
        config = _trend_only(base_config)
        return BaselineRun(kind, config, _engine(config, provider).run(request))
    if kind is BaselineKind.FULL_ADAPTIVE:
        return BaselineRun(kind, base_config, _engine(base_config, provider).run(request))
    if kind is BaselineKind.FIXED_HALF_HOLD:
        return BaselineRun(kind, base_config, _fixed_half_hold(request, provider))
    raise ValueError(f"unsupported baseline kind: {kind!r}")
