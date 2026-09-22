$ErrorActionPreference = 'Stop'
$root = 'C:/Users/swami/Projects/gct-gpt'
$repo = "$root/work/batch15"
$out = "$repo/results/a25_01"
$audit = Get-Content -Raw "$root/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/astra_batch25_prompts/v1_20260921T002624Z/INPUT_AUDIT.json" | ConvertFrom-Json
$wanted = @('kernel','row10','lemmas','lemma_review','archive','fiveblock_review','tail','purepower','review23','review24','ledger24','koszul_review')
$records = @()
foreach ($packet in $audit.packets) {
    if ($packet.id -notin $wanted) { continue }
    foreach ($file in $packet.files) {
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = 'git'
        $psi.Arguments = '-C "' + $repo + '" show ' + $packet.commit + ':' + $file.path
        $psi.UseShellExecute = $false
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $proc = New-Object System.Diagnostics.Process
        $proc.StartInfo = $psi
        [void]$proc.Start()
        $buffer = New-Object System.IO.MemoryStream
        $proc.StandardOutput.BaseStream.CopyTo($buffer)
        $err = $proc.StandardError.ReadToEnd()
        $proc.WaitForExit()
        if ($proc.ExitCode -ne 0) { throw $err }
        $raw = $buffer.ToArray()
        $sha = [System.Security.Cryptography.SHA256]::Create()
        $digest = ([BitConverter]::ToString($sha.ComputeHash($raw))).Replace('-','').ToLowerInvariant()
        $expected = $file.sha256
        if ($file.committed_sha256) { $expected = $file.committed_sha256 }
        if ($digest -ne $expected) { throw "Pinned byte mismatch: $($packet.id) $($file.path)" }
        $blob = (& git -C $repo rev-parse ($packet.commit + ':' + $file.path)).Trim()
        $latest = @(& git -C $repo log --all -1 --format=%H -- $file.path)
        $records += [ordered]@{id=$packet.id; original_repository=$packet.repo; object_store_read_via=$repo; commit=$packet.commit; path=$file.path; blob=$blob; bytes=$raw.Length; sha256=$digest; drafting_hash_match=$true; latest_local_path_change=$latest; method='READ of named sections; raw committed blob hash verification; no mathematical replay'}
        $buffer.Dispose()
        $proc.Dispose()
        $sha.Dispose()
    }
}
$result = [ordered]@{utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'); status='UNCOMMITTED administrative audit'; records=$records; limit='Only bound blobs checked. Historical transitive pilot files not revalidated; no historical numeric result is a premise of the new theorem.'}
[IO.File]::WriteAllText("$out/SOURCE_BINDINGS.json", ($result | ConvertTo-Json -Depth 8) + "`n", (New-Object Text.UTF8Encoding($false)))
$records | ForEach-Object { [pscustomobject]$_ } | Select-Object id,path,sha256 | Format-Table -AutoSize
