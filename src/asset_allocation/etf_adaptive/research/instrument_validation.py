"""Fixed-universe contracts for independent ETF strategy validation."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Protocol

from ..config import AdaptiveConfig
from ..contracts import DataQualityError, DualPriceBar, SubLayer
from ..indicators import IndicatorSnapshot, compute_indicators
from ..state import BacktestRequest
from ..state import BacktestEvent, DailyNav
from .baselines import BaselineKind, run_baseline, run_baselines
from .parameters import ParameterCandidate, grid_candidates, stable_parameter_neighborhood, trend_candidates
from .metrics import max_drawdown
from .walk_forward import build_windows


class ValidationStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    DATA_REJECTED = "data_rejected"


class ValidationScope(str, Enum):
    FORMAL = "formal"
    REFERENCE_ONLY = "reference_only"


@dataclass(frozen=True)
class ValidationTarget:
    exposure_id: str
    stock_code: str
    sub_layer: SubLayer
    scope: ValidationScope = ValidationScope.FORMAL
    minimum_train_sessions: int = 504
    available_from: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.exposure_id, str) or not self.exposure_id.strip():
            raise ValueError("exposure_id must be a non-empty string")
        if not isinstance(self.stock_code, str) or not self.stock_code.strip():
            raise ValueError("stock_code must be a non-empty string")
        if not isinstance(self.sub_layer, SubLayer):
            raise ValueError("sub_layer must be a SubLayer")
        if not isinstance(self.scope, ValidationScope):
            raise ValueError("scope must be a ValidationScope")
        required = 252 if self.scope is ValidationScope.REFERENCE_ONLY else 504
        if self.minimum_train_sessions != required:
            raise ValueError("minimum_train_sessions does not match validation scope")


@dataclass(frozen=True)
class InstrumentValidationResult:
    target: ValidationTarget
    status: ValidationStatus
    as_of_date: date
    rejection_reason: str | None = None
    windows: tuple["ValidationWindowResult", ...] = ()
    strategy_annual_return: float | None = None
    benchmark_annual_return: float | None = None
    strategy_max_drawdown: float | None = None
    benchmark_max_drawdown: float | None = None
    scope: ValidationScope = ValidationScope.FORMAL
    activation_eligible: bool = False


@dataclass(frozen=True)
class ValidationWindowResult:
    window_id: str
    training_end: date
    validation_start: date
    config_hash: str
    strategy_return: float
    benchmark_return: float
    strategy_nav: tuple[float, ...]
    benchmark_nav: tuple[float, ...]
    strategy_events: tuple[BacktestEvent, ...] = ()
    benchmark_events: tuple[BacktestEvent, ...] = ()
    strategy_daily_nav: tuple[DailyNav, ...] = ()
    benchmark_daily_nav: tuple[DailyNav, ...] = ()
    market_bars: tuple[DualPriceBar, ...] = ()
    indicator_snapshots: tuple[IndicatorSnapshot | None, ...] = ()


class _Provider(Protocol):
    def load_bars(self, stock_code: str, start_date: date, end_date: date) -> tuple[object, ...]: ...


class CachedValidationProvider:
    """Per-run read-through cache for immutable market-data requests.

    Training evaluates many candidates against identical segments.  Caching
    those provider reads preserves every strategy replay while removing
    repeated database materialisation.
    """

    def __init__(self, provider: object) -> None:
        self._provider = provider
        self._bars: dict[tuple[str, date | None, date | None], object] = {}
        self._actions: dict[tuple[str, date | None, date | None], object] = {}
        self._eligibility: dict[tuple[str, tuple[date, ...]], object] = {}

    def load_bars(self, stock_code: str, start_date: date | None, end_date: date | None):
        key = (stock_code, start_date, end_date)
        if key not in self._bars:
            self._bars[key] = self._provider.load_bars(stock_code, start_date, end_date)
        return self._bars[key]

    def load_actions(self, stock_code: str, start_date: date | None, end_date: date | None):
        key = (stock_code, start_date, end_date)
        if key not in self._actions:
            self._actions[key] = self._provider.load_actions(stock_code, start_date, end_date)
        return self._actions[key]

    def load_eligibility(self, stock_code: str, bars):
        key = (stock_code, tuple(bar.trade_date for bar in bars))
        if key not in self._eligibility:
            self._eligibility[key] = self._provider.load_eligibility(stock_code, bars)
        return self._eligibility[key]

    def __getattr__(self, name: str):
        return getattr(self._provider, name)


FIXED_VALIDATION_TARGETS = (
    ValidationTarget("sp_china_low_vol_dividend", "515450.SH", SubLayer.DEFENSIVE_DIVIDEND_ETF),
    ValidationTarget("csi_dividend", "515080.SH", SubLayer.DEFENSIVE_DIVIDEND_ETF),
    ValidationTarget("csi_300", "510300.SH", SubLayer.DOMESTIC_CORE),
    ValidationTarget("csi_a500", "563360.SH", SubLayer.DOMESTIC_CORE, ValidationScope.REFERENCE_ONLY, 252, date(2024, 10, 15)),
    ValidationTarget("chinext", "159915.SZ", SubLayer.DOMESTIC_GROWTH),
    ValidationTarget("star_50", "588000.SH", SubLayer.DOMESTIC_GROWTH),
    ValidationTarget("nasdaq_100", "513100.SH", SubLayer.OVERSEAS_MATURE),
    ValidationTarget("sp_500", "513500.SH", SubLayer.OVERSEAS_MATURE),
    ValidationTarget("hang_seng_tech", "513130.SH", SubLayer.HONG_KONG_OFFSHORE),
    ValidationTarget("hang_seng_internet_technology", "513330.SH", SubLayer.HONG_KONG_OFFSHORE),
)


def evaluate_validation_gate(*, annual_excess: float, drawdown_excess: float, non_lagging_windows: int, total_windows: int) -> ValidationStatus:
    if total_windows <= 0:
        raise ValueError("total_windows must be positive")
    return ValidationStatus.PASSED if (annual_excess > 0.0 and drawdown_excess <= 0.02 and non_lagging_windows > total_windows / 2) else ValidationStatus.FAILED


def run_instrument_validation(
    target: ValidationTarget,
    provider: _Provider,
    start_date: date,
    as_of_date: date,
    initial_cash: Decimal,
) -> InstrumentValidationResult:
    """Fail closed before any parameter screening when history is absent."""

    if not isinstance(target, ValidationTarget):
        raise ValueError("target must be a ValidationTarget")
    if not isinstance(start_date, date) or not isinstance(as_of_date, date) or start_date > as_of_date:
        raise ValueError("invalid validation date range")
    if not isinstance(initial_cash, Decimal) or not initial_cash.is_finite() or initial_cash <= 0:
        raise ValueError("initial_cash must be a positive finite Decimal")
    try:
        provider = CachedValidationProvider(provider)
        bars = tuple(provider.load_bars(target.stock_code, start_date, as_of_date))
    except DataQualityError as exc:
        return InstrumentValidationResult(target, ValidationStatus.DATA_REJECTED, as_of_date, str(exc))
    if not bars:
        return InstrumentValidationResult(target, ValidationStatus.DATA_REJECTED, as_of_date, "no market bars in requested range")
    try:
        windows = build_windows(tuple(bar.trade_date for bar in bars), train_sessions=target.minimum_train_sessions)
    except ValueError:
        return InstrumentValidationResult(target, ValidationStatus.DATA_REJECTED, as_of_date, "insufficient history for walk-forward validation")
    results: list[ValidationWindowResult] = []
    bars_by_date = {bar.trade_date: bar for bar in bars}
    snapshots_by_date = {
        bar.trade_date: snapshot
        for bar, snapshot in zip(bars, compute_indicators(bars))
    }
    try:
        for window in windows:
            if target.scope is ValidationScope.REFERENCE_ONLY:
                config = AdaptiveConfig.default()
            else:
                segment_size = len(window.train_dates) // 4
                grid = _select_training_candidate(target.stock_code, provider, window.train_dates, initial_cash, grid_candidates(), ("step_pct", "unit_pct", "fixed_initial_pct"), segment_size)
                trend = _select_training_candidate(target.stock_code, provider, window.train_dates, initial_cash, trend_candidates(), ("risk_per_unit", "add_n", "max_units", "amount_ratio_min"), segment_size)
                if grid is None or trend is None:
                    return InstrumentValidationResult(target, ValidationStatus.FAILED, as_of_date, "no_stable_training_parameters", tuple(results))
                config = AdaptiveConfig(grid=grid.config.grid, trend=trend.config.trend, cost=AdaptiveConfig.default().cost)
            # Indicators see the training history, but the Task 1 engine
            # starts the accounting state at the validation boundary.
            runs = run_baselines(BacktestRequest(target.stock_code, initial_cash, window.train_dates[0], window.validation_end, window.validation_dates[0]), provider, config)
            strategy_nav = _validation_nav(runs[BaselineKind.FULL_ADAPTIVE].result.nav, window.validation_dates)
            benchmark_nav = _validation_nav(runs[BaselineKind.BUY_AND_HOLD].result.nav, window.validation_dates)
            strategy = strategy_nav[-1] / strategy_nav[0] - 1
            benchmark = benchmark_nav[-1] / benchmark_nav[0] - 1
            strategy_result = runs[BaselineKind.FULL_ADAPTIVE].result
            benchmark_result = runs[BaselineKind.BUY_AND_HOLD].result
            results.append(ValidationWindowResult(
                window.window_id, window.train_end, window.validation_dates[0], config.config_hash(),
                strategy, benchmark, strategy_nav, benchmark_nav,
                strategy_result.events, benchmark_result.events, strategy_result.nav, benchmark_result.nav,
                tuple(bars_by_date[day] for day in window.validation_dates),
                tuple(snapshots_by_date[day] for day in window.validation_dates),
            ))
    except (ValueError, DataQualityError) as exc:
        return InstrumentValidationResult(target, ValidationStatus.DATA_REJECTED, as_of_date, str(exc), tuple(results))
    strategy_path = _stitch_paths(tuple(row.strategy_nav for row in results))
    benchmark_path = _stitch_paths(tuple(row.benchmark_nav for row in results))
    strategy_annual = _annual_return(strategy_path)
    benchmark_annual = _annual_return(benchmark_path)
    strategy_drawdown = abs(max_drawdown(strategy_path))
    benchmark_drawdown = abs(max_drawdown(benchmark_path))
    status = evaluate_validation_gate(
        annual_excess=strategy_annual - benchmark_annual,
        drawdown_excess=strategy_drawdown - benchmark_drawdown,
        non_lagging_windows=sum(row.strategy_return >= row.benchmark_return for row in results),
        total_windows=len(results),
    )
    return InstrumentValidationResult(
        target, status, as_of_date, None, tuple(results), strategy_annual,
        benchmark_annual, strategy_drawdown, benchmark_drawdown, target.scope,
        target.scope is ValidationScope.FORMAL and status is ValidationStatus.PASSED,
    )


@dataclass(frozen=True)
class _TrainingPoint:
    candidate: ParameterCandidate
    positive_windows: tuple[bool, ...]
    oos_returns: tuple[float, ...]
    last_training_date: date

    @property
    def config_hash(self) -> str:
        return self.candidate.config_hash

    @property
    def positive_window_share(self) -> float:
        return sum(self.positive_windows) / len(self.positive_windows)


def _select_training_candidate(stock_code, provider, dates, initial_cash, candidates, axes, segment_size):
    segments = tuple(dates[index:index + segment_size] for index in range(0, len(dates), segment_size))
    points = {}
    candidate_kind = BaselineKind.GRID_ONLY if candidates[0].family == "grid_only" else BaselineKind.TREND_ONLY
    for candidate in candidates:
        excess = []
        for segment in segments:
            request = BacktestRequest(stock_code, initial_cash, segment[0], segment[-1])
            strategy = run_baseline(candidate_kind, request, provider, candidate.config)
            benchmark = run_baseline(BaselineKind.BUY_AND_HOLD, request, provider, candidate.config)
            excess.append(_nav_return(strategy.result.nav) - _nav_return(benchmark.result.nav))
        points[candidate.config_hash] = _TrainingPoint(candidate, tuple(value >= 0 for value in excess), tuple(excess), dates[-1])
    selected = stable_parameter_neighborhood(points, axes=axes, min_positive_window_share=.75)
    return selected[0] if selected else None


def _nav_return(nav) -> float:
    if not nav or nav[0].total <= 0:
        raise ValueError("backtest NAV is empty or non-positive")
    return float(nav[-1].total / nav[0].total - 1)


def _validation_nav(nav, validation_dates) -> tuple[float, ...]:
    """Normalize a warmed full path at validation start, excluding train P&L."""
    by_date = {point.nav_date: float(point.total) for point in nav}
    first = by_date[validation_dates[0]]
    if first <= 0:
        raise ValueError("validation NAV is non-positive")
    return tuple(by_date[day] / first for day in validation_dates)


def _stitch_paths(paths) -> tuple[float, ...]:
    compounded = 1.0
    stitched = []
    for path in paths:
        if not path:
            raise ValueError("window NAV is empty")
        stitched.extend(compounded * value for value in path)
        compounded = stitched[-1]
    return tuple(stitched)


def _annual_return(nav) -> float:
    if len(nav) < 2:
        raise ValueError("stitched NAV requires two sessions")
    return (nav[-1] / nav[0]) ** (252 / (len(nav) - 1)) - 1
