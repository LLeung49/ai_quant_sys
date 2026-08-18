from datetime import date

from morning_conference.sector_rotation2.research.contracts import (
    CandidateSnapshot,
    ResearchContext,
    SnapshotIdentity,
)
from morning_conference.sector_rotation2.research.status import (
    ExecutionStatus,
    ResearchStatus,
    SnapshotMode,
    ValidationStatus,
)


def test_candidate_snapshot_separates_candidate_and_research_status() -> None:
    snap = CandidateSnapshot(
        as_of_date=date(2026, 8, 17), entity_type="etf", entity_code="512480.SH",
        sector_level=1, sector_name="半导体", strategy_type="etf_core",
        candidate_status="ready", candidate_score=0.9, research_status=ResearchStatus.SHADOW,
        validation_status=ValidationStatus.NOT_EVALUATED,
        execution_status=ExecutionStatus.MANUAL_ONLY, model_version="v1", config_hash="abc",
        run_id="run-1", snapshot_mode=SnapshotMode.LIVE_SHADOW,
    )
    assert snap.candidate_status == "ready"
    assert snap.research_status is ResearchStatus.SHADOW
    assert snap.execution_status is ExecutionStatus.MANUAL_ONLY
    assert snap.identity == SnapshotIdentity(date(2026, 8, 17), "etf", "512480.SH", "etf_core", "v1", "abc", SnapshotMode.LIVE_SHADOW)


def test_research_context_is_immutable() -> None:
    context = ResearchContext(date(2026, 8, 17), 1, "v1", "abc", "run-1")
    assert context.as_of_date == date(2026, 8, 17)
