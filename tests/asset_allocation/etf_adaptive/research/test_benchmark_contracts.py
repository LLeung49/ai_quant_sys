"""Contracts for the fixed-weight layered benchmark gate."""

from __future__ import annotations

from datetime import date

import pytest

from asset_allocation.etf_adaptive.contracts import AssetLayer, SubLayer
from asset_allocation.etf_adaptive.research.benchmark_contracts import (
    BenchmarkSeries,
    StrategicPortfolio,
    WhitelistEntry,
    evaluate_portfolio_gate,
)


def test_strategic_portfolio_rejects_weights_that_do_not_sum_to_one() -> None:
    with pytest.raises(ValueError, match="sum to 1"):
        StrategicPortfolio(
            portfolio_id="defensive_strategy",
            asset_layer=AssetLayer.DEFENSIVE,
            weights={
                SubLayer.DEFENSIVE_DIVIDEND_ETF: 0.6429,
                SubLayer.DEFENSIVE_BLUE_CHIP: 0.3500,
            },
        )


def test_whitelist_entry_rejects_identical_primary_and_backup() -> None:
    with pytest.raises(ValueError, match="primary_code and backup_code"):
        WhitelistEntry(
            exposure_id="csi_dividend_low_vol",
            sub_layer=SubLayer.DEFENSIVE_DIVIDEND_ETF,
            primary_code="515450.SH",
            backup_code="515450.SH",
            effective_from=date(2020, 1, 1),
            effective_to=None,
            source_hash="a" * 64,
            valuation_multiplier=1.0,
        )


def test_overseas_whitelist_entry_rejects_non_neutral_valuation_multiplier() -> None:
    with pytest.raises(ValueError, match="valuation_multiplier"):
        WhitelistEntry(
            exposure_id="nasdaq_100",
            sub_layer=SubLayer.OVERSEAS_MATURE,
            primary_code="513100.SH",
            backup_code="159941.SZ",
            effective_from=date(2020, 1, 1),
            effective_to=None,
            source_hash="b" * 64,
            valuation_multiplier=0.85,
        )


def test_portfolio_gate_accepts_drawdown_exactly_two_percentage_points_worse() -> None:
    gate = evaluate_portfolio_gate(
        strategy=BenchmarkSeries(
            series_id="full_adaptive",
            annualized_return=0.10,
            max_drawdown=-0.12,
        ),
        benchmark=BenchmarkSeries(
            series_id="buy_and_hold",
            annualized_return=0.08,
            max_drawdown=-0.10,
        ),
        window_excess_returns=(0.01, 0.00, -0.01),
    )

    assert gate.passed is True
    assert gate.drawdown_passed is True
    assert gate.non_lagging_windows == 2


def test_portfolio_gate_rejects_when_a_majority_of_windows_lag() -> None:
    gate = evaluate_portfolio_gate(
        strategy=BenchmarkSeries(
            series_id="full_adaptive",
            annualized_return=0.10,
            max_drawdown=-0.12,
        ),
        benchmark=BenchmarkSeries(
            series_id="buy_and_hold",
            annualized_return=0.08,
            max_drawdown=-0.10,
        ),
        window_excess_returns=(0.01, -0.01, -0.02),
    )

    assert gate.return_passed is True
    assert gate.drawdown_passed is True
    assert gate.majority_windows_passed is False
    assert gate.passed is False
