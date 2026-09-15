param([switch]$Seal)
$ErrorActionPreference = 'Stop'
$wt = Split-Path $PSScriptRoot -Parent
$project = [IO.Path]::GetFullPath((Join-Path $wt '../../..'))
$out = Join-Path $wt 'results/b17_11'
$delivery = Join-Path $wt 'delivery/b17_11'
New-Item -ItemType Directory -Force -Path $out,$delivery,(Join-Path $delivery 'inputs') | Out-Null
function Digest($path) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() }
function Record($path) {
    $item = Get-Item -LiteralPath $path
    [ordered]@{path=$item.FullName; bytes=$item.Length; sha256=(Digest $item.FullName)}
}
if (-not $Seal) {
    $paths = @('Batch17/BOARD.md','Batch17_Planning/SCREEN_REPORT.md','Batch17_Planning/symmetry_dream/COMMON_CONTEXT.md','Batch16/STOCKTAKE.md','Batch16/INTAKE.json','Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md') | ForEach-Object { Join-Path $project $_ }
    $paths += @('analysis/b15_bound.py','.venv/python.exe','analysis/b17_11_verify.py') | ForEach-Object { Join-Path $wt $_ }
    foreach ($s in '01','03','05','06','07') {
        $other = Join-Path (Split-Path $wt -Parent) ('B15-'+$s)
        $paths += Join-Path $other ('docs/b17_'+$s+'_report.md')
        $paths += Join-Path $other ('delivery/b17_'+$s+'/MANIFEST.json')
        if ($s -ne '03') { $paths += Join-Path $other ('analysis/b17_'+$s+'_verify.py') }
    }
    $relative = @(
      'B15-01/results/b17_01/certificate.json','B15-01/results/b17_01/input_hashes.json',
      'B15-01/docs/b16_01_proof.md','B15-01/docs/b16_01_report.md','B15-01/delivery/b16_01/MANIFEST.json',
      'B15-04/docs/b16_04_proof.md','B15-04/docs/b16_04_report.md','B15-04/delivery/b16_04/MANIFEST.json','B15-04/results/b16_04/universal_pole_certificate.json',
      'B15-05/results/b17_05/image_certificate.json','B15-05/results/b17_05/input_hashes.json',
      'B15-06/docs/b16_06_proof.md','B15-06/delivery/b16_06/MANIFEST.json','B15-06/results/b17_06/control_01.json',
      'B15-10/docs/b16_10_proof.md','B15-10/delivery/b16_10/SHA256_MANIFEST.json',
      'B15-07/results/b17_07/verification.json'
    )
    $paths += $relative | ForEach-Object { Join-Path (Split-Path $wt -Parent) $_ }
    $paths += @('Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/DREAM_REPORT.md','Batch15_Launch/native_20260913/reviews_filesystem/Dream_Upper288/integrator_review.json') | ForEach-Object { Join-Path $project $_ }
    $bindings = @()
    foreach ($s in '01','03','05','06','07') {
        $other = Join-Path (Split-Path $wt -Parent) ('B15-'+$s)
        $manifest = Get-Content -Raw -LiteralPath (Join-Path $other ('delivery/b17_'+$s+'/MANIFEST.json')) | ConvertFrom-Json
        $entries = if ($s -eq '01') { $manifest.artifact_files } else { $manifest.artifacts }
        foreach ($e in $entries) {
            $p = if ([IO.Path]::IsPathRooted($e.path)) { $e.path } else { Join-Path $other $e.path }
            $actual = Digest $p
            $bindings += [ordered]@{slot=$s;path=$p;expected=$e.sha256;actual=$actual;match=($actual -eq $e.sha256)}
        }
    }
    # Original accepted proof bindings; no inherited arithmetic is relabeled fresh.
    foreach ($s in '01','04','06') {
        $other = Join-Path (Split-Path $wt -Parent) ('B15-'+$s)
        $m = Get-Content -Raw -LiteralPath (Join-Path $other ('delivery/b16_'+$s+'/MANIFEST.json')) | ConvertFrom-Json
        $p = Join-Path $other ('docs/b16_'+$s+'_proof.md')
        $actual = Digest $p
        $declared = @($m.artifacts) + @($m.files) + @($m.artifact_files)
        $e = $declared | Where-Object { $_ -and ($_.path -replace '\\','/').EndsWith('/b16_'+$s+'_proof.md') } | Select-Object -First 1
        if (-not $e) { throw ('Missing original proof binding '+$s) }
        $bindings += [ordered]@{slot=('B16-'+$s);path=$p;expected=$e.sha256;actual=$actual;match=($actual -eq $e.sha256)}
    }
    $records = @()
    foreach ($p in ($paths | Sort-Object -Unique)) {
        $r = Record $p
        if ($r.path -notlike '*\.venv\python.exe' -and $r.path -notlike '*\B15-11\analysis\b17_11_verify.py') {
            $rel = [IO.Path]::GetRelativePath($project,$r.path)
            $dest = Join-Path (Join-Path $delivery 'inputs') $rel
            New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
            Copy-Item -LiteralPath $r.path -Destination $dest
            $r.snapshot = [IO.Path]::GetRelativePath($wt,$dest).Replace('\','/')
            if ((Digest $dest) -ne $r.sha256) { throw 'Snapshot mismatch' }
        }
        $records += $r
    }
    [ordered]@{created_utc=[DateTime]::UtcNow.ToString('o');files=$records} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'input_hashes.json') -Encoding utf8
    [ordered]@{all_match=(@($bindings | Where-Object { -not $_.match }).Count -eq 0);checks=$bindings} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'delivery_bindings.json') -Encoding utf8
    Write-Output ('Pinned '+$records.Count+' inputs; checked '+$bindings.Count+' artifact bindings; mismatches '+@($bindings | Where-Object { -not $_.match }).Count)
} else {
    $pins = Get-Content -Raw -LiteralPath (Join-Path $out 'input_hashes.json') | ConvertFrom-Json
    $checks = @($pins.files | ForEach-Object { [ordered]@{path=$_.path;unchanged=((Digest $_.path) -eq $_.sha256)} })
    [ordered]@{checked_utc=[DateTime]::UtcNow.ToString('o');all_unchanged=(@($checks | Where-Object { -not $_.unchanged }).Count -eq 0);checks=$checks} | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out 'final_integrity.json') -Encoding utf8
    $artifacts = @()
    $owned = @('analysis/b17_11*','docs/b17_11*','results/b17_11/*','results/logs/b17_11*','delivery/b17_11/inputs/*')
    foreach ($pattern in $owned) {
        Get-ChildItem -Path (Join-Path $wt $pattern) -Recurse -File | ForEach-Object { $artifacts += Record $_.FullName }
    }
    $run = Get-Content -Raw -LiteralPath (Join-Path $wt 'results/logs/b17_11_review_resources.json') | ConvertFrom-Json
    $verification = Get-Content -Raw -LiteralPath (Join-Path $out 'verification.json') | ConvertFrom-Json
    [ordered]@{task='B17-11';status='COMPLETE';scope='First-stage independent review of released 01/03/05/06/07; no 09/10 candidates supplied';workspace=$wt;created_utc=[DateTime]::UtcNow.ToString('o');report='docs/b17_11_report.md';model='gpt-6-astra';reasoning='xhigh';mathematical_computations=1;run=$run;verification=$verification;input_files=$pins.files;artifacts=$artifacts;fresh='Proof audit, source checks, independent arithmetic and controls; explicitly identified 05 circuit replay';inherited='B16 complete ideals, stable rank and source bounds; no character census replay';unverified=@('02/04/12 unfinished outputs','Full unrestricted J24 and saturation','Any positive new cell or beyond-occurrence witness','delta7(per3)>280');slot08_gate='No finite (d,lambda), global B and U>B supplied; theory priority exactly five rows';heavy_lease=$false;subagents=0;prohibited_actions_performed=$false;remote_bytes_hash_pinned=$false;source_notes='results/b17_11/primary_sources.json';blocked_actions='results/b17_11/access_record.json';manifest_self_hash=$false} | ConvertTo-Json -Depth 40 | Set-Content -LiteralPath (Join-Path $delivery 'MANIFEST.json') -Encoding utf8
    Write-Output ('Sealed '+$artifacts.Count+' artifacts; inputs unchanged '+(@($checks | Where-Object { -not $_.unchanged }).Count -eq 0))
}
