# Administrative bytes/Git inspection only. No producer code is executed.
$ErrorActionPreference='Stop'
$root='C:\Users\swami\Projects\gct-gpt'
$out=Join-Path $root 'work\batch15_workers\B15-12\results\b25_12'
$utf8=[Text.UTF8Encoding]::new($false)
function Sha([byte[]]$b){$h=[Security.Cryptography.SHA256]::Create();try{([BitConverter]::ToString($h.ComputeHash($b))).Replace('-','').ToLowerInvariant()}finally{$h.Dispose()}}
function Git([string]$repo,[string[]]$ga){
 $si=[Diagnostics.ProcessStartInfo]::new('git'); $si.UseShellExecute=$false;$si.RedirectStandardOutput=$true;$si.RedirectStandardError=$true;$si.CreateNoWindow=$true
 $si.ArgumentList.Add('-C');$si.ArgumentList.Add($repo);foreach($a in $ga){$si.ArgumentList.Add($a)}
 $p=[Diagnostics.Process]::Start($si);$ms=[IO.MemoryStream]::new();$err=$p.StandardError.ReadToEndAsync();$p.StandardOutput.BaseStream.CopyTo($ms);$p.WaitForExit()
 $bytes=$ms.ToArray();[pscustomobject]@{code=$p.ExitCode;bytes=$bytes;text=$utf8.GetString($bytes).TrimEnd();stderr=$err.Result}
}
function WriteJson($name,$obj){[IO.File]::WriteAllText((Join-Path $out $name),($obj|ConvertTo-Json -Depth 60),$utf8)}
$map=[ordered]@{'a25_01'='work/batch15';'a25_02'='work/batch15';'a25_03'='work/batch15';'a25_04'='work/batch15';'a25_05'='work/batch15';'b25_01'='work/batch15_workers/B23-04';'b25_02'='work/batch15_workers/B24-06';'b25_03'='work/batch15_workers/B23-05';'b25_04'='work/batch15_workers/B15-02';'b25_05'='work/batch15_workers/B15-01';'b25_06'='work/batch15_workers/B23-03'}
$repos=@{};foreach($rel in @($map.Values)+@('work/batch15_workers/B15-12','work/batch15_workers/B15-10')|Select-Object -Unique){
 $repo=Join-Path $root $rel;$head=Git $repo @('rev-parse','HEAD');if($head.code-ne 0){throw $head.stderr}
 $repos[$rel]=[ordered]@{head=$head.text;branch=(Git $repo @('branch','--show-current')).text;status=(Git $repo @('status','--short','--untracked-files=all')).text;attributes=(Get-Content -Raw -LiteralPath (Join-Path $repo '.gitattributes') -ErrorAction SilentlyContinue);ignore=(Get-Content -Raw -LiteralPath (Join-Path $repo '.gitignore'))}
}
$packets=@()
foreach($slot in $map.Keys){
 $rel=$map[$slot];$repo=Join-Path $root $rel;$expected=@{};$manifestPath="results/$slot/MANIFEST.json";$mf=Join-Path $repo $manifestPath;$meta=$null
 if(Test-Path -LiteralPath $mf){
  $meta=Get-Content -Raw -LiteralPath $mf|ConvertFrom-Json
  foreach($key in @('files','artifacts','packet_files')){
   $set=$meta.$key;if($null-eq $set){continue}
   if($set -is [array]){foreach($e in $set){$expected[$e.path]=$e}}
   else{foreach($e in $set.PSObject.Properties){$expected[$e.Name]=$e.Value}}
  }
  if($meta.six_path_bindings){foreach($e in $meta.six_path_bindings.PSObject.Properties){$expected[$e.Name]=[pscustomobject]@{sha256=$e.Value.after_working_copy_sha256_UNCOMMITTED}}}
 }else{
  $manifestPath="results/$slot/FILES.sha256";$mf=Join-Path $repo $manifestPath
  foreach($line in Get-Content -LiteralPath $mf){if($line-match '^([a-f0-9]{64}) \*(.+)$'){$path=$Matches[2];if($path-notmatch '/'){$path="results/$slot/$path"};$expected[$path]=[pscustomobject]@{sha256=$Matches[1]}}}
  $bind=Get-Content -Raw -LiteralPath (Join-Path $repo "results/$slot/bindings.md")
  $after=($bind-split '## After \(UNCOMMITTED\)')[1]-split '## Committed inputs'
  foreach($m in [regex]::Matches($after[0],'\| `([^`]+)` \| `([a-f0-9]{64})` \| ([\d,]+)')){$expected[$m.Groups[1].Value]=[pscustomobject]@{sha256=$m.Groups[2].Value;bytes=[long]$m.Groups[3].Value.Replace(',','')}}
 }
 $paths=@($expected.Keys)+@($manifestPath)
 foreach($folder in @("results/$slot")){foreach($f in Get-ChildItem -LiteralPath (Join-Path $repo $folder) -File -Recurse){$paths+=[IO.Path]::GetRelativePath($repo,$f.FullName).Replace('\','/')}}
 foreach($folder in @('analysis','results/logs')){foreach($f in Get-ChildItem -LiteralPath (Join-Path $repo $folder) -File -Filter "${slot}_*" -ErrorAction SilentlyContinue){$paths+=[IO.Path]::GetRelativePath($repo,$f.FullName).Replace('\','/')}}
 $rows=@();foreach($path in $paths|Sort-Object -Unique){
  $full=Join-Path $repo $path;if(!(Test-Path -LiteralPath $full)){throw "Missing $slot $path"};$b=[IO.File]::ReadAllBytes($full);$sha=Sha $b;$e=$expected[$path];$want=$e.sha256;if(!$want){$want=$e.sha256_raw};$wantSize=$e.bytes
  $raw=Git $repo @('hash-object','--no-filters','--',$path);$filtered=Git $repo @('hash-object','--',$path);$before=Git $repo @('show',"HEAD:$path");$blob=Git $repo @('rev-parse',"HEAD:$path");$ignored=Git $repo @('check-ignore','-v','--',$path)
  $txt=$utf8.GetString($b)
  $rows+=[ordered]@{path=$path;absolute_path=$full;bytes=$b.Length;sha256_raw=$sha;expected_sha256=$want;hash_match=if($want){$sha-eq $want}else{$null};size_match=if($null-ne $wantSize){$b.Length-eq $wantSize}else{$null};crlf=([regex]::Matches($txt,"`r`n")).Count;lf=([regex]::Matches($txt,"(?<!`r)`n")).Count;raw_git_blob=$raw.text;filtered_git_blob=$filtered.text;filter_changes_bytes=($raw.text-ne $filtered.text);attributes=(Git $repo @('check-attr','text','eol','filter','--',$path)).text;ignored=($ignored.code-eq 0);ignore_rule=$ignored.text;before_blob=if($blob.code-eq 0){$blob.text}else{$null};before_bytes=if($before.code-eq 0){$before.bytes.Length}else{$null};before_sha256=if($before.code-eq 0){Sha $before.bytes}else{$null};delivery_action=if($before.code-eq 0 -and (Sha $before.bytes)-eq $sha){'ALREADY_TRACKED_UNCHANGED'}elseif($slot-eq 'b25_03' -and $path-in @('paper/det3-conductor.tex','README.md')){'BIND_ONLY_UNCHANGED_CRLF_RENDERING'}else{'ADD_EXACT_PATH'}}
 }
 $packets+=[ordered]@{slot=$slot;worktree=$rel;branch=$repos[$rel].branch;head=$repos[$rel].head;manifest=$manifestPath;manifest_sha256=(Sha ([IO.File]::ReadAllBytes($mf)));producer_metadata=$meta;files=$rows}
}
WriteJson 'INTAKE_INVENTORY_20260922.json' ([ordered]@{observed_utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ');method='Administrative read/hash/Git only; no mathematical execution';repositories=$repos;packets=$packets})
$packets|ForEach-Object{[pscustomobject]@{slot=$_.slot;paths=$_.files.Count;hash_failures=@($_.files|Where-Object {$_.hash_match-eq $false -or $_.size_match-eq $false}).Count;filter_changes=@($_.files|Where-Object filter_changes_bytes).Count;ignored=@($_.files|Where-Object ignored).Count;manifest=$_.manifest_sha256}}|ConvertTo-Json
