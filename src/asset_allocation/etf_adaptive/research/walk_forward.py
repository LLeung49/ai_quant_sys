"""Walk-forward window construction and staged parameter selection.

Walk-forward selection splits the trading calendar into rolling training and
validation windows. Within each training window the GRID-only and TREND-only
candidate families are screened separately, their stable neighborhoods are
combined, and the resulting full configuration is frozen for the subsequent
validation window. The selector callable only ever observes training
evidence; validation results never feed back into parameter selection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Mapping, Protocol, Sequence

from ..config import AdaptiveConfig
from .parameters import ParameterCandidate


TRAIN_SESSIONS: int = 504
VALIDATION_SESSIONS: int = 126
STEP_SESSIONS: int = 126


def _require_sorted_unique_dates(dates: Sequence[date]) -> tuple[date, ...]:
    if not dates:
        raise ValueError("build_windows requires at least one trading date")
    sorted_dates = tuple(sorted(dates))
    if sorted_dates != tuple(dates):
        raise ValueError("build_windows requires sorted trading dates")
    if len(sorted_dates) != len(set(sorted_dates)):
        raise ValueError("build_windows requires unique trading dates")
    return sorted_dates


@dataclass(frozen=True)
class WalkForwardWindow:
    window_id: str
    train_dates: tuple[date, ...]
    validation_dates: tuple[date, ...]

    def __post_init__(self) -> None:
        if not self.train_dates:
            raise ValueError("train_dates must not be empty")
        if not self.validation_dates:
            raise ValueError("validation_dates must not be empty")
        if self.train_dates[-1] >= self.validation_dates[0]:
            raise ValueError("validation window must start after the training window")

    @property
    def train_end(self) -> date:
        return self.train_dates[-1]

    @property
    def validation_end(self) -> date:
        return self.validation_dates[-1]


def build_windows(
    trading_dates: Sequence[date],
    *,
    train_sessions: int = TRAIN_SESSIONS,
    validation_sessions: int = VALIDATION_SESSIONS,
    step_sessions: int = STEP_SESSIONS,
) -> tuple[WalkForwardWindow, ...]:
    """Return rolling windows that satisfy the warm-up, training, validation spec."""

    if train_sessions <= 0 or validation_sessions <= 0 or step_sessions <= 0:
        raise ValueError("train, validation, and step sizes must be positive")
    dates = _require_sorted_unique_dates(trading_dates)
    minimum_length = train_sessions + validation_sessions
    if len(dates) < minimum_length:
        raise ValueError(
            f"need at least {minimum_length} dates for the first window "
            f"(train {train_sessions} + validation {validation_sessions})",
        )

    windows: list[WalkForwardWindow] = []
    for validation_start in range(train_sessions, len(dates) - validation_sessions + 1, step_sessions):
        train_slice = dates[validation_start - train_sessions:validation_start]
        validation_slice = dates[validation_start:validation_start + validation_sessions]
        windows.append(WalkForwardWindow(
            window_id=f"wf_{len(windows):03d}",
            train_dates=train_slice,
            validation_dates=validation_slice,
        ))
    return tuple(windows)


class TrainingSurfacePointLike(Protocol):
    """The minimum shape the staged selector observes per candidate."""

    candidate_hash: str
    candidate: ParameterCandidate
    last_training_date: date
    positive_windows: Sequence[bool]
    oos_returns: Sequence[float]

    @property
    def positive_window_share(self) -> float: ...


class StagedSelector(Protocol):
    """A selector callable that consumes staged training evidence."""

    def __call__(
        self,
        window: WalkForwardWindow,
        training_results: Mapping[str, Mapping[str, TrainingSurfacePointLike]],
    ) -> tuple[ParameterCandidate, ParameterCandidate]: ...


@dataclass(frozen=True)
class StagedWalkForwardRequest:
    """Inputs required to drive one staged walk-forward pass."""

    trading_dates: Sequence[date]
    selector: StagedSelector
    base_config: AdaptiveConfig = field(default_factory=AdaptiveConfig.default)


@dataclass(frozen=True)
class FrozenWindowSelection:
    """The frozen full configuration and the evidence that produced it."""

    window: WalkForwardWindow
    frozen_grid: ParameterCandidate
    frozen_trend: ParameterCandidate
    grid_training_results: Mapping[str, TrainingSurfacePointLike]
    trend_training_results: Mapping[str, TrainingSurfacePointLike]


@dataclass(frozen=True)
class WalkForwardResult:
    """The complete output of a staged walk-forward run."""

    request: StagedWalkForwardRequest
    windows: tuple[WalkForwardWindow, ...]
    window_selections: tuple[FrozenWindowSelection, ...]

    @property
    def stitched_grid_configs(self) -> tuple[ParameterCandidate, ...]:
        return tuple(selection.frozen_grid for selection in self.window_selections)

    @property
    def stitched_trend_configs(self) -> tuple[ParameterCandidate, ...]:
        return tuple(selection.frozen_trend for selection in self.window_selections)


def _ensure_selector_only_sees_training(
    selector: StagedSelector,
    window: WalkForwardWindow,
    training_results: Mapping[str, Mapping[str, TrainingSurfacePointLike]],
) -> tuple[ParameterCandidate, ParameterCandidate]:
    train_end = window.train_end
    for family_results in training_results.values():
        for point in family_results.values():
            if point.last_training_date > train_end:
                raise ValueError(
                    f"selector input contains dates beyond training end: {point.last_training_date}"
                )
    return selector(window, training_results)


def run_staged_walk_forward(
    request: StagedWalkForwardRequest,
    *,
    training_evidence: Callable[
        [WalkForwardWindow],
        Mapping[str, Mapping[str, TrainingSurfacePointLike]],
    ] | None = None,
) -> WalkForwardResult:
    """Run staged training-then-validation selection over every walk-forward window.

    ``training_evidence`` is a callable that, for each window, supplies the
    GRID and TREND training results (already produced upstream by the backtest
    engine). When omitted, an empty evidence map is used so the orchestration
    can be exercised in isolation.
    """

    if not isinstance(request, StagedWalkForwardRequest):
        raise ValueError("run_staged_walk_forward expects a StagedWalkForwardRequest")
    windows = build_windows(request.trading_dates)
    evidence_builder = training_evidence or (lambda window: {"grid": {}, "trend": {}})
    selections: list[FrozenWindowSelection] = []
    for window in windows:
        training_results = evidence_builder(window)
        grid_candidate, trend_candidate = _ensure_selector_only_sees_training(
            request.selector, window, training_results,
        )
        grid_training = training_results.get("grid", {})
        trend_training = training_results.get("trend", {})
        selections.append(FrozenWindowSelection(
            window=window,
            frozen_grid=grid_candidate,
            frozen_trend=trend_candidate,
            grid_training_results=grid_training,
            trend_training_results=trend_training,
        ))
    return WalkForwardResult(
        request=request,
        windows=windows,
        window_selections=tuple(selections),
    )
