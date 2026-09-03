#!/usr/bin/env python3
"""
Session 44, Phase 4.3 -- the singular curve of a generic six-parameter 4x4
pencil, and the module J(M)/J_F.

  * Sing(det M) = Z(M) = {rank M(s) <= 2}, cut by the sixteen 3x3 minors.
    For a generic pencil Kleiman transversality makes this a curve in P^5
    (codimension 4 in P(M_4)).  Its degree is the Harris-Tu number
    nu(4) = 20 and, if J(M) is saturated, H_{S/J(M)}(d) = 20d - 20 for d >> 0,
    i.e. arithmetic genus 21.
  * measured: H_{S/J(M)}(d) against the Gulliksen-Negard prediction, and the
    Hilbert function of Q = J(M)/J_F, the cokernel of the six partials inside
    the sixteen minors.  H_Q(d) = dim J(M)_d - rank M_d.

usage: wk9_s44_locus.py [seed] [dmax]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 8
N, R, BOX = 4, 6, 10 ** 6

if __name__ == '__main__':
    t0 = time.time()
    print(f"[s44 locus] n={N} r={R}, seed {SEED}, primes {PRIMES}")
    rnd = random.Random(SEED)
    A = rand_pencil(N, R, rnd, BOX)
    ent = pencil_entries(A, N, R)
    F = det_form(ent, N)
    minors = submax_minors(ent, N)
    print(f"  sixteen 3x3 minors built; F has {len(F)} monomials of degree 4")
    # linear independence of the minors (dim J(M)_3 = 16)
    print(f"\n{'d':>3} {'dimS_d':>7} {'H_GN':>6} {'H meas p1':>10} {'H meas p2':>10} "
          f"{'dimJ(M)':>8} {'rank M_d':>9} {'rho_d':>6} {'H_Q=J/J_F':>10}")
    for d in range(N - 1, DMAX + 1):
        cols = dim_sym(d, R)
        hgn = H_GN(d, N, R)
        meas = [cols - ideal_dim(minors, N - 1, d, R, p) for p in PRIMES]
        dJ = cols - meas[0]
        rk = [macaulay_rank(F, N, d, R, p) for p in PRIMES]
        assert rk[0] == rk[1], ("prime disagreement", d, rk)
        print(f"{d:3d} {cols:7d} {hgn:6d} {meas[0]:10d} {meas[1]:10d} {dJ:8d} "
              f"{rk[0]:9d} {rho_generic(d,N,R):6d} {dJ-rk[0]:10d}")
        sys.stdout.flush()
    print(f"\n  H_GN(d) - H_GN(d-1) for d >= 5 gives the degree of the curve;")
    print(f"  H_GN(d) = 20d - 20 => degree 20 = nu(4) = n^2(n^2-1)/12, "
          f"arithmetic genus 21.")
    for d in range(5, 12):
        assert H_GN(d, N, R) == 20 * d - 20, (d, H_GN(d, N, R))
    print(f"  checked H_GN(d) = 20d - 20 for d = 5..11 (Gulliksen-Negard, exact)")
    print(f"[s44 locus] done in {time.time()-t0:.1f}s")
