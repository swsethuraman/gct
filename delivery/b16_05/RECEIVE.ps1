# B16-05 receiver: same four points in each family, sequential bounded runs.
# Execute in the original worktree; inherited inputs are hash checked.
$ErrorActionPreference = 'Stop'
$slotRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).Path
Push-Location -LiteralPath $slotRoot
try {
    & ./.venv/python.exe -B analysis/b15_bound.py --slot 05 --name b16_05_receive_projection --seconds 60 --memory-mb 512 analysis/b16_05_receiver.py replay
    if ($LASTEXITCODE -ne 0) { throw 'Projection receiver failed' }
    & ./.venv/python.exe -B analysis/b15_bound.py --slot 05 --name b16_05_receive_proof --seconds 60 --memory-mb 512 analysis/b16_05_proof.py
    if ($LASTEXITCODE -ne 0) { throw 'Proof receiver failed' }
}
finally {
    Pop-Location
}
