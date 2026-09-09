from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import CostConfig, TrendConfig
from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.contracts import CorporateAction, CorporateActionType
from asset_allocation.etf_adaptive.execution import (
    ExecutionSimulator,
    aggregate_trend_risk,
    apply_corporate_actions,
    rebase_signal_state,
)
from asset_allocation.etf_adaptive.state import OrderIntent, OrderReason, Side, StrategyState, TrendUnit


def _bar(
    *, raw_open: float = 4.0, adjustment_ratio: float = 0.25,
    buy_locked: bool = False, sell_locked: bool = False,
) -> DualPriceBar:
    return DualPriceBar(
        stock_code="510300.SH", trade_date=date(2026, 9, 3),
        signal_open=raw_open * adjustment_ratio, signal_high=raw_open * adjustment_ratio,
        signal_low=raw_open * adjustment_ratio, signal_close=raw_open * adjustment_ratio,
        raw_open=raw_open, raw_high=raw_open, raw_low=raw_open, raw_close=raw_open,
        amount=20_000_000.0, suspended=False, adjustment_ratio=adjustment_ratio,
        execution_availability=ExecutionAvailability(buy_locked, sell_locked, "exchange"),
    )


def _intent(*, signal_atr20: float | None = 0.05) -> OrderIntent:
    return OrderIntent(
        signal_date=date(2026, 9, 2), side=Side.BUY, reason=OrderReason.TREND_ENTRY,
        signal_atr20=signal_atr20, signal_thresholds=(("entry", 1.0), ("trend_stop", 0.9)),
        target_budget=120_000.0, risk_per_unit=0.005, quantity_rationale="trend ATR risk unit",
    )


def test_execution_converts_signal_atr_before_raw_lot_sizing() -> None:
    simulator = ExecutionSimulator(CostConfig(), TrendConfig())

    result = simulator.execute((_intent(),), _bar(), StrategyState(cash=Decimal("120000")))

    assert result.raw_atr20 == pytest.approx(0.20)
    assert result.stop_distance == pytest.approx(0.40)
    assert result.raw_thresholds == (("entry", 4.0), ("trend_stop", 3.6))
    assert result.fills[0].shares == 1_500
    assert result.fills[0].raw_price == pytest.approx(4.0012)
    assert result.fills[0].commission == Decimal("5.00")


def test_execution_rejects_missing_signal_atr_payload() -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_intent(signal_atr20=None),), _bar(), StrategyState(cash=Decimal("120000")),
    )

    assert result.fills == ()
    assert "missing signal_atr20" in result.rejected_reasons


def test_locked_buy_rejects_before_slippage_and_fee() -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_intent(),), _bar(buy_locked=True), StrategyState(cash=Decimal("120000")),
    )

    assert result.fills == ()
    assert result.state == StrategyState(cash=Decimal("120000"))
    assert result.rejected_reasons == ("buy_locked",)


def test_corporate_actions_are_applied_once_in_raw_accounting_space() -> None:
    state = StrategyState(cash=Decimal("1000"), position_shares=100)
    actions = (
        CorporateAction("510300.SH", date(2026, 9, 3), CorporateActionType.CASH_DIVIDEND, Decimal("0.20"), Decimal("1")),
        CorporateAction("510300.SH", date(2026, 9, 3), CorporateActionType.SHARE_SPLIT, None, Decimal("1.1")),
    )

    applied, event_ids = apply_corporate_actions(state, actions, ())
    repeated, repeated_ids = apply_corporate_actions(applied, actions, event_ids)

    assert applied.cash == Decimal("1020.00")
    assert applied.position_shares == 110
    assert repeated == applied
    assert repeated_ids == event_ids


def test_rebase_signal_state_changes_only_signal_coordinate_levels() -> None:
    state = StrategyState(
        grid_anchor=1.0, cycle_entry_price=1.2, grid_stop_price=0.9,
        trend_stop_price=1.1, highest_close=1.3, cash=Decimal("1000"),
        position_shares=100,
        units=(TrendUnit(4.0, 1.0, 0.05, 100, 1.025),),
    )

    rebased = rebase_signal_state(state, old_ratio=0.25, new_ratio=0.20)

    assert rebased.grid_anchor == pytest.approx(0.8)
    assert rebased.cycle_entry_price == pytest.approx(0.96)
    assert rebased.units[0].raw_fill_price == 4.0
    assert rebased.units[0].signal_atr20 == pytest.approx(0.04)
    assert rebased.cash == Decimal("1000")
    assert rebased.position_shares == 100


