#!/usr/bin/env python3
"""
Session 36 -- the point-free reducibility multiplicity  mult_red(lam, delta).

Theorem (proved in docs/stabiliser_reduction.md section 4; post-hoc to the
first bite, labelled so).  Let X_r = closure{l . c} in Sym^4 C^r be the
reducible-with-a-linear-factor locus, and L_i = {F : x_i | F} = the coordinate
subspace {c_alpha = 0 for all alpha with alpha_i = 0}.  For a highest-weight
vector v (a B-eigenvector), Bruhat's G = B W P_i gives

    v in I(X_r)  <=>  v in I(L_i) for every i  <=>  every monomial of v has,
                      for every i in [r], a factor c_alpha with alpha_i = 0.

So with M_red = {weight-lam monomials with that property} (a Stab-invariant set),

    mult_red(lam, delta) := a - dim( HWV_lam ∩ span M_red )

is computable from the HWV kernel alone, with no evaluation points.  At r = 5,
D_5^pad = X_5 (per_3-pencils are dense in quinary cubics; dim 39 = 5 + 35 - 1),
so mult_pad = mult_red EXACTLY -- a point-free cross-check of every ell = 5
measurement.  At r = 6, D_6^pad is a proper subvariety of X_6 (55 < 61), so
mult_pad <= mult_red, and a strict gap is precisely a permanent-specific
equation (the prereg's sharper falsifier, in exact form).

usage: python3 wk9_s36_red.py [cell pickles...]   (default: all in /root/s36)
"""
import sys, os, glob, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s36_stabred import orbit_setup, exps, monomials, nmod_mat, P1, P2

def is_red(m, A, r):
    return all(any(A[k][i] == 0 for k in m) for i in range(r))

def mult_red(out):
    lam = out['lam']; r = len(lam); delta = sum(lam) // 4; a = out['a']
    A = exps(4, r)
    basis, vecs, group = orbit_setup(4, r, delta, lam, verbose=False)
    assert len(vecs) == out['n_chi']
    nonred = [j for j, vec in enumerate(vecs) if not is_red(next(iter(vec)), A, r)]
    # sanity: an orbit is entirely red or entirely non-red
    for j in nonred[:50]:
        assert not any(is_red(m, A, r) for m in vecs[j])
    res = {}
    for p in (P1, P2):
        kern = out['per_prime'][p]['kern']
        if a == 0: res[p] = 0; continue
        rows = [[kv[j] % p for j in nonred] for kv in kern]          # a x |nonred|
        rk = nmod_mat(a, len(nonred), [v for rw in rows for v in rw], p).rank()
        res[p] = rk       # = a - dim(HWV ∩ span M_red)
    assert res[P1] == res[P2], (lam, res)
    monomials.cache_clear()
    return res[P1], len(nonred), len(vecs) - len(nonred)

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob('/root/s36/cell_*.pkl'))
    print("| lam | delta | ell | a | mult_det | mult_pad (points) | mult_red (point-free) | red orbits / n_chi | reading |")
    print("|---|---|---|---|---|---|---|---|---|")
    for fn in files:
        out = pickle.load(open(fn, 'rb'))
        lam = out['lam']; r = len(lam); delta = sum(lam) // 4
        mr, nnr, nr = mult_red(out)
        if r == 5:
            reading = "pad = red, as the theorem requires" if mr == out['mult_pad'] else "**MISMATCH**"
        else:
            reading = ("pad = red: no permanent-specific equation" if mr == out['mult_pad']
                       else f"**pad < red: permanent-specific equation(s), {mr - out['mult_pad']}**")
        print(f"| `{lam}` | {delta} | {r} | {out['a']} | {out['mult_det']} | {out['mult_pad']} | {mr} | {nr} / {out['n_chi']} | {reading} |")
        sys.stdout.flush()
