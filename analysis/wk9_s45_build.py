#!/usr/bin/env python3
"""
Session 45 -- the memory-lean build: weight-lam monomials, the isotypic
reduction, the raising operators and the evaluation rows, all in O(N_S + nnz)
memory with no Python list of N_S monomial tuples and no dense object of size
n_chi^2.

Why this module exists.  The stabiliser reduction divides the weight space by
|Stab_W(lam)|, which is 1 when the parts of lam are distinct -- so the BALANCED
cells, exactly the ones where the determinant ideal would first appear, get no
reduction at all and have n_chi = N_S.  Session 42's build
(wk9_s42_orbits.orbit_setup_fast) is vectorised but stores |Stab| index arrays
of length N_S, the Python `basis` list of N_S tuples and (optionally) the
`vecs` list of N_S dicts, and its reduced_rows_fast does an np.unique over an
(N_S*delta) concatenation.  At N_S ~ 10^6 that is already gigabytes; the sparse
solve itself needs only O(nnz + n).

What is kept identical to the validated code:
  * the monomial order (the lexicographic DFS order of wk8_s30_core.monomials),
  * the multiset combinadic code of wk9_s42_orbits._codes,
  * the orbit partition, the twisted coefficients acc[j] = sum_g chi(g)[g.rep_j = j],
    and every assertion s42 makes on them,
  * the raising rule E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j} and the
    H-orbit dedup of target rows with the chi-obstructed rows asserted to cancel,
  * the chi-coordinate evaluation rows of wk9_s36_stabred.point_rows.
Every one of these is checked against the s36/s42 implementations in
analysis/wk9_s45_validate.py (V5).

The changes are all in HOW, never in WHAT:
  * monomials are enumerated level by level as an (N_S x delta) int32 array with
    the prune rem_i <= n*(factors left);
  * the orbit setup makes two |Stab|-passes (canon, then acc) instead of storing
    |Stab| index arrays;
  * the raising operators are assembled chunkwise against a DIRECTLY ENUMERATED
    target basis (monomials of weight lam + e_i - e_j), so no np.unique over the
    big concatenation is needed, with periodic consolidation into CSR;
  * the evaluation rows are numpy products + add.reduceat instead of a Python
    loop over N_S x delta.
"""
import sys, os, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_core import exps, restrict
from wk9_s36_stabred import stab_group, perm_tables
from wk9_s42_orbits import _codes
from math import comb

def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()

def _rss_gb():
    try:
        with open('/proc/self/status') as f:
            for line in f:
                if line.startswith('VmHWM'): return int(line.split()[1]) / 1048576.0
    except Exception: pass
    return float('nan')

# --------------------------------------------------------------- monomials
def _dp_tables(n, r, delta, lam):
    """Exact feasibility DP over the small state space (partial residual weight,
    minimum allowed index).  Returns, for each level k = 0..delta-1, the distinct
    residual weights REM[k] (D_k x r), their integer keys, the successor map
    nid[k] (D_k x L -> index into REM[k+1], -1 where A[i] does not fit) and the
    boolean G[k] (D_k x L) with

        G[k][t][i] = 1  iff  A[i] <= REM[k][t]  and  REM[k][t] - A[i] can be
                     written as a sum of (delta-k-1) exponent vectors with
                     indices >= i.

    G is an EXACT prune: a prefix is extended by index i at level k iff G says so,
    so every prefix generated extends to at least one weight-lam monomial and the
    number of live prefixes never exceeds N_S at any level.  State space
    D_k * L * r, independent of N_S."""
    A = np.array(exps(n, r), dtype=np.int32); L = A.shape[0]
    base = int(max(lam)) + 1
    pw = np.array([base ** c for c in range(r)], dtype=np.int64)
    def keys(V): return (V.astype(np.int64) * pw).sum(1)
    REM = [np.array([lam], dtype=np.int32)]
    KEY = [keys(REM[0])]
    NID = []
    for k in range(delta):
        cur = REM[k]                                        # D x r
        d = cur[:, None, :] - A[None, :, :]                 # D x L x r
        fit = (d >= 0).all(2)                               # D x L
        nxt = d[fit]                                        # F x r
        kk = keys(nxt)
        uk, inv = np.unique(kk, return_inverse=True)
        # representative rows for the unique keys
        first = np.zeros(len(uk), dtype=np.int64)
        first[inv[::-1]] = np.arange(len(inv) - 1, -1, -1)
        REM.append(nxt[first]); KEY.append(uk)
        nid = np.full(fit.shape, -1, dtype=np.int64)
        nid[fit] = inv
        NID.append(nid)
        del d, fit, nxt, kk, inv, first
    # backward feasibility
    F = [None] * (delta + 1)
    F[delta] = (REM[delta] == 0).all(1)[:, None] & np.ones((1, L + 1), dtype=bool)
    G = [None] * delta
    for k in range(delta - 1, -1, -1):
        nid = NID[k]
        ok = nid >= 0
        g = np.zeros(nid.shape, dtype=bool)
        # F[k+1][nid[t,i]][i]
        ii = np.nonzero(ok)
        g[ii] = F[k + 1][nid[ii], ii[1]]
        G[k] = g
        # F[k][t][s] = any_{i >= s} g[t][i]  (suffix OR, with an extra column for s = L)
        suf = np.zeros((g.shape[0], L + 1), dtype=bool)
        suf[:, :L] = np.logical_or.accumulate(g[:, ::-1], axis=1)[:, ::-1]
        F[k] = suf
    return REM, NID, G

