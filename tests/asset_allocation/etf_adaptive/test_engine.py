from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility
from asset_allocation.etf_adaptive.engine import AdaptiveBacktestEngine, process_close
from asset_allocation.etf_adaptive.execution import ExecutionSimulator
from asset_allocation.etf_adaptive.contracts import DualPriceBar
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import BacktestRequest, OrderReason, Regime, StrategyState


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
