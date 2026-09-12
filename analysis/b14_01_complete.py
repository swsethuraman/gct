#!/usr/bin/env python3
"""B14-01 -- targeted completion.  Loads the merged basis, finds the blocks whose
directed members still span less than the banked a_3(mu), and searches ONLY those,
stratified over the tall-column overlap k.  Accepts only rank-raising members.
Checkpoints after every acceptance, so a bounded run never loses its work -- the
S1/S2/S3 runner wrote only at the end, which is a defect recorded in the report."""
import argparse, json, os, random, sys, time
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from b14_01_mixed import (MixedFilling, strip_filling_k, mixed_eval_c, rank_mod,
                          strip_ell_cells, random_mixed_filling)
from b14_01_controls import horiz_strips
from b14_01_run import load_points, msyms, CFG
from wk8_s30_core import P1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=13)
    ap.add_argument("--seed", type=int, default=4242)
    ap.add_argument("--max-seconds", type=float, default=2400)
    ap.add_argument("--inp", default=None)
    a = ap.parse_args()
    C = CFG[a.degree]
    h, n2, n1, delta, r, DIM = C["h"], C["n2"], C["n1"], C["delta"], C["r"], C["dim"]
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    inp = a.inp or os.path.join(ROOT, "results", "b14_01", f"members_d{delta}_merged.json")
    D = json.load(open(inp))
    meta, prim = load_points(C["pts"], "primary")
    MS = msyms(prim, r, P1)
    probe = MS[:3]
    S = horiz_strips(lam, delta, r)
    a3 = C["a3"] or [None] * len(S)
    rng = random.Random(a.seed)
    t0 = time.time()

    mat = list(D["rows_P1"])
    keep = list(D["members"])
    seen = {json.dumps(m["filling"], sort_keys=True) for m in keep}
    by = defaultdict(list)
    for m, row in zip(D["members"], D["rows_P1"]):
        if m.get("mu"): by[tuple(m["mu"])].append(row)

    def deficits():
        out = []
        for i, mu in enumerate(S):
            rk = rank_mod(by[tuple(mu)], P1) if by[tuple(mu)] else 0
            if a3[i] and rk < a3[i]: out.append((tuple(mu), a3[i] - rk))
        return out

    dfc = deficits()
    print("initial rank %d/%d; deficient blocks: %s" % (len(mat), DIM,
          ", ".join(f"{mu}:-{d}" for mu, d in dfc) or "none"), flush=True)

    out = os.path.join(ROOT, "results", "b14_01", f"members_d{delta}_completed_{a.seed}.json")

    def save():
        json.dump(dict(degree=delta, target_dim_adopted=DIM, rank_P1=len(mat),
                       members=keep, rows_P1=mat,
                       elapsed_s=round(time.time() - t0, 1)), open(out, "w"))

    tried = 0
    while time.time() - t0 < a.max_seconds and len(mat) < DIM:
        dfc = deficits()
        targets = [mu for mu, _ in dfc] or [tuple(x) for x in S]
        for mu in targets:
            for k in list(range(h + 1)):
                if time.time() - t0 > a.max_seconds or len(mat) >= DIM: break
                mode = rng.random()
                if mode < 0.6:
                    cells = strip_ell_cells(lam, list(mu), h, n2, n1, rng)
                    F = strip_filling_k(h, n2, n1, delta, cells, k, rng)
                else:
                    allc = ([(0, q) for q in range(h)] + [(1, q) for q in range(h)]
                            + [(2 + e, q) for e in range(n2) for q in (0, 1)]
                            + [(2 + n2 + c, 0) for c in range(n1)])
                    bycol = {}
                    for cl in allc: bycol.setdefault(cl[0], []).append(cl)
                    cols = list(bycol); rng.shuffle(cols)
                    cells = [rng.choice(bycol[c]) for c in cols[:delta]]
                    F = strip_filling_k(h, n2, n1, delta, cells, k, rng)
                tried += 1
                if F is None: continue
                key = json.dumps(F.to_json(), sort_keys=True)
                if key in seen: continue
                seen.add(key)
                if not any(mixed_eval_c(F, ms, P1, r=r) for ms in probe): continue
                row = [mixed_eval_c(F, ms, P1, r=r) for ms in MS]
                if not any(row): continue
                if rank_mod(mat + [row], P1) <= len(mat): continue
                mat.append(row)
                keep.append(dict(phase="S3c-complete", mu=list(mu), k=k, filling=F.to_json()))
                by[mu].append(row)
                save()
                print(f"[{time.time()-t0:7.1f}s] rank {len(mat)}/{DIM} (mu={mu}, k={k}, {tried} tried)", flush=True)
    save()
    print(f"[{time.time()-t0:7.1f}s] FINAL rank {len(mat)}/{DIM}, {tried} tried -> {out}", flush=True)


if __name__ == "__main__":
    main()