def monomials_array(n, r, delta, lam, block=250000, verbose=False):
    """Weight-lam degree-delta monomials as an (N_S x delta) int32 array of
    indices into exps(n, r), rows nondecreasing, in the lexicographic order of
    wk8_s30_core.monomials (asserted identical on the V5 cells).

    Level-by-level numpy expansion under the exact DP prune of _dp_tables, so no
    Python list of tuples is ever built and no dead prefix is ever stored.  BFS in
    index order preserves the DFS lexicographic order."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    L = len(exps(n, r))
    if sum(lam) != delta * n:
        return np.zeros((0, delta), dtype=np.int32)
    REM, NID, G = _dp_tables(n, r, delta, lam)
    pref = np.zeros((1, 0), dtype=np.int32)
    tid = np.zeros(1, dtype=np.int64)          # residual-weight state
    last = np.zeros(1, dtype=np.int32)         # minimum allowed next index
    ar_L = np.arange(L, dtype=np.int32)
    for k in range(delta):
        g = G[k]; nid = NID[k]
        op, ot, ol = [], [], []
        for b0 in range(0, pref.shape[0], block):
            b1 = min(b0 + block, pref.shape[0])
            ok = g[tid[b0:b1]] & (ar_L[None, :] >= last[b0:b1, None])
            bi, ii = np.nonzero(ok)
            del ok
            if bi.size == 0: continue
            op.append(np.concatenate([pref[b0:b1][bi], ii[:, None].astype(np.int32)], axis=1))
            ot.append(nid[tid[b0:b1][bi], ii])
            ol.append(ii.astype(np.int32))
        if not op:
            return np.zeros((0, delta), dtype=np.int32)
        pref = np.concatenate(op); tid = np.concatenate(ot); last = np.concatenate(ol)
        del op, ot, ol
        if verbose: log(f"      level {k+1}: {pref.shape[0]} prefixes")
    assert not REM[delta][tid].any(), "residual weight nonzero at the last level"
    return pref

# ------------------------------------------------------- isotypic reduction
def _image_index(M, tab, sorted_codes, order, L):
    """index in the basis of g.m for every monomial m (g given by its index
    permutation table)."""
    img = np.sort(np.asarray(tab, dtype=np.int32)[M], axis=1)
    c = _codes(img, L)
    del img
    p = np.searchsorted(sorted_codes, c)
    assert p.max(initial=0) < len(sorted_codes) and np.all(sorted_codes[p] == c), \
        "image monomial not in the basis (weight not preserved?)"
    del c
    return order[p]

def _canon_acc(M, tabs, L, want_sign=True):
    """(canon, acc) with canon[j] = min_g index(g.m_j) and
    acc[j] = sum_g chi(g) [ g.(rep of j) = j ], in two passes over the group
    (never storing |Stab| index arrays)."""
    N = M.shape[0]
    codes0 = _codes(M, L)
    order = np.argsort(codes0, kind='stable')
    sorted_codes = codes0[order]
    assert np.all(np.diff(sorted_codes) > 0), "codes not injective"
    del codes0
    canon = np.arange(N, dtype=np.int64)
    for tab, ch in tabs:
        np.minimum(canon, _image_index(M, tab, sorted_codes, order, L), out=canon)
    acc = np.zeros(N, dtype=np.int64)
    ar = np.arange(N, dtype=np.int64)
    obstructed = np.zeros(N, dtype=bool)
    for tab, ch in tabs:
        idx = _image_index(M, tab, sorted_codes, order, L)
        acc += ch * (idx[canon] == ar)
        if ch == -1: obstructed |= (idx == ar)
        del idx
    del sorted_codes, order
    return canon, acc, obstructed

def orbit_setup_arr(n, r, delta, lam, M=None, verbose=True):
    """The chi_lam-isotypic reduction as arrays only.  Returns
    dict(M, col_of, sgn, n_chi, N_S, stab, dropped) with

        col_of[m] = the chi-column (orbit number) of monomial m, -1 if the
                    orbit's twisted sum vanishes,
        sgn[m]    = the coefficient +-1 of m in that twisted orbit sum, 0 if dropped.

    Identical partition, columns and signs (up to the per-orbit global sign that
    no rank depends on) to wk9_s42_orbits.orbit_setup_fast -- checked in V5."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    L = len(exps(n, r))
    group = stab_group(lam)
    tabs = perm_tables(n, r, group)
    if M is None:
        M = monomials_array(n, r, delta, lam, verbose=verbose)
    N = M.shape[0]
    if N == 0:
        return dict(M=M, col_of=np.zeros(0, np.int64), sgn=np.zeros(0, np.int64),
                    n_chi=0, N_S=0, stab=len(group), dropped=0, secs=0.0)
    canon, acc, _ = _canon_acc(M, tabs, L)
    ar = np.arange(N, dtype=np.int64)
    is_rep = canon == ar
    kept = is_rep & (acc != 0)
    n_chi = int(kept.sum())
    dropped = int(is_rep.sum()) - n_chi
    orbnum = np.full(N, -1, dtype=np.int64)
    orbnum[kept] = np.arange(n_chi, dtype=np.int64)
    col_of = orbnum[canon]
    del orbnum, is_rep
    sgn = np.where(acc > 0, 1, -1).astype(np.int64)
    sgn[col_of < 0] = 0
    # the s42 assertions, vectorised: |acc| = |Stab| / |orbit| on every kept
    # orbit, and the twisted sum vanishes on EVERY member of a dropped orbit
    sizes = np.bincount(canon, minlength=N)
    sel = col_of >= 0
    G = len(group)
    assert np.all(np.abs(acc[sel]) * sizes[canon[sel]] == G), \
        ("twisted coefficients not +-|Stab(m)|", lam)
    assert not acc[~sel].any(), ("dropped orbit with a nonzero twisted coefficient", lam)
    del canon, acc, sizes, sel, kept, ar
    if verbose:
        log(f"  lam={lam}: N_S={N} |Stab|={G} n_chi={n_chi} (orbits dropped: {dropped}) "
            f"[lean, {time.time()-t0:.0f}s, HWM {_rss_gb():.2f} GB]")
    return dict(M=M, col_of=col_of, sgn=sgn, n_chi=n_chi, N_S=N, stab=G,
                dropped=dropped, secs=time.time() - t0)

