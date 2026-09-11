#!/usr/bin/env python3
"""Find data artefacts a staged report names but the tree does not carry.

Batch 13's first pass at this was an ad-hoc scan with no script behind it.  It
reported six gaps: four real, two false, and it missed five more.  Both false
positives came from matching a bare filename without asking *where* -- one named
a file that lives under a different session's directory, the other appeared in a
sentence whose whole point was that the file is absent.  The misses came from
testing a basename against the whole tree, so `results/b13_02/input_manifest.json`
made S2's missing manifest look present.

So: resolve by path, not by name; never drop a reference silently.  A reference
that looks explained is *reported as explained*, with the evidence, for a human
to confirm.  That is the same rule check_delivery.py learned -- a check that
quietly passes is worse than no check.

usage:  python3 tools/integrate/scan_unstaged.py [--json results/integrate/unstaged_artefacts.json]
"""
import argparse, json, os, pathlib, posixpath, re, signal, subprocess, sys

# `scan_unstaged.py | head` should print and stop, not traceback.  The hasattr
# guard is not decoration: Windows has no SIGPIPE, so the bare call raised
# AttributeError at import and the tool would not start on the machine it is
# actually run on.  Added by Astra, after I broke it fixing a cosmetic traceback.
if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Git speaks forward slashes on every platform.  os.path.join is ntpath.join on
# Windows and yields "results/astra/S1\\name.json", which matches nothing in
# `git ls-files`, so every "is it beside its report" test failed there and the
# reference fell through to the basename lookup.  Astra's Windows run recorded 48
# resolved-elsewhere against 13 here on the identical tree; that gap is this bug.
# Repo paths are posixpath, always -- never os.path.
rjoin = posixpath.join
rdirname = posixpath.dirname
rbasename = posixpath.basename

DATA_EXT = r'\.(?:json|jsonl|npz|npy|csv|gz|txt|dat|pkl|h5|parquet)'

# Reports were written against a working directory on the delivering host.  This
# is the one mapping from that host's layout into the repository.
HOST_ROOT = re.compile(r'C:/Users/[A-Za-z0-9_]+/Projects/gct-gpt/Batch12_Results/'
                       r'([A-Za-z0-9_./\-]+)')
HOST_REWRITE = [("degree13_conversion_20260908", "degree13_conversion")]

BARE = re.compile(r'`([A-Za-z0-9_./\-]+' + DATA_EXT + r')`')

# A sentence that asserts the file is NOT there is not a staging gap.  Context is
# the whole PARAGRAPH, not the line: these reports are hard-wrapped, and the first
# version of this scan missed five deliberate non-stagings because the filenames
# sat on one line and the "was **not** copied" that explained them sat on the next.
# Over-suppressing is safe here only because nothing is dropped -- a suppressed
# reference is reported in its own list, with the marker that suppressed it.
ABSENCE = [
    "contains **no**", "contains no ", "not committed", "did not locate",
    "were not located", "not recovered", "remain a dependency gap",
    "is absent", "are absent", "not delivered", "not present",
    "not copied", "would breach", "regenerable",
]

# results/astra/S<n>/ is one workstream.  A same-named file found OUTSIDE it --
# results/b13_02/input_manifest.json, say -- is a basename collision and is not
# evidence of anything; that collision is what made S2's missing manifest look
# present in the first pass.  Inside the workstream a cross-session reference is
# plausible but still needs a hash check before it counts as resolved.
ASTRA_ROOT = "results/astra/"


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"git {' '.join(a)}: {r.stderr.strip()}")
    return r.stdout


def paragraphs(text):
    """Yield (starting line number, paragraph text).  Blank-line separated."""
    buf, start = [], 1
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip():
            if not buf:
                start = n
            buf.append(line)
        elif buf:
            yield start, " ".join(buf)
            buf = []
    if buf:
        yield start, " ".join(buf)


