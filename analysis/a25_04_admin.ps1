# Administrative source/packet integrity only. No mathematical computation.
$ErrorActionPreference = 'Stop'
$repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$outDir = Join-Path $repo 'results/a25_04'
[IO.Directory]::CreateDirectory($outDir) | Out-Null
function Get-Sha([byte[]]$bytes) {
    [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
}
function Read-GitBlob([string]$spec) {
    $psi = [Diagnostics.ProcessStartInfo]::new('git')
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    foreach ($arg in @('-C', $repo, 'show', $spec)) { $psi.ArgumentList.Add($arg) }
    $proc = [Diagnostics.Process]::Start($psi)
    $ms = [IO.MemoryStream]::new()
    $proc.StandardOutput.BaseStream.CopyTo($ms)
    $err = $proc.StandardError.ReadToEnd()
    $proc.WaitForExit()
    if ($proc.ExitCode -ne 0) { throw $err }
    return ,$ms.ToArray()
}
$prior = @()
foreach ($slot in @('a25_01','a25_02')) {
    $manifestPath = "results/$slot/MANIFEST.json"
    $manifest = Get-Content -Raw (Join-Path $repo $manifestPath) | ConvertFrom-Json
    $payload = if ($slot -eq 'a25_01') { $manifest.files } else { $manifest.artifacts }
    foreach ($f in $payload) {
        $bytes = [IO.File]::ReadAllBytes((Join-Path $repo $f.path))
        $sha = Get-Sha $bytes
        if ($sha -ne $f.sha256 -or $bytes.Length -ne $f.bytes) { throw "Prior manifest mismatch: $($f.path)" }
        $prior += [ordered]@{path=$f.path; bytes=$bytes.Length; sha256=$sha; manifest=$manifestPath; matches=$true; state='UNCOMMITTED / NOT INDEPENDENTLY REVIEWED'; method='Administrative integrity check only; read scope in SOURCE_READS.md'}
    }
    $mb = [IO.File]::ReadAllBytes((Join-Path $repo $manifestPath))
    $prior += [ordered]@{path=$manifestPath; bytes=$mb.Length; sha256=(Get-Sha $mb); state='UNCOMMITTED / NOT INDEPENDENTLY REVIEWED'; method='Manifest bytes bound separately; no self-hash claim'}
}
$sourceIndex = Get-Content -Raw (Join-Path $repo 'results/a25_02/SOURCE_BINDINGS.json') | ConvertFrom-Json
$ids = @('lemmas','lemma_review','koszul','fiveblock_review','review24','ledger24','tail','purepower','archive')
$committed = @()
foreach ($f in $sourceIndex.sources) {
    if ($f.id -notin $ids) { continue }
    $spec = "$($f.commit):$($f.path)"
    $bytes = Read-GitBlob $spec
    $sha = Get-Sha $bytes
    $blob = (& git -C $repo rev-parse $spec).Trim()
    if ($LASTEXITCODE -ne 0 -or $sha -ne $f.sha256 -or $blob -ne $f.blob) { throw "Committed source mismatch: $spec" }
    $committed += [ordered]@{id=$f.id; repository=$repo; commit=$f.commit; path=$f.path; blob=$blob; bytes=$bytes.Length; sha256=$sha; state='COMMITTED SOURCE CONTENT'; method='Fresh raw git-object read/hash; read scope and use status in SOURCE_READS.md'; provisional_locator_matched=$true}
}
$root = 'C:/Users/swami/Projects/gct-gpt'
$adminPaths = @(
    'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_followup/v1_20260921T032518Z/A25-04.md',
    'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_followup/v1_20260921T032518Z/FOLLOWUP_COMMON.md',
    'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/CLAUDE_COMMON.md',
    'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/SOURCE_INDEX.md',
    'Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/COMPUTE_PROTOCOL.md',
    'work/batch15_workers/B15-12/docs/b25_12_ledger.md'
)
$admin = foreach ($path in $adminPaths) {
    $full = Join-Path $root $path
    $bytes = [IO.File]::ReadAllBytes($full)
    [ordered]@{path=$full; bytes=$bytes.Length; sha256=(Get-Sha $bytes); state='UNCOMMITTED ADMINISTRATIVE INPUT'; method='READ in full; authorization/scope, not mathematical evidence'}
}
$bindingRecord = [ordered]@{
    checked_utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
    method='Administrative raw-byte integrity; not REPLAY or INDEPENDENT EVALUATOR'
    prior_packets=$prior
    committed_sources=$committed
    administrative_inputs=@($admin)
}
$json = ($bindingRecord | ConvertTo-Json -Depth 8).Replace("`r`n", "`n") + "`n"
[IO.File]::WriteAllText((Join-Path $outDir 'SOURCE_BINDINGS.json'), $json, [Text.UTF8Encoding]::new($false))
"Verified $($prior.Count - 2) prior payload entries, 2 provisional manifests, and $($committed.Count) committed blobs. Mathematical pilots: 0."
