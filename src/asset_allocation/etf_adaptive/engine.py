"""Daily coordinator for the adaptive ETF state machine."""

from dataclasses import replace
from decimal import Decimal
from typing import Mapping

from .config import AdaptiveConfig
from .contracts import CorporateAction, ETFEligibility
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
) -> StrategyState:
    """Apply raw ledger actions once, then preserve continuous signal levels."""
    accounted, action_ids = apply_corporate_actions(state, actions, state.applied_action_ids)
    rebased = rebase_signal_state(accounted, old_ratio, new_ratio)
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

    def __init__(self, config: AdaptiveConfig, execution: ExecutionSimulator) -> None:
        self._config = config
        self._execution = execution

    def run(
        self,
        request: BacktestRequest,
        bars: tuple,
        eligibility_by_date: Mapping,
        actions_by_date: Mapping | None = None,
    ) -> BacktestResult:
        from .indicators import compute_indicators

        state = StrategyState(cash=request.initial_cash)
        pending: tuple[OrderIntent, ...] = ()
        events: list[BacktestEvent] = []
        nav: list[DailyNav] = []
        snapshots = compute_indicators(bars)
        previous_ratio: float | None = None
        for bar, snapshot in zip(bars, snapshots):
            actions = () if actions_by_date is None else actions_by_date.get(bar.trade_date, ())
            previously_applied = set(state.applied_action_ids)
            state = apply_session_actions(
                state,
                actions,
                old_ratio=bar.adjustment_ratio if previous_ratio is None else previous_ratio,
                new_ratio=bar.adjustment_ratio,
            )
            recorded_action_ids: set[str] = set()
            for action in actions:
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
                    events.append(BacktestEvent(fill.fill_date, "fill", (("reason", fill.reason.value), ("shares", str(fill.shares)))))
                pending = tuple(retried)
            if snapshot is not None:
                decision = process_close(state, snapshot, eligibility_by_date[bar.trade_date], self._config)
                state = decision.state
                if not pending:
                    pending = decision.orders
            nav.append(DailyNav(bar.trade_date, state.cash, Decimal(str(bar.raw_close)) * state.position_shares))
            previous_ratio = bar.adjustment_ratio
        return BacktestResult(request, tuple(events), tuple(nav))
