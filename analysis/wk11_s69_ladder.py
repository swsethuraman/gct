#!/usr/bin/env python3
"""Session 69: the LADDER spanner -- span M_lambda by climbing, not by sampling from scratch.

Lemma L (s57): multiplication by u = e_1^n (the s_1^n coefficient functional) is injective
M_{delta-1} -> M_delta.  In filling terms u.F is F with one new letter placed as n height-1
columns (all index 1).  Verified identity (wk11_s69_ladder validation): for any filling F and
form f,   (u.F)(f) = F(f) * n! * f_{(n,0,..)} .  So at a FIXED set of points, climbing is a
diagonal scaling of the evaluation row by  ufac[point] := f_{(n,0,..)}  (the n! is a global
constant per step, dropped -- it does not change any rank or kernel).

Therefore a spanning set of M_{delta_top} is built rung by rung: carry the lower basis up for
free (scale its rows), and at each rung sample only for the  a_delta - a_{delta-1}  NEW
directions.  This replaces one a_top-dimensional coupon-collector problem (which concentrates,
session 69 R-LMR) by a sequence of small ones, and makes the last rungs -- where M_delta /
u.M_{delta-1} is 1- or few-dimensional -- trivial: almost any fresh filling completes them.

Generic-side rank uses the scaling trick (native row lifted by ufac^{top-delta}); the det side
evaluates the ACTUAL climbed delta_top fillings at det pencils, so the basis and any kernel
vector U_D are genuine delta_top bracket circuits.

    python3 analysis/wk11_s69_ladder.py --n 3            # validate on the n=3 ladder (a=6)
    python3 analysis/wk11_s69_ladder.py --n 4            # the LMR cell (a=274), checkpointed

State: results/s69_ladder_n<n>.json (resumable).
"""
import argparse, json, math, os, random, sys, time
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import exps, P1, P2                                       # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs, generic_point,
                              det_point, dp_eval_c, rank_mod, left_kernel_mod, reconstruct_integer_vector)  # noqa: E402

T0 = time.time()
_MS = None; _TAB = None; _P = None


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def _init(msyms, tab, p):
    global _MS, _TAB, _P
    _MS = msyms; _TAB = tab; _P = p


def _eval_native(args):
    """evaluate a native filling (dict) at all _MS points; short-circuit on the first."""
    Fj = args
    F = Filling.from_json(Fj)
    v0 = dp_eval_c(F, _MS[0], _P, _TAB)
    if v0 == 0:
        return None
    return [v0] + [dp_eval_c(F, ms, _P, _TAB) for ms in _MS[1:]]


# ------------------------------------------------------------------ ladder parameters
def ladder_params(n):
    if n == 3:
        return dict(n=3, r=7, h=7, n2=5, deltas=list(range(9, 13)),          # a = 2,4,5,6
                    a={9: 2, 10: 4, 11: 5, 12: 6}, top=12, lam_top=(19, 7, 2, 2, 2, 2, 2))
    if n == 4:
        a = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255, 20: 264,
             21: 269, 22: 272, 23: 273, 24: 274}
        return dict(n=4, r=9, h=9, n2=15, deltas=list(range(12, 25)), a=a, top=24,
                    lam_top=(65, 17, 2, 2, 2, 2, 2, 2, 2))
    raise ValueError(n)


def n1_of(P, delta):
    # lambda' = (h,h,2^{n2},1^{n1}); n1 = n*delta - 2h - 2*n2
    return P["n"] * delta - 2 * P["h"] - 2 * P["n2"]


