"""Daily coordinator for the adaptive ETF state machine."""

from dataclasses import replace
from datetime import date
from decimal import Decimal
from typing import Mapping

from .backtest_provider import AdaptiveBacktestDataProvider
from .config import AdaptiveConfig
from .contracts import CorporateAction, DualPriceBar, ETFEligibility
from .grid import evaluate_grid_close, next_grid_stop
from .grid import initial_grid_target_pct
from .indicators import IndicatorSnapshot
from .regime import next_regime
from .state import Decision, OrderReason, Regime, Side, StrategyState
from .state import BacktestEvent, BacktestRequest, BacktestResult, DailyNav, OrderIntent
from .execution import ExecutionSimulator
from .execution import apply_corporate_actions, is_protective_exit, rebase_signal_state
from .grid import apply_grid_fill
from .trend import evaluate_trend_close
from .trend import apply_trend_fill


def apply_session_actions(
    state: StrategyState, actions: tuple[CorporateAction, ...], *, old_ratio: float, new_ratio: float,
    old_offset: float = 0.0, new_offset: float = 0.0,
) -> StrategyState:
    """Apply raw ledger actions once, then preserve continuous signal levels."""
    accounted, action_ids = apply_corporate_actions(state, actions, state.applied_action_ids)
    rebased = rebase_signal_state(
        accounted, old_ratio, new_ratio, old_offset, new_offset
    )
    return replace(rebased, applied_action_ids=action_ids)


def apply_exit_fill(state: StrategyState, fill) -> StrategyState:
    """Clear price-space cycle state only after an actual full exit fill."""
    if (
        fill.reason not in {OrderReason.GRID_STOP, OrderReason.HARD_STOP, OrderReason.TREND_STOP}
        or state.position_shares != 0
    ):
        return state
    return replace(
        state,
        grid_anchor=None,
        cycle_entry_price=None,
        grid_stop_price=None,
        trend_stop_price=None,
        highest_close=None,
        units=(),
    )


def process_close(
    state: StrategyState, snapshot: IndicatorSnapshot, eligibility: ETFEligibility,
    config: AdaptiveConfig,
) -> Decision:
    """Make at most one next-session decision from only this close's facts."""
    if (
        state.position_shares > 0
        and state.cycle_entry_price is not None
        and snapshot.close < state.cycle_entry_price * 0.90
    ):
        if snapshot.signal_date is None:
            raise ValueError("hard stop requires a signal date")
        cooldown = config.grid.cooldown_sessions if state.regime is Regime.GRID else 0
        intent = OrderIntent(
            snapshot.signal_date, Side.SELL, OrderReason.HARD_STOP, snapshot.atr20,
            (("hard_stop", state.cycle_entry_price * 0.90),), 0.0, 0.0,
            "cycle hard stop full exit",
        )
        return Decision(replace(state, cooldown_remaining=cooldown), (intent,))
    if state.regime is Regime.GRID and state.cooldown_remaining > 0:
        return Decision(replace(state, cooldown_remaining=state.cooldown_remaining - 1), ())
    if (
        state.regime is Regime.GRID
        and state.position_shares > 0
        and state.grid_stop_price is not None
        and snapshot.close < state.grid_stop_price
    ):
        if snapshot.signal_date is None:
            raise ValueError("grid stop requires a signal date")
        intent = OrderIntent(
            snapshot.signal_date, Side.SELL, OrderReason.GRID_STOP, snapshot.atr20,
            (("grid_stop", state.grid_stop_price),), 0.0, 0.0,
            "GRID stop full exit",
        )
        return Decision(state, (intent,))
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
        if state.regime is Regime.GRID and state.position_shares > 0:
            if snapshot.signal_date is None or snapshot.atr20 is None:
                raise ValueError("GRID to TREND transition requires signal date and ATR20")
            trend_stop = max(
                state.grid_stop_price if state.grid_stop_price is not None else float("-inf"),
                snapshot.close - config.trend.stop_n * snapshot.atr20,
            )
            intent = OrderIntent(
                snapshot.signal_date, Side.REBALANCE, OrderReason.GRID_TO_TREND_REBALANCE,
                snapshot.atr20,
                (("entry", snapshot.close), ("trend_stop", trend_stop)),
                float(state.cash), config.trend.risk_per_unit,
                "reuse GRID inventory and calibrate first TREND unit",
            )
            return Decision(trend_state, (intent,))
        return evaluate_trend_close(trend_state, snapshot, config.trend, eligibility.eligible)
    if state.regime is Regime.GRID:
        if state.position_shares > 0 and snapshot.atr20 is not None:
            highest = max(state.highest_close or snapshot.close, snapshot.close)
            state = replace(
                state,
                highest_close=highest,
                grid_stop_price=next_grid_stop(state.grid_stop_price, highest, snapshot.atr20),
            )
        if (
            state.position_shares == 0
            and state.grid_anchor is None
            and eligibility.eligible
            and snapshot.close > snapshot.ma20
        ):
            if snapshot.signal_date is None or snapshot.atr20 is None:
                raise ValueError("grid initialization requires signal date and ATR20")
            target_budget = float(state.cash) * initial_grid_target_pct(snapshot, config.grid)
            initial = OrderIntent(
                snapshot.signal_date, Side.BUY, OrderReason.GRID_INITIALIZE,
                snapshot.atr20,
                (("entry", snapshot.close), ("lower_band", snapshot.ma20 - 2 * snapshot.std20)),
                target_budget, 0.0, "initial GRID target exposure",
            )
            return Decision(state, (initial,))
        return evaluate_grid_close(state, snapshot, config.grid, eligibility.eligible)
    return Decision(replace(state, regime=requested), ())


