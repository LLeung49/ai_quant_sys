"""Deterministic ranking of training evidence inside an approved plateau."""

from dataclasses import asdict, dataclass, fields
from math import isfinite
from types import MappingProxyType
from typing import Mapping, Sequence, get_type_hints

from ..config import AdaptiveConfig, CostConfig, GridConfig, TrendConfig
from .decision import _MAX_COST_DRAG
from .parameters import conservative_config_key


class _ImmutableMapping(Mapping[str, object]):
    """Deep read-only snapshot preserved by ordinary copy protocols."""

    __slots__ = ("_data",)

    def __init__(self, payload: Mapping[str, object]) -> None:
        if hasattr(self, "_data"):
            raise TypeError("configuration snapshot is immutable")
        object.__setattr__(self, "_data", MappingProxyType({
            key: _ImmutableMapping(value) if isinstance(value, Mapping) else value
            for key, value in payload.items()
        }))

    def __getitem__(self, key: str) -> object:
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __setattr__(self, name, value) -> None:
        raise TypeError("configuration snapshot is immutable")

    def __delattr__(self, name) -> None:
        raise TypeError("configuration snapshot is immutable")

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


def _finite_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and isfinite(value)


def _validated_config(payload: Mapping[str, object], config_hash: str) -> dict[str, object]:
    """Require all canonical fields and types before binding the full hash."""
    section_types = {"grid": GridConfig, "trend": TrendConfig, "cost": CostConfig}
    if not isinstance(payload, Mapping) or set(payload) != set(section_types):
        raise ValueError("config must contain exactly grid, trend, and cost")
    sections = {}
    for section, config_type in section_types.items():
        values = payload[section]
        if not isinstance(values, Mapping) or set(values) != {field.name for field in fields(config_type)}:
            raise ValueError(f"config.{section} must contain every canonical field and no extras")
        for name, expected in get_type_hints(config_type).items():
            value = values[name]
            if expected in (float, float | None):
                valid = _finite_number(value) or (expected == float | None and value is None)
            else:
                valid = type(value) is expected
            if not valid:
                raise ValueError(f"config.{section}.{name} has a noncanonical value")
        try:
            sections[section] = config_type(**values)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid config.{section}: {exc}") from exc
    canonical = AdaptiveConfig(**sections)
    if config_hash != canonical.config_hash():
        raise ValueError("config_hash does not match the complete canonical config")
    return asdict(canonical)


_SCORE_METRICS = (
    "positive_subperiod_share", "sortino_excess", "sharpe_excess",
    "drawdown_improvement", "cvar5_improvement", "cost_drag", "exposure_ratio",
)


def _metric_rejection_reason(score: "TrainingCandidateScore") -> str | None:
    invalid = [name for name in _SCORE_METRICS
               if getattr(score, name) is not None and not _finite_number(getattr(score, name))]
    if invalid:
        return "invalid_training_metrics:" + ",".join(invalid)
    unavailable = [name for name in _SCORE_METRICS if getattr(score, name) is None]
    if unavailable:
        return "unavailable_training_metrics:" + ",".join(unavailable)
    for name, upper in (("positive_subperiod_share", 1.0), ("exposure_ratio", 1.0), ("cost_drag", _MAX_COST_DRAG)):
        if not 0.0 <= getattr(score, name) <= upper:
            return name + "_out_of_bounds"
    return None


@dataclass(frozen=True)
class TrainingCandidateScore:
    """Equal-subperiod excess metrics; no validation observations are inputs.

    ``positive_subperiod_share`` retains the stability rule's non-lagging
    convention (strategy return >= B&H return). Cost drag is total strategy
    cost divided by the sum of starting training NAVs; exposure is the share
    of recorded training sessions with an invested position. Family and axes
    distinguish repeated configurations across sequential screening stages.
    Unavailable/invalid metrics are recorded as None with an explicit rejection
    reason. Selection also requires the existing 2% research cost-drag limit.
    """

    config_hash: str
    config: Mapping[str, object]
    positive_subperiod_share: float | None
    sortino_excess: float | None
    sharpe_excess: float | None
    drawdown_improvement: float | None
    cvar5_improvement: float | None
    cost_drag: float | None
    exposure_ratio: float | None
    stable: bool
    rejection_reason: str | None
    family: str = "full"
    screened_axes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "config", _ImmutableMapping(_validated_config(self.config, self.config_hash)))
        reason = _metric_rejection_reason(self)
        if reason is not None:
            for name in _SCORE_METRICS:
                if not _finite_number(getattr(self, name)):
                    object.__setattr__(self, name, None)
        elif not isinstance(self.stable, bool) or (
            self.rejection_reason is not None
            and (not isinstance(self.rejection_reason, str) or not self.rejection_reason.strip())
        ):
            reason = "invalid_score_state"
        else:
            reason = self.rejection_reason or (None if self.stable else "outside_stable_plateau")
        object.__setattr__(self, "stable", self.stable is True and reason is None)
        object.__setattr__(self, "rejection_reason", reason)

    def to_dict(self) -> dict[str, object]:
        """Return an independent JSON-ready payload, distinct from copying.

        Ordinary copies must retain the immutable config/hash relationship.
        Only this explicit serialization boundary emits writable dictionaries.
        """
        payload = asdict(self)
        payload["config"] = _validated_config(self.config, self.config_hash)
        return payload


def select_stable_representative(
    scores: Sequence[TrainingCandidateScore],
) -> TrainingCandidateScore | None:
    """Apply the stability gate before lexicographic training-only ranking."""
    stable = []
    for score in scores:
        if score.stable is not True or score.rejection_reason is not None or _metric_rejection_reason(score) is not None:
            continue
        try:
            _validated_config(score.config, score.config_hash)
        except ValueError:
            continue
        stable.append(score)
    return min(stable, key=lambda score: (
        -score.positive_subperiod_share,
        -score.sortino_excess,
        -score.sharpe_excess,
        score.cost_drag,
        conservative_config_key(score.config),
        score.config_hash,
    ), default=None)
