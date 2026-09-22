# Administrative local validation only. No mathematical evaluator or Git mutation.
$ErrorActionPreference = 'Stop'
$a25Repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$a25Out = "$a25Repo/results/a25_03"
$payload = @(
 'docs/a25_03_report.md',
 'analysis/a25_03_admin.ps1',
 'analysis/a25_03_seal.ps1',
 'results/a25_03/STATUS.md',
 'results/a25_03/FRAMES.md',
 'results/a25_03/PROOF.md',
 'results/a25_03/INDEPENDENT_LEMMAS.md',
 'results/a25_03/EXCLUSION_PADDING.md',
 'results/a25_03/JACOBIAN_CERTIFICATE.json',
 'results/a25_03/SOURCE_READS.md',
 'results/a25_03/SOURCE_BINDINGS.json',
 'results/a25_03/RESOURCES_NEXT.md',
 'results/a25_03/DELIVERY_NOTE.md',
 'results/a25_03/ADD_LIST.txt'
)
$all = @($payload) + 'results/a25_03/ADMIN_VERIFICATION.json' + 'results/a25_03/MANIFEST.json'
[IO.File]::WriteAllText("$a25Out/ADD_LIST.txt", ($all -join "`n")+"`n", [Text.UTF8Encoding]::new($false))
$head = (& git -C $a25Repo rev-parse HEAD).Trim()
$branch = (& git -C $a25Repo branch --show-current).Trim()
if ($head -ne '82633a60893236fab4fbc317df416e1b8a349005' -or $branch -ne 'batch15-launch') { throw 'Repository baseline changed; inspect before sealing.' }
$status = @(& git -C $a25Repo status --short 2>$null)
$tracked = @(& git -C $a25Repo diff --name-only 2>$null)
$staged = @(& git -C $a25Repo diff --cached --name-only 2>$null)
$checks = @()
foreach ($p in $payload) {
  if (-not (Test-Path -LiteralPath "$a25Repo/$p" -PathType Leaf)) { throw "Missing $p" }
  $raw = (& git -C $a25Repo hash-object --no-filters -- "$a25Repo/$p").Trim()
  $filtered = (& git -C $a25Repo hash-object "--path=$p" -- "$a25Repo/$p" 2>$null).Trim()
  $attrs = @(& git -C $a25Repo check-attr text eol filter -- $p)
  $ignored = @(& git -C $a25Repo check-ignore -- $p 2>$null)
  $ignoreCode = $LASTEXITCODE
  if ($ignoreCode -notin @(0,1)) { throw "Ignore check error for $p" }
  if ($ignoreCode -eq 0) { throw "Proposed file ignored: $p" }
  $checks += [ordered]@{path=$p; raw_blob_id=$raw; filtered_blob_id=$filtered; raw_equals_filtered=($raw -eq $filtered); attributes=$attrs; ignored=$false; status='UNCOMMITTED working bytes; object IDs computed without writing objects'}
}
# JSON syntax checks are administrative; no rank/arithmetic certificate is evaluated.
$null = Get-Content -Raw "$a25Out/JACOBIAN_CERTIFICATE.json" | ConvertFrom-Json
$source = Get-Content -Raw "$a25Out/SOURCE_BINDINGS.json" | ConvertFrom-Json
$priorChecks = @()
foreach($packet in $source.prior_packets) {
  $manifestSha = (Get-FileHash -Algorithm SHA256 -LiteralPath "$a25Repo/$($packet.manifest_path)").Hash.ToLowerInvariant()
  if ($manifestSha -ne $packet.manifest_sha256) { throw "Prior manifest changed: $($packet.slot)" }
  foreach($entry in $packet.verified_payload) {
    $actual=(Get-FileHash -Algorithm SHA256 -LiteralPath "$a25Repo/$($entry.path)").Hash.ToLowerInvariant()
    if ($actual -ne $entry.sha256) { throw "Prior source changed: $($entry.path)" }
  }
  $priorChecks += [ordered]@{slot=$packet.slot; payload_count=$packet.verified_payload.Count; manifests_and_payload_unchanged=$true; acceptance='Integrity only; provisional and UNCOMMITTED'}
}
$links=@()
$report=[IO.File]::ReadAllText("$a25Repo/docs/a25_03_report.md")
foreach($match in [regex]::Matches($report,'\]\(([^)]+)\)')) {
  $target=$match.Groups[1].Value
  if ($target -match '^(https?:|#)') { continue }
  $resolved=[IO.Path]::GetFullPath([IO.Path]::Combine("$a25Repo/docs",$target))
  $generated=$target -match '(MANIFEST.json|ADMIN_VERIFICATION.json)$'
  if (-not(Test-Path -LiteralPath $resolved) -and -not $generated) { throw "Broken report link: $target" }
  $links += [ordered]@{target=$target; resolved=$resolved; exists_or_generated_by_seal=$true}
}
$now=[DateTime]::UtcNow
$verification=[ordered]@{
 utc=$now.ToString('yyyy-MM-ddTHH:mm:ssZ'); status='UNCOMMITTED administrative checks only';
 branch=$branch; head=$head; worktree_short_status=$status; tracked_differences=$tracked; staged_differences=$staged;
 own_file_checks=$checks; prior_packet_rechecks=$priorChecks; report_links=$links;
 global_ignore_note='Git status warns that account global ignore is unreadable in sandbox; relevant queries succeeded; no trust or ownership change';
 mathematical_evaluator_runs=0; tool_memory_created=$false; tool_memory_consumed=$false
}
$verification | ConvertTo-Json -Depth 10 | Set-Content -Encoding utf8NoBOM "$a25Out/ADMIN_VERIFICATION.json"
$payload += 'results/a25_03/ADMIN_VERIFICATION.json'
$artifacts = foreach($p in $payload) {
 [ordered]@{path=$p; bytes=(Get-Item -LiteralPath "$a25Repo/$p").Length; sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath "$a25Repo/$p").Hash.ToLowerInvariant(); status='UNCOMMITTED / NOT RELEASED'}
}
$manifest=[ordered]@{
 schema='a25_03.local_packet.v1'; slot='A25-03'; outcome=3;
 status='LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED'; claim_status='PROVED by hand, producer-only; independent review pending';
 repository=$a25Repo; branch=$branch; research_head=$head; delivery_commit=$null;
 assessment_started_utc='2026-09-21T03:27:10Z'; mechanism_frozen_utc='2026-09-21T03:28:13Z'; outcome_selected_by_utc='2026-09-21T03:30:32Z';
 sealed_utc=$now.ToString('yyyy-MM-ddTHH:mm:ssZ'); elapsed_wall_seconds=[math]::Round(($now-[datetime]::Parse('2026-09-21T03:27:10Z').ToUniversalTime()).TotalSeconds,1);
 result='Two fixed distinct-center second-transverse jets: overlap dimension 1, actual joint dimension 29, dominant determinant projection; no nonzero polynomial determinant equation in joint ring in any degree';
 certificate='Exact hand-derived 29-by-29 Jacobian with determinant 5308416; bases in JACOBIAN_CERTIFICATE.json';
 frame_scope='Every fixed rational or complex pair with distinct center lines; proof of GL5 transport in FRAMES.md';
 padding_status='No nonzero equation exists in the family, hence no actual-padding separator from it; no product-equality premise';
 evidence_method='READ plus independent hand derivation; no computational REPLAY or INDEPENDENT EVALUATOR';
 mathematical_pilots=0; mathematical_computational_seconds=0; compute_lease_acquired=$false;
 provisional_inputs='A25-01/02 current manifests and 29 payload hashes verified; needed elementary lemmas independently derived; no conditional dependence in new proof';
 source_bindings='results/a25_03/SOURCE_BINDINGS.json'; source_reads='results/a25_03/SOURCE_READS.md';
 artifacts=@($artifacts); manifest_self_hashed=$false;
 proposed_delivery_paths='results/a25_03/ADD_LIST.txt'; next_certificate='Independent audit of J29 and frame/global implication, estimated 20-40 minutes';
 tool_memory_created=$false; tool_memory_consumed=$false;
 limitations=@('No extra-frame or higher-jet investigation','No coefficient-dependent frames','No surjectivity or rational-section assertion','No padding nonvanishing, multiplicity gap or asymptotic bound','G29 delivery and independent review pending','All new hashes identify uncommitted bytes')
}
$manifest | ConvertTo-Json -Depth 12 | Set-Content -Encoding utf8NoBOM "$a25Out/MANIFEST.json"
$reloaded=Get-Content -Raw "$a25Out/MANIFEST.json" | ConvertFrom-Json
foreach($a in $reloaded.artifacts) {
 $actual=(Get-FileHash -Algorithm SHA256 -LiteralPath "$a25Repo/$($a.path)").Hash.ToLowerInvariant()
 if ($actual -ne $a.sha256) { throw "Seal mismatch: $($a.path)" }
}
$actualOwn=@(Get-ChildItem -LiteralPath $a25Out -File | ForEach-Object {"results/a25_03/$($_.Name)"}) + @('docs/a25_03_report.md') + @(Get-ChildItem -Path "$a25Repo/analysis/a25_03_*" -File | ForEach-Object {"analysis/$($_.Name)"})
$unlisted=@($actualOwn | Where-Object {$_ -notin $all})
if ($unlisted.Count -gt 0) {throw "Unlisted own outputs: $($unlisted -join ', ')"}
foreach($p in $all) { if(-not(Test-Path -LiteralPath "$a25Repo/$p")) { throw "Add list missing $p" } }
"Verified $($artifacts.Count) payload hashes, $($all.Count) proposed files and $($links.Count) report links."
"Prior packets unchanged; no mathematical program or Git mutation."
"Pre-seal payload raw/filtered mismatches: $(@($checks | Where-Object {-not $_.raw_equals_filtered}).Count)."
foreach($p in @('results/a25_03/ADMIN_VERIFICATION.json','results/a25_03/MANIFEST.json')) {
 $raw=(& git -C $a25Repo hash-object --no-filters -- "$a25Repo/$p").Trim()
 $filtered=(& git -C $a25Repo hash-object "--path=$p" -- "$a25Repo/$p" 2>$null).Trim()
 "Generated metadata check: $p raw_equals_filtered=$($raw -eq $filtered); UNCOMMITTED bytes."
}
"UNCOMMITTED manifest SHA256: $((Get-FileHash -Algorithm SHA256 -LiteralPath "$a25Out/MANIFEST.json").Hash.ToLowerInvariant())"
"Elapsed wall seconds: $($manifest.elapsed_wall_seconds)."
