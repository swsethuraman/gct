#!/usr/bin/env python3
"""
Session 29 -- B: pin e, the degree of the determinantal-quartic hypersurface.

D_4^{det_4} = {F = 0} has codimension 1, so its ideal is principal and F is an
SL_4-invariant of quaternary quartics of degree e.  a((delta^4),delta) =
0,0,0,1,0,1,1,3 for delta = 1..8, and mult_det((4^4),4) = a = 1 rules out e = 4.
The next candidate is e = 6, decided by one bit: mult_det((6,6,6,6), 6).

The weight space has dimension 12,652, beyond dense pure-Python elimination.
Solved here by BLOCKED elimination over F_p with p = 46337 < 2^15.5, carried in
float64 so the rank-k updates run through BLAS dgemm: products are < p^2 ~ 2e9
and a block sum of 12,652 of them is < 2^45, exact in float64.

Self-checks: rank(R) must equal N - a with a = 1 from the plethysm; the kernel
vector must be annihilated by every raising row; and the whole computation is
repeated modulo a second prime.
"""
import sys, time, random
import numpy as np
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import build_R, restrict, eval_row, det_form, per_padded, exps
from wk8_s29_pleth import a_of

def elim_kernel(rows, nc, p, block=96, verbose=True):
    """Unblocked Gaussian elimination mod p over float64, vectorised per pivot.

    NB an earlier BLOCKED version of this routine was WRONG: it applied the
    rank-k trailing update using panel pivot rows that had not themselves been
    reduced by the earlier pivots of the same panel, so the multipliers did not
    correspond to a unit-triangular factor.  It under-reported the rank
    (11588 instead of 12651 at (6,6,6,6)) and is recorded in the session notes.
    The version below updates the full row width at every pivot, so no such
    ordering question arises.  Entries stay < p^2 < 2^31 between reductions, so
    float64 is exact.
    """
    m = len(rows)
    M = np.zeros((m, nc), dtype=np.float64)
    for i, rw in enumerate(rows):
        for c, v in rw.items(): M[i, c] = v % p
    piv_row, piv_col = 0, []
    t0 = time.time()
    for c in range(nc):
        if piv_row >= m: break
        col = M[piv_row:, c]
        nz = np.nonzero(col)[0]
        if nz.size == 0: continue
        r = piv_row + nz[0]
        if r != piv_row: M[[piv_row, r]] = M[[r, piv_row]]
        inv = pow(int(M[piv_row, c]), p - 2, p)
        M[piv_row, c:] = np.mod(M[piv_row, c:] * inv, p)
        sub = M[piv_row + 1:, c]
        act = np.nonzero(sub)[0]
        if act.size:
            idx = piv_row + 1 + act
            M[idx, c:] = np.mod(M[idx, c:] - np.outer(M[idx, c], M[piv_row, c:]), p)
        piv_col.append(c); piv_row += 1
        if verbose and piv_row % 1000 == 0:
            print("      pivot %5d/%d  col %5d  [%.0fs]" % (piv_row, nc, c,
                  time.time() - t0)); sys.stdout.flush()
    rank = piv_row
    pset = set(piv_col)
    free = [x for x in range(nc) if x not in pset]
    ker = []
    if len(free) <= 4:
        for i in range(rank - 1, -1, -1):
            pc = piv_col[i]
            above = np.nonzero(M[:i, pc])[0]
            if above.size:
                M[above, pc:] = np.mod(M[above, pc:] - np.outer(M[above, pc],
                                                                M[i, pc:]), p)
        for fc in free:
            v = np.zeros(nc, dtype=np.int64); v[fc] = 1
            for i, pc in enumerate(piv_col): v[pc] = int(-M[i, fc]) % p
            ker.append(v)
    return rank, ker, piv_col

def run(lam, delta, n=4, r=4, primes=(46337, 46327)):
    a_pl = a_of(lam, delta, n, r)
    print("lam = %s, delta = %d : plethysm says a = %d" % (str(lam), delta, a_pl))
    basis, R = build_R(n, r, delta, lam)
    N = len(basis)
    print("  weight space %d, raising rows %d" % (N, len(R)))
    rnd = random.Random(3)
    rows = R if len(R) <= int(1.04 * N) else rnd.sample(R, int(1.04 * N))
    print("  using %d rows (row-subsampled)" % len(rows))
    A = exps(n, r)
    d4, N4 = det_form(4)
    out = {}
    for p in primes:
        t0 = time.time()
        rank, ker, pc = elim_kernel([dict(x) for x in rows], N, p)
        a_meas = N - rank
        print("  p=%d : rank %d, a = %d  %s  [%.0fs]"
              % (p, rank, a_meas, "OK" if a_meas == a_pl else "*** a MISMATCH ***",
                 time.time() - t0))
        assert a_meas == a_pl, (lam, a_meas, a_pl)
        # verify the kernel against the FULL row set, not just the subsample
        for v in ker:
            for rw in R:
                s = sum(co * int(v[c]) for c, co in rw.items()) % p
                assert s == 0, ("kernel vector not annihilated", lam, p)
        # evaluate
        rr = random.Random(17)
        vals = []
        for _ in range(6):
            As = [[rr.randint(-30, 30) for _ in range(N4)] for _ in range(r)]
            ev = eval_row(basis, restrict(d4, N4, n, r, As), n, r)
            vals.append([sum(ev[i] * int(v[i]) for i in range(N)) % p for v in ker])
        nonzero = any(any(x) for x in vals)
        mult = 1 if nonzero else 0
        print("  p=%d : h vanishes on the orbit? %s  ->  mult_det = %d"
              % (p, "NO" if nonzero else "YES (at all 6 points)", mult))
        out[p] = mult
    assert len(set(out.values())) == 1, out
    return a_pl, list(out.values())[0]

if __name__ == '__main__':
    lam = eval(sys.argv[1]) if len(sys.argv) > 1 else (6, 6, 6, 6)
    delta = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    a, mult = run(lam, delta)
    print()
    if mult < a:
        print("mult_det < a  ->  the degree-%d invariant VANISHES on D_4^{det_4}" % delta)
        print("=>  e = %d" % delta)
    else:
        print("mult_det = a  ->  the degree-%d invariant does NOT vanish on D_4^{det_4}"
              % delta)
        print("=>  e != %d" % delta)
