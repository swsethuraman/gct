<#
    Run-Batch13Rewrite.ps1  (v3)

    Batch-13 history rewrite, start to finish, with every check that the
    previous attempt skipped.  Nothing is pushed; the push commands are
    printed at the end for you to run by hand.

    Usage, from anywhere:

        powershell -ExecutionPolicy Bypass -File .\Run-Batch13Rewrite.ps1

    It expects C:\Users\swami\Projects\gct\work to be on integration/batch13
    at b31a0de.  Override the location with -Root if it has moved.

    The script stops at the first failed check.  A stop is safe: it never
    touches `work`, and everything it does happens in a throwaway clone.
#>

[CmdletBinding()]
param(
    [string] $Root = "C:\Users\swami\Projects\gct",
    [switch] $RemoveStaleClone
)

$ErrorActionPreference = "Stop"

# ---- expected values, measured on two independent runs of the same rewrite --
$EXPECT_WORK_HEAD    = "b31a0de1c078d577325eb12a2b85fafddf46de00"
$EXPECT_OLD_MAIN     = "00495110c62acfbbbc951e82cc218ed091563b3f"
$EXPECT_NEW_BATCH13  = "743d640ded1c303b6f9d534ca8db76e075ae75e9"
$EXPECT_NEW_MAIN     = "ea2ad3087eca6c39acb506973dafab0aec7455a6"
$EXPECT_MAP_LINES    = 1549     # 1548 commits + one header line
$STALE_MAP_LINES     = 769      # the batch-10-era map that got committed by mistake

function Step ($n, $t) { Write-Host ""; Write-Host "== $n. $t" -ForegroundColor Cyan }
function Ok   ($t)     { Write-Host "   ok    $t" -ForegroundColor Green }
function Die  ($t)     { Write-Host "   STOP  $t" -ForegroundColor Red; exit 1 }

$clone = Join-Path $Root "gct-rewrite"
$work  = Join-Path $Root "work"

# --------------------------------------------------------------------------
Step 1 "check the source repository"
if (-not (Test-Path (Join-Path $work ".git"))) { Die "no git repository at $work" }
Push-Location $work
$branch = (git rev-parse --abbrev-ref HEAD).Trim()
$head   = (git rev-parse HEAD).Trim()
$dirty  = (git status --porcelain)
Pop-Location
if ($branch -ne "integration/batch13") { Die "work is on '$branch', expected integration/batch13" }
if ($head -ne $EXPECT_WORK_HEAD)       { Die "work HEAD is $head, expected $EXPECT_WORK_HEAD" }
if ($dirty)                            { Die "work has uncommitted changes; commit or stash them first" }
Ok "work is clean, on integration/batch13 at $($head.Substring(0,12))"

# --------------------------------------------------------------------------
Step 2 "clear the stale clone"
if (Test-Path $clone) {
    Write-Host "   $clone already exists." -ForegroundColor Yellow
    Write-Host "   It is left over from the batch-10-era rewrite.  Its .git\filter-repo\"
    Write-Host "   holds that run's commit-map, which is what got committed by mistake"
    Write-Host "   as e635b45.  It has to go -- reusing it is what poisoned the map."
    if (-not $RemoveStaleClone) {
        Write-Host ""
        $a = Read-Host "   Delete $clone and everything under it? (type YES)"
        if ($a -ne "YES") { Die "left in place; nothing done" }
    }
    Remove-Item -Recurse -Force $clone
}
Ok "no clone at $clone"

# --------------------------------------------------------------------------
Step 3 "fresh clone"
Push-Location $Root
git clone --no-local work gct-rewrite
if ($LASTEXITCODE -ne 0) { Pop-Location; Die "clone failed" }
Pop-Location
Push-Location $clone
# No 2>&1 anywhere near a native command.  PowerShell turns redirected native
# stderr into error records, and with ErrorActionPreference=Stop that kills the
# script on git's own success chatter ("Already on 'integration/batch13'").
# The clone lands on work's HEAD branch already, so only check out if it did not.
$b = (git rev-parse --abbrev-ref HEAD).Trim()
if ($b -ne "integration/batch13") {
    git checkout integration/batch13
    if ($LASTEXITCODE -ne 0) { Pop-Location; Die "could not check out integration/batch13" }
    $b = (git rev-parse --abbrev-ref HEAD).Trim()
}
if ($b -ne "integration/batch13") { Pop-Location; Die "clone is on '$b'" }
Ok "cloned and on integration/batch13"

Write-Host ""
Write-Host "   refs in the clone (the rewrite acts on all of them):"
git for-each-ref --format='     %(refname) %(objectname:short=12)'
$refs = @(git for-each-ref --format='%(refname)')
$unexpected = $refs | Where-Object {
    $_ -notin @("refs/heads/integration/batch13",
                "refs/remotes/origin/HEAD",
                "refs/remotes/origin/main",
                "refs/remotes/origin/integration/batch13")
}
if ($unexpected) {
    Write-Host ""
    Write-Host "   These refs are not in the set I rewrote here:" -ForegroundColor Yellow
    $unexpected | ForEach-Object { Write-Host "     $_" -ForegroundColor Yellow }
    Die "the rewrite scope differs from mine, so the expected hashes will not match -- send me this list before going on"
}
Ok "ref set matches the one I rewrote"

