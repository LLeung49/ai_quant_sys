$reportDir = Join-Path $PSScriptRoot 'daily-update-20261019'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$python = if ($env:AI_QUANT_PYTHON) { $env:AI_QUANT_PYTHON } elseif (Test-Path 'D:\Programs\Python\Python313\python.exe') { 'D:\Programs\Python\Python313\python.exe' } else { (Get-Command python -ErrorAction Stop).Source }

Write-Output '=== Stock-only collection ==='
$stockPidPath = Join-Path $reportDir 'stock.pid'
if (Test-Path $stockPidPath) {
    $stockPid = [int](Get-Content -LiteralPath $stockPidPath -Raw)
    $stockProcess = Get-Process -Id $stockPid -ErrorAction SilentlyContinue
    if ($stockProcess) { Write-Output "RUNNING pid=$stockPid" } else { Write-Output "STOPPED pid=$stockPid" }
}
$stockLog = Join-Path $reportDir 'stock-stdout.log'
if (Test-Path $stockLog) { Get-Content -LiteralPath $stockLog -Tail 8 -Encoding Default }
$stockError = Join-Path $reportDir 'stock-stderr.log'
if (Test-Path $stockError) { Get-Content -LiteralPath $stockError -Tail 5 -Encoding Default }
$stockResult = Join-Path $reportDir 'stock-result.json'
$stockSummary = $null
if (Test-Path $stockResult) {
    $stockSummary = Get-Content -LiteralPath $stockResult -Raw -Encoding UTF8 | ConvertFrom-Json
    Write-Output "RESULT succeeded=$($stockSummary.succeeded) failed=$($stockSummary.failed)"
} else { Write-Output 'RESULT_PENDING' }

Write-Output '=== ETF collection ==='
$etfPidPath = Join-Path $reportDir 'etf.pid'
if (Test-Path $etfPidPath) {
    $etfPid = [int](Get-Content -LiteralPath $etfPidPath -Raw)
    $etfProcess = Get-Process -Id $etfPid -ErrorAction SilentlyContinue
    if ($etfProcess) { Write-Output "RUNNING pid=$etfPid" } else { Write-Output "STOPPED pid=$etfPid" }
}
$etfLog = Join-Path $reportDir 'etf-stdout.log'
if (Test-Path $etfLog) { Get-Content -LiteralPath $etfLog -Tail 8 -Encoding UTF8 }
$etfError = Join-Path $reportDir 'etf-stderr.log'
if (Test-Path $etfError) { Get-Content -LiteralPath $etfError -Tail 5 -Encoding UTF8 }
$etfResult = Join-Path $reportDir 'etf-result.json'
$etfSummary = $null
if (Test-Path $etfResult) {
    $etfSummary = Get-Content -LiteralPath $etfResult -Raw -Encoding UTF8 | ConvertFrom-Json
    Write-Output "RESULT succeeded=$($etfSummary.succeeded) failed=$($etfSummary.failed)"
} else { Write-Output 'RESULT_PENDING' }

Write-Output '=== Collection status ==='
if (!$stockSummary -or !$etfSummary) {
    Write-Output 'NOT COMPLETE: collection final result pending'
} elseif ($stockSummary.failed -or $etfSummary.failed) {
    Write-Output 'NEEDS REPAIR: one or more codes failed after retry'
} else {
    Write-Output 'COLLECTION COMPLETE: see downstream and acceptance status below'
}

Write-Output '=== Downstream task ==='
$derivedPidPath = Join-Path $reportDir 'derived.pid'
if (Test-Path $derivedPidPath) {
    $derivedPid = [int](Get-Content -LiteralPath $derivedPidPath -Raw)
    $derivedProcess = Get-Process -Id $derivedPid -ErrorAction SilentlyContinue
    if ($derivedProcess) { Write-Output "RUNNING pid=$derivedPid" } else { Write-Output "STOPPED pid=$derivedPid" }
} else { Write-Output 'NOT STARTED' }
$derivedLog = Join-Path $reportDir 'derived-stdout.log'
if (Test-Path $derivedLog) { Get-Content -LiteralPath $derivedLog -Tail 8 -Encoding UTF8 }
$derivedError = Join-Path $reportDir 'derived-stderr.log'
if (Test-Path $derivedError) { Get-Content -LiteralPath $derivedError -Tail 8 -Encoding UTF8 }

Write-Output '=== Acceptance status ==='
$acceptancePath = Join-Path $reportDir 'acceptance.json'
if (Test-Path $acceptancePath) {
    $acceptance = Get-Content -LiteralPath $acceptancePath -Raw -Encoding UTF8 | ConvertFrom-Json
    $failedChecks = @($acceptance.checks.PSObject.Properties | Where-Object { $_.Value -ne $true } | Select-Object -ExpandProperty Name)
    if ($failedChecks.Count -eq 0) { Write-Output 'PASSED: market, downstream tables, and Web API checks' }
    else { Write-Output "FAILED: $($failedChecks -join ', ')" }
    Write-Output "TREND_QUALITY_BLOCKED=$($acceptance.api.research_summary.summary.data_quality_blocked) (known deferred issue)"
} else { Write-Output 'PENDING: acceptance.json does not exist yet' }

Write-Output '=== Database coverage ==='
$env:PYTHONPATH = Join-Path $repoRoot 'src'
$env:PYTHONUTF8 = '1'
Push-Location $repoRoot
try {
    & $python -c "from data_ingestion.db_config import execute_query; import json; tables=['trade_stock_daily_raw','trade_stock_daily_qfq','trade_stock_daily_bfq']; result={table: execute_query('SELECT COUNT(*) AS rows_count, SUM(open_price<=0 OR high_price<=0 OR low_price<=0 OR close_price<=0) AS invalid_ohlc FROM '+table+' WHERE trade_date=%s', ('2026-10-19',))[0] for table in tables}; print(json.dumps(result, ensure_ascii=False, default=str, indent=2))"
} finally { Pop-Location }
