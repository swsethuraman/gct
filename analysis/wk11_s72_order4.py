#!/usr/bin/env python3
"""
Session 72 -- Residue 3: contact order 4 at the incidences.

s66 measured contact orders 1, 2, 3 at every incidence and the reducible
fixed-factor image stabilised (order 2 = order 3 at all of them; s59 showed
order 1..4 invariant at the generic strata).  This module extends the arc to
order 4 at the incidences where the order-3 image is largest (ker cap coker 29,
SP cap c21 and SP cap coker 28), to confirm no climb from order 3 to 4.

The arc  M_0(theta) + t M_1 + t^2 M_2 + t^3 M_3 + t^4 M_4  with M_1 in a tangent
space T_i is built by solving  g_2 = 0, g_3 = 0  fully (dPhi(M_j) = -c_j, with
the kernel freedom of each M_j carried as free parameters) and  pi g_4 = 0, then
the fixed-factor image is  rank d(g_1,g_2,g_3,g_4) - rank d(g_1,g_2,g_3,pi g_4)
over (theta, M_1-jet, the carried kernel freedoms, M_4).
"""
import sys, json, argparse, random, zlib
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import family, all_g, pencil_int, solve_aug
from wk10_s66_order2 import tangents_at
from wk10_s66_bilinear import rref_basis

