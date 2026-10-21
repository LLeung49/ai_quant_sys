param(
    [string]$StartDate = '2026-09-18',
    [string]$EndDate = '2026-10-16',
    [string]$CompletedAfter = '1900-01-01 00:00:00'
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$python = if ($env:AI_QUANT_PYTHON) { $env:AI_QUANT_PYTHON } else { (Get-Command python -ErrorAction Stop).Source }
$env:PYTHONPATH = Join-Path $repoRoot 'src'
$env:PYTHONUTF8 = '1'
$env:REPAIR_START_DATE = $StartDate
$env:REPAIR_END_DATE = $EndDate
$env:REPAIR_COMPLETED_AFTER = $CompletedAfter

Push-Location $repoRoot
try {
@'
import json
import os
from data_ingestion.db_config import execute_query

window = (os.environ['REPAIR_START_DATE'], os.environ['REPAIR_END_DATE'])
expected = execute_query('''
    SELECT DISTINCT as_of_date FROM research_candidate_snapshot
    WHERE as_of_date BETWEEN %s AND %s AND sector_level=2
      AND strategy_type='sector_opportunity' AND snapshot_mode='backfill'
    ORDER BY as_of_date
''', window)
coverage = execute_query('''
    SELECT s.as_of_date, COUNT(*) AS rows_count,
           COUNT(DISTINCT s.entity_code) AS stock_count,
           SUM(JSON_CONTAINS(s.risk_flags_json, '"missing_market_cap"')) AS missing_market_cap,
           MAX(CASE WHEN l.status='succeeded' AND l.started_at >= %s THEN 1 ELSE 0 END) AS has_succeeded_run
    FROM research_candidate_snapshot s
    LEFT JOIN sector_rotation_run_log l ON l.run_id=s.run_id
    WHERE s.as_of_date BETWEEN %s AND %s AND s.sector_level=2
      AND s.strategy_type='stock_repair' AND s.snapshot_mode='backfill'
    GROUP BY s.as_of_date ORDER BY s.as_of_date
''', (os.environ['REPAIR_COMPLETED_AFTER'], *window))
completed = {str(row['as_of_date']) for row in coverage if row['has_succeeded_run']}
result = {
    'expected_dates': [str(row['as_of_date']) for row in expected],
    'completed_dates': sorted(completed),
    'remaining_dates': [str(row['as_of_date']) for row in expected if str(row['as_of_date']) not in completed],
    'coverage': coverage,
}
print(json.dumps(result, ensure_ascii=False, default=str, indent=2))
'@ | & $python -
    if ($LASTEXITCODE -ne 0) { throw "Repair Alpha 监控查询失败：$LASTEXITCODE" }
} finally {
    Pop-Location
}
