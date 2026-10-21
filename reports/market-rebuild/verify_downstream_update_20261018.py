from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query


START, END = "2026-10-14", "2026-10-16"


def query(sql: str):
    return execute_query(sql, (START, END))


result = {
    "window": [START, END],
    "sector_kline": query(
        "SELECT trade_date, sector_level, COUNT(*) AS rows_count "
        "FROM trade_sector_daily WHERE trade_date BETWEEN %s AND %s "
        "GROUP BY trade_date, sector_level ORDER BY trade_date, sector_level"
    ),
    "short_term_snapshots": query(
        "SELECT as_of_date, sector_level, COUNT(*) AS rows_count, "
        "SUM(score_eligible=1) AS eligible_count "
        "FROM sector_rotation_short_term_daily_snapshot "
        "WHERE as_of_date BETWEEN %s AND %s "
        "GROUP BY as_of_date, sector_level ORDER BY as_of_date, sector_level"
    ),
    "medium_term_snapshots": query(
        "SELECT as_of_date, sector_level, COUNT(*) AS rows_count, "
        "SUM(score_eligible=1) AS eligible_count "
        "FROM sector_rotation_sector_daily_snapshot "
        "WHERE as_of_date BETWEEN %s AND %s "
        "GROUP BY as_of_date, sector_level ORDER BY as_of_date, sector_level"
    ),
    "macd_entities": query(
        "SELECT as_of_date, COUNT(*) AS rows_count "
        "FROM sector_rotation_macd_entity_daily "
        "WHERE as_of_date BETWEEN %s AND %s GROUP BY as_of_date ORDER BY as_of_date"
    ),
    "macd_pool": query(
        "SELECT as_of_date, COUNT(*) AS rows_count "
        "FROM sector_rotation_macd_pool "
        "WHERE as_of_date BETWEEN %s AND %s GROUP BY as_of_date ORDER BY as_of_date"
    ),
    "research_snapshots": query(
        "SELECT as_of_date, strategy_type, snapshot_mode, COUNT(*) AS rows_count "
        "FROM research_candidate_snapshot WHERE as_of_date BETWEEN %s AND %s "
        "GROUP BY as_of_date, strategy_type, snapshot_mode "
        "ORDER BY as_of_date, strategy_type, snapshot_mode"
    ),
    "run_log": query(
        "SELECT as_of_date, model_version, status, COUNT(*) AS run_count, "
        "MAX(started_at) AS latest_started_at "
        "FROM sector_rotation_run_log WHERE as_of_date BETWEEN %s AND %s "
        "GROUP BY as_of_date, model_version, status "
        "ORDER BY as_of_date, model_version, status"
    ),
}

output = Path(__file__).with_name("daily-update-20261018") / "downstream-verification.json"
output.write_text(
    json.dumps(result, ensure_ascii=False, default=str, indent=2),
    encoding="utf-8",
)
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
