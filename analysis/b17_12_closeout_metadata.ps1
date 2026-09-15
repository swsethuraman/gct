param([ValidateSet('Snapshot','Seal')][string]$Mode = 'Snapshot')
$ErrorActionPreference = 'Stop'
$projectRoot = 'C:/Users/swami/Projects/gct-gpt'
$workspaceRoot = 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12'
$ownedRoot = Join-Path $workspaceRoot 'results/b17_12'
$snapshotRoot = Join-Path $ownedRoot 'closeout_inputs'
$encoding = [System.Text.UTF8Encoding]::new($false)
function Write-Json([string]$path, $value) {
    [System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($path)) | Out-Null
    [System.IO.File]::WriteAllText($path, ($value | ConvertTo-Json -Depth 50) + "`n", $encoding)
}
function Hash-File([string]$path) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() }
if ($Mode -eq 'Snapshot') {
    $records = [System.Collections.Generic.List[object]]::new()
    $checks = [System.Collections.Generic.List[object]]::new()
    $index = @{}
    function Save-Input([string]$relative, [string]$role, [string]$expected = '', [string]$authority = '') {
        $relative = $relative.Replace('\','/')
        if (-not $index.ContainsKey($relative)) {
            $source = Join-Path $projectRoot $relative
            $destination = [System.IO.Path]::GetFullPath((Join-Path $snapshotRoot $relative))
            if (-not $destination.StartsWith([System.IO.Path]::GetFullPath($snapshotRoot) + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Unowned snapshot destination' }
            if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
                $records.Add([pscustomobject]@{path=$relative; role=$role; status='MISSING'})
                return
            }
            [System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($destination)) | Out-Null
            if (-not (Test-Path -LiteralPath $destination)) { [System.IO.File]::WriteAllBytes($destination, [System.IO.File]::ReadAllBytes($source)) }
            $record = [pscustomobject]@{path=$relative; role=$role; status='PINNED'; sha256=(Hash-File $destination); bytes=(Get-Item -LiteralPath $destination).Length; snapshot=('results/b17_12/closeout_inputs/' + $relative); observed_utc=[DateTime]::UtcNow.ToString('o')}
            $records.Add($record)
            $index[$relative] = $record
        }
        if ($expected) { $checks.Add([pscustomobject]@{path=$relative; authority=$authority; expected_sha256=$expected; actual_sha256=$index[$relative].sha256; matches=($expected -eq $index[$relative].sha256)}) }
    }
    function Read-Saved([string]$relative) { Get-Content -LiteralPath (Join-Path $snapshotRoot $relative) -Raw | ConvertFrom-Json }
    foreach ($relative in @('Batch17/BOARD.md','Batch17/COORDINATION.json','Batch17/LEASES.json','Batch17/SESSIONS.md','Batch17/DISPATCHED.json','Batch17/CAPELLI_FOLLOWUP.md')) { Save-Input $relative 'current_coordination_context_not_acceptance' }
    foreach ($slot in @('01','02','03','04','05','06','07','08','11')) {
        $prefix = 'work/batch15_workers/B15-' + $slot
        $manifestRelative = $prefix + '/delivery/b17_' + $slot + '/MANIFEST.json'
        Save-Input ($prefix + '/docs/b17_' + $slot + '_report.md') 'original_report_read'
        Save-Input $manifestRelative 'original_delivery_manifest'
        $manifest = Read-Saved $manifestRelative
        $entries = @($manifest.artifacts) + @($manifest.artifact_files) + @($manifest.outputs) + @($manifest.files)
        foreach ($entry in $entries) {
            if ($null -eq $entry -or -not $entry.path) { continue }
            $relative = $entry.path.Replace('\','/')
            if ($relative.StartsWith($projectRoot + '/', [System.StringComparison]::OrdinalIgnoreCase)) { $relative = $relative.Substring($projectRoot.Length + 1) }
            elseif (-not [System.IO.Path]::IsPathRooted($relative)) { $relative = $prefix + '/' + $relative.TrimStart('./') }
            if ($relative.Contains('/inputs/') -or $relative.Contains('/input_snapshots/') -or $relative.Contains('/initial_delivery/')) { continue }
            if ($relative -match ('/(analysis/b17_' + $slot + '[^/]*|docs/b17_' + $slot + '[^/]*|results/b17_' + $slot + '/.*|results/logs/b17_' + $slot + '[^/]*|delivery/b17_' + $slot + '/[^/]*)$')) {
                Save-Input $relative 'producer_artifact_not_executed' $entry.sha256 $manifestRelative
            }
        }
    }
    $reviewPrefix = 'work/batch15_workers/B15-11'
    foreach ($relative in @('docs/b17_11_supplement02.md','results/b17_11/input_hashes.json','results/b17_11/supplement02/input_hashes.json','results/b17_11/supplement02/decisions.json','results/b17_11/supplement02/verification.json','results/logs/b17_11_supplement02_resources.json','delivery/b17_11/supplement02/MANIFEST.json','delivery/b17_11/supplement02/FIRST_STAGE_MANIFEST.json')) { Save-Input ($reviewPrefix + '/' + $relative) 'independent_review_evidence' }
    foreach ($reviewInput in @('results/b17_11/input_hashes.json','results/b17_11/supplement02/input_hashes.json')) {
        $authority = $reviewPrefix + '/' + $reviewInput
        $ledger = Read-Saved $authority
        foreach ($entry in $ledger.files) {
            $relative = $entry.path.Replace('\','/')
            if ($relative.StartsWith($projectRoot + '/', [System.StringComparison]::OrdinalIgnoreCase)) { $relative = $relative.Substring($projectRoot.Length + 1) }
            if ($index.ContainsKey($relative)) { Save-Input $relative 'reviewed_version_binding' $entry.sha256 $authority }
        }
    }
    $supplement = Read-Saved ($reviewPrefix + '/delivery/b17_11/supplement02/MANIFEST.json')
    foreach ($entry in @($supplement.artifacts)) {
        if ($null -eq $entry -or -not $entry.path) { continue }
        $relative = $entry.path.Replace('\','/')
        if ($relative.StartsWith($projectRoot + '/', [System.StringComparison]::OrdinalIgnoreCase)) { $relative = $relative.Substring($projectRoot.Length + 1) }
        elseif (-not [System.IO.Path]::IsPathRooted($relative)) { $relative = $reviewPrefix + '/' + $relative }
        if ($index.ContainsKey($relative)) { Save-Input $relative 'review_supplement_binding' $entry.sha256 ($reviewPrefix + '/delivery/b17_11/supplement02/MANIFEST.json') }
    }
    $extraPrefix = 'work/capelli_cayley_investigation/expanded_repair'
    Save-Input ($extraPrefix + '/artifact_hashes.json') 'supplementary_producer_manifest_not_independently_accepted'
    foreach ($entry in (Read-Saved ($extraPrefix + '/artifact_hashes.json'))) { Save-Input ($extraPrefix + '/' + $entry.name) 'supplementary_producer_artifact_not_executed' $entry.sha256_bytes ($extraPrefix + '/artifact_hashes.json') }
    $missing = @($records | Where-Object status -eq 'MISSING')
    $mismatches = @($checks | Where-Object matches -eq $false)
    Write-Json (Join-Path $ownedRoot 'closeout_input_inventory.json') ([ordered]@{schema='b17_12_closeout_inputs_v1'; created_utc=[DateTime]::UtcNow.ToString('o'); project_root=$projectRoot; files=@($records); binding_checks=@($checks); missing=$missing; mismatches=$mismatches; scope='Raw-byte pinning and selected producer/reviewer bindings only; no scientific execution'; final04_08_review='Not present in the one observed review-directory inventory; not polled or awaited'})
    [pscustomobject]@{input_count=$records.Count; binding_count=$checks.Count; missing=$missing.Count; mismatches=$mismatches.Count} | ConvertTo-Json
    if ($missing.Count -or $mismatches.Count) { $missing; $mismatches }
    exit
}
$inventory = Get-Content -LiteralPath (Join-Path $ownedRoot 'closeout_input_inventory.json') -Raw | ConvertFrom-Json
$ledger = Get-Content -LiteralPath (Join-Path $ownedRoot 'closeout_ledger.json') -Raw | ConvertFrom-Json
$outputRecords = [System.Collections.Generic.List[object]]::new()
$paths = @()
$paths += @(Get-ChildItem -LiteralPath (Join-Path $workspaceRoot 'analysis') -File -Filter 'b17_12*')
$paths += @(Get-ChildItem -LiteralPath (Join-Path $workspaceRoot 'docs') -File -Filter 'b17_12*')
$paths += @(Get-ChildItem -LiteralPath $ownedRoot -Recurse -File)
$paths += @(Get-ChildItem -LiteralPath (Join-Path $workspaceRoot 'results/logs') -File -Filter 'b17_12*')
foreach ($file in $paths) { $relative = $file.FullName.Replace('\','/').Substring($workspaceRoot.Length+1); $outputRecords.Add([pscustomobject]@{path=$relative; bytes=$file.Length; sha256=(Hash-File $file.FullName)}) }
$manifest = [ordered]@{
    schema='b17_12_closure_ready_delivery_v1'; status='COMPLETE_SCOPED_CLOSURE_READY_LEDGER'; sealed_utc=[DateTime]::UtcNow.ToString('o'); workspace=$workspaceRoot;
    report='docs/b17_12_closeout.md'; historical_report='docs/b17_12_report.md'; initial_report_preserved=$true;
    decision='STOP_CURRENT_EVALUATION_BRANCH_NO_FINITE_FAMILY; retain reviewed theory roadmap'; final_batch_acceptance='PENDING_04_08_FINAL_REVIEW_AND_INTEGRATOR_CLOSEOUT';
    accepted_scoped_slots=@('01','02','03','05','06','07'); pending_final_review=@('04','08'); slots09_10='NOT_TRIGGERED'; supplementary_repair='PRODUCER_VERIFIED_NOT_INDEPENDENTLY_ACCEPTED';
    input_inventory='results/b17_12/closeout_input_inventory.json'; inputs=$inventory.files; binding_checks=$inventory.binding_checks;
    initial_input_inventory='results/b17_12/input_inventory.json'; initial_inputs_status='Historical successful file snapshots retained; failed initial Python audit is not a PASS';
    scientific_computations_this_continuation=0; python_invocations_this_continuation=0; heavy_lease_requested_or_held=$false;
    historical_own_run=@{command='.venv/python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_12_verify --slot 12 analysis/b17_12_verify.py'; status='FAILED_METADATA_AUDIT_NOT_RERUN'; reason="KeyError: 'files' while accessing sealed['files']"; receipt='results/logs/b17_12_verify_resources.json'; exit_code=1; wall_seconds=0.08928269997704774; peak_job_bytes=13701120; cap_hit=$false};
    inherited_resources=$ledger.resources; metadata_only=$true; no_new_mathematical_acceptance_by12=$true; remote_source_note='Primary literature statements inherited from pinned reviewed reports; no new remote-paper hash claim';
    unresolved=$ledger.unresolved; final_integration_steps=$ledger.final_integration_steps; constraints=@{agents=0; new_tasks=0; new_worktrees=0; commits=0; push=$false; publication=$false; configuration_changes=$false; external_messages=0; new_git_operations=0};
    output_files=@($outputRecords); self_hash_excluded=$true
}
Write-Json (Join-Path $workspaceRoot 'delivery/b17_12/MANIFEST.json') $manifest
[pscustomobject]@{status=$manifest.status; output_files=$outputRecords.Count; closeout_inputs=$inventory.files.Count; scientific_computations=0} | ConvertTo-Json
