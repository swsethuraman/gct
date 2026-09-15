param([switch]$Seal)
$ErrorActionPreference='Stop'
$wt=Split-Path $PSScriptRoot -Parent
$workers=Split-Path $wt -Parent
$project=[IO.Path]::GetFullPath((Join-Path $wt '../../..'))
$out=Join-Path $wt 'results/b17_11/supplement02'
$delivery=Join-Path $wt 'delivery/b17_11/supplement02'
$mainManifest=Join-Path $wt 'delivery/b17_11/MANIFEST.json'
$archive=Join-Path $delivery 'FIRST_STAGE_MANIFEST.json'
New-Item -ItemType Directory -Force -Path $out,$delivery,(Join-Path $delivery 'inputs') | Out-Null
function Hash($p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLowerInvariant() }
function Rec($p) { $i=Get-Item -LiteralPath $p; [ordered]@{path=$i.FullName;bytes=$i.Length;sha256=(Hash $p)} }
if (-not $Seal) {
    if (Test-Path -LiteralPath $archive) { throw 'Preserve existing first-stage archive' }
    Copy-Item -LiteralPath $mainManifest -Destination $archive
    $first=Get-Content -Raw -LiteralPath $archive | ConvertFrom-Json
    foreach ($e in $first.artifacts) { if ((Hash $e.path) -ne $e.sha256) { throw ('First-stage artifact mismatch '+$e.path) } }
    $paths=@(
      (Join-Path $wt 'analysis/b15_bound.py'),(Join-Path $wt '.venv/python.exe'),
      (Join-Path $wt 'analysis/b17_11_supplement02_verify.py'),$archive,
      (Join-Path $wt 'docs/b17_11_report.md'),
      (Join-Path $workers 'B15-02/docs/b17_02_report.md'),
      (Join-Path $workers 'B15-02/docs/b17_02_preflight.md'),
      (Join-Path $workers 'B15-02/analysis/b17_02_verify.py'),
      (Join-Path $workers 'B15-02/delivery/b17_02/MANIFEST.json'),
      (Join-Path $workers 'B15-02/results/b17_02/verification.json'),
      (Join-Path $workers 'B15-02/results/b17_02/input_hashes.json'),
      (Join-Path $workers 'B15-02/results/b17_02/primary_source_extracts.json'),
      (Join-Path $workers 'B15-08/docs/b16_08_proof.md'),
      (Join-Path $workers 'B15-08/delivery/b16_08/ARTIFACT_HASHES.json'),
      (Join-Path $workers 'B15-08/delivery/b16_08/INPUT_HASHES.json'),
      (Join-Path $project 'Batch16/INTAKE.json'),
      (Join-Path $project 'Batch16/reviews/12_milestone/intake_08.json'),
      (Join-Path $project 'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md')
    )
    $records=@()
    foreach ($p in $paths) {
        $r=Rec $p
        if ($p.StartsWith($workers+'\B15-02') -or $p.StartsWith($workers+'\B15-08') -or $p.StartsWith($project+'\Batch')) {
            $rel=[IO.Path]::GetRelativePath($project,$p)
            $dest=Join-Path (Join-Path $delivery 'inputs') $rel
            New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
            Copy-Item -LiteralPath $p -Destination $dest
            $r.snapshot=[IO.Path]::GetRelativePath($wt,$dest).Replace('\','/')
        }
        $records+=$r
    }
    $producer=Get-Content -Raw -LiteralPath (Join-Path $workers 'B15-02/delivery/b17_02/MANIFEST.json') | ConvertFrom-Json
    $bindings=@($producer.artifacts | ForEach-Object { [ordered]@{path=$_.path;expected=$_.sha256;actual=(Hash $_.path);match=((Hash $_.path) -eq $_.sha256)} })
    $old=Get-Content -Raw -LiteralPath (Join-Path $workers 'B15-08/delivery/b16_08/ARTIFACT_HASHES.json') | ConvertFrom-Json
    $proof=$old.files | Where-Object { $_.path.EndsWith('b16_08_proof.md') }
    $bindings+=[ordered]@{path=$proof.path;expected=$proof.sha256;actual=(Hash $proof.path);match=((Hash $proof.path) -eq $proof.sha256)}
    $shared=Join-Path $project 'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md'
    $oldInputs=Get-Content -Raw -LiteralPath (Join-Path $workers 'B15-08/delivery/b16_08/INPUT_HASHES.json') | ConvertFrom-Json
    $e=$oldInputs.files | Where-Object { ($_.path -replace '\\','/').EndsWith('/Hessian11_1631/REPORT.md') }
    if (-not $e) { throw 'Missing original Hessian input binding' }
    $bindings+=[ordered]@{path=$shared;expected=$e.sha256;actual=(Hash $shared);match=((Hash $shared) -eq $e.sha256)}
    [ordered]@{created_utc=[DateTime]::UtcNow.ToString('o');files=$records;first_stage_artifacts_preserved=$first.artifacts.Count} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'input_hashes.json') -Encoding utf8
    [ordered]@{all_match=(@($bindings | Where-Object {-not $_.match}).Count -eq 0);checks=$bindings} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'delivery_bindings.json') -Encoding utf8
    Write-Output ('Pinned '+$records.Count+' inputs; checked '+$bindings.Count+' bindings; first-stage artifacts preserved '+$first.artifacts.Count)
} else {
    $bindingResult=Get-Content -Raw -LiteralPath (Join-Path $out 'delivery_bindings.json') | ConvertFrom-Json
    if (-not $bindingResult.all_match) { throw 'Producer or inherited binding mismatch' }
    $pins=Get-Content -Raw -LiteralPath (Join-Path $out 'input_hashes.json') | ConvertFrom-Json
    foreach ($e in $pins.files) { if ((Hash $e.path) -ne $e.sha256) { throw ('Input changed '+$e.path) } }
    $first=Get-Content -Raw -LiteralPath $archive | ConvertFrom-Json
    foreach ($e in $first.artifacts) { if ((Hash $e.path) -ne $e.sha256) { throw ('First-stage artifact changed '+$e.path) } }
    [ordered]@{checked_utc=[DateTime]::UtcNow.ToString('o');supplement_inputs_unchanged=$pins.files.Count;first_stage_artifacts_unchanged=$first.artifacts.Count;first_stage_manifest_archive_sha256=(Hash $archive)} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $out 'final_integrity.json') -Encoding utf8
    $artifacts=@()
    foreach ($pat in @('analysis/b17_11_supplement02*','docs/b17_11_supplement02*','results/b17_11/supplement02/*','results/logs/b17_11_supplement02*','delivery/b17_11/supplement02/*')) {
        Get-ChildItem -Path (Join-Path $wt $pat) -File -Recurse | Where-Object { $_.Name -ne 'MANIFEST.json' -or $_.FullName -like '*\inputs\*' } | ForEach-Object { $artifacts+=Rec $_.FullName }
    }
    $run=Get-Content -Raw -LiteralPath (Join-Path $wt 'results/logs/b17_11_supplement02_resources.json') | ConvertFrom-Json
    $v=Get-Content -Raw -LiteralPath (Join-Path $out 'verification.json') | ConvertFrom-Json
    $sup=[ordered]@{id='supplement02';status='COMPLETE_ACCEPTED_SCOPED_REVIEW';report='docs/b17_11_supplement02.md';inputs=$pins.files;artifacts=$artifacts;mathematical_computations=1;run=$run;verification=$v;accepted='Polynomial boundary arc, convention and full-H orbit source, forbidden interval [0,2d], clipped upper bound and all-degree original-entry-diagonal negative control';uncomputed=@('H-invariant basis for a new finite cell','Forbidden projection rank','Strict numerical improvement','Padding lower bound');no_agents_or_heavy_lease=$true;primary_source_notes='results/b17_11/supplement02/primary_sources.json';remote_pdf_hashes_claimed=$false}
    $sup | ConvertTo-Json -Depth 40 | Set-Content -LiteralPath (Join-Path $delivery 'MANIFEST.json') -Encoding utf8
    $sup.manifest_file=Rec (Join-Path $delivery 'MANIFEST.json')
    $first.scope='First-stage reviews01/03/05/06/07 preserved; supplementary independent review02 complete'
    $first.mathematical_computations=2
    $first.unverified=@('04/12 not reviewed by this supplement','Full unrestricted J24 and saturation','Any positive new cell or beyond-occurrence witness','delta7(per3)>280','02 forbidden-weight rank and any strict numerical improvement')
    $first | Add-Member -NotePropertyName first_stage_manifest_archive -NotePropertyValue (Rec $archive)
    $first | Add-Member -NotePropertyName first_stage_run_and_verification_fields_preserved -NotePropertyValue $true
    $first | Add-Member -NotePropertyName supplements -NotePropertyValue @($sup)
    $first | Add-Member -NotePropertyName updated_utc -NotePropertyValue ([DateTime]::UtcNow.ToString('o'))
    $first | ConvertTo-Json -Depth 50 | Set-Content -LiteralPath $mainManifest -Encoding utf8
    Write-Output ('Sealed supplement '+$artifacts.Count+' artifacts; preserved first-stage '+$first.artifacts.Count+' artifacts; total research runs2')
}
