#!/usr/bin/env python3
"""
Session 44 -- a rigorous multimodular certificate that the rank of M_d over Q
drops at an explicit integer determinantal pencil, and the Schwartz-Zippel step
that turns it into a statement about the generic point.

Why this is needed.  A rank computed modulo p is a LOWER bound on the rank over
Q (reduction can only drop rank), and the rank at a point is a LOWER bound on
the generic rank.  So a mod-p drop at a random pencil proves nothing about
D_r^{det_n}: both inequalities point the wrong way.  Two rigorous steps:

  (1) Multimodular certificate.  Every rho x rho minor of M_d is an integer.
      Hadamard: |minor| <= prod of the 2-norms of the rho rows used, and every
      row of M_d is a permutation of the coefficient vector of some partial of
      F, so |minor| <= (max_i ||grad_i F||_2)^rho =: H.  If rank_p M_d < rho for
      a set of primes with product > 2H, then every rho x rho minor is
      divisible by that product while being at most H in absolute value, hence
      zero.  Therefore rank_Q M_d < rho AT THAT PENCIL -- exactly, not modulo
      anything.

  (2) Schwartz-Zippel.  The entries of M_d(F) are linear in the coefficients of
      F, which are polynomials of degree n in the pencil entries, so each
      rho x rho minor is a polynomial of degree n*rho in the r*n^2 pencil
      entries.  If the GENERIC determinantal rank were rho, at least one such
      minor would be a nonzero polynomial of degree n*rho; a pencil drawn
      uniformly from a box of side 2*BOX+1 kills it with probability at most
      n*rho/(2*BOX+1).  Independent pencils multiply.

usage: wk9_s44_certify.py [seed] [logbox] [pencils] [n] [r] [d] [pmin_bits]
"""
import sys, os, random, time
from math import isqrt, log2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *
from flint import nmod_mat

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
LOGBOX = int(sys.argv[2]) if len(sys.argv) > 2 else 9
NPEN = int(sys.argv[3]) if len(sys.argv) > 3 else 3
N = int(sys.argv[4]) if len(sys.argv) > 4 else 4
R = int(sys.argv[5]) if len(sys.argv) > 5 else 6
D = int(sys.argv[6]) if len(sys.argv) > 6 else 7
PBITS = int(sys.argv[7]) if len(sys.argv) > 7 else 62
BOX = 10 ** LOGBOX


def is_prime(m):
    if m < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0: return m == q
    d, s = m - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1): continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1: break
        else:
            return False
    return True


def primes_below(start, count):
    out, m = [], start | 1
    while len(out) < count:
        if is_prime(m): out.append(m)
        m -= 2
    return out


def certify(F, n, d, r, verbose=True):
    """returns (rank_Q_is_below_rho, rho, ranks_seen, nprimes, seconds)."""
    rho = rho_generic(d, n, r)
    grads = [pderiv(F, i) for i in range(r)]
    rows, nc = ideal_rows(grads, n - 1, d, r)
    # Hadamard: every row of M_d is a copy of some grad's coefficient vector
    norms = [isqrt(sum(c * c for c in g.values())) + 1 for g in grads]
    logH = rho * log2(max(norms))
    need = logH + 1                      # product of primes must exceed 2H
    npr = int(need / (PBITS - 1)) + 2
    if verbose:
        print(f"    Hadamard: max ||grad||_2 <= {max(norms)} "
              f"(~2^{log2(max(norms)):.1f}); log2 H <= {logH:.0f}; "
              f"need {npr} primes of {PBITS} bits")
    ps = primes_below(1 << PBITS, npr)
    t0 = time.time()
    ent0 = [0] * (len(rows) * nc)
    seen = set()
    for j, p in enumerate(ps):
        ent = list(ent0)
        for i, row in enumerate(rows):
            b = i * nc
            for c, v in row.items():
                ent[b + c] = v % p
        rk = nmod_mat(len(rows), nc, ent, p).rank()
        seen.add(rk)
        if rk >= rho:
            return False, rho, sorted(seen), j + 1, time.time() - t0
        if verbose and (j + 1) % 250 == 0:
            el = time.time() - t0
            print(f"      {j+1}/{npr} primes, ranks {sorted(seen)}, "
                  f"{el:.0f}s ({el/(j+1):.2f}s/prime, eta {el/(j+1)*(npr-j-1)/60:.1f}min)")
            sys.stdout.flush()
    return True, rho, sorted(seen), len(ps), time.time() - t0


if __name__ == '__main__':
    rho = rho_generic(D, N, R)
    deg = N * rho
    print(f"[s44 certify] n={N} r={R} d={D} rho={rho}, box +-10^{LOGBOX}, "
          f"{NPEN} pencils, {PBITS}-bit primes")
    print(f"  rho x rho minor has degree n*rho = {deg} in the {R*N*N} pencil entries")
    print(f"  Schwartz-Zippel per pencil <= {deg}/{2*BOX+1} = {deg/(2*BOX+1):.3e}")
    good = 0
    for t in range(NPEN):
        rnd = random.Random(SEED + 5150081 * t)
        F = det_point(N, R, rnd, BOX)
        print(f"  pencil {t} (seed offset {5150081*t}):")
        ok, rho, seen, npr, sec = certify(F, N, D, R)
        print(f"    -> rank_Q M_{D} {'<' if ok else '>='} {rho}: ranks mod primes "
              f"{seen} over {npr} primes [{sec/60:.1f} min]  "
              f"{'CERTIFIED DROP OVER Q' if ok else 'NO DROP'}")
        good += ok
        sys.stdout.flush()
    if good == NPEN:
        pr = (deg / (2 * BOX + 1)) ** NPEN
        print(f"\n  {NPEN}/{NPEN} pencils certified over Q.  If the generic "
              f"determinantal rank were {rho}, the probability of this is "
              f"<= {pr:.3e}.")
