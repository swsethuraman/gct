# Administrative source binding only: no mathematical computation.
$ErrorActionPreference = 'Stop'
$a25Repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$a25Out = "$a25Repo/results/a25_03"
$prior = @()
foreach ($slot in @('a25_01','a25_02')) {
  $manifestPath = "$a25Repo/results/$slot/MANIFEST.json"
  $manifest = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
  $items = if ($manifest.artifacts) { $manifest.artifacts } else { $manifest.files }
  if (-not $items) { throw "No payload entries for $slot" }
  $checked = @()
  foreach ($item in $items) {
    $path = "$a25Repo/$($item.path)"
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
    if ($sha -ne $item.sha256) { throw "Prior packet mismatch: $path" }
    $checked += [ordered]@{path=$item.path; bytes=(Get-Item -LiteralPath $path).Length; sha256=$sha; match=$true; status='UNCOMMITTED provisional bytes; integrity only, not acceptance'}
  }
  $prior += [ordered]@{slot=$slot; manifest_path="results/$slot/MANIFEST.json"; manifest_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash.ToLowerInvariant(); status='UNCOMMITTED / NOT INDEPENDENTLY REVIEWED'; verified_payload=$checked}
}
$locators = (Get-Content -Raw "$a25Repo/results/a25_02/SOURCE_BINDINGS.json" | ConvertFrom-Json).sources
$wanted = @('lemmas','lemma_review','purepower','tail','archive','fiveblock_review','review24','ledger24')
$bound = @()
foreach ($entry in $locators) {
  if ($entry.id -notin $wanted) { continue }
  $locator = "$($entry.commit):$($entry.path)"
  $psi = [Diagnostics.ProcessStartInfo]::new('git')
  $psi.UseShellExecute = $false
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  foreach ($arg in @('-C',$a25Repo,'show',$locator)) { $psi.ArgumentList.Add($arg) }
  $proc = [Diagnostics.Process]::Start($psi)
  $ms = [IO.MemoryStream]::new()
  $proc.StandardOutput.BaseStream.CopyTo($ms)
  $err = $proc.StandardError.ReadToEnd()
  $proc.WaitForExit()
  if ($proc.ExitCode -ne 0) { throw $err }
  $bytes = $ms.ToArray()
  $sha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
  if ($sha -ne $entry.sha256) { throw "Committed input mismatch: $locator" }
  $blob = (& git -C $a25Repo rev-parse $locator).Trim()
  $bound += [ordered]@{id=$entry.id; original_repository=$entry.original_repository; read_repository=$a25Repo; commit=$entry.commit; path=$entry.path; blob=$blob; bytes=$bytes.Length; sha256=$sha; status='VERIFIED COMMITTED OBJECT CONTENT'; method='Fresh raw Git object byte hash; reading scope in SOURCE_READS.md; not replay'}
}
$adminPaths = @(
 'C:/Users/swami/Projects/gct-gpt/RUNBOOK.md',
 'C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_followup/v1_20260921T032518Z/A25-03.md',
 'C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_followup/v1_20260921T032518Z/FOLLOWUP_COMMON.md',
 'C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/CLAUDE_COMMON.md',
 'C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/SOURCE_INDEX.md',
 'C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch25_launch/v1_20260921T003934Z/COMPUTE_PROTOCOL.md',
 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/docs/b25_12_ledger.md'
)
$admin = foreach($path in $adminPaths) { [ordered]@{path=$path; bytes=(Get-Item -LiteralPath $path).Length; sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant(); status='UNCOMMITTED administrative bytes at read/binding; not mathematical evidence'} }
[ordered]@{utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'); prior_packets=$prior; sources=$bound; administrative_inputs=@($admin); mathematical_computations=0} | ConvertTo-Json -Depth 12 | Set-Content -Encoding utf8NoBOM "$a25Out/SOURCE_BINDINGS.json"
"Bound $($bound.Count) committed objects; verified prior payload counts: $($prior.verified_payload.Count -join ', '); no mathematical computation."
