$ErrorActionPreference='Stop'
$repo='C:/Users/swami/Projects/gct-gpt/work/batch15'
$packet=Join-Path $repo 'results/a25_05'
$utf8=New-Object Text.UTF8Encoding($false)
function Write-Json([string]$name,$obj) { [IO.File]::WriteAllText((Join-Path $packet $name),(($obj|ConvertTo-Json -Depth 12).Replace("`r`n","`n"))+"`n",$utf8) }
function File-Record([string]$rel) {
  $abs=Join-Path $repo $rel; $f=Get-Item -LiteralPath $abs
  [ordered]@{path=$rel;bytes=$f.Length;sha256=(Get-FileHash -LiteralPath $abs -Algorithm SHA256).Hash.ToLowerInvariant();state='UNCOMMITTED / NOT RELEASED'}
}
$head=(& git -C $repo rev-parse HEAD).Trim(); $branch=(& git -C $repo branch --show-current).Trim()
if($head -ne '82633a60893236fab4fbc317df416e1b8a349005' -or $branch -ne 'batch15-launch'){throw 'Repository identity changed; preserve work and review before sealing.'}
$fixed=@('docs/a25_05_report.md','analysis/a25_05_admin.ps1','analysis/a25_05_seal.ps1')
$extra=@('results/a25_05/ADD_LIST.txt','results/a25_05/ADMIN_VERIFICATION.json','results/a25_05/MANIFEST.json','results/a25_05/MANIFEST_RECEIPT.json')
$found=@(Get-ChildItem -LiteralPath $packet -File | ForEach-Object {'results/a25_05/'+$_.Name})
$all=@($fixed+$found+$extra | Sort-Object -Unique)
foreach($rel in $all) { if($rel -notmatch '^(docs/a25_05_report\.md|analysis/a25_05_[^/]+|results/a25_05/[^/]+)$'){throw ('Out-of-scope delivery path '+$rel)} }
[IO.File]::WriteAllText((Join-Path $packet 'ADD_LIST.txt'),($all -join "`n")+"`n",$utf8)
$checks=@()
foreach($rel in $all) {
  if($rel -match '/(ADMIN_VERIFICATION|MANIFEST|MANIFEST_RECEIPT)\.json$'){continue}
  $abs=Join-Path $repo $rel
  $raw=(& git -C $repo hash-object --no-filters -- $abs).Trim()
  $filtered=(& git -C $repo hash-object --path=$rel -- $abs).Trim()
  $checks += [ordered]@{path=$rel;raw_blob=$raw;filtered_blob=$filtered;byte_preserving_under_current_filters=($raw -eq $filtered)}
}
$status=@(& git -C $repo status --short --untracked-files=normal)
$tracked=@(& git -C $repo diff --name-only)
Write-Json 'ADMIN_VERIFICATION.json' ([ordered]@{utc=[DateTime]::UtcNow.ToString('o');status='UNCOMMITTED administrative verification, not mathematical evidence';head=$head;branch=$branch;tracked_diff_paths=$tracked;status_lines=$status;own_raw_filtered_checks=$checks;git_write_performed=$false;note='Git warned that the user global ignore file was unreadable; repository queries succeeded. No trust/ownership change.'})
$payload=@($all | Where-Object {$_ -notmatch '/(MANIFEST|MANIFEST_RECEIPT)\.json$'} | ForEach-Object {File-Record $_})
$manifest=[ordered]@{
  schema='a25_05.local_packet.v1';slot='A25-05';outcome=3;status='LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED';claim_status='PROVED structural lemmas, producer-only; projected actual-padding containment OPEN';repository=$repo;branch=$branch;baseline_head=$head;delivery_commit=$null;
  first_recorded_intake_utc='2026-09-21T04:15:25Z';mechanism_frozen_by_utc='2026-09-21T04:17:54Z';research_stopped_utc='2026-09-21T11:52:37Z';sealed_utc=[DateTime]::UtcNow.ToString('o');theory_ceiling_minutes=90;theory_budget_compliance='UNVERIFIED: uninstrumented long interval; observed wall span exceeds ceiling; disclosed timing-control defect';observed_intake_to_stop='7h37m12s';
  mathematical_pilots=0;mathematical_computational_seconds=0;mathematical_peak_memory=$null;compute_lease_acquired=$false;additional_agents_or_tasks=0;tool_memory_created=$false;tool_memory_consumed=$false;
  evidence='READ plus hand derivation; administrative hash checks; no computational replay/evaluator';optional_dependencies=@('C_PER: committed B13-07 rank-35 permanent certificate, ADOPTED/READ not replayed','C_DUBE: primary Corollary 8.3 statement, ADOPTED for optional universal finite cap');
  result='Targets 42/54/65; actual-image determinant upper bound 50; exact fixed-factor padding kernels; product projections 35/38/39; at most four generic product completions; explicit actual-padding determinant completion; five-center 33-to-48 map versus four affine 22-planes; old triangular differential rank <=39 at three centers';
  limitations=@('No all-padding containment or separator','No m=3 dominance theorem or exact higher-center determinant rank','No equation or actual-padding nonzero evaluation of an equation','No multiplicity gap or asymptotic bound','Independent review and byte-preserving committed delivery pending','90-minute substantive-theory compliance not verified');
  next_certificate='Exact closed-image ideal/pullback comparison specified in NEXT_CERTIFICATE.md; no affordable pilot identified';source_bindings='results/a25_05/SOURCE_BINDINGS.json';delivery_list='results/a25_05/ADD_LIST.txt';artifacts=$payload;excluded_from_hash_graph=@('MANIFEST.json itself','MANIFEST_RECEIPT.json, which hashes the manifest after sealing')
}
Write-Json 'MANIFEST.json' $manifest
Write-Json 'MANIFEST_RECEIPT.json' ([ordered]@{utc=[DateTime]::UtcNow.ToString('o');state='UNCOMMITTED / NOT RELEASED';manifest=(File-Record 'results/a25_05/MANIFEST.json');delivery_commit=$null;note='Administrative local seal, not independent acceptance.'})
Write-Output ('Sealed '+$payload.Count+' payload files; '+$all.Count+' delivery paths.')
Write-Output ((File-Record 'results/a25_05/MANIFEST.json')|ConvertTo-Json)
