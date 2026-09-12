"""Deterministic research baselines that share the backtest engine contract."""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import ETFEligibility, ExecutionAvailability, DualPriceBar
from asset_allocation.etf_adaptive.research.baselines import (
    BaselineKind,
    BaselineRun,
    run_baselines,
)
from asset_allocation.etf_adaptive.state import BacktestRequest


class _StubProvider:
    def __init__(self, bars):
        self._bars = bars

    def load_bars(self, stock_code, start_date, end_date):
        return tuple(bar for bar in self._bars if start_date <= bar.trade_date <= end_date)

    def load_actions(self, stock_code, start_date, end_date):
        return ()

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


def _bar(trade_date, raw_open, raw_close, signal_open=None, signal_close=None):
    signal_open = signal_open if signal_open is not None else raw_open
    signal_close = signal_close if signal_close is not None else raw_close
    return DualPriceBar(
        stock_code="510300.SH",
        trade_date=trade_date,
        signal_open=signal_open,
        signal_high=max(signal_open, signal_close),
        signal_low=min(signal_open, signal_close),
        signal_close=signal_close,
        raw_open=raw_open,
        raw_high=max(raw_open, raw_close),
        raw_low=min(raw_open, raw_close),
        raw_close=raw_close,
        amount=20_000_000.0,
        suspended=False,
        adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "stub"),
    )


def test_run_baselines_returns_every_required_kind() -> None:
    bars = tuple(
        _bar(date(2026, 9, offset + 1), 1.00 + 0.01 * offset, 1.01 + 0.01 * offset)
        for offset in range(20)
    )
    provider = _StubProvider(bars)
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("100000"),
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 20),
    )

    runs = run_baselines(request, provider, AdaptiveConfig.default())

    expected_kinds = {
        BaselineKind.BUY_AND_HOLD,
        BaselineKind.FIXED_HALF_HOLD,
        BaselineKind.GRID_ONLY,
        BaselineKind.TREND_ONLY,
        BaselineKind.FULL_ADAPTIVE,
    }
    assert set(runs.keys()) == expected_kinds
    for run in runs.values():
        assert isinstance(run, BaselineRun)
        assert run.result.nav
        assert run.result.request == request


def test_buy_and_hold_baseline_holds_initial_position_through_terminal_session() -> None:
    bars = tuple(
        _bar(date(2026, 9, offset + 1), 1.0 + 0.05 * offset, 1.02 + 0.05 * offset)
        for offset in range(15)
    )
    provider = _StubProvider(bars)
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("100000"),
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 15),
    )

    runs = run_baselines(request, provider, AdaptiveConfig.default())
    buy_hold = runs[BaselineKind.BUY_AND_HOLD]

    assert buy_hold.notes
    fill_events = [event for event in buy_hold.result.events if event.kind == "fill"]
    assert len(fill_events) == 1
    assert fill_events[0].payload and fill_events[0].payload[0] == ("reason", "grid_initialize")
    assert all(nav.nav_date == bars[count].trade_date for count, nav in enumerate(buy_hold.result.nav))


def test_buy_and_hold_deducts_the_shared_execution_cost_model() -> None:
    bars = tuple(
        _bar(date(2026, 9, offset + 1), 10.0, 10.0)
        for offset in range(3)
    )
    provider = _StubProvider(bars)
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("100000"),
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 3),
    )

    buy_hold = run_baselines(request, provider, AdaptiveConfig.default())[BaselineKind.BUY_AND_HOLD]

    assert buy_hold.result.nav[0].cash > Decimal("0")


def test_buy_and_hold_only_records_nav_from_trade_start_date() -> None:
    bars = tuple(_bar(date(2026, 9, offset + 1), 10.0, 10.0) for offset in range(4))
    request = BacktestRequest(
        stock_code="510300.SH", initial_cash=Decimal("100000"),
        start_date=bars[0].trade_date, end_date=bars[-1].trade_date,
        trade_start_date=bars[2].trade_date,
    )

    buy_hold = run_baselines(request, _StubProvider(bars), AdaptiveConfig.default())[BaselineKind.BUY_AND_HOLD]

    assert [point.nav_date for point in buy_hold.result.nav] == [bars[2].trade_date, bars[3].trade_date]
    assert buy_hold.result.events[0].event_date == bars[3].trade_date


def test_fixed_half_hold_baseline_rebalances_to_fifty_percent_each_session() -> None:
    bars = tuple(
        _bar(date(2026, 9, offset + 1), 1.0 + 0.01 * offset, 1.02 + 0.01 * offset)
        for offset in range(10)
    )
    provider = _StubProvider(bars)
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("100000"),
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 10),
    )

    runs = run_baselines(request, provider, AdaptiveConfig.default())
    half = runs[BaselineKind.FIXED_HALF_HOLD]

    fill_events = [event for event in half.result.events if event.kind == "fill"]
    assert fill_events, "fixed_half_hold must rebalance at least once"
    reasons = {payload[0][1] for payload in (event.payload for event in fill_events)}
    assert reasons.issubset({"grid_initialize", "grid_buy", "grid_sell"})


def test_baseline_configs_are_isolated_per_run() -> None:
    bars = tuple(
        _bar(date(2026, 9, offset + 1), 1.0 + 0.005 * offset, 1.005 + 0.005 * offset)
        for offset in range(8)
    )
    provider = _StubProvider(bars)
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("50000"),
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 8),
    )

    runs = run_baselines(request, provider, AdaptiveConfig.default())
    grid_only = runs[BaselineKind.GRID_ONLY].config
    trend_only = runs[BaselineKind.TREND_ONLY].config
    assert grid_only.grid.step_pct == 0.02
    assert grid_only.trend.add_n == 0.5
    assert trend_only.grid.step_pct == 0.02
    assert trend_only.trend.add_n == 0.5


def test_baseline_runs_record_the_compatibility_spec_hash() -> None:
    bars = tuple(_bar(date(2026, 9, offset + 1), 10.0, 10.0) for offset in range(4))
    request = BacktestRequest(
        stock_code="510300.SH",
        initial_cash=Decimal("100000"),
        start_date=bars[0].trade_date,
        end_date=bars[-1].trade_date,
    )

    runs = run_baselines(request, _StubProvider(bars), AdaptiveConfig.default())

    for kind, run in runs.items():
        if kind in {BaselineKind.GRID_ONLY, BaselineKind.TREND_ONLY, BaselineKind.FULL_ADAPTIVE}:
            assert run.strategy_spec_hash is not None
            assert run.benchmark_spec_hash is None
        else:
            assert run.strategy_spec_hash is None
            assert run.benchmark_spec_hash is not None