# --------------------------------------------------------------------------
Step 4 "run the rewrite"
# No bash.  Git Bash exists on this machine but pip's Scripts directory is not
# on its PATH, so `git filter-repo` is invisible there.  Python is the right
# driver anyway: it passes the multi-line callback as one argv element without
# PowerShell mangling its quotes, and it can reach filter-repo as a module even
# when the git subcommand wrapper is missing.
$driver = @'
"""Batch-13 rewrite driver.  Run from the root of the throwaway clone.

Exists because PowerShell mangles a multi-line argument containing quotes,
and because Git Bash may not have pip's Scripts directory on PATH.  Python
passes argv natively and can find filter-repo as a module.
"""
import pathlib, subprocess, sys

def probe():
    for form in (["git", "filter-repo"], [sys.executable, "-m", "git_filter_repo"]):
        try:
            r = subprocess.run(form + ["--version"], capture_output=True, text=True)
            if r.returncode == 0:
                return form, r.stdout.strip()
        except OSError:
            pass
    return None, None

def git(*a, **kw):
    return subprocess.run(["git", *a], capture_output=True, text=True, **kw).stdout

form, ver = probe()
if form is None:
    sys.stderr.write(
        "\n   git-filter-repo is not installed.\n\n"
        "   Install it, then re-run this script:\n\n"
        "       pip install git-filter-repo\n\n"
        "   (or:  py -m pip install git-filter-repo)\n\n"
        "   It is a single Python file published by its author on PyPI; it is\n"
        "   the tool docs/history_rewrite.md already names.  Nothing else is\n"
        "   needed -- no compiler, no Git for Windows reinstall.\n\n")
    sys.exit(2)

print("   filter-repo: %s (%s)" % (" ".join(form), ver))
cb = pathlib.Path("tools/rewrite/message_callback.py").read_text(encoding="utf-8")
rc = subprocess.call(form + ["--force",
                             "--commit-callback", cb,
                             "--strip-blobs-bigger-than", "5M"])
if rc:
    sys.exit(rc)

# --- the post-checks run_rewrite.sh used to print ---------------------------
msgs = git("log", "--all", "--format=%B")
objs = subprocess.run(["git", "cat-file",
                       "--batch-check=%(objecttype) %(objectname) %(objectsize) %(rest)"],
                      input=git("rev-list", "--objects", "--all"),
                      capture_output=True, text=True).stdout
big = sum(1 for l in objs.splitlines()
          for p in [l.split()]
          if len(p) >= 3 and p[0] == "blob" and p[2].isdigit() and int(p[2]) > 5 * 1024 * 1024)

print()
print("   === post-rewrite checks ===")
print("   commits with a byte-order mark : %d" % msgs.count("\ufeff"))
print("   commits with 'h_pad >= 19'     : %d" % msgs.count("h_pad >= 19"))
print("   commits with a session link    : %d" % msgs.count("claude.ai"))
print("   blobs over 5 MB in history     : %d" % big)
print("   commits total                  : %s" % git("rev-list", "--count", "--all").strip())
'@
# WriteAllText, not Out-File: Out-File -Encoding utf8 prepends a BOM on
# PowerShell 5.1, which is the very defect the callback exists to clean up.
# Written to TEMP, not into the clone, so filter-repo never sees a stray file.
$driverPath = Join-Path $env:TEMP "b13_rewrite_driver.py"
[IO.File]::WriteAllText($driverPath, $driver, (New-Object Text.UTF8Encoding $false))

$python = @("python", "py") |
          Where-Object { Get-Command $_ -ErrorAction SilentlyContinue } |
          Select-Object -First 1
if (-not $python) { Pop-Location; Die "no python on PATH -- check_delivery.py needs it too" }

& $python $driverPath
$rc = $LASTEXITCODE
Remove-Item $driverPath -Force -ErrorAction SilentlyContinue
if ($rc -eq 2) {
    Pop-Location
    Write-Host ""
    Write-Host "   git-filter-repo is not installed on this machine." -ForegroundColor Yellow
    Write-Host "   Install it and re-run this script:"
    Write-Host ""
    Write-Host "       pip install git-filter-repo"
    Write-Host ""
    Die "missing dependency; nothing was rewritten"
}
if ($rc -ne 0) { Pop-Location; Die "the rewrite failed (exit $rc)" }
Ok "rewrite finished"

