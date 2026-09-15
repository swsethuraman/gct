$ErrorActionPreference = 'Stop'
$projectRoot = 'C:/Users/swami/Projects/gct-gpt'
$workspaceRoot = 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12'
$destinationRoot = Join-Path $workspaceRoot 'results/b17_12/inputs'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$records = [System.Collections.Generic.List[object]]::new()
$seen = @{}
function Save-Input([string]$relative, [string]$role, [string]$expected = '') {
    $relative = $relative.Replace('\','/')
    if ($seen.ContainsKey($relative)) { return }
    $seen[$relative] = $true
    $source = Join-Path $projectRoot $relative
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        $records.Add([ordered]@{path=$relative; role=$role; status='MISSING'; expected_sha256=$expected})
        return
    }
    $destination = [System.IO.Path]::GetFullPath((Join-Path $destinationRoot $relative))
    if (-not $destination.StartsWith([System.IO.Path]::GetFullPath($destinationRoot) + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Snapshot path escaped owned destination' }
    [System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($destination)) | Out-Null
    if (Test-Path -LiteralPath $destination) {
        $bytes = [System.IO.File]::ReadAllBytes($destination)
    } else {
        $bytes = [System.IO.File]::ReadAllBytes($source)
        [System.IO.File]::WriteAllBytes($destination, $bytes)
    }
    $digest = (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant()
    $records.Add([ordered]@{path=$relative; role=$role; status='PINNED'; sha256=$digest; bytes=$bytes.Length; snapshot=('results/b17_12/inputs/' + $relative); observed_utc=[DateTime]::UtcNow.ToString('o'); expected_sha256=$expected; expected_match=$(if ($expected) {$digest -eq $expected} else {$null})})
}
foreach ($relative in @('Batch17/BOARD.md','Batch17/launch/PREFLIGHT.json','Batch17/launch/INPUT_MANIFEST.json','Batch17/DISPATCHED.json','Batch17/LEASES.json','Batch17/COORDINATION.json','Batch17_Planning/SCREEN_REPORT.md','Batch17_Planning/SCREEN_MANIFEST.json','Batch17_Planning/symmetry_dream/COMMON_CONTEXT.md','Batch16/INTAKE.json','Batch16/STOCKTAKE.md','Batch16/CLOSEOUT.json','Batch16/LEASES.json','Batch16/reviews/12_final/ORIGINAL_DELIVERY_MANIFEST.json')) { Save-Input $relative 'launch_or_acceptance' }
$launch = Get-Content -LiteralPath (Join-Path $destinationRoot 'Batch17/launch/INPUT_MANIFEST.json') -Raw | ConvertFrom-Json
foreach ($task in $launch.tasks) { Save-Input ('Batch17/launch/B17-' + $task.slot + '.md') 'dispatch_brief' $task.sha256 }
$screens = Get-Content -LiteralPath (Join-Path $destinationRoot 'Batch17_Planning/SCREEN_MANIFEST.json') -Raw | ConvertFrom-Json
foreach ($entry in $screens.artifacts) { Save-Input ('Batch17_Planning/' + $entry.path) 'screen_certificate_or_code' $entry.sha256 }
foreach ($entry in $screens.inherited_sources) { Save-Input $entry.path 'screen_inherited_source' $entry.sha256 }
foreach ($number in 1..12) {
    $slot = '{0:d2}' -f $number
    $prefix = 'work/batch15_workers/B15-' + $slot
    $manifestName = switch ($slot) { '08' {'ARTIFACT_HASHES.json'} '09' {'delivery_manifest.json'} '10' {'SHA256_MANIFEST.json'} '11' {'DELIVERY_MANIFEST.json'} default {'MANIFEST.json'} }
    $manifestRelative = $prefix + '/delivery/b16_' + $slot + '/' + $manifestName
    Save-Input $manifestRelative 'original_delivery_manifest'
    Save-Input ('Batch16/reviews/' + $slot + '/integrator_review.json') 'integrator_acceptance_receipt'
    Save-Input ($prefix + '/docs/b16_' + $slot + '_report.md') 'original_report'
    $manifest = Get-Content -LiteralPath (Join-Path $destinationRoot $manifestRelative) -Raw | ConvertFrom-Json
    $entries = @($manifest.files) + @($manifest.artifacts) + @($manifest.outputs)
    foreach ($entry in $entries) {
        if ($null -eq $entry -or -not $entry.path) { continue }
        $rel = $entry.path.Replace('\','/')
        if ($rel.StartsWith($projectRoot + '/', [System.StringComparison]::OrdinalIgnoreCase)) { $rel = $rel.Substring($projectRoot.Length + 1) }
        elseif (-not [System.IO.Path]::IsPathRooted($rel)) { $rel = $prefix + '/' + $rel }
        $workerRelative = $rel.Substring($prefix.Length + 1)
        if ($workerRelative -match ('^docs/b16_' + $slot + '.*\.md$') -or $workerRelative -match ('^results/b16_' + $slot + '/[^/]+\.(json|json\.gz)$')) {
            Save-Input $rel 'selected_original_evidence' $entry.sha256
        }
    }
    if ($slot -eq '08') { foreach ($name in @('CLAIMS.json','RESOURCE_SUMMARY.json','INPUT_HASHES.json')) { Save-Input ($prefix + '/delivery/b16_08/' + $name) 'selected_original_evidence' } }
    if ($slot -eq '10') { Save-Input ($prefix + '/delivery/b16_10/docs/b16_10_report.md') 'sealed_original_report' }
    if ($slot -eq '11') { foreach ($name in @('REPORT.md','INPUT_HASHES.json','FINAL_RECEIVER_RESULT.json')) { Save-Input ($prefix + '/delivery/b16_11/' + $name) 'selected_original_evidence' } }
}
foreach ($name in @('b16_12_report.md','b16_12_proof.md','b16_12_receive02.md','b16_12_receive03_07.md','b16_12_receive04_05_06_08.md')) { Save-Input ('Batch16/reviews/12_final/docs/' + $name) 'sealed_review_copy' }
Save-Input 'Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md' 'intake_explicit_review_pointer'
Save-Input 'work/batch15_workers/B15-12/analysis/b15_bound.py' 'inspected_wrapper'
Save-Input 'work/batch15_workers/B15-12/.venv/python.exe' 'existing_interpreter'
foreach ($relative in @('Batch15_Launch/native_20260913/INTAKE.json','work/batch15_workers/B15-06/docs/b15_06_report.md','work/batch15_workers/B15-06/docs/b15_06_proved.md','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/DREAM_REPORT.md','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/integrator_review.json','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/DELIVERY_MANIFEST.json','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/cubic_bound.json')) { Save-Input $relative 'upstream_accepted_premise' }
$ledger = [ordered]@{schema='b17_12_input_inventory_v1'; created_utc=[DateTime]::UtcNow.ToString('o'); project_root=$projectRoot; workspace=$workspaceRoot; scope='Launch/source ledger only. Selected original evidence, not recursive mathematical replay.'; files=@($records)}
[System.IO.File]::WriteAllText((Join-Path $workspaceRoot 'results/b17_12/input_inventory.json'), ($ledger | ConvertTo-Json -Depth 12) + "`n", $utf8)
$parsed = $ledger | ConvertTo-Json -Depth 12 | ConvertFrom-Json
$parsed.files | Group-Object status | Select-Object Name,Count | ConvertTo-Json
$parsed.files | Where-Object { $_.status -eq 'MISSING' -or $_.expected_match -eq $false } | ConvertTo-Json -Depth 5
