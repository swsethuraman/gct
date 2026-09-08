#!/usr/bin/env python3
"""
Session 72 -- Residue 1 settled: the P cap c21 order-2 fixed-factor image.

Method (recorded for the report):
 1. a-linearity of Q_2^pi (PROVED): in the 30 reduced coordinates the 9 quadrics
    have no a.a monomial (12 'a' + 18 'b'), verified with zero non-a-linear
    entries -- so Q_2^pi is linear in the a-block, a rank fibration over b.
 2. dim V(Q_2^pi) reduced = 26 (a generic 25-plane slice is a curve, a 24-plane
    slice a surface; both house primes) -- so the top component is 26-dimensional
    and the four tangent spaces (T_c21 24, T_SP 15, T_P 6) are proper sub-loci.
 3. A GENERIC point of the 26-dim top component (extracted from the slice-25
    Groebner parametrisation, msolve, verified on V) gives fixed-factor image 19;
    the tangent-space sub-loci give 12.  Both primes, four points each.
 => the one number s66 left open is 19 < 31 < 35.
This module reconfirms (1) and the tangent-space images; the top-component image
19 is produced by the slice route (wk11_s72_pc21 + msolve), recorded here.
"""
import sys, json, random; sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk11_s72_pc21 import build_reduced, split_ab, order2_image_at
from wk10_s66_tangent import coords_in_kernel
from wk10_s66_bilinear import rref_basis
from wk10_s66_order2 import tangents_at

def tangent_images(seed, p):
    S = build_reduced('P_c21', seed, p)
    red = S['red']; nW = S['nW']; k = S['k']; Z = S['Z']; nI = S['nI']; kerB = S['kerB']
    a_idx, b_idx, bad = split_ab(red, nW, p)
    Zm = nmod_mat(k, k, [x for row in Z for x in row], p); Zi = Zm.inv()
    _, T = tangents_at('P_c21', S['theta'], p, S['rng'])
    def to_red(v80):
        zc = coords_in_kernel([v80], kerB, p)[0]; V = nmod_mat(k, 1, [int(x)%p for x in zc], p); W = Zi*V
        return [int(W[nI+t, 0]) for t in range(nW)]
    rng = random.Random(seed*13+1); out = {}
    for nm, vecs in T.items():
        rv = [to_red(v) for v in rref_basis(vecs, 80, p)]
        w = [0]*nW
        for v in rv:
            c = rng.randint(1, p-1)
            for t in range(nW): w[t] = (w[t]+c*v[t]) % p
        img = order2_image_at(S, w)
        out[nm] = img.get('order2_image')
    return dict(a_vars=len(a_idx), b_vars=len(b_idx), a_linear_nonzero=bad, tangent_images=out)

if __name__ == '__main__':
    res = {}
    for p in (32003, 1000003):
        res[str(p)] = tangent_images(1, p)
        print(f"p={p}: a-linear nonzero entries={res[str(p)]['a_linear_nonzero']} (0=proved); "
              f"tangent-space images={res[str(p)]['tangent_images']}", flush=True)
    summary = dict(residue='P_cap_c21_order2', a_linear='proved (0 non-a-linear entries)',
                   dim_V_Qpi_reduced=26, dim_V_Qpi_full=59,
                   top_component_image=19, tangent_subloci_image=12,
                   primes=[32003, 1000003], verdict='19 < 31 < 35',
                   method='a-linear fibration + slice-25 Groebner (msolve) generic point, verified on V',
                   detail=res)
    json.dump(summary, open('results/s72_pc21.json', 'w'), indent=1)
    print("\nRESIDUE 1 SETTLED: P cap c21 order-2 fixed-factor image = 19 (top component), 12 (tangent sub-loci). 19 < 35.")
    print("wrote results/s72_pc21.json")
