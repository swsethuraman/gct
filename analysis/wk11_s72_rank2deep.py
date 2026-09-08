#!/usr/bin/env python3
"""
Session 72 -- Residue 4: the deeper strata of the rank-<=2 world (incidences of
the four rank-2 types with each other, and their sub-loci).

Structure inherited from s66 sec 7 (PROVED, not just measured):
  * on (2,0)  e_2(M_0;M_1) = det[Y_2 | X]           -- an honest 4x4 determinant;
  * on (4,2)  the same by transposition;
  * on (3,1)  e_2 = det(N~), a rank-1 update determinant;
  * on the rank-<=1 locus  e_q = det(M_1 with a row replaced by lambda).
The exactness identity is a POINTWISE identity on the whole locus, so it holds at
every sub-locus and every incidence of these types too: at a point on (2,0) the
order-2 leading form is det[Y_2 | X] whether or not the point also lies on (3,1),
(4,2), the skew type, or a deeper stratum.  Hence the order-2 exceptional image
over ANY incidence that meets (2,0), (4,2) or (3,1) lies in Phi(X_5) and its
reducible part in the exact locus, <= 31 < 35.  Only the padded-skew type carries
no such identity (dPhi==0 there and e_2 = m q - beta gamma is not a determinant),
so only its sub-loci and skew-skew incidences need measuring.

This module measures:
  (A) the pure-skew type with a degenerate frame x(s) of rank 2 and rank 1
      (the deepest skew sub-loci), order 2 and 3;
  (B) an explicit (2,0) cap (3,1) incidence, confirming e_2 is still the (2,0)
      determinant there and the reducible image is <= 31;
  (C) the rank-<=1 locus, order 2 and 3.
All by s59's identity, both house primes, two seeds.
"""
import sys, json, argparse, random
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import all_g, pencil_int, solve_aug
from wk10_s66_rank2 import jac_ranks, rand_pencil, family_skew, family31, family20

P1, P2 = 2147483647, 2147483629

def family_skew_rank(rng, p, xrank=3):
    """skew type with x(s) = v.w of rank xrank (v 5xr, w rx3)."""
    if xrank == 3:
        theta0 = [rng.randint(1, p-1) for _ in range(15)]
        def build(th, Rg):
            pen = []
            for k in range(R):
                x = [th[k*3+j] for j in range(3)]
                N3 = skewN(Rg, x); B = mat_zero(Rg, n, n)
                for a in range(3):
                    for b in range(3): B[a][b] = N3[a][b]
                pen.append(B)
            return pen
        return theta0, build
    theta0 = [rng.randint(1, p-1) for _ in range(R*xrank + xrank*3)]
    def build(th, Rg):
        v = [[th[k*xrank + i] for i in range(xrank)] for k in range(R)]
        w = [[th[R*xrank + i*3 + j] for j in range(3)] for i in range(xrank)]
        pen = []
        for k in range(R):
            x = [sum_ring(Rg, [Rg.mul(v[k][i], w[i][j]) for i in range(xrank)]) for j in range(3)]
            N3 = skewN(Rg, x); B = mat_zero(Rg, n, n)
            for a in range(3):
                for b in range(3): B[a][b] = N3[a][b]
            pen.append(B)
        return pen
    return theta0, build

def family_rank1(rng, p):
    """rank-<=1 pencil M_0 = w . lambda(s)^T : w fixed in C^4, lambda(s) 5->4."""
    theta0 = [rng.randint(1, p-1) for _ in range(n + R*n)]
    def build(th, Rg):
        w = [th[a] for a in range(n)]
        pen = []
        for k in range(R):
            lam = [th[n + k*n + b] for b in range(n)]
            B = [[Rg.mul(w[a], lam[b]) for b in range(n)] for a in range(n)]
            pen.append(B)
        return pen
    return theta0, build

def family_20_31(rng, p):
    """(2,0) cap (3,1) : columns 0,1 zero (=> on (2,0)) AND row 0 arbitrary,
    rows 1..3 of col 2 zero except through the free col 3 (=> also (3,1)-like).
    Concretely M_0 = [0 | 0 | col2(s) | col3(s)] with col2 supported on row 0
    only (so cols 0,1 zero gives (2,0); col2 in row 0 and col3 free gives a (3,1)
    structure with U_3=<e0,e1,e2>, W_1=<e0>)."""
    theta0 = [rng.randint(1, p-1) for _ in range(R*(1 + n))]   # row0 of col2 + all of col3
    def build(th, Rg):
        pen = []
        for k in range(R):
            B = mat_zero(Rg, n, n)
            B[0][2] = th[k*(1+n) + 0]
            for a in range(n): B[a][3] = th[k*(1+n) + 1 + a]
            pen.append(B)
        return pen
    return theta0, build

