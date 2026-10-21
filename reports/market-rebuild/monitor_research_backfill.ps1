$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
Push-Location $projectRoot
try {
    $env:PYTHONPATH = 'src'
    Write-Output '=== Trend recovery process ==='
    $pidFile = 'reports/market-rebuild/trend-backfill-20261016.pid'
    if (Test-Path $pidFile) {
        Get-Process -Id (Get-Content $pidFile) -ErrorAction SilentlyContinue |
            Select-Object Id, CPU, StartTime
    }
    Write-Output '=== Trend recovery log ==='
    Get-Content 'reports/market-rebuild/trend-backfill-20261016.log' -Tail 12 -ErrorAction SilentlyContinue
    Write-Output '=== Trend recovery errors ==='
    Get-Content 'reports/market-rebuild/trend-backfill-20261016.err.log' -Tail 12 -ErrorAction SilentlyContinue
    Write-Output '=== Final result ==='
    $finalFile = 'reports/market-rebuild/trend-backfill-20261016-final.json'
    if (Test-Path $finalFile) { Get-Content $finalFile } else { Write-Output 'still running: final result JSON does not exist yet' }
    Write-Output '=== Database coverage ==='
    python reports/market-rebuild/monitor_research_backfill.py
} finally {
    Pop-Location
}
