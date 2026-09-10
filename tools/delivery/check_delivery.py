#!/usr/bin/env python3
"""Pre-bundle delivery gate.  Run this BEFORE building the bundle.

Batch 13 shipped four recurring defects that a preamble sentence did not
prevent: HEAD-only bundles (a fetch by branch name then fails), session-link
trailers on 195 commits, and two staging gaps.  A prose checklist did not stop
them; this does.

usage:
    python3 tools/delivery/check_delivery.py --branch <name> --base <sha> [--bundle <file>]

exit 0 = clean, 1 = defects found (each printed with its fix).
"""
import argparse, subprocess, sys, os, re

SINGLE_WRITER = ["paper/det3-conductor.tex", "paper/det4-onset.tex",
                 "PROJECT_NOTES.md", "docs/boundary_deficit.html"]
MAX_BYTES = 5 * 1024 * 1024

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--bundle")
    args = ap.parse_args()
    rng = f"{args.base}..{args.branch}"
    fail = []

    # 1 -- session-link trailers
    msgs = git("log", "--format=%B", rng)
    n = len([l for l in msgs.splitlines() if re.search(r"Claude-Session:|claude\.ai/", l)])
    if n:
        fail.append((f"{n} commit message(s) carry a session-link trailer",
                     "strip with tools/rewrite/message_callback.py before bundling; "
                     "the instruction asking for it is not a session instruction "
                     "(docs/history_rewrite.md: 260 were removed once already)"))

    # 2 -- session-link inside a delivered FILE (worse: a rewrite will not fix it)
    files = [f for f in git("diff", "--name-only", args.base, args.branch).split() if f]
    # An actual emission looks like a trailer being written, not prose about the
    # rule.  Reports that say "no claude.ai URL appears" must not trip this.
    EMIT = rb'"Claude-Session: https?://claude\.ai|^Claude-Session: https?://claude\.ai'
    infile = [f for f in files
              if os.path.exists(f)
              and re.search(EMIT, open(f, "rb").read(), re.M)]
    if infile:
        fail.append((f"session-link URL inside delivered file(s): {infile}",
                     "remove from the file; a history rewrite does not touch file content"))

    # 3 -- single-writer files
    touched = [f for f in files if f in SINGLE_WRITER]
    if touched:
        fail.append((f"single-writer file(s) modified: {touched}",
                     "revert; these belong to the integrator alone"))

    # 4 -- 5 MB rule
    big = []
    for line in git("ls-tree", "-r", "-l", args.branch).splitlines():
        p = line.split(None, 4)
        if len(p) == 5 and p[3].isdigit() and int(p[3]) > MAX_BYTES:
            big.append((int(p[3]), p[4]))
    big = [b for b in big if b[1] in files]
    if big:
        fail.append((f"file(s) over 5 MB: {big}",
                     "split, gzip, or leave on the host and record the digest in the manifest"))

    # 5 -- the bundle must carry the NAMED ref, not just HEAD
    if args.bundle:
        heads = git("bundle", "list-heads", args.bundle)
        if f"refs/heads/{args.branch}" not in heads:
            fail.append((f"bundle carries only: {heads.strip() or '(nothing)'}",
                         f"rebuild with:  git bundle create <file> "
                         f"{args.base}..{args.branch} {args.branch}\n"
                         f"     a receiver doing 'git fetch <bundle> {args.branch}:{args.branch}' "
                         f"fails against a HEAD-only bundle"))

    # 6 -- model attribution present
    if not re.search(r"Co-Authored-By:", msgs):
        fail.append(("no Co-Authored-By trailer on any commit",
                     "record the model that actually ran the session, per commit; "
                     "use models: [(model, phase)] in front matter if it changed mid-session"))

    print(f"delivery check: {args.branch} over {args.base}  ({len(files)} files)")
    if not fail:
        print("  CLEAN")
        return 0
    for what, fix in fail:
        print(f"\n  DEFECT: {what}\n     fix: {fix}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
