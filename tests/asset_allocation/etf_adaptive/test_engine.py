from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility, ExecutionAvailability
from asset_allocation.etf_adaptive.engine import AdaptiveBacktestEngine, apply_exit_fill, process_close
from asset_allocation.etf_adaptive import engine as engine_module
from asset_allocation.etf_adaptive.execution import ExecutionSimulator
from asset_allocation.etf_adaptive.contracts import CorporateAction, CorporateActionType, DualPriceBar
from asset_allocation.etf_adaptive.engine import apply_session_actions
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import (
    BacktestRequest,
    BacktestEvent,
    Decision,
    Fill,
    OrderIntent,
    OrderReason,
    Regime,
    Side,
    StrategyState,
    TrendUnit,
)


def test_grid_to_trend_cancels_grid_logic_and_creates_trend_intent() -> None:
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.0, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=26.0, dif=0.02, dea=0.01,
        amount_ratio=1.2, signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)

    decision = process_close(
        StrategyState(regime=Regime.GRID, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.state.regime is Regime.TREND
    assert decision.orders[0].reason is OrderReason.TREND_ENTRY


def test_trend_to_grid_with_inventory_waits_for_trend_exit() -> None:
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.2, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=19.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)

    decision = process_close(
        StrategyState(regime=Regime.TREND, position_shares=1_000, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.orders == ()
    assert decision.state.pending_grid is True
    assert decision.state.regime is Regime.TREND


def test_hard_stop_has_priority_and_starts_grid_cooldown() -> None:
    snapshot = IndicatorSnapshot(
        close=0.89, prior_high_20=1.0, prior_low_10=0.8, ma20=1.0,
        std20=0.05, atr20=0.05, adx=26.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    state = StrategyState(
        regime=Regime.GRID, position_shares=1_000, cash=Decimal("120000"),
        cycle_entry_price=1.0,
    )

    decision = process_close(state, snapshot, eligibility, AdaptiveConfig.default())

    assert decision.orders[0].reason is OrderReason.HARD_STOP
    assert decision.state.cooldown_remaining == 5


def test_grid_cooldown_blocks_new_orders_and_decrements_each_close() -> None:
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.2, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=19.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)

    decision = process_close(
        StrategyState(regime=Regime.GRID, cooldown_remaining=2, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.orders == ()
    assert decision.state.cooldown_remaining == 1


def test_grid_initialization_requires_recovery_and_carries_target_budget() -> None:
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.2, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=19.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)

    decision = process_close(
        StrategyState(regime=Regime.GRID, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.orders[0].reason is OrderReason.GRID_INITIALIZE
    assert decision.orders[0].target_budget == 60_000.0
    assert decision.state.grid_anchor is None


def test_grid_highest_close_raises_stop_but_never_lowers_it() -> None:
    snapshot = IndicatorSnapshot(
        close=1.2, prior_high_20=1.3, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.1, adx=19.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    state = StrategyState(
        regime=Regime.GRID, grid_anchor=1.0, highest_close=1.0,
        grid_stop_price=0.8, position_shares=1_000, cash=Decimal("120000"),
    )

    decision = process_close(state, snapshot, eligibility, AdaptiveConfig.default())

    assert decision.state.highest_close == 1.2
    assert decision.state.grid_stop_price == pytest.approx(0.9)


def test_grid_stop_exit_has_priority_over_grid_orders() -> None:
    snapshot = IndicatorSnapshot(
        close=0.85, prior_high_20=1.1, prior_low_10=0.8, ma20=1.0,
        std20=0.05, atr20=0.1, adx=19.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    state = StrategyState(
        regime=Regime.GRID, grid_anchor=1.0, grid_stop_price=0.9,
        highest_close=1.2, position_shares=1_000, cash=Decimal("120000"),
    )

    decision = process_close(state, snapshot, eligibility, AdaptiveConfig.default())

    assert decision.orders[0].reason is OrderReason.GRID_STOP


def test_session_actions_apply_raw_ledger_then_rebase_signal_state() -> None:
    state = StrategyState(grid_anchor=1.0, position_shares=100, cash=Decimal("1000"))
    action = CorporateAction(
        "510300.SH", date(2026, 9, 3), CorporateActionType.SHARE_SPLIT,
        None, Decimal("1.1"),
    )

    updated = apply_session_actions(state, (action,), old_ratio=0.25, new_ratio=0.20)

    assert updated.position_shares == 110
    assert updated.grid_anchor == pytest.approx(0.8)
    assert updated.applied_action_ids == (action.event_id,)


def test_full_exit_fill_clears_completed_cycle_levels() -> None:
    state = StrategyState(
        regime=Regime.GRID, grid_anchor=1.0, cycle_entry_price=1.0,
        grid_stop_price=0.9, trend_stop_price=0.95, highest_close=1.2,
        units=(TrendUnit(4.0, 1.0, 0.05, 1_000, 1.025),),
        position_shares=0, cash=Decimal("120000"),
    )
    fill = Fill(
        date(2026, 9, 3), Side.SELL, 1_000, 4.0, Decimal("5"),
        OrderReason.GRID_STOP,
    )

    cleared = apply_exit_fill(state, fill)

    assert cleared.grid_anchor is None
    assert cleared.cycle_entry_price is None
    assert cleared.grid_stop_price is None
    assert cleared.trend_stop_price is None
    assert cleared.highest_close is None
    assert cleared.units == ()


def test_daily_engine_marks_nav_with_raw_close() -> None:
    bars = tuple(
        DualPriceBar("510300.SH", date(2026, 1, 1).fromordinal(date(2026, 1, 1).toordinal() + day), 1.0, 1.1, 0.9, 1.0, 4.0, 4.4, 3.6, 4.0, 20_000_000.0, False, 0.25)
        for day in range(253)
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    engine = AdaptiveBacktestEngine(AdaptiveConfig.default(), ExecutionSimulator(AdaptiveConfig.default().cost, AdaptiveConfig.default().trend))

    result = engine.run(BacktestRequest("510300.SH", Decimal("1000")), bars, {bar.trade_date: eligibility for bar in bars})

    assert len(result.nav) == 253
    assert result.nav[-1].market_value == Decimal("0")


def test_daily_engine_records_company_action_before_processing_the_session() -> None:
    bar = DualPriceBar(
        "510300.SH", date(2026, 9, 3),
        1.0, 1.1, 0.9, 1.0,
        4.0, 4.4, 3.6, 4.0,
        20_000_000.0, False, 0.25,
    )
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    action = CorporateAction(
        "510300.SH", bar.trade_date, CorporateActionType.SHARE_SPLIT,
        None, Decimal("1.1"),
    )
    config = AdaptiveConfig.default()
    engine = AdaptiveBacktestEngine(config, ExecutionSimulator(config.cost, config.trend))

    result = engine.run(
        BacktestRequest("510300.SH", Decimal("1000")),
        (bar,),
        {bar.trade_date: eligibility},
        {bar.trade_date: (action, action)},
    )

    assert len(result.events) == 1
    assert result.events[0].kind == "corporate_action"
    assert result.events[0].payload == (("event_id", action.event_id),)


def test_locked_stop_is_retried_but_locked_entry_expires(monkeypatch: pytest.MonkeyPatch) -> None:
    dates = tuple(date(2026, 9, 1 + offset) for offset in range(3))
    bars = tuple(
        DualPriceBar(
            "510300.SH", trade_date, 1.0, 1.1, 0.9, 1.0, 4.0, 4.4, 3.6, 4.0,
            20_000_000.0, False, 0.25, 4.0,
            ExecutionAvailability(offset == 1, offset == 1, "exchange"),
        )
        for offset, trade_date in enumerate(dates)
    )
    stop = OrderIntent(dates[0], Side.SELL, OrderReason.GRID_STOP, 0.05, (), 0.0, 0.0, "stop")
    entry = OrderIntent(dates[0], Side.BUY, OrderReason.TREND_ENTRY, 0.05, (), 120_000.0, 0.005, "entry")
    attempted_entry = OrderIntent(dates[1], Side.BUY, OrderReason.GRID_INITIALIZE, 0.05, (), 60_000.0, 0.0, "suppressed")
    decisions = iter((
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), (stop, entry)),
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), (attempted_entry,)),
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), ()),
    ))
    monkeypatch.setattr(
        "asset_allocation.etf_adaptive.indicators.compute_indicators",
        lambda values: (object(),) * len(values),
    )
    monkeypatch.setattr(engine_module, "process_close", lambda *_: next(decisions))
    config = AdaptiveConfig.default()
    result = AdaptiveBacktestEngine(config, ExecutionSimulator(config.cost, config.trend)).run(
        BacktestRequest("510300.SH", Decimal("120000")), bars,
        {bar.trade_date: ETFEligibility(True, (), "broad", 252, 20_000_000.0) for bar in bars},
    )

    assert [event.payload[-1][1] for event in result.events if event.kind == "rejected_order"] == [
        "sell_locked", "buy_locked",
    ]
    assert [(event.kind, event.payload[0][1]) for event in result.events if event.kind == "fill"] == [
        ("fill", "grid_stop"),
    ]


@pytest.mark.parametrize("suspended, amount", ((True, 20_000_000.0), (False, 0.0)))
def test_protective_stop_retries_after_an_unexecutable_session(
    monkeypatch: pytest.MonkeyPatch, suspended: bool, amount: float,
) -> None:
    dates = tuple(date(2026, 9, 1 + offset) for offset in range(3))
    bars = tuple(
        DualPriceBar(
            "510300.SH", trade_date, 1.0, 1.1, 0.9, 1.0, 4.0, 4.4, 3.6, 4.0,
            amount if offset == 1 else 20_000_000.0, suspended if offset == 1 else False, 0.25,
            4.0, ExecutionAvailability(False, False, "exchange"),
        )
        for offset, trade_date in enumerate(dates)
    )
    stop = OrderIntent(dates[0], Side.SELL, OrderReason.GRID_STOP, 0.05, (), 0.0, 0.0, "stop")
    decisions = iter((
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), (stop,)),
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), ()),
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), ()),
    ))
    monkeypatch.setattr("asset_allocation.etf_adaptive.indicators.compute_indicators", lambda values: (object(),) * len(values))
    monkeypatch.setattr(engine_module, "process_close", lambda *_: next(decisions))
    config = AdaptiveConfig.default()

    result = AdaptiveBacktestEngine(config, ExecutionSimulator(config.cost, config.trend)).run(
        BacktestRequest("510300.SH", Decimal("120000")), bars,
        {bar.trade_date: ETFEligibility(True, (), "broad", 252, 20_000_000.0) for bar in bars},
    )

    assert [(event.kind, event.payload[-1][1]) for event in result.events] == [
        ("rejected_order", "unexecutable next bar"), ("fill", "1000"),
    ]


