"""Immutable data contracts shared by all candidate-producing strategies."""

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Any, Mapping

from .availability import AvailabilityBasis
from .status import ExecutionStatus, ResearchStatus, SnapshotMode, ValidationStatus


@dataclass(frozen=True)
class ResearchContext:
    as_of_date: date
    sector_level: int
    model_version: str
    config_hash: str
    run_id: str


class _EvaluationStringEnum(str, Enum):
    """String enum base kept compatible with the project's Python baseline."""


class ReturnStatus(_EvaluationStringEnum):
    COMPLETE = "complete"
    NOT_MATURED = "not_matured"
    MISSING_SIGNAL_BAR = "missing_signal_bar"
    UNEXECUTABLE_ENTRY = "unexecutable_entry"
    MISSING_EXIT = "missing_exit"
    UNSUPPORTED_PRICE_WINDOW = "unsupported_price_window"


class PathStatus(_EvaluationStringEnum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    UNSUPPORTED = "unsupported"


class BenchmarkStatus(_EvaluationStringEnum):
    NOT_REQUESTED = "not_requested"
    COMPLETE = "complete"
    MISSING_ENTRY = "missing_entry"
    MISSING_EXIT = "missing_exit"
    UNSUPPORTED_WINDOW = "unsupported_window"


@dataclass(frozen=True)
class SignalFrameSpec:
    signal_family: str
    score_col: str | None
    cross_section_cols: tuple[str, ...]
    event_id_col: str
    supports_rank_metrics: bool


@dataclass(frozen=True)
class ForwardLabel:
    signal_date: date
    entity_type: str
    entity_code: str
    benchmark_type: str
    benchmark_code: str
    horizon: int
    label_type: str
    entry_date: date | None
    exit_date: date | None
    price_basis: str
    signal_close: float | None
    entry_price: float | None
    exit_price: float | None
    entry_gap: float | None
    forward_return: float | None
    benchmark_return: float | None
    excess_return: float | None
    mae: float | None
    mfe: float | None
    return_status: ReturnStatus
    path_status: PathStatus
    benchmark_status: BenchmarkStatus
    is_complete: bool
    excess_is_complete: bool
    source_snapshot_id: int | None = None
    snapshot_mode: SnapshotMode | None = None


@dataclass(frozen=True)
class SnapshotIdentity:
    as_of_date: date
    entity_type: str
    entity_code: str
    strategy_type: str
    model_version: str
    config_hash: str
    snapshot_mode: SnapshotMode


@dataclass(frozen=True)
class CandidateSnapshot:
    as_of_date: date
    entity_type: str
    entity_code: str
    sector_level: int | None
    sector_name: str | None
    strategy_type: str
    candidate_status: str
    candidate_score: float | None
    model_version: str
    config_hash: str
    run_id: str
    research_status: ResearchStatus = ResearchStatus.SHADOW
    validation_status: ValidationStatus = ValidationStatus.NOT_EVALUATED
    execution_status: ExecutionStatus = ExecutionStatus.MANUAL_ONLY
    snapshot_mode: SnapshotMode = SnapshotMode.LIVE_SHADOW
    feature_json: Mapping[str, Any] = field(default_factory=dict)
    reasons_json: tuple[str, ...] = ()
    risk_flags_json: tuple[str, ...] = ()
    rank_in_sector: int | None = None
    snapshot_id: int | None = None
    data_available_at: datetime | None = None
    run_at: datetime | None = None
    execution_eligible_at: datetime | None = None
    availability_basis: AvailabilityBasis | None = None

    @property
    def identity(self) -> SnapshotIdentity:
        return SnapshotIdentity(
            self.as_of_date, self.entity_type, self.entity_code, self.strategy_type,
            self.model_version, self.config_hash, self.snapshot_mode,
        )
