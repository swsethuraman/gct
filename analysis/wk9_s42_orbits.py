#!/usr/bin/env python3
"""
Session 42 -- vectorised isotypic basis (drop-in for wk9_s36_stabred.orbit_setup).

Same output contract as orbit_setup: (basis, vecs, group) with basis the
weight-lam monomials (tuples of exponent indices, as wk8_s30_core.monomials),
vecs the chi_lam-twisted Stab-orbit sums as dicts {monomial: +-1} (orbits whose
twisted sum vanishes dropped), group = stab_group(lam).  The orbit sums are the
same as orbit_setup's up to the overall sign of each orbit (a basis-vector
convention that no rank, nullity or (★)-split depends on); the validation
routine below checks orbits, supports and signs-up-to-global-sign against
orbit_setup on every cell it is given.

Method: monomials as an (N_S x delta) int32 array; for each group element g,
the image multiset (row-wise sort of tab_g[M]) is ranked by the multiset
combinadic  code(m) = sum_k C(m_k + k, k + 1)  (an injection into int64), and
searchsorted against the codes of the basis gives the index of g.m.  The orbit
representative is the member of minimal index; the twisted coefficient at
member j is  acc[j] = sum_g chi(g) [g . rep(j) = j],  accumulated over g.  Cost
|Stab| numpy passes over N_S x delta instead of a Python loop over N_S x |Stab|.
"""
import sys, os, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s36_stabred import stab_group, perm_tables, orbit_setup
from wk8_s30_core import exps, monomials
from math import comb

def _codes(M, L):
    """multiset combinadic of each row of the (N x d) sorted int array M (values < L)."""
    N, d = M.shape
    code = np.zeros(N, dtype=np.int64)
    for k in range(d):
        # C(m + k, k + 1) via a lookup table over m in [0, L)
        tab = np.array([comb(m + k, k + 1) for m in range(L)], dtype=np.int64)
        code += tab[M[:, k]]
    assert comb(L + d - 1, d) < (1 << 63)
    return code

def orbit_setup_fast(n, r, delta, lam, verbose=True):
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    basis = monomials(n, r, delta, lam)
    group = stab_group(lam)
    if not basis:
        return basis, [], group
    tabs = perm_tables(n, r, group)
    L = len(exps(n, r))
    M = np.array(basis, dtype=np.int32)          # N_S x delta, rows sorted ascending
    N = M.shape[0]
    codes0 = _codes(M, L)
    order = np.argsort(codes0, kind='stable')
    sorted_codes = codes0[order]
    assert np.all(np.diff(sorted_codes) > 0), "codes not injective"
    canon = np.arange(N, dtype=np.int64)
    pos_list = []
    for tab, ch in tabs:
        tabarr = np.asarray(tab, dtype=np.int32)
        img = np.sort(tabarr[M], axis=1)
        c = _codes(img, L)
        p = np.searchsorted(sorted_codes, c)
        assert np.all(sorted_codes[p] == c), "image monomial not in the basis (weight not preserved?)"
        idx = order[p]                            # index of g.m in `basis`
        pos_list.append((idx, ch))
        canon = np.minimum(canon, idx)
    acc = np.zeros(N, dtype=np.int64)
    ar = np.arange(N, dtype=np.int64)
    for idx, ch in pos_list:
        acc += ch * (idx[canon] == ar)
    # orbits: group members by canonical representative
    orbit_of = canon
    reps = np.unique(orbit_of)
    dropped = 0
    vecs = []
    sizes = np.bincount(orbit_of, minlength=N)
    G = len(group)
    for rep in reps:
        if acc[rep] == 0:
            dropped += 1
            continue
        members = np.nonzero(orbit_of == rep)[0] if False else None
        vecs.append(rep)
    # gather members per kept orbit efficiently
    keep = np.zeros(N, dtype=bool); keep[vecs] = True
    keep_members = keep[orbit_of]
    mem_idx = np.nonzero(keep_members)[0]
    mem_orb = orbit_of[mem_idx]
    srt = np.argsort(mem_orb, kind='stable')
    mem_idx = mem_idx[srt]; mem_orb = mem_orb[srt]
    bounds = np.searchsorted(mem_orb, np.array(vecs, dtype=np.int64))
    bounds = np.append(bounds, len(mem_idx))
    out = []
    for oi, rep in enumerate(vecs):
        ids = mem_idx[bounds[oi]:bounds[oi + 1]]
        st = G // len(ids)
        a = acc[ids]
        assert np.all(np.abs(a) == st), ("twisted coefficients not +-|Stab(m)|", lam, rep)
        out.append({basis[j]: (1 if a[k] > 0 else -1) for k, j in enumerate(ids)})
    if verbose:
        print(f"  lam={lam}: N_S={N} |Stab|={G} n_chi={len(out)} (orbits dropped: {dropped}) [fast, {time.time()-t0:.0f}s]", file=sys.stderr, flush=True)
    return basis, out, group

