$ErrorActionPreference='Stop'
$taskRoot=Split-Path -Parent $PSScriptRoot
$taskProject='C:/Users/swami/Projects/gct-gpt'
$taskOutput=Join-Path $taskRoot 'results/b16_03'
$taskDelivery=Join-Path $taskRoot 'delivery/b16_03'
$taskIntake=Join-Path $taskProject 'Batch15_Launch/native_20260913'
$taskHessian=Join-Path $taskIntake 'reviews_filesystem/Hessian11_1631'
$taskCensusPath=Join-Path $taskProject 'work/batch15_workers/B15-02/results/b16_02/census.json'
$taskCensus=Get-Content -LiteralPath $taskCensusPath -Raw|ConvertFrom-Json
$taskAcceptancePath=Join-Path $taskProject 'Batch16/reviews/02/integrator_review.json'
$taskAcceptance=Get-Content -LiteralPath $taskAcceptancePath -Raw|ConvertFrom-Json
if($taskAcceptance.status -ne 'PASS_INDEPENDENT_INTEGRATOR_REVIEW' -or $taskAcceptance.counts[0] -ne 189){throw 'Slot02 acceptance mismatch'}
$taskCell=@($taskCensus.rows|Where-Object degree -eq 23)[0]
if($taskCell.a -ne 189){throw 'Unexpected slot02 cell; assess the new input before packaging'}
$taskComparison=[ordered]@{
    status='EXCLUSION_USING_ACCEPTED_SLOT02_COUNT_AND_ACCEPTED_B15_BOUNDS'
    degree=23;lambda=@(61,15,2,2,2,2,2,2,2,2);a=$taskCell.a
    ambient_count_independently_recomputed_by_03=$false
    ambient_input_path=$taskCensusPath
    ambient_input_sha256=(Get-FileHash -LiteralPath $taskCensusPath -Algorithm SHA256).Hash.ToLower()
    ambient_acceptance_path=$taskAcceptancePath
    ambient_acceptance_sha256=(Get-FileHash -LiteralPath $taskAcceptancePath -Algorithm SHA256).Hash.ToLower()
    ambient_count_independently_accepted_by_integrator=$true
    padding_coordinate_upper=158;determinant_ideal_upper=11
    padded_ideal_lower=31;determinant_coordinate_lower=178;D_upper=-20
    fresh_equation_floor=1;fresh_padding_coordinate_floor=1
    proof='Finite chart injection followed by s2^2 injects degree23 determinant ideals into stable tail19 ideal; stable429-418=11. Source158 bounds image from above. D<=11-(189-158)=-20.'
    next_sufficient_witness='This cell is excluded using accepted inputs. Positive gap requires another nonexcluded finite cell with q+r>a.'
}
$taskComparison|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $taskOutput 'finite_comparison.json') -Encoding utf8