def test_rebase_signal_state_preserves_raw_levels_when_cash_offset_changes() -> None:
    state = StrategyState(
        grid_anchor=0.554, cycle_entry_price=0.554, cash=Decimal("1000"),
        units=(TrendUnit(0.994, 0.554, 0.05, 100, 0.579),),
    )

    rebased = rebase_signal_state(
        state, old_ratio=1.0, new_ratio=1.0,
        old_offset=-0.44, new_offset=-0.455,
    )

    assert rebased.grid_anchor == pytest.approx(0.539)
    assert rebased.units[0].signal_fill_price == pytest.approx(0.539)
    assert rebased.units[0].next_add_signal_price == pytest.approx(0.564)


def test_rebase_signal_state_rejects_non_positive_adjustment_ratios() -> None:
    with pytest.raises(ValueError, match="adjustment ratios must be positive"):
        rebase_signal_state(StrategyState(), old_ratio=0.0, new_ratio=0.20)


def test_grid_initialization_lots_are_sized_from_raw_open_and_target_budget() -> None:
    intent = OrderIntent(
        date(2026, 9, 2), Side.BUY, OrderReason.GRID_INITIALIZE, 0.05,
        (("entry", 1.0),), 60_000.0, 0.0, "initial GRID target exposure",
    )

    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (intent,), _bar(), StrategyState(cash=Decimal("120000")),
    )

    assert result.fills[0].shares == 14_900


def test_a_share_sell_deducts_commission_stamp_duty_and_transfer_fee() -> None:
    intent = OrderIntent(
        date(2026, 9, 2), Side.SELL, OrderReason.GRID_SELL, 0.05,
        (("grid_anchor", 1.0),), 1.0, 0.0, "close A-share GRID unit",
    )
    cost = CostConfig(
        commission_rate=0.0003, minimum_commission=5.0, slippage_bps=0.0,
        sell_tax_rate=0.0005, transfer_fee_rate=0.00001,
    )

    result = ExecutionSimulator(cost, TrendConfig()).execute(
        (intent,), _bar(), StrategyState(cash=Decimal("0"), position_shares=100),
    )

    assert result.fills[0].commission == Decimal("5.20")
    assert result.state.cash == Decimal("394.80")


@pytest.mark.parametrize("side", (Side.BUY, Side.SELL))
def test_grid_step_uses_raw_portfolio_equity_for_one_unit_lot(side: Side) -> None:
    intent = OrderIntent(
        date(2026, 9, 2), side,
        OrderReason.GRID_BUY if side is Side.BUY else OrderReason.GRID_SELL,
        0.05, (("grid_anchor", 1.0),), 0.10, 0.0, "one GRID unit",
    )
    state = StrategyState(cash=Decimal("100000"), position_shares=10_000)

    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute((intent,), _bar(), state)

    assert result.fills[0].shares == 3_500


def test_grid_to_trend_rebalance_buys_only_the_missing_first_unit_shares() -> None:
    intent = OrderIntent(
        date(2026, 9, 2), Side.BUY, OrderReason.GRID_TO_TREND_REBALANCE,
        0.05, (("entry", 1.0), ("trend_stop", 0.9)),
        120_000.0, 0.005, "reuse GRID inventory and calibrate first TREND unit",
    )

    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (intent,), _bar(), StrategyState(cash=Decimal("120000"), position_shares=1_000),
    )

    assert result.fills[0].side is Side.BUY
    assert result.fills[0].shares == 500


