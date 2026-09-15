$ErrorActionPreference = 'Stop'
$b1607Worktree = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$b1607Stamp = Get-Date -Format 'yyyyMMdd_HHmmss_ffff'
$b1607Run = "b16_07_receive_$b1607Stamp"
Push-Location -LiteralPath $b1607Worktree
try {
    & './.venv/python.exe' -B 'analysis/b15_bound.py' --slot 07 --name $b1607Run --seconds 60 --memory-mb 512 'analysis/b16_07_receive.py' --out "results/b16_07/receiver_$b1607Stamp.json"
    if ($LASTEXITCODE -ne 0) { throw "B16-07 receiver failed with exit $LASTEXITCODE" }
} finally {
    Pop-Location
}