$taskInputs=@(
    (Join-Path $taskProject 'Batch16/BOARD.md'),
    (Join-Path $taskProject 'Batch16/launch/INPUT_MANIFEST.json'),
    (Join-Path $taskProject 'Batch16/launch/B16-03.md'),
    (Join-Path $taskProject 'Batch16/launch/runtime_03.json'),
    (Join-Path $taskProject 'Batch16/launch/dispatch_02.json'),
    (Join-Path $taskIntake 'INTAKE.json'),
    (Join-Path $taskHessian 'REPORT.md'),
    (Join-Path $taskHessian 'verify_small.py'),
    (Join-Path $taskHessian 'integrator_review.json'),
    (Join-Path $taskHessian 'input_receipt.json'),
    (Join-Path $taskHessian 'MANIFEST.json'),
    (Join-Path $taskIntake 'reviews_filesystem/Dream_Upper288/integrator_review.json'),
    (Join-Path $taskIntake 'reviews_filesystem/Dream_Upper288/DREAM_REPORT.md'),
    (Join-Path $taskIntake 'equation_review/astra/REVIEW.md'),
    (Join-Path $taskIntake 'equation_review/astra/hessian_relations.py'),
    (Join-Path $taskIntake 'equation_review/padding_test/REPORT.md'),
    (Join-Path $taskProject 'work/batch15_workers/B15-05/docs/b15_05_proved.md'),
    (Join-Path $taskProject 'work/batch15_workers/B15-05/docs/b15_05_report.md'),
    (Join-Path $taskProject 'work/batch15_workers/B15-02/analysis/b16_02_census.py'),
    $taskCensusPath,
    $taskAcceptancePath,
    (Join-Path $taskProject 'work/batch15_workers/B15-02/results/b16_02/controls.json'),
    (Join-Path $taskRoot 'analysis/b15_bound.py'),
    (Join-Path $taskRoot '.venv/python.exe'),
    (Join-Path $taskRoot '.git'),
    (Join-Path $taskRoot 'results/logs/b16_03_runtime_resources.json')
)
$taskRecords=@(foreach($taskInput in $taskInputs){
    $taskFile=Get-Item -LiteralPath $taskInput -Force
    [ordered]@{path=$taskFile.FullName;bytes=$taskFile.Length;sha256=(Get-FileHash -LiteralPath $taskInput -Algorithm SHA256).Hash.ToLower();convention='RAW_FILE_BYTES'}
})
$taskRuntimeFiles=@(
    (Get-Item -LiteralPath (Join-Path $taskRoot '.venv/python312.dll')),
    (Get-Item -LiteralPath (Join-Path $taskRoot '.venv/python3.dll'))
)
$taskRuntimeFiles+=@(Get-ChildItem -LiteralPath (Join-Path $taskRoot '.venv/Lib/site-packages/flint') -Recurse -File|Where-Object {$_.Extension -in @('.py','.pyd','.dll') -and $_.FullName -notmatch '[\\/]test[\\/]'} )
$taskRuntimeFiles+=@(Get-ChildItem -Path (Join-Path $taskRoot '.venv/Lib/site-packages/python_flint*') -Directory|ForEach-Object { Get-ChildItem -LiteralPath $_.FullName -Recurse -File|Where-Object {$_.Extension -eq '.dll' -or $_.Name -eq 'METADATA'} })
$taskRuntimeRecords=@(foreach($taskFile in $taskRuntimeFiles){
    [ordered]@{path=$taskFile.FullName;bytes=$taskFile.Length;sha256=(Get-FileHash -LiteralPath $taskFile.FullName -Algorithm SHA256).Hash.ToLower();role='LOCAL_RUNTIME_BINARY_OR_FLINT_MODULE'}
})
$taskFrozen=Get-Content -LiteralPath (Join-Path $taskProject 'Batch16/launch/INPUT_MANIFEST.json') -Raw|ConvertFrom-Json
$taskFrozenChecks=@(foreach($taskInput in $taskFrozen.inputs){
    $taskHash=(Get-FileHash -LiteralPath $taskInput.path -Algorithm SHA256).Hash.ToLower()
    if($taskHash -ne $taskInput.sha256){throw "Frozen launch input hash mismatch: $($taskInput.path)"}
    [ordered]@{path=$taskInput.path;sha256=$taskHash;matches_frozen_launch=$true;role='FROZEN_MANIFEST_INTEGRITY_CHECK'}
})
[ordered]@{
    status='RAW_SHA256_INPUT_BINDING';checked_utc=[DateTime]::UtcNow.ToString('o')
    frozen_worktree_head='fde81352a5868a1d152a73716f47ecd4b285adbe'
    git_binding='HEAD confirmed read-only; no Git mutation or unified merged base claimed'
    inputs=$taskRecords;frozen_manifest_integrity_checks=$taskFrozenChecks
    runtime_inventory=$taskRuntimeRecords;runtime_scope='Python engine and installed flint modules/bundled DLLs; system OS libraries and standard library are not a vendored dependency snapshot'
    saved_B15_raw_Hessian_coefficients_used=$false
    arithmetic_input='Deterministic new maps and literal universal recipes in the B16 source; no imported B15 evaluator'
}|ConvertTo-Json -Depth 10|Set-Content -LiteralPath (Join-Path $taskOutput 'input_hashes.json') -Encoding utf8

