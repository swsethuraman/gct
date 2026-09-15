# Filesystem packaging and process-exit inspection only; all mathematical runs use b15_bound.py.
$ErrorActionPreference = 'Stop'
$b16Work = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
if ($b16Work -ne 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-12') { throw 'Wrong owned worktree' }
$b16Out = Join-Path $b16Work 'results/b16_12'
$b16Delivery = Join-Path $b16Work 'delivery/b16_12'
$b16Utf8 = [Text.UTF8Encoding]::new($false)
function Write-B16Json($Path, $Value) {
    [IO.File]::WriteAllText($Path, (($Value | ConvertTo-Json -Depth 40) + "`n"), $b16Utf8)
}
$b16Runs = @()
foreach ($b16File in (Get-ChildItem -LiteralPath (Join-Path $b16Work 'results/logs') -File -Filter 'b16_12*_resources.json' | Sort-Object Name)) {
    $b16Rec = Get-Content -LiteralPath $b16File.FullName -Raw | ConvertFrom-Json
    $b16Scope = if ($b16File.Name -eq 'b16_12_runtime_resources.json') { 'INHERITED_LAUNCH_PREFLIGHT' } else { 'CURRENT_SLOT12_RUN' }
    $b16Absent = $null -eq (Get-Process -Id $b16Rec.pid -ErrorAction SilentlyContinue)
    if (-not $b16Absent) { throw ('Recorded numerical PID still present: ' + $b16Rec.pid) }
    if ($b16Rec.exit_code -ne 0) { throw ('Nonzero run: ' + $b16File.Name) }
    if (-not $b16Rec.job_object_enforced) { throw 'Missing Job Object enforcement' }
    if ($b16Scope -eq 'CURRENT_SLOT12_RUN' -and ($b16Rec.memory_cap_mb -ne 512 -or $b16Rec.wall_cap_seconds -ne 60 -or $b16Rec.workers -ne 1 -or $b16Rec.blas_threads -ne 1 -or $b16Rec.wall_seconds -gt 60)) { throw 'Unexpected run cap' }
    $b16Runs += [ordered]@{name=$b16File.Name;scope=$b16Scope;pid=$b16Rec.pid;exit_code=$b16Rec.exit_code;wall_seconds=$b16Rec.wall_seconds;peak_working_set=$b16Rec.process_memory.peak_working_set;peak_job_memory=$b16Rec.job_memory.peak_job_memory;job_object=$b16Rec.job_object_enforced;cap_seconds=$b16Rec.wall_cap_seconds;cap_MiB=$b16Rec.memory_cap_mb;process_absent=$b16Absent;sha256=(Get-FileHash -LiteralPath $b16File.FullName -Algorithm SHA256).Hash.ToLowerInvariant()}
}
$b16Time = [DateTime]::UtcNow.ToString('o')
Write-B16Json (Join-Path $b16Out 'resource_summary.json') ([ordered]@{checked_utc=$b16Time;heavy_lease='Never acquired; no lease to release';runs=$b16Runs;all_recorded_numerical_processes_absent=$true;unrelated_processes_untouched=$true;note='Legacy batch15/B15-12 wrapper labels are unchanged. The inherited runtime receipt is launch preflight.'})
$b16Python = @(Get-Process -Name python -ErrorAction SilentlyContinue | Select-Object Id,ProcessName,WorkingSet64)
Write-B16Json (Join-Path $b16Out 'process_exit_final.json') ([ordered]@{checked_utc=$b16Time;all_receipt_pids_absent=$true;receipt_count=$b16Runs.Count;unrelated_python_processes=$b16Python;processes_terminated_by_slot12=@();heavy_lease='None'})
$b16ManifestPath = Join-Path $b16Delivery 'MANIFEST.json'
$b16OldPath = Join-Path $b16Out 'delivery_milestone_manifest.json'
if ((Test-Path -LiteralPath $b16ManifestPath) -and -not (Test-Path -LiteralPath $b16OldPath)) {
    [IO.File]::WriteAllBytes($b16OldPath, [IO.File]::ReadAllBytes($b16ManifestPath))
}
$b16Files = @()
$b16Files += @(Get-ChildItem -LiteralPath (Join-Path $b16Work 'analysis') -File -Filter 'b16_12*')
$b16Files += @(Get-ChildItem -LiteralPath (Join-Path $b16Work 'docs') -File -Filter 'b16_12*')
$b16Files += @(Get-ChildItem -LiteralPath $b16Out -Recurse -File)
$b16Files += @(Get-ChildItem -LiteralPath $b16Delivery -Recurse -File | Where-Object {$_.FullName -ne $b16ManifestPath})
$b16Files += @(Get-ChildItem -LiteralPath (Join-Path $b16Work 'results/logs') -File -Filter 'b16_12*')
$b16Artifacts = @($b16Files | Sort-Object FullName -Unique | ForEach-Object {
    [ordered]@{path=[IO.Path]::GetRelativePath($b16Work,$_.FullName).Replace('\','/');bytes=$_.Length;sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()}
})
$b16Manifest = [ordered]@{schema='b16_12_complete_review_delivery_v1';slot='12';status='PASS_288_AND_ALL_DELIVERED_02_THROUGH_08';created_utc=$b16Time;frozen_head_inherited='f6e75623b91ac50146baba6278b1abe90a635502';git_operations_performed=$false;report='docs/b16_12_report.md';latest_receiver='results/b16_12/receiver_complete.json';final_audit='results/b16_12/final_audit.json';resource_summary='results/b16_12/resource_summary.json';process_exit='results/b16_12/process_exit_final.json';pending_slots=@();positive_gap_claimed=$false;finite_gap_upper=@(-30,-72,-72,-130);heavy_lease='Never acquired';integrator_notification='UNSENT_AFTER_AUTO_REVIEW_REJECTION';notification_text='delivery/b16_12/INTEGRATOR_NOTICE.md';artifacts=$b16Artifacts;self_hash_excluded=$true}
Write-B16Json $b16ManifestPath $b16Manifest
$b16Check = Get-Content -LiteralPath $b16ManifestPath -Raw | ConvertFrom-Json
foreach ($b16Artifact in $b16Check.artifacts) {
    $b16Path = Join-Path $b16Work $b16Artifact.path
    if ((Get-Item -LiteralPath $b16Path).Length -ne $b16Artifact.bytes -or (Get-FileHash -LiteralPath $b16Path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $b16Artifact.sha256) { throw ('Packaging hash mismatch: ' + $b16Path) }
}
[ordered]@{status='PASS_COMPLETE_DELIVERY_MANIFEST';artifacts=$b16Artifacts.Count;resource_receipts=$b16Runs.Count;all_recorded_processes_absent=$true;manifest_sha256=(Get-FileHash -LiteralPath $b16ManifestPath -Algorithm SHA256).Hash.ToLowerInvariant()} | ConvertTo-Json