# ---------------------------------------------------- raising operators
def raising_rows_arr(n, r, delta, lam, arr, chunk=400000, cap=6_000_000, verbose=True):
    """The rows of every simple raising operator E_{i,i+1} restricted to V_chi,
    one canonical representative per H-orbit of target monomials
    (H = Stab(lam) cap Stab(lam + e_i - e_j)), chi-obstructed H-fixed target rows
    asserted to cancel -- the same matrix as wk9_s36_stabred.reduced_rows and
    wk9_s42_orbits.reduced_rows_fast up to the choice of representative row in
    each H-orbit (a scalar).  Returned as a scipy CSR (int64 raw values) over the
    n_chi columns.

    Lean in two ways: the target basis is enumerated directly (monomials of
    weight lam + e_i - e_j) instead of being recovered by np.unique over an
    (N_S*delta) concatenation, and the triples are consolidated into CSR every
    `cap` of them."""
    from scipy import sparse
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}; L = len(A)
    Aarr = np.array(A, dtype=np.int32)
    M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']; n_chi = arr['n_chi']
    N, d = M.shape
    blocks = []
    nfixed = 0
    for i in range(r - 1):
        j = i + 1
        if lam[j] == 0: continue
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0)) for k in range(r))
        T = monomials_array(n, r, delta, tgt)
        nt = T.shape[0]
        if nt == 0: continue
        codesT = _codes(T, L)
        orderT = np.argsort(codesT, kind='stable')
        sortedT = codesT[orderT]
        assert np.all(np.diff(sortedT) > 0)
        del codesT
        H = stab_group(lam, fix=(i, j))
        Htabs = perm_tables(n, r, H)
        canonT, _, obstructedT = _canon_acc(T, Htabs, L)
        arT = np.arange(nt, dtype=np.int64)
        keepT = (canonT == arT) & ~obstructedT
        # rows kept: the canonical non-obstructed targets, plus every obstructed
        # target (whose row must cancel to zero -- asserted below)
        useT = keepT | obstructedT
        nrow = int(useT.sum())
        rowid = np.full(nt, -1, dtype=np.int64)
        rowid[useT] = np.arange(nrow, dtype=np.int64)
        obst_row = np.zeros(nrow, dtype=bool)
        obst_row[rowid[obstructedT]] = True
        del canonT, arT
        shift = np.full(L, -1, dtype=np.int64)
        for a, al in enumerate(A):
            if al[j] > 0:
                nb = list(al); nb[j] -= 1; nb[i] += 1; shift[a] = idx[tuple(nb)]
        acc_r, acc_c, acc_v = [], [], []
        pend = [0]
        hit = np.zeros(nt, dtype=bool)      # targets actually reached by this operator
        Ei = sparse.csr_matrix((nrow, n_chi), dtype=np.int64)

        def consolidate():
            nonlocal Ei, acc_r, acc_c, acc_v, pend
            if not acc_r: return
            rr = np.concatenate(acc_r); cc = np.concatenate(acc_c); vv = np.concatenate(acc_v)
            acc_r, acc_c, acc_v = [], [], []; pend[0] = 0
            X = sparse.coo_matrix((vv, (rr, cc)), shape=(nrow, n_chi), dtype=np.int64).tocsr()
            del rr, cc, vv
            X.sum_duplicates()
            Ei = (Ei + X).tocsr()
            del X

        for k in range(d):
            for b0 in range(0, N, chunk):
                b1 = min(b0 + chunk, N)
                colc = col_of[b0:b1]
                src = M[b0:b1, k]
                new = shift[src]
                valid = (new >= 0) & (colc >= 0)
                if not valid.any(): continue
                rows_new = M[b0:b1][valid].copy()
                rows_new[:, k] = new[valid]
                rows_new.sort(axis=1)
                c = _codes(rows_new, L); del rows_new
                p = np.searchsorted(sortedT, c)
                assert p.max(initial=0) < nt and np.all(sortedT[p] == c), \
                    "raising image not in the target basis"
                t = orderT[p]; del c, p
                hit[t] = True
                rid = rowid[t]; del t
                sel = rid >= 0
                if not sel.any(): continue
                coef = sgn[b0:b1][valid] * (Aarr[src[valid], i].astype(np.int64) + 1)
                acc_r.append(rid[sel]); acc_c.append(colc[valid][sel]); acc_v.append(coef[sel])
                pend[0] += int(sel.sum())
                del rid, sel, coef, valid, new, src, colc
                if pend[0] > cap: consolidate()
        consolidate()
        Ei.eliminate_zeros()
        if obst_row.any():
            sub = Ei[np.nonzero(obst_row)[0]]
            assert sub.nnz == 0, ("chi-obstructed fixed rows failed to cancel", lam, i, int(sub.nnz))
            del sub
        # count only the obstructed targets the operator actually reaches -- the
        # same population wk9_s42_orbits counts (its target set is the reached
        # one; this module enumerates the whole weight-lam' basis)
        nfixed += int((obstructedT & hit).sum())
        Ek = Ei[np.nonzero(~obst_row)[0]]
        del Ei
        Ek.eliminate_zeros()
        nz = np.diff(Ek.indptr) > 0
        Ek = Ek[np.nonzero(nz)[0]]
        blocks.append(Ek)
        if verbose:
            log(f"    E_{i}{j}: |H|={len(H)} targets {nt} canonical rows {Ek.shape[0]} "
                f"nnz {Ek.nnz} (obstructed fixed targets cancelled: {int((obstructedT & hit).sum())}) "
                f"[{time.time()-t0:.0f}s, HWM {_rss_gb():.2f} GB]")
        del T, sortedT, orderT, rowid, obst_row, keepT, obstructedT, useT, hit
    from scipy import sparse as _sp
    E = _sp.vstack(blocks).tocsr() if blocks else _sp.csr_matrix((0, n_chi), dtype=np.int64)
    E.sort_indices()
    return E, nfixed