def validate(cells, n=4):
    """compare orbit_setup_fast with orbit_setup on the given (lam, delta) cells."""
    ok = 0
    for lam, delta in cells:
        r = len(lam)
        t = time.time(); b1, v1, g1 = orbit_setup(n, r, delta, lam, verbose=False); t1 = time.time() - t
        t = time.time(); b2, v2, g2 = orbit_setup_fast(n, r, delta, lam, verbose=False); t2 = time.time() - t
        assert b1 == b2 and g1 == g2
        s1 = {frozenset(v.keys()): v for v in v1}
        s2 = {frozenset(v.keys()): v for v in v2}
        assert set(s1) == set(s2), ("orbit sets differ", lam, delta, len(s1), len(s2))
        for kset, v in s1.items():
            w = s2[kset]
            m0 = next(iter(kset))
            sgn = v[m0] * w[m0]
            assert all(v[m] == sgn * w[m] for m in kset), ("sign pattern differs", lam, delta)
        ok += 1
        print(f"  {lam} d{delta}: N_S={len(b1)} n_chi={len(v1)} identical up to orbit signs; slow {t1:.1f}s fast {t2:.1f}s", flush=True)
    return ok

def _main():
    cells = [((8,4,4,4,4),6), ((10,10,2,2,2,2),7), ((13,5,4,1,1),6), ((12,5,5,1,1),6), ((7,7,4,1,1),5),
             ((10,8,7,1,1,1),7), ((15,4,4,2,2,1),7), ((14,7,4,2,1),7), ((8,8,8,1,1,1,1),7), ((12,8,8,1,1,1,1),8),
             ((13,8,2,2,2,1),7), ((14,6,2,2,2,2),7), ((4,4,4,4,4),5), ((9,7,4,2,1,1),6), ((20,4,2,2,2,2),8), ((11,11,2,2,1,1),7)]
    print("validated", validate(cells), "cells")
    validate_rows(cells)

if __name__ == '__main__':
    _main()

