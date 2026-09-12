"""Capability-scoped close and fill policies for the adaptive ETF strategy."""

from dataclasses import replace
from typing import Protocol

from .config import AdaptiveConfig
from .contracts import ETFEligibility
from .grid import apply_grid_fill, evaluate_grid_close, initial_grid_target_pct, next_grid_stop
from .indicators import IndicatorSnapshot
from .regime import next_regime
from .state import Decision, Fill, OrderIntent, OrderReason, Regime, Side, StrategyState
from .trend import apply_trend_fill, evaluate_trend_close


class StrategyPolicy(Protocol):
    """Defines which adaptive-strategy capabilities a run may exercise."""

    policy_id: str

    def process_close(
        self,
        state: StrategyState,
        snapshot: IndicatorSnapshot,
        eligibility: ETFEligibility,
        config: AdaptiveConfig,
    ) -> Decision: ...

    def apply_fill(
        self,
        state: StrategyState,
        fill: Fill,
        config: AdaptiveConfig,
    ) -> StrategyState: ...


def apply_exit_fill(state: StrategyState, fill: Fill) -> StrategyState:
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


def _hard_stop(state: StrategyState, snapshot: IndicatorSnapshot, config: AdaptiveConfig) -> Decision | None:
    if (
        state.position_shares <= 0
        or state.cycle_entry_price is None
        or snapshot.close >= state.cycle_entry_price * 0.90
    ):
        return None
    if snapshot.signal_date is None:
        raise ValueError("hard stop requires a signal date")
    cooldown = config.grid.cooldown_sessions if state.regime is Regime.GRID else 0
    intent = OrderIntent(
        snapshot.signal_date, Side.SELL, OrderReason.HARD_STOP, snapshot.atr20,
        (("hard_stop", state.cycle_entry_price * 0.90),), 0.0, 0.0,
        "cycle hard stop full exit",
    )
    return Decision(replace(state, cooldown_remaining=cooldown), (intent,))


def _process_grid_close(
    state: StrategyState,
    snapshot: IndicatorSnapshot,
    eligibility: ETFEligibility,
    config: AdaptiveConfig,
) -> Decision:
    if state.cooldown_remaining > 0:
        return Decision(replace(state, cooldown_remaining=state.cooldown_remaining - 1), ())
    if (
        state.position_shares > 0
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


class FullAdaptivePolicy:
    """The legacy adaptive behavior, composed behind the policy boundary."""

    policy_id = "full_adaptive"

    def process_close(
        self,
        state: StrategyState,
        snapshot: IndicatorSnapshot,
        eligibility: ETFEligibility,
        config: AdaptiveConfig,
    ) -> Decision:
        hard_stop = _hard_stop(state, snapshot, config)
        if hard_stop is not None:
            return hard_stop
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

    def apply_fill(self, state: StrategyState, fill: Fill, config: AdaptiveConfig) -> StrategyState:
        if fill.reason.name.startswith("GRID"):
            state = apply_grid_fill(state, fill)
        if fill.reason in {
            OrderReason.TREND_ENTRY,
            OrderReason.TREND_ADD,
            OrderReason.GRID_TO_TREND_REBALANCE,
        } and (fill.side is Side.BUY or fill.reason is OrderReason.GRID_TO_TREND_REBALANCE):
            state = apply_trend_fill(state, fill, config.trend)
        return apply_exit_fill(state, fill)


class GridOnlyPolicy:
    """GRID initialization, trading, stops, and fill state without TREND transitions."""

    policy_id = "grid_only"

    def process_close(
        self,
        state: StrategyState,
        snapshot: IndicatorSnapshot,
        eligibility: ETFEligibility,
        config: AdaptiveConfig,
    ) -> Decision:
        grid_state = state if state.regime is Regime.GRID else replace(state, regime=Regime.GRID)
        hard_stop = _hard_stop(grid_state, snapshot, config)
        if hard_stop is not None:
            return hard_stop
        return _process_grid_close(grid_state, snapshot, eligibility, config)

    def apply_fill(self, state: StrategyState, fill: Fill, config: AdaptiveConfig) -> StrategyState:
        return apply_exit_fill(apply_grid_fill(state, fill), fill)


class TrendOnlyPolicy:
    """TREND entry, adds, stops, and fill state without GRID transitions."""

    policy_id = "trend_only"

    def process_close(
        self,
        state: StrategyState,
        snapshot: IndicatorSnapshot,
        eligibility: ETFEligibility,
        config: AdaptiveConfig,
    ) -> Decision:
        trend_state = state if state.regime is Regime.TREND else replace(state, regime=Regime.TREND)
        return evaluate_trend_close(trend_state, snapshot, config.trend, eligibility.eligible)

    def apply_fill(self, state: StrategyState, fill: Fill, config: AdaptiveConfig) -> StrategyState:
        if fill.reason in {OrderReason.TREND_ENTRY, OrderReason.TREND_ADD} and fill.side is Side.BUY:
            state = apply_trend_fill(state, fill, config.trend)
        return apply_exit_fill(state, fill)


FULL_ADAPTIVE_POLICY: StrategyPolicy = FullAdaptivePolicy()
GRID_ONLY_POLICY: StrategyPolicy = GridOnlyPolicy()
TREND_ONLY_POLICY: StrategyPolicy = TrendOnlyPolicy()
