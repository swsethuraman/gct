#!/usr/bin/env python3
"""
Session 68 (C1) -- the ladder source: seed then births, exact over F_p.

The LMR source M_lam = HWV_lam = ker E on the chi-isotypic reduced weight space
V_chi (docs/sparse_det_route.md).  This module builds M_delta up a ladder of
fixed tail t (lam_delta = (4 delta - |t|, t)) one rung at a time:

    M_delta = J(M_{delta-1})  (+)  B_delta ,      dim B_delta = a_delta - a_{delta-1},

where J is multiplication by the s_1^4 coefficient c = c_{(4,0,...,0)} (Lemma L,
proved in s57: J is injective on C[W] and carries HWVs of weight lam_{delta-1} to
HWVs of weight lam_delta), and B_delta is obtained by DEFLATION: the nullspace of
[E_delta ; R] with R a generic dense block of a_{delta-1} rows, which has
dimension exactly a_delta - a_{delta-1} and is a complement to J(M_{delta-1})
whenever R restricted to J(M_{delta-1}) is nonsingular.

Everything here is EXACT over F_p (python-flint nmod_mat); for the reachable
validation ladders n_chi is small enough that the ground-truth kernel ker_Q E is
computed directly, so the transport+deflate construction is checked against it at
every rung.  At LMR scale the same construction would run on the sparse [E;R] via
the s45 Wiedemann route; the seed cost there is sized in wk11_s68_seed.py.

Three-part rung certificate (all required, both primes):
  (i)  the a_{delta-1} transported vectors lie in ker E_delta (full E, not
       support-restricted), and J is injective (rank a_{delta-1});
  (ii) dim ker[E_delta; R] = a_delta - a_{delta-1} with a_delta independently
       known, and R|_{J(M_{delta-1})} nonsingular;
  (iii) every new B_delta vector passes the full raising action, and
       span(J(M_{delta-1}) (+) B_delta) = ker_Q E_delta exactly.
"""
import os, sys, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from flint import nmod_mat
from wk8_s30_core import exps
from wk9_s42_orbits import _codes
from wk9_s45_build import build_cell, ev_rows_arr
from wk9_s36_stabred import DET4, N_DET, PAD34, N_PAD, P1, P2

FORMS = dict(det=(DET4, N_DET), pad=(PAD34, N_PAD))
SEEDS = dict(det=11, pad=29)

def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()

# ------------------------------------------------------------ flint helpers
def to_nmod(csr, p):
    """scipy CSR (int64) -> flint nmod_mat over F_p (dense; small cells only)."""
    D = csr.toarray()
    D = np.mod(D, p).astype(np.int64)
    return nmod_mat(D.shape[0], D.shape[1], [int(x) for x in D.ravel()], p)

def np_to_nmod(D, p):
    D = np.mod(np.asarray(D, dtype=object), p)
    return nmod_mat(D.shape[0], D.shape[1], [int(x) for x in D.ravel()], p)

def nmod_to_np(M):
    r, c = M.nrows(), M.ncols()
    return np.array([[int(M[i, j]) for j in range(c)] for i in range(r)], dtype=object)

def kernel_cols(M):
    """(basis, nullity): basis is n x nullity nmod_mat whose columns span ker M."""
    X, nul = M.nullspace()
    n = X.nrows()
    if nul == 0:
        return nmod_mat(n, 0, [], M.modulus()), 0
    # first `nul` columns of X span the nullspace
    p = M.modulus()
    B = nmod_mat(n, nul, [int(X[i, j]) for i in range(n) for j in range(nul)], p)
    return B, nul

def rank_of(M):
    return M.rank()

def hstack(mats, p):
    """horizontal concat of nmod_mats with equal nrows."""
    mats = [m for m in mats if m.ncols() > 0]
    if not mats:
        return nmod_mat(0, 0, [], p)
    r = mats[0].nrows()
    cols = sum(m.ncols() for m in mats)
    out = nmod_mat(r, cols, [0] * (r * cols), p)
    off = 0
    for m in mats:
        for i in range(r):
            for j in range(m.ncols()):
                out[i, off + j] = m[i, j]
        off += m.ncols()
    return out

def vstack2(A, B, p):
    ra, rb, c = A.nrows(), B.nrows(), A.ncols()
    assert B.ncols() == c
    out = nmod_mat(ra + rb, c, [0] * ((ra + rb) * c), p)
    for i in range(ra):
        for j in range(c):
            out[i, j] = A[i, j]
    for i in range(rb):
        for j in range(c):
            out[ra + i, j] = B[i, j]
    return out

# ------------------------------------------------------------ a cell
def build_one(lam, delta, p, n=4, verbose=False):
    B = build_cell(lam, delta, n=n, verbose=verbose)
    Efl = to_nmod(B['E'], p)
    K, a = kernel_cols(Efl)                 # n_chi x a, columns = HWV basis mod p
    return dict(lam=tuple(lam), delta=delta, p=p, B=B, E=B['E'], Efl=Efl,
                n_chi=B['n_chi'], a=a, K=K, N_S=B['N_S'], stab=B['stab'],
                nrows=int(B['E'].shape[0]), nnz=int(B['E'].nnz))

