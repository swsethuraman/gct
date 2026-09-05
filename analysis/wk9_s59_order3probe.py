#!/usr/bin/env python3
"""
Session 59 -- order-3 solvability probe (the stopping-rule evidence).

To push contact order from 2 to 3 with EXACT cancellation, an arc needs
g_1 == 0 AND g_2 == 0. With M_0 in a stratum and M_1 in the g_1==0 space,
    g_2 = tr(adj M_0 M_2) + e_2(M_0; M_1),
linear in M_2, with e_2 QUADRATIC in M_1. g_2 == 0 asks tr(adj M_0 M_2) =
-e_2(M_1); solvable in M_2 iff -e_2(M_1) lies in image(M_2 |-> tr(adj M_0 M_2)),
a fixed low-dim (rank r0) subspace of the 70 quartics. For a generic M_1 in the
g_1==0 space this FAILS -- so reaching q=3 forces M_1 into the proper subvariety
{ e_2(M_1) in image }, which is cut out by (70 - r0) equations QUADRATIC in M_1.
That nonlinear locus is the higher Rees relation; solving it needs a Groebner /
elimination engine (no CAS here). This probe measures, at each stratum, the
codimension of the obstruction -- i.e. how far a generic order-2 arc is from
extending -- and thus why the order-by-order route halts at order 2 in
python-flint alone.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk9_s59_core import (R, n, NQ, S5DEG0, det_arc, pencils_to_entry,
                          rank_mod, quartic_vec, stratum_E_basis, STRATA)
from wk9_s59_order2 import m0_from, gen_from, g12

P1, P2 = 2147483647, 2147483629

def image_rank_M2(Eb, cpar, p):
    """rank of M_2 |-> tr(adj M_0 M_2) = g_2 with M_1=0 (the order-1 map, M_0 fixed)."""
    zero = [[[0]*n for _ in range(n)] for _ in range(R)]
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                _, g2 = g12(Eb, cpar, zero, zero, p, dual=('m2', k, a, b))
                cols.append(g2)
    return cols  # 80 columns, 70-dim

def probe(name, p, seed=5, ntest=6):
    rng = random.Random(seed)
    Eb = stratum_E_basis(name, rng, p); m = len(Eb)
    cpar = [[rng.randint(1, p-1) for _ in range(m)] for _ in range(R)]
    zero = [[[0]*n for _ in range(n)] for _ in range(R)]
    # image of M_2 -> tr(adj M_0 M_2)
    imgcols = image_rank_M2(Eb, cpar, p)
    r0 = rank_mod(imgcols, NQ, p)                      # dim of image (M_0 fixed)
    Img = nmod_mat(len(imgcols), NQ,
                   [int(imgcols[j][c]) for j in range(len(imgcols)) for c in range(NQ)], p)
    # g_1==0 nullspace basis for M_1
    g1cols = []; idx = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                g1, _ = g12(Eb, cpar, zero, zero, p, dual=('m1', k, a, b))
                g1cols.append(g1); idx.append((k, a, b))
    A = nmod_mat(NQ, len(g1cols), [int(g1cols[j][r]) for r in range(NQ) for j in range(len(g1cols))], p)
    Xns, nul = A.nullspace()
    # for several generic M_1 in the nullspace, test if e_2(M_1) in image
    solvable = 0; codims = []
    for _ in range(ntest):
        m1 = [[[0]*n for _ in range(n)] for _ in range(R)]
        for t in range(nul):
            w = rng.randint(1, p-1)
            for r, (k, a, b) in enumerate(idx):
                m1[k][a][b] = (m1[k][a][b] + w*int(Xns[r, t])) % p
        _, e2 = g12(Eb, cpar, m1, zero, p)             # g_2 with M_2=0 = e_2(M_1)
        # is -e2 in column space of Img ?  rank[Img rows ; e2] == r0 ?
        rows = [imgcols[j] for j in range(len(imgcols))] + [e2]
        rk = rank_mod(rows, NQ, p)
        if rk == r0: solvable += 1
        codims.append(rk - r0)                          # 0 = solvable, 1 = obstructed
    return dict(name=name, dimE=m, image_rank=r0, g1_nullity=nul,
                solvable=solvable, ntest=ntest, obstruction_codim=codims)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--out', default='results/s59_order3probe.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    res = {}
    for p in primes:
        res[str(p)] = {}
        for name in STRATA:
            r = probe(name, p)
            res[str(p)][name] = r
            print(f"[p={p}] {name:5s} image_rank(M0 fixed)={r['image_rank']:2d} "
                  f"g1_nullity={r['g1_nullity']:2d} "
                  f"order3-extendable at generic M_1: {r['solvable']}/{r['ntest']} "
                  f"(codim {set(r['obstruction_codim'])})", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
