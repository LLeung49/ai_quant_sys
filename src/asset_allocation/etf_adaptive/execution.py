"""T+1 execution in raw-price coordinates."""

from dataclasses import replace
from decimal import Decimal, ROUND_HALF_UP

from .config import CostConfig, TrendConfig
from .contracts import DualPriceBar
from .contracts import CorporateAction, CorporateActionType
from .market_data import to_raw_distance, to_raw_price, to_signal_price
from .state import ExecutionResult, Fill, OrderIntent, OrderReason, RejectedOrder, Side, StrategyState


def is_protective_exit(reason: OrderReason) -> bool:
    """Whether a rejected order must remain active until it can be sold."""
    return reason in {
        OrderReason.GRID_STOP,
        OrderReason.TREND_STOP,
        OrderReason.HARD_STOP,
    }


def aggregate_trend_risk(
    state: StrategyState, raw_stop: float, adjustment_ratio: float,
    adjustment_offset: float = 0.0,
) -> Decimal:
    """Return open TREND-unit loss to the current stop in raw-price space."""
    raw_stop_decimal = Decimal(str(raw_stop))
    risk = Decimal("0")
    for unit in state.units:
        raw_entry = Decimal(str(to_raw_price(
            unit.signal_fill_price, adjustment_ratio, adjustment_offset
        )))
        risk += max(Decimal("0"), raw_entry - raw_stop_decimal) * unit.shares
    return risk


def commission(notional: Decimal, config: CostConfig) -> Decimal:
    charged = max(notional * Decimal(str(config.commission_rate)), Decimal(str(config.minimum_commission)))
    return charged.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def execution_fee(notional: Decimal, side: Side, config: CostConfig) -> Decimal:
    """Return all exchange costs charged to this fill in account currency."""

    tax = notional * Decimal(str(config.sell_tax_rate)) if side is Side.SELL else Decimal("0")
    transfer = notional * Decimal(str(config.transfer_fee_rate))
    return (
        commission(notional, config)
        + tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        + transfer.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )


def slipped_open(raw_open: float, side: Side, bps: float) -> float:
    return raw_open * (1.0 + bps / 10_000.0 if side is Side.BUY else 1.0 - bps / 10_000.0)


def apply_corporate_actions(
    state: StrategyState, actions: tuple[CorporateAction, ...], applied_action_ids: tuple[str, ...],
) -> tuple[StrategyState, tuple[str, ...]]:
    """Apply modeled actions once, without using adjusted prices as account values."""
    applied = set(applied_action_ids)
    current = state
    for action in actions:
        if action.event_id in applied:
            continue
        if action.action_type is CorporateActionType.CASH_DIVIDEND:
            assert action.cash_per_share is not None
            current = replace(
                current,
                cash=current.cash + Decimal(current.position_shares) * action.cash_per_share,
            )
        elif action.action_type is CorporateActionType.SHARE_SPLIT:
            exact_shares = Decimal(current.position_shares) * action.share_multiplier
            if exact_shares != exact_shares.to_integral_value():
                raise ValueError("fractional corporate-action entitlement is unsupported")
            current = replace(current, position_shares=int(exact_shares))
        else:
            raise ValueError("unsupported corporate action")
        applied.add(action.event_id)
    return current, tuple(sorted(applied))


def rebase_signal_state(
    state: StrategyState, old_ratio: float, new_ratio: float,
    old_offset: float = 0.0, new_offset: float = 0.0,
) -> StrategyState:
    """Keep persistent signal levels continuous when the adjustment basis changes."""
    if old_ratio <= 0 or new_ratio <= 0:
        raise ValueError("adjustment ratios must be positive")
    scale = new_ratio / old_ratio
    def level(value: float | None) -> float | None:
        return None if value is None else (value - old_offset) * scale + new_offset
    return replace(
        state,
        grid_anchor=level(state.grid_anchor),
        cycle_entry_price=level(state.cycle_entry_price),
        grid_stop_price=level(state.grid_stop_price),
        trend_stop_price=level(state.trend_stop_price),
        highest_close=level(state.highest_close),
        units=tuple(
            replace(
                unit,
                signal_fill_price=(unit.signal_fill_price - old_offset) * scale + new_offset,
                signal_atr20=unit.signal_atr20 * scale,
                next_add_signal_price=(unit.next_add_signal_price - old_offset) * scale + new_offset,
            )
            for unit in state.units
        ),
    )