@pytest.mark.parametrize(
    ("initial_shares", "buy_locked", "sell_locked", "expected_side"),
    ((1_000, True, False, "buy"), (2_000, False, True, "sell")),
)
def test_locked_rebalance_emits_resolved_side_in_rejection_event(
    monkeypatch: pytest.MonkeyPatch, initial_shares: int, buy_locked: bool, sell_locked: bool, expected_side: str,
) -> None:
    dates = (date(2026, 9, 1), date(2026, 9, 2))
    bars = tuple(
        DualPriceBar(
            "510300.SH", trade_date, 1.0, 1.1, 0.9, 1.0, 4.0, 4.4, 3.6, 4.0,
            20_000_000.0, False, 0.25, 4.0,
            ExecutionAvailability(buy_locked if offset else False, sell_locked if offset else False, "exchange"),
        )
        for offset, trade_date in enumerate(dates)
    )
    rebalance = OrderIntent(dates[0], Side.REBALANCE, OrderReason.GRID_TO_TREND_REBALANCE, 0.05, (), 120_000.0, 0.005, "rebalance")
    decisions = iter((
        Decision(StrategyState(cash=Decimal("120000"), position_shares=initial_shares), (rebalance,)),
        Decision(StrategyState(cash=Decimal("120000"), position_shares=initial_shares), ()),
    ))
    monkeypatch.setattr("asset_allocation.etf_adaptive.indicators.compute_indicators", lambda values: (object(),) * len(values))
    monkeypatch.setattr(engine_module, "process_close", lambda *_: next(decisions))
    config = AdaptiveConfig.default()

    result = AdaptiveBacktestEngine(config, ExecutionSimulator(config.cost, config.trend)).run(
        BacktestRequest("510300.SH", Decimal("120000")), bars,
        {bar.trade_date: ETFEligibility(True, (), "broad", 252, 20_000_000.0) for bar in bars},
    )

    rejected = next(event for event in result.events if event.kind == "rejected_order")
    assert rejected.payload == (
        ("side", expected_side), ("signal_date", dates[0].isoformat()),
        ("execution_date", dates[1].isoformat()), ("reason", f"{expected_side}_locked"),
    )


