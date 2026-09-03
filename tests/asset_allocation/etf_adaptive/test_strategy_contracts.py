from dataclasses import FrozenInstanceError, replace
from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig, CostConfig, TrendConfig
from asset_allocation.etf_adaptive.state import (
    BacktestEvent, BacktestRequest, BacktestResult, DailyNav, Decision, Fill,
    OrderIntent, OrderReason, Regime, Side, StrategyState,
)


def test_config_hash_is_stable_and_rejects_unsafe_limits() -> None:
    left = AdaptiveConfig.default()
    right = AdaptiveConfig.default()

    assert left.config_hash() == right.config_hash()
    with pytest.raises(ValueError, match="max_grid_per_day must equal 1"):
        replace(left, grid=replace(left.grid, max_grid_per_day=2))


def test_frozen_order_intent_keeps_signal_coordinate_execution_payload() -> None:
    intent = OrderIntent(
        signal_date=date(2026, 9, 2), side=Side.BUY,
        reason=OrderReason.TREND_ENTRY, signal_atr20=0.05,
        signal_thresholds=(("entry", 1.0), ("stop", 0.9)),
        target_budget=120_000.0, risk_per_unit=0.005,
        quantity_rationale="trend entry",
    )

    assert intent.signal_thresholds == (("entry", 1.0), ("stop", 0.9))
    with pytest.raises(FrozenInstanceError):
        intent.signal_atr20 = 0.1  # type: ignore[misc]


def test_state_and_config_reject_unsafe_contract_values() -> None:
    assert StrategyState(regime=Regime.GRID, cash=Decimal("1000"))
    assert Decision(state=StrategyState(), orders=())
    with pytest.raises(ValueError, match="commission_rate"):
        CostConfig(commission_rate=0.0)
    with pytest.raises(ValueError, match="max_units"):
        TrendConfig(max_units=0)


def test_fill_and_backtest_result_preserve_auditable_daily_records() -> None:
    fill = Fill(
        fill_date=date(2026, 9, 3), side=Side.BUY, shares=100,
        raw_price=4.0, commission=Decimal("5.00"), reason=OrderReason.TREND_ENTRY,
    )
    event = BacktestEvent(event_date=fill.fill_date, kind="fill", payload=(("shares", "100"),))
    nav = DailyNav(nav_date=fill.fill_date, cash=Decimal("595"), market_value=Decimal("400"))
    result = BacktestResult(request=BacktestRequest("510300.SH", Decimal("1000")), events=(event,), nav=(nav,))

    assert fill.shares == 100
    assert result.nav[0].total == Decimal("995")
