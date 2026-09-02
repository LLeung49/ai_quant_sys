"""Build immutable Sector Opportunity candidates from v1-owned sector rows."""

from collections.abc import Iterable, Mapping
from dataclasses import replace
from datetime import date
from typing import Any

from ..config_hash import build_config_hash
from ..availability import AvailabilityMetadata
from ..contracts import CandidateSnapshot
from ..snapshot import SnapshotStore
from ..status import SnapshotMode
from .confidence import build_evidence, map_playbook
from .labels import classify_short_term_direction
from .rules import classify_opportunity
from .store import persist_sector_opportunity


def build_sector_opportunity_snapshots(
    store: SnapshotStore,
    v1_rows: Iterable[Mapping[str, Any]],
    v2_rows: Iterable[Mapping[str, Any]],
    as_of_date: date,
    sector_level: int,
    run_id: str,
    *,
    model_version: str = "sector_opportunity_v1",
    snapshot_mode: SnapshotMode = SnapshotMode.LIVE_SHADOW,
    availability: AvailabilityMetadata | None = None,
    persist: bool = True,
) -> list[CandidateSnapshot]:
    """Join exact-name v2 evidence onto the v1 sector universe and persist candidates."""
    v2_by_sector = {str(row["sector_name"]): row for row in v2_rows}
    config_hash = build_config_hash({"model_version": model_version, "sector_level": sector_level})
    snapshots: list[CandidateSnapshot] = []
    for v1 in v1_rows:
        sector_name = str(v1["sector_name"])
        v2 = v2_by_sector.get(sector_name, {})
        direction = classify_short_term_direction(v2.get("short_term_labels"))
        state = classify_opportunity(v1, direction)
        evidence = build_evidence(v1, direction, state)
        snapshot = CandidateSnapshot(
            as_of_date=as_of_date,
            entity_type="sector",
            entity_code=sector_name,
            sector_level=sector_level,
            sector_name=sector_name,
            strategy_type="sector_opportunity",
            candidate_status=state.value,
            candidate_score=_as_float(v1.get("composite_score")),
            model_version=model_version,
            config_hash=config_hash,
            run_id=run_id,
            snapshot_mode=snapshot_mode,
            feature_json={
                "lifecycle_state": v1.get("lifecycle_state"),
                "phase_confirmed": v1.get("phase_confirmed"),
                "short_term_direction": direction,
                "playbook": map_playbook(state).value,
                "support_count": evidence.support_count,
                "conflict_count": evidence.conflict_count,
                "confidence_level": evidence.confidence_level,
            },
            reasons_json=evidence.reasons or (evidence.primary_reason,),
            risk_flags_json=evidence.risk_flags,
        )
        if availability is not None:
            snapshot = replace(
                snapshot,
                data_available_at=availability.data_available_at,
                run_at=availability.run_at,
                execution_eligible_at=availability.execution_eligible_at,
                availability_basis=availability.availability_basis,
            )
        snapshots.append(persist_sector_opportunity(store, snapshot) if persist else snapshot)
    return snapshots


def _as_float(value: Any) -> float | None:
    return None if value is None else float(value)
