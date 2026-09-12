"""Versioned strategy and benchmark specifications for ETF research runs.

Strategy specs select an explicit adaptive capability policy.  Benchmark
specs use the same point-in-time data and :class:`ExecutionSimulator`, but
their targets are deterministic rather than indicator-driven.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date
from decimal import Decimal
from hashlib import sha256
import json

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..engine import _validate_run_inputs, apply_session_actions
from ..execution import ExecutionSimulator
from ..state import (
    BacktestEvent,
    BacktestRequest,
    BacktestResult,
    DailyNav,
    OrderIntent,
    OrderReason,
    Side,
    StrategyState,
)
from ..strategy_policy import (
    FULL_ADAPTIVE_POLICY,
    GRID_ONLY_POLICY,
    TREND_ONLY_POLICY,
    StrategyPolicy,
)


@dataclass(frozen=True)
class StrategySpec:
    """A reproducible selection of adaptive policy and immutable config."""

    strategy_id: str
    version: str
    config: AdaptiveConfig
    policy_id: str

    def spec_hash(self) -> str:
        return _hash_spec({
            "strategy_id": self.strategy_id,
            "version": self.version,
            "config_hash": self.config.config_hash(),
            "policy_id": self.policy_id,
        })


@dataclass(frozen=True)
class BenchmarkSpec:
    """A versioned deterministic benchmark policy."""

    benchmark_id: str
    version: str
    rebalance_sessions: int | None
    target_weight: float = 1.0

    def __post_init__(self) -> None:
        if self.rebalance_sessions is not None and (
            not isinstance(self.rebalance_sessions, int) or self.rebalance_sessions < 1
        ):
            raise ValueError("rebalance_sessions must be a positive integer or None")
        if not isinstance(self.target_weight, (int, float)) or not 0 < self.target_weight <= 1:
            raise ValueError("target_weight must be in (0, 1]")

    def spec_hash(self) -> str:
        return _hash_spec({
            "benchmark_id": self.benchmark_id,
            "version": self.version,
            "rebalance_sessions": self.rebalance_sessions,
            "target_weight": self.target_weight,
        })


FULL_ADAPTIVE_SPEC = StrategySpec(
    "full_adaptive", "1", AdaptiveConfig.default(), FULL_ADAPTIVE_POLICY.policy_id,
)
GRID_ONLY_SPEC = StrategySpec(
    "grid_only", "1", AdaptiveConfig.default(), GRID_ONLY_POLICY.policy_id,
)
TREND_ONLY_SPEC = StrategySpec(
    "trend_only", "1", AdaptiveConfig.default(), TREND_ONLY_POLICY.policy_id,
)
BUY_AND_HOLD_SPEC = BenchmarkSpec("buy_and_hold", "1", None, 1.0)
FIXED_HALF_SPEC = BenchmarkSpec("fixed_half_hold", "1", 1, 0.5)


def benchmark_provenance_hash(spec: BenchmarkSpec, config: AdaptiveConfig) -> str:
    """Identify a benchmark run including its policy target and cost model."""

    return _hash_spec({
        "benchmark_spec_hash": spec.spec_hash(),
        "config_hash": config.config_hash(),
        "target_weight": spec.target_weight,
    })


def run_strategy_spec(
    spec: StrategySpec,
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
) -> BacktestResult:
    """Run an adaptive spec through the shared state-machine engine."""

    from ..engine import AdaptiveBacktestEngine

    policy = _policy_for(spec.policy_id)
    execution = ExecutionSimulator(spec.config.cost, spec.config.trend)
    return AdaptiveBacktestEngine(spec.config, execution, provider, policy).run(request)


def run_benchmark_spec(
    spec: BenchmarkSpec,
    config: AdaptiveConfig,
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
) -> BacktestResult:
    """Run a benchmark with the engine's raw ledger and T+1 execution rules."""

    if request.start_date is None or request.end_date is None:
        raise ValueError("backtest request requires start_date and end_date")
    bars = tuple(provider.load_bars(request.stock_code, request.start_date, request.end_date))
    actions = tuple(provider.load_actions(request.stock_code, request.start_date, request.end_date))
    eligibility_by_date = provider.load_eligibility(request.stock_code, bars)
    _validate_run_inputs(request, bars, eligibility_by_date, actions)

    execution = ExecutionSimulator(config.cost, config.trend)
    actions_by_date: dict[date, list] = {}
    for action in actions:
        actions_by_date.setdefault(action.effective_date, []).append(action)

    state = StrategyState(cash=request.initial_cash)
    pending: tuple[OrderIntent, ...] = ()
    events: list[BacktestEvent] = []
    nav: list[DailyNav] = []
    previous_ratio: float | None = None
    previous_offset: float | None = None
    eligible_sessions = 0
    entered = False

    for bar in bars:
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
            if action.event_id not in previously_applied and action.event_id not in recorded_action_ids:
                events.append(BacktestEvent(bar.trade_date, "corporate_action", (("event_id", action.event_id),)))
                recorded_action_ids.add(action.event_id)

        if pending:
            outcome = execution.execute(pending, bar, state)
            state = outcome.state
            for rejected_order in outcome.rejected_orders:
                events.append(_rejected_event(bar.trade_date, rejected_order))
            for fill in outcome.fills:
                events.append(_fill_event(fill))
                entered = True
            pending = ()

        eligibility = eligibility_by_date[bar.trade_date]
        if eligibility.eligible:
            eligible_sessions += 1
            intent = _benchmark_intent(
                spec, state, bar.raw_close, bar.trade_date, eligible_sessions, entered,
            )
            if intent is not None:
                pending = (intent,)
        nav.append(DailyNav(
            bar.trade_date, state.cash, Decimal(str(bar.raw_close)) * state.position_shares,
        ))
        previous_ratio = bar.adjustment_ratio
        previous_offset = bar.adjustment_offset
    return BacktestResult(request, tuple(events), tuple(nav))


