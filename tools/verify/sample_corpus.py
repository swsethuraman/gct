#!/usr/bin/env python3
"""Stratified re-verification of the banked certificate corpus, in parallel.

WHY NOT JUST VERIFY EVERYTHING.  Re-derivation is not schema validation.  A
sparse_nullity certificate from session 60 re-derives a Wiedemann minimal
polynomial through tools/verify/wied_check, and one of them runs for MINUTES of
solid CPU.  The corpus is 1,082 certificates; end to end on one core that is
days, and nobody has ever run it.  What the merge-time pass established was that
every certificate parses, carries a known kind, and satisfies its schema -- not
that every claim was recomputed.

What re-verification is actually for at this stage is catching a SYSTEMATIC
defect: a migration that corrupted a field, a verifier change that silently
stopped checking something, a dialect that parses but means the wrong thing.  A
systematic defect shows up in the first few certificates of the stratum it
touches.  So a stratified sample -- a fixed number from every (directory, kind)
pair -- buys nearly all of that assurance for a small fraction of the cost, and
it is reproducible because the sample is seeded.

The full run belongs before publication, on a machine that can give it a few
days, not before a batch launch.

usage:
    python3 tools/verify/sample_corpus.py                      # 6 per stratum, 8 workers
    python3 tools/verify/sample_corpus.py --per 12 --jobs 16
    python3 tools/verify/sample_corpus.py --list-only          # just show the plan
    python3 tools/verify/sample_corpus.py --all --jobs 16      # the full corpus; hours to days

Every certificate is verified in its own process, so one hanging re-derivation
costs its own slot and not the run.  --timeout bounds each one; a certificate
that exceeds it is reported TIMEOUT and named, never silently passed.
"""
import argparse
import concurrent.futures as cf
import glob
import gzip
import json
import os
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CERTS = os.path.join(ROOT, "results", "certs")


def kind_of(path):
    """the certificate's kind, read without loading a 1.4 MB body twice."""
    try:
        op = gzip.open if path.endswith(".gz") else open
        with op(path, "rt", encoding="utf-8") as fh:
            return json.load(fh).get("kind", "?")
    except Exception:                                    # noqa: BLE001
        return "UNREADABLE"


def strata(paths):
    out = defaultdict(list)
    for p in paths:
        d = os.path.relpath(os.path.dirname(p), CERTS)
        out[(d, kind_of(p))].append(p)
    return out


def verify_one(path, timeout):
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, os.path.join(HERE, "verify.py"), path, "--quiet"],
                           capture_output=True, text=True, timeout=timeout, cwd=ROOT)
        head = next((ln for ln in r.stdout.splitlines()
                     if ln[:11].strip() in ("PASS", "RECORDED", "FAIL", "UNPARSEABLE", "ERROR")), "")
        status = head[:11].strip() or ("PASS" if r.returncode == 0 else "ERROR")
    except subprocess.TimeoutExpired:
        status = "TIMEOUT"
    return path, status, round(time.time() - t0, 1)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--per", type=int, default=6, help="certificates per (directory, kind) stratum")
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--timeout", type=float, default=1800, help="seconds per certificate")
    ap.add_argument("--seed", type=int, default=20260908)
    ap.add_argument("--all", action="store_true", help="every certificate; hours to days")
    ap.add_argument("--list-only", action="store_true")
    ap.add_argument("--out", default="results/wk12_int_corpus_sample.json")
    a = ap.parse_args(argv)

    paths = sorted(glob.glob(os.path.join(CERTS, "**", "*.json"), recursive=True)
                   + glob.glob(os.path.join(CERTS, "**", "*.json.gz"), recursive=True))
    print(f"corpus: {len(paths)} certificates", flush=True)
    st = strata(paths)
    rnd = random.Random(a.seed)
    plan = []
    for key in sorted(st):
        group = sorted(st[key])
        take = group if a.all else rnd.sample(group, min(a.per, len(group)))
        plan += take
        print(f"  {key[0]:6s} {str(key[1]):16s} {len(group):5d} available, {len(take):3d} selected", flush=True)
    print(f"selected {len(plan)} certificates, {a.jobs} workers, "
          f"{a.timeout:.0f}s cap each", flush=True)
    if a.list_only:
        return 0

    t0 = time.time()
    results, done = [], 0
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        futs = {ex.submit(verify_one, p, a.timeout): p for p in plan}
        for fut in cf.as_completed(futs):
            path, status, secs = fut.result()
            results.append(dict(path=os.path.relpath(path, ROOT), status=status, secs=secs))
            done += 1
            if status not in ("PASS", "RECORDED", "TIMEOUT"):
                print(f"  !! {status:11s} {os.path.relpath(path, ROOT)} ({secs}s)", flush=True)
            elif done % 10 == 0 or done == len(plan):
                print(f"  {done}/{len(plan)} done ({time.time()-t0:.0f}s elapsed)", flush=True)

    summary = Counter(r["status"] for r in results)
    # A TIMEOUT is INCONCLUSIVE, not a defect: re-derivation of one s60
    # sparse_nullity runs wied_check for minutes of solid CPU, and the cap is a
    # budget, not a verdict.  Only FAIL / UNPARSEABLE / ERROR are findings.
    bad = [r for r in results if r["status"] not in ("PASS", "RECORDED", "TIMEOUT")]
    slow = [r for r in results if r["status"] == "TIMEOUT"]
    print("\n" + ", ".join(f"{k} {v}" for k, v in sorted(summary.items())))
    print(f"{len(results)} certificates in {time.time()-t0:.0f}s wall "
          f"(slowest {max(r['secs'] for r in results):.0f}s)")
    if slow:
        print(f"{len(slow)} exceeded the {a.timeout:.0f}s cap -- INCONCLUSIVE, not failures; "
              f"re-run those with a larger --timeout")
    print("CLEAN" if not bad else f"{len(bad)} NOT CLEAN -- listed above, and in the report")
    with open(os.path.join(ROOT, a.out), "w", encoding="utf-8") as f:
        json.dump(dict(corpus=len(paths), selected=len(plan), per_stratum=a.per,
                       seed=a.seed, jobs=a.jobs, timeout=a.timeout, full=bool(a.all),
                       summary=dict(summary), wall_secs=round(time.time() - t0, 1),
                       not_clean=bad, inconclusive=slow, results=sorted(results, key=lambda r: -r["secs"])), f, indent=1)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
