from dataclasses import replace
from datetime import date, timedelta
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.backtest_provider import AdaptiveBacktestDataProvider
from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ETFEligibility,
    ExecutionAvailability,
)
from asset_allocation.etf_adaptive.scenarios import run_slippage_scenarios
from asset_allocation.etf_adaptive.state import BacktestRequest, BacktestResult


CODE = "510300.SH"
START = date(2026, 1, 1)
INITIAL_CASH = Decimal("120000")


class InMemoryBacktestProvider:
    def __init__(self, bars: tuple[DualPriceBar, ...]) -> None:
        self._bars = bars
        self._eligibility = {
            bar.trade_date: ETFEligibility(
                True, (), "broad", 252, 20_000_000.0,
            )
            for bar in bars
        }

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[DualPriceBar, ...]:
        assert (stock_code, start_date, end_date) == (
            CODE, self._bars[0].trade_date, self._bars[-1].trade_date,
        )
        return self._bars

    def load_actions(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[()]:
        assert (stock_code, start_date, end_date) == (
            CODE, self._bars[0].trade_date, self._bars[-1].trade_date,
        )
        return ()

    def load_eligibility(
        self, stock_code: str, bars: tuple[DualPriceBar, ...],
    ) -> dict[date, ETFEligibility]:
        assert stock_code == CODE
        assert bars is self._bars
        return self._eligibility


def _provider() -> AdaptiveBacktestDataProvider:
    bars = tuple(
        DualPriceBar(
            CODE,
            START + timedelta(days=index),
            4.0 + index * 0.01,
            4.001 + index * 0.01,
            3.999 + index * 0.01,
            4.0 + index * 0.01,
            4.0 + index * 0.01,
            4.001 + index * 0.01,
            3.999 + index * 0.01,
            4.0 + index * 0.01,
            20_000_000.0,
            False,
            1.0,
            4.0 + max(index - 1, 0) * 0.01,
            ExecutionAvailability(False, False, "exchange"),
        )
        for index in range(254)
    )
    return InMemoryBacktestProvider(bars)


def _request() -> BacktestRequest:
    return BacktestRequest(
        CODE, INITIAL_CASH, START, START + timedelta(days=253),
    )


def _first_buy_price(result: BacktestResult) -> Decimal:
    fill = next(event for event in result.events if event.kind == "fill")
    assert fill.payload[0] == ("reason", "trend_entry")
    return Decimal(dict(fill.payload)["raw_price"])


def test_standard_slippage_grid_is_independent_and_auditable() -> None:
    config = AdaptiveConfig.default()

    results = run_slippage_scenarios(_request(), _provider(), config)

    assert tuple(results) == (0, 1, 3, 5, 10)
    assert results[0] is not results[1]
    assert config == AdaptiveConfig.default()
    for bps, result in results.items():
        scenario_config = replace(
            config, cost=replace(config.cost, slippage_bps=float(bps)),
        )
        assert result.events[-1].kind == "slippage_scenario"
        assert result.events[-1].payload == (
            ("slippage_bps", str(bps)),
            ("config_hash", scenario_config.config_hash()),
        )


def test_higher_buy_slippage_never_reduces_fill_price() -> None:
    results = run_slippage_scenarios(_request(), _provider(), AdaptiveConfig.default(), (0, 10))

    assert _first_buy_price(results[10]) >= _first_buy_price(results[0])


@pytest.mark.parametrize("bps_values", ((0, 0), (True,), (-1,), (1.0,), ("1",)))
def test_invalid_slippage_values_are_rejected_before_running_scenarios(
    bps_values: tuple[object, ...],
) -> None:
    with pytest.raises(ValueError, match="slippage"):
        run_slippage_scenarios(_request(), _provider(), AdaptiveConfig.default(), bps_values)
