#!/usr/bin/env python3
"""
Session 51, section 4 -- identify the GL_r-module of the non-Koszul syzygies as
Lambda^5 V, by the dimension-polynomial argument.

The extra-syzygy space E(V) is a polynomial GL(V)-functor (it is the generic
fibre of a GL(V)-equivariant construction: pick a basis of the pencil = choose an
isomorphism V = C^r, and E transforms accordingly).  Its dimension is therefore a
single polynomial in r on the stable (non-ceiling) range.  We measure it at
r = 2,3,4,5,6,7 -- six points pin a degree-5 polynomial.  If those six values are
C(r,5), then dim E(C^r) = C(r,5) as polynomials, and by linear independence of the
Schur-functor dimension polynomials {dim S_lambda(C^r) : lambda |- 5} the only
non-negative integer combination equal to C(r,5) is S_{1^5} = Lambda^5.

Ceiling caveat: C(r,5) is the drop only where the Gulliksen-Negard ceiling
dim S_d - H_GN(d) does not bind.  We use n=4 (d=7) for r<=6 (checked non-binding),
and the s48 value at (n,r)=(5,7).  r=8 is added at n=6 (d=13) as an
over-determination when it is non-ceiling and affordable.
"""
import sys, os, random, time, gc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (dim_sym, h_smooth, rho_generic, monos, mono_index, pderiv,
   rand_pencil, pencil_entries, det_form, H_GN, P1, P2)
from flint import nmod_mat
from math import comb

def macaulay_rank_lean(F, n, d, r, p):
    idx = mono_index(d, r); mult = monos(d - n + 1, r)
    nc, nr = len(idx), r * len(mult)
    A = nmod_mat(nr, nc, p); i = 0
    for k in range(r):
        g = [(e, c % p) for e, c in pderiv(F, k).items() if c % p]
        for m in mult:
            for e, c in g:
                A[i, idx[tuple(x + y for x, y in zip(e, m))]] = c
            i += 1
    rk = A.rank(); del A; gc.collect()
    return rk

def drop_at(n, r, d, seed, primes=(P1,)):
    rho = rho_generic(d, n, r); ceil_ = dim_sym(d, r) - H_GN(d, n, r)
    binds = ceil_ < rho
    vals = []
    for p in primes:
        rnd = random.Random(seed); A = rand_pencil(n, r, rnd, 10 ** 5)
        ent = pencil_entries(A, n, r); F = det_form(ent, n)
        t = time.time(); rk = macaulay_rank_lean(F, n, d, r, p); dt = time.time() - t
        vals.append((p, rho - rk, dt))
    return rho, ceil_, binds, vals

def main():
    print("# S51 section 4 -- module identification via dim polynomial", flush=True)
    print("# r : n d : drop : C(r,5) : ceiling(binds?)", flush=True)
    pts = []
    for r in (2, 3, 4, 5, 6):
        rho, ceil_, binds, vals = drop_at(4, r, 7, 4200 + r)
        drop = vals[0][1]; pts.append((r, drop))
        print(f"  r={r} : n=4 d=7 : drop={drop} : C(r,5)={comb(r,5)} : ceil={ceil_} rho={rho} binds={binds}  {vals[0][2]:.1f}s", flush=True)
    # r=7 from s48 (5,7): re-derive here at both primes to be self-contained
    rho, ceil_, binds, vals = drop_at(5, 7, 10, 5177, primes=(P1, P2))
    print(f"  r=7 : n=5 d=10 : drop={[v[1] for v in vals]} : C(7,5)={comb(7,5)} : ceil={ceil_} rho={rho} binds={binds}  {[round(v[2],1) for v in vals]}s", flush=True)
    pts.append((7, vals[0][1]))
    # optional over-determination r=8: find a non-ceiling (n,d)
    print("# r=8 ceiling scan (looking for non-binding, affordable):", flush=True)
    for n in (5, 6, 7):
        d = 3 * n - 5
        rho = rho_generic(d, n, 8); ceil_ = dim_sym(d, 8) - H_GN(d, n, 8)
        nrows = 8 * dim_sym(d - n + 1, 8); ncols = dim_sym(d, 8)
        print(f"    n={n} d={d}: rho={rho} ceil={ceil_} binds={ceil_<rho} matrix {nrows}x{ncols}", flush=True)
    print("# polynomial check:", flush=True)
    # fit unique degree-5 polynomial through r=2..7 values and compare to C(r,5)
    rs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    allmatch = all(y == comb(r, 5) for r, y in pts)
    print(f"  measured (r,drop) = {pts}", flush=True)
    print(f"  all equal C(r,5)? {allmatch}", flush=True)

if __name__ == "__main__":
    main()
