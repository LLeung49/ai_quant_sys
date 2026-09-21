"""Construct ETF SHADOW candidates from already-calculated evidence."""

from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Any, Mapping

from ..config_hash import build_config_hash
from ..contracts import CandidateSnapshot
from ..status import SnapshotMode
from ..snapshot import (
    SnapshotStore, persist_backfill_snapshot, persist_delayed_shadow_snapshot,
    persist_live_shadow_snapshot,
)
from .selector import select_candidate_status


def build_etf_candidate(*, as_of_date: date, sector_level: int, sector_name: str, etf_code: str,
                        sector_allowed: bool, liquid: bool | None, macd_evidence: dict[str, Any] | None,
                        extended: bool | None, run_id: str, model_version: str = "etf_core_v1",
                        snapshot_mode: SnapshotMode = SnapshotMode.LIVE_SHADOW,
                        mapping_metadata: Mapping[str, Any] | None = None,
                        execution_evidence: Mapping[str, Any] | None = None) -> CandidateSnapshot:
    evidence = macd_evidence or {}
    normalized_mapping = normalize_mapping_metadata(mapping_metadata or {})
    mapping = _mapping_provenance(
        normalized_mapping, sector_level=sector_level, sector_name=sector_name, etf_code=etf_code,
    )
    execution = normalize_mapping_metadata(execution_evidence or {})
    if not isinstance(execution, dict):
        execution = {}
    liquid_value = execution.get("liquid") if type(execution.get("liquid")) is bool else liquid
    extended_value = execution.get("extended") if type(execution.get("extended")) is bool else extended
    liquid_value = liquid_value if type(liquid_value) is bool else None
    extended_value = extended_value if type(extended_value) is bool else None
    if liquid_value is not None:
        execution["liquid"] = liquid_value
    if extended_value is not None:
        execution["extended"] = extended_value
    freshness_status = normalized_mapping.get("freshness_status")
    confidence_status = normalized_mapping.get("confidence_status")
    status = select_candidate_status(sector_allowed=sector_allowed, liquid=liquid_value,
                                     macd_triggered=bool(evidence.get("macd_triggered")), extended=extended_value,
                                     freshness_status=freshness_status if isinstance(freshness_status, str) else None,
                                     confidence_status=confidence_status if isinstance(confidence_status, str) else None)
    missing_execution = liquid_value is None or extended_value is None
    risk_flags = (
        *(("stale_holdings",) if freshness_status == "stale" else ()),
        *(("low_return_exposure_confidence",) if confidence_status == "low_confidence" else ()),
        *(("missing_execution_evidence",) if missing_execution else ()),
    )
    return CandidateSnapshot(
        as_of_date=as_of_date, entity_type="etf", entity_code=etf_code, sector_level=sector_level,
        sector_name=sector_name, strategy_type="etf_core", candidate_status=status, candidate_score=None,
        model_version=model_version,
        config_hash=build_config_hash({"model_version": model_version, "mapping": mapping}), run_id=run_id,
        snapshot_mode=snapshot_mode,
        feature_json={"sector_allowed": sector_allowed, "mapping": mapping, **execution, **evidence},
        reasons_json=(f"candidate_status={status}",),
        risk_flags_json=risk_flags,
    )


def persist_etf_candidate(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW:
        return persist_live_shadow_snapshot(store, snapshot)
    if snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW:
        return persist_delayed_shadow_snapshot(store, snapshot)
    return persist_backfill_snapshot(store, snapshot)


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
        "membership_asof_mode", "mapping_type", "quality_status", "source_reference",
        "constituent_reported_date", "holdings_age_days", "freshness_status",
        "freshness_confidence", "basket_source_priority", "cross_check_status",
        "cross_check_detail",
        "mapping_method", "window_start_date", "window_end_date",
        "lookback_trading_days", "sample_count", "corr", "beta", "r_squared",
        "residual_vol", "sector_fit_score", "confidence_status", "price_source",
        "price_as_of_date", "universe_source",
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

