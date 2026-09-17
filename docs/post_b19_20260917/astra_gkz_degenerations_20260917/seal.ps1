param([switch]$VerifyOnly)
$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Users\swami\Projects\gct-gpt'
$taskDir = $PSScriptRoot
$taskOriginal = 'C:\Users\swami\Projects\gct'
$taskPaths = @(
 'RUNBOOK.md',
 'CLAUDE_CODE_COMMIT_TASK.md',
 'Claude_Handover_B15_B18\batch19_launch\B19_PREAMBLE.md',
 'Claude_Handover_B15_B18\batch18_launch\B18-02.md',
 'work\claude_transverse_structure_20260916_followup\clarification_20260917\SOURCE_HANDOFF.md',
 'work\claude_transverse_structure_20260916_followup\clarification_20260917\STABILIZER.md',
 'work\claude_transverse_structure_20260916_followup\clarification_20260917\CORRIGENDUM.md',
 'work\claude_transverse_structure_20260916_followup\clarification_20260917\MANIFEST.json',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\REPORT.md',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\MANIFEST.json',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\certificates\n02_definition.json',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\certificates\independence_q3_q7_e_n02.json',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\certificates\transverse_triple_rank3.json',
 'work\claude_source_vectors_20260917\arc_target_dimension_followup\REPORT.md',
 'work\claude_source_vectors_20260917\arc_target_dimension_followup\MANIFEST.json',
 'work\claude_source_vectors_20260917\arc_target_dimension_followup\results\b_L_branching.json',
 'work\batch15_workers\B15-01\docs\b19_01_report.md',
 'work\batch15_workers\B15-02\docs\b17_02_report.md',
 'work\batch15_workers\B15-02\docs\b18_02_report.md',
 'work\batch15_workers\B15-02\analysis\b17_02_verify.py',
 'work\batch15_workers\B15-02\analysis\b18_02_carrier.py',
 'work\batch15_workers\B15-02\analysis\b15_bound.py',
 'work\batch15_workers\B15-02\.venv\python.exe',
 'work\batch15_workers\B15-02\results\b17_02\input_hashes.json',
 'work\batch15_workers\B15-11\docs\b17_11_supplement02.md',
 'work\batch15_workers\B15-01\docs\b18_01_report.md',
 'work\batch15_workers\B15-05\docs\b18_05_report.md',
 'work\claude_singular_locus_audit_20260916\REPORT.md'
) | ForEach-Object { Join-Path $taskRoot $_ }
$taskPaths += @(
 'work\docs\onset_conjecture.md', 'work\docs\PROVED.md',
 'work\docs\delivery_contract.md', 'work\docs\brief_wording.md',
 'astra_delivery_recipe.md'
) | ForEach-Object { Join-Path $taskOriginal $_ }
$taskPaths += 'C:\Users\swami\.codex\attachments\b761ec10-00f9-43e0-a67d-60a9fef2334d\pasted-text.txt'
$taskPaths += 'C:\Users\swami\AppData\Local\Temp\astra_gkz_20260917_literature\segal_2412.14748v1.pdf'
$taskPaths += 'C:\Users\swami\AppData\Local\Temp\astra_gkz_20260917_literature\segal_2412.14748v1.txt'

