param([ValidateSet('Pin','Verify','Seal')][string]$Mode = 'Verify')
$ErrorActionPreference = 'Stop'
$taskRoot = 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-08'
$projectRoot = 'C:/Users/swami/Projects/gct-gpt'
$resultRoot = Join-Path $taskRoot 'results/b17_08'
$deliveryRoot = Join-Path $taskRoot 'delivery/b17_08'
$utf8 = [System.Text.UTF8Encoding]::new($false)
function Write-Json($path, $value) {
    [System.IO.File]::WriteAllText($path, ($value | ConvertTo-Json -Depth 30) + "`n", $utf8)
}
function Hash-Record($path) {
    $item = Get-Item -LiteralPath $path
    [ordered]@{path=$item.FullName; bytes=$item.Length; sha256=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()}
}
$relativeInputs = @(
    'Batch17/BOARD.md', 'Batch17_Planning/SCREEN_REPORT.md',
    'Batch17_Planning/symmetry_dream/COMMON_CONTEXT.md', 'Batch16/STOCKTAKE.md', 'Batch16/INTAKE.json',
    'Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md',
    'Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/DREAM_REPORT.md',
    'Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/integrator_review.json',
    'work/batch15_workers/B15-11/docs/b17_11_report.md',
    'work/batch15_workers/B15-11/results/b17_11/input_hashes.json',
    'work/batch15_workers/B15-11/delivery/b17_11/MANIFEST.json',
    'work/batch15_workers/B15-01/docs/b16_01_proof.md',
    'work/batch15_workers/B15-01/delivery/b16_01/MANIFEST.json',
    'work/batch15_workers/B15-02/docs/b16_02_proof.md',
    'work/batch15_workers/B15-02/delivery/b16_02/MANIFEST.json',
    'work/batch15_workers/B15-04/docs/b16_04_proof.md',
    'work/batch15_workers/B15-04/delivery/b16_04/MANIFEST.json',
    'work/batch15_workers/B15-06/docs/b16_06_proof.md',
    'work/batch15_workers/B15-06/delivery/b16_06/MANIFEST.json',
    'work/batch15_workers/B15-08/docs/b16_08_proof.md',
    'work/batch15_workers/B15-08/delivery/b16_08/ARTIFACT_HASHES.json',
    'work/batch15_workers/B15-10/docs/b16_10_proof.md',
    'work/batch15_workers/B15-10/delivery/b16_10/SHA256_MANIFEST.json',
    'work/batch15_workers/B15-08/analysis/b15_bound.py',
    'work/batch15_workers/B15-08/.venv/python.exe'
)
foreach ($slot in @('01','02','03','05','06','07')) {
    $relativeInputs += "work/batch15_workers/B15-$slot/docs/b17_${slot}_report.md"
    $relativeInputs += "work/batch15_workers/B15-$slot/delivery/b17_$slot/MANIFEST.json"
}
if ($Mode -eq 'Pin') {
    New-Item -ItemType Directory -Force -Path $resultRoot,$deliveryRoot | Out-Null
    $ledgerPath = Join-Path $resultRoot 'input_hashes.json'
    if (Test-Path -LiteralPath $ledgerPath) { throw 'Input ledger already exists; refuse to repin.' }
    $records = foreach ($relative in $relativeInputs) {
        $source = Join-Path $projectRoot $relative
        $record = Hash-Record $source
        $snapshotRelative = 'delivery/b17_08/inputs/' + $relative
        $snapshot = Join-Path $taskRoot $snapshotRelative
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $snapshot) | Out-Null
        Copy-Item -LiteralPath $source -Destination $snapshot
        if ((Hash-Record $snapshot).sha256 -ne $record.sha256) { throw "Snapshot mismatch: $relative" }
        $record['snapshot'] = $snapshotRelative
        $record
    }
    Write-Json $ledgerPath ([ordered]@{task='B17-08'; created_utc=[DateTime]::UtcNow.ToString('o'); files=@($records)})
    Write-Output "Pinned $($records.Count) inputs. No mathematical computation."
    exit 0
}
$ledger = Get-Content -LiteralPath (Join-Path $resultRoot 'input_hashes.json') -Raw | ConvertFrom-Json
$drift = @()
foreach ($record in $ledger.files) {
    if ((Hash-Record (Join-Path $taskRoot $record.snapshot)).sha256 -ne $record.sha256) { throw "Snapshot corrupted: $($record.snapshot)" }
    if ((Hash-Record $record.path).sha256 -ne $record.sha256) { $drift += $record.path }
}
function Pinned-Path($relative) { Join-Path $taskRoot ('delivery/b17_08/inputs/' + $relative) }
$reviewLedger = Get-Content -LiteralPath (Pinned-Path 'work/batch15_workers/B15-11/results/b17_11/input_hashes.json') -Raw | ConvertFrom-Json
$reviewChecks = foreach ($slot in @('01','03','05','06','07')) {
    $relative = "work/batch15_workers/B15-$slot/docs/b17_${slot}_report.md"
    $source = [System.IO.Path]::GetFullPath((Join-Path $projectRoot $relative))
    $entry = @($reviewLedger.files | Where-Object { [System.IO.Path]::GetFullPath($_.path) -eq $source })
    if ($entry.Count -ne 1) { throw "Missing reviewed report binding: $relative" }
    $actual = (Hash-Record (Pinned-Path $relative)).sha256
    if ($actual -ne $entry[0].sha256) { throw "Reviewed report mismatch: $relative" }
    [ordered]@{slot=$slot; sha256=$actual; matches_reviewed_version=$true}
}
$bindingChecks = foreach ($slot in @('01','02','04','06','08','10')) {
    $base = "work/batch15_workers/B15-$slot/"
    $manifestName = if ($slot -eq '08') { 'ARTIFACT_HASHES.json' } elseif ($slot -eq '10') { 'SHA256_MANIFEST.json' } else { 'MANIFEST.json' }
    $manifest = Get-Content -LiteralPath (Pinned-Path ($base + "delivery/b16_$slot/$manifestName")) -Raw | ConvertFrom-Json
    $entries = @($manifest.artifacts) + @($manifest.files)
    if ($slot -eq '08') { $entries += @($manifest) }
    $proofRelative = "docs/b16_${slot}_proof.md"
    $matched = @($entries | Where-Object { $_.path -and (($_.path -replace '\\','/').EndsWith($proofRelative)) })
    if ($matched.Count -ne 1) { throw "Missing original proof binding: $slot" }
    $actual = (Hash-Record (Pinned-Path ($base + $proofRelative))).sha256
    if ($actual -ne $matched[0].sha256) { throw "Original proof mismatch: $slot" }
    [ordered]@{slot=$slot; proof=$proofRelative; sha256=$actual; matches_original_delivery=$true}
}
$verification = [ordered]@{
    task='B17-08'; checked_utc=[DateTime]::UtcNow.ToString('o'); scope='Metadata verification only; no mathematical replay';
    pinned_inputs=$ledger.files.Count; snapshots_match=$true; current_input_drift=$drift;
    reviewed_report_bindings=@($reviewChecks); original_B16_proof_bindings=@($bindingChecks);
    slot02_status='PROVISIONAL: supplied report and manifest; no independent supplement consumed'
}
if ($Mode -eq 'Seal') {
    Write-Json (Join-Path $resultRoot 'verification.json') $verification
    $artifactPaths = @(
        (Join-Path $taskRoot 'analysis/b17_08_metadata.ps1'),
        (Join-Path $taskRoot 'docs/b17_08_report.md')
    ) + @(Get-ChildItem -LiteralPath $resultRoot -File | ForEach-Object { $_.FullName }) +
        @(Get-ChildItem -LiteralPath (Join-Path $deliveryRoot 'inputs') -File -Recurse | ForEach-Object { $_.FullName })
    $artifacts = @($artifactPaths | Sort-Object -Unique | ForEach-Object { Hash-Record $_ })
    $manifest = [ordered]@{
        schema='b17_08_theory_selection_v1'; task='B17-08'; status='COMPLETE_NO_SUPPORTED_FINITE_CANDIDATE';
        sealed_utc=[DateTime]::UtcNow.ToString('o'); worktree=$taskRoot;
        requested_model='gpt-6-astra'; requested_reasoning='xhigh';
        git_head_read_only='0256ed2561964fe4085ad847518e3fcf85837024';
        report='docs/b17_08_report.md'; nominations=@();
        input_hashes=$ledger; verification=$verification;
        resources=[ordered]@{
            scientific_computations=0; python_invocations=0; numerical_evaluations=0; heavy_lease=$false;
            measured_scientific_seconds=$null; measured_scientific_peak_bytes=$null;
            wrapper_inspected='analysis/b15_bound.py'; interpreter_located='.venv/python.exe';
            authorized_continuation='Theory only'; proposed_finite_calculations=@();
            future_caps=[ordered]@{seconds=60; aggregate_mib=512; processes=1; blas_threads=1; cap_hit='UNCOMPUTED'; larger_lease='Integrator review required'}
        };
        dependencies=[ordered]@{slot02='Provisional pending independent supplement'; slot09='HELD'; slot10='HELD';
            missing='One explicit five-row finite cell with certified a,s,U and forbidden-projection minor b >= max(0,s-U+1), plus actual-padding circuits and a concrete support price'};
        fresh_deductions=@('Five-variable product-map rank equals actual padding multiplicity in length<=5', 'Exact ambient-clipped boundary-loss threshold', 'Polynomial Jflag multiples cannot have five rows', 'Conditional support pricing and capacity gate');
        inherited='Scoped 01/03/05/06/07 review and original B16 evidence; no scientific replay';
        approvals='No escalated action or automatic approval rejection; inherited Git ignore read warning recorded separately';
        artifacts=$artifacts; self_hash_excluded=$true
    }
    Write-Json (Join-Path $deliveryRoot 'MANIFEST.json') $manifest
}
if ($Mode -eq 'Verify' -and (Test-Path -LiteralPath (Join-Path $deliveryRoot 'MANIFEST.json'))) {
    $sealed = Get-Content -LiteralPath (Join-Path $deliveryRoot 'MANIFEST.json') -Raw | ConvertFrom-Json
    foreach ($artifact in $sealed.artifacts) {
        if ((Hash-Record $artifact.path).sha256 -ne $artifact.sha256) { throw "Output hash mismatch: $($artifact.path)" }
    }
    Write-Output "Verified $($sealed.artifacts.Count) sealed output hashes without modifying the delivery."
}
Write-Output "Verified $($ledger.files.Count) snapshots, $($reviewChecks.Count) reviewed report bindings and $($bindingChecks.Count) original proofs; current drift: $($drift.Count). Mode: $Mode."
