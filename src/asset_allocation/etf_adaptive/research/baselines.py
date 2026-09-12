"""Backwards-compatible names for versioned ETF strategy and benchmark specs."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Mapping

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..state import BacktestRequest, BacktestResult
from .strategy_specs import (
    BUY_AND_HOLD_SPEC,
    FIXED_HALF_SPEC,
    FULL_ADAPTIVE_SPEC,
    GRID_ONLY_SPEC,
    TREND_ONLY_SPEC,
    BenchmarkSpec,
    StrategySpec,
    benchmark_provenance_hash,
    run_benchmark_spec,
    run_strategy_spec,
)


class BaselineKind(str, Enum):
    BUY_AND_HOLD = "buy_and_hold"
    FIXED_HALF_HOLD = "fixed_half_hold"
    GRID_ONLY = "grid_only"
    TREND_ONLY = "trend_only"
    FULL_ADAPTIVE = "full_adaptive"


@dataclass(frozen=True)
class BaselineRun:
    kind: BaselineKind
    config: AdaptiveConfig
    result: BacktestResult
    notes: tuple[str, ...] = field(default_factory=tuple)
    strategy_spec_hash: str | None = None
    benchmark_spec_hash: str | None = None

    @property
    def provenance(self) -> Mapping[str, object]:
        """Publishable identity and notes for this mutually-exclusive baseline run."""

        return {
            "notes": self.notes,
            "strategy_spec_hash": self.strategy_spec_hash,
            "benchmark_spec_hash": self.benchmark_spec_hash,
        }


def run_baselines(
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    base_config: AdaptiveConfig,
) -> Mapping[BaselineKind, BaselineRun]:
    """Execute all compatibility names through their immutable specifications."""

    return {
        kind: run_baseline(kind, request, provider, base_config)
        for kind in BaselineKind
    }


def run_baseline(
    kind: BaselineKind,
    request: BacktestRequest,
    provider: AdaptiveBacktestDataProvider,
    base_config: AdaptiveConfig,
) -> BaselineRun:
    """Run one legacy baseline name without bypassing research specifications."""

    strategy_spec = _strategy_spec_for(kind, base_config)
    if strategy_spec is not None:
        spec_hash = strategy_spec.spec_hash()
        return BaselineRun(
            kind=kind,
            config=strategy_spec.config,
            result=run_strategy_spec(strategy_spec, request, provider),
            notes=(
                f"strategy_spec={strategy_spec.strategy_id}@{strategy_spec.version}",
                f"strategy_spec_hash={spec_hash}",
            ),
            strategy_spec_hash=spec_hash,
        )

    benchmark_spec = _benchmark_spec_for(kind)
    if benchmark_spec is not None:
        spec_hash = benchmark_provenance_hash(benchmark_spec, base_config)
        return BaselineRun(
            kind=kind,
            config=base_config,
            result=run_benchmark_spec(benchmark_spec, base_config, request, provider),
            notes=(
                f"benchmark_spec={benchmark_spec.benchmark_id}@{benchmark_spec.version}",
                f"benchmark_config_hash={base_config.config_hash()}",
                f"benchmark_target_weight={benchmark_spec.target_weight}",
                f"benchmark_spec_hash={spec_hash}",
            ),
            benchmark_spec_hash=spec_hash,
        )
    raise ValueError(f"unsupported baseline kind: {kind!r}")


def _strategy_spec_for(kind: BaselineKind, base_config: AdaptiveConfig) -> StrategySpec | None:
    if kind is BaselineKind.FULL_ADAPTIVE:
        return replace(FULL_ADAPTIVE_SPEC, config=base_config)
    if kind is BaselineKind.GRID_ONLY:
        return replace(GRID_ONLY_SPEC, config=base_config)
    if kind is BaselineKind.TREND_ONLY:
        return replace(TREND_ONLY_SPEC, config=base_config)
    return None


def _benchmark_spec_for(kind: BaselineKind) -> BenchmarkSpec | None:
    if kind is BaselineKind.BUY_AND_HOLD:
        return BUY_AND_HOLD_SPEC
    if kind is BaselineKind.FIXED_HALF_HOLD:
        return FIXED_HALF_SPEC
    return None