# ------------------------------------------------ vectorised reduced rows
def reduced_rows_fast(n, r, delta, lam, basis, vecs, verbose=True):
    """The rows of every simple raising operator E_{i,i+1} restricted to V_chi,
    one canonical representative per H-orbit of target monomials
    (H = Stab(lam) ∩ Stab(lam')), chi-obstructed H-fixed targets asserted to
    cancel -- the same matrix as wk9_s36_stabred.reduced_rows up to the choice
    of representative row in each H-orbit (a scalar), returned as a scipy csr
    (int64 raw values) over the n_chi columns, plus the per-monomial column
    map.  Cost: numpy passes, no Python loop over monomials."""
    from scipy import sparse
    lam = tuple(lam) + (0,) * (r - len(lam))
    t0 = time.time()
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}; L = len(A)
    M = np.array(basis, dtype=np.int32); N = M.shape[0]; d = M.shape[1]
    # column and sign of every monomial (members of dropped orbits: col -1)
    col_of = np.full(N, -1, dtype=np.int64); sgn = np.zeros(N, dtype=np.int64)
    pos = {m: k for k, m in enumerate(basis)}
    for c, vec in enumerate(vecs):
        for m, s in vec.items():
            k = pos[m]; col_of[k] = c; sgn[k] = s
    Aarr = np.array(A, dtype=np.int32)              # L x r
    blocks = []
    nfixed = 0
    for i in range(r - 1):
        j = i + 1
        if lam[j] == 0: continue
        shift = np.full(L, -1, dtype=np.int64)
        for a, al in enumerate(A):
            if al[j] > 0:
                nb = list(al); nb[j] -= 1; nb[i] += 1; shift[a] = idx[tuple(nb)]
        codes_all, cols_all, vals_all, mons_all = [], [], [], []
        for k in range(d):
            src = M[:, k]
            new = shift[src]
            valid = (new >= 0) & (col_of >= 0)
            if not valid.any(): continue
            rows_new = M[valid].copy(); rows_new[:, k] = new[valid]
            rows_new.sort(axis=1)
            codes_t = _codes(rows_new, L)
            coef = sgn[valid] * (Aarr[src[valid], i].astype(np.int64) + 1)
            codes_all.append(codes_t); cols_all.append(col_of[valid]); vals_all.append(coef); mons_all.append(rows_new)
        codes_t = np.concatenate(codes_all); cols = np.concatenate(cols_all); vals = np.concatenate(vals_all); mons = np.concatenate(mons_all)
        ucodes, first, rowid = np.unique(codes_t, return_index=True, return_inverse=True)
        T = mons[first]                                  # one monomial per target
        nt = len(ucodes)
        Ei = sparse.coo_matrix((vals, (rowid, cols)), shape=(nt, len(vecs)), dtype=np.int64).tocsr()
        Ei.sum_duplicates(); Ei.eliminate_zeros()
        # H-orbit dedup of the target rows
        H = stab_group(lam, fix=(i, j))
        Htabs = perm_tables(n, r, H)
        canon = np.arange(nt, dtype=np.int64); obstructed = np.zeros(nt, dtype=bool)
        for tab, ch in Htabs:
            tabarr = np.asarray(tab, dtype=np.int32)
            img = np.sort(tabarr[T], axis=1)
            c = _codes(img, L)
            p = np.searchsorted(ucodes, c)
            hit = (p < nt)
            hit[hit] &= (ucodes[p[hit]] == c[hit])
            q = np.where(hit, p, -1)
            # targets whose H-image is outside the hit set are not in the target set of this weight (cannot happen: weight preserved) -- assert
            assert hit.all(), "H-image of a target not among the targets"
            if ch == -1: obstructed |= (q == np.arange(nt))
            canon = np.minimum(canon, q)
        keep = (canon == np.arange(nt)) & ~obstructed
        obs_rows = np.nonzero(obstructed)[0]
        if len(obs_rows):
            sub = Ei[obs_rows]
            assert sub.nnz == 0, ("chi-obstructed fixed rows failed to cancel", i, int(sub.nnz))
        nfixed += int(obstructed.sum())
        Ek = Ei[np.nonzero(keep)[0]]
        Ek.eliminate_zeros()
        nz = np.diff(Ek.indptr) > 0
        Ek = Ek[np.nonzero(nz)[0]]
        blocks.append(Ek)
        if verbose:
            print(f"    E_{i}{j}: |H|={len(H)} targets {nt} canonical rows {Ek.shape[0]} nnz {Ek.nnz} (obstructed fixed targets cancelled: {int(obstructed.sum())}) [{time.time()-t0:.0f}s]", file=sys.stderr, flush=True)
    E = sparse.vstack(blocks).tocsr() if blocks else sparse.csr_matrix((0, len(vecs)), dtype=np.int64)
    return E, nfixed

def validate_rows(cells, n=4):
    from wk9_s36_stabred import reduced_rows
    from wk9_s42_sparse import rows_to_csr
    from flint import nmod_mat
    P = 2147483647
    for lam, delta in cells:
        r = len(lam)
        basis, vecs, group = orbit_setup_fast(n, r, delta, lam, verbose=False)
        t = time.time(); rows, nf1 = reduced_rows(n, r, delta, lam, vecs, verbose=False); t1 = time.time() - t
        t = time.time(); E, nf2 = reduced_rows_fast(n, r, delta, lam, basis, vecs, verbose=False); t2 = time.time() - t
        E1 = rows_to_csr(rows, len(vecs))
        assert E1.shape[0] == E.shape[0] and E1.nnz == E.nnz, ("row count / nnz differ", lam, delta, E1.shape, E.shape, E1.nnz, E.nnz)
        # same row space: rank of each and of the stack, mod P (small cells only)
        if len(vecs) <= 1500:
            def rk(X):
                X = X.tocoo(); Mx = nmod_mat(X.shape[0], X.shape[1], P)
                for a, b, v in zip(X.row, X.col, X.data): Mx[int(a), int(b)] = int(v) % P
                return Mx.rank()
            from scipy import sparse
            r1, r2, r12 = rk(E1), rk(E), rk(sparse.vstack([E1, E]))
            assert r1 == r2 == r12, ("row spaces differ", lam, delta, r1, r2, r12)
            note = f"row spaces equal (rank {r1})"
        else:
            note = "sizes equal"
        print(f"  {lam} d{delta}: rows {E.shape[0]} nnz {E.nnz} obstructed {nf1}/{nf2}: {note}; slow {t1:.1f}s fast {t2:.1f}s", flush=True)
