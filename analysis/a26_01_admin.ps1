param([ValidateSet('Audit','Seal')][string]$Mode = 'Audit')

# Administrative only: committed-byte reads, hashes, inventory and manifest creation.
# No mathematical code, imported research modules, symbolic evaluation or certificate replay.
$ErrorActionPreference = 'Stop'
$taskRepo = 'C:\Users\swami\Projects\gct-gpt\work\batch15'
$taskRoot = 'C:\Users\swami\Projects\gct-gpt'
$taskOut = Join-Path $taskRepo 'results\a26_01'
$taskExpectedHead = 'd00da15c830cd2bc9bec8c3e8b4260506c9e1f2f'
$taskUtf8 = [System.Text.UTF8Encoding]::new($false)
$taskBindings = [ordered]@{}
$taskBlobBytes = @{}
$taskPayloadChecks = [System.Collections.Generic.List[object]]::new()

function Read-GitBytes([string[]]$GitArgs) {
    $taskPsi = [System.Diagnostics.ProcessStartInfo]::new()
    $taskPsi.FileName = 'git'
    $taskPsi.WorkingDirectory = $taskRepo
    $taskPsi.UseShellExecute = $false
    $taskPsi.CreateNoWindow = $true
    $taskPsi.RedirectStandardOutput = $true
    $taskPsi.RedirectStandardError = $true
    foreach ($taskArg in $GitArgs) { $taskPsi.ArgumentList.Add($taskArg) }
    $taskProc = [System.Diagnostics.Process]::new()
    $taskProc.StartInfo = $taskPsi
    [void]$taskProc.Start()
    $taskErrTask = $taskProc.StandardError.ReadToEndAsync()
    $taskStream = [System.IO.MemoryStream]::new()
    $taskProc.StandardOutput.BaseStream.CopyTo($taskStream)
    $taskProc.WaitForExit()
    $taskErr = $taskErrTask.GetAwaiter().GetResult()
    if ($taskProc.ExitCode -ne 0) { throw "git failed: $($GitArgs -join ' '): $taskErr" }
    if ($taskErr) { Write-Warning $taskErr.Trim() }
    $taskBytes = $taskStream.ToArray()
    $taskStream.Dispose()
    $taskProc.Dispose()
    return ,$taskBytes
}
function Read-GitText([string[]]$GitArgs) {
    return $taskUtf8.GetString((Read-GitBytes $GitArgs)).TrimEnd()
}
function Get-Sha([byte[]]$Bytes) {
    return [Convert]::ToHexString([System.Security.Cryptography.SHA256]::HashData($Bytes)).ToLowerInvariant()
}
function Save-Json([string]$Name, $Value) {
    if ($Name -notmatch '^[A-Z_]+\.json$') { throw 'Unexpected output name' }
    [System.IO.File]::WriteAllText((Join-Path $taskOut $Name), (($Value | ConvertTo-Json -Depth 20) + "`n"), $taskUtf8)
}
function Get-Binding([string]$Commit, [string]$Path) {
    $taskKey = "${Commit}:$Path"
    if (-not $taskBindings.Contains($taskKey)) {
        $taskBlob = Read-GitText @('rev-parse',$taskKey)
        $taskBytes = Read-GitBytes @('cat-file','blob',$taskKey)
        $taskBindings[$taskKey] = [ordered]@{
            commit=$Commit; path=$Path; blob=$taskBlob; bytes=$taskBytes.Length
            sha256=(Get-Sha $taskBytes); status='COMMITTED; content read status is separate'
        }
        $taskBlobBytes[$taskKey] = $taskBytes
    }
    return $taskBindings[$taskKey]
}
function Check-Payload([string]$Commit,[string]$Path,[string]$Hash,$Size,[string]$Manifest) {
    $taskBound = Get-Binding $Commit $Path
    $taskMatch = $taskBound.sha256 -eq $Hash.ToLowerInvariant()
    if ($null -ne $Size) { $taskMatch = $taskMatch -and ($taskBound.bytes -eq $Size) }
    $taskPayloadChecks.Add([ordered]@{
        manifest=$Manifest; commit=$Commit; path=$Path; declared_sha256=$Hash
        declared_bytes=$Size; matches=$taskMatch
    })
    if (-not $taskMatch) { throw "Manifest mismatch: ${Commit}:$Path" }
}