# ------------------------------------------------------------ transport J
def transport_matrix(prev, cur, p, n=4):
    """J : V_chi(delta-1) -> V_chi(delta), multiplication by c_{(4,0,...,0)}.

    Built at the chi level from the monomial arrays (the scalable form) and
    checked for consistency across every monomial of each target orbit.  Returns
    an n_chi(delta) x n_chi(delta-1) nmod_mat.
    """
    r = prev['B']['r']; assert cur['B']['r'] == r
    A = exps(n, r); L = len(A)
    i0 = A.index(tuple([n] + [0] * (r - 1)))          # (4,0,...,0) index (= L-1)
    Mp = prev['B']['arr']['M']; colp = prev['B']['arr']['col_of']; sgp = prev['B']['arr']['sgn']
    Mc = cur['B']['arr']['M'];  colc = cur['B']['arr']['col_of'];  sgc = cur['B']['arr']['sgn']
    ncp, ncc = prev['n_chi'], cur['n_chi']
    # index Mp by combinadic code for O(log) lookup of m = m' \ {i0}
    codesp = _codes(Mp, L); order = np.argsort(codesp, kind='stable'); sortedp = codesp[order]
    assert np.all(np.diff(sortedp) > 0)
    # entries J[ci, cj] = sgp(m) * sgc(m')  (constant over each target orbit ci)
    entries = {}
    dcur = Mc.shape[1]
    for row in range(Mc.shape[0]):
        ci = colc[row]
        if ci < 0:
            continue
        mrow = Mc[row]
        pos = np.searchsorted(mrow, i0)
        if pos >= dcur or mrow[pos] != i0:
            continue                                   # m' has no c-factor: not in image of J
        m = np.delete(mrow, pos)                        # remove one i0 -> weight lam_{delta-1}
        c = int((_codes(m[None, :], L))[0])
        q = np.searchsorted(sortedp, c)
        if q >= len(sortedp) or sortedp[q] != c:
            continue                                    # predecessor monomial not in basis (dropped orbit)
        rp = int(order[q])
        cj = colp[rp]
        if cj < 0:
            continue
        val = (int(sgp[rp]) * int(sgc[row])) % p
        key = (int(ci), int(cj))
        if key in entries:
            assert entries[key] == val, ("transport sign inconsistent", key, entries[key], val)
        else:
            entries[key] = val
    J = nmod_mat(ncc, ncp, [0] * (ncc * ncp), p)
    for (ci, cj), v in entries.items():
        J[ci, cj] = v
    return J

# ------------------------------------------------------------ deflation
def deflate(cur, prev_transported, a_prev, p, rng):
    """B_delta = ker[E_delta ; R], R = a_prev generic dense rows over F_p.
    Returns (Bdef, birth, R, JK) where JK = the transported predecessor kernel."""
    nc = cur['n_chi']
    if a_prev == 0:
        Bdef, birth = cur['K'], cur['a']         # seed: nothing to deflate
        return Bdef, birth, None, None
    R = nmod_mat(a_prev, nc, [int(x) for x in rng.integers(0, p, size=a_prev * nc)], p)
    stacked = vstack2(cur['Efl'], R, p)
    Bdef, birth = kernel_cols(stacked)
    return Bdef, birth, R, prev_transported

