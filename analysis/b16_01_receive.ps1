$ErrorActionPreference = 'Stop'
$b16Worktree = Split-Path -Parent $PSScriptRoot
Push-Location -LiteralPath $b16Worktree
try {
    & '.venv/python.exe' -B 'analysis/b15_bound.py' --slot 01 --name b16_01_receiver --seconds 60 --memory-mb 512 'analysis/b16_01_finite.py' verify
    if ($LASTEXITCODE -ne 0) { throw 'Finite cubic receiver failed.' }
    & '.venv/python.exe' -B 'analysis/b15_bound.py' --slot 01 --name b16_01_transport --seconds 60 --memory-mb 512 'analysis/b16_01_transport.py'
    if ($LASTEXITCODE -ne 0) { throw 'Transport receiver failed.' }
} finally {
    Pop-Location
}
