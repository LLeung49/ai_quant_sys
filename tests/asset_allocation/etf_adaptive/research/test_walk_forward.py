"""Walk-forward windows and staged parameter selection."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Iterable, Mapping

from asset_allocation.etf_adaptive.config import AdaptiveConfig, GridConfig, TrendConfig
from asset_allocation.etf_adaptive.research.parameters import (
    ParameterCandidate,
    grid_candidates,
    trend_candidates,
)
from asset_allocation.etf_adaptive.research.walk_forward import (
    FrozenWindowSelection,
    StagedWalkForwardRequest,
    TrainingSurfacePointLike,
    WalkForwardResult,
    WalkForwardWindow,
    build_windows,
    run_staged_walk_forward,
)


def _trading_dates(count: int) -> tuple[date, ...]:
    start = date(2024, 1, 2)
    return tuple(start + timedelta(days=offset) for offset in range(count))


def test_windows_use_504_train_126_validation_and_126_step() -> None:
    dates = _trading_dates(882)

    windows = build_windows(dates)

    assert len(windows[0].train_dates) == 504
    assert len(windows[0].validation_dates) == 126
    assert windows[1].validation_dates[0] == dates[630]
    assert windows[2].validation_dates[-1] == dates[-1]
    assert windows[0].window_id == "wf_000"


def test_build_windows_rejects_short_calendar() -> None:
    dates = _trading_dates(600)

    try:
        build_windows(dates)
    except ValueError as exc:
        assert "504" in str(exc) or "630" in str(exc)
    else:
        raise AssertionError("expected ValueError when calendar is too short")


def test_build_windows_rejects_unsorted_dates() -> None:
    dates = _trading_dates(882)
    shuffled = (dates[0],) + tuple(reversed(dates[1:]))

    try:
        build_windows(shuffled)
    except ValueError as exc:
        assert "sorted" in str(exc)
    else:
        raise AssertionError("expected ValueError for unsorted dates")


@dataclass(frozen=True)
class _TrainingPoint:
    candidate: ParameterCandidate
    last_training_date: date
    positive_windows: tuple[bool, ...]
    oos_returns: tuple[float, ...]

    @property
    def candidate_hash(self) -> str:
        return self.candidate.config_hash

    @property
    def positive_window_share(self) -> float:
        if not self.positive_windows:
            return 0.0
        return sum(1 for value in self.positive_windows if value) / len(self.positive_windows)


@dataclass
class _SelectorCall:
    window: WalkForwardWindow
    max_date: date
    selected_grid_hash: str
    selected_trend_hash: str


@dataclass
class _SpySelector:
    calls: list[_SelectorCall] = field(default_factory=list)

    def __call__(
        self,
        window: WalkForwardWindow,
        training_results: Mapping[str, Mapping[str, TrainingSurfacePointLike]],
    ) -> tuple[ParameterCandidate, ParameterCandidate]:
        grid_points = training_results["grid"]  # type: ignore[index]
        trend_points = training_results["trend"]  # type: ignore[index]
        max_date = window.train_dates[-1]
        for point in grid_points.values():
            assert point.last_training_date <= max_date
        for point in trend_points.values():
            assert point.last_training_date <= max_date
        grid_first = next(iter(grid_points.values()))
        trend_first = next(iter(trend_points.values()))
        self.calls.append(
            _SelectorCall(
                window=window,
                max_date=max_date,
                selected_grid_hash=grid_first.candidate_hash,
                selected_trend_hash=trend_first.candidate_hash,
            )
        )
        return grid_first.candidate, trend_first.candidate


def _training_evidence(window: WalkForwardWindow) -> dict[str, dict[str, _TrainingPoint]]:
    grid = grid_candidates()
    trend = trend_candidates()
    grid_points = {
        candidate.config_hash: _TrainingPoint(
            candidate=candidate,
            last_training_date=window.train_end,
            positive_windows=(True, True, True),
            oos_returns=(0.05, 0.04, 0.03),
        )
        for candidate in grid[:2]
    }
    trend_points = {
        candidate.config_hash: _TrainingPoint(
            candidate=candidate,
            last_training_date=window.train_end,
            positive_windows=(True, True, True),
            oos_returns=(0.05, 0.04, 0.03),
        )
        for candidate in trend[:2]
    }
    return {"grid": grid_points, "trend": trend_points}


def _request(
    *, selector: _SpySelector, dates: Iterable[date] = (),
) -> StagedWalkForwardRequest:
    return StagedWalkForwardRequest(
        trading_dates=tuple(dates),
        selector=selector,  # type: ignore[arg-type]
        base_config=AdaptiveConfig(grid=GridConfig(), trend=TrendConfig()),
    )


def test_validation_never_calls_selector_with_validation_returns() -> None:
    selector = _SpySelector()

    run_staged_walk_forward(
        _request(selector=selector, dates=_trading_dates(882)),
        training_evidence=_training_evidence,
    )

    assert selector.calls, "selector should be invoked for each window"
    for call in selector.calls:
        assert call.max_date <= call.window.train_end
        assert call.window.validation_dates[0] > call.window.train_end


def test_run_staged_walk_forward_iterates_each_window_once() -> None:
    selector = _SpySelector()

    result = run_staged_walk_forward(
        _request(selector=selector, dates=_trading_dates(882)),
        training_evidence=_training_evidence,
    )

    expected_windows = build_windows(_trading_dates(882))
    assert len(selector.calls) == len(expected_windows)
    assert len(result.window_selections) == len(expected_windows)
    assert tuple(selection.window for selection in result.window_selections) == expected_windows


def test_run_staged_walk_forward_passes_grid_and_trend_training_results() -> None:
    selector = _SpySelector()

    result = run_staged_walk_forward(
        _request(selector=selector, dates=_trading_dates(882)),
        training_evidence=_training_evidence,
    )

    selection = result.window_selections[0]
    assert selection.grid_training_results
    assert selection.trend_training_results
    assert selection.frozen_grid.config_hash != selection.frozen_trend.config_hash