# ------------------------------------------------------- evaluation rows
def _grouping(arr):
    """monomial indices grouped by chi-column, for add.reduceat."""
    if 'mem' in arr: return arr['mem'], arr['starts']
    col_of = arr['col_of']; n_chi = arr['n_chi']
    idx_k = np.nonzero(col_of >= 0)[0]
    o = np.argsort(col_of[idx_k], kind='stable')
    mem = idx_k[o].astype(np.int64)
    cols = col_of[mem]
    starts = np.searchsorted(cols, np.arange(n_chi, dtype=np.int64))
    assert len(mem) and cols[0] == 0 and cols[-1] == n_chi - 1
    arr['mem'] = mem; arr['starts'] = starts
    return mem, starts

def ev_rows_arr(f, N, n, r, arr, K, seed, bound, prime, chunk=2_000_000, rnd=None):
    """K evaluation rows in chi-coordinates:  row_j = sum_{m in O_j} s_m * prod_{k in m} c_{A[k]}(P).
    Identical to wk9_s36_stabred.point_rows (same random stream, same order)
    -- asserted entrywise in V5 -- but vectorised."""
    import random
    if rnd is None: rnd = random.Random(seed)
    A = exps(n, r); L = len(A)
    M = arr['M']; sgn = arr['sgn']; n_chi = arr['n_chi']
    mem, starts = _grouping(arr)
    out = []
    for _ in range(K):
        As = [[rnd.randint(-bound, bound) for _ in range(N)] for _ in range(r)]
        co = restrict(f, N, n, r, As)
        cv = np.zeros(L, dtype=np.int64)
        for a, al in enumerate(A):
            v = co.get(al, 0) % prime
            cv[a] = v
        row = np.zeros(n_chi, dtype=np.int64)
        for b0 in range(0, len(mem), chunk):
            mm = mem[b0:b0 + chunk]
            term = cv[M[mm, 0]].copy()
            for k in range(1, M.shape[1]):
                term *= cv[M[mm, k]]
                term %= prime
            term *= sgn[mm]
            term %= prime
            # groups are contiguous in `mem`; reduceat over the part inside this chunk
            s0 = np.searchsorted(starts, b0, side='right') - 1
            s1 = np.searchsorted(starts, b0 + len(mm), side='left')
            loc = np.maximum(starts[s0:s1] - b0, 0)
            np.add.at(row, np.arange(s0, s1), np.add.reduceat(term, loc) % prime)
            del term, mm, loc
        out.append((row % prime).astype(np.int64))
    return np.array(out, dtype=np.int64)

