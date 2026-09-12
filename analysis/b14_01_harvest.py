#!/usr/bin/env python3
"""B14-01 -- S3b: harvest live members with the tall-column overlap k stratified.

Pre-registered as part of S3 (the fallback), and therefore reported EXPLORATORY.
Writes every live member and its P1 row; the greedy basis is built afterwards by
merging with the S1/S2 members, so two searches can run concurrently without
sharing state."""
import argparse, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from b14_01_mixed import (strip_filling_k, mixed_eval_c, rank_mod, strip_ell_cells,
                          random_mixed_filling)
from b14_01_controls import horiz_strips
from b14_01_run import load_points, msyms, CFG
from wk8_s30_core import P1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=13)
    ap.add_argument("--seed", type=int, default=770001)
    ap.add_argument("--max-seconds", type=float, default=4200)
    ap.add_argument("--out", default=None)
    ap.add_argument("--mode", default="strip", choices=["strip", "free", "cells"],
                    help="strip = l-letters on the cells of lambda/mu (directed); "
                         "free = UNCONSTRAINED mixed fillings, which is what PREREG "
                         "section 4 S3 actually specifies; "
                         "cells = l-letters on random distinct-column cells, not "
                         "necessarily a horizontal strip")
    a = ap.parse_args()
    C = CFG[a.degree]
    h, n2, n1, delta, r, DIM = C["h"], C["n2"], C["n1"], C["delta"], C["r"], C["dim"]
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    out = a.out or os.path.join(ROOT, "results", "b14_01", f"harvest_d{delta}_{a.mode}_{a.seed}.json")
    meta, prim = load_points(C["pts"], "primary")
    MS = msyms(prim, r, P1)
    probe = MS[:3]
    S = horiz_strips(lam, delta, r)
    rng = random.Random(a.seed)
    t0 = time.time()
    mat = []; keep = []; seen = set(); tried = 0
    ks = list(range(0, h + 1))
    while time.time() - t0 < a.max_seconds and len(mat) < DIM:
        for si, mu in enumerate(S):
            for k in ks:
                if time.time() - t0 > a.max_seconds or len(mat) >= DIM: break
                if a.mode == "strip":
                    cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                    F = strip_filling_k(h, n2, n1, delta, cells, k, rng)
                elif a.mode == "free":
                    try:
                        F = random_mixed_filling(h, n2, n1, delta, delta, rng)
                    except RuntimeError:
                        F = None
                else:
                    allcells = ([(0, q) for q in range(h)] + [(1, q) for q in range(h)]
                                + [(2 + e, q) for e in range(n2) for q in (0, 1)]
                                + [(2 + n2 + c, 0) for c in range(n1)])
                    bycol = {}
                    for cl in allcells: bycol.setdefault(cl[0], []).append(cl)
                    cols = list(bycol); rng.shuffle(cols)
                    cells = [rng.choice(bycol[c]) for c in cols[:delta]]
                    F = strip_filling_k(h, n2, n1, delta, cells, k, rng)
                tried += 1
                if F is None: continue
                key = F.key()
                if key in seen: continue
                seen.add(key)
                if not any(mixed_eval_c(F, ms, P1, r=r) for ms in probe): continue
                row = [mixed_eval_c(F, ms, P1, r=r) for ms in MS]
                if not any(row): continue
                if rank_mod(mat + [row], P1) <= len(mat): continue
                mat.append(row); keep.append((list(mu), k, F.to_json(), row))
                if len(mat) % 10 == 0:
                    print(f"[{time.time()-t0:7.1f}s] rank {len(mat)}/{DIM}  ({tried} tried)", flush=True)
    res = dict(degree=delta, seed=a.seed, rank_P1=len(mat), tried=tried,
               elapsed_s=round(time.time() - t0, 1),
               mode=a.mode,
               members=[dict(mu=m, k=k, mode=a.mode, filling=f) for m, k, f, _ in keep],
               rows_P1=[row for _, _, _, row in keep])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"))
    print(f"[{time.time()-t0:7.1f}s] FINAL rank {len(mat)}/{DIM}, {tried} tried -> {out}", flush=True)


if __name__ == "__main__":
    main()