class ExecutionSimulator:
    def __init__(self, cost: CostConfig, trend: TrendConfig) -> None:
        self.cost = cost
        self.trend = trend

    def execute(
        self, intents: tuple[OrderIntent, ...], next_bar: DualPriceBar, state: StrategyState,
    ) -> ExecutionResult:
        fills: list[Fill] = []
        rejected: list[str] = []
        rejected_orders: list[RejectedOrder] = []
        current = state
        raw_atr: float | None = None
        stop_distance: float | None = None
        raw_thresholds: tuple[tuple[str, float], ...] = ()
        reserved_trend_risk = Decimal("0")
        def reject(intent: OrderIntent, side: Side, reason: str) -> None:
            rejected.append(reason)
            rejected_orders.append(RejectedOrder(intent, side, reason))

        for intent in intents:
            side = intent.side
            if next_bar.suspended or next_bar.amount <= 0:
                reject(intent, side, "unexecutable next bar")
                continue
            if intent.reason in {OrderReason.TREND_ENTRY, OrderReason.TREND_ADD, OrderReason.GRID_TO_TREND_REBALANCE}:
                if intent.signal_atr20 is None:
                    reject(intent, side, "missing signal_atr20")
                    continue
                raw_atr = to_raw_distance(intent.signal_atr20, next_bar.adjustment_ratio)
                stop_distance = self.trend.stop_n * raw_atr
                target_shares = int(intent.target_budget * intent.risk_per_unit / stop_distance // 100) * 100
                signal_stop = state.trend_stop_price
                if signal_stop is None:
                    signal_stop = next(
                        (value for name, value in intent.signal_thresholds if name == "trend_stop"),
                        None,
                    )
                if signal_stop is None:
                    raw_stop = next_bar.raw_open - stop_distance
                else:
                    raw_stop = to_raw_price(
                        signal_stop,
                        next_bar.adjustment_ratio,
                        next_bar.adjustment_offset,
                    )
                raw_equity = current.cash + Decimal(str(next_bar.raw_open)) * current.position_shares
                risk_cap = (
                    raw_equity
                    * Decimal(str(intent.risk_per_unit))
                    * self.trend.max_units
                )
                remaining_risk = max(
                    Decimal("0"),
                    risk_cap
                    - aggregate_trend_risk(
                        current,
                        raw_stop,
                        next_bar.adjustment_ratio,
                        next_bar.adjustment_offset,
                    )
                    - reserved_trend_risk,
                )
                candidate_price = Decimal(str(slipped_open(
                    next_bar.raw_open, Side.BUY, self.cost.slippage_bps,
                )))
                risk_per_share = max(
                    Decimal(str(stop_distance)), candidate_price - Decimal(str(raw_stop)),
                )
                risk_limited_shares = int(
                    (remaining_risk / risk_per_share) // 100
                ) * 100
                target_shares = min(target_shares, risk_limited_shares)
                shares = (
                    abs(target_shares - current.position_shares)
                    if intent.reason is OrderReason.GRID_TO_TREND_REBALANCE
                    else target_shares
                )
                if intent.reason is OrderReason.GRID_TO_TREND_REBALANCE:
                    side = Side.BUY if target_shares >= current.position_shares else Side.SELL
            elif intent.reason is OrderReason.GRID_INITIALIZE:
                candidate_price = slipped_open(next_bar.raw_open, intent.side, self.cost.slippage_bps)
                shares = int(intent.target_budget / candidate_price // 100) * 100
            elif intent.reason in {OrderReason.GRID_BUY, OrderReason.GRID_SELL}:
                raw_equity = current.cash + Decimal(str(next_bar.raw_open)) * current.position_shares
                unit_notional = raw_equity * Decimal(str(intent.target_budget))
                shares = int(unit_notional / Decimal(str(next_bar.raw_open)) // 100) * 100
            else:
                shares = current.position_shares
            if side is Side.BUY and next_bar.execution_availability.buy_locked:
                reject(intent, side, "buy_locked")
                continue
            if side is Side.SELL and next_bar.execution_availability.sell_locked:
                reject(intent, side, "sell_locked")
                continue
            raw_thresholds = tuple(
                (
                    name,
                    to_raw_price(
                        value,
                        next_bar.adjustment_ratio,
                        next_bar.adjustment_offset,
                    ),
                )
                for name, value in intent.signal_thresholds
            )
            if shares < 100:
                reject(
                    intent,
                    side,
                    "aggregate_risk_budget"
                    if intent.reason in {
                        OrderReason.TREND_ENTRY,
                        OrderReason.TREND_ADD,
                        OrderReason.GRID_TO_TREND_REBALANCE,
                    }
                    else "insufficient lot size",
                )
                continue
            price = slipped_open(next_bar.raw_open, side, self.cost.slippage_bps)
            notional = Decimal(str(price)) * shares
            fee = execution_fee(notional, side, self.cost)
            if side is Side.BUY:
                while shares >= 100 and notional + fee > current.cash:
                    shares -= 100
                    notional = Decimal(str(price)) * shares
                    fee = execution_fee(notional, side, self.cost)
                if shares < 100:
                    reject(intent, side, "insufficient cash")
                    continue
                current = replace(current, cash=current.cash - notional - fee, position_shares=current.position_shares + shares)
            else:
                if shares > current.position_shares:
                    reject(intent, side, "insufficient shares")
                    continue
                current = replace(current, cash=current.cash + notional - fee, position_shares=current.position_shares - shares)
            if (
                side is Side.BUY
                and intent.reason in {
                    OrderReason.TREND_ENTRY,
                    OrderReason.TREND_ADD,
                    OrderReason.GRID_TO_TREND_REBALANCE,
                }
            ):
                reserved_trend_risk += risk_per_share * shares
            fills.append(Fill(
                next_bar.trade_date, side, shares, price, fee, intent.reason,
                to_signal_price(
                    price, next_bar.adjustment_ratio, next_bar.adjustment_offset
                ),
                intent.signal_atr20,
            ))
        return ExecutionResult(
            tuple(fills), current, tuple(rejected), tuple(rejected_orders), raw_atr, stop_distance, raw_thresholds,
        )
