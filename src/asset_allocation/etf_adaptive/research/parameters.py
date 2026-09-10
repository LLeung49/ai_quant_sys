"""Deterministic parameter families and stable-neighborhood selection.

The approved parameter spaces below are the only values that may be screened.
Adding or removing a value requires updating the implementation plan and the
specification. ``stable_parameter_neighborhood`` enforces the adjacency rule
the spec mandates: a candidate is part of the plateau only when every tuned
numeric axis sits at a non-edge canonical position, the candidate's own OOS
subperiods clear ``min_positive_window_share``, and every adjacent candidate
that is actually present in the screened surface also clears the threshold.
When a plateau has even cardinality the more conservative (lower-risk)
candidate wins.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Mapping, Protocol, Sequence

from ..config import AdaptiveConfig, GridConfig, TrendConfig


GRID_STEPS: tuple[float, ...] = tuple(value / 1000 for value in range(10, 65, 5))
GRID_UNITS: tuple[float, ...] = (0.05, 0.10, 0.15, 0.20)
FIXED_INITIAL: tuple[float, ...] = (0.30, 0.40, 0.50, 0.60, 0.70)
RISK_PER_UNIT: tuple[float, ...] = (0.0025, 0.0050, 0.0075, 0.0100)
ADD_N: tuple[float, ...] = (0.5, 0.75, 1.0)
MAX_UNITS: tuple[int, ...] = (2, 3, 4)
AMOUNT_RATIO: tuple[float | None, ...] = (None, 1.0, 1.2, 1.5)
GRID_ATR_STOP_MULTIPLES: tuple[float, ...] = (2.0, 3.0, 4.0)
GRID_COOLDOWN_SESSIONS: tuple[int, ...] = (0, 3, 5, 10)
TREND_STOP_N: tuple[float, ...] = (1.5, 2.0, 2.5, 3.0)
TREND_REQUIRE_MACD_BULLISH: tuple[bool, ...] = (False, True)

_GRID_AXES = (
    "step_pct",
    "unit_pct",
    "fixed_initial_pct",
    "atr_stop_multiple",
    "cooldown_sessions",
)
_TREND_AXES = (
    "stop_n",
    "risk_per_unit",
    "add_n",
    "max_units",
    "amount_ratio_min",
    "require_macd_bullish",
)
_EXPANDABLE_AXES = {
    "atr_stop_multiple",
    "cooldown_sessions",
    "stop_n",
    "require_macd_bullish",
}
_AxisValue = float | bool


def _axis_values(axis: str) -> Sequence[_AxisValue]:
    if axis == "step_pct":
        return GRID_STEPS
    if axis == "unit_pct":
        return GRID_UNITS
    if axis == "fixed_initial_pct":
        return FIXED_INITIAL
    if axis == "risk_per_unit":
        return RISK_PER_UNIT
    if axis == "add_n":
        return ADD_N
    if axis == "max_units":
        return tuple(float(value) for value in MAX_UNITS)
    if axis == "amount_ratio_min":
        return tuple(value if value is not None else float("-inf") for value in AMOUNT_RATIO)
    if axis == "atr_stop_multiple":
        return GRID_ATR_STOP_MULTIPLES
    if axis == "cooldown_sessions":
        return tuple(float(value) for value in GRID_COOLDOWN_SESSIONS)
    if axis == "stop_n":
        return TREND_STOP_N
    if axis == "require_macd_bullish":
        return TREND_REQUIRE_MACD_BULLISH
    raise ValueError(f"unknown tuned axis: {axis}")


def _axis_key(axis: str, candidate: "ParameterCandidate") -> _AxisValue:
    if axis == "step_pct":
        return candidate.config.grid.step_pct
    if axis == "unit_pct":
        return candidate.config.grid.unit_pct
    if axis == "fixed_initial_pct":
        value = candidate.config.grid.fixed_initial_pct
        if value is None:
            raise ValueError("fixed_initial_pct axis requires a fixed_initial_pct value")
        return value
    if axis == "risk_per_unit":
        return candidate.config.trend.risk_per_unit
    if axis == "add_n":
        return candidate.config.trend.add_n
    if axis == "max_units":
        return float(candidate.config.trend.max_units)
    if axis == "amount_ratio_min":
        value = candidate.config.trend.amount_ratio_min
        return float("-inf") if value is None else value
    if axis == "atr_stop_multiple":
        return candidate.config.grid.atr_stop_multiple
    if axis == "cooldown_sessions":
        return float(candidate.config.grid.cooldown_sessions)
    if axis == "stop_n":
        return candidate.config.trend.stop_n
    if axis == "require_macd_bullish":
        return candidate.config.trend.require_macd_bullish
    raise ValueError(f"unknown tuned axis: {axis}")


@dataclass(frozen=True)
class ParameterCandidate:
    """A frozen (grid, trend) configuration and its canonical identity."""

    config: AdaptiveConfig
    family: str = "full"

    def __post_init__(self) -> None:
        if self.family not in {"grid_only", "trend_only", "full"}:
            raise ValueError("family must be grid_only, trend_only, or full")

    @property
    def config_hash(self) -> str:
        return self.config.config_hash()


class SurfacePointLike(Protocol):
    """The minimum shape ``stable_parameter_neighborhood`` accepts."""

    config_hash: str
    axis_values: Mapping[str, _AxisValue]
    positive_windows: Sequence[bool]

    @property
    def positive_window_share(self) -> float: ...


def _grid_only_configs() -> tuple[GridConfig, ...]:
    configs: list[GridConfig] = []
    for step in GRID_STEPS:
        for unit in GRID_UNITS:
            for fixed in FIXED_INITIAL:
                for stop_multiple in GRID_ATR_STOP_MULTIPLES:
                    for cooldown_sessions in GRID_COOLDOWN_SESSIONS:
                        configs.append(
                            GridConfig(
                                step_pct=step,
                                unit_pct=unit,
                                initial_model="fixed",
                                fixed_initial_pct=fixed,
                                atr_stop_multiple=stop_multiple,
                                cooldown_sessions=cooldown_sessions,
                            )
                        )
    return tuple(configs)


def _trend_only_configs() -> tuple[TrendConfig, ...]:
    configs: list[TrendConfig] = []
    for risk in RISK_PER_UNIT:
        for add in ADD_N:
            for units in MAX_UNITS:
                for amount in AMOUNT_RATIO:
                    for stop_n in TREND_STOP_N:
                        for require_macd_bullish in TREND_REQUIRE_MACD_BULLISH:
                            configs.append(
                                TrendConfig(
                                    stop_n=stop_n,
                                    risk_per_unit=risk,
                                    add_n=add,
                                    max_units=units,
                                    require_macd_bullish=require_macd_bullish,
                                    amount_ratio_min=amount,
                                )
                            )
    return tuple(configs)


def _candidates_for(configs: Sequence[AdaptiveConfig], family: str) -> tuple[ParameterCandidate, ...]:
    seen: set[str] = set()
    ordered: list[ParameterCandidate] = []
    for config in configs:
        candidate = ParameterCandidate(config=config, family=family)
        if candidate.config_hash in seen:
            raise ValueError(f"duplicate canonical id detected: {candidate.config_hash}")
        seen.add(candidate.config_hash)
        ordered.append(candidate)
    return tuple(ordered)


def grid_candidates() -> tuple[ParameterCandidate, ...]:
    """Enumerate every deterministic GRID-only candidate as a frozen tuple."""

    configs = [
        AdaptiveConfig(grid=grid, trend=TrendConfig())
        for grid in _grid_only_configs()
    ]
    return _candidates_for(configs, family="grid_only")


def trend_candidates() -> tuple[ParameterCandidate, ...]:
    """Enumerate every deterministic TREND-only candidate as a frozen tuple."""

    configs = [
        AdaptiveConfig(grid=GridConfig(), trend=trend)
        for trend in _trend_only_configs()
    ]
    return _candidates_for(configs, family="trend_only")


def expand_candidate_axis(
    base_candidate: ParameterCandidate,
    *,
    axis: str,
) -> tuple[ParameterCandidate, ...]:
    """Vary one approved exit/filter axis while preserving a selected base.

    Walk-forward selection uses this bounded expansion after choosing the
    existing training candidate, rather than replaying a cross-product of
    legacy and new axes. The returned sequence includes the base value when
    it is approved so adjacent values can form a complete screened surface.
    """

    if axis not in _EXPANDABLE_AXES:
        raise ValueError(f"axis is not approved for one-axis expansion: {axis}")
    if axis in _GRID_AXES and base_candidate.family == "trend_only":
        raise ValueError("grid axes require a grid_only or full base candidate")
    if axis in _TREND_AXES and base_candidate.family == "grid_only":
        raise ValueError("trend axes require a trend_only or full base candidate")

    configs: list[AdaptiveConfig] = []
    for value in _axis_values(axis):
        if axis == "atr_stop_multiple":
            config = replace(
                base_candidate.config,
                grid=replace(base_candidate.config.grid, atr_stop_multiple=float(value)),
            )
        elif axis == "cooldown_sessions":
            config = replace(
                base_candidate.config,
                grid=replace(base_candidate.config.grid, cooldown_sessions=int(value)),
            )
        elif axis == "stop_n":
            config = replace(
                base_candidate.config,
                trend=replace(base_candidate.config.trend, stop_n=float(value)),
            )
        else:
            config = replace(
                base_candidate.config,
                trend=replace(base_candidate.config.trend, require_macd_bullish=bool(value)),
            )
        configs.append(config)
    return _candidates_for(configs, family=base_candidate.family)


def _index_axis(value: float, axis: str) -> int:
    values = _axis_values(axis)
    for index, candidate in enumerate(values):
        if candidate == value or abs(candidate - value) < 1e-12:
            return index
    raise ValueError(f"value {value} not part of axis {axis}")


def _same_axis_value(left: _AxisValue, right: _AxisValue) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return left is right
    return left == right or abs(left - right) < 1e-9


def _axis_group(axis: str) -> Sequence[str]:
    if axis in _GRID_AXES:
        return _GRID_AXES
    if axis in _TREND_AXES:
        return _TREND_AXES
    raise ValueError(f"unknown tuned axis: {axis}")


def _matches_every_nonchanged_axis(
    candidate: ParameterCandidate,
    other_candidate: ParameterCandidate,
    *,
    axis: str,
) -> bool:
    return all(
        _same_axis_value(
            _axis_key(other_axis, candidate),
            _axis_key(other_axis, other_candidate),
        )
        for other_axis in _axis_group(axis)
        if other_axis != axis
    )


def _every_in_surface_neighbor_positive(
    candidate: ParameterCandidate,
    *,
    axis: str,
    surface: Mapping[str, "SurfacePointLike"],
    config_index: Mapping[str, "ParameterCandidate"],
    min_positive_window_share: float,
) -> bool:
    if axis == "require_macd_bullish":
        observed_values: set[bool] = set()
        for other_hash, other_point in surface.items():
            other_candidate = config_index.get(other_hash)
            if other_candidate is None or not _matches_every_nonchanged_axis(
                candidate, other_candidate, axis=axis,
            ):
                continue
            other_value = _axis_key(axis, other_candidate)
            if not isinstance(other_value, bool):
                continue
            if other_point.positive_window_share + 1e-9 < min_positive_window_share:
                return False
            observed_values.add(other_value)
        return observed_values == set(TREND_REQUIRE_MACD_BULLISH)

    axis_index = _index_axis(_axis_key(axis, candidate), axis)
    values = _axis_values(axis)
    if axis_index == 0 or axis_index == len(values) - 1:
        return False
    lower_value = values[axis_index - 1]
    upper_value = values[axis_index + 1]
    found_lower = False
    found_upper = False
    for other_hash, other_point in surface.items():
        if other_hash == candidate.config_hash:
            continue
        other_candidate = config_index.get(other_hash)
        if other_candidate is None or not _matches_every_nonchanged_axis(
            candidate, other_candidate, axis=axis,
        ):
            continue
        other_axis_value = _axis_key(axis, other_candidate)
        is_lower = _same_axis_value(other_axis_value, lower_value)
        is_upper = _same_axis_value(other_axis_value, upper_value)
        if not (is_lower or is_upper):
            continue
        if other_point.positive_window_share + 1e-9 < min_positive_window_share:
            return False
        if is_lower:
            found_lower = True
        if is_upper:
            found_upper = True
    return found_lower and found_upper


def _candidate_key(
    candidate: ParameterCandidate, axes: Sequence[str],
) -> tuple[_AxisValue, ...]:
    return tuple(_axis_key(axis, candidate) for axis in axes)


def stable_parameter_neighborhood(
    results: Mapping[str, SurfacePointLike],
    *,
    axes: Sequence[str],
    min_positive_window_share: float,
) -> tuple[ParameterCandidate, ...]:
    """Return the middle candidate(s) of the stable neighborhood.

    A candidate is part of the plateau when:

    * it sits at a non-edge position on every canonical tuned axis;
    * the candidate's own OOS subperiods clear ``min_positive_window_share``;
    * every numeric axis has a passing lower and upper immediate neighbor
      with every other axis unchanged; and
    * categorical MACD stability has both observed values passing with every
      other axis unchanged.

    When the plateau has even cardinality the more conservative
    (lower-risk) candidate wins.
    """

    if not axes:
        raise ValueError("stable_parameter_neighborhood requires at least one axis")
    if not 0.0 <= min_positive_window_share <= 1.0:
        raise ValueError("min_positive_window_share must be between 0 and 1")

    candidate_index: dict[str, ParameterCandidate] = {}
    for candidates in (grid_candidates(), trend_candidates()):
        for candidate in candidates:
            candidate_index[candidate.config_hash] = candidate

    plateau: list[ParameterCandidate] = []
    for point in results.values():
        candidate = candidate_index.get(point.config_hash)
        if candidate is None:
            continue
        if point.positive_window_share + 1e-9 < min_positive_window_share:
            continue
        if not all(
            _every_in_surface_neighbor_positive(
                candidate,
                axis=axis,
                surface=results,
                config_index=candidate_index,
                min_positive_window_share=min_positive_window_share,
            )
            for axis in axes
        ):
            continue
        plateau.append(candidate)

    if not plateau:
        return ()

    plateau.sort(key=lambda item: _candidate_key(item, axes))
    if len(plateau) % 2 == 0:
        middle_a = plateau[len(plateau) // 2 - 1]
        middle_b = plateau[len(plateau) // 2]
        if middle_a.config.trend.risk_per_unit != middle_b.config.trend.risk_per_unit:
            chosen = min(
                (middle_a, middle_b),
                key=lambda item: (item.config.trend.risk_per_unit, item.config_hash),
            )
        else:
            chosen = min((middle_a, middle_b), key=lambda item: item.config_hash)
        return (chosen,)

    return (plateau[len(plateau) // 2],)
