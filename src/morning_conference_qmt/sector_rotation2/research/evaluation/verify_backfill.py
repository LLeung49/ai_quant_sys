"""Read-only database acceptance checks for real forward-label backfill."""

from data_ingestion_qmt.db_config import execute_query


def verify() -> dict[str, object]:
    distributions = execute_query(
        "SELECT snapshot_mode, return_status, label_type, COUNT(*) AS n "
        "FROM sector_rotation_research_forward_label "
        "GROUP BY snapshot_mode, return_status, label_type ORDER BY snapshot_mode, return_status, label_type"
    )
    modes = execute_query(
        "SELECT snapshot_mode, COUNT(*) AS n, COUNT(DISTINCT source_snapshot_id) AS snapshots, "
        "SUM(is_complete) AS complete_count FROM sector_rotation_research_forward_label GROUP BY snapshot_mode"
    )
    mode_mismatches = execute_query(
        "SELECT COUNT(*) AS n FROM sector_rotation_research_forward_label f "
        "JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id "
        "WHERE f.snapshot_mode<>s.snapshot_mode"
    )[0]["n"]
    duplicate_keys = execute_query(
        "SELECT COUNT(*) AS n FROM (SELECT source_snapshot_id, snapshot_mode, benchmark_type, benchmark_code, "
        "horizon, label_type, price_basis, label_model_version, label_config_hash, COUNT(*) AS c "
        "FROM sector_rotation_research_forward_label GROUP BY source_snapshot_id, snapshot_mode, benchmark_type, "
        "benchmark_code, horizon, label_type, price_basis, label_model_version, label_config_hash HAVING c>1) x"
    )[0]["n"]
    snapshot_rows = execute_query("SELECT COUNT(*) AS n FROM research_candidate_snapshot")[0]["n"]
    availability_null_rows = execute_query(
        "SELECT snapshot_mode, COUNT(*) AS n FROM research_candidate_snapshot "
        "WHERE data_available_at IS NULL OR run_at IS NULL OR execution_eligible_at IS NULL "
        "OR availability_basis IS NULL GROUP BY snapshot_mode ORDER BY snapshot_mode"
    )
    delayed_missing_metadata = execute_query(
        "SELECT COUNT(*) AS n FROM research_candidate_snapshot "
        "WHERE snapshot_mode='delayed_shadow' AND (data_available_at IS NULL OR run_at IS NULL "
        "OR execution_eligible_at IS NULL OR availability_basis IS NULL)"
    )[0]["n"]
    return {
        "distributions": distributions, "modes": modes,
        "mode_mismatch_count": mode_mismatches, "duplicate_key_group_count": duplicate_keys,
        "candidate_snapshot_row_count": snapshot_rows,
        "availability_null_counts": {row["snapshot_mode"]: row["n"] for row in availability_null_rows},
        "delayed_missing_metadata_count": delayed_missing_metadata,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(verify(), ensure_ascii=False, default=str, indent=2))

