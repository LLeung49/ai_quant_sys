"""Daily coordinator for the adaptive ETF state machine."""

from dataclasses import replace
from decimal import Decimal
from typing import Mapping

from .config import AdaptiveConfig
from .contracts import ETFEligibility
from .grid import evaluate_grid_close
from .indicators import IndicatorSnapshot
from .regime import next_regime
from .state import Decision, Regime, StrategyState
from .state import BacktestEvent, BacktestRequest, BacktestResult, DailyNav, OrderIntent
from .execution import ExecutionSimulator
from .grid import apply_grid_fill
from .trend import evaluate_trend_close
from .trend import apply_trend_fill


def process_close(
    state: StrategyState, snapshot: IndicatorSnapshot, eligibility: ETFEligibility,
    config: AdaptiveConfig,
) -> Decision:
    """Make at most one next-session decision from only this close's facts."""
    if snapshot.adx is None:
        return Decision(state, ())
    requested = next_regime(state.regime, snapshot.adx)
    if requested is None:
        return Decision(state, ())
    if state.regime is Regime.TREND:
        # A TREND exit always receives priority over a mode transition.
        trend = evaluate_trend_close(state, snapshot, config.trend, eligibility.eligible)
        if trend.orders or requested is Regime.TREND:
            return trend
        if state.position_shares:
            return Decision(replace(state, pending_grid=True), ())
        return Decision(replace(state, regime=Regime.GRID), ())
    if requested is Regime.TREND:
        trend_state = replace(state, regime=Regime.TREND)
        return evaluate_trend_close(trend_state, snapshot, config.trend, eligibility.eligible)
    if state.regime is Regime.GRID:
        return evaluate_grid_close(state, snapshot, config.grid, eligibility.eligible)
    return Decision(replace(state, regime=requested), ())


class AdaptiveBacktestEngine:
    """Deterministic daily runner; all fills happen before that day's close."""

    def __init__(self, config: AdaptiveConfig, execution: ExecutionSimulator) -> None:
        self._config = config
        self._execution = execution

    def run(
        self, request: BacktestRequest, bars: tuple, eligibility_by_date: Mapping,
    ) -> BacktestResult:
        from .indicators import compute_indicators

        state = StrategyState(cash=request.initial_cash)
        pending: tuple[OrderIntent, ...] = ()
        events: list[BacktestEvent] = []
        nav: list[DailyNav] = []
        snapshots = compute_indicators(bars)
        for bar, snapshot in zip(bars, snapshots):
            if pending:
                outcome = self._execution.execute(pending, bar, state)
                state = outcome.state
                for fill in outcome.fills:
                    if fill.reason.name.startswith("GRID"):
                        state = apply_grid_fill(state, fill)
                    elif fill.reason.name.startswith("TREND") and fill.side.value == "buy":
                        state = apply_trend_fill(state, fill, self._config.trend)
                    events.append(BacktestEvent(fill.fill_date, "fill", (("reason", fill.reason.value), ("shares", str(fill.shares)))))
                pending = ()
            if snapshot is not None:
                decision = process_close(state, snapshot, eligibility_by_date[bar.trade_date], self._config)
                state, pending = decision.state, decision.orders
            nav.append(DailyNav(bar.trade_date, state.cash, Decimal(str(bar.raw_close)) * state.position_shares))
        return BacktestResult(request, tuple(events), tuple(nav))
