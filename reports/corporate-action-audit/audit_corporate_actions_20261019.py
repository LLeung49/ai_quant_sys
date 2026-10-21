"""Read-only corporate-action coverage audit."""

from __future__ import annotations

import json
from pathlib import Path

from data_ingestion.db_config import execute_query


def main() -> None:
    report = {
        "table": execute_query(
            """SELECT data_source, event_status, COUNT(*) AS rows_count,
                      COUNT(DISTINCT stock_code) AS code_count,
                      MIN(ex_date) AS first_date, MAX(ex_date) AS last_date
                 FROM trade_corporate_action
                GROUP BY data_source, event_status
                ORDER BY data_source, event_status"""
        ),
        "etf_universe": execute_query(
            """SELECT COUNT(DISTINCT stock_code) AS code_count
                 FROM trade_stock_status
                WHERE (RIGHT(stock_code, 3) = '.SH' AND LEFT(stock_code, 3) IN
                      ('510','511','512','513','515','516','517','518',
                       '560','561','562','563','588','589'))
                   OR (RIGHT(stock_code, 3) = '.SZ' AND LEFT(stock_code, 3) = '159')"""
        )[0],
        "etf_action_coverage": execute_query(
            """SELECT data_source, COUNT(DISTINCT stock_code) AS code_count,
                      COUNT(*) AS rows_count
                 FROM trade_corporate_action
                WHERE (RIGHT(stock_code, 3) = '.SH' AND LEFT(stock_code, 3) IN
                      ('510','511','512','513','515','516','517','518',
                       '560','561','562','563','588','589'))
                   OR (RIGHT(stock_code, 3) = '.SZ' AND LEFT(stock_code, 3) = '159')
                GROUP BY data_source ORDER BY data_source"""
        ),
    }
    output = Path("reports/corporate-action-audit/corporate-action-coverage-20261019.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, default=str, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, default=str, indent=2))


if __name__ == "__main__":
    main()
