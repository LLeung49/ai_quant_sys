"""One-time additive migration with a concise, auditable before/after report."""

from data_ingestion.db_config import get_connection


REQUIRED_COLUMNS = {
    "data_available_at": "DATETIME NULL",
    "run_at": "DATETIME NULL",
    "execution_eligible_at": "DATETIME NULL",
    "availability_basis": "VARCHAR(32) NULL",
}
INDEX_NAME = "idx_research_snapshot_execution"


def _state(cursor):
    cursor.execute("SELECT DATABASE(), COUNT(*) FROM research_candidate_snapshot")
    database, row_count = cursor.fetchone()
    cursor.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_schema=DATABASE() AND table_name='research_candidate_snapshot'"
    )
    columns = {row[0] for row in cursor.fetchall()}
    cursor.execute(
        "SELECT index_name FROM information_schema.statistics "
        "WHERE table_schema=DATABASE() AND table_name='research_candidate_snapshot'"
    )
    indexes = {row[0] for row in cursor.fetchall()}
    return database, row_count, sorted(columns & REQUIRED_COLUMNS.keys()), INDEX_NAME in indexes


def main():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        print("before", _state(cursor))
        cursor.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema=DATABASE() AND table_name='research_candidate_snapshot'"
        )
        existing_columns = {row[0] for row in cursor.fetchall()}
        for name, definition in REQUIRED_COLUMNS.items():
            if name not in existing_columns:
                cursor.execute(
                    f"ALTER TABLE research_candidate_snapshot ADD COLUMN {name} {definition}"
                )
        cursor.execute(
            "SELECT 1 FROM information_schema.statistics WHERE table_schema=DATABASE() "
            "AND table_name='research_candidate_snapshot' "
            "AND index_name='idx_research_snapshot_execution'"
        )
        if cursor.fetchone() is None:
            cursor.execute(
                "ALTER TABLE research_candidate_snapshot ADD KEY "
                "idx_research_snapshot_execution (snapshot_mode, execution_eligible_at)"
            )
        connection.commit()
        print("after", _state(cursor))
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