$taskHead = Read-GitText @('rev-parse','HEAD')
$taskBranch = Read-GitText @('branch','--show-current')
if ($taskHead -ne $taskExpectedHead -or $taskBranch -ne 'batch15-launch') { throw 'Repository baseline changed' }

if ($Mode -eq 'Audit') {
    $taskLaunchDir = Join-Path $taskRoot 'Claude_Handover_B15_B18\post_b19_housekeeping_20260917\batch26_launch'
    $taskReceiptPath = Join-Path $taskLaunchDir 'A26-01_INPUT_PREFLIGHT.json'
    $taskReceipt = [System.IO.File]::ReadAllText($taskReceiptPath) | ConvertFrom-Json
    $taskReceiptChecks = [System.Collections.Generic.List[object]]::new()
    foreach ($taskExpected in $taskReceipt.bindings) {
        $taskActual = Get-Binding $taskExpected.commit $taskExpected.path
        $taskMatches = ($taskActual.blob -eq $taskExpected.blob) -and ($taskActual.sha256 -eq $taskExpected.sha256) -and ($taskActual.bytes -eq $taskExpected.bytes)
        $taskReceiptChecks.Add([ordered]@{commit=$taskExpected.commit; path=$taskExpected.path; matches=$taskMatches})
        if (-not $taskMatches) { throw "Dispatch binding mismatch: $($taskExpected.path)" }
    }
    $taskManifests = @(
        '5007de860ba195100adc4f5a6cdebd3d344cadaa:results/a25_02/MANIFEST.json',
        '90dd22151511867f5dbb3488c5f3085034c6d7b3:results/a25_03/MANIFEST.json',
        '81967ddeb68340f31762bc41d424379cdd57527c:results/a25_04/MANIFEST.json',
        'eb53b97cf0904e2d54fdb7d101d83b024822811b:results/a25_05/MANIFEST.json',
        '92a7d054369a20854fd51685ee09ecb756344e8d:results/b25_04/MANIFEST.json',
        'ab4f527189bea14b5d146f9dc9d5b445844eaff3:results/a25_10/MANIFEST.json',
        'e22a41b1787ff5e8a284433d5d7e0d2a6a2d35b8:results/b22_02/MANIFEST.json',
        '82633a60893236fab4fbc317df416e1b8a349005:docs/post_b19_20260917/claude_gkz_incidence_20260917/scope_corrigendum/MANIFEST.json'
    )
    foreach ($taskSpec in $taskManifests) {
        $taskParts = $taskSpec.Split(':',2)
        $taskCommit = $taskParts[0]
        $taskManifestPath = $taskParts[1]
        [void](Get-Binding $taskCommit $taskManifestPath)
        $taskManifest = $taskUtf8.GetString($taskBlobBytes[$taskSpec]) | ConvertFrom-Json
        if ($taskManifest.artifacts) {
            foreach ($taskEntry in $taskManifest.artifacts) { Check-Payload $taskCommit $taskEntry.path $taskEntry.sha256 $taskEntry.bytes $taskSpec }
        } elseif ($taskManifest.files -is [array]) {
            foreach ($taskEntry in $taskManifest.files) { Check-Payload $taskCommit $taskEntry.path $taskEntry.sha256 $taskEntry.bytes $taskSpec }
        } elseif ($taskManifest.files) {
            foreach ($taskProp in $taskManifest.files.PSObject.Properties) { Check-Payload $taskCommit $taskProp.Name $taskProp.Value.sha256 $taskProp.Value.bytes $taskSpec }
        } elseif ($taskManifest.outputs) {
            foreach ($taskProp in $taskManifest.outputs.PSObject.Properties) { Check-Payload $taskCommit $taskProp.Name $taskProp.Value $null $taskSpec }
        } elseif ($taskManifest.outputs_sha256) {
            $taskPrefix = $taskManifestPath.Substring(0,$taskManifestPath.LastIndexOf('/')+1)
            foreach ($taskProp in $taskManifest.outputs_sha256.PSObject.Properties) { Check-Payload $taskCommit ($taskPrefix+$taskProp.Name) $taskProp.Value $null $taskSpec }
        } else { throw "Unknown manifest payload schema: $taskSpec" }
    }
    $taskAdminPaths = @(
        $taskReceiptPath,
        (Join-Path $taskLaunchDir 'A26-01.md'),
        (Join-Path (Split-Path $taskLaunchDir) 'BATCH26_REVISED_BOARD_v2.md'),
        (Join-Path (Split-Path $taskLaunchDir) 'BATCH26_PROPOSED_BOARD_v1.md'),
        (Join-Path (Split-Path $taskLaunchDir) 'BATCH26_LIVE_LEDGER.md'),
        (Join-Path (Split-Path $taskLaunchDir) 'batch25_launch\v1_20260921T003934Z\COMPUTE_PROTOCOL.md')
    )
    $taskAdmin = foreach ($taskFile in $taskAdminPaths) {
        $taskBytes = [System.IO.File]::ReadAllBytes($taskFile)
        [ordered]@{path=$taskFile; bytes=$taskBytes.Length; sha256=(Get-Sha $taskBytes); status='UNCOMMITTED administrative bytes; not mathematical acceptance'}
    }
    Save-Json 'INPUT_BINDINGS.json' ([ordered]@{
        schema='a26-01-input-audit/1'; observed_utc=[DateTime]::UtcNow.ToString('o')
        repository=$taskRepo; branch=$taskBranch; head=$taskHead
        method='Read-only Git committed-byte hashes and manifest declarations; no research code executed'
        dispatch_binding_count=$taskReceiptChecks.Count; dispatch_checks=$taskReceiptChecks
        distinct_committed_bindings=$taskBindings.Count; bindings=@($taskBindings.Values)
        manifest_payload_check_count=$taskPayloadChecks.Count; manifest_payload_checks=$taskPayloadChecks
        administrative_inputs=@($taskAdmin); mathematical_programs=0
        content_read_status='SOURCE_METHOD_LEDGER.md; byte verification does not mean content read or acceptance'
        recursive_historical_inputs_verified=$false
    })
    Write-Output "Verified $($taskReceiptChecks.Count) dispatch bindings, $($taskBindings.Count) distinct committed objects and $($taskPayloadChecks.Count) manifest payload declarations; zero mismatches."
} else {
    $taskNames = @('docs/a26_01_report.md','analysis/a26_01_admin.ps1')
    $taskNames += Get-ChildItem -LiteralPath $taskOut -File | Where-Object { $_.Name -ne 'MANIFEST.json' } | ForEach-Object { 'results/a26_01/'+$_.Name }
    $taskNames = @($taskNames | Sort-Object -Unique)
    $taskAllNames = @($taskNames + 'results/a26_01/MANIFEST.json' | Sort-Object -Unique)
    [System.IO.File]::WriteAllText((Join-Path $taskOut 'PROPOSED_DELIVERY_PATHS.txt'), (($taskAllNames -join "`n")+"`n"), $taskUtf8)
    $taskFiles = foreach ($taskName in $taskNames) {
        $taskBytes = [System.IO.File]::ReadAllBytes((Join-Path $taskRepo $taskName))
        [ordered]@{path=$taskName; bytes=$taskBytes.Length; sha256=(Get-Sha $taskBytes); status='UNCOMMITTED raw bytes / PRODUCER ONLY'}
    }
    Save-Json 'MANIFEST.json' ([ordered]@{
        schema='a26-01-producer-packet/1'; slot='A26-01'; sealed_utc=[DateTime]::UtcNow.ToString('o')
        status='UNCOMMITTED / PRODUCER ONLY / NOT INDEPENDENTLY REVIEWED'; delivery_commit=$null
        repository=$taskRepo; branch=$taskBranch; baseline_head=$taskHead
        registered_outcome=2; achieved_level='Scoped geometric containment/no-go for padded symmetric 3-by-3 permanents'
        mathematical_programs=0; mathematical_pilots=0; mathematical_computational_seconds=0
        theory_start_utc='2026-09-22T20:16:38Z'; checkpoint_utc='2026-09-22T20:20:57Z'; theory_stop_utc='2026-09-22T20:25:46Z'
        method='Committed-source READ and self-contained hand derivation; administrative hashing only'
        files=@($taskFiles); excludes=@('results/a26_01/MANIFEST.json')
        manifest_self_hashed=$false; proposed_delivery_paths=$taskAllNames
        general_five_center_actual_padding_comparison='OPEN'
    })
    $taskManifestBytes = [System.IO.File]::ReadAllBytes((Join-Path $taskOut 'MANIFEST.json'))
    Write-Output "Sealed $($taskFiles.Count) payloads; manifest raw SHA-256 $(Get-Sha $taskManifestBytes)."
}
