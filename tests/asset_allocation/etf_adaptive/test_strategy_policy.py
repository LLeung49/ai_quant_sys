"""Capability boundaries for adaptive ETF strategy policies."""

from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility
from asset_allocation.etf_adaptive.indicators import IndicatorSnapshot
from asset_allocation.etf_adaptive.state import Regime, StrategyState, TrendUnit
from asset_allocation.etf_adaptive.strategy_policy import GRID_ONLY_POLICY, TREND_ONLY_POLICY


def _snapshot(*, adx: float, close: float = 1.1) -> IndicatorSnapshot:
    return IndicatorSnapshot(
        close=close,
        prior_high_20=1.0,
        prior_low_10=0.9,
        ma20=1.0,
        std20=0.05,
        atr20=0.05,
        adx=adx,
        dif=0.02,
        dea=0.01,
        amount_ratio=1.2,
        signal_date=date(2026, 9, 2),
    )


def _eligible() -> ETFEligibility:
    return ETFEligibility(True, (), "broad", 252, 20_000_000.0)


def test_grid_only_policy_never_emits_trend_order_when_adx_requests_trend() -> None:
    grid_state = StrategyState(regime=Regime.GRID, cash=Decimal("120000"))

    decision = GRID_ONLY_POLICY.process_close(
        grid_state, _snapshot(adx=26.0), _eligible(), AdaptiveConfig.default(),
    )

    assert decision.state.regime is Regime.GRID
    assert all(not intent.reason.value.startswith("trend_") for intent in decision.orders)


def test_trend_only_policy_never_emits_grid_order_when_adx_requests_grid() -> None:
    trend_state = StrategyState(
        regime=Regime.TREND,
        cash=Decimal("120000"),
        position_shares=1_000,
        units=(TrendUnit(4.0, 1.0, 0.05, 1_000, 1.05),),
    )

    decision = TREND_ONLY_POLICY.process_close(
        trend_state, _snapshot(adx=19.0), _eligible(), AdaptiveConfig.default(),
    )

    assert decision.state.regime is Regime.TREND
    assert all(not intent.reason.value.startswith("grid_") for intent in decision.orders)
