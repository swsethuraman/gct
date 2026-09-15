param([switch]$Seal)
$ErrorActionPreference='Stop'
$wt=Split-Path $PSScriptRoot -Parent
$workers=Split-Path $wt -Parent
$project=[IO.Path]::GetFullPath((Join-Path $wt '../../..'))
$out=Join-Path $wt 'results/b17_11/supplement04_08'
$delivery=Join-Path $wt 'delivery/b17_11/supplement04_08'
$mainManifest=Join-Path $wt 'delivery/b17_11/MANIFEST.json'
$archive=Join-Path $delivery 'PREVIOUS_MANIFEST.json'
New-Item -ItemType Directory -Force -Path $out,$delivery,(Join-Path $delivery 'inputs') | Out-Null
function Hash($p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLowerInvariant() }
function Rec($p) { $i=Get-Item -LiteralPath $p; [ordered]@{path=$i.FullName;bytes=$i.Length;sha256=(Hash $p)} }
function Prior-Checks($prior) {
    $count=0
    foreach ($e in $prior.artifacts) {
        if ((Hash $e.path) -ne $e.sha256) { throw ('First-stage changed '+$e.path) }; $count++
    }
    foreach ($s in $prior.supplements) {
        foreach ($e in $s.artifacts) {
            if ((Hash $e.path) -ne $e.sha256) { throw ('Earlier supplement changed '+$e.path) }; $count++
        }
        if ((Hash $s.manifest_file.path) -ne $s.manifest_file.sha256) { throw 'Earlier supplement manifest changed' }; $count++
    }
    return $count
}
if (-not $Seal) {
    if (Test-Path -LiteralPath $archive) { throw 'Previous-manifest archive already exists; preserve it' }
    Copy-Item -LiteralPath $mainManifest -Destination $archive
    $prior=Get-Content -Raw -LiteralPath $archive | ConvertFrom-Json
    $preserved=Prior-Checks $prior
    $paths=@($archive,(Join-Path $wt 'analysis/b15_bound.py'),(Join-Path $wt '.venv/python.exe'),
      (Join-Path $wt 'analysis/b17_11_supplement04_08_verify.py'),
      (Join-Path $wt 'docs/b17_11_report.md'),(Join-Path $wt 'docs/b17_11_supplement02.md'),
      (Join-Path $wt 'results/b17_11/input_hashes.json'),
      (Join-Path $wt 'results/b17_11/supplement02/input_hashes.json'),
      (Join-Path $wt 'delivery/b17_11/supplement02/MANIFEST.json'))
    foreach ($rel in @('Batch17/BOARD.md','Batch17_Planning/SCREEN_REPORT.md',
       'Batch17_Planning/symmetry_dream/COMMON_CONTEXT.md','Batch16/STOCKTAKE.md','Batch16/INTAKE.json',
       'Batch16/claude_review/exact_ideals.json',
       'Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md',
       'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md',
       'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py',
       'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/small_evidence.json')) { $paths+=Join-Path $project $rel }
    foreach ($rel in @('docs/b17_04_report.md','docs/b17_04_preflight.md','docs/b17_04_retry_authorization.md',
       'analysis/b17_04_verify_next.py','delivery/b17_04/MANIFEST.json',
       'results/b17_04/basis_match.json','results/b17_04/Euler_relations.json',
       'results/b17_04/padding_points.json','results/b17_04/restriction.json',
       'results/b17_04/kernel_target.json','results/b17_04/verification.json',
       'results/b17_04/input_hashes.json','results/b17_04/status.json',
       'results/logs/b17_04_retry_20260914_01_resources.json',
       'docs/b16_04_proof.md','delivery/b16_04/MANIFEST.json')) { $paths+=Join-Path $workers ('B15-04/'+$rel) }
    foreach ($rel in @('docs/b17_08_report.md','analysis/b17_08_metadata.ps1','delivery/b17_08/MANIFEST.json',
       'results/b17_08/input_hashes.json','results/b17_08/verification.json','results/b17_08/primary_sources.json',
       'delivery/b17_08/inputs/work/batch15_workers/B15-02/docs/b17_02_report.md',
       'delivery/b17_08/inputs/work/batch15_workers/B15-02/delivery/b17_02/MANIFEST.json')) { $paths+=Join-Path $workers ('B15-08/'+$rel) }
    foreach ($slot in @('01','03','05','06','07')) { $paths+=Join-Path $workers "B15-$slot/docs/b17_${slot}_report.md" }
    foreach ($slot in @('01','06')) {
       $paths+=Join-Path $workers "B15-$slot/docs/b16_${slot}_proof.md"
       $paths+=Join-Path $workers "B15-$slot/delivery/b16_$slot/MANIFEST.json"
    }
    $records=@()
    foreach ($p in $paths) {
        $r=Rec $p
        if (-not $r.path.StartsWith($wt+'\')) {
            $rel=[IO.Path]::GetRelativePath($project,$r.path)
            $dest=Join-Path (Join-Path $delivery 'inputs') $rel
            New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
            Copy-Item -LiteralPath $p -Destination $dest
            $r.snapshot=[IO.Path]::GetRelativePath($wt,$dest).Replace('\','/')
            if ((Hash $dest) -ne $r.sha256) { throw 'Snapshot mismatch' }
        }
        $records+=$r
    }
    $bindings=@()
    foreach ($slot in @('04','08')) {
        $m=Get-Content -Raw -LiteralPath (Join-Path $workers "B15-$slot/delivery/b17_$slot/MANIFEST.json") | ConvertFrom-Json
        foreach ($e in $m.artifacts) { $bindings+=[ordered]@{kind="B17-$slot delivery";path=$e.path;expected=$e.sha256;actual=(Hash $e.path);match=((Hash $e.path) -eq $e.sha256)} }
    }
    $prodPins=Get-Content -Raw -LiteralPath (Join-Path $workers 'B15-04/results/b17_04/input_hashes.json') | ConvertFrom-Json
    foreach ($e in $prodPins.inputs) { $bindings+=[ordered]@{kind='04 original-input chain';path=$e.path;expected=$e.sha256;actual=(Hash $e.path);match=((Hash $e.path) -eq $e.sha256)} }
    $old08=Get-Content -Raw -LiteralPath (Join-Path $workers 'B15-08/results/b17_08/input_hashes.json') | ConvertFrom-Json
    foreach ($e in $old08.files) {
        $snap=Join-Path $workers ('B15-08/'+$e.snapshot)
        $bindings+=[ordered]@{kind='08 historical snapshot';path=$snap;expected=$e.sha256;actual=(Hash $snap);match=((Hash $snap) -eq $e.sha256)}
    }
    foreach ($slot in @('01','04','06')) {
        $m=Get-Content -Raw -LiteralPath (Join-Path $workers "B15-$slot/delivery/b16_$slot/MANIFEST.json") | ConvertFrom-Json
        $e=@($m.artifacts)+@($m.files) | Where-Object { $_.path -and ($_.path -replace '\\','/').EndsWith("docs/b16_${slot}_proof.md") }
        if (@($e).Count -ne 1) { throw "Missing original proof binding $slot" }
        $p=Join-Path $workers "B15-$slot/docs/b16_${slot}_proof.md"
        $bindings+=[ordered]@{kind='B16 original proof';path=$p;expected=$e.sha256;actual=(Hash $p);match=((Hash $p) -eq $e.sha256)}
    }
    [ordered]@{created_utc=[DateTime]::UtcNow.ToString('o');files=$records;prior_artifact_checks=$preserved} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'input_hashes.json') -Encoding utf8
    [ordered]@{all_match=(@($bindings | Where-Object {-not $_.match}).Count -eq 0);checks=$bindings} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'delivery_bindings.json') -Encoding utf8
    $candidateFiles=@()
    foreach ($slot in @('09','10')) {
        $files=@(& rg --files (Join-Path $workers "B15-$slot/docs") (Join-Path $workers "B15-$slot/results") (Join-Path $workers "B15-$slot/delivery") | Where-Object {$_ -match '[\\/]b17[_\\/]'} )
        $candidateFiles+=[ordered]@{slot=$slot;observed_b17_files=$files;candidate_count=0;basis='No B17 candidate artifacts;08 explicitly nominates zero. Absence is scoped to this saved review.'}
    }
    [ordered]@{checked_utc=[DateTime]::UtcNow.ToString('o');slots=$candidateFiles;waited_for12=$false;research_searches=0;approval_rejections=0} | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $out 'candidate_status.json') -Encoding utf8
    Write-Output ('Pinned '+$records.Count+' inputs; '+$bindings.Count+' bindings; preserved '+$preserved+' earlier artifact checks')
    if (@($bindings | Where-Object {-not $_.match}).Count) { throw 'Binding mismatch saved; inspect before computation' }
} else {
    $prior=Get-Content -Raw -LiteralPath $archive | ConvertFrom-Json
    $preserved=Prior-Checks $prior
    $pins=Get-Content -Raw -LiteralPath (Join-Path $out 'input_hashes.json') | ConvertFrom-Json
    foreach ($e in $pins.files) {
        if ((Hash $e.path) -ne $e.sha256) { throw ('Pinned input changed '+$e.path) }
        if ($e.snapshot -and (Hash (Join-Path $wt $e.snapshot)) -ne $e.sha256) { throw 'Snapshot changed' }
    }
    $bindings=Get-Content -Raw -LiteralPath (Join-Path $out 'delivery_bindings.json') | ConvertFrom-Json
    if (-not $bindings.all_match) { throw 'Unresolved binding mismatch' }
    [ordered]@{checked_utc=[DateTime]::UtcNow.ToString('o');inputs_unchanged=$pins.files.Count;prior_artifact_checks=$preserved;previous_manifest_sha256=(Hash $archive)} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $out 'final_integrity.json') -Encoding utf8
    $artifacts=@()
    foreach ($pat in @('analysis/b17_11_supplement04_08*','docs/b17_11_supplement04_08*','results/b17_11/supplement04_08/*','results/logs/b17_11_supplement04_08*','delivery/b17_11/supplement04_08/*')) {
        Get-ChildItem -Path (Join-Path $wt $pat) -File -Recurse | Where-Object { $_.Name -ne 'MANIFEST.json' -or $_.FullName -like '*\inputs\*' } | ForEach-Object { $artifacts+=Rec $_.FullName }
    }
    $run=Get-Content -Raw -LiteralPath (Join-Path $wt 'results/logs/b17_11_supplement04_08_resources.json') | ConvertFrom-Json
    $v=Get-Content -Raw -LiteralPath (Join-Path $out 'verification.json') | ConvertFrom-Json
    $decisions=Get-Content -Raw -LiteralPath (Join-Path $out 'decisions.json') | ConvertFrom-Json
    if ($run.exit_code -ne 0 -or $v.status -ne 'PASS_SCOPED_INDEPENDENT_CONTROL') { throw 'No successful scientific receipt; do not seal an acceptance' }
    if ($decisions.scientific_executions_during_finalization -ne 0) { throw 'Finalization must be metadata only' }
    if (@($prior.supplements | Where-Object {$_.id -eq 'supplement04_08'}).Count) { throw 'Supplement already exists in previous archive' }
    $sup=[ordered]@{id='supplement04_08';status='COMPLETE_ACCEPTED_SCOPED_REVIEW';report='docs/b17_11_supplement04_08.md';inputs=$pins.files;artifacts=$artifacts;mathematical_computations=1;run=$run;verification=$v;previous_manifest_archive=(Rec $archive);prior_artifact_checks=$preserved;decisions='results/b17_11/supplement04_08/decisions.json';supported_finite_candidates09_10=0;further_research_searches=0;no_agents_or_heavy_lease=$true}
    $sup | ConvertTo-Json -Depth 40 | Set-Content -LiteralPath (Join-Path $delivery 'MANIFEST.json') -Encoding utf8
    $sup.manifest_file=Rec (Join-Path $delivery 'MANIFEST.json')
    $prior.scope='First-stage and supplement02 preserved; final bounded review04/08 complete; no supported09/10 finite candidate'
    $prior.mathematical_computations=3
    $prior.unverified=@('04 second global kernel direction and exact restriction rank9','Full unrestricted J24 and saturation','Any positive new cell or beyond-occurrence witness','delta7(per3)>280','02 forbidden-weight rank and any strict numerical improvement','12 not reviewed or awaited')
    $prior.supplements=@($prior.supplements)+@($sup)
    $prior.updated_utc=[DateTime]::UtcNow.ToString('o')
    $prior | ConvertTo-Json -Depth 50 | Set-Content -LiteralPath $mainManifest -Encoding utf8
    Write-Output ('Sealed '+$artifacts.Count+' new artifacts; preserved '+$preserved+' previous checks; research invocations3 total')
}
