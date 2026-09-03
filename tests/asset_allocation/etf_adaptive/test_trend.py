from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import TrendConfig
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import Fill, OrderReason, Regime, Side, StrategyState, TrendUnit
from asset_allocation.etf_adaptive.trend import apply_trend_fill, evaluate_trend_close, trend_entry_allowed


def _snapshot(*, close: float = 1.1, atr20: float = 0.05, prior_low_10: float = 0.9) -> IndicatorSnapshot:
    return IndicatorSnapshot(
        close=close,
        prior_high_20=1.0,
        prior_low_10=prior_low_10,
        ma20=1.0,
        std20=0.05,
        atr20=atr20,
        adx=26.0,
        dif=0.02,
        dea=0.01,
        amount_ratio=1.2,
        signal_date=date(2026, 9, 2),
    )


def test_trend_entry_intent_carries_signal_atr_until_execution() -> None:
    state = StrategyState(regime=Regime.TREND, cash=Decimal("120000"))

    decision = evaluate_trend_close(state, _snapshot(), TrendConfig(), eligible=True)

    assert trend_entry_allowed(_snapshot(), TrendConfig())
    assert len(decision.orders) == 1
    intent = decision.orders[0]
    assert intent.reason is OrderReason.TREND_ENTRY
    assert intent.signal_atr20 == 0.05
    assert dict(intent.signal_thresholds)["entry"] == 1.1
    assert intent.signal_date == date(2026, 9, 2)


def test_trend_exit_wins_over_an_add_signal() -> None:
    state = StrategyState(
        regime=Regime.TREND,
        cash=Decimal("120000"),
        position_shares=1_000,
        trend_stop_price=1.0,
    )

    decision = evaluate_trend_close(state, _snapshot(close=0.95), TrendConfig(), eligible=True)

    assert len(decision.orders) == 1
    assert decision.orders[0].reason is OrderReason.TREND_STOP


def test_trend_exits_on_an_exact_macd_dead_cross() -> None:
    state = StrategyState(regime=Regime.TREND, position_shares=1_000, cash=Decimal("120000"))
    snapshot = IndicatorSnapshot(
        **{
            **_snapshot(close=1.1).__dict__,
            "dif": 0.005,
            "dea": 0.01,
            "prior_dif": 0.02,
            "prior_dea": 0.01,
        }
    )

    decision = evaluate_trend_close(state, snapshot, TrendConfig(), eligible=True)

    assert decision.orders[0].reason is OrderReason.TREND_STOP


def test_trend_adds_at_most_one_unit_and_advances_only_after_fill() -> None:
    state = StrategyState(
        regime=Regime.TREND,
        cash=Decimal("120000"),
        position_shares=1_000,
        units=(TrendUnit(4.0, 1.1, 0.05, 1_000, 1.125),),
    )

    decision = evaluate_trend_close(state, _snapshot(close=1.13), TrendConfig(), eligible=True)

    assert len(decision.orders) == 1
    assert decision.orders[0].reason is OrderReason.TREND_ADD
    assert decision.state.units == state.units
    filled = apply_trend_fill(
        StrategyState(
            regime=Regime.TREND, cash=Decimal("117000"), position_shares=1_500,
            units=decision.state.units,
        ),
        Fill(
            date(2026, 9, 3), decision.orders[0].side, 500, 4.1,
            Decimal("5"), decision.orders[0].reason, signal_price=1.13,
            signal_atr20=0.05,
        ),
        TrendConfig(),
    )
    assert len(filled.units) == 2
    assert filled.position_shares == 1_500
    assert filled.units[-1].next_add_signal_price == pytest.approx(1.155)


def test_grid_to_trend_rebalance_fill_creates_the_first_trend_unit() -> None:
    state = StrategyState(regime=Regime.TREND, position_shares=1_500, cash=Decimal("114000"))
    fill = Fill(
        date(2026, 9, 3), Side.BUY, 500, 4.0, Decimal("5"),
        OrderReason.GRID_TO_TREND_REBALANCE, signal_price=1.0, signal_atr20=0.05,
    )

    transitioned = apply_trend_fill(state, fill, TrendConfig())

    assert len(transitioned.units) == 1
    assert transitioned.units[0].shares == 1_500
    assert transitioned.trend_stop_price == pytest.approx(0.9)


def test_grid_to_trend_trim_fill_also_creates_the_first_trend_unit() -> None:
    state = StrategyState(regime=Regime.TREND, position_shares=1_500, cash=Decimal("126000"))
    fill = Fill(
        date(2026, 9, 3), Side.SELL, 500, 4.0, Decimal("5"),
        OrderReason.GRID_TO_TREND_REBALANCE, signal_price=1.0, signal_atr20=0.05,
    )

    transitioned = apply_trend_fill(state, fill, TrendConfig())

    assert len(transitioned.units) == 1
    assert transitioned.units[0].shares == 1_500
