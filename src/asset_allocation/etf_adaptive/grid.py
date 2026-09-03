"""GRID close decisions in signal-price coordinates."""

from dataclasses import replace

from .config import GridConfig
from .indicators import IndicatorSnapshot
from .state import Decision, Fill, OrderIntent, OrderReason, Side, StrategyState


def next_grid_stop(previous: float | None, highest_close: float, atr20: float) -> float:
    """Return the monotone signal-coordinate GRID stop."""
    candidate = highest_close - 3.0 * atr20
    return candidate if previous is None else max(previous, candidate)


def initial_grid_target_pct(snapshot: IndicatorSnapshot, config: GridConfig) -> float:
    """Choose the initial target exposure, always constrained to [0, 1]."""
    if config.initial_model == "bollinger_position":
        if snapshot.std20 <= 0:
            location = 0.0
        else:
            location = (snapshot.close - snapshot.ma20) / (2.0 * snapshot.std20)
        target = 0.50 - 0.20 * min(1.0, max(-1.0, location))
    elif config.initial_model == "price_percentile_252":
        if snapshot.price_percentile_252 is None:
            raise ValueError("price_percentile_252 is required for this initial model")
        target = 0.70 - 0.10 * min(4, int(snapshot.price_percentile_252 * 5))
    else:
        if config.fixed_initial_pct is None:
            raise ValueError("fixed_initial_pct is required for the fixed initial model")
        target = config.fixed_initial_pct
    return min(1.0, max(0.0, target))


def _intent(side: Side, reason: OrderReason, snapshot: IndicatorSnapshot) -> OrderIntent:
    if snapshot.signal_date is None:
        raise ValueError("grid intent requires a signal_date")
    return OrderIntent(
        signal_date=snapshot.signal_date, side=side, reason=reason,
        signal_atr20=snapshot.atr20,
        signal_thresholds=(("grid_anchor", snapshot.close),),
        target_budget=0.0, risk_per_unit=0.0, quantity_rationale="grid step",
    )


def evaluate_grid_close(state: StrategyState, snapshot: IndicatorSnapshot, config: GridConfig, eligible: bool) -> Decision:
    anchor = state.grid_anchor
    if anchor is None:
        return Decision(state, ())
    lower = snapshot.ma20 - 2.0 * snapshot.std20
    if snapshot.close <= anchor * (1.0 - config.step_pct) and snapshot.close >= lower and eligible:
        return Decision(state, (_intent(Side.BUY, OrderReason.GRID_BUY, snapshot),))
    if snapshot.close >= anchor * (1.0 + config.step_pct) and state.position_shares:
        return Decision(state, (_intent(Side.SELL, OrderReason.GRID_SELL, snapshot),))
    return Decision(state, ())


def apply_grid_fill(state: StrategyState, fill: Fill) -> StrategyState:
    if fill.reason not in {OrderReason.GRID_BUY, OrderReason.GRID_SELL}:
        return state
    if fill.signal_price is None:
        raise ValueError("grid fill requires signal_price")
    return replace(state, grid_anchor=fill.signal_price)