# --------------------------------------------------------------------------
Step 5 "verify the result against my run"
$newB13  = (git rev-parse integration/batch13).Trim()
$newMain = (git rev-parse main).Trim()
Write-Host "   integration/batch13  $newB13"
Write-Host "   main                 $newMain"
if ($newB13  -ne $EXPECT_NEW_BATCH13) { Pop-Location; Die "batch13 tip is $newB13, I got $EXPECT_NEW_BATCH13 -- do not push, send me this" }
if ($newMain -ne $EXPECT_NEW_MAIN)    { Pop-Location; Die "main tip is $newMain, I got $EXPECT_NEW_MAIN -- do not push, send me this" }
Ok "both tips are bit-identical to mine"

$mapPath = ".git\filter-repo\commit-map"
if (-not (Test-Path $mapPath)) { Pop-Location; Die "no commit-map was produced -- the rewrite did not run" }
$mapLines = @(Get-Content $mapPath).Count
Write-Host "   commit-map lines     $mapLines"
if ($mapLines -eq $STALE_MAP_LINES) { Pop-Location; Die "$mapLines lines is the OLD batch-10 map -- this is the stale-map failure again" }
if ($mapLines -ne $EXPECT_MAP_LINES){ Pop-Location; Die "expected $EXPECT_MAP_LINES lines, got $mapLines" }
Ok "commit-map is this run's, $EXPECT_MAP_LINES lines"

$links = @(git log --all --format='%B' | Select-String -Pattern 'claude\.ai').Count
if ($links -ne 0) { Pop-Location; Die "$links commit message(s) still carry a session link" }
Ok "no session link in any commit message"

# --------------------------------------------------------------------------
Step 6 "bank the commit map"
New-Item -ItemType Directory -Force -Path "results\integrate" | Out-Null
Copy-Item $mapPath "results\integrate\batch13_commit_map.txt" -Force
git add results/integrate/batch13_commit_map.txt
$msg = @"
Batch-13 history rewrite: the original-to-rewritten commit map.

206 commit messages carried a session-link trailer: 195 new in batch 13 and
11 already on main (s71 x3, s72 x8).  All 206 are stripped.  768 of 1548
commits keep their original hashes; 780 are rewritten.  Both branch trees are
bit-identical before and after, verified object-for-object.

Two side effects, both intended and both recorded here rather than discovered
later: SSH signatures are dropped from the 780 rewritten commits (647 of them
were signed -- a signature cannot survive a message change), and 24 pairs of
signature-only twin commits in the s74/s79 range collapse into 24 single
commits, taking the count from 1548 to 1524.  No commit is dropped: every
entry in the map points at a real rewritten commit.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
"@
$msgPath = Join-Path $env:TEMP "b13_rewrite_msg.txt"
[IO.File]::WriteAllText($msgPath, $msg, (New-Object Text.UTF8Encoding $false))
git commit -F $msgPath
$rc = $LASTEXITCODE
Remove-Item $msgPath -Force
if ($rc -ne 0) { Pop-Location; Die "commit failed" }
$finalB13 = (git rev-parse integration/batch13).Trim()
$onBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if ($onBranch -ne "integration/batch13") { Pop-Location; Die "the map got committed on '$onBranch', not integration/batch13" }
Ok "map committed on integration/batch13; tip is now $($finalB13.Substring(0,12))"

# --------------------------------------------------------------------------
Step 7 "delivery gate, against the REWRITTEN base"
# 0049511 no longer exists here.  Giving the gate a base it cannot resolve
# makes it report 0 files and a bogus defect instead of failing, so the new
# base has to come out of the map.
$newBase = (Select-String -Path $mapPath -Pattern "^$EXPECT_OLD_MAIN" | Select-Object -First 1).Line -split '\s+' | Select-Object -Last 1
if (-not $newBase) { Pop-Location; Die "could not find the rewritten base in the commit map" }
Write-Host "   $($EXPECT_OLD_MAIN.Substring(0,12)) -> $($newBase.Substring(0,12))"
python tools\delivery\check_delivery.py --branch integration/batch13 --base $newBase
if ($LASTEXITCODE -ne 0) { Pop-Location; Die "delivery gate reported defects" }
Ok "gate is CLEAN"

# --------------------------------------------------------------------------
Step 8 "what is left, for you to run by hand"
Pop-Location
Write-Host ""
Write-Host "Rewrite done and verified.  Nothing has been pushed." -ForegroundColor Green
Write-Host ""
Write-Host "This force-pushes BOTH branches; main's history changes too, because"
Write-Host "11 of the contaminated commits were already published on it."
Write-Host ""
Write-Host "    cd $clone"
Write-Host "    git remote add origin https://github.com/swsethuraman/gct.git"
Write-Host "    git push --force origin main"
Write-Host "    git push --force origin integration/batch13"
Write-Host ""
Write-Host "Then repoint your working clone at the rewritten history:"
Write-Host ""
Write-Host "    cd $work"
Write-Host "    git fetch origin"
Write-Host "    git checkout integration/batch13"
Write-Host "    git reset --hard origin/integration/batch13"
Write-Host "    git checkout main"
Write-Host "    git reset --hard origin/main"
Write-Host "    git checkout integration/batch13"
Write-Host ""
