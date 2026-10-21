param(
    [string]$AsOfDate,
    [switch]$SkipMarketCollection,
    [switch]$RetryMissingMarket,
    [switch]$IncludeFinancial,
    [switch]$PlanOnly
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$configuredPython = $env:AI_QUANT_PYTHON
$python = if ($configuredPython) {
    $configuredPython
} elseif (Test-Path 'D:\Programs\Python\Python313\python.exe') {
    'D:\Programs\Python\Python313\python.exe'
} else {
    (Get-Command python -ErrorAction Stop).Source
}

$env:PYTHONPATH = Join-Path $repoRoot 'src'
$env:PYTHONUTF8 = '1'
$arguments = @('-m', 'data_ingestion.run_daily_market_pipeline')
if ($AsOfDate) { $arguments += @('--as-of-date', $AsOfDate) }
if ($SkipMarketCollection) { $arguments += '--skip-market-collection' }
if ($RetryMissingMarket) { $arguments += '--retry-missing-market' }
if ($IncludeFinancial) { $arguments += '--include-financial' }
if ($PlanOnly) { $arguments += '--plan' }

Push-Location $repoRoot
try {
    & $python @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "每日任务失败，退出码：$LASTEXITCODE"
    }
} finally {
    Pop-Location
}
