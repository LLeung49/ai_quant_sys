$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$outputDir = Join-Path $PSScriptRoot 'daily-update-20261018\derived-backfill'
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
$dates = @('2026-10-14', '2026-10-15')
$results = @()

Push-Location $repoRoot
try {
    foreach ($date in $dates) {
        $logPath = Join-Path $outputDir "$date.log"
        $stdoutPath = Join-Path $outputDir "$date.stdout.log"
        $stderrPath = Join-Path $outputDir "$date.stderr.log"
        try {
            $dateProcess = Start-Process `
                -FilePath 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' `
                -ArgumentList @(
                    '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                    (Join-Path $repoRoot 'scripts\run_daily_once.ps1'),
                    '-AsOfDate', $date, '-SkipMarketCollection'
                ) `
                -RedirectStandardOutput $stdoutPath `
                -RedirectStandardError $stderrPath `
                -WindowStyle Hidden -Wait -PassThru
            Get-Content $stdoutPath -ErrorAction SilentlyContinue |
                Set-Content -Path $logPath -Encoding utf8
            Get-Content $stderrPath -ErrorAction SilentlyContinue |
                Add-Content -Path $logPath -Encoding utf8
            if ($dateProcess.ExitCode -ne 0) {
                throw "daily pipeline exited with code $($dateProcess.ExitCode)"
            }
            $results += [ordered]@{ date = $date; status = 'succeeded'; log = $logPath }
        } catch {
            $_ | Out-String | Add-Content -Path $logPath -Encoding utf8
            $results += [ordered]@{ date = $date; status = 'failed'; log = $logPath; error = $_.Exception.Message }
            throw
        } finally {
            Remove-Item -LiteralPath $stdoutPath, $stderrPath -Force -ErrorAction SilentlyContinue
        }
    }
} finally {
    $final = [ordered]@{
        completed_at = (Get-Date).ToString('s')
        results = $results
        status = if ($results.Count -eq $dates.Count -and @($results | Where-Object status -ne 'succeeded').Count -eq 0) { 'complete' } else { 'failed' }
    }
    $final | ConvertTo-Json -Depth 5 | Set-Content -Path (Join-Path $outputDir 'result.json') -Encoding utf8
    Pop-Location
}
