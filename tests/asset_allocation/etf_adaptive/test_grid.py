from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.config import GridConfig
from asset_allocation.etf_adaptive.grid import (
    apply_grid_fill,
    evaluate_grid_close,
    initial_grid_target_pct,
    next_grid_stop,
)
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import Fill, OrderReason, Regime, Side, StrategyState


def _snapshot(close: float, lower: float) -> IndicatorSnapshot:
    return IndicatorSnapshot(
        close=close,
        prior_high_20=1.1,
        prior_low_10=0.8,
        ma20=1.0,
        std20=(1.0 - lower) / 2,
        atr20=0.1,
        signal_date=date(2026, 9, 2),
    )


def _state(anchor: float, shares: int = 1_000) -> StrategyState:
    return StrategyState(regime=Regime.GRID, grid_anchor=anchor, position_shares=shares, cash=Decimal("10000"))


def test_grid_anchor_moves_only_after_fill_and_gap_creates_one_order() -> None:
    decision = evaluate_grid_close(_state(1.0), _snapshot(0.94, 0.90), GridConfig(), eligible=True)

    assert len(decision.orders) == 1
    assert decision.orders[0].signal_date == date(2026, 9, 2)
    assert decision.state.grid_anchor == 1.0
    filled = apply_grid_fill(decision.state, Fill(date(2026, 9, 3), Side.BUY, 100, 0.94, Decimal("5"), OrderReason.GRID_BUY, signal_price=0.94))
    assert filled.grid_anchor == 0.94


def test_grid_does_not_buy_below_lower_band_but_can_sell() -> None:
    assert evaluate_grid_close(_state(1.0), _snapshot(0.89, 0.90), GridConfig(), True).orders == ()
    assert evaluate_grid_close(_state(0.80), _snapshot(0.89, 0.90), GridConfig(), True).orders[0].side is Side.SELL


def test_grid_initial_target_is_clamped_and_stop_never_moves_down() -> None:
    snapshot = _snapshot(1.3, 0.9)
    config = GridConfig(initial_model="bollinger_position")

    assert initial_grid_target_pct(snapshot, config) == 0.3
    assert next_grid_stop(None, highest_close=1.0, atr20=0.1) == 0.7
    assert next_grid_stop(0.8, highest_close=1.0, atr20=0.1) == 0.8