def order4_image(spec, comp, seed, p, verbose=True):
    rng = random.Random(seed*7919 + zlib.crc32((spec+comp).encode()) % 1000 + 4)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); kerB = kernel_basis(dP); k = len(kerB)
    dcols = [[int(dP[i, j]) for i in range(NQ)] for j in range(80)]
    _, T = tangents_at(spec, theta, p, rng)
    if comp not in T: return dict(spec=spec, comp=comp, note='no such component')
    zero = pencil_zero(Fp(p))
    # M_1 generic in T_comp
    basis = rref_basis(T[comp], 80, p); m1v = [0]*80
    for v in basis:
        c = rng.randint(1, p-1)
        for r_ in range(80): m1v[r_] = (m1v[r_] + c*v[r_]) % p
    M1 = vec_pencil(m1v)
    g1, g2c = all_g(build, theta, [M1, zero], 2, p)
    if any(g1): return dict(spec=spec, comp=comp, note='M1 not in kernel')
    # solve g_2 = 0 : dPhi(M2) = -e2(M1)   (M1 in T_i => solvable)
    part2 = solve_aug(dcols, g2c, NQ, p)
    if part2 is None: return dict(spec=spec, comp=comp, note='g2=0 unsolvable (M1 not 2nd-order solvable)')
    m2p = [v % p for v in part2]
    # carry M2 kernel freedom: M2 = m2p + sum f2_c kerB[c]
    # solve g_3 = 0 : g_3 affine in M3 (via dPhi) and depends on M2 (through the
    # kernel freedoms f2).  We need c_3(f2) in im dPhi; that is a linear condition
    # on f2.  Build g_3's constant + its f2-dependence + its M3-dependence, then
    # solve jointly for (f2, M3) so that g_3 == 0 fully.
    M2p = vec_pencil(m2p)
    g1, g2, g3c = all_g(build, theta, [M1, M2p, zero], 3, p)
    assert not any(g1) and not any(g2)
    # columns: d g_3 / d f2_c  (move M2 by kerB[c]); d g_3 / d M3 (= dPhi cols)
    cols_f2 = []
    for v in kerB:
        Dp = vec_pencil(v)
        gp = all_g(build, theta, [M1, pencil_add(Fp(p), M2p, Dp), zero], 3, p)[2]
        cols_f2.append([(gp[i] - g3c[i]) % p for i in range(NQ)])
    cols_M3 = [[int(dP[i, j]) for i in range(NQ)] for j in range(80)]
    allcols = cols_f2 + cols_M3
    part3 = solve_aug(allcols, g3c, NQ, p)          # solve g_3 == 0 fully
    if part3 is None:
        return dict(spec=spec, comp=comp, note='g3=0 not solvable in (f2,M3): order-3 obstructed for this component')
    f2 = [part3[c] % p for c in range(k)]
    m3p = [part3[k + j] % p for j in range(80)]
    # PARTICULAR M2, M3 (g_2 = g_3 = 0 exactly)
    m2v = list(m2p)
    for c in range(k):
        for r_ in range(80): m2v[r_] = (m2v[r_] + f2[c]*kerB[c][r_]) % p
    M2f = vec_pencil(m2v); M3f = vec_pencil(m3p)
    g1, g2, g3 = all_g(build, theta, [M1, M2f, M3f], 3, p)
    assert not any(g1) and not any(g2) and not any(g3), "arc not order-4 base"
    # solve pi g_4 = 0 for M4 alone (M4 enters g_4 linearly via dPhi(M4))
    g1, g2, g3b, g4c = all_g(build, theta, [M1, M2f, M3f, zero], 4, p)
    const = [g4c[i] for i in S5DEG0]
    cols4 = []
    for kk in range(R):
        for a_ in range(n):
            for b_ in range(n):
                gp = all_g(build, theta, [M1, M2f, M3f, zero], 4, p, dual=('m', 4, kk, a_, b_))[3]
                cols4.append([gp[i] for i in S5DEG0])
    part4 = solve_aug(cols4, const, len(S5DEG0), p)
    if part4 is None:
        return dict(spec=spec, comp=comp, note='pi g4 = 0 unsolvable')
    m4v = [v % p for v in part4]
    X4, nul4 = nmod_mat(len(S5DEG0), 80, [int(cols4[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
    for t in range(nul4):
        c = rng.randint(1, p-1)
        for r_ in range(80): m4v[r_] = (m4v[r_] + c*int(X4[r_, t])) % p
    M4 = vec_pencil(m4v)
    g = all_g(build, theta, [M1, M2f, M3f, M4], 4, p)
    assert not any(g[0]) and not any(g[1]) and not any(g[2]) and not any(g[3][i] for i in S5DEG0), "not a valid order-4 V-point"
    g4_in_im = solve_aug(dcols, [(-x) % p for x in g[3]], NQ, p) is not None
    # image Jacobian over (theta, M1, M2, M3, M4)  vs constrained (pi g_4)
    rows_full = []; rows_con = []
    params = [('t', i) for i in range(len(theta))] + \
             [('m', j, kk, a_, b_) for j in (1, 2, 3, 4) for kk in range(R) for a_ in range(n) for b_ in range(n)]
    for pr in params:
        gg = all_g(build, theta, [M1, M2f, M3f, M4], 4, p, dual=pr)
        rows_full.append(gg[0] + gg[1] + gg[2] + gg[3])
        rows_con.append(gg[0] + gg[1] + gg[2] + [gg[3][i] for i in S5DEG0])
    rf = rank_mod(rows_full, 4*NQ, p); rc = rank_mod(rows_con, 3*NQ + len(S5DEG0), p)
    return dict(spec=spec, comp=comp, seed=seed, p=p, g4_nonzero=any(g[3]), g4_in_im_dPhi=g4_in_im,
                rank_full=rf, rank_con=rc, order4_image=rf - rc)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--targets', default='ker_coker:ker,ker_coker:coker,SP_c21:c21,SP_coker:coker,c21_c32:c21')
    ap.add_argument('--primes', default='2147483647,2147483629')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s72_order4.json')
    a = ap.parse_args()
    res = []
    for tgt in a.targets.split(','):
        spec, comp = tgt.split(':')
        for p in [int(x) for x in a.primes.split(',')]:
            for seed in [int(x) for x in a.seeds.split(',')]:
                r = order4_image(spec, comp, seed, p)
                r.setdefault('spec', spec); r.setdefault('comp', comp)
                r['p'] = p; r['seed'] = seed
                res.append(r); json.dump(res, open(a.out, 'w'), indent=1)
                print(f"[{spec}:{comp} p={p} seed={seed}] order-4 image = {r.get('order4_image')}  {r.get('note','')}", flush=True)
    print("wrote", a.out)