if ($VerifyOnly) {
    $taskManifest = Get-Content -LiteralPath (Join-Path $taskDir 'MANIFEST.json') -Raw | ConvertFrom-Json
    foreach ($taskEntry in $taskManifest.outputs) {
        $taskActual = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $taskDir $taskEntry.path)).Hash.ToLowerInvariant()
        if ($taskActual -ne $taskEntry.sha256) { throw "Output mismatch: $($taskEntry.path)" }
    }
    $taskPins = Get-Content -LiteralPath (Join-Path $taskDir 'INPUT_PINS.json') -Raw | ConvertFrom-Json
    foreach ($taskEntry in $taskPins.files) {
        $taskActual = (Get-FileHash -Algorithm SHA256 -LiteralPath $taskEntry.path).Hash.ToLowerInvariant()
        if ($taskActual -ne $taskEntry.sha256) { throw "Input mismatch: $($taskEntry.path)" }
    }
    $taskDiskPaths = @(Get-ChildItem -LiteralPath $taskDir -Recurse -File | Where-Object { $_.Name -ne 'MANIFEST.json' } | ForEach-Object { $_.FullName.Substring($taskDir.Length + 1).Replace('\','/') } | Sort-Object)
    $taskListedPaths = @($taskManifest.outputs.path | Sort-Object)
    if (@(Compare-Object $taskDiskPaths $taskListedPaths).Count -ne 0) { throw 'Output inventory mismatch' }
    Write-Output "Verified $($taskManifest.outputs.Count) output hashes and $($taskPins.files.Count) input hashes; no unlisted outputs."
    exit 0
}

$taskExpected = @{}
$taskManifestPaths = @(
 'work\claude_transverse_structure_20260916_followup\clarification_20260917\MANIFEST.json',
 'work\claude_source_vectors_20260917\routeA_signfilter_20260917\MANIFEST.json',
 'work\claude_source_vectors_20260917\arc_target_dimension_followup\MANIFEST.json'
)
foreach ($taskRel in $taskManifestPaths) {
    $taskPath = Join-Path $taskRoot $taskRel
    $taskJson = Get-Content -LiteralPath $taskPath -Raw | ConvertFrom-Json
    foreach ($taskField in $taskJson.PSObject.Properties) {
        if ($taskField.Name -notlike '*sha256') { continue }
        foreach ($taskProp in $taskField.Value.PSObject.Properties) {
            if ($taskProp.Value -notmatch '^[0-9a-f]{64}$') { continue }
            $taskKey = if ($taskProp.Name.StartsWith('work/')) {
                [IO.Path]::GetFullPath((Join-Path $taskRoot $taskProp.Name))
            } else {
                [IO.Path]::GetFullPath((Join-Path (Split-Path $taskPath) $taskProp.Name))
            }
            if ($taskExpected.ContainsKey($taskKey) -and $taskExpected[$taskKey].sha256 -ne $taskProp.Value) {
                throw "Conflicting historical pins: $taskKey"
            }
            $taskExpected[$taskKey] = @{sha256=$taskProp.Value; manifest=$taskRel}
        }
    }
}
$taskFiles = foreach ($taskPath in ($taskPaths | Sort-Object -Unique)) {
    $taskItem = Get-Item -LiteralPath $taskPath
    $taskHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $taskPath).Hash.ToLowerInvariant()
    $taskBinding = $taskExpected[$taskItem.FullName]
    if ($taskBinding -and $taskHash -ne $taskBinding.sha256) { throw "Historical hash mismatch: $taskPath" }
    [ordered]@{path=$taskItem.FullName; bytes=$taskItem.Length; sha256=$taskHash;
        supplied_manifest=if ($taskBinding) {$taskBinding.manifest} else {$null};
        matches_supplied_manifest=if ($taskBinding) {$true} else {$null}}
}
$taskPins = [ordered]@{
    created_utc=(Get-Date).ToUniversalTime().ToString('o'); hash_convention='SHA256_RAW_BYTES';
    status='All referenced supplied-manifest hashes matched'; files=@($taskFiles);
    note='Selected inputs actually used. Historical numerical certificates are adopted, not recomputed. No unfinished direct-relation output was read.'
}
$taskPins | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $taskDir 'INPUT_PINS.json') -Encoding utf8
$taskReceiptPath = 'results/logs/p1_fiveblock_exact_resources.json'
$taskReceipt = Get-Content -LiteralPath (Join-Path $taskDir $taskReceiptPath) -Raw | ConvertFrom-Json
$taskOutputs = @(Get-ChildItem -LiteralPath $taskDir -File -Recurse | Where-Object { $_.Name -ne 'MANIFEST.json' } | Sort-Object FullName | ForEach-Object {
    [ordered]@{path=$_.FullName.Substring($taskDir.Length+1).Replace('\','/'); bytes=$_.Length;
        sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()}
})
$taskManifest = [ordered]@{
    session='astra_gkz_degenerations_20260917'; sealed_utc=(Get-Date).ToUniversalTime().ToString('o');
    outcome='C: all five-block interval and exact-exponent-support tests factor through the old arc C';
    theorem_status='proved globally in REPORT.md sections 7-8, independently of finite pilot controls';
    family='Fixed adapted (a,r,c,S,v) block-scalar torus; nine normal-fan initial-form classes';
    rank_comparison='rank(C,T,N)=rank(C,T) on full M; rank(C,T) not computed';
    positive_multiplicity_obstruction=$false;
    wrapped_pilots_used=1; wrapped_pilots_cap=3; computational_wall_cap_seconds=180;
    wrapper_wall_seconds_total=$taskReceipt.wall_seconds; shell_wall_seconds=0.3436697;
    peak_job_memory_bytes=$taskReceipt.job_memory.peak_job_memory;
    receipt=$taskReceiptPath; exit_code=$taskReceipt.exit_code;
    command="& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-02\.venv\python.exe' -B 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-02\analysis\b15_bound.py' --seconds 60 --memory-mb 512 --name p1_fiveblock_exact --slot astra_gkz_20260917 'pilot_exact.py' 2>&1 | Tee-Object -FilePath 'pilot_console.log'";
    cwd=$taskDir; historical_files_modified=@(); workers_spawned=0; source_vectors_evaluated=0;
    unwrapped_symbolic_pilots=0; git_commands=0; manifest_mismatches=@();
    nonpilot_operations='Document reads/download/extraction, process inspection, file writing, SHA256 and inventory checks only';
    literature_cache='C:\Users\swami\AppData\Local\Temp\astra_gkz_20260917_literature';
    outputs=$taskOutputs; self_hash_policy='MANIFEST.json does not hash itself; all other delivery files are included';
    next_action='Close this five-block weight-search route; no more evaluations or fan enumeration needed'
}
$taskManifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $taskDir 'MANIFEST.json') -Encoding utf8
Write-Output "Sealed $($taskOutputs.Count) outputs and $($taskFiles.Count) input pins."
