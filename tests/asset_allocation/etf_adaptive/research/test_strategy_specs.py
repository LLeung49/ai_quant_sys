"""Observable contracts for fair ETF strategy and benchmark specifications."""

from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import (
    CorporateAction,
    CorporateActionType,
    DualPriceBar,
    ETFEligibility,
    ExecutionAvailability,
)
from asset_allocation.etf_adaptive.research.strategy_specs import (
    FIXED_HALF_SPEC,
    GRID_ONLY_SPEC,
    run_benchmark_spec,
    run_strategy_spec,
)
from asset_allocation.etf_adaptive.state import BacktestRequest


class _Provider:
    def __init__(self, bars: tuple[DualPriceBar, ...], actions=()) -> None:
        self._bars = bars
        self._actions = tuple(actions)

    def load_bars(self, stock_code, start_date, end_date):
        return tuple(
            bar for bar in self._bars
            if bar.stock_code == stock_code and start_date <= bar.trade_date <= end_date
        )

    def load_actions(self, stock_code, start_date, end_date):
        return tuple(
            action for action in self._actions
            if action.stock_code == stock_code and start_date <= action.effective_date <= end_date
        )

    def load_eligibility(self, stock_code, bars):
        return {
            bar.trade_date: ETFEligibility(
                eligible=True,
                rejection_reasons=(),
                exposure_group="core_broad",
                history_session_count=252,
                average_amount_20d=20_000_000.0,
            )
            for bar in bars
        }


def _bar(day: date, price: float) -> DualPriceBar:
    return DualPriceBar(
        stock_code="510300.SH",
        trade_date=day,
        signal_open=price,
        signal_high=price * 1.01,
        signal_low=price * 0.99,
        signal_close=price,
        raw_open=price,
        raw_high=price * 1.01,
        raw_low=price * 0.99,
        raw_close=price,
        amount=20_000_000.0,
        suspended=False,
        adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "test"),
    )


def _request_and_provider() -> tuple[BacktestRequest, _Provider]:
    start = date(2026, 8, 3)
    bars = tuple(_bar(start + timedelta(days=index), 10.0 + index * 0.02) for index in range(35))
    return (
        BacktestRequest("510300.SH", Decimal("100000"), bars[0].trade_date, bars[-1].trade_date),
        _Provider(bars),
    )


def _event_reason(event) -> str | None:
    return dict(event.payload).get("reason")


def _fill_commission(event) -> Decimal:
    return Decimal(dict(event.payload).get("commission", "0"))


def test_grid_only_spec_uses_grid_policy_not_default_trend_config() -> None:
    request, provider = _request_and_provider()

    result = run_strategy_spec(GRID_ONLY_SPEC, request, provider)

    trend_reasons = {"trend_entry", "trend_add", "trend_stop", "grid_to_trend_rebalance"}
    assert {_event_reason(event) for event in result.events}.isdisjoint(trend_reasons)


def test_fixed_half_benchmark_records_shared_cost_model() -> None:
    request, provider = _request_and_provider()

    result = run_benchmark_spec(FIXED_HALF_SPEC, AdaptiveConfig.default(), request, provider)

    assert sum(_fill_commission(event) for event in result.events) > 0


def test_benchmark_records_each_duplicate_corporate_action_once() -> None:
    request, provider = _request_and_provider()
    action = CorporateAction(
        stock_code=request.stock_code,
        effective_date=request.start_date + timedelta(days=3),
        action_type=CorporateActionType.CASH_DIVIDEND,
        cash_per_share=Decimal("0.10"),
        share_multiplier=Decimal("1"),
    )
    provider = _Provider(provider._bars, (action, action))

    result = run_benchmark_spec(FIXED_HALF_SPEC, AdaptiveConfig.default(), request, provider)

    assert [event.kind for event in result.events].count("corporate_action") == 1