def climb_to_top(F, P):
    """the actual delta_top filling: F plus (top-delta) e_1^n letters, each n one-columns
    with a fresh letter index."""
    top = P["top"]; n = P["n"]
    one = list(F.one); nxt = F.delta
    for step in range(top - F.delta):
        one += [nxt] * n; nxt += 1
    return Filling(P["h"], n, top, F.C1, F.C2, F.two, one)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--npts", type=int, default=300)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--batch", type=int, default=120)
    ap.add_argument("--kset", default="")
    ap.add_argument("--maxbatch_per_rung", type=int, default=60)
    ap.add_argument("--seed", type=int, default=6969)
    ap.add_argument("--prime", type=int, default=P1)
    args = ap.parse_args()
    P = ladder_params(args.n)
    n, r, h, top = P["n"], P["r"], P["h"], P["top"]
    p = args.prime
    A, idx, fact, tab = sym_table(n, r)
    NPTS = args.npts
    kset = [int(x) for x in args.kset.split(",")] if args.kset else (list(range(5, h + 1)) if n == 3 else list(range(6, h + 1)))

    # fixed generic points with nonzero s_1^n coefficient (so ufac != 0)
    e_top = tuple([n] + [0] * (r - 1)); i_top = idx[e_top]
    pts = []; i = 0
    while len(pts) < NPTS:
        cv = generic_point(n, r, p, random.Random(69 * 1000 + i)); i += 1
        if cv[i_top] % p != 0:
            pts.append(cv)
    msyms = [symbols_from_coeffs(cv, n, r, p) for cv in pts]
    ufac = np.array([cv[i_top] % p for cv in pts], dtype=object)   # per-point s_1^n coeff
    upow = {d: np.array([pow(int(u), top - d, p) for u in ufac], dtype=object) for d in P["deltas"]}

    statef = os.path.join(ROOT, "results", f"s69_ladder_n{n}.json")
    st = json.load(open(statef)) if os.path.exists(statef) else dict(n=n, top=top, a=P["a"], basis=[], rung_log=[])
    basis = st["basis"]           # list of dict(filling=native json, birth=delta)
    rows = []                      # lifted-to-top rows (mod p) for the current basis
    # rebuild lifted rows for any saved basis
    if basis:
        with Pool(args.workers, initializer=_init, initargs=(msyms, tab, p)) as pool:
            native_rows = pool.map(_eval_native, [b["filling"] for b in basis])
        for b, nr in zip(basis, native_rows):
            up = upow[b["birth"]]
            rows.append([int(x) * int(up[j]) % p for j, x in enumerate(nr)])
        log(f"resume: {len(basis)} basis vectors, rank {rank_mod(rows, p)}")
    rank = rank_mod(rows, p) if rows else 0

    rng = random.Random(args.seed + len(basis))
    with Pool(args.workers, initializer=_init, initargs=(msyms, tab, p)) as pool:
        for delta in P["deltas"]:
            target = P["a"][delta]
            n1 = n1_of(P, delta)
            rung_batches = 0
            while rank < target and rung_batches < args.maxbatch_per_rung:
                batch = [random_filling(h, n, delta, P["n2"], n1, rng, k=rng.choice(kset)).to_json()
                         for _ in range(args.batch)]
                res = pool.map(_eval_native, batch, chunksize=8)
                up = upow[delta]; added = 0; nz = 0
                for Fj, nr in zip(batch, res):
                    if nr is None: continue
                    nz += 1
                    lifted = [int(x) * int(up[j]) % p for j, x in enumerate(nr)]
                    if rank_mod(rows + [lifted], p) > rank:
                        rows.append(lifted); basis.append(dict(filling=Fj, birth=delta)); rank += 1; added += 1
                        if rank >= target: break
                rung_batches += 1
                st["basis"] = basis; st["rank"] = rank
                json.dump(st, open(statef + ".tmp", "w")); os.replace(statef + ".tmp", statef)
                log(f"  delta={delta} target {target}: batch {len(batch)}, {nz} nonzero, +{added} -> rank {rank}")
            st["rung_log"].append(dict(delta=delta, target=target, rank=rank, batches=rung_batches))
            json.dump(st, open(statef + ".tmp", "w")); os.replace(statef + ".tmp", statef)
            if rank < target:
                log(f"  delta={delta}: STUCK at rank {rank} < {target} after {rung_batches} batches"); break
            log(f"delta={delta}: rank {rank}/{target} DONE")
    st["generic_rank"] = rank
    json.dump(st, open(statef, "w"))
    log(f"generic spanning: rank {rank} of {P['a'][top]}")


if __name__ == "__main__":
    main()
