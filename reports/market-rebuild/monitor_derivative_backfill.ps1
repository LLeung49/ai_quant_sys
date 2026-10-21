$ErrorActionPreference = 'Stop'
$repo = 'D:\aiQuant\ai_quant_sys\.worktrees\akshare-qmt-recovery'
$logDir = Join-Path $repo 'reports\market-rebuild\short-term-level1-logs'
$result = Join-Path $repo 'reports\market-rebuild\short-term-level1-backfill-20261016.json'

Write-Host '=== Active recovery Python processes ==='
$processes = Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" |
    Where-Object {
        $_.CommandLine -like '*parallel_short_term_level1_backfill.py*' -or
        $_.CommandLine -like '*sector_rotation2.short_term.run_daily*'
    } |
    Select-Object ProcessId, CreationDate, CommandLine
if ($processes) { $processes | Format-Table -AutoSize } else { Write-Host 'none' }

Write-Host '=== Completed per-date logs ==='
if (Test-Path -LiteralPath $logDir) {
    Get-ChildItem -LiteralPath $logDir -Filter '*.log' |
        Sort-Object Name |
        Select-Object Name, Length, LastWriteTime |
        Format-Table -AutoSize
} else {
    Write-Host 'none'
}

Write-Host '=== Final result ==='
if (Test-Path -LiteralPath $result) {
    Get-Content -LiteralPath $result -Raw -Encoding UTF8
} else {
    Write-Host 'still running: final result JSON does not exist yet'
}

Write-Host '=== Database coverage ==='
Push-Location $repo
try {
    $env:PYTHONPATH = 'src'
    & 'D:\Programs\Python\Python313\python.exe' `
        'reports\market-rebuild\audit_downstream_date_coverage.py'
} finally {
    Pop-Location
}
