import json
from pathlib import Path

from data_ingestion.db_config import execute_query


columns = execute_query(
    """
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema=DATABASE()
      AND (table_name LIKE 'sector_rotation%%'
        OR table_name='research_candidate_snapshot')
      AND column_name IN ('trade_date', 'as_of_date', 'run_date', 'snapshot_date')
    ORDER BY table_name, ordinal_position
    """
)
coverage = []
for item in columns:
    table = item.get("table_name") or item.get("TABLE_NAME")
    column = item.get("column_name") or item.get("COLUMN_NAME")
    row = execute_query(
        f"""
        SELECT COUNT(*) AS total_rows, MIN({column}) AS first_date,
               MAX({column}) AS last_date,
               SUM({column}>='2026-09-18' AND {column}<='2026-10-13') AS recovery_rows,
               COUNT(DISTINCT CASE WHEN {column}>='2026-09-18' AND {column}<='2026-10-13'
                                   THEN {column} END) AS recovery_dates
        FROM {table}
        """
    )[0]
    coverage.append({"table": table, "date_column": column, **row})

report = {"window": ["2026-09-18", "2026-10-13"], "coverage": coverage}
Path("reports/market-rebuild/downstream-date-coverage-20261016.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
