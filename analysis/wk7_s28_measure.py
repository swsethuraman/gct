"""Session 28 -- the measurement, made feasible at long weights.

Session 26's `measure_np` eliminated the FULL raising-operator matrix R, which
has (r-1) * N_S rows against N_S columns.  At N_S ~ 4500 and r = 6 that is a
22000 x 4500 int64 array -- 800 MB and O(rows * N_S^2) work.

The fix is that the row space of R has rank exactly N_S - a, with `a` known
independently from the plethysm.  So a random SUBSET of rows suffices, provided
we verify that its rank equals N_S - a; if it does, its row space IS the row
space of R (a subset of a matrix whose rank equals the full rank spans the same
row space), and

    mult = rank([R_subset ; E]) - rank(R_subset)

exactly as before.  Cost drops to one O(N_S^3) elimination.  The check
`rank(R_subset) == N_S - a` is also a strong cross-check on the whole
construction: the raising operators and the plethysm coefficient are computed
by completely different routes and have to agree.

Certification, per the pre-registration:
  * rank == a               ->  mult = a, PROVED (a explicit points at which a
                                highest-weight vectors are independent);
  * rank == m_det < a       ->  mult = m_det, PROVED (rank <= mult <= m_det);
  * a > m_det               ->  mult < a, PROVED, no rank needed;
  * anything else           ->  bounds only, reported as bounds.
"""
import random, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import a_pleth, m_det, cubic_exponents
from wk6_s26_hwv import weight_basis, raise_op, form_coeffs

NP1, NP2 = 46337, 46309


def _echelon_rank(rows, ncol, mod, extra=None):
    """Rank of `rows` and of `rows + extra`, in one pass.  numpy, mod prime."""
    import numpy as np
    M = np.array(rows, dtype=np.int64) % mod
    n = M.shape[0]
    piv_cols = []
    rk = 0
    for col in range(ncol):
        if rk >= n:
            break
        nz = np.nonzero(M[rk:, col])[0]
        if nz.size == 0:
            continue
        p = rk + int(nz[0])
        if p != rk:
            M[[rk, p]] = M[[p, rk]]
        inv = pow(int(M[rk, col]), mod - 2, mod)
        M[rk] = (M[rk] * inv) % mod
        colv = M[:, col].copy()
        colv[rk] = 0
        nzr = np.nonzero(colv)[0]
        if nzr.size:
            M[nzr] = (M[nzr] - np.outer(colv[nzr], M[rk])) % mod
        piv_cols.append(col)
        rk += 1
    rank_R = rk
    if extra is None:
        return rank_R, rank_R
    # reduce each extra row against the echelon basis, then among themselves
    E = np.array(extra, dtype=np.int64) % mod
    for i, col in enumerate(piv_cols):
        cv = E[:, col].copy()
        nzr = np.nonzero(cv)[0]
        if nzr.size:
            E[nzr] = (E[nzr] - np.outer(cv[nzr], M[i])) % mod
    add = 0
    m = E.shape[0]
    for col in range(ncol):
        if add >= m:
            break
        nz = np.nonzero(E[add:, col])[0]
        if nz.size == 0:
            continue
        p = add + int(nz[0])
        if p != add:
            E[[add, p]] = E[[p, add]]
        inv = pow(int(E[add, col]), mod - 2, mod)
        E[add] = (E[add] * inv) % mod
        cv = E[:, col].copy()
        cv[add] = 0
        nzr = np.nonzero(cv)[0]
        if nzr.size:
            E[nzr] = (E[nzr] - np.outer(cv[nzr], E[add])) % mod
        add += 1
    return rank_R, rank_R + add


def measure(lam, delta, kind='det', npts=None, seed=28, spread=6,
            mods=(NP1, NP2), rowfac=1.15, verbose=False):
    """Returns (a, mult_lower_bound, N_S, rank_R_ok).

    `mult_lower_bound` is the measured rank; it equals mult whenever it attains
    `a` (see the module docstring for the certification rules)."""
    lam = tuple(x for x in lam if x)
    r = len(lam)
    aa = a_pleth(lam, delta)
    if aa == 0:
        return 0, 0, 0, True
    src, exps = weight_basis(delta, r, lam)
    ns = len(src)
    eidx = {a: i for i, a in enumerate(exps)}
    # build R's rows, then subsample
    tgt, ent = {}, []
    for i in range(r - 1):
        for col, m in enumerate(src):
            for nm, c in raise_op(m, 1, i, i + 1, exps, eidx).items():
                key = (i, nm)
                if key not in tgt:
                    tgt[key] = len(tgt)
                ent.append((tgt[key], col, c))
    rows = {}
    for rr, cc, v in ent:
        rows.setdefault(rr, {})[cc] = rows.setdefault(rr, {}).get(cc, 0) + v
    Rrows = [d for d in rows.values() if d]
    rng = random.Random(seed)
    need = min(len(Rrows), int(rowfac * (ns - aa)) + 12)
    rng.shuffle(Rrows)
    sub = Rrows[:need]
    Rd = [[d.get(c, 0) for c in range(ns)] for d in sub]
    k = npts or (aa + 3)
    rng2 = random.Random(seed + 1)
    out = []
    for mod in mods:
        E = []
        rng2 = random.Random(seed + 1)
        for _ in range(k):
            As = [[[rng2.randint(-spread, spread) for _ in range(3)]
                   for _ in range(3)] for _ in range(r)]
            co = form_coeffs(As, exps, kind)
            row = []
            for m in src:
                p = 1
                for i in m:
                    p = (p * co[i]) % mod
                row.append(p)
            E.append(row)
        rR, rRE = _echelon_rank(Rd, ns, mod, E)
        out.append((rR, rRE))
    assert len(set(out)) == 1, ("two primes disagree", lam, delta, out)
    rR, rRE = out[0]
    ok = (rR == ns - aa)
    if not ok:                       # subsample did not span; retry with all
        Rd = [[d.get(c, 0) for c in range(ns)] for d in Rrows]
        rR, rRE = _echelon_rank(Rd, ns, mods[0], E)
        ok = (rR == ns - aa)
    if verbose:
        print("   lam=%-24s d=%d  N_S=%-6d a=%-3d rank=%d  (rank R = %d, want %d) %s"
              % (str(lam), delta, ns, aa, rRE - rR, rR, ns - aa,
                 "ok" if ok else "*** R-RANK MISMATCH ***"), flush=True)
    return aa, rRE - rR, ns, ok


def verdict(lam, delta, kind='det', **kw):
    """(a, m_det, measured rank, status string)."""
    aa, rk, ns, ok = measure(lam, delta, kind, **kw)
    md = m_det(lam, 3, delta) if kind == 'det' else None
    if not ok:
        return aa, md, rk, "R-RANK MISMATCH -- construction inconsistent"
    if md is not None and aa > md:
        return aa, md, rk, "BITES (arithmetic: a > m_det, mult <= m_det)"
    if rk == aa:
        return aa, md, rk, "mult = a  (proved)"
    if md is not None and rk == md:
        return aa, md, rk, "mult = m_det < a  (proved: rank <= mult <= m_det) -- BITES"
    return aa, md, rk, "INCONCLUSIVE: %d <= mult <= %d" % (rk, min(aa, md if md is not None else aa))
