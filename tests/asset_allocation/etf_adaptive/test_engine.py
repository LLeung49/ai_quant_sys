from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility
from asset_allocation.etf_adaptive.engine import AdaptiveBacktestEngine, apply_exit_fill, process_close
from asset_allocation.etf_adaptive.execution import ExecutionSimulator
from asset_allocation.etf_adaptive.contracts import CorporateAction, CorporateActionType, DualPriceBar
from asset_allocation.etf_adaptive.engine import apply_session_actions
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import (
    BacktestRequest,
    Fill,
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