class AdaptiveBacktestEngine:
    """Deterministic daily runner; all fills happen before that day's close."""

    def __init__(
        self,
        config: AdaptiveConfig,
        execution: ExecutionSimulator,
        provider: AdaptiveBacktestDataProvider | None = None,
    ) -> None:
        self._config = config
        self._execution = execution
        self._provider = provider

    def run(
        self,
        request: BacktestRequest,
    ) -> BacktestResult:
        """Load all point-in-time inputs from the configured production boundary."""

        start_date, end_date = _request_range(request)
        if self._provider is None:
            raise ValueError("backtest provider is required for run")
        bars = tuple(
            self._provider.load_bars(request.stock_code, start_date, end_date)
        )
        actions = tuple(
            self._provider.load_actions(request.stock_code, start_date, end_date)
        )
        eligibility_by_date = self._provider.load_eligibility(
            request.stock_code, bars
        )
        return self.run_with_data(request, bars, eligibility_by_date, actions)

    def run_with_data(
        self,
        request: BacktestRequest,
        bars: tuple[DualPriceBar, ...],
        eligibility_by_date: Mapping[date, ETFEligibility],
        actions: tuple[CorporateAction, ...] = (),
    ) -> BacktestResult:
        """Run against explicit immutable inputs for tests and research."""

        from .indicators import compute_indicators

        _validate_run_inputs(request, bars, eligibility_by_date, actions)
        actions_by_date: dict[date, list[CorporateAction]] = {}
        for action in actions:
            actions_by_date.setdefault(action.effective_date, []).append(action)
        state = StrategyState(cash=request.initial_cash)
        pending: tuple[OrderIntent, ...] = ()
        events: list[BacktestEvent] = []
        nav: list[DailyNav] = []
        snapshots = compute_indicators(bars)
        previous_ratio: float | None = None
        previous_offset: float | None = None
        for bar, snapshot in zip(bars, snapshots):
            trading_enabled = request.trade_start_date is None or bar.trade_date >= request.trade_start_date
            if not trading_enabled:
                previous_ratio = bar.adjustment_ratio
                previous_offset = bar.adjustment_offset
                continue
            session_actions = tuple(actions_by_date.get(bar.trade_date, ()))
            previously_applied = set(state.applied_action_ids)
            state = apply_session_actions(
                state,
                session_actions,
                old_ratio=bar.adjustment_ratio if previous_ratio is None else previous_ratio,
                new_ratio=bar.adjustment_ratio,
                old_offset=bar.adjustment_offset if previous_offset is None else previous_offset,
                new_offset=bar.adjustment_offset,
            )
            recorded_action_ids: set[str] = set()
            for action in session_actions:
                if (
                    action.event_id not in previously_applied
                    and action.event_id not in recorded_action_ids
                ):
                    events.append(
                        BacktestEvent(
                            bar.trade_date,
                            "corporate_action",
                            (("event_id", action.event_id),),
                        )
                    )
                    recorded_action_ids.add(action.event_id)
            if pending:
                outcome = self._execution.execute(pending, bar, state)
                state = outcome.state
                retried: list[OrderIntent] = []
                for rejected_order in outcome.rejected_orders:
                    events.append(
                        BacktestEvent(
                            bar.trade_date,
                            "rejected_order",
                            (
                                ("side", rejected_order.side.value),
                                ("signal_date", rejected_order.intent.signal_date.isoformat()),
                                ("execution_date", bar.trade_date.isoformat()),
                                ("reason", rejected_order.reason),
                            ),
                        )
                    )
                    if (
                        is_protective_exit(rejected_order.intent.reason)
                        and state.position_shares > 0
                        and rejected_order.intent not in retried
                    ):
                        retried.append(rejected_order.intent)
                for fill in outcome.fills:
                    if fill.reason.name.startswith("GRID"):
                        state = apply_grid_fill(state, fill)
                    elif fill.reason in {
                        OrderReason.TREND_ENTRY,
                        OrderReason.TREND_ADD,
                        OrderReason.GRID_TO_TREND_REBALANCE,
                    } and (fill.side is Side.BUY or fill.reason is OrderReason.GRID_TO_TREND_REBALANCE):
                        state = apply_trend_fill(state, fill, self._config.trend)
                    state = apply_exit_fill(state, fill)
                    events.append(
                        BacktestEvent(
                            fill.fill_date,
                            "fill",
                            (
                                ("reason", fill.reason.value),
                                ("side", fill.side.value),
                                ("shares", str(fill.shares)),
                                ("raw_price", str(fill.raw_price)),
                                ("commission", str(fill.commission)),
                            ),
                        )
                    )
                pending = tuple(retried)
            if snapshot is not None:
                decision = process_close(state, snapshot, eligibility_by_date[bar.trade_date], self._config)
                state = decision.state
                if not pending:
                    pending = decision.orders
            nav.append(DailyNav(bar.trade_date, state.cash, Decimal(str(bar.raw_close)) * state.position_shares))
            previous_ratio = bar.adjustment_ratio
            previous_offset = bar.adjustment_offset
        return BacktestResult(request, tuple(events), tuple(nav))


