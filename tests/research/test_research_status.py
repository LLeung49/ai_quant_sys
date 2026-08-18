from morning_conference.sector_rotation2.research.status import (
    ExecutionStatus,
    ResearchStatus,
    SnapshotMode,
    ValidationStatus,
)


def test_research_status_contract() -> None:
    assert ResearchStatus.DRAFT.value == "draft"
    assert ResearchStatus.SHADOW.value == "shadow"
    assert ResearchStatus.VALIDATED.value == "validated"
    assert ResearchStatus.REJECTED.value == "rejected"


def test_validation_status_contract() -> None:
    assert ValidationStatus.NOT_EVALUATED.value == "not_evaluated"
    assert ValidationStatus.EVALUATING.value == "evaluating"
    assert ValidationStatus.VALIDATED.value == "validated"
    assert ValidationStatus.REJECTED.value == "rejected"


def test_snapshot_modes_are_distinct() -> None:
    assert SnapshotMode.LIVE_SHADOW.value == "live_shadow"
    assert SnapshotMode.BACKFILL.value == "backfill"
    assert SnapshotMode.REPLAY.value == "replay"


def test_v0_execution_is_manual_only() -> None:
    assert ExecutionStatus.MANUAL_ONLY.value == "manual_only"
