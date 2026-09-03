from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import CostConfig, TrendConfig
from asset_allocation.etf_adaptive.contracts import DualPriceBar
from asset_allocation.etf_adaptive.contracts import CorporateAction, CorporateActionType
from asset_allocation.etf_adaptive.execution import ExecutionSimulator, apply_corporate_actions
from asset_allocation.etf_adaptive.state import OrderIntent, OrderReason, Side, StrategyState


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
