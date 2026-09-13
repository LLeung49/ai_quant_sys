"""Fixed-universe contracts for independent ETF strategy validation."""

from dataclasses import asdict, dataclass, replace
from datetime import date
from decimal import Decimal
from enum import Enum
from hashlib import sha256
from math import isfinite
from typing import Mapping, Protocol, Sequence

from ..config import AdaptiveConfig, CostConfig
from ..contracts import DataQualityError, DualPriceBar, SubLayer
from ..execution import commission, execution_fee
from ..indicators import IndicatorSnapshot, compute_indicators
from ..state import BacktestRequest
from ..state import BacktestEvent, DailyNav, Side
from .baselines import BaselineKind, run_baseline, run_baselines
from .candidate_scoring import TrainingCandidateScore, select_stable_representative
from .decision import DecisionSummary, ResearchConclusion, ResearchEvidence, evaluate_research_decision
from .metrics import PerformanceMetrics, Trade, calculate_performance, session_returns
from .parameters import (
    ParameterCandidate,
    expand_candidate_axis,
    grid_candidates,
    stable_parameter_candidates,
    trend_candidates,
)
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
    evidence: ResearchEvidence | None = None
    decision: DecisionSummary | None = None
    strategy_metrics: PerformanceMetrics | None = None
    benchmark_metrics: PerformanceMetrics | None = None
    strategy_invested_sessions: int = 0
    strategy_cash_sessions: int = 0
    benchmark_invested_sessions: int = 0
    benchmark_cash_sessions: int = 0
    run_manifest: Mapping[str, object] | None = None


@dataclass(frozen=True)
class TrainingSurfaceSummary:
    """Primitive-only summary of one train-only parameter replay."""

    config_hash: str
    positive_windows: tuple[bool, ...]
    oos_returns: tuple[float, ...]
    positive_window_share: float


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
    strategy_metrics: PerformanceMetrics | None = None
    benchmark_metrics: PerformanceMetrics | None = None
    strategy_invested_sessions: int = 0
    strategy_cash_sessions: int = 0
    benchmark_invested_sessions: int = 0
    benchmark_cash_sessions: int = 0
    grid_training_surface: tuple[TrainingSurfaceSummary, ...] = ()
    trend_training_surface: tuple[TrainingSurfaceSummary, ...] = ()
    cost_config: CostConfig | None = None
    selected_config: Mapping[str, object] | None = None
    candidate_scores: tuple[TrainingCandidateScore, ...] = ()
    selected_scores: Mapping[str, TrainingCandidateScore] | None = None
    screened_axes: Mapping[str, tuple[tuple[str, ...], ...]] | None = None


class _Provider(Protocol):
    def load_bars(self, stock_code: str, start_date: date, end_date: date) -> tuple[object, ...]: ...


