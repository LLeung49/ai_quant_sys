$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$outputDir = Join-Path $PSScriptRoot 'daily-update-20261018\derived-backfill'
$pidPath = Join-Path $outputDir 'process.pid'
$resultPath = Join-Path $outputDir 'result.json'

Write-Output '=== Derived backfill process ==='
if (Test-Path $pidPath) {
    $processId = [int](Get-Content -Raw $pidPath)
    Get-Process -Id $processId -ErrorAction SilentlyContinue |
        Select-Object Id, ProcessName, StartTime, CPU
}

Write-Output '=== Per-date log tails ==='
foreach ($date in @('2026-10-14', '2026-10-15')) {
    $logPath = Join-Path $outputDir "$date.log"
    $liveOutputPath = Join-Path $outputDir "$date.stdout.log"
    $liveErrorPath = Join-Path $outputDir "$date.stderr.log"
    Write-Output "--- $date ---"
    if (Test-Path $liveOutputPath) {
        Get-Content -Tail 8 $liveOutputPath
        if (Test-Path $liveErrorPath) { Get-Content -Tail 4 $liveErrorPath }
    } elseif (Test-Path $logPath) {
        Get-Content -Tail 12 $logPath
    } else {
        Write-Output 'not started'
    }
}

Write-Output '=== Final result ==='
if (Test-Path $resultPath) { Get-Content -Raw $resultPath } else { Write-Output 'still running' }

Write-Output '=== Database coverage ==='
Push-Location $repoRoot
try {
    $env:PYTHONPATH = Join-Path $repoRoot 'src'
    python 'reports\market-rebuild\verify_downstream_update_20261018.py'
} finally {
    Pop-Location
}
