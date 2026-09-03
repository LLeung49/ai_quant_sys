"""T+1 execution in raw-price coordinates."""

from dataclasses import replace
from decimal import Decimal, ROUND_HALF_UP

from .config import CostConfig, TrendConfig
from .contracts import DualPriceBar
from .contracts import CorporateAction, CorporateActionType
from .market_data import to_raw_distance, to_signal_price
from .state import ExecutionResult, Fill, OrderIntent, OrderReason, Side, StrategyState


def commission(notional: Decimal, config: CostConfig) -> Decimal:
    charged = max(notional * Decimal(str(config.commission_rate)), Decimal(str(config.minimum_commission)))
    return charged.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


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


class ExecutionSimulator:
    def __init__(self, cost: CostConfig, trend: TrendConfig) -> None:
        self.cost = cost
        self.trend = trend

    def execute(
        self, intents: tuple[OrderIntent, ...], next_bar: DualPriceBar, state: StrategyState,
    ) -> ExecutionResult:
        fills: list[Fill] = []
        rejected: list[str] = []
        current = state
        raw_atr: float | None = None
        stop_distance: float | None = None
        for intent in intents:
            if next_bar.suspended or next_bar.amount <= 0:
                rejected.append("unexecutable next bar")
                continue
            if intent.reason in {OrderReason.TREND_ENTRY, OrderReason.TREND_ADD}:
                if intent.signal_atr20 is None:
                    rejected.append("missing signal_atr20")
                    continue
                raw_atr = to_raw_distance(intent.signal_atr20, next_bar.adjustment_ratio)
                stop_distance = self.trend.stop_n * raw_atr
                shares = int(intent.target_budget * intent.risk_per_unit / stop_distance // 100) * 100
            else:
                shares = current.position_shares
            if shares < 100:
                rejected.append("insufficient lot size")
                continue
            price = slipped_open(next_bar.raw_open, intent.side, self.cost.slippage_bps)
            notional = Decimal(str(price)) * shares
            fee = commission(notional, self.cost)
            if intent.side is Side.BUY:
                while shares >= 100 and notional + fee > current.cash:
                    shares -= 100
                    notional = Decimal(str(price)) * shares
                    fee = commission(notional, self.cost)
                if shares < 100:
                    rejected.append("insufficient cash")
                    continue
                current = replace(current, cash=current.cash - notional - fee, position_shares=current.position_shares + shares)
            else:
                if shares > current.position_shares:
                    rejected.append("insufficient shares")
                    continue
                current = replace(current, cash=current.cash + notional - fee, position_shares=current.position_shares - shares)
            fills.append(Fill(next_bar.trade_date, intent.side, shares, price, fee, intent.reason, to_signal_price(price, next_bar.adjustment_ratio), intent.signal_atr20))
        return ExecutionResult(tuple(fills), current, tuple(rejected), raw_atr, stop_distance)
