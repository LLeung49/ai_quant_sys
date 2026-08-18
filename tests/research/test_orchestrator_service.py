from datetime import date

import pytest

from morning_conference.sector_rotation2.research.orchestrator.service import build_sector_opportunity_snapshots
from morning_conference.sector_rotation2.research.snapshot import InMemorySnapshotStore, SnapshotConflictError
from morning_conference.sector_rotation2.research.status import ExecutionStatus, ResearchStatus, SnapshotMode


def v1_row(**changes: object) -> dict[str, object]:
    row = {
        "sector_name": "半导体", "score_eligible": True, "lifecycle_state": "trending",
        "phase_confirmed": "accel_up", "phase_confidence": 0.8, "participation_score": 0.2,
        "rank_change_5d": 2, "composite_score": 0.75,
    }
    row.update(changes)
    return row


def test_live_run_produces_shadow_manual_only_live_snapshot() -> None:
    store = InMemorySnapshotStore()
    snapshots = build_sector_opportunity_snapshots(
        store, [v1_row()], [{"sector_name": "半导体", "short_term_labels": "pulse_up"}],
        as_of_date=date(2026, 8, 18), sector_level=1, run_id="run-1",
    )
    snapshot = snapshots[0]
    assert snapshot.research_status is ResearchStatus.SHADOW
    assert snapshot.execution_status is ExecutionStatus.MANUAL_ONLY
    assert snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW
    assert snapshot.candidate_status == "trend_reinforced"


def test_backfill_marks_snapshot_mode_backfill() -> None:
    snapshots = build_sector_opportunity_snapshots(
        InMemorySnapshotStore(), [v1_row()], [], as_of_date=date(2026, 8, 18),
        sector_level=1, run_id="run-1", snapshot_mode=SnapshotMode.BACKFILL,
    )
    assert snapshots[0].snapshot_mode is SnapshotMode.BACKFILL


def test_changed_live_payload_conflicts_instead_of_overwriting() -> None:
    store = InMemorySnapshotStore()
    build_sector_opportunity_snapshots(store, [v1_row(composite_score=0.75)], [], date(2026, 8, 18), 1, "run-1")
    with pytest.raises(SnapshotConflictError):
        build_sector_opportunity_snapshots(store, [v1_row(composite_score=0.80)], [], date(2026, 8, 18), 1, "run-2")


def test_v2_only_sector_is_ignored_because_v1_owns_the_universe() -> None:
    assert build_sector_opportunity_snapshots(
        InMemorySnapshotStore(), [], [{"sector_name": "半导体", "short_term_labels": "pulse_up"}],
        date(2026, 8, 18), 1, "run-1",
    ) == []
