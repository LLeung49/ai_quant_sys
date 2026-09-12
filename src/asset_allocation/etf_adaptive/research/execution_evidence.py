"""Run existing backtest baselines over frozen out-of-sample windows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from math import isfinite

from ..backtest_provider import AdaptiveBacktestDataProvider
from ..config import AdaptiveConfig, CostConfig
from ..execution import commission, execution_fee
from ..state import BacktestEvent, BacktestRequest, DailyNav, Side
from .baselines import BaselineKind, run_baselines
from .benchmark_contracts import WhitelistEntry
from .metrics import Trade, calculate_performance
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
    events: tuple[BacktestEvent, ...] = ()
    cost_config: CostConfig | None = None


@dataclass(frozen=True)
class ExecutionCostTurnover:
    """Recorded, account-currency execution evidence for one baseline."""

    total_cost: float
    turnover: float

    def __post_init__(self) -> None:
        for name, value in (("total_cost", self.total_cost), ("turnover", self.turnover)):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or value < 0.0:
                raise ValueError(f"{name} must be a finite non-negative number")


@dataclass(frozen=True)
class TargetEvidence:
    """Five cost-net paths per frozen validation window for one exposure."""

    entry: WhitelistEntry
    initial_cash: Decimal
    paths: Mapping[BaselineKind, tuple[WindowExecutionPath, ...]]
    stitched_paths: Mapping[BaselineKind, tuple[StitchedNavPoint, ...]]
    execution_evidence: Mapping[BaselineKind, ExecutionCostTurnover] = field(default_factory=dict)
    baseline_provenance: Mapping[BaselineKind, Mapping[str, object]] = field(default_factory=dict)


@dataclass(frozen=True)
class StitchedNavPoint:
    window_id: str
    nav_date: date
    nav_total: float


def stitch_window_nav(
    paths: Sequence[WindowExecutionPath], *, initial_cash: Decimal
) -> tuple[StitchedNavPoint, ...]:
    """Compound reset-per-window NAVs into one cost-net OOS NAV path."""

    if not isinstance(initial_cash, Decimal) or not initial_cash.is_finite() or initial_cash <= 0:
        raise ValueError("initial_cash must be a positive finite Decimal")
    compounded = 1.0
    stitched: list[StitchedNavPoint] = []
    previous_date: date | None = None
    for path in paths:
        if not isinstance(path, WindowExecutionPath) or not path.nav:
            raise ValueError("paths must contain non-empty WindowExecutionPath values")
        if previous_date is not None and path.nav[0].nav_date <= previous_date:
            raise ValueError("window NAV dates must be strictly increasing")
        for point in path.nav:
            ratio = float(point.total / initial_cash)
            if ratio <= 0:
                raise ValueError("window NAV must remain positive")
            stitched.append(StitchedNavPoint(path.window_id, point.nav_date, compounded * ratio))
        compounded = stitched[-1].nav_total
        previous_date = path.nav[-1].nav_date
    return tuple(stitched)


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


def _recorded_trades(
    events: Sequence[BacktestEvent], cost_config: CostConfig | None,
) -> tuple[Trade, ...]:
    """Translate persisted fill/rejection events without inventing execution data."""

    trades: list[Trade] = []
    for event in events:
        payload = dict(event.payload)
        if event.kind == "fill":
            side = Side(payload.get("side", ""))
            shares = int(payload.get("shares", "0"))
            price = Decimal(payload.get("raw_price", "0"))
            notional = price * shares
            if cost_config is None:
                raise ValueError("recorded fill is missing its cost configuration")
            recorded_fee = Decimal(payload.get("commission", "0"))
            reconstructed_fee = execution_fee(notional, side, cost_config)
            bps = Decimal(str(cost_config.slippage_bps)) / Decimal("10000")
            raw_open = price / (
                Decimal("1") + bps if side is Side.BUY else Decimal("1") - bps
            )
            trades.append(Trade(
                signal_date=event.event_date,
                fill_date=event.event_date,
                side=side.value,
                shares=shares,
                raw_price=float(price),
                commission=max(recorded_fee, reconstructed_fee),
                slippage_cost=abs(price - raw_open) * shares,
                minimum_commission_applied=(
                    commission(notional, cost_config)
                    == Decimal(str(cost_config.minimum_commission))
                ),
                is_unfilled=False,
            ))
        elif event.kind == "rejected_order":
            trades.append(Trade(
                signal_date=event.event_date,
                fill_date=event.event_date,
                side=payload.get("side", ""),
                shares=0,
                raw_price=0.0,
                commission=Decimal("0"),
                slippage_cost=Decimal("0"),
                minimum_commission_applied=False,
                is_unfilled=True,
            ))
    return tuple(trades)


def _execution_cost_turnover(
    paths: Sequence[WindowExecutionPath], *, initial_cash: Decimal,
) -> ExecutionCostTurnover:
    stitched = stitch_window_nav(paths, initial_cash=initial_cash)
    metrics = calculate_performance(
        tuple(point.nav_total * float(initial_cash) for point in stitched),
        tuple(
            trade
            for path in paths
            for trade in _recorded_trades(path.events, path.cost_config)
        ),
    )
    return ExecutionCostTurnover(metrics.total_cost, metrics.turnover)


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
    baseline_provenance: dict[BaselineKind, Mapping[str, object]] = {}
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
            paths[kind].append(WindowExecutionPath(
                window.window_id,
                run.result.nav,
                run.result.events,
                run.config.cost,
            ))
            recorded_provenance = run.provenance
            prior_provenance = baseline_provenance.setdefault(kind, recorded_provenance)
            if prior_provenance != recorded_provenance:
                raise ValueError("baseline provenance must remain stable across validation windows")
    frozen_paths = {kind: tuple(value) for kind, value in paths.items()}
    return TargetEvidence(
        entry=entry,
        initial_cash=config.initial_cash,
        paths=frozen_paths,
        stitched_paths={
            kind: stitch_window_nav(path, initial_cash=config.initial_cash)
            for kind, path in frozen_paths.items()
        },
        execution_evidence={
            kind: _execution_cost_turnover(path, initial_cash=config.initial_cash)
            for kind, path in frozen_paths.items()
            if kind in {BaselineKind.FULL_ADAPTIVE, BaselineKind.BUY_AND_HOLD}
        },
        baseline_provenance=baseline_provenance,
    )


__all__ = [
    "TargetEvidence",
    "TargetWalkForwardConfig",
    "ExecutionCostTurnover",
    "StitchedNavPoint",
    "WindowExecutionPath",
    "run_target_walk_forward",
    "stitch_window_nav",
]
