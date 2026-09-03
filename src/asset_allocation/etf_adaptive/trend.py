"""TREND close decisions expressed entirely in signal-price coordinates."""

from dataclasses import replace

from .config import TrendConfig
from .indicators import IndicatorSnapshot
from .state import Decision, Fill, OrderIntent, OrderReason, Regime, Side, StrategyState, TrendUnit


def trend_entry_allowed(snapshot: IndicatorSnapshot, config: TrendConfig) -> bool:
    """Return whether a warmed signal bar authorizes a new TREND campaign."""
    base = (
        snapshot.adx is not None
        and snapshot.adx > 25.0
        and snapshot.close > snapshot.prior_high_20
    )
    macd_ok = (
        not config.require_macd_bullish
        or (snapshot.dif is not None and snapshot.dea is not None and snapshot.dif > snapshot.dea)
    )
    amount_ok = (
        config.amount_ratio_min is None
        or (snapshot.amount_ratio is not None and snapshot.amount_ratio >= config.amount_ratio_min)
    )
    return base and macd_ok and amount_ok


def _intent(
    *, side: Side, reason: OrderReason, state: StrategyState,
    snapshot: IndicatorSnapshot, config: TrendConfig,
) -> OrderIntent:
    if snapshot.signal_date is None or snapshot.atr20 is None:
        raise ValueError("trend intent requires a signal date and ATR20")
    thresholds = (
        ("entry", snapshot.close),
        ("trend_stop", max(
            state.trend_stop_price if state.trend_stop_price is not None else float("-inf"),
            snapshot.close - config.stop_n * snapshot.atr20,
        )),
        ("prior_low_10", snapshot.prior_low_10),
    )
    return OrderIntent(
        signal_date=snapshot.signal_date,
        side=side,
        reason=reason,
        signal_atr20=snapshot.atr20,
        signal_thresholds=thresholds,
        target_budget=float(state.cash),
        risk_per_unit=config.risk_per_unit,
        quantity_rationale="trend ATR risk unit",
    )


def evaluate_trend_close(
    state: StrategyState, snapshot: IndicatorSnapshot, config: TrendConfig, eligible: bool,
    *, allow_add: bool = True,
) -> Decision:
    """Generate at most one T+1 intent; exits take priority over all entries."""
    if state.regime is not Regime.TREND:
        return Decision(state, ())
    stop_hit = state.trend_stop_price is not None and snapshot.close < state.trend_stop_price
    channel_exit = state.position_shares > 0 and snapshot.close < snapshot.prior_low_10
    macd_dead_cross = (
        snapshot.dif is not None
        and snapshot.dea is not None
        and snapshot.prior_dif is not None
        and snapshot.prior_dea is not None
        and snapshot.dif < snapshot.dea
        and snapshot.prior_dif >= snapshot.prior_dea
    )
    if state.position_shares > 0 and (stop_hit or channel_exit or macd_dead_cross):
        return Decision(state, (_intent(
            side=Side.SELL, reason=OrderReason.TREND_STOP, state=state,
            snapshot=snapshot, config=config,
        ),))
    if state.position_shares == 0 and eligible and trend_entry_allowed(snapshot, config):
        return Decision(state, (_intent(
            side=Side.BUY, reason=OrderReason.TREND_ENTRY, state=state,
            snapshot=snapshot, config=config,
        ),))
    if (
        allow_add
        and eligible
        and state.units
        and len(state.units) < config.max_units
        and snapshot.close >= state.units[-1].next_add_signal_price
    ):
        return Decision(state, (_intent(
            side=Side.BUY, reason=OrderReason.TREND_ADD, state=state,
            snapshot=snapshot, config=config,
        ),))
    return Decision(state, ())


def apply_trend_fill(state: StrategyState, fill: Fill, config: TrendConfig) -> StrategyState:
    """Record a real fill; never advance TREND units on an unfilled intent."""
    if fill.reason not in {OrderReason.TREND_ENTRY, OrderReason.TREND_ADD}:
        return state
    if fill.side is not Side.BUY or fill.signal_price is None or fill.signal_atr20 is None:
        raise ValueError("trend buy fills require signal_price and signal_atr20")
    signal_atr20 = fill.signal_atr20
    unit = TrendUnit(
        raw_fill_price=fill.raw_price,
        signal_fill_price=fill.signal_price,
        signal_atr20=signal_atr20,
        shares=fill.shares,
        next_add_signal_price=fill.signal_price + config.add_n * signal_atr20,
    )
    new_stop = fill.signal_price - config.stop_n * signal_atr20
    return replace(
        state,
        position_shares=state.position_shares + fill.shares,
        units=state.units + (unit,),
        trend_stop_price=max(state.trend_stop_price or new_stop, new_stop),
    )