def host_to_repo(rest):
    for a, b in HOST_REWRITE:
        rest = rest.replace(a, b)
    return "results/astra/" + rest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="results/astra")
    ap.add_argument("--json", default="results/integrate/unstaged_artefacts.json")
    args = ap.parse_args()

    tracked = set(git("ls-files").split())
    by_base = {}
    for p in tracked:
        by_base.setdefault(rbasename(p), []).append(p)

    reports = [p for p in tracked
               if p.startswith(args.root + "/") and p.endswith(".md")]

    missing, explained_absent, resolved_elsewhere = [], [], []
    seen = set()

    for rep in sorted(reports):
        repdir = rdirname(rep)
        for lineno, line in paragraphs(pathlib.Path(rep).read_text(errors="replace")):
            marker = next((m for m in ABSENCE if m in line), None)

            # (a) absolute host paths -- these carry their directory with them
            for rest in HOST_ROOT.findall(line):
                if not re.search(DATA_EXT + r'$', rest):
                    continue
                cand = host_to_repo(rest)
                key = (rep, cand)
                if key in seen or cand in tracked:
                    continue
                seen.add(key)
                rec = {"report": rep, "line": lineno, "expected_path": cand,
                       "how": "absolute host path"}
                (explained_absent if marker else missing).append(
                    dict(rec, **({"reported_absent_by": marker} if marker else {})))

            # (b) bare backticked names -- resolve beside the report first
            for name in BARE.findall(line):
                if "/" in name and name.startswith("results/"):
                    continue                       # already a repo path
                for cand in (rjoin(repdir, name),
                             rjoin(repdir, "artifacts", name)):
                    if cand in tracked:
                        break
                else:
                    key = (rep, name)
                    if key in seen:
                        continue
                    seen.add(key)
                    rec = {"report": rep, "line": lineno, "referenced": name,
                           "how": "bare name, not beside the report"}
                    if marker:
                        explained_absent.append(dict(rec, reported_absent_by=marker))
                    else:
                        found = sorted(by_base.get(rbasename(name), []))
                        inside = [f for f in found if f.startswith(ASTRA_ROOT)]
                        if inside:
                            resolved_elsewhere.append(
                                dict(rec, found_at=inside,
                                     caveat="cross-session within results/astra: "
                                            "confirm by hash before treating as resolved"))
                        else:
                            missing.append(
                                dict(rec, **({"same_name_outside_workstream": found}
                                             if found else {})))

    out = {
        "note": ("Data artefacts named by a staged report and absent from the tree. "
                 "References resolved by PATH: an absolute host path maps through "
                 "Batch12_Results/<rest> -> results/astra/<rest>; a bare name resolves "
                 "beside its report or in that report's artifacts/. Nothing is dropped "
                 "silently: a reference whose own sentence says the file is absent, or "
                 "one that resolves under another path, is reported in its own list "
                 "with the evidence."),
        "generated_by": "tools/integrate/scan_unstaged.py",
        "reports_scanned": len(reports),
        "missing": missing,
        "resolved_elsewhere": resolved_elsewhere,
        "reported_absent_by_the_report_itself": explained_absent,
    }
    pathlib.Path(args.json).write_text(json.dumps(out, indent=1) + "\n")

    # Count distinct FILES, not distinct names: S4's input_manifest.json and
    # S6's are two different files that happen to share a basename, and the
    # whole point of this tool is not to conflate those.
    def ident(m):
        return m.get("expected_path") or rjoin(
            rdirname(m["report"]), m["referenced"])

    out["distinct_missing_files"] = len({ident(m) for m in missing})
    pathlib.Path(args.json).write_text(json.dumps(out, indent=1) + "\n")

    print(f"reports scanned            : {len(reports)}")
    print(f"MISSING                    : {len(missing)} references, "
          f"{out['distinct_missing_files']} distinct files")
    print(f"resolved under another path: {len(resolved_elsewhere)}")
    print(f"reported absent by the report itself: {len(explained_absent)}")
    for m in missing:
        print("  MISSING  " + (m.get("expected_path") or m["referenced"]))
        print(f"           {m['report']}:{m['line']}")
    for m in resolved_elsewhere:
        print(f"  elsewhere {m['referenced']} -> {', '.join(m['found_at'])}")
        print(f"           {m['report']}:{m['line']}")
    for m in explained_absent:
        print("  absent-by-report " + (m.get("expected_path") or m["referenced"]))
        print(f"           {m['report']}:{m['line']}  ({m['reported_absent_by']!r})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
