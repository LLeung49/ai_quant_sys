"""Immutable state and intent contracts for the adaptive ETF backtest."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"
    REBALANCE = "rebalance"


class Regime(str, Enum):
    GRID = "grid"
    TREND = "trend"


class OrderReason(str, Enum):
    GRID_INITIALIZE = "grid_initialize"
    GRID_BUY = "grid_buy"
    GRID_SELL = "grid_sell"
    GRID_STOP = "grid_stop"
    GRID_TO_TREND_REBALANCE = "grid_to_trend_rebalance"
    TREND_ENTRY = "trend_entry"
    TREND_ADD = "trend_add"
    TREND_STOP = "trend_stop"
    HARD_STOP = "hard_stop"


@dataclass(frozen=True)
class OrderIntent:
    signal_date: date
    side: Side
    reason: OrderReason
    signal_atr20: float | None
    signal_thresholds: tuple[tuple[str, float], ...]
    target_budget: float
    risk_per_unit: float
    quantity_rationale: str


@dataclass(frozen=True)
class TrendUnit:
    raw_fill_price: float
    signal_fill_price: float
    signal_atr20: float
    shares: int
    next_add_signal_price: float


@dataclass(frozen=True)
class StrategyState:
    regime: Regime | None = None
    pending_grid: bool = False
    grid_anchor: float | None = None
    cycle_entry_price: float | None = None
    grid_stop_price: float | None = None
    trend_stop_price: float | None = None
    highest_close: float | None = None
    units: tuple[TrendUnit, ...] = ()
    cooldown_remaining: int = 0
    applied_action_ids: tuple[str, ...] = ()
    position_shares: int = 0
    cash: Decimal = Decimal("0")


@dataclass(frozen=True)
class Decision:
    state: StrategyState
    orders: tuple[OrderIntent, ...]


@dataclass(frozen=True)
class Fill:
    fill_date: date
    side: Side
    shares: int
    raw_price: float
    commission: Decimal
    reason: OrderReason
    signal_price: float | None = None
    signal_atr20: float | None = None


@dataclass(frozen=True)
class RejectedOrder:
    intent: OrderIntent
    side: Side
    reason: str


@dataclass(frozen=True)
class ExecutionResult:
    fills: tuple[Fill, ...]
    state: StrategyState
    rejected_reasons: tuple[str, ...] = ()
    rejected_orders: tuple[RejectedOrder, ...] = ()
    raw_atr20: float | None = None
    stop_distance: float | None = None
    raw_thresholds: tuple[tuple[str, float], ...] = ()


@dataclass(frozen=True)
class BacktestRequest:
    stock_code: str
    initial_cash: Decimal
    start_date: date | None = None
    end_date: date | None = None


@dataclass(frozen=True)
class BacktestEvent:
    event_date: date
    kind: str
    payload: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class DailyNav:
    nav_date: date
    cash: Decimal
    market_value: Decimal

    @property
    def total(self) -> Decimal:
        return self.cash + self.market_value


@dataclass(frozen=True)
class BacktestResult:
    request: BacktestRequest
    events: tuple[BacktestEvent, ...]
    nav: tuple[DailyNav, ...]