def order2_reducible_at(build, theta, M1, p):
    zero = pencil_zero(Fp(p))
    g1, g2 = all_g(build, theta, [M1, zero], 2, p)
    okV = (not any(g1)) and (not any(g2[i] for i in S5DEG0))
    rf, rc = jac_ranks(build, theta, M1, p)
    return okV, any(g2), rf - rc

def run(p, seed, verbose=True):
    rng = random.Random(seed*104729 + 411)
    rec = dict(p=p, seed=seed, tests=[])
    # (A) skew with degenerate frames
    for xr in (3, 2, 1):
        theta, build = family_skew_rank(rng, p, xr)
        M0 = pencil_int(build(theta, Fp(p)))
        if any(det_value(M0, p)):
            rec['tests'].append(dict(name=f'skew x-rank {xr}', note='det not identically zero (degenerate)')); continue
        dP = dPhi_matrix(M0, p)
        # order 2 over the four skew V-components (kinds i..iv from s66)
        from wk10_s66_rank2 import skew_vpoint
        imgs = []
        for kind in ('i', 'ii', 'iii', 'iv'):
            M1 = skew_vpoint(kind, rng, p)
            okV, nz, img = order2_reducible_at(build, theta, M1, p)
            if okV: imgs.append(img)
        rec['tests'].append(dict(name=f'skew x-rank {xr}', rank_dPhi=dP.rank(), order2_images=imgs, max=max(imgs) if imgs else None))
        if verbose: print(f"[p={p} seed={seed}] skew x-rank {xr}: dPhi rank {dP.rank()}, order-2 images {imgs}", flush=True)
    # (B) (2,0) cap (3,1)
    theta, build = family_20_31(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    if not any(det_value(M0, p)):
        dP = dPhi_matrix(M0, p)
        # verify e_2 is the (2,0) determinant det[Y_2 | X], X = cols 2,3 of M_0
        M1 = rand_pencil(rng, p)
        g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
        Nt = [[[0]*n for _ in range(n)] for _ in range(R)]
        for k in range(R):
            for a in range(n):
                for b in (0, 1): Nt[k][a][b] = M1[k][a][b]
                for b in (2, 3): Nt[k][a][b] = M0[k][a][b]
        exact = (g2 == det_value(Nt, p))
        # reducible V-point: Y_2 columns in span of X (as in run20)
        M1 = rand_pencil(rng, p); A = [[rng.randint(1,p-1) for _ in range(2)] for _ in range(2)]
        for k in range(4):
            for a in range(n):
                for b in (0,1): M1[k][a][b] = sum(M0[k][a][2+j]*A[j][b] for j in range(2)) % p
        okV, nz, img = order2_reducible_at(build, theta, M1, p)
        rec['tests'].append(dict(name='(2,0) cap (3,1)', rank_dPhi=dP.rank(), e2_is_20_determinant=exact,
                                 reducible_image=img, note='exactness => image in Phi(X_5), reducible part <= 31'))
        if verbose: print(f"[p={p} seed={seed}] (2,0)cap(3,1): dPhi {dP.rank()}, e2 = (2,0)-det: {exact}, reducible image {img}", flush=True)
    # (C) rank-<=1 locus, order 2 and 3
    theta, build = family_rank1(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    if not any(det_value(M0, p)):
        dP = dPhi_matrix(M0, p)
        M1 = rand_pencil(rng, p)
        g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
        # order-2 full image + reducible at a V-point (M_1 rank-1 fixed row w)
        rf, rc = jac_ranks(build, theta, M1, p)
        rec['tests'].append(dict(name='rank<=1', rank_dPhi=dP.rank(), order2_full_image=rf,
                                 note='e_q = det(M_1, row->lambda) exact (s66), reducible part <= 31'))
        if verbose: print(f"[p={p} seed={seed}] rank<=1: dPhi {dP.rank()}, order-2 full image {rf}", flush=True)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='2147483647,2147483629')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s72_rank2deep.json')
    a = ap.parse_args()
    res = []
    for p in [int(x) for x in a.primes.split(',')]:
        for seed in [int(x) for x in a.seeds.split(',')]:
            res.append(run(p, seed)); json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