def _request_range(request: BacktestRequest) -> tuple[date, date]:
    if request.start_date is None or request.end_date is None:
        raise ValueError("backtest request requires start_date and end_date")
    if type(request.start_date) is not date:
        raise ValueError("start_date must be a date")
    if type(request.end_date) is not date:
        raise ValueError("end_date must be a date")
    if request.start_date > request.end_date:
        raise ValueError("start_date must not be after end_date")
    return request.start_date, request.end_date


def _validate_run_inputs(
    request: BacktestRequest,
    bars: tuple[DualPriceBar, ...],
    eligibility_by_date: Mapping[date, ETFEligibility],
    actions: tuple[CorporateAction, ...],
) -> None:
    start_date, end_date = _request_range(request)
    if not bars:
        raise ValueError("bar coverage must include the requested start and end dates")
    if any(bar.stock_code != request.stock_code for bar in bars):
        raise ValueError("bar stock code must exactly match the request")
    sessions = tuple(bar.trade_date for bar in bars)
    if sessions != tuple(sorted(sessions)) or len(sessions) != len(set(sessions)):
        raise ValueError("bars must contain ordered unique sessions")
    if sessions[0] != start_date or sessions[-1] != end_date:
        raise ValueError("bar coverage must include the requested start and end dates")
    session_set = set(sessions)
    if request.trade_start_date is not None:
        if type(request.trade_start_date) is not date:
            raise ValueError("trade_start_date must be a date")
        if request.trade_start_date not in session_set:
            raise ValueError("trade_start_date must match a bar session")
    for action in actions:
        if action.stock_code != request.stock_code:
            raise ValueError("corporate action stock code must exactly match the request")
        if action.effective_date < start_date or action.effective_date > end_date:
            raise ValueError("corporate action date must be within the requested range")
        if action.effective_date not in session_set:
            raise ValueError("corporate action date must match a bar session")

    eligibility_dates = set(eligibility_by_date)
    if eligibility_dates != session_set:
        raise ValueError("eligibility coverage must exactly match bar sessions")
    if any(
        not isinstance(eligibility_by_date[session], ETFEligibility)
        for session in sessions
    ):
        raise ValueError("eligibility values must be ETFEligibility instances")