def test_locked_rebalance_rejects_using_its_resolved_buy_side() -> None:
    intent = OrderIntent(
        date(2026, 9, 2), Side.REBALANCE, OrderReason.GRID_TO_TREND_REBALANCE,
        0.05, (("entry", 1.0), ("trend_stop", 0.9)),
        120_000.0, 0.005, "rebalance",
    )

    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (intent,), _bar(buy_locked=True), StrategyState(cash=Decimal("120000"), position_shares=1_000),
    )

    assert result.fills == ()
    assert result.rejected_reasons == ("buy_locked",)
    assert result.rejected_orders[0].side is Side.BUY
    assert result.rejected_orders[0].reason == "buy_locked"


def _state_with_existing_raw_risk(existing_shares: int = 2_300) -> StrategyState:
    return StrategyState(
        cash=Decimal("120000"),
        position_shares=existing_shares,
        trend_stop_price=1.0,
        units=(TrendUnit(5.0, 1.25, 0.05, existing_shares, 1.275),),
    )


def _trend_intent(reason: OrderReason) -> OrderIntent:
    return OrderIntent(
        signal_date=date(2026, 9, 2),
        side=Side.REBALANCE if reason is OrderReason.GRID_TO_TREND_REBALANCE else Side.BUY,
        reason=reason,
        signal_atr20=0.05,
        signal_thresholds=(("entry", 1.0), ("trend_stop", 1.0)),
        target_budget=120_000.0,
        risk_per_unit=0.005,
        quantity_rationale="trend ATR risk unit",
    )


def test_aggregate_trend_risk_uses_current_raw_coordinate_stop() -> None:
    state = _state_with_existing_raw_risk()

    assert aggregate_trend_risk(state, raw_stop=4.0, adjustment_ratio=0.25) == Decimal("2300.00")


@pytest.mark.parametrize("reason", (OrderReason.TREND_ENTRY, OrderReason.TREND_ADD))
def test_trend_entry_or_add_is_trimmed_to_remaining_stop_risk(reason: OrderReason) -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_trend_intent(reason),), _bar(), _state_with_existing_raw_risk(),
    )

    assert result.fills[0].shares == 700


def test_trend_add_below_one_lot_remaining_risk_is_rejected() -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_trend_intent(OrderReason.TREND_ADD),), _bar(), _state_with_existing_raw_risk(2_600),
    )

    assert "aggregate_risk_budget" in result.rejected_reasons


def test_grid_to_trend_rebalance_reduces_to_aggregate_raw_risk_cap() -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_trend_intent(OrderReason.GRID_TO_TREND_REBALANCE),), _bar(), _state_with_existing_raw_risk(),
    )

    assert result.fills[0].side is Side.SELL
    assert result.fills[0].shares == 1_600


def test_trend_batch_reserves_remaining_risk_after_each_fill() -> None:
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_trend_intent(OrderReason.TREND_ADD), _trend_intent(OrderReason.TREND_ADD)),
        _bar(),
        _state_with_existing_raw_risk(),
    )

    assert tuple(fill.shares for fill in result.fills) == (700,)
    assert result.rejected_reasons == ("aggregate_risk_budget",)


def test_trend_add_caps_gapped_fill_risk_after_adjustment_ratio_change() -> None:
    old_basis = StrategyState(
        cash=Decimal("100000"),
        position_shares=1_200,
        trend_stop_price=0.9,
        units=(
            TrendUnit(5.0, 1.25, 0.05, 1_000, 1.275),
            TrendUnit(6.0, 1.50, 0.05, 200, 1.525),
        ),
    )
    state = rebase_signal_state(old_basis, old_ratio=0.25, new_ratio=0.20)
    bar = _bar(raw_open=5.5, adjustment_ratio=0.20)
    result = ExecutionSimulator(CostConfig(), TrendConfig()).execute(
        (_trend_intent(OrderReason.TREND_ADD),), bar, state,
    )

    fill = result.fills[0]
    raw_stop = 3.6
    post_fill_risk = aggregate_trend_risk(state, raw_stop, bar.adjustment_ratio) + (
        Decimal(str(fill.raw_price - raw_stop)) * fill.shares
    )
    raw_equity = state.cash + Decimal(str(bar.raw_open)) * state.position_shares
    risk_cap = raw_equity * Decimal("0.005") * 4

    assert fill.shares == 100
    assert post_fill_risk <= risk_cap
