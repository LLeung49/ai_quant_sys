"""Resume the post-cutover MACD recovery one trading day at a time."""
from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query
from morning_conference.sector_rotation2.run_macd_daily import run


START = '2026-09-18'
END = '2026-10-13'
RESULTS = Path('reports/market-rebuild/macd-backfill-20261016.jsonl')


def main() -> None:
    dates = [str(row['trade_date']) for row in execute_query(
        'SELECT DISTINCT trade_date FROM trade_stock_daily_qfq '
        'WHERE trade_date BETWEEN %s AND %s ORDER BY trade_date',
        (START, END),
    )]
    completed = set()
    if RESULTS.exists():
        for line in RESULTS.read_text(encoding='utf-8').splitlines():
            result = json.loads(line)
            if result.get('status') == 'succeeded':
                completed.add(result['as_of_date'])
    for date in dates:
        if date in completed:
            continue
        print(f'START {date}', flush=True)
        try:
            result = run(date, sync_names=False)
        except Exception as exc:
            record = {'as_of_date': date, 'status': 'failed', 'error': repr(exc)}
            with RESULTS.open('a', encoding='utf-8') as output:
                output.write(json.dumps(record, ensure_ascii=False) + '\n')
            raise
        record = {'as_of_date': date, 'status': 'succeeded', **result}
        with RESULTS.open('a', encoding='utf-8') as output:
            output.write(json.dumps(record, ensure_ascii=False) + '\n')
        print(f'DONE {date}: {result}', flush=True)


if __name__ == '__main__':
    main()
