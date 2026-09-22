$ErrorActionPreference = 'Stop'
$repo = 'C:/Users/swami/Projects/gct-gpt/work/batch15'
$out = Join-Path $repo 'results/a25_05'
[IO.Directory]::CreateDirectory($out) | Out-Null
$utf8 = New-Object System.Text.UTF8Encoding($false)
function Sha([byte[]]$b) { $h=[Security.Cryptography.SHA256]::Create(); try { ([BitConverter]::ToString($h.ComputeHash($b))).Replace('-','').ToLowerInvariant() } finally { $h.Dispose() } }
function Read-GitBytes([string]$spec) {
  $psi = New-Object Diagnostics.ProcessStartInfo
  $psi.FileName='git'; $psi.Arguments='-C "'+$repo+'" cat-file blob '+$spec
  $psi.UseShellExecute=$false; $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true; $psi.CreateNoWindow=$true
  $proc=New-Object Diagnostics.Process; $proc.StartInfo=$psi; $proc.Start() | Out-Null
  $ms=New-Object IO.MemoryStream; $proc.StandardOutput.BaseStream.CopyTo($ms); $err=$proc.StandardError.ReadToEnd(); $proc.WaitForExit()
  if($proc.ExitCode -ne 0) { throw $err }; $b=$ms.ToArray(); $ms.Dispose(); $proc.Dispose(); return ,$b
}
$bindings=@()
foreach($n in 1..4) {
  $mp='results/a25_0'+$n+'/MANIFEST.json'; $mb=[IO.File]::ReadAllBytes((Join-Path $repo $mp)); $m=$utf8.GetString($mb)|ConvertFrom-Json
  $bindings += [ordered]@{kind='provisional_manifest';path=$mp;bytes=$mb.Length;sha256=(Sha $mb);state='UNCOMMITTED / NOT INDEPENDENTLY ACCEPTED'}
  $entries=$m.artifacts; if($null -eq $entries){$entries=$m.files}
  foreach($e in $entries) {
    $b=[IO.File]::ReadAllBytes((Join-Path $repo $e.path)); $h=Sha $b
    if($h -ne $e.sha256 -or $b.Length -ne $e.bytes){throw ('Prior packet mismatch: '+$e.path)}
    $bindings += [ordered]@{kind='provisional_payload';path=$e.path;bytes=$b.Length;sha256=$h;manifest=$mp;manifest_match=$true;state='UNCOMMITTED / NOT INDEPENDENTLY ACCEPTED';access='Hash verification; READ status separately in SOURCE_READS.md'}
  }
}
$base='C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917'
$admin=@(
  "$base/astra_deep_dive/v1_20260921T040134Z/A25-05.md",
  "$base/batch25_launch/v1_20260921T003934Z/SOURCE_INDEX.md",
  "$base/batch25_launch/v1_20260921T003934Z/CLAUDE_COMMON.md",
  "$base/batch25_launch/v1_20260921T003934Z/COMPUTE_PROTOCOL.md",
  'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/docs/b25_12_ledger.md'
)
foreach($p in $admin) { $b=[IO.File]::ReadAllBytes($p); $bindings += [ordered]@{kind='administrative';path=$p;bytes=$b.Length;sha256=(Sha $b);state='UNCOMMITTED';access='READ in full'} }
$pins=@(
  @('review24','ab2f8a407f5eac320c13d1eefca33c9b930ded86','docs/b24_10_review.md'),
  @('lemmas','e22a41b1787ff5e8a284433d5d7e0d2a6a2d35b8','docs/b22_02_report.md'),
  @('fiveblock_review','f8273c3b5542fe085c596e3814c45621d3608ca7','docs/b24_02_report.md'),
  @('ledger24','f55ed57f636e5ae6ea791f3238a66f9414008c90','docs/b24_12_ledger.md'),
  @('boundary_context','3bcad66601a586936ce5c76fdf72d9551700dab3','docs/b23_03_report.md'),
  @('permanent_audit','82633a60893236fab4fbc317df416e1b8a349005','docs/b13_07_report.md'),
  @('permanent_certificate','82633a60893236fab4fbc317df416e1b8a349005','results/b13_07/dominance.json'),
  @('washout_context','82633a60893236fab4fbc317df416e1b8a349005','docs/washout_lemma.md')
)
foreach($pin in $pins) {
  $spec=$pin[1]+':'+$pin[2]; $b=Read-GitBytes $spec; $blob=(& git -C $repo rev-parse $spec).Trim()
  $bindings += [ordered]@{kind='committed_blob';id=$pin[0];commit=$pin[1];path=$pin[2];blob=$blob;bytes=$b.Length;sha256=(Sha $b);access='READ scope separately in SOURCE_READS.md'}
}
foreach($p in @('docs/b13_07_report.md','results/b13_07/dominance.json','docs/washout_lemma.md','results/a25_01/PADDING_STATUS.md','results/a25_03/SOURCE_READS.md')) {
  $b=[IO.File]::ReadAllBytes((Join-Path $repo $p))
  $bindings += [ordered]@{kind='working_copy_read';path=$p;bytes=$b.Length;sha256=(Sha $b);state='CURRENT RAW WORKING COPY; committed binding separate where supplied';access='READ scope separately in SOURCE_READS.md'}
}
$record=[ordered]@{slot='A25-05';created_utc=[DateTime]::UtcNow.ToString('o');method='Administrative raw-byte and Git blob hash checks; no mathematical computation';head=(& git -C $repo rev-parse HEAD).Trim();branch=(& git -C $repo branch --show-current).Trim();bindings=$bindings}
[IO.File]::WriteAllText((Join-Path $out 'SOURCE_BINDINGS.json'),(($record|ConvertTo-Json -Depth 10).Replace("`r`n","`n"))+"`n",$utf8)
Write-Output ('Verified and bound '+$bindings.Count+' input objects.')
