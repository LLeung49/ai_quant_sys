from morning_conference.sector_rotation2.research.orchestrator.store import RESEARCH_SNAPSHOT_DDL


def test_research_snapshot_schema_keeps_live_identity_immutable() -> None:
    normalized = " ".join(RESEARCH_SNAPSHOT_DDL.lower().split())
    assert "create table if not exists research_candidate_snapshot" in normalized
    assert "snapshot_mode varchar(16) not null" in normalized
    assert "unique key uk_research_snapshot_identity" in normalized
    assert "as_of_date, entity_type, entity_code, strategy_type, model_version, config_hash, snapshot_mode" in normalized
    assert "on duplicate key update" not in normalized
