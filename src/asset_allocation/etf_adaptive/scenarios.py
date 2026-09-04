"""Reproducible, isolated slippage sensitivity runs."""

from __future__ import annotations

from dataclasses import replace
from types import MappingProxyType
from typing import Mapping

from .backtest_provider import AdaptiveBacktestDataProvider
from .config import AdaptiveConfig
from .engine import AdaptiveBacktestEngine
from .execution import ExecutionSimulator
from .state import BacktestEvent, BacktestRequest, BacktestResult


def _validate_bps_values(bps_values: tuple[int, ...]) -> tuple[int, ...]:
    """Return valid unique integer slippage values without normalizing inputs."""
    values = tuple(bps_values)
    if not values:
        raise ValueError("slippage scenarios require at least one value")
    if any(type(value) is not int or value < 0 for value in values):
        raise ValueError("slippage values must be non-negative integers")
    if len(values) != len(set(values)):
        raise ValueError("slippage values must not contain duplicates")
    return values


def run_slippage_scenarios(
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    config: AdaptiveConfig,
    bps_values: tuple[int, ...] = (0, 1, 3, 5, 10),
) -> Mapping[int, BacktestResult]:
    """Run one provider-backed backtest per immutable slippage configuration."""
    results: dict[int, BacktestResult] = {}
    for bps in _validate_bps_values(bps_values):
        scenario_config = replace(
            config,
            cost=replace(config.cost, slippage_bps=float(bps)),
        )
        execution = ExecutionSimulator(scenario_config.cost, scenario_config.trend)
        result = AdaptiveBacktestEngine(scenario_config, execution, provider).run(request)
        audit_event = BacktestEvent(
            result.nav[-1].nav_date,
            "slippage_scenario",
            (
                ("slippage_bps", str(bps)),
                ("config_hash", scenario_config.config_hash()),
            ),
        )
        results[bps] = replace(result, events=result.events + (audit_event,))
    return MappingProxyType(results)