$taskResourceFiles=@(Get-ChildItem -LiteralPath (Join-Path $taskRoot 'results/logs') -Filter 'b16_03*_resources.json'|Where-Object Name -ne 'b16_03_runtime_resources.json')
$taskResources=@(foreach($taskFile in $taskResourceFiles){
    $taskData=Get-Content -LiteralPath $taskFile.FullName -Raw|ConvertFrom-Json
    [ordered]@{file=$taskFile.FullName;sha256=(Get-FileHash -LiteralPath $taskFile.FullName -Algorithm SHA256).Hash.ToLower();receipt=$taskData}
})
[ordered]@{batch=16;slot='03';wrapper_retains_B15_labels=$true;runs=$taskResources}|ConvertTo-Json -Depth 12|Set-Content -LiteralPath (Join-Path $taskOutput 'resource_summary.json') -Encoding utf8
$taskProcessChecks=@(foreach($taskRecord in $taskResources){
    $taskRunning=Get-Process -Id $taskRecord.receipt.pid -ErrorAction SilentlyContinue
    if($null -ne $taskRunning){throw "Owned numerical PID still exists: $($taskRecord.receipt.pid)"}
    [ordered]@{pid=$taskRecord.receipt.pid;process_present=$false;exit_code=$taskRecord.receipt.exit_code}
})
[ordered]@{status='ALL_OWNED_NUMERICAL_PROCESSES_EXITED';heavy_lease='NEVER_ACQUIRED_NONE_HELD';release_complete=$true;checked_utc=[DateTime]::UtcNow.ToString('o');process_checks=$taskProcessChecks;note='No heavy lease needed. Job Object memory/deadlines enforced for every numerical run.'}|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $taskOutput 'lease_release.json') -Encoding utf8

foreach($taskSubdir in @('analysis','docs','results/b16_03','results/logs')){
    New-Item -ItemType Directory -Force -Path (Join-Path $taskDelivery $taskSubdir)|Out-Null
}
foreach($taskName in @('b16_03_equation.py','b16_03_receiver.py','b16_03_package.ps1','b15_bound.py')){
    Copy-Item -LiteralPath (Join-Path $taskRoot "analysis/$taskName") -Destination (Join-Path $taskDelivery "analysis/$taskName") -Force
}
foreach($taskName in @('b16_03_report.md','b16_03_proof.md')){
    Copy-Item -LiteralPath (Join-Path $taskRoot "docs/$taskName") -Destination (Join-Path $taskDelivery "docs/$taskName") -Force
}
Get-ChildItem -LiteralPath $taskOutput -File|Copy-Item -Destination (Join-Path $taskDelivery 'results/b16_03') -Force
$taskResourceFiles|Copy-Item -Destination (Join-Path $taskDelivery 'results/logs') -Force
$taskPackageManifest=@(Get-ChildItem -LiteralPath $taskDelivery -Recurse -File|Where-Object Name -ne 'MANIFEST.json'|ForEach-Object{
    [ordered]@{path=[IO.Path]::GetRelativePath($taskDelivery,$_.FullName).Replace('\','/');bytes=$_.Length;sha256=(Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower()}
})
[ordered]@{status='FILESYSTEM_DELIVERY_NO_GIT_MUTATION';created_utc=[DateTime]::UtcNow.ToString('o');slot='03';files=$taskPackageManifest}|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $taskDelivery 'MANIFEST.json') -Encoding utf8
Write-Output ([ordered]@{delivery=$taskDelivery;files=$taskPackageManifest.Count;input_count=$taskRecords.Count;finite_D_upper=-20;all_owned_numerical_processes_exited=$true}|ConvertTo-Json -Compress)
