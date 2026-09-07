"""Independent full-weight-space build for the sparse-route checker (session 67).

This module rebuilds, from a cell (n=4, r, lambda, delta) and recorded evaluation
points, the two matrices whose joint column rank decides a sparse-route claim:

  * E  -- the stacked simple raising operators E_{i,i+1} on the FULL weight-lambda
          space of C[Sym^4 C^r]_delta (no stabiliser reduction), so ker_p E is the
          highest-weight space and dim ker_Q E = a (the plethysm value);
  * ev -- the evaluation rows at the recorded points, one dense row per point.

Then mult_X(lambda, delta) = a - nullity_Q[E; ev] and, since rank_p <= rank_Q,
nullity_p[E; ev] = 0 at one prime proves mult_X = a over Q (docs/sparse_det_route.md
Lemmas 1-2).

It deliberately does NOT use the stabiliser/character reduction the original run
used (analysis/wk9_s45_build via docs/stabiliser_reduction.md): working in the
full weight space is simpler and makes the re-derivation an independent check of
that reduction as well.  It shares nothing with analysis/; the only imports are
numpy/scipy and the verifier's own forms.py (to rebuild a point's quartic) and
the raising rule fixed in tools/verify/FORMAT.md.

Conventions (identical to FORMAT.md / hwv.py):
  E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}   (0 if alpha_j = 0).
"""
import numpy as np
from scipy import sparse
from points import form_of_point          # verifier-owned; rebuilds the quartic from substitution data


def exps(n, r):
    """degree-n exponent tuples in r variables, in a fixed order."""
    if r == 1:
        return [(n,)]
    out = []
    for a in range(n, -1, -1):
        for rest in exps(n - a, r - 1):
            out.append((a,) + rest)
    return out


def _row_codes(M, L):
    """Injective integer key per sorted monomial row (positional base-L; int64
    when L**delta fits, else exact Python integers).  Used only for argsort /
    searchsorted, so any injection gives the same lookups."""
    N, d = M.shape
    wide = (L ** d) >= (1 << 62)
    dt = object if wide else np.int64
    code = np.zeros(N, dtype=dt)
    for k in range(d):
        code = code * L + M[:, k].astype(dt)
    return code


def weight_monomials_idx(n, r, delta, lam):
    """Weight-lambda degree-delta monomials as an (N_S x delta) int32 array of
    letter indices (into exps(n, r)), rows sorted ascending, in lexicographic
    order of the index tuples.  Level-by-level numpy expansion: a prefix of k
    sorted letters is kept iff its residual weight is nonnegative and reachable by
    the remaining delta-k letters."""
    lam = tuple(lam)
    A = np.array(exps(n, r), dtype=np.int32)          # L x r
    L = A.shape[0]
    if sum(lam) != delta * n:
        return np.zeros((0, delta), dtype=np.int32)
    lamv = np.array(lam, dtype=np.int32)
    # prefixes: (P x k) letter indices; residual weight (P x r); last letter index
    pref = np.zeros((1, 0), dtype=np.int32)
    rem = lamv[None, :].copy()
    last = np.zeros(1, dtype=np.int32)
    for level in range(delta):
        left = delta - level - 1
        rows_p, rows_rem, rows_last = [], [], []
        for i in range(L):
            a = A[i]
            take = (last <= i)                          # keep multiset sorted
            if not take.any():
                continue
            nr = rem[take] - a[None, :]
            good = (nr >= 0).all(1) & (nr <= left * n).all(1)
            if not good.any():
                continue
            base = np.nonzero(take)[0][good]
            pp = np.concatenate([pref[base], np.full((base.size, 1), i, dtype=np.int32)], axis=1)
            rows_p.append(pp)
            rows_rem.append(rem[base] - a[None, :])
            rows_last.append(np.full(base.size, i, dtype=np.int32))
        if not rows_p:
            return np.zeros((0, delta), dtype=np.int32)
        pref = np.concatenate(rows_p)
        rem = np.concatenate(rows_rem)
        last = np.concatenate(rows_last)
    keep = (rem == 0).all(1)
    M = pref[keep]
    # sort rows lexicographically for a canonical order
    order = np.lexsort([M[:, k] for k in range(delta - 1, -1, -1)])
    return M[order]


