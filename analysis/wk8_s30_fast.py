#!/usr/bin/env python3
"""
Session 30 -- the fast measurement path.

Two fixes over wk8_s30_core.measure:
  * R and rank(R) are built ONCE per cell and shared by both forms (the raising
    matrix does not depend on f);
  * flint matrices are built with the zero constructor + sparse setitem, not a
    dense python list of nrows*ncols ints.
Rows of R are subsampled to ~1.05 N_S; the structural check rank(R) = N_S - a
(with `a` taken independently from the plethysm) is what certifies the sample.
"""
import sys, time, random
sys.path.insert(0, '/root/gct/analysis')
from flint import nmod_mat
from wk8_s30_core import (build_R, restrict, eval_row, monomials, P1, P2)

def mat_sparse(rows, nc, p):
    M = nmod_mat(len(rows), nc, p)
    for i, rw in enumerate(rows):
        if isinstance(rw, dict):
            for c, v in rw.items():
                v %= p
                if v: M[i, c] = v
        else:
            for c, v in enumerate(rw):
                v %= p
                if v: M[i, c] = v
    return M

def cell(f_list, n, r, delta, lam, a_expect, npts=None, bound=40, seeds=None,
         primes=(P1, P2), verbose=True):
    """f_list = [(name, f, N), ...].  Returns {name: mult} plus diagnostics."""
    t0 = time.time()
    basis, R = build_R(n, r, delta, lam)
    nb = len(basis)
    # NB row subsampling to 1.05 N_S was tried and REJECTED: at (13,5,4,1,1) it
    # gave rank(R) = 1772 against the required N_S - a = 1822.  The `a` check
    # below caught it.  All rows are used; rank cost is linear in the row count.
    Rs = R
    tb = time.time() - t0
    out = {'nbasis': nb, 'rows': len(R), 'rows_used': len(Rs)}
    rkR = {}
    for p in primes:
        t = time.time()
        rkR[p] = mat_sparse(Rs, nb, p).rank()
        if verbose: print("      rank(R) mod %d = %d  [%.0fs]" % (p, rkR[p],
                          time.time() - t)); sys.stdout.flush()
    a = nb - rkR[primes[0]]
    assert all(nb - rkR[p] == a for p in primes), (lam, rkR)
    assert a == a_expect, ("a mismatch vs plethysm", lam, a, a_expect)
    out['a'] = a
    for name, f, N in f_list:
        sd = (seeds or {}).get(name, 11)
        rnd = random.Random(sd)
        K = npts if npts else a + 8
        ev = [eval_row(basis, restrict(f, N, n, r,
              [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]),
              n, r) for _ in range(K)]
        ms = {}
        for p in primes:
            t = time.time()
            ms[p] = mat_sparse(Rs + ev, nb, p).rank() - rkR[p]
            if verbose: print("      %s mult mod %d = %d  [%.0fs]" % (name, p, ms[p],
                              time.time() - t)); sys.stdout.flush()
        assert len(set(ms.values())) == 1, (lam, name, ms)
        out[name] = ms[primes[0]]
    out['secs'] = time.time() - t0
    out['build_secs'] = tb
    return out
