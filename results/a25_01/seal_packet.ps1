$ErrorActionPreference = 'Stop'
$repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$dir = "$repo/results/a25_01"
$encoding = New-Object Text.UTF8Encoding($false)
$listPath = "$dir/PROPOSED_ADD_LIST.txt"
$paths = @('docs/a25_01_report.md')
$paths += @(Get-ChildItem -LiteralPath $dir -File | Where-Object { $_.Name -notin @('MANIFEST.json','PROPOSED_ADD_LIST.txt') } | ForEach-Object { 'results/a25_01/' + $_.Name })
$paths += @('results/a25_01/PROPOSED_ADD_LIST.txt','results/a25_01/MANIFEST.json')
$paths = @($paths | Sort-Object -Unique)
[IO.File]::WriteAllText($listPath, ($paths -join "`n") + "`n", $encoding)
$files = @()
foreach ($path in $paths) {
    if ($path -eq 'results/a25_01/MANIFEST.json') { continue }
    $full = "$repo/$path"
    $files += [ordered]@{path=$path; bytes=(Get-Item -LiteralPath $full).Length; sha256=(Get-FileHash -LiteralPath $full -Algorithm SHA256).Hash.ToLowerInvariant(); state='UNCOMMITTED'}
}
$sources = Get-Content -Raw "$dir/SOURCE_BINDINGS.json" | ConvertFrom-Json
$manifest = [ordered]@{
    slot='A25-01'; status='LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED'; outcome=3
    sealed_utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
    starting_head='82633a60893236fab4fbc317df416e1b8a349005'; branch='batch15-launch'; delivery_commit=$null
    theorem='Rational section on a!=0 for 15 second-transverse-jet coordinates; K intersect R2=0 in every degree.'
    claim_status='PROVED, producer-only'; method='READ plus independent hand derivation; no replay or computational evaluator'
    source_bindings=$sources.records
    pilots=0; mathematical_computational_seconds=0; computational_environment='Not used; administrative PowerShell/Git/.NET hashing only'
    files=$files
    excluded=@('Manifest self-hash','All other producers and shared ledgers','Runtime/PID receipts: none exist','Git mutation and publication')
    gates_open=@('Separately authorized committed-byte delivery binding','Independent review')
}
[IO.File]::WriteAllText("$dir/MANIFEST.json", ($manifest | ConvertTo-Json -Depth 10) + "`n", $encoding)
foreach ($item in $files) {
    if ((Get-FileHash -LiteralPath "$repo/$($item.path)" -Algorithm SHA256).Hash.ToLowerInvariant() -ne $item.sha256) { throw "Seal changed: $($item.path)" }
}
Write-Output "Verified bound files: $($files.Count)"
Write-Output "Proposed add paths: $($paths.Count)"
Write-Output ('Manifest SHA-256 (UNCOMMITTED): ' + (Get-FileHash -LiteralPath "$dir/MANIFEST.json" -Algorithm SHA256).Hash.ToLowerInvariant())
