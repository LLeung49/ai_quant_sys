"""Read-only acceptance checks for materialized evaluation headers/metrics."""

from data_ingestion_qmt.db_config import execute_query


def verify() -> dict[str, object]:
    calendar_2024 = execute_query(
        "SELECT COUNT(DISTINCT trade_date) AS n, MIN(trade_date) AS min_date, MAX(trade_date) AS max_date "
        "FROM trade_sector_daily WHERE sector_level=2 AND trade_date BETWEEN %s AND %s",
        ("2024-01-01", "2026-08-20"),
    )[0]
    headers = execute_query(
        "SELECT snapshot_mode, COUNT(*) AS group_count, SUM(candidate_count) AS candidates, "
        "SUM(return_complete_count) AS complete_returns FROM sector_rotation_research_evaluation "
        "GROUP BY snapshot_mode ORDER BY snapshot_mode"
    )
    metrics = execute_query(
        "SELECT e.snapshot_mode, COUNT(m.id) AS metric_rows, "
        "SUM(CASE WHEN m.metric_name='mean_return' AND m.sample_count>0 THEN 1 ELSE 0 END) AS nonempty_mean_return "
        "FROM sector_rotation_research_evaluation e JOIN sector_rotation_research_evaluation_metric m "
        "ON m.evaluation_id=e.id GROUP BY e.snapshot_mode ORDER BY e.snapshot_mode"
    )
    confidence = execute_query(
        "SELECT e.snapshot_mode, COUNT(*) AS mean_return_rows, SUM(m.ci_low IS NOT NULL) AS ci_rows "
        "FROM sector_rotation_research_evaluation e JOIN sector_rotation_research_evaluation_metric m "
        "ON m.evaluation_id=e.id WHERE m.metric_name='mean_return' GROUP BY e.snapshot_mode ORDER BY e.snapshot_mode"
    )
    mode_collisions = execute_query(
        "SELECT COUNT(*) AS n FROM (SELECT signal_family,horizon,label_type,event_sampling_mode,sample_scope,snapshot_mode,model_version,config_hash,COUNT(*) c "
        "FROM sector_rotation_research_evaluation GROUP BY signal_family,horizon,label_type,event_sampling_mode,sample_scope,snapshot_mode,model_version,config_hash HAVING c>1) x"
    )[0]["n"]
    live_counts = execute_query(
        "SELECT SUM(return_complete_count) AS complete_returns, SUM(candidate_count) AS candidates "
        "FROM sector_rotation_research_evaluation WHERE snapshot_mode='live_shadow'"
    )[0]
    evaluation_mode_mismatches = execute_query(
        "SELECT COUNT(*) AS n FROM sector_rotation_research_forward_label f "
        "JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id "
        "WHERE f.snapshot_mode<>s.snapshot_mode"
    )[0]["n"]
    delayed_missing_metadata = execute_query(
        "SELECT COUNT(*) AS n FROM research_candidate_snapshot "
        "WHERE snapshot_mode='delayed_shadow' AND (data_available_at IS NULL OR run_at IS NULL "
        "OR execution_eligible_at IS NULL OR availability_basis IS NULL)"
    )[0]["n"]
    return {
        "calendar_2024_to_latest": calendar_2024, "required_oos_dates": 756,
        "headers": headers, "metrics": metrics, "confidence": confidence,
        "mode_collision_groups": mode_collisions, "live_shadow": live_counts,
        "evaluation_mode_mismatch_count": evaluation_mode_mismatches,
        "delayed_missing_metadata_count": delayed_missing_metadata,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(verify(), ensure_ascii=False, default=str, indent=2))

