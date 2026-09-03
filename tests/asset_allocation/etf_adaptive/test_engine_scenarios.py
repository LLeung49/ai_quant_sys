from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility
from asset_allocation.etf_adaptive.engine import process_close
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import OrderReason, Regime, StrategyState


def _snapshot(day: date, adx: float) -> IndicatorSnapshot:
    return IndicatorSnapshot(
        close=1.1, prior_high_20=1.2, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=adx, dif=0.02, dea=0.01,
        signal_date=day,
    )


def test_trend_to_grid_initializes_only_after_actual_exit_has_cleared_inventory() -> None:
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    config = AdaptiveConfig.default()
    first = process_close(
        StrategyState(regime=Regime.TREND, position_shares=1_000, cash=Decimal("120000")),
        _snapshot(date(2026, 9, 1), 19.0), eligibility, config,
    )
    after_fill = StrategyState(
        regime=first.state.regime, pending_grid=first.state.pending_grid,
        position_shares=0, cash=Decimal("124000"),
    )
    transition = process_close(after_fill, _snapshot(date(2026, 9, 2), 19.0), eligibility, config)
    initialization = process_close(transition.state, _snapshot(date(2026, 9, 3), 19.0), eligibility, config)

    assert first.state.pending_grid is True
    assert first.orders == ()
    assert transition.orders == ()
    assert initialization.orders[0].reason is OrderReason.GRID_INITIALIZE
    assert initialization.orders[0].signal_date > date(2026, 9, 2)


def test_grid_to_trend_reuses_inventory_via_a_single_risk_rebalance_intent() -> None:
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.0, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=26.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )

    decision = process_close(
        StrategyState(regime=Regime.GRID, grid_anchor=1.0, cycle_entry_price=1.0,
                      grid_stop_price=0.9, position_shares=1_000, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.state.regime is Regime.TREND
    assert decision.orders[0].reason is OrderReason.GRID_TO_TREND_REBALANCE
    assert decision.orders[0].side.value == "rebalance"
    assert decision.orders[0].signal_atr20 == 0.05


def test_grid_to_trend_trims_inventory_when_it_exceeds_first_risk_unit() -> None:
    eligibility = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    snapshot = IndicatorSnapshot(
        close=1.1, prior_high_20=1.0, prior_low_10=0.9, ma20=1.0,
        std20=0.05, atr20=0.05, adx=26.0, dif=0.02, dea=0.01,
        signal_date=date(2026, 9, 2),
    )

    decision = process_close(
        StrategyState(regime=Regime.GRID, grid_anchor=1.0, position_shares=2_000, cash=Decimal("120000")),
        snapshot, eligibility, AdaptiveConfig.default(),
    )

    assert decision.orders[0].reason is OrderReason.GRID_TO_TREND_REBALANCE
    assert decision.orders[0].side.value == "rebalance"
