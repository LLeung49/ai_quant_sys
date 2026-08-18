from datetime import date
from decimal import Decimal

from morning_conference.sector_rotation2.research.etf_core.service import build_etf_candidate
from morning_conference.sector_rotation2.research.snapshot import InMemorySnapshotStore, persist_live_shadow_snapshot
from morning_conference.sector_rotation2.research.status import ResearchStatus, SnapshotMode


def test_ready_etf_candidate_is_shadow_and_manual_only() -> None:
    snapshot = build_etf_candidate(
        as_of_date=date(2026, 8, 17), sector_level=1, sector_name="半导体", etf_code="512480.SH",
        sector_allowed=True, liquid=True, macd_evidence={"macd_triggered": True, "gc_offset": 1},
        extended=False, run_id="run-1",
    )
    assert snapshot.candidate_status == "ready"
    assert snapshot.research_status is ResearchStatus.SHADOW
    assert snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW


def test_etf_candidate_binds_mapping_metadata_to_features_and_config_identity() -> None:
    metadata = {
        "mapping_version": "exposure_v1",
        "config_hash": "mapping-config",
        "rank_no": 1,
        "source_as_of_date": "2026-08-17",
        "membership_as_of_date": "2026-08-17",
        "constituent_as_of_date": "2026-08-17",
    }

    snapshot = build_etf_candidate(
        as_of_date=date(2026, 8, 17), sector_level=1, sector_name="半导体", etf_code="512480.SH",
        sector_allowed=True, liquid=True, macd_evidence={"macd_triggered": True}, extended=False,
        run_id="run-1", mapping_metadata=metadata,
    )

    assert snapshot.feature_json["mapping"] == {
        **metadata, "sector_level": 1, "sector_name": "半导体", "etf_code": "512480.SH",
    }
    assert snapshot.config_hash != build_etf_candidate(
        as_of_date=date(2026, 8, 17), sector_level=1, sector_name="半导体", etf_code="512480.SH",
        sector_allowed=True, liquid=True, macd_evidence={"macd_triggered": True}, extended=False,
        run_id="run-1", mapping_metadata={**metadata, "config_hash": "other"},
    ).config_hash


def test_mapping_metadata_is_json_safe_and_effective_to_is_not_in_candidate_identity() -> None:
    metadata = {
        "source_as_of_date": date(2026, 8, 17), "membership_as_of_date": date(2026, 8, 17),
        "constituent_as_of_date": date(2026, 8, 17), "exposure_weight": Decimal("0.80"),
        "coverage_ratio": Decimal("0.90"), "mapping_version": "exposure_v1", "config_hash": "map_cfg",
        "rank_no": 1, "source_provider": "provider_x", "effective_to": date(2026, 8, 31),
    }
    common = dict(
        as_of_date=date(2026, 8, 17), sector_level=2, sector_name="半导体", etf_code="510001.SH",
        sector_allowed=True, liquid=True, macd_evidence={"macd_triggered": True}, extended=False, run_id="run-1",
    )

    snapshot = build_etf_candidate(**common, mapping_metadata=metadata)
    changed_effective_date = build_etf_candidate(
        **common, mapping_metadata={**metadata, "effective_to": date(2026, 9, 1)},
    )

    assert snapshot.feature_json["mapping"]["source_as_of_date"] == "2026-08-17"
    assert snapshot.feature_json["mapping"]["exposure_weight"] == "0.80"
    assert "effective_to" not in snapshot.feature_json["mapping"]
    assert snapshot.config_hash == changed_effective_date.config_hash
    store = InMemorySnapshotStore()
    persist_live_shadow_snapshot(store, snapshot)
    persist_live_shadow_snapshot(store, changed_effective_date)
