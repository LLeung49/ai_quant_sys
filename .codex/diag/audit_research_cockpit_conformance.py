"""Read-only production conformance audit for the research cockpit."""

from data_ingestion.db_config import get_connection


def _print_rows(cursor, title, sql):
    print(f"[{title}]")
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        _print_rows(cursor, "candidate_projection", """
            SELECT snapshot_mode, strategy_type, COUNT(*) AS candidates,
                   SUM(candidate_status='data_quality_blocked' OR JSON_CONTAINS(COALESCE(risk_flags_json, JSON_ARRAY()), JSON_QUOTE('data_quality_blocked'))) AS quality_blocked,
                   SUM(candidate_score IS NULL AND NOT (candidate_status='data_quality_blocked' OR JSON_CONTAINS(COALESCE(risk_flags_json, JSON_ARRAY()), JSON_QUOTE('data_quality_blocked')))) AS unscored_not_blocked,
                   SUM(data_available_at IS NULL OR run_at IS NULL OR execution_eligible_at IS NULL OR availability_basis IS NULL) AS missing_time_contract,
                   MAX(as_of_date) AS latest_as_of_date
              FROM research_candidate_snapshot
             GROUP BY snapshot_mode, strategy_type
             ORDER BY snapshot_mode, strategy_type
        """)
        _print_rows(cursor, "security_names", """
            SELECT s.snapshot_mode, s.strategy_type, COUNT(*) AS candidates,
                   SUM(COALESCE(NULLIF(status.stock_name, ''), s.entity_code)=s.entity_code) AS code_fallbacks
              FROM research_candidate_snapshot AS s
              LEFT JOIN trade_stock_status AS status ON status.stock_code=s.entity_code
             WHERE s.entity_type IN ('etf', 'stock')
             GROUP BY s.snapshot_mode, s.strategy_type
             ORDER BY s.snapshot_mode, s.strategy_type
        """)
        _print_rows(cursor, "delayed_timing", """
            SELECT strategy_type, COUNT(*) AS candidates,
                   MIN(data_available_at), MAX(data_available_at), MIN(run_at), MAX(run_at),
                   MIN(execution_eligible_at), MAX(execution_eligible_at), GROUP_CONCAT(DISTINCT availability_basis)
              FROM research_candidate_snapshot
             WHERE snapshot_mode='delayed_shadow'
             GROUP BY strategy_type ORDER BY strategy_type
        """)
        _print_rows(cursor, "evaluation_modes", """
            SELECT snapshot_mode, COUNT(*) AS evaluation_rows, MIN(created_at), MAX(created_at)
              FROM sector_rotation_research_evaluation
             GROUP BY snapshot_mode ORDER BY snapshot_mode
        """)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
