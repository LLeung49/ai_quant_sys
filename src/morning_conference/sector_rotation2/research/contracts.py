"""Immutable data contracts shared by all candidate-producing strategies."""

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping

from .status import ExecutionStatus, ResearchStatus, SnapshotMode, ValidationStatus


@dataclass(frozen=True)
class ResearchContext:
    as_of_date: date
    sector_level: int
    model_version: str
    config_hash: str
    run_id: str


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

    @property
    def identity(self) -> SnapshotIdentity:
        return SnapshotIdentity(
            self.as_of_date, self.entity_type, self.entity_code, self.strategy_type,
            self.model_version, self.config_hash, self.snapshot_mode,
        )
