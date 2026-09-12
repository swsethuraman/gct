#!/usr/bin/env python3
"""B14-01 -- pool the members found by the concurrent searches and build one
greedy independent basis.  Rank is rank: pooling candidates from searches with
different seeds and different directed parameters is legitimate, and every
member keeps the phase label it was found under (S1/S2 pre-registered, S3 and
S3b exploratory)."""
import argparse, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from b14_01_mixed import rank_mod
from b14_01_run import CFG
from wk8_s30_core import P1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=13)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    C = CFG[a.degree]; DIM = C["dim"]; delta = C["delta"]
    files = []
    f0 = os.path.join(ROOT, "results", "b14_01", f"members_d{delta}.json")
    if os.path.exists(f0): files.append(f0)
    files += sorted(glob.glob(os.path.join(ROOT, "results", "b14_01", f"harvest_d{delta}_*.json")))
    pool = []
    for fn in files:
        D = json.load(open(fn))
        ph = "S1/S2/S3" if os.path.basename(fn).startswith("members") else "S3b"
        for m, row in zip(D["members"], D["rows_P1"]):
            pool.append((m.get("phase", ph), m, row, os.path.basename(fn)))
    print(f"pooled {len(pool)} members from {len(files)} file(s)")
    mat = []; keep = []
    seen = set()
    for ph, m, row, src in pool:
        k = json.dumps(m["filling"], sort_keys=True)
        if k in seen: continue
        seen.add(k)
        if not any(row): continue
        if rank_mod(mat + [row], P1) <= len(mat): continue
        mat.append(row); keep.append(dict(phase=ph, mu=m.get("mu"), k=m.get("k"),
                                          filling=m["filling"], source=src))
        if len(mat) >= DIM: break
    print(f"merged rank over P1 = {len(mat)} / {DIM}  (from {len(seen)} distinct members)")
    out = a.out or os.path.join(ROOT, "results", "b14_01", f"members_d{delta}_merged.json")
    json.dump(dict(degree=delta, target_dim_adopted=DIM, rank_P1=len(mat),
                   n_pooled=len(seen), sources=[os.path.basename(f) for f in files],
                   members=keep, rows_P1=mat), open(out, "w"))
    print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()


def per_strip_report(delta=13):
    """which blocks are short: rank of the members directed at each strip mu,
    against the banked a_3(mu, delta).  A block whose directed members span less
    than a_3 is where the search still owes directions."""
    C = CFG[delta]
    fn = os.path.join(ROOT, "results", "b14_01", f"members_d{delta}_merged.json")
    D = json.load(open(fn))
    from collections import defaultdict
    by = defaultdict(list)
    for m, row in zip(D["members"], D["rows_P1"]):
        by[tuple(m["mu"])].append(row)
    a3 = C["a3"]
    from b14_01_controls import horiz_strips
    lam = tuple([2 + C["n2"] + C["n1"], 2 + C["n2"]] + [2] * (C["h"] - 2))
    S = horiz_strips(lam, delta, C["r"])
    short = []
    print(f"{'mu':<34} {'a3':>3} {'members':>8} {'rank':>5}")
    for i, mu in enumerate(S):
        rows = by.get(tuple(mu), [])
        rk = rank_mod(rows, P1) if rows else 0
        aa = a3[i] if a3 else None
        flag = "" if (aa is None or rk >= aa) else "  SHORT"
        print(f"{str(mu):<34} {aa if aa is not None else '-':>3} {len(rows):>8} {rk:>5}{flag}")
        if aa is not None and rk < aa: short.append((list(mu), aa, rk))
    print("total accepted:", len(D["members"]), " rank:", D["rank_P1"], "/", C["dim"])
    return short
