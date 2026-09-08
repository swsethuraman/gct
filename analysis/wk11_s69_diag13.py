#!/usr/bin/env python3
"""Diagnostic: can delta=13 be spanned to rank 39 (a_13) with different k-sets / heavy sampling?
Parallel.  Tells sampler-limitation from fundamental concentration."""
import sys, os, random, time, json
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk11_s69_circuit import *
n, r, h, p = 4, 9, 9, P1
A, idx, fact, tab = sym_table(n, r)
e = tuple([4] + [0] * 8); it = idx[e]
NP = 55
pts = []; i = 0
while len(pts) < NP:
    cv = generic_point(n, r, p, random.Random(69000 + i)); i += 1
    if cv[it] % p: pts.append(cv)
MS = [symbols_from_coeffs(cv, n, r, p) for cv in pts]
UP11 = [pow(cv[it] % p, 11, p) for cv in pts]
UP12 = [pow(cv[it] % p, 12, p) for cv in pts]


def ev(Fj):
    F = Filling.from_json(Fj)
    v0 = dp_eval_c(F, MS[0], p, tab)
    if v0 == 0: return None
    return [v0] + [dp_eval_c(F, m, p, tab) for m in MS[1:]]


def main():
    ksets = {"5-9": [5, 6, 7, 8, 9], "5": [5], "9": [9], "6-9": [6, 7, 8, 9]}
    with Pool(2) as pool:
        # seed: 2 delta=12 vectors
        rng = random.Random(1); seeds = [random_filling(h, n, 12, 15, 0, rng, k=rng.choice([6, 7, 8, 9])).to_json() for _ in range(60)]
        srows = [r_ for r_ in pool.map(ev, seeds) if r_]
        seed_rows = []
        for r_ in srows:
            lifted = [r_[j] * UP12[j] % p for j in range(NP)]
            if rank_mod(seed_rows + [lifted], p) > len(seed_rows): seed_rows.append(lifted)
            if len(seed_rows) >= 2: break
        print("seed rank", rank_mod(seed_rows, p), flush=True)
        for name, kset in ksets.items():
            rng = random.Random(7); rows = list(seed_rows); tot = 0
            for rd in range(12):
                batch = [random_filling(h, n, 13, 15, 4, rng, k=rng.choice(kset)).to_json() for _ in range(80)]
                res = pool.map(ev, batch, chunksize=8); tot += 80
                for r_ in res:
                    if not r_: continue
                    lifted = [r_[j] * UP11[j] % p for j in range(NP)]
                    if rank_mod(rows + [lifted], p) > len(rows): rows.append(lifted)
                rk = rank_mod(rows, p)
                if rk >= 39 or rd == 11:
                    print(f"kset={name}: rank {rk}/39 after {tot} samples", flush=True); break
                if rd % 2 == 1:
                    print(f"  kset={name}: rank {rk}/39 at {tot} samples", flush=True)


if __name__ == "__main__":
    main()
