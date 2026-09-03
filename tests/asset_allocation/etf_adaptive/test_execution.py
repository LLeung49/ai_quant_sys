from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import CostConfig, TrendConfig
from asset_allocation.etf_adaptive.contracts import DualPriceBar
from asset_allocation.etf_adaptive.contracts import CorporateAction, CorporateActionType
from asset_allocation.etf_adaptive.execution import ExecutionSimulator, apply_corporate_actions, rebase_signal_state
from asset_allocation.etf_adaptive.state import OrderIntent, OrderReason, Side, StrategyState, TrendUnit


def _bar(*, raw_open: float = 4.0, adjustment_ratio: float = 0.25) -> DualPriceBar:
    return DualPriceBar(
        stock_code="510300.SH", trade_date=date(2026, 9, 3),
        signal_open=raw_open * adjustment_ratio, signal_high=raw_open * adjustment_ratio,
        signal_low=raw_open * adjustment_ratio, signal_close=raw_open * adjustment_ratio,
        raw_open=raw_open, raw_high=raw_open, raw_low=raw_open, raw_close=raw_open,
        amount=20_000_000.0, suspended=False, adjustment_ratio=adjustment_ratio,
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
