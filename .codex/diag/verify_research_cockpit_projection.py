"""Read-only aggregation matching the cockpit candidate projection."""

from data_ingestion.db_config import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT s.strategy_type, COUNT(*) AS candidates,
                      SUM(COALESCE(NULLIF(ss.stock_name, ''), s.entity_code) = s.entity_code) AS code_fallbacks,
                      SUM(s.execution_eligible_at <= '2026-08-31 09:30:00') AS eligible_at_open
                 FROM research_candidate_snapshot AS s
                 LEFT JOIN trade_stock_status AS ss ON ss.stock_code=s.entity_code
                WHERE s.as_of_date='2026-08-28' AND s.sector_level=2
                  AND s.snapshot_mode='delayed_shadow'
                GROUP BY s.strategy_type ORDER BY s.strategy_type"""
        )
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    main()
