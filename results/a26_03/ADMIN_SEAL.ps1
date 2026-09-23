# Administrative byte binding and manifest generation only. No mathematics.
# This script reads pinned Git blobs, hashes bytes and seals this slot's payloads.
$ErrorActionPreference = 'Stop'
$root = 'C:\Users\swami\Projects\gct-gpt\work\batch15'
$out = Join-Path $root 'results\a26_03'
$encoding = [System.Text.UTF8Encoding]::new($false)
function Get-BytesHash([byte[]]$bytes) {
    [Convert]::ToHexString([System.Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
}
function Read-Blob([string]$spec) {
    $start = [System.Diagnostics.ProcessStartInfo]::new()
    $start.FileName = 'git'
    foreach ($arg in @('-C', $root, 'show', $spec)) { $start.ArgumentList.Add($arg) }
    $start.UseShellExecute = $false
    $start.RedirectStandardOutput = $true
    $start.CreateNoWindow = $true
    $proc = [System.Diagnostics.Process]::Start($start)
    $buffer = [System.IO.MemoryStream]::new()
    $proc.StandardOutput.BaseStream.CopyTo($buffer)
    $proc.WaitForExit()
    if ($proc.ExitCode -ne 0) { throw "git show failed: $spec" }
    return ,$buffer.ToArray()
}
$specs = @(
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:docs/b26_02_review.md',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/MANIFEST.json',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/INPUT_BINDINGS.md',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/CHECKPOINT.md',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/RESOURCE_RECEIPT.md',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/PROPOSED_DELIVERY_PATHS.txt',
    '0d6f5a8cc206e8703e3ebd9c0c45acb88adea0eb:results/b26_expander_input/CONSTRUCTION_AND_LIMITATIONS.md',
    '0d6f5a8cc206e8703e3ebd9c0c45acb88adea0eb:results/b26_expander_input/PADDING_SURVIVAL.md',
    '0d6f5a8cc206e8703e3ebd9c0c45acb88adea0eb:results/b26_expander_input/DETERMINANT_REJECTION.md',
    '92a7d054369a20854fd51685ee09ecb756344e8d:docs/b25_04_report.md',
    '9e12d7892734f6ec199da3b947e64f09704959d7:results/b25_04/SCOPE_ERRATUM_20260922.md',
    '7464a2bd02c9740db55d15ac43571cca74acea5f:docs/a26_01_report.md',
    '7464a2bd02c9740db55d15ac43571cca74acea5f:results/a26_01/PROOF.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:results/a25_10/NEXT_ACTION.md',
    'cdf6839cd81031d42e43dc640b08e2746a7ef22c:docs/b22_02_report.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:results/a25_02/APPLICATIONS.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:results/a25_02/SCOPE_MATRIX.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:results/a25_10/REVIEW.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/REVISED_VERDICT.md',
    'ab4f527189bea14b5d146f9dc9d5b445844eaff3:docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/CLAIM_SCOPE_TABLE.md'
)
$records = foreach ($spec in $specs) {
    $bytes = Read-Blob $spec
    $parts = $spec.Split(':', 2)
    [ordered]@{
        commit = $parts[0]
        path = $parts[1]
        bytes = $bytes.Length
        sha256 = Get-BytesHash $bytes
        cr_bytes = @($bytes.Where({ $_ -eq 13 })).Count
        hash_names = 'exact committed Git blob bytes, no working-copy conversion'
    }
}
$auditManifestBytes = Read-Blob 'cdf6839cd81031d42e43dc640b08e2746a7ef22c:results/b26_02/MANIFEST.json'
if ((Get-BytesHash $auditManifestBytes) -ne '02060eac5391002420d5bbc216da02543a3dec79899c05a835bc84b6951a0cb9') {
    throw 'Governing manifest mismatch'
}
$auditManifest = [System.Text.Encoding]::UTF8.GetString($auditManifestBytes) | ConvertFrom-Json
foreach ($entry in $auditManifest.files) {
    $bytes = Read-Blob ('cdf6839cd81031d42e43dc640b08e2746a7ef22c:' + $entry.path)
    if ($bytes.Length -ne $entry.bytes -or (Get-BytesHash $bytes) -ne $entry.sha256) {
        throw "Audit payload mismatch: $($entry.path)"
    }
}
$bindings = [ordered]@{
    status = 'UNCOMMITTED / PRODUCER ONLY'
    administrative_only = $true
    preflight_worktree = $root
    preflight_branch = 'batch15-launch'
    preflight_head = '7464a2bd02c9740db55d15ac43571cca74acea5f'
    administrative_raw_sha256_at_preflight = [ordered]@{
        B26_COMMON = 'a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd'
        A26_03 = 'd1a15deda8dd8af882dc2b77bd6c2d01934718027c884d38f8b8e4291cfc1991'
        BATCH26_LIVE_LEDGER = '1ec1ff50dc397e8df4505e03902393fd95cd7974b1196468b66c4e5115c38a10'
    }
    audit_manifest_payloads_verified = 5
    read_scope = 'See SOURCE_LEDGER.md. Hash verification is not mathematical reading or review.'
    inputs = @($records)
}
[System.IO.File]::WriteAllText((Join-Path $out 'INPUT_BINDINGS.json'), ($bindings | ConvertTo-Json -Depth 8) + [char]10, $encoding)
$paths = @(
    'docs/a26_03_report.md',
    'results/a26_03/ADMIN_SEAL.ps1',
    'results/a26_03/CHECKPOINT.md',
    'results/a26_03/INPUT_BINDINGS.json',
    'results/a26_03/PROOF.md',
    'results/a26_03/PROPOSED_DELIVERY_PATHS.txt',
    'results/a26_03/RESOURCE_RECEIPT.md',
    'results/a26_03/SOURCE_LEDGER.md'
)
$listed = @($paths + 'results/a26_03/MANIFEST.json' | Sort-Object)
[System.IO.File]::WriteAllText((Join-Path $out 'PROPOSED_DELIVERY_PATHS.txt'), ($listed -join [char]10) + [char]10, $encoding)
$files = foreach ($path in $paths) {
    $bytes = [System.IO.File]::ReadAllBytes((Join-Path $root $path))
    [ordered]@{ path=$path; bytes=$bytes.Length; sha256=(Get-BytesHash $bytes) }
}
$manifest = [ordered]@{
    schema = 'a26_03_manifest_v1'
    status = 'UNCOMMITTED / PRODUCER ONLY'
    hash = 'SHA-256 of raw payload bytes on disk; no newline conversion'
    manifest_self_hashed = $false
    files = @($files)
}
[System.IO.File]::WriteAllText((Join-Path $out 'MANIFEST.json'), ($manifest | ConvertTo-Json -Depth 8) + [char]10, $encoding)
$verify = Get-Content -LiteralPath (Join-Path $out 'MANIFEST.json') -Raw | ConvertFrom-Json
foreach ($entry in $verify.files) {
    $bytes = [System.IO.File]::ReadAllBytes((Join-Path $root $entry.path))
    if ($bytes.Length -ne $entry.bytes -or (Get-BytesHash $bytes) -ne $entry.sha256) {
        throw "Output payload mismatch: $($entry.path)"
    }
}
$actual = @(Get-ChildItem -LiteralPath $out -File | ForEach-Object { 'results/a26_03/' + $_.Name })
$actual += 'docs/a26_03_report.md'
if (Compare-Object ($actual | Sort-Object) $listed) { throw 'Output inventory mismatch' }
Write-Output 'Administrative verification: 5 audit payloads match; 8 output payloads match; 9 delivery paths match.'
Write-Output ('Output manifest raw SHA-256: ' + (Get-BytesHash ([System.IO.File]::ReadAllBytes((Join-Path $out 'MANIFEST.json')))))
