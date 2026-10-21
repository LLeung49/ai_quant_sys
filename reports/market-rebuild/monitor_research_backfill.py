"""Read-only progress check for the post-cutover research recovery."""
from __future__ import annotations

import json

from data_ingestion.db_config import execute_query


START, END = '2026-09-18', '2026-10-13'
dates = [str(row['trade_date']) for row in execute_query(
    'SELECT DISTINCT trade_date FROM trade_stock_daily_qfq '
    'WHERE trade_date BETWEEN %s AND %s ORDER BY trade_date', (START, END),
)]
rows = execute_query(
    "SELECT as_of_date,strategy_type,snapshot_mode,COUNT(*) AS n "
    "FROM research_candidate_snapshot WHERE as_of_date BETWEEN %s AND %s "
    "AND sector_level=2 AND snapshot_mode='backfill' "
    "AND strategy_type IN ('sector_opportunity','etf_core','stock_trend') "
    "GROUP BY as_of_date,strategy_type,snapshot_mode ORDER BY as_of_date,strategy_type",
    (START, END),
)
run_rows = execute_query(
    "SELECT as_of_date,model_version,status,eligible_sector_count,started_at "
    "FROM sector_rotation_run_log WHERE as_of_date BETWEEN %s AND %s "
    "AND model_version='stock_trend_v2' ORDER BY started_at",
    (START, END),
)
by_date: dict[str, dict[str, int]] = {day: {} for day in dates}
for row in rows:
    by_date[str(row['as_of_date'])][row['strategy_type']] = row['n']
result = {
    'expected_dates': dates,
    'snapshot_counts': by_date,
    'trend_runs': run_rows,
    'macd_result_dates': [
        str(row['as_of_date']) for row in execute_query(
            'SELECT DISTINCT as_of_date FROM sector_rotation_macd_entity_daily '
            'WHERE as_of_date BETWEEN %s AND %s ORDER BY as_of_date', (START, END),
        )
    ],
}
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
