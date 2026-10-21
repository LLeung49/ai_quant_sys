"""Isolate obsolete Repair Alpha shadow observations and aggregate evaluations."""

import json

from data_ingestion.db_config import get_connection
from .archive_repair_dependencies import archived_bounds
from .rebuild_repair_history import DEFAULT_MANIFEST, verify_backup


def isolate() -> dict:
    verify_backup(DEFAULT_MANIFEST)
    bounds = archived_bounds()
    connection = get_connection()
    cursor = connection.cursor()
    counts = {}
    try:
        cursor.execute(
            "UPDATE research_candidate_snapshot SET validation_status='rejected', "
            "research_status='rejected' WHERE strategy_type='stock_repair' "
            "AND snapshot_mode IN ('live_shadow','delayed_shadow') "
            "AND as_of_date < '2026-09-19' AND validation_status<>'rejected'"
        )
        counts["rejected_shadow_snapshots"] = cursor.rowcount
        cursor.execute(
            "DELETE f FROM sector_rotation_research_forward_label f "
            "JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id "
            "WHERE s.strategy_type='stock_repair' AND s.validation_status='rejected' "
            "AND f.id<=%s AND f.updated_at<=%s",
            (bounds["forward_labels"]["max_id"], bounds["forward_labels"]["max_updated"]),
        )
        counts["archived_shadow_labels_removed"] = cursor.rowcount
        cursor.execute(
            "DELETE m FROM sector_rotation_research_evaluation_metric m "
            "JOIN sector_rotation_research_evaluation e ON e.id=m.evaluation_id "
            "WHERE e.signal_family='stock_repair' AND e.snapshot_mode IN "
            "('live_shadow','delayed_shadow') AND e.id<=%s AND m.id<=%s",
            (bounds["evaluations"]["max_id"], bounds["evaluation_metrics"]["max_id"]),
        )
        counts["archived_metrics_removed"] = cursor.rowcount
        cursor.execute(
            "DELETE FROM sector_rotation_research_evaluation WHERE signal_family='stock_repair' "
            "AND snapshot_mode IN ('live_shadow','delayed_shadow') AND id<=%s",
            (bounds["evaluations"]["max_id"],),
        )
        counts["archived_evaluations_removed"] = cursor.rowcount
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
    return counts


if __name__ == "__main__":
    print(json.dumps(isolate(), indent=2))