# --------------------------------------------------------------- the cell
def build_cell(lam, delta, n=4, verbose=True):
    """Memory-lean isotypic build of one cell: arrays + E (scipy CSR)."""
    lam = tuple(lam); r = len(lam)
    assert sum(lam) == n * delta and all(lam[i] >= lam[i + 1] for i in range(r - 1)) and lam[-1] > 0
    t0 = time.time(); t_m = time.time()
    M = monomials_array(n, r, delta, lam, verbose=verbose)
    mono_secs = time.time() - t_m
    arr = orbit_setup_arr(n, r, delta, lam, M=M, verbose=verbose)
    t_e = time.time()
    E, nfx = raising_rows_arr(n, r, delta, lam, arr, verbose=verbose)
    rows_secs = time.time() - t_e
    out = dict(lam=lam, delta=delta, r=r, arr=arr, E=E, N_S=arr['N_S'], stab=arr['stab'],
               n_chi=arr['n_chi'], nrows=int(E.shape[0]), nnz=int(E.nnz), nfixed=nfx,
               mono_secs=mono_secs, orbit_secs=arr['secs'], rows_secs=rows_secs,
               build_secs=time.time() - t0, hwm_gb=_rss_gb())
    if verbose:
        log(f"  built {lam} d{delta}: N_S={out['N_S']} |Stab|={out['stab']} n_chi={out['n_chi']} "
            f"rows={out['nrows']} nnz={out['nnz']} ({out['build_secs']:.0f}s: mono {mono_secs:.0f}s "
            f"orbits {arr['secs']:.0f}s rows {rows_secs:.0f}s; HWM {out['hwm_gb']:.2f} GB)")
    return out