def resolve_validation_start(provider: object, stock_code: str, start_date: date, end_date: date) -> date:
    """Advance only across the pre-listing interval when evidence is available."""
    resolver = getattr(provider, "first_aligned_session", None)
    if not callable(resolver):
        return start_date
    first = resolver(stock_code, start_date, end_date)
    if first is None:
        return start_date
    if not isinstance(first, date) or first < start_date or first > end_date:
        raise ValueError("invalid first aligned market session")
    return first


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
        start_date = resolve_validation_start(provider, target.stock_code, start_date, as_of_date)
        provider = CachedValidationProvider(provider)
        bars = tuple(provider.load_bars(target.stock_code, start_date, as_of_date))
    except DataQualityError as exc:
        return _data_rejected_result(target, as_of_date, str(exc))
    if not bars:
        return _data_rejected_result(target, as_of_date, "no market bars in requested range")
    try:
        windows = build_windows(tuple(bar.trade_date for bar in bars), train_sessions=target.minimum_train_sessions)
    except ValueError:
        return _data_rejected_result(target, as_of_date, "insufficient history for walk-forward validation")
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
                grid_surface: tuple[TrainingSurfaceSummary, ...] = ()
                trend_surface: tuple[TrainingSurfaceSummary, ...] = ()
                candidate_scores: tuple[TrainingCandidateScore, ...] = ()
                selected_scores: dict[str, TrainingCandidateScore] = {}
                screened_axes: dict[str, tuple[tuple[str, ...], ...]] = {}
            else:
                segment_size = len(window.train_dates) // 4
                grid_selection = _select_training_candidate(
                    target.stock_code, provider, window.train_dates, initial_cash,
                    grid_candidates(), ("step_pct", "unit_pct", "fixed_initial_pct"),
                    segment_size, ("atr_stop_multiple", "cooldown_sessions"),
                )
                trend_selection = _select_training_candidate(
                    target.stock_code, provider, window.train_dates, initial_cash,
                    trend_candidates(), ("risk_per_unit", "add_n", "max_units", "amount_ratio_min"),
                    segment_size, ("stop_n", "require_macd_bullish"),
                )
                if grid_selection is None or trend_selection is None:
                    return _no_trade_result(
                        target, ValidationStatus.FAILED, as_of_date,
                        "no_stable_training_parameters", tuple(results),
                    )
                config = AdaptiveConfig(
                    grid=grid_selection.candidate.config.grid,
                    trend=trend_selection.candidate.config.trend,
                    cost=AdaptiveConfig.default().cost,
                )
                grid_surface = grid_selection.surface
                trend_surface = trend_selection.surface
                candidate_scores = grid_selection.candidate_scores + trend_selection.candidate_scores
                selected_scores = {
                    "grid_only": grid_selection.selected_score,
                    "trend_only": trend_selection.selected_score,
                }
                screened_axes = {
                    "grid_only": grid_selection.screened_axes,
                    "trend_only": trend_selection.screened_axes,
                }
            # Indicators see the training history, but the Task 1 engine
            # starts the accounting state at the validation boundary.
            runs = run_baselines(BacktestRequest(target.stock_code, initial_cash, window.train_dates[0], window.validation_end, window.validation_dates[0]), provider, config)
            strategy_nav = _validation_nav(runs[BaselineKind.FULL_ADAPTIVE].result.nav, window.validation_dates)
            benchmark_nav = _validation_nav(runs[BaselineKind.BUY_AND_HOLD].result.nav, window.validation_dates)
            strategy = strategy_nav[-1] / strategy_nav[0] - 1
            benchmark = benchmark_nav[-1] / benchmark_nav[0] - 1
            strategy_result = runs[BaselineKind.FULL_ADAPTIVE].result
            benchmark_result = runs[BaselineKind.BUY_AND_HOLD].result
            strategy_metrics = _recorded_performance(strategy_result.nav, strategy_result.events, config.cost)
            benchmark_metrics = _recorded_performance(benchmark_result.nav, benchmark_result.events, config.cost)
            strategy_invested, strategy_cash = _recorded_exposure(strategy_result.nav)
            benchmark_invested, benchmark_cash = _recorded_exposure(benchmark_result.nav)
            results.append(ValidationWindowResult(
                window.window_id, window.train_end, window.validation_dates[0], config.config_hash(),
                strategy, benchmark, strategy_nav, benchmark_nav,
                strategy_result.events, benchmark_result.events, strategy_result.nav, benchmark_result.nav,
                tuple(bars_by_date[day] for day in window.validation_dates),
                tuple(snapshots_by_date[day] for day in window.validation_dates),
                strategy_metrics, benchmark_metrics,
                strategy_invested, strategy_cash, benchmark_invested, benchmark_cash,
                grid_surface, trend_surface,
                config.cost,
                asdict(config),
                candidate_scores=candidate_scores,
                selected_scores=selected_scores,
                screened_axes=screened_axes,
            ))
    except (ValueError, DataQualityError) as exc:
        return _data_rejected_result(target, as_of_date, str(exc), tuple(results))
    strategy_path = _stitch_paths(tuple(row.strategy_nav for row in results))
    benchmark_path = _stitch_paths(tuple(row.benchmark_nav for row in results))
    strategy_annual = _annual_return(strategy_path)
    benchmark_annual = _annual_return(benchmark_path)
    strategy_drawdown = abs(max_drawdown(strategy_path))
    benchmark_drawdown = abs(max_drawdown(benchmark_path))
    initial_oos_nav = float(results[0].strategy_daily_nav[0].total)
    strategy_metrics = calculate_performance(
        tuple(value * initial_oos_nav for value in strategy_path),
        tuple(trade for row in results for trade in _recorded_trades(row.strategy_events, row.cost_config)),
    )
    benchmark_metrics = calculate_performance(
        tuple(value * initial_oos_nav for value in benchmark_path),
        tuple(trade for row in results for trade in _recorded_trades(row.benchmark_events, row.cost_config)),
    )
    evidence = _research_evidence(results, strategy_metrics, benchmark_metrics)
    decision = evaluate_research_decision(evidence)
    status = ValidationStatus.PASSED if decision.conclusion is ResearchConclusion.PASSED else ValidationStatus.FAILED
    return InstrumentValidationResult(
        target, status, as_of_date, None, tuple(results), strategy_annual,
        benchmark_annual, strategy_drawdown, benchmark_drawdown, target.scope,
        _activation_eligible(target.scope, decision),
        evidence, decision, strategy_metrics, benchmark_metrics,
        sum(row.strategy_invested_sessions for row in results),
        sum(row.strategy_cash_sessions for row in results),
        sum(row.benchmark_invested_sessions for row in results),
        sum(row.benchmark_cash_sessions for row in results),
        _run_manifest(target, start_date, as_of_date, provider, bars, results),
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


@dataclass(frozen=True)
class _TrainingSelection:
    candidate: ParameterCandidate
    surface: tuple[TrainingSurfaceSummary, ...]
    candidate_scores: tuple[TrainingCandidateScore, ...]
    selected_score: TrainingCandidateScore
    screened_axes: tuple[tuple[str, ...], ...]


def _select_training_candidate(
    stock_code,
    provider,
    dates,
    initial_cash,
    candidates: Sequence[ParameterCandidate],
    axes: Sequence[str],
    segment_size: int,
    expansion_axes: Sequence[str] = (),
) -> _TrainingSelection | None:
    """Select a baseline, then screen each approved new axis in sequence.

    Every replay below is bounded to a training segment.  In particular, an
    expansion starts from the previously selected candidate and never creates
    a cross-product of the newly approved axes.
    """

    selected, summaries, scores = _screen_training_candidates(
        stock_code, provider, dates, initial_cash, candidates, axes, segment_size,
    )
    if selected is None:
        return None
    all_summaries = list(summaries)
    all_scores = list(scores)
    screened_axes = [tuple(axes)]
    for axis in expansion_axes:
        expanded = expand_candidate_axis(selected, axis=axis)
        selected, summaries, scores = _screen_training_candidates(
            stock_code, provider, dates, initial_cash, expanded, (axis,), segment_size,
        )
        if selected is None:
            return None
        all_summaries.extend(summaries)
        all_scores.extend(scores)
        screened_axes.append((axis,))
    selected_score = next(score for score in scores if score.config_hash == selected.config_hash)
    return _TrainingSelection(
        selected, tuple(all_summaries), tuple(all_scores), selected_score, tuple(screened_axes),
    )


def _screen_training_candidates(stock_code, provider, dates, initial_cash, candidates, axes, segment_size):
    segments = tuple(dates[index:index + segment_size] for index in range(0, len(dates), segment_size))
    points = {}
    raw_scores = []
    candidate_kind = BaselineKind.GRID_ONLY if candidates[0].family == "grid_only" else BaselineKind.TREND_ONLY
    for candidate in candidates:
        excess = []
        strategy_metrics = []
        benchmark_metrics = []
        sortino_pairs = []
        sharpe_pairs = []
        starting_nav = 0.0
        invested_sessions = 0
        total_sessions = 0
        for segment in segments:
            request = BacktestRequest(stock_code, initial_cash, segment[0], segment[-1])
            strategy = run_baseline(candidate_kind, request, provider, candidate.config)
            benchmark = run_baseline(BaselineKind.BUY_AND_HOLD, request, provider, candidate.config)
            excess.append(_nav_return(strategy.result.nav) - _nav_return(benchmark.result.nav))
            strategy_metrics.append(_recorded_performance(strategy.result.nav, strategy.result.events, candidate.config.cost))
            benchmark_metrics.append(_recorded_performance(benchmark.result.nav, benchmark.result.events, candidate.config.cost))
            strategy_sortino, strategy_sharpe = _available_training_ratios(strategy.result.nav, strategy_metrics[-1])
            benchmark_sortino, benchmark_sharpe = _available_training_ratios(benchmark.result.nav, benchmark_metrics[-1])
            sortino_pairs.append((strategy_sortino, benchmark_sortino))
            sharpe_pairs.append((strategy_sharpe, benchmark_sharpe))
            starting_nav += float(strategy.result.nav[0].total)
            invested_sessions += _recorded_exposure(strategy.result.nav)[0]
            total_sessions += len(strategy.result.nav)
        points[candidate.config_hash] = _TrainingPoint(candidate, tuple(value >= 0 for value in excess), tuple(excess), dates[-1])
        paired_metrics = tuple(zip(strategy_metrics, benchmark_metrics))
        costs = tuple(s.total_cost for s in strategy_metrics)
        raw_scores.append(TrainingCandidateScore(
            config_hash=candidate.config_hash,
            config=asdict(candidate.config),
            positive_subperiod_share=points[candidate.config_hash].positive_window_share,
            sortino_excess=_mean_training_difference(sortino_pairs),
            sharpe_excess=_mean_training_difference(sharpe_pairs),
            drawdown_improvement=_mean_training_difference(
                tuple((b.max_drawdown, s.max_drawdown) for s, b in paired_metrics), absolute=True,
            ),
            cvar5_improvement=_mean_training_difference(tuple((s.cvar5, b.cvar5) for s, b in paired_metrics)),
            cost_drag=sum(costs) / starting_nav if all(_finite_training_value(value) for value in costs) else None,
            exposure_ratio=invested_sessions / total_sessions,
            stable=False,
            rejection_reason="outside_stable_plateau",
            family=candidate.family,
            screened_axes=tuple(axes),
        ))
    plateau = stable_parameter_candidates(
        points, candidates=candidates, axes=axes, min_positive_window_share=.75,
    )
    stable_hashes = {candidate.config_hash for candidate in plateau}
    scores = tuple(
        replace(score, stable=True, rejection_reason=None)
        if score.config_hash in stable_hashes and score.rejection_reason == "outside_stable_plateau" else score
        for score in sorted(raw_scores, key=lambda score: score.config_hash)
    )
    selected_score = select_stable_representative(scores)
    selected = next((candidate for candidate in plateau if selected_score is not None
                     and candidate.config_hash == selected_score.config_hash), None)
    summaries = tuple(
        TrainingSurfaceSummary(
            config_hash=point.config_hash,
            positive_windows=point.positive_windows,
            oos_returns=point.oos_returns,
            positive_window_share=point.positive_window_share,
        )
        for point in points.values()
    )
    return selected, summaries, scores


def _finite_training_value(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and isfinite(value)


def _available_training_ratios(
    nav: Sequence[DailyNav], metrics: PerformanceMetrics,
) -> tuple[float | None, float | None]:
    """Keep undefined denominator fallbacks out of candidate scoring only.

    Legacy Sortino uses the population deviation of negative daily returns,
    which requires at least two distinct negative returns. A finite zero
    ratio with a nonzero denominator remains valid evidence.
    """
    returns = session_returns(tuple(float(point.total) for point in nav))
    downside_returns = {value for value in returns if value < 0.0}
    sortino = metrics.sortino if len(downside_returns) > 1 else None
    sharpe = metrics.sharpe if (
        _finite_training_value(metrics.annual_volatility) and metrics.annual_volatility > 0.0
    ) else None
    return sortino, sharpe


def _mean_training_difference(
    pairs: Sequence[tuple[float | None, float | None]], *, absolute: bool = False,
) -> float | None:
    if not pairs or any(not _finite_training_value(value) for pair in pairs for value in pair):
        return None
    return sum(abs(left) - abs(right) if absolute else left - right for left, right in pairs) / len(pairs)


def _recorded_trades(
    events: Sequence[BacktestEvent],
    cost_config: CostConfig | None,
) -> tuple[Trade, ...]:
    trades: list[Trade] = []
    for event in events:
        payload = dict(event.payload)
        if event.kind == "fill":
            side = Side(payload.get("side", ""))
            shares = int(payload.get("shares", "0"))
            price = Decimal(payload.get("raw_price", "0"))
            notional = price * shares
            if cost_config is None:
                recorded_fee = Decimal(payload.get("commission", "0"))
                slippage_cost = Decimal(payload.get("slippage_cost", "0"))
                minimum_applied = payload.get("minimum_commission_applied") == "true"
            else:
                recorded_fee = Decimal(payload.get("commission", "0"))
                reconstructed_fee = execution_fee(notional, side, cost_config)
                bps = Decimal(str(cost_config.slippage_bps)) / Decimal("10000")
                raw_open = price / (Decimal("1") + bps if side is Side.BUY else Decimal("1") - bps)
                slippage_cost = abs(price - raw_open) * shares
                minimum_applied = commission(notional, cost_config) == Decimal(str(cost_config.minimum_commission))
            trades.append(Trade(
                signal_date=event.event_date,
                fill_date=event.event_date,
                side=side.value,
                shares=shares,
                raw_price=float(price),
                commission=max(recorded_fee, reconstructed_fee) if cost_config is not None else recorded_fee,
                slippage_cost=slippage_cost,
                minimum_commission_applied=minimum_applied,
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


def _recorded_performance(
    nav: Sequence[DailyNav], events: Sequence[BacktestEvent], cost_config: CostConfig | None = None,
) -> PerformanceMetrics:
    """Calculate research metrics solely from the persisted backtest result."""
    return calculate_performance(tuple(float(point.total) for point in nav), _recorded_trades(events, cost_config))


def _recorded_exposure(nav: Sequence[DailyNav]) -> tuple[int, int]:
    invested = sum(point.market_value > 0 for point in nav)
    return invested, len(nav) - invested


def _research_evidence(
    results: Sequence[ValidationWindowResult],
    strategy: PerformanceMetrics,
    benchmark: PerformanceMetrics,
) -> ResearchEvidence:
    initial_oos_nav = float(results[0].strategy_daily_nav[0].total)
    total_cost = sum(row.strategy_metrics.total_cost for row in results if row.strategy_metrics is not None)
    invested = sum(row.strategy_invested_sessions for row in results)
    sessions = sum(row.strategy_invested_sessions + row.strategy_cash_sessions for row in results)
    return ResearchEvidence(
        data_valid=True,
        oos_window_count=len(results),
        oos_non_lagging_share=sum(row.strategy_return >= row.benchmark_return for row in results) / len(results),
        stable_parameter_region=all(row.grid_training_surface and row.trend_training_surface for row in results),
        annual_excess=strategy.annual_return - benchmark.annual_return,
        drawdown_improvement=abs(benchmark.max_drawdown) - abs(strategy.max_drawdown),
        sharpe_excess=strategy.sharpe - benchmark.sharpe,
        sortino_excess=strategy.sortino - benchmark.sortino,
        calmar_excess=strategy.calmar - benchmark.calmar,
        cvar5_improvement=strategy.cvar5 - benchmark.cvar5,
        exposure_ratio=invested / sessions if sessions else 0.0,
        turnover=strategy.turnover,
        total_cost=total_cost,
        initial_oos_nav=initial_oos_nav,
        cost_drag=total_cost / initial_oos_nav,
        persistent_failure_windows=sum(
            row.strategy_return < row.benchmark_return
            and row.strategy_metrics is not None
            and row.benchmark_metrics is not None
            and row.strategy_metrics.sharpe <= row.benchmark_metrics.sharpe
            for row in results
        ),
    )


def _run_manifest(
    target: ValidationTarget,
    start_date: date,
    as_of_date: date,
    provider: object,
    bars: Sequence[DualPriceBar],
    windows: Sequence[ValidationWindowResult],
) -> Mapping[str, object]:
    """Record enough immutable evidence to replay and audit a formal run."""
    data_fingerprint = sha256(repr(tuple(bars)).encode("utf-8")).hexdigest()
    return {
        "schema_version": 1,
        "runner": "run_instrument_validation",
        "source_provider": type(getattr(provider, "_provider", provider)).__name__,
        "data_cutoff": as_of_date.isoformat(),
        "requested_start": start_date.isoformat(),
        "data_fingerprint": data_fingerprint,
        "target": {
            "exposure_id": target.exposure_id,
            "stock_code": target.stock_code,
            "sub_layer": target.sub_layer.value,
            "scope": target.scope.value,
        },
        "selected_configs": [
            {"window_id": row.window_id, "config_hash": row.config_hash,
             "config": row.selected_config}
            for row in windows
        ],
        "screened_axes": {
            "grid": ["step_pct", "unit_pct", "fixed_initial_pct", "atr_stop_multiple", "cooldown_sessions"],
            "trend": ["risk_per_unit", "add_n", "max_units", "amount_ratio_min", "stop_n", "require_macd_bullish"],
        },
    }


def _data_rejected_result(
    target: ValidationTarget,
    as_of_date: date,
    reason: str,
    windows: tuple[ValidationWindowResult, ...] = (),
) -> InstrumentValidationResult:
    return _no_trade_result(target, ValidationStatus.DATA_REJECTED, as_of_date, reason, windows, data_valid=False)


def _no_trade_result(
    target: ValidationTarget,
    status: ValidationStatus,
    as_of_date: date,
    reason: str,
    windows: tuple[ValidationWindowResult, ...] = (),
    *,
    data_valid: bool = True,
) -> InstrumentValidationResult:
    blocker = "data_valid" if not data_valid else "stable_parameter_region"
    return InstrumentValidationResult(
        target, status, as_of_date, reason, windows,
        scope=target.scope,
        decision=DecisionSummary(ResearchConclusion.DO_NOT_TRADE, (blocker,)),
    )


def _activation_eligible(scope: ValidationScope, decision: DecisionSummary) -> bool:
    """Formal research can activate only on an explicit passed conclusion."""
    return scope is ValidationScope.FORMAL and decision.conclusion is ResearchConclusion.PASSED


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
