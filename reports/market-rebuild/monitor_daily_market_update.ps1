$reportDir = Join-Path $PSScriptRoot 'daily-update-20261018'
$pidPath = Join-Path $reportDir 'run.pid'
$stdoutPath = Join-Path $reportDir 'stdout.log'
$stderrPath = Join-Path $reportDir 'stderr.log'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$python = if ($env:AI_QUANT_PYTHON) {
    $env:AI_QUANT_PYTHON
} elseif (Test-Path 'D:\Programs\Python\Python313\python.exe') {
    'D:\Programs\Python\Python313\python.exe'
} else {
    (Get-Command python -ErrorAction Stop).Source
}

Write-Output '=== Daily update process ==='
if (Test-Path $pidPath) {
    $processId = [int](Get-Content -Raw $pidPath)
    $process = Get-Process -Id $processId -ErrorAction SilentlyContinue
    if ($process) {
        $process | Select-Object Id, ProcessName, StartTime, CPU
    } else {
        Write-Output "not running (last pid: $processId)"
    }
} else {
    Write-Output 'pid file does not exist'
}

Write-Output '=== Standard output tail ==='
if (Test-Path $stdoutPath) { Get-Content -Tail 20 $stdoutPath }
Write-Output '=== Error output tail ==='
if (Test-Path $stderrPath) { Get-Content -Tail 20 $stderrPath }

Write-Output '=== Database coverage ==='
$env:PYTHONPATH = Join-Path $repoRoot 'src'
$env:PYTHONUTF8 = '1'
Push-Location $repoRoot
try {
    & $python -c "from data_ingestion.db_config import execute_query; import json; tables=['trade_stock_daily_raw','trade_stock_daily_qfq','trade_stock_daily_bfq']; out={t:execute_query('SELECT trade_date, COUNT(*) AS rows_count, SUM(open_price=0 OR high_price=0 OR low_price=0 OR close_price=0) AS zero_rows FROM '+t+' WHERE trade_date BETWEEN %s AND %s GROUP BY trade_date ORDER BY trade_date', ('2026-10-14','2026-10-16')) for t in tables}; print(json.dumps(out, ensure_ascii=False, default=str, indent=2))"
} finally {
    Pop-Location
}