# ------------------------------------------------------------ certify a rung
def certify_rung(prev, cur, p, rng, n=4):
    """Full three-part certificate for cur built from prev.  Returns a dict."""
    out = dict(lam=list(cur['lam']), delta=cur['delta'], p=int(p),
               a=cur['a'], a_prev=(prev['a'] if prev else 0),
               n_chi=cur['n_chi'], N_S=int(cur['N_S']), stab=int(cur['stab']),
               nrows=cur['nrows'], nnz=cur['nnz'])
    if prev is None:
        # seed: M_delta = ker E, computed from scratch
        out['role'] = 'seed'
        out['birth'] = cur['a']
        out['seed_kernel_dim'] = cur['a']
        # confirm E @ K == 0 on the full E (raising certificate)
        Z = cur['Efl'] * cur['K']
        out['cert_full_raising'] = bool(all(Z[i, j] == 0 for i in range(Z.nrows()) for j in range(Z.ncols())))
        out['support_frac'] = support_frac(cur['K'])
        out['ok'] = out['cert_full_raising'] and out['birth'] == cur['a']
        return out
    out['role'] = 'rung'
    a_prev = prev['a']
    # ---- transport
    J = transport_matrix(prev, cur, p, n=n)
    out['transport_rank'] = rank_of(J)                       # must be n_chi(prev): J injective
    JK = J * prev['K']                                       # n_chi(cur) x a_prev
    # (i) transported vectors in ker E_delta (full E), and J injective on M_{prev}
    Z = cur['Efl'] * JK
    out['cert_i_transported_in_kernel'] = bool(all(Z[i, j] == 0 for i in range(Z.nrows()) for j in range(Z.ncols())))
    out['transported_rank'] = rank_of(JK)                    # = a_prev
    out['cert_i_injective'] = (out['transported_rank'] == a_prev) and (out['transport_rank'] == prev['n_chi'])
    # ---- deflate
    Bdef, birth, R, _ = deflate(cur, JK, a_prev, p, rng)
    out['birth'] = birth
    out['birth_expected'] = cur['a'] - a_prev
    # (ii) birth dim right, R nonsingular on J(M_{prev})
    out['cert_ii_birth_dim'] = (birth == cur['a'] - a_prev)
    RJK = R * JK
    out['cert_ii_R_nonsingular_on_J'] = (rank_of(RJK) == a_prev)
    # (iii) full raising on the new vectors, and completeness
    Zb = cur['Efl'] * Bdef
    out['cert_iii_new_full_raising'] = bool(all(Zb[i, j] == 0 for i in range(Zb.nrows()) for j in range(Zb.ncols())))
    # span(J(M_prev) (+) B_delta) has dim a_delta, and equals ker_Q E_delta
    both = hstack([JK, Bdef], p)
    out['sum_rank'] = rank_of(both)                          # = a_delta if direct sum fills
    withK = hstack([JK, Bdef, cur['K']], p)
    out['span_equals_kernel'] = (rank_of(withK) == cur['a']) and (out['sum_rank'] == cur['a'])
    out['cert_iii_complete'] = out['span_equals_kernel']
    # ---- support measurements
    out['support_frac'] = support_frac(cur['K'])
    out['support_frac_births'] = support_frac(Bdef)
    out['support_frac_transported'] = support_frac(JK)
    out['support_size'] = support_size(cur['K'])
    out['ok'] = all([out['cert_i_transported_in_kernel'], out['cert_i_injective'],
                     out['cert_ii_birth_dim'], out['cert_ii_R_nonsingular_on_J'],
                     out['cert_iii_new_full_raising'], out['cert_iii_complete']])
    return out, dict(J=J, JK=JK, Bdef=Bdef)

# ------------------------------------------------------------ support
def support_size(K):
    """number of chi-coordinates (rows) on which the subspace spanned by the
    columns of K is supported (basis-independent)."""
    r, c = K.nrows(), K.ncols()
    if c == 0:
        return 0
    s = 0
    for i in range(r):
        if any(K[i, j] != 0 for j in range(c)):
            s += 1
    return s

def support_frac(K):
    r = K.nrows()
    return round(support_size(K) / r, 4) if r else 0.0

# ------------------------------------------------------------ by-products i_X
def i_of(cur, side, p, npts=None, bound=40):
    """i_X(lam,delta) = nullity([E ; ev_X]) = a - mult_X, by the s45 pairing."""
    f, N = FORMS[side]
    a = cur['a']; K = npts if npts else a + 8
    EV = ev_rows_arr(f, N, 4, cur['B']['r'], cur['B']['arr'], K, SEEDS[side], bound, p)
    EVfl = np_to_nmod(EV, p)
    stacked = vstack2(cur['Efl'], EVfl, p)
    _, nul = kernel_cols(stacked)
    return dict(side=side, i=nul, mult=a - nul, a=a)

# ------------------------------------------------------------ idx0-free restriction (the scalable deflation)
def idx0_free_columns(cur, n=4):
    """chi-columns whose orbit monomials have NO c=(4,0,...,0) factor.  'Has a
    c-factor' is constant on each Stab(t)-orbit (Stab fixes position 1), so this
    is well-defined per column.  These are the columns where births live
    (lmr_cell.md sec 6: every new direction is represented in the u-free part)."""
    r = cur['B']['r']; A = exps(n, r); i0 = A.index(tuple([n] + [0] * (r - 1)))
    M = cur['B']['arr']['M']; col = cur['B']['arr']['col_of']; ncc = cur['n_chi']
    has_c = (M == i0).any(axis=1)
    free = np.ones(ncc, dtype=bool)
    # a column is idx0-free iff its (any) monomial is idx0-free; assert consistency
    seen = np.zeros(ncc, dtype=np.int8)  # 0 unset, 1 free, 2 hasc
    for row in range(M.shape[0]):
        c = col[row]
        if c < 0: continue
        val = 2 if has_c[row] else 1
        if seen[c] == 0: seen[c] = val
        else: assert seen[c] == val, ("idx0-free not constant on orbit", int(c))
    free = (seen == 1)
    return free, int(free.sum())

def deflate_restricted(cur, p):
    """Births by RESTRICTING E_delta to its idx0-free columns and taking the
    nullspace there -- the scalable form (no generic R, no full carrier).  Returns
    (dim, n_free)."""
    free, nfree = idx0_free_columns(cur)
    if nfree == 0:
        return 0, 0
    idx = np.nonzero(free)[0]
    Efree = cur['E'][:, idx]                       # scipy submatrix, n_rows x n_free
    Efl = to_nmod(Efree, p)
    _, nul = kernel_cols(Efl)
    return nul, nfree