def raising_operator_full(n, r, delta, lam):
    """The stacked simple raising operators E_{i,i+1} on the full weight-lambda
    space, as a scipy CSR over N_S columns (integer entries), and the monomial
    array M (columns).  ker_p of this matrix is the highest-weight space
    (dim = a).  Vectorised over monomials and factor positions."""
    A = exps(n, r)
    Aa = np.array(A, dtype=np.int32)
    idx = {a: k for k, a in enumerate(A)}
    L = len(A)
    M = weight_monomials_idx(n, r, delta, lam)
    N_S = M.shape[0]
    if N_S == 0:
        return sparse.csr_matrix((0, 0), dtype=np.int64), M
    lam = tuple(lam)
    blocks = []
    for i in range(r - 1):
        j = i + 1
        if lam[j] == 0:
            continue
        tgt = tuple(lam[k] + (1 if k == i else (-1 if k == j else 0)) for k in range(r))
        T = weight_monomials_idx(n, r, delta, tgt)
        nt = T.shape[0]
        if nt == 0:
            continue
        tcodes = _row_codes(T, L)
        torder = np.argsort(tcodes, kind='stable')
        tsorted = tcodes[torder]
        # letter shift for this (i, j): letter index -> index of alpha + e_i - e_j, or -1
        shift = np.full(L, -1, dtype=np.int64)
        for a, al in enumerate(A):
            if al[j] > 0:
                b = list(al); b[i] += 1; b[j] -= 1
                shift[a] = idx[tuple(b)]
        rr, cc, vv = [], [], []
        cols = np.arange(N_S)
        for k in range(delta):
            src = M[:, k]
            new = shift[src]
            valid = new >= 0
            if not valid.any():
                continue
            rowsnew = M[valid].copy()
            rowsnew[:, k] = new[valid]
            rowsnew.sort(axis=1)
            codes = _row_codes(rowsnew, L)
            p = np.searchsorted(tsorted, codes)
            # every image must be a target monomial (weight preserved)
            assert p.max(initial=0) < nt and np.all(tsorted[np.minimum(p, nt - 1)] == codes), \
                "raising image not in the target basis"
            ridx = torder[p]
            coef = (Aa[src[valid], i] + 1).astype(np.int64)
            rr.append(ridx); cc.append(cols[valid]); vv.append(coef)
        if not rr:
            continue
        Ei = sparse.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                               shape=(nt, N_S), dtype=np.int64).tocsr()
        Ei.sum_duplicates(); Ei.eliminate_zeros()
        nz = np.diff(Ei.indptr) > 0
        Ei = Ei[np.nonzero(nz)[0]]
        blocks.append(Ei)
    if not blocks:
        return sparse.csr_matrix((0, N_S), dtype=np.int64), M
    E = sparse.vstack(blocks).tocsr()
    E.sort_indices()
    return E, M


def eval_rows_full(M, n, r, points, prime):
    """Dense evaluation rows (one per point) over the N_S monomial columns, mod p.

    ev[point][mono] = prod over the delta letters of the point's quartic
    coefficient at that letter.  The point is rebuilt from its substitution data
    by forms.form_of_point (which is the check that it lies on the claimed
    variety)."""
    A = exps(n, r)
    N_S, delta = M.shape
    rows = np.zeros((len(points), N_S), dtype=np.int64)
    for pj, pt in enumerate(points):
        F = form_of_point(pt, r)
        cv = np.zeros(len(A), dtype=np.int64)
        for a, al in enumerate(A):
            cv[a] = F.get(al, 0) % prime
        # product over the delta letters of each monomial
        col = np.ones(N_S, dtype=np.int64)
        for k in range(delta):
            col = (col * cv[M[:, k]]) % prime
        rows[pj] = col
    return rows
