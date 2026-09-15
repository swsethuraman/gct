# Metadata only: no mathematical computation, Python execution, or child job.
# Run once before writing the report to pin inputs, and with -Seal afterwards.
param([switch]$Seal)
$ErrorActionPreference = 'Stop'
$b17Workspace = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$b17Expected = 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-03'
if ($b17Workspace.TrimEnd('\') -ne $b17Expected) { throw 'Unexpected worktree' }
$b17Project = 'C:\Users\swami\Projects\gct-gpt'
$b17Output = Join-Path $b17Workspace 'results/b17_03'
$b17Delivery = Join-Path $b17Workspace 'delivery/b17_03'
$b17Utf8 = New-Object System.Text.UTF8Encoding($false)
function Save-Json($Value, $Destination) {
    $b17Absolute = [IO.Path]::GetFullPath($Destination)
    if (-not ($b17Absolute.StartsWith($b17Output + '\') -or $b17Absolute.StartsWith($b17Delivery + '\'))) {
        throw "Output outside assigned directories: $b17Absolute"
    }
    [IO.File]::WriteAllText($b17Absolute, (($Value | ConvertTo-Json -Depth 15) + "`n"), $b17Utf8)
}
function File-Record($Path, $Role) {
    $b17File = Get-Item -LiteralPath $Path
    [ordered]@{path=$b17File.FullName; bytes=$b17File.Length; sha256=(Get-FileHash -LiteralPath $b17File.FullName -Algorithm SHA256).Hash.ToLowerInvariant(); role=$Role}
}
$b17PinPath = Join-Path $b17Output 'input_hashes.json'
if (-not $Seal) {
    if (Test-Path -LiteralPath $b17PinPath) { throw 'Inputs already pinned; refusing to overwrite the baseline' }
    $b17Records = @()
    foreach ($b17Relative in @('Batch17/BOARD.md','Batch17_Planning/SCREEN_REPORT.md','Batch17_Planning/symmetry_dream/COMMON_CONTEXT.md','Batch16/STOCKTAKE.md','Batch16/INTAKE.json','Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md')) {
        $b17Records += File-Record (Join-Path $b17Project $b17Relative) 'required_context_or_intake_review'
    }
    foreach ($b17Relative in @('docs/isotypic_rank.md','docs/b14_05_transport.md','docs/b15_03_proved.md','docs/session_29.md','docs/visible_ideals.md','docs/l5_containment.md','analysis/b15_bound.py')) {
        $b17Records += File-Record (Join-Path $b17Workspace $b17Relative) 'local_original_source_or_inspected_wrapper'
    }
    foreach ($b17Relative in @('B15-01/docs/b16_01_report.md','B15-01/docs/b16_01_proof.md','B15-01/delivery/b16_01/MANIFEST.json','B15-01/results/b16_01/input_hashes.json','B15-12/docs/b15_12_proved.md')) {
        $b17Records += File-Record (Join-Path (Join-Path $b17Project 'work/batch15_workers') $b17Relative) 'original_evidence_read_only'
    }
    $b17Records += File-Record (Join-Path $b17Workspace '.venv/python.exe') 'existing_interpreter_available_but_not_executed'
    $b17Records += File-Record (Join-Path $b17Delivery 'sources/primary_source_note.json') 'primary_source_reading_note_not_remote_pdf'
    Save-Json ([ordered]@{pinned_utc=[DateTime]::UtcNow.ToString('o'); algorithm='SHA256'; hash_scope='Exact local bytes; the remote PDF is unavailable and is not assigned a hash.'; files=$b17Records}) $b17PinPath
    Write-Output "Pinned $($b17Records.Count) inputs."
    exit
}
$b17Pins = Get-Content -Raw -LiteralPath $b17PinPath | ConvertFrom-Json
$b17Mismatches = @()
foreach ($b17Input in $b17Pins.files) {
    $b17Current = (Get-FileHash -LiteralPath $b17Input.path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($b17Current -ne $b17Input.sha256) { $b17Mismatches += $b17Input.path }
}
if ($b17Mismatches.Count) { throw "Inputs changed after pinning: $($b17Mismatches -join ', ')" }
# Check original report/proof byte bindings against their accepted delivery.
$b17Original = Get-Content -Raw -LiteralPath (Join-Path $b17Project 'work/batch15_workers/B15-01/delivery/b16_01/MANIFEST.json') | ConvertFrom-Json
$b17Bindings = @()
foreach ($b17Name in @('b16_01_report.md','b16_01_proof.md')) {
    $b17Binding = @($b17Original.files | Where-Object { [IO.Path]::GetFileName($_.path) -eq $b17Name })
    if ($b17Binding.Count -ne 1) { throw "Expected one original binding for $b17Name" }
    $b17Actual = (Get-FileHash -LiteralPath $b17Binding[0].path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($b17Actual -ne $b17Binding[0].sha256) { throw "Original delivery hash mismatch: $b17Name" }
    $b17Bindings += [ordered]@{path=$b17Binding[0].path; sha256=$b17Actual; match=$true}
}
Save-Json ([ordered]@{status='PASS_METADATA_ONLY'; checked_utc=[DateTime]::UtcNow.ToString('o'); input_hashes_rechecked=$b17Pins.files.Count; mismatches=@(); original_delivery_bindings=$b17Bindings; mathematical_replays=0; external_independent_review=$false}) (Join-Path $b17Output 'verification.json')
$b17Artifacts = @()
foreach ($b17Relative in @('docs/b17_03_report.md','analysis/b17_03_metadata.ps1','results/b17_03/input_hashes.json','results/b17_03/verification.json','results/b17_03/blocked_actions.json','delivery/b17_03/sources/primary_source_note.json')) {
    $b17Artifacts += File-Record (Join-Path $b17Workspace $b17Relative) 'delivery_artifact'
}
$b17Wrapper = @($b17Pins.files | Where-Object { $_.path -like '*\analysis\b15_bound.py' })[0]
$b17Interpreter = @($b17Pins.files | Where-Object { $_.role -eq 'existing_interpreter_available_but_not_executed' })[0]
$b17Manifest = [ordered]@{
    task='B17-03'; status='COMPLETE_SOURCE_GROUNDED_DEDUCTION_PENDING_INDEPENDENT_REVIEW'; created_utc=[DateTime]::UtcNow.ToString('o'); workspace=$b17Workspace
    report='docs/b17_03_report.md'; result='For every d >= 0 and partition lambda of 4d with length <= 4, m_pad(d,lambda) <= m_det(d,lambda), for independent z*per3 versus det4 in GL16.'
    convention='Ordinary coefficient functionals c_alpha(F)=[x^alpha]F; positive weights; E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j) if alpha_j>0, else 0.'
    fresh=@('Coefficient-action and quartic length-restriction proof','Polynomial extension from smooth cubic surfaces to arbitrary cubic cores','Restricted-variety inclusion and same-cell kernel inclusion at every degree','Elementary support-ten corollary')
    inherited=@('Beauville Corollary 6.4, directly read as a primary literature theorem','Characteristic-zero complete reducibility','Batch16 numerical exclusions are contextual only and not premises of the new theorem')
    review='New deduction for integrator/reviewer acceptance, not a previously replayed certificate or literature priority claim.'
    resources=[ordered]@{mode='theory_and_literature_only'; mathematical_computations=0; python_invocations=0; heavy_lease='none'; larger_lease_requested=$false; optional_computation_cap_seconds=60; optional_computation_cap_mib=512; permitted_processes=1; permitted_blas_threads=1; measured_mathematical_runtime_seconds=0; mathematical_peak_memory_bytes=$null; cap_hit=$false; inspected_wrapper=$b17Wrapper; existing_unused_interpreter=$b17Interpreter; metadata_operations='PowerShell read/hash/JSON only; no symbolic expansion, rank evaluation, numerical job, or subprocess parallelism'; executable_mathematical_verifier='Not required: no computed premise. Full proof is in the report.'}
    constraints=[ordered]@{agents_spawned=0; tasks_created=0; worktrees_created=0; commits=0; pushes=0; publications=0; git_operations=0; ownership_trust_changes=0; sandbox_changes=0; closed_batch_outputs_modified=$false; common_coordination_files_modified=$false}
    blocked_actions='results/b17_03/blocked_actions.json'; full_remote_pdf_hash_available=$false
    inputs=$b17Pins.files; artifacts=$b17Artifacts; manifest_self_hash='Intentionally omitted to avoid self-reference.'
}
Save-Json $b17Manifest (Join-Path $b17Delivery 'MANIFEST.json')
Write-Output "Sealed manifest: $($b17Pins.files.Count) unchanged input hashes, $($b17Bindings.Count) original delivery bindings, $($b17Artifacts.Count) artifact hashes. No mathematical computation."
