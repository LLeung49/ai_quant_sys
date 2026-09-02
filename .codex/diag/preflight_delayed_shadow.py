"""Read-only preflight for the first delayed-shadow production batch."""

from data_ingestion.db_config import get_connection


def _one(cursor, statement):
    cursor.execute(statement)
    return cursor.fetchone()


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        print("daily_sector", _one(cursor, "SELECT MAX(trade_date), COUNT(*) FROM trade_sector_daily"))
        print(
            "delayed_snapshots",
            _one(
                cursor,
                "SELECT COUNT(*), MIN(as_of_date), MAX(as_of_date) "
                "FROM research_candidate_snapshot WHERE snapshot_mode='delayed_shadow'",
            ),
        )
        print(
            "backfill_roots_latest",
            _one(
                cursor,
                "SELECT MAX(as_of_date), COUNT(*) FROM research_candidate_snapshot "
                "WHERE snapshot_mode='backfill' AND entity_type='sector' "
                "AND strategy_type='sector_opportunity'",
            ),
        )
        print(
            "market_bars_latest",
            _one(cursor, "SELECT MAX(trade_date), COUNT(*) FROM trade_stock_daily"),
        )
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
