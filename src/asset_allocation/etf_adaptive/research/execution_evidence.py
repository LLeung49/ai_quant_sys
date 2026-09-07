"""Run existing backtest baselines over frozen out-of-sample windows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig
from ..state import BacktestRequest, DailyNav
from .baselines import BaselineKind, run_baselines
from .benchmark_contracts import WhitelistEntry
from .walk_forward import WalkForwardWindow


@dataclass(frozen=True)
class TargetWalkForwardConfig:
    """Frozen configuration used to execute validation windows only."""

    windows: tuple[WalkForwardWindow, ...]
    initial_cash: Decimal
    base_config: AdaptiveConfig

    def __post_init__(self) -> None:
        if not self.windows:
            raise ValueError("windows must not be empty")
        if not isinstance(self.initial_cash, Decimal) or not self.initial_cash.is_finite() or self.initial_cash <= 0:
            raise ValueError("initial_cash must be a positive finite Decimal")
        if not isinstance(self.base_config, AdaptiveConfig):
            raise ValueError("base_config must be an AdaptiveConfig")


@dataclass(frozen=True)
class WindowExecutionPath:
    window_id: str
    nav: tuple[DailyNav, ...]


@dataclass(frozen=True)
class TargetEvidence:
    """Five cost-net paths per frozen validation window for one exposure."""

    entry: WhitelistEntry
    paths: Mapping[BaselineKind, tuple[WindowExecutionPath, ...]]


def _validate_window_inputs(
    entry: WhitelistEntry,
    provider: AdaptiveBacktestDataProvider,
    window: WalkForwardWindow,
) -> None:
    bars = tuple(
        provider.load_bars(
            entry.primary_code, window.validation_dates[0], window.validation_end
        )
    )
    if tuple(bar.trade_date for bar in bars) != window.validation_dates:
        raise ValueError("bar coverage must exactly match validation sessions")
    actions = tuple(
        provider.load_actions(
            entry.primary_code, window.validation_dates[0], window.validation_end
        )
    )
    sessions = set(window.validation_dates)
    if any(
        action.stock_code != entry.primary_code or action.effective_date not in sessions
        for action in actions
    ):
        raise ValueError("corporate action coverage must exactly match validation sessions")


def run_target_walk_forward(
    entry: WhitelistEntry,
    provider: AdaptiveBacktestDataProvider,
    config: TargetWalkForwardConfig,
) -> TargetEvidence:
    """Execute all aligned baseline paths without selecting from validation data."""

    if not isinstance(entry, WhitelistEntry):
        raise ValueError("entry must be a WhitelistEntry")
    if not isinstance(config, TargetWalkForwardConfig):
        raise ValueError("config must be a TargetWalkForwardConfig")
    paths: dict[BaselineKind, list[WindowExecutionPath]] = {
        kind: [] for kind in BaselineKind
    }
    for window in config.windows:
        _validate_window_inputs(entry, provider, window)
        request = BacktestRequest(
            stock_code=entry.primary_code,
            initial_cash=config.initial_cash,
            start_date=window.validation_dates[0],
            end_date=window.validation_end,
        )
        for kind, run in run_baselines(request, provider, config.base_config).items():
            if tuple(point.nav_date for point in run.result.nav) != window.validation_dates:
                raise ValueError("execution NAV must exactly match validation sessions")
            paths[kind].append(WindowExecutionPath(window.window_id, run.result.nav))
    return TargetEvidence(
        entry=entry,
        paths={kind: tuple(value) for kind, value in paths.items()},
    )


__all__ = [
    "TargetEvidence",
    "TargetWalkForwardConfig",
    "WindowExecutionPath",
    "run_target_walk_forward",
]
