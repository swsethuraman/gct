param([string]$ProjectRoot = 'C:/Users/swami/Projects/gct-gpt')
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath($ProjectRoot)
$owned = Join-Path $root 'work/batch15_workers/B15-11'
$out = Join-Path $owned 'results/b16_11'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$manifestPath = Join-Path $root 'Batch16/launch/INPUT_MANIFEST.json'
$manifest = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
$started = [DateTime]::UtcNow.ToString('o')
$clock = [Diagnostics.Stopwatch]::StartNew()
$observations = @()
foreach ($w in $manifest.worktrees) {
    # Read-only Git, one invocation at a time; no configuration override.
    $head = & git -C $w.worktree rev-parse HEAD
    if ($LASTEXITCODE -ne 0) { throw "HEAD read failed for slot $($w.slot)" }
    $branch = & git -C $w.worktree symbolic-ref --short HEAD
    if ($LASTEXITCODE -ne 0) { throw "branch read failed for slot $($w.slot)" }
    $frozenTree = & git -C $w.worktree rev-parse "$($w.head)^{tree}"
    if ($LASTEXITCODE -ne 0) { throw "frozen tree read failed for slot $($w.slot)" }
    $type = & git -C $w.worktree cat-file -t $w.head
    if ($LASTEXITCODE -ne 0) { throw "frozen object read failed for slot $($w.slot)" }
    $observations += [pscustomobject]@{
        slot=$w.slot; observed_head="$head"; observed_branch="$branch"
        frozen_head=$w.head; frozen_tree="$frozenTree"; frozen_object_type="$type"
        head_matches=("$head" -eq $w.head); branch_matches=("$branch" -eq $w.branch)
        tree_matches=("$frozenTree" -eq $w.tree)
    }
}
$bindings = @()
$sources = @{
    '01'=@('analysis/b15_01_verify.py','tools/verify/b15_01_ci159.py','docs/b15_01_report.md')
    '05'=@('docs/b15_05_report.md','docs/b15_05_proved.md')
    '06'=@('docs/b15_06_report.md','docs/b15_06_proved.md')
    '08'=@('docs/b15_08_report.md','docs/b15_08_proved.md','analysis/b15_08_witness.py')
    '11'=@('docs/b15_11_report.md','analysis/b15_11_memory.py','analysis/b15_bound.py')
}
foreach ($slot in ($sources.Keys | Sort-Object)) {
    $w = $manifest.worktrees | Where-Object { $_.slot -eq $slot }
    foreach ($relative in $sources[$slot]) {
        $treeLine = & git -C $w.worktree ls-tree $w.head -- $relative
        if ($LASTEXITCODE -ne 0) { throw "source binding read failed: $slot $relative" }
        $bindings += [pscustomobject]@{
            slot=$slot; path=$relative; frozen_head=$w.head; ls_tree="$treeLine"
            exists=(Test-Path -LiteralPath (Join-Path $w.worktree $relative) -PathType Leaf)
        }
    }
}
$pythonProcesses = @(Get-Process -Name python,pythonw -ErrorAction SilentlyContinue |
    Select-Object Id,ProcessName,Path,StartTime)
$prior = Get-Content -Raw -LiteralPath (Join-Path $owned 'results/logs/b16_11_runtime_resources.json') | ConvertFrom-Json
$clock.Stop()
$receipt = [ordered]@{
    schema='b16-11-git-audit/1'; started_utc=$started; finished_utc=[DateTime]::UtcNow.ToString('o')
    manifest_sha256=(Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLower()
    worktrees=$observations; source_bindings=$bindings; metadata_wall_seconds=$clock.Elapsed.TotalSeconds
    scope='Read-only object/ref checks; no bundle replay, mathematics, commit, staging, or configuration change.'
    process_inspection=@{method='Get-Process'; prior_slot11_pid=$prior.pid; prior_slot11_pid_present=($prior.pid -in $pythonProcesses.Id); python_processes=$pythonProcesses; limitation='CIM command-line query was denied; no command-line attribution for unrelated Python processes.'}
}
$receipt | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $out 'git_audit.json') -Encoding utf8
$observations | Format-Table slot,head_matches,branch_matches,tree_matches
Write-Output "Read-only Git receipt saved; $($clock.Elapsed.TotalSeconds) seconds."
