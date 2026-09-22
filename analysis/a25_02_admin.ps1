# Administrative provenance only: no symbolic, numerical or sampling work.
$ErrorActionPreference = 'Stop'
$root = 'C:/Users/swami/Projects/gct-gpt'
$repo = "$root/work/batch15"
$audit = Get-Content -Raw "$root/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_batch25_prompts/v1_20260921T002624Z/INPUT_AUDIT.json" | ConvertFrom-Json
$ids = @('lemmas','lemma_review','purepower','tail','archive','fiveblock_review','gkz','gkz_verdict','gkz_scope','koszul','koszul16','koszul_review','intersection','kernel','row10','review23','review24','ledger24','claims','gaps','c45','cap')
$rows = @()
foreach($packet in $audit.packets) {
 if($packet.id -notin $ids) { continue }
 foreach($f in $packet.files) {
  $psi = [Diagnostics.ProcessStartInfo]::new('git')
  $psi.UseShellExecute = $false
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  foreach($arg in @('-C',$repo,'show',"$($packet.commit):$($f.path)")) { $psi.ArgumentList.Add($arg) }
  $proc = [Diagnostics.Process]::Start($psi)
  $ms = [IO.MemoryStream]::new()
  $proc.StandardOutput.BaseStream.CopyTo($ms)
  $err = $proc.StandardError.ReadToEnd()
  $proc.WaitForExit()
  if($proc.ExitCode -ne 0) { throw $err }
  $bytes = $ms.ToArray()
  $sha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
  $expected = if($f.committed_sha256) {$f.committed_sha256} else {$f.sha256}
  if($sha -ne $expected) { throw "Source hash mismatch: $($packet.id) $($f.path)" }
  $blob = (& git -C $repo rev-parse "$($packet.commit):$($f.path)").Trim()
  $rows += [ordered]@{id=$packet.id; original_repository=$packet.repo; read_repository=$repo; commit=$packet.commit; path=$f.path; blob=$blob; bytes=$bytes.Length; sha256=$sha; drafting_digest_match=$true; method='Fresh committed-blob byte check; content reading scope separately documented'}
 }
}
$out = [ordered]@{utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'); method='READ/provenance; not replay or mathematical evaluator'; sources=$rows}
$out | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8NoBOM "$repo/results/a25_02/SOURCE_BINDINGS.json"
"Verified $($rows.Count) committed source blobs; no mathematical computation."
