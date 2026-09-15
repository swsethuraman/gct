param([string]$ReceiptName = ('b16_08_receive_' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')))
$ErrorActionPreference = 'Stop'
if ($ReceiptName -notmatch '^b16_08_[A-Za-z0-9_]+$') { throw 'Receipt name must have the owned b16_08_ prefix.' }
$TaskRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
Push-Location -LiteralPath $TaskRoot
try {
    & (Join-Path $TaskRoot '.venv/python.exe') -B analysis/b15_bound.py --slot 08 --name $ReceiptName --seconds 60 --memory-mb 512 analysis/b16_08_jets.py receive
    if ($LASTEXITCODE -ne 0) { throw "Receiver failed with exit $LASTEXITCODE" }
} finally {
    Pop-Location
}
