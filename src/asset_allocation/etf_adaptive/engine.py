"""Daily coordinator for the adaptive ETF state machine."""

from dataclasses import replace
from datetime import date
from decimal import Decimal
from typing import Mapping

from .backtest_provider import AdaptiveBacktestDataProvider
from .config import AdaptiveConfig
from .contracts import CorporateAction, DualPriceBar, ETFEligibility
from .indicators import IndicatorSnapshot
from .state import Decision, StrategyState
from .state import (
    BacktestEvent,
    BacktestRequest,
    BacktestResult,
    DailyNav,
    DailyStrategyObservation,
    Fill,
    OrderIntent,
)
from .execution import ExecutionSimulator
from .execution import apply_corporate_actions, is_protective_exit, rebase_signal_state
from .strategy_policy import FULL_ADAPTIVE_POLICY, StrategyPolicy, apply_exit_fill


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


def process_close(
    state: StrategyState, snapshot: IndicatorSnapshot, eligibility: ETFEligibility,
    config: AdaptiveConfig,
) -> Decision:
    """Run the backwards-compatible full-adaptive close policy."""
    return FULL_ADAPTIVE_POLICY.process_close(state, snapshot, eligibility, config)


class AdaptiveBacktestEngine:
    """Deterministic daily runner; all fills happen before that day's close."""

    def __init__(
        self,
        config: AdaptiveConfig,
        execution: ExecutionSimulator,
        provider: AdaptiveBacktestDataProvider | None = None,
        policy: StrategyPolicy = FULL_ADAPTIVE_POLICY,
    ) -> None:
        self._config = config
        self._execution = execution
        self._provider = provider
        self._policy = policy

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
        observations: list[DailyStrategyObservation] = []
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
            session_fills = ()
            if pending:
                outcome = self._execution.execute(pending, bar, state)
                state = outcome.state
                session_fills = outcome.fills
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
                    state = self._policy.apply_fill(state, fill, self._config)
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
                decision = self._policy.process_close(
                    state, snapshot, eligibility_by_date[bar.trade_date], self._config,
                )
                state = decision.state
                if not pending:
                    pending = decision.orders
            daily_nav = DailyNav(
                bar.trade_date, state.cash, Decimal(str(bar.raw_close)) * state.position_shares,
            )
            nav.append(daily_nav)
            observations.append(_daily_observation(state, pending, session_fills, daily_nav))
            previous_ratio = bar.adjustment_ratio
            previous_offset = bar.adjustment_offset
        return BacktestResult(request, tuple(events), tuple(nav), tuple(observations))


def _daily_observation(
    state: StrategyState,
    pending: tuple[OrderIntent, ...],
    fills: tuple[Fill, ...],
    nav: DailyNav,
) -> DailyStrategyObservation:
    """Capture only state that exists after the completed session's NAV mark."""

    actual_exposure = float(nav.market_value / nav.total) if nav.total > 0 else 0.0
    return DailyStrategyObservation(
        nav_date=nav.nav_date,
        regime=state.regime,
        # The immutable accounting state does not retain an unfilled order's
        # sizing target.  After a completed session the executable target is
        # therefore the NAV-marked exposure actually held in that state.
        target_exposure=actual_exposure,
        actual_exposure=actual_exposure,
        cooldown_remaining=state.cooldown_remaining,
        pending_order_count=len(pending),
        state_reason=_state_reason(state, pending, fills),
    )


def _state_reason(
    state: StrategyState, pending: tuple[OrderIntent, ...], fills: tuple[Fill, ...],
) -> str:
    if fills:
        return fills[-1].reason.value
    if pending:
        return pending[0].reason.value
    return state.regime.value if state.regime is not None else "cash"


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
