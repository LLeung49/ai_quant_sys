import json

from data_ingestion.db_config import execute_query


result = {
    "short_term": execute_query(
        """
        SELECT as_of_date, sector_level, model_version, COUNT(*) AS row_count
        FROM sector_rotation_short_term_daily_snapshot
        WHERE as_of_date BETWEEN '2026-09-18' AND '2026-10-13'
        GROUP BY as_of_date, sector_level, model_version
        ORDER BY as_of_date, sector_level, model_version
        """
    ),
    "medium_term": execute_query(
        """
        SELECT as_of_date, sector_level, model_version, COUNT(*) AS row_count
        FROM sector_rotation_sector_daily_snapshot
        WHERE as_of_date BETWEEN '2026-09-18' AND '2026-10-13'
        GROUP BY as_of_date, sector_level, model_version
        ORDER BY as_of_date, sector_level, model_version
        """
    ),
    "run_log": execute_query(
        """
        SELECT as_of_date, sector_level, model_version, status, COUNT(*) AS row_count,
               MAX(created_at) AS latest_created_at
        FROM sector_rotation_run_log
        WHERE as_of_date BETWEEN '2026-09-18' AND '2026-10-13'
        GROUP BY as_of_date, sector_level, model_version, status
        ORDER BY as_of_date, sector_level, model_version, status
        """
    ),
}
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