def _policy_for(policy_id: str) -> StrategyPolicy:
    policies = {
        FULL_ADAPTIVE_POLICY.policy_id: FULL_ADAPTIVE_POLICY,
        GRID_ONLY_POLICY.policy_id: GRID_ONLY_POLICY,
        TREND_ONLY_POLICY.policy_id: TREND_ONLY_POLICY,
    }
    try:
        return policies[policy_id]
    except KeyError as exc:
        raise ValueError(f"unsupported strategy policy: {policy_id!r}") from exc


def _benchmark_intent(
    spec: BenchmarkSpec,
    state: StrategyState,
    raw_close: float,
    signal_date: date,
    eligible_sessions: int,
    entered: bool,
) -> OrderIntent | None:
    if spec.benchmark_id == BUY_AND_HOLD_SPEC.benchmark_id:
        if entered:
            return None
        return _intent(signal_date, Side.BUY, OrderReason.GRID_INITIALIZE, float(state.cash), "buy-and-hold entry")
    if spec.benchmark_id != FIXED_HALF_SPEC.benchmark_id:
        raise ValueError(f"unsupported benchmark spec: {spec.benchmark_id!r}")
    if spec.rebalance_sessions is None or eligible_sessions % spec.rebalance_sessions:
        return None

    total = state.cash + Decimal(str(raw_close)) * state.position_shares
    if total <= 0:
        return None
    target_value = total * Decimal(str(spec.target_weight))
    position_value = Decimal(str(raw_close)) * state.position_shares
    difference = target_value - position_value
    one_lot_value = Decimal(str(raw_close)) * 100
    if abs(difference) < one_lot_value:
        return None
    if difference > 0:
        if state.position_shares == 0:
            return _intent(
                signal_date, Side.BUY, OrderReason.GRID_INITIALIZE, float(target_value),
                "fixed-half initial 50% target using prior close",
            )
        return _intent(
            signal_date, Side.BUY, OrderReason.GRID_BUY, float(difference / total),
            "fixed-half rebalance toward 50% using prior close",
        )
    return _intent(
        signal_date, Side.SELL, OrderReason.GRID_SELL, float(-difference / total),
        "fixed-half rebalance toward 50% using prior close",
    )


def _intent(
    signal_date: date, side: Side, reason: OrderReason, target_budget: float, rationale: str,
) -> OrderIntent:
    return OrderIntent(signal_date, side, reason, None, (), target_budget, 0.0, rationale)


def _fill_event(fill) -> BacktestEvent:
    return BacktestEvent(fill.fill_date, "fill", (
        ("reason", fill.reason.value),
        ("side", fill.side.value),
        ("shares", str(fill.shares)),
        ("raw_price", str(fill.raw_price)),
        ("commission", str(fill.commission)),
    ))


def _rejected_event(execution_date: date, rejected_order) -> BacktestEvent:
    return BacktestEvent(execution_date, "rejected_order", (
        ("side", rejected_order.side.value),
        ("signal_date", rejected_order.intent.signal_date.isoformat()),
        ("execution_date", execution_date.isoformat()),
        ("reason", rejected_order.reason),
    ))


def _hash_spec(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(encoded.encode("utf-8")).hexdigest()
