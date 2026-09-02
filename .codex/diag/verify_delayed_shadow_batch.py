"""Read-only verification of one delayed-shadow production batch."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT entity_type, strategy_type, COUNT(*) AS n, "
            "SUM(data_available_at IS NULL OR run_at IS NULL OR execution_eligible_at IS NULL "
            "OR availability_basis IS NULL) AS missing_timing, "
            "MIN(data_available_at), MAX(data_available_at), "
            "MIN(run_at), MAX(run_at), "
            "MIN(execution_eligible_at), MAX(execution_eligible_at), "
            "GROUP_CONCAT(DISTINCT availability_basis) "
            "FROM research_candidate_snapshot "
            "WHERE as_of_date='2026-08-28' AND snapshot_mode='delayed_shadow' "
            "GROUP BY entity_type, strategy_type ORDER BY entity_type, strategy_type"
        )
        for row in cursor.fetchall():
            print(row)
        cursor.execute(
            "SELECT COUNT(*) FROM research_candidate_snapshot "
            "WHERE as_of_date='2026-08-28' AND snapshot_mode <> 'delayed_shadow' "
            "AND (entity_type, strategy_type) IN ("
            "('sector','sector_opportunity'), ('etf','etf_candidate'), "
            "('stock','trend_candidate'), ('stock','repair_candidate'))"
        )
        print("other_mode_same_day", cursor.fetchone()[0])
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
