# Administrative packet verification/seal only. No mathematical computation.
$ErrorActionPreference = 'Stop'
$repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$packet = Join-Path $repo 'results/a25_04'
function Get-Sha([byte[]]$bytes) {
    [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
}
function Write-OwnJson([string]$path, $record) {
    $json = ($record | ConvertTo-Json -Depth 8).Replace("`r`n", "`n") + "`n"
    [IO.File]::WriteAllText($path, $json, [Text.UTF8Encoding]::new($false))
}
function Invoke-ReadGit([string[]]$gitArgs) {
    $psi = [Diagnostics.ProcessStartInfo]::new('git')
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    foreach ($arg in (@('-C', $repo) + $gitArgs)) { $psi.ArgumentList.Add($arg) }
    $proc = [Diagnostics.Process]::Start($psi)
    $output = $proc.StandardOutput.ReadToEnd()
    $err = $proc.StandardError.ReadToEnd()
    $proc.WaitForExit()
    if ($proc.ExitCode -ne 0) { throw "git read failed: $err" }
    [ordered]@{stdout=$output.TrimEnd(); stderr=$err.TrimEnd(); exit_code=$proc.ExitCode}
}
$head = Invoke-ReadGit @('rev-parse','HEAD')
$branch = Invoke-ReadGit @('branch','--show-current')
if ($head.stdout -ne '82633a60893236fab4fbc317df416e1b8a349005' -or $branch.stdout -ne 'batch15-launch') { throw 'Branch or baseline changed; inspect before resealing' }
$listed = @(Get-Content -LiteralPath (Join-Path $packet 'ADD_LIST.txt') | Where-Object { $_.Trim() })
$manifestRel = 'results/a25_04/MANIFEST.json'
$verifyRel = 'results/a25_04/ADMIN_VERIFICATION.json'
$allowed = '^docs/a25_04_report\.md$|^analysis/a25_04_[^/]+$|^results/a25_04/'
foreach ($path in $listed) { if ($path -notmatch $allowed) { throw "Out-of-scope path: $path" } }
$tracked = Invoke-ReadGit @('diff','--name-only','HEAD')
$status = Invoke-ReadGit @('status','--short')
$checks = @()
foreach ($path in $listed) {
    if ($path -in @($manifestRel,$verifyRel)) { continue }
    $full = Join-Path $repo $path
    if (-not (Test-Path -LiteralPath $full)) { throw "Missing artifact: $path" }
    $bytes = [IO.File]::ReadAllBytes($full)
    $raw = Invoke-ReadGit @('hash-object','--no-filters',$full)
    $filtered = Invoke-ReadGit @('hash-object',"--path=$path",$full)
    $checks += [ordered]@{path=$path; bytes=$bytes.Length; sha256=(Get-Sha $bytes); raw_git_hash=$raw.stdout; filtered_git_hash=$filtered.stdout; raw_equals_filtered=($raw.stdout -eq $filtered.stdout); filtering_stderr=$filtered.stderr; state='UNCOMMITTED raw bytes'}
}
$priorBinding = Get-Content -Raw (Join-Path $packet 'SOURCE_BINDINGS.json') | ConvertFrom-Json
$priorUnchanged = @()
foreach ($row in $priorBinding.prior_packets) {
    $bytes = [IO.File]::ReadAllBytes((Join-Path $repo $row.path))
    $same = (Get-Sha $bytes) -eq $row.sha256
    if (-not $same) { throw "Prior packet changed: $($row.path)" }
    $priorUnchanged += [ordered]@{path=$row.path; unchanged=$same}
}
$utc = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
$verificationRecord = [ordered]@{
    utc=$utc
    method='Administrative file/hash/read-only Git verification, not a mathematical evaluator'
    branch=$branch.stdout
    head=$head.stdout
    tracked_diff=$tracked
    observed_status=$status
    payload_filter_checks=$checks
    excluded_from_filter_check=@($verifyRel,$manifestRel)
    exclusion_reason='Avoid circular receipt/self-hash; both are hashed externally or in the payload manifest as applicable'
    prior_packet_entries_unchanged=$priorUnchanged
    mathematical_pilots=0
    git_mutation=$false
}
Write-OwnJson (Join-Path $repo $verifyRel) $verificationRecord
$actual = @('docs/a25_04_report.md')
$actual += Get-ChildItem -LiteralPath (Join-Path $repo 'analysis') -File -Filter 'a25_04_*' | ForEach-Object { 'analysis/' + $_.Name }
$actual += Get-ChildItem -LiteralPath $packet -File -Recurse | ForEach-Object { [IO.Path]::GetRelativePath($repo,$_.FullName).Replace('\','/') }
$expectedNow = $listed | Where-Object { $_ -ne $manifestRel }
$actualNow = $actual | Where-Object { $_ -ne $manifestRel }
$difference = Compare-Object ($expectedNow | Sort-Object) ($actualNow | Sort-Object)
if ($difference) { throw "Artifact-list discrepancy: $($difference | Out-String)" }
$artifacts = foreach ($path in $expectedNow) {
    $bytes = [IO.File]::ReadAllBytes((Join-Path $repo $path))
    [ordered]@{path=$path; bytes=$bytes.Length; sha256=(Get-Sha $bytes); state='UNCOMMITTED / NOT RELEASED'}
}
$manifestRecord = [ordered]@{
    schema='a25_04.local_packet.v1'
    slot='A25-04'
    outcome=3
    status='LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED'
    theorem_status='PROVED, self-contained hand derivation, producer-only; independent review pending'
    theorem='The ten specified bordered 2-minors of d_1^(3) at N=5 admit a polynomial section from determinant pencils; their polynomial algebra has zero intersection with I(D45).'
    candidate='h0=det(m_ij), coefficient degree 8; h0(det control)=256; h0(actual padding control)=-4096; h0 is not a determinant equation'
    repository=$repo
    branch=$branch.stdout
    baseline_head=$head.stdout
    delivery_commit=$null
    started_utc='2026-09-21T03:27:11Z'
    mechanism_frozen_by_utc='2026-09-21T03:29:36Z'
    outcome_fixed_by_utc='2026-09-21T03:33:27Z'
    sealed_utc=$utc
    evidence_method='READ plus self-contained hand derivation; no REPLAY or computational INDEPENDENT EVALUATOR'
    source_bindings='results/a25_04/SOURCE_BINDINGS.json'
    source_read_status='results/a25_04/SOURCE_READS.md'
    mathematical_pilots=0
    mathematical_computational_seconds=0
    compute_lease_touched=$false
    tool_memory_created=$false
    tool_memory_used_as_evidence=$false
    additional_agents_or_tasks=0
    next_certificate='Independent hand review of section/global identity and exact controls; 20–40 minutes; no pilot proposed'
    artifacts=@($artifacts)
    excludes=@('Manifest self-hash','All other producer paths','Shared ledger and lease','Git mutation and publication')
    proposed_delivery_paths='results/a25_04/ADD_LIST.txt'
    open_gates=@('Independent review','G29 separately authorized committed-byte delivery')
}
Write-OwnJson (Join-Path $repo $manifestRel) $manifestRecord
$manifestBytes = [IO.File]::ReadAllBytes((Join-Path $repo $manifestRel))
"Sealed $(@($artifacts).Count) payload artifacts plus manifest at $utc."
"UNCOMMITTED manifest SHA-256: $(Get-Sha $manifestBytes)"
"Raw/filter differences among checked files: $(@($checks | Where-Object { -not $_.raw_equals_filtered }).Count)."
"Prior payloads and manifests unchanged: $($priorUnchanged.Count)."
