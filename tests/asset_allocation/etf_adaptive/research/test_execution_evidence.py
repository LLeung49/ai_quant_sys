"""Engine-backed, aligned OOS evidence for one approved exposure."""

from __future__ import annotations

from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ETFEligibility,
    ExecutionAvailability,
    SubLayer,
)
from asset_allocation.etf_adaptive.research.baselines import BaselineKind
from asset_allocation.etf_adaptive.research.benchmark_contracts import WhitelistEntry
from asset_allocation.etf_adaptive.research.execution_evidence import (
    TargetWalkForwardConfig,
    run_target_walk_forward,
)
from asset_allocation.etf_adaptive.research.walk_forward import WalkForwardWindow

class _Provider:
    def __init__(self, bars):
        self._bars = tuple(bars)

    def load_bars(self, stock_code, start_date, end_date):
        return tuple(
            bar for bar in self._bars
            if bar.stock_code == stock_code and start_date <= bar.trade_date <= end_date
        )

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


def _entry() -> WhitelistEntry:
    return WhitelistEntry(
        exposure_id="csi_dividend_low_vol",
        sub_layer=SubLayer.DEFENSIVE_DIVIDEND_ETF,
        primary_code="510300.SH",
        backup_code="510310.SH",
        effective_from=date(2020, 1, 1),
        effective_to=None,
        source_hash="c" * 64,
        valuation_multiplier=1.0,
    )


def _window() -> WalkForwardWindow:
    return WalkForwardWindow(
        window_id="wf_000",
        train_dates=(date(2024, 1, 2),),
        validation_dates=(date(2024, 1, 3), date(2024, 1, 4), date(2024, 1, 5)),
    )


def _bar(day: date, raw_open: float, raw_close: float) -> DualPriceBar:
    return DualPriceBar(
        stock_code="510300.SH",
        trade_date=day,
        signal_open=raw_open,
        signal_high=max(raw_open, raw_close),
        signal_low=min(raw_open, raw_close),
        signal_close=raw_close,
        raw_open=raw_open,
        raw_high=max(raw_open, raw_close),
        raw_low=min(raw_open, raw_close),
        raw_close=raw_close,
        amount=20_000_000.0,
        suspended=False,
        adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "test"),
    )


def test_target_walk_forward_runs_all_five_aligned_execution_paths() -> None:
    bars = tuple(
        _bar(day, 10.0 + offset, 10.1 + offset)
        for offset, day in enumerate(_window().validation_dates)
    )

    evidence = run_target_walk_forward(
        _entry(),
        _Provider(bars),
        TargetWalkForwardConfig(
            windows=(_window(),),
            initial_cash=Decimal("100000"),
            base_config=AdaptiveConfig.default(),
        ),
    )

    assert set(evidence.paths) == set(BaselineKind)
    for path in evidence.paths.values():
        assert path[0].window_id == "wf_000"
        assert tuple(point.nav_date for point in path[0].nav) == _window().validation_dates


def test_target_walk_forward_rejects_missing_aligned_bars() -> None:
    bars = (_bar(date(2024, 1, 3), 10.0, 10.1), _bar(date(2024, 1, 5), 12.0, 12.1))

    with pytest.raises(ValueError, match="bar coverage"):
        run_target_walk_forward(
            _entry(),
            _Provider(bars),
            TargetWalkForwardConfig(
                windows=(_window(),),
                initial_cash=Decimal("100000"),
                base_config=AdaptiveConfig.default(),
            ),
        )
