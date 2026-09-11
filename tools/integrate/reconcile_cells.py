#!/usr/bin/env python3
"""Cross-session cell reconciliation.

The integrator's own check.  Batch 13 closed the same cells twice and left the
combined theorem unstated, because twelve reports were read one at a time and
nobody joined their cell lists.  This joins them.

A cell is keyed  (n, ell, delta, lambda)  -- polynomial degree, PARTITION LENGTH,
coefficient degree, weight -- and every source contributes a verdict:

    CLOSED   mult == a at both primes, or an exact-determinant certificate
    OPEN     enumerated in a frontier and not measured
    DROP     mult <  a  (would be a candidate; none exist in batch 13)

It then reports, per frontier, the UNION of closures across sources, and flags
every cell one source calls OPEN that another calls CLOSED.  That flag is the
one that would have caught B13-05's 25 open cells being B13-09's completed 42.

usage: python3 tools/integrate/reconcile_cells.py [--json OUT]
"""
import json, os, sys, glob, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

def key(n, r, delta, lam):
    lam = tuple(int(x) for x in lam)
    while lam and lam[-1] == 0:
        lam = lam[:-1]
    return (int(n), int(r), int(delta), lam)

def jsonl(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return
    with open(p) as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)

def jload(path):
    p = os.path.join(ROOT, path)
    return json.load(open(p)) if os.path.exists(p) else None


def collect():
    """-> {cellkey: [(source, verdict, note), ...]}

    CENSUS FIRST.  A frontier is enumerated from its census/queue, so a cell
    that no session ever measured still appears -- as OPEN.  Reading only
    result files under-reports the frontier, which is the same class of error
    as reading only one session's list.
    """
    rec = collections.defaultdict(list)

    def add(src, verdict, n, r, delta, lam, note=""):
        # The third slot is ell(lambda), the partition length -- NOT the ambient
        # dimension r of D_r, which the theory side also calls r.  Five sources
        # fill it with len(mu) and three with their own "r" field, so the two
        # readings sit in one slot and nothing was checking they agree.  They do,
        # in all 1846 cells; this asserts it so that the first source which means
        # ambient dimension fails here instead of silently mis-joining.
        ell = len([x for x in lam if x])
        if int(r) != ell:
            raise SystemExit(
                f"{src}: cell key slot is ell(lambda), but this row gives r={r} "
                f"with lambda={lam} (length {ell}). If this source means the "
                f"ambient dimension of D_r, it must be converted before joining.")
        rec[key(n, r, delta, lam)].append((src, verdict, note))

    # ---- census / queue enumeration (every cell starts OPEN) --------------
    q = jload("results/s79_per6_queue.json")
    if q:
        for d, rows in (q.items() if isinstance(q, dict) else []):
            if not str(d).isdigit():
                continue
            for row in rows:
                mu = row.get("mu") if isinstance(row, dict) else row
                if mu:
                    add("census:s79_per6", "OPEN", 3, 6, int(d), mu)
    c9 = jload("results/b13_09_census.json")
    if c9:
        for gname, rows in c9.get("cells", {}).items():
            for row in rows:
                add("census:b13_09", "OPEN", 3, row["r"], row["delta"], row["mu"])
    c5 = jload("results/b13_05_census.json")
    if c5:
        rows = c5 if isinstance(c5, list) else next(
            (v for v in c5.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])
        for row in rows:
            mu = row.get("mu") or row.get("lam")
            if mu and row.get("a", 1) >= 1 and row.get("delta"):
                add("census:b13_05", "OPEN", 3, len(mu), row["delta"], mu)

    # ---- s79's length-6 degree-10 record (the inherited queue) -------------
    for row in jsonl("results/s79_per6.jsonl"):
        mu, d = row.get("mu"), row.get("delta")
        if mu is None or d is None:
            continue
        a, m = row.get("a"), row.get("mult")
        v = "CLOSED" if (a is not None and m == a) else ("DROP" if m is not None and m < a else "OPEN")
        add("s79", v, 3, len(mu), d, mu)

    # ---- B13-05: exact top-cell determinants + its degree-8 campaign -------
    tc = jload("results/b13_05_topcells.json")
    if tc:
        rows = tc if isinstance(tc, list) else next(
            (v for v in tc.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])
        for r_ in rows:
            mu = r_.get("mu") or r_.get("lam")
            if mu is None or r_.get("i") != 0:
                continue
            add("B13-05:topcell", "CLOSED", 3, len(mu), r_["delta"], mu,
                "exact integer determinant, catalecticant maximal minor")
    fin = jload("results/b13_05_final.json")
    if fin:
        for c in fin.get("certified_here", []):
            add("B13-05", "CLOSED", 3, len(c["mu"]), c["delta"], c["mu"], "injectivity certificate")
        for o in fin.get("open", []):
            add("B13-05", "OPEN", 3, o.get("ell", len(o["mu"])), o["delta"], o["mu"])
    clo = jload("results/b13_05_closure.json")
    if clo:
        # Theorem D/F structural closures live ONLY here -- final.json carries a
        # count, not a list.  Missing this re-dispatches cells already closed.
        for c in clo.get("derived", []):
            add("B13-05:thmF", "CLOSED", 3, len(c["mu"]), c["delta"], c["mu"],
                "Theorem F product witness: " + str(c.get("witnesses"))[:80])

    # ---- B13-08: the moderate degree-10 remainder --------------------------
    for row in jsonl("results/b13_08/per6_d10.jsonl"):
        a, m = row.get("a"), row.get("mult")
        v = "CLOSED" if m == a else ("DROP" if m is not None and m < a else "OPEN")
        add("B13-08", v, row.get("n", 3), row.get("r", 6), row["delta"], row["mu"])

    # ---- B13-09: lengths 7 and 8 ------------------------------------------
    for path in sorted(glob.glob(os.path.join(ROOT, "results/b13_09/per_r*_d*.jsonl"))):
        for row in jsonl(os.path.relpath(path, ROOT)):
            a, m = row.get("a"), row.get("mult")
            v = "CLOSED" if m == a else ("DROP" if m is not None and m < a else "OPEN")
            add("B13-09", v, row.get("n", 3), row.get("r"), row["delta"], row["mu"])
    for path in sorted(glob.glob(os.path.join(ROOT, "results/b13_09/status_r*_d*.json"))):
        st = json.load(open(path))
        r_, d = st.get("r"), st.get("delta")
        for w in st.get("not_reached", []) + st.get("unreached", []):
            mu = w.get("mu") if isinstance(w, dict) else w
            if mu:
                add("B13-09", "OPEN", 3, r_, d, mu)

    # ---- theorem-level exclusions (the PROVED-index join) -----------------
    inh = jload("results/integrate/inherited_exclusions.json")
    for ex in (inh or {}).get("exclusions", []):
        pr = ex.get("predicate", {})
        if not any(k in pr for k in ("r_max", "delta_max", "r")):
            continue
        for k in list(rec):
            n_, r_, d_, _ = k
            if "n" in pr and n_ != pr["n"]:
                continue
            if "r" in pr and r_ != pr["r"]:
                continue
            if "r_max" in pr and r_ > pr["r_max"]:
                continue
            if "delta_max" in pr and d_ > pr["delta_max"]:
                continue
            rec[k].append((f"PROVED:{ex['id']}", "CLOSED", ex["source"]))

    return rec


