"""Construct ETF SHADOW candidates from already-calculated evidence."""

from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Any, Mapping

from ..config_hash import build_config_hash
from ..contracts import CandidateSnapshot
from ..status import SnapshotMode
from ..snapshot import SnapshotStore, persist_backfill_snapshot, persist_live_shadow_snapshot
from .selector import select_candidate_status


def build_etf_candidate(*, as_of_date: date, sector_level: int, sector_name: str, etf_code: str,
                        sector_allowed: bool, liquid: bool, macd_evidence: dict[str, Any] | None,
                        extended: bool, run_id: str, model_version: str = "etf_core_v1",
                        snapshot_mode: SnapshotMode = SnapshotMode.LIVE_SHADOW,
                        mapping_metadata: Mapping[str, Any] | None = None) -> CandidateSnapshot:
    evidence = macd_evidence or {}
    normalized_mapping = normalize_mapping_metadata(mapping_metadata or {})
    mapping = _mapping_provenance(
        normalized_mapping, sector_level=sector_level, sector_name=sector_name, etf_code=etf_code,
    )
    status = select_candidate_status(sector_allowed=sector_allowed, liquid=liquid,
                                     macd_triggered=bool(evidence.get("macd_triggered")), extended=extended)
    return CandidateSnapshot(
        as_of_date=as_of_date, entity_type="etf", entity_code=etf_code, sector_level=sector_level,
        sector_name=sector_name, strategy_type="etf_core", candidate_status=status, candidate_score=None,
        model_version=model_version,
        config_hash=build_config_hash({"model_version": model_version, "mapping": mapping}), run_id=run_id,
        snapshot_mode=snapshot_mode,
        feature_json={"sector_allowed": sector_allowed, "liquid": liquid, "mapping": mapping, **evidence},
        reasons_json=(f"candidate_status={status}",), risk_flags_json=(),
    )


def persist_etf_candidate(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    return persist_live_shadow_snapshot(store, snapshot) if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW else persist_backfill_snapshot(store, snapshot)


def normalize_mapping_metadata(value: Any) -> Any:
    """Convert database scalar types in mapping metadata to JSON-safe values."""

    if isinstance(value, (date, Decimal)):
        return value.isoformat() if isinstance(value, date) else str(value)
    if isinstance(value, Enum):
        return normalize_mapping_metadata(value.value)
    if isinstance(value, Mapping):
        return {str(key): normalize_mapping_metadata(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize_mapping_metadata(item) for item in value]
    return value


def _mapping_provenance(
    mapping: Mapping[str, Any], *, sector_level: int, sector_name: str, etf_code: str,
) -> dict[str, Any]:
    """Select immutable mapping inputs for the ETF snapshot identity hash."""

    fields = (
        "source_as_of_date", "source_provider", "membership_as_of_date",
        "constituent_as_of_date", "exposure_weight", "coverage_ratio",
        "mapping_version", "config_hash", "rank_no", "weight_unit",
        "membership_asof_mode", "mapping_type", "quality_status",
    )
    provenance = {
        "sector_level": sector_level,
        "sector_name": sector_name,
        "etf_code": etf_code,
        **{name: mapping[name] for name in fields if name in mapping},
    }
    upstream = mapping.get("upstream_sector_snapshot")
    if isinstance(upstream, Mapping):
        upstream_fields = (
            "as_of_date", "entity_type", "entity_code", "strategy_type",
            "model_version", "config_hash", "snapshot_mode",
        )
        provenance["upstream_sector_snapshot"] = {
            name: upstream[name] for name in upstream_fields if name in upstream
        }
    return provenance