def test_consecutive_locked_sessions_keep_one_protective_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    dates = tuple(date(2026, 9, 1 + offset) for offset in range(4))
    bars = tuple(
        DualPriceBar(
            "510300.SH", trade_date, 1.0, 1.1, 0.9, 1.0, 4.0, 4.4, 3.6, 4.0,
            20_000_000.0, False, 0.25, 4.0,
            ExecutionAvailability(False, offset in {1, 2}, "exchange"),
        )
        for offset, trade_date in enumerate(dates)
    )
    stop = OrderIntent(dates[0], Side.SELL, OrderReason.GRID_STOP, 0.05, (), 0.0, 0.0, "stop")
    decisions = iter(tuple(
        Decision(StrategyState(cash=Decimal("116000"), position_shares=1_000), (stop,))
        for _ in dates
    ))
    monkeypatch.setattr("asset_allocation.etf_adaptive.indicators.compute_indicators", lambda values: (object(),) * len(values))
    monkeypatch.setattr(engine_module, "process_close", lambda *_: next(decisions))
    config = AdaptiveConfig.default()

    result = AdaptiveBacktestEngine(config, ExecutionSimulator(config.cost, config.trend)).run(
        BacktestRequest("510300.SH", Decimal("120000")), bars,
        {bar.trade_date: ETFEligibility(True, (), "broad", 252, 20_000_000.0) for bar in bars},
    )

    assert [event.payload[-1][1] for event in result.events if event.kind == "rejected_order"] == ["sell_locked", "sell_locked"]
    assert [event for event in result.events if event.kind == "fill"] == [
        BacktestEvent(dates[3], "fill", (("reason", "grid_stop"), ("shares", "1000"))),
    ]