def frontier(k):
    n, r, delta, lam = k
    return f"n={n} ell={r} delta={delta}"


def main():
    rec = collect()
    conflicts, drops = [], []
    fr = collections.defaultdict(lambda: {"CLOSED": set(), "OPEN": set(), "DROP": set()})

    for k, entries in rec.items():
        verdicts = {v for _, v, _ in entries}
        closed = "CLOSED" in verdicts
        f = fr[frontier(k)]
        non_census = {v for s_, v, _ in entries if not s_.startswith("census:")}
        if "DROP" in verdicts:
            f["DROP"].add(k); drops.append((k, entries))
        elif closed:
            f["CLOSED"].add(k)
            if "OPEN" in non_census:
                conflicts.append((k, entries))
        else:
            f["OPEN"].add(k)

    print("=" * 78)
    print("CROSS-SESSION CELL RECONCILIATION")
    print("=" * 78)
    print(f"cells seen: {len(rec)}   sources: "
          f"{sorted({s for e in rec.values() for s, _, _ in e})}\n")

    print("--- frontiers: union of closures across all sources ---")
    print(f"{'frontier':<24} {'cells':>6} {'closed':>7} {'open':>6} {'drop':>5}")
    for name in sorted(fr):
        d = fr[name]
        tot = len(d['CLOSED']) + len(d['OPEN']) + len(d['DROP'])
        print(f"{name:<24} {tot:>6} {len(d['CLOSED']):>7} {len(d['OPEN']):>6} {len(d['DROP']):>5}")

    print(f"\n--- OPEN-vs-CLOSED conflicts: {len(conflicts)} ---")
    print("    (one source calls the cell open, another has already closed it;")
    print("     every one of these is work that must not be re-dispatched)")
    by_pair = collections.Counter()
    for k, entries in conflicts:
        o = sorted({s for s, v, _ in entries if v == "OPEN"})
        c = sorted({s for s, v, _ in entries if v == "CLOSED"})
        by_pair[(tuple(o), tuple(c), frontier(k))] += 1
    for (o, c, f), n in sorted(by_pair.items(), key=lambda x: -x[1]):
        print(f"    {n:>4} cells at {f}:  OPEN per {','.join(o)}  ->  CLOSED by {','.join(c)}")

    print(f"\n--- DROPS (candidate permanent-specific equations): {len(drops)} ---")
    for k, entries in drops[:20]:
        print("   ", k, entries)
    if not drops:
        print("    none.")

    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        payload = {
            "cells": len(rec),
            "frontiers": {name: {v: sorted(map(list, s)) for v, s in d.items()} for name, d in fr.items()},
            "conflicts": [{"cell": list(k), "entries": e} for k, e in conflicts],
            "drops": [{"cell": list(k), "entries": e} for k, e in drops],
        }
        json.dump(payload, open(out, "w"), indent=1)
        print(f"\nwritten: {out}")
    return 1 if drops else 0


if __name__ == "__main__":
    sys.exit(main())
