"""Resume the post-cutover Trend Alpha recovery with a durable result file."""
from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.research.stock_alpha.run_trend_daily import run_one_date
from morning_conference.sector_rotation2.research.status import SnapshotMode


START, END = '2026-09-18', '2026-10-13'
RECOVERY_STARTED = '2026-10-16 19:45:00'
RESULTS = Path('reports/market-rebuild/trend-backfill-20261016.jsonl')
FINAL = Path('reports/market-rebuild/trend-backfill-20261016-final.json')


def completed_dates() -> set[str]:
    rows = execute_query(
        "SELECT DISTINCT as_of_date FROM sector_rotation_run_log "
        "WHERE as_of_date BETWEEN %s AND %s AND model_version='stock_trend_v2' "
        "AND status='succeeded' AND started_at >= %s",
        (START, END, RECOVERY_STARTED),
    )
    return {str(row['as_of_date']) for row in rows}


def main() -> None:
    dates = [str(row['trade_date']) for row in execute_query(
        'SELECT DISTINCT trade_date FROM trade_stock_daily_qfq '
        'WHERE trade_date BETWEEN %s AND %s ORDER BY trade_date', (START, END),
    )]
    for day in dates:
        if day in completed_dates():
            print(f'SKIP completed {day}', flush=True)
            continue
        print(f'START {day}', flush=True)
        try:
            count = run_one_date(day, 2, SnapshotMode.BACKFILL,
                                 workers=2, force_replace=True)
        except Exception as exc:
            record = {'date': day, 'status': 'failed', 'error': repr(exc)}
            with RESULTS.open('a', encoding='utf-8') as output:
                output.write(json.dumps(record, ensure_ascii=False) + '\n')
            raise
        record = {'date': day, 'status': 'succeeded', 'rows': count}
        with RESULTS.open('a', encoding='utf-8') as output:
            output.write(json.dumps(record, ensure_ascii=False) + '\n')
        print(f'DONE {day}: {count}', flush=True)
    remaining = [day for day in dates if day not in completed_dates()]
    FINAL.write_text(json.dumps({
        'dates': dates,
        'completed_dates': sorted(completed_dates()),
        'remaining_dates': remaining,
        'status': 'complete' if not remaining else 'incomplete',
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    if remaining:
        raise RuntimeError(f'Incomplete trend backfill: {remaining}')


if __name__ == '__main__':
    main()
