#!/usr/bin/env python3
"""Session 45 -- V5: the memory-lean build against the s36 / s42 implementations.

Checks, per cell, that wk9_s45_build reproduces exactly what the validated code
produces:
  (a) the monomial array equals wk8_s30_core.monomials in content AND order;
  (b) the orbit partition and the twisted signs equal orbit_setup_fast's up to
      the per-orbit global sign (which no rank depends on) -- so identical n_chi,
      identical orbits, identical column map up to a permutation of columns and a
      sign per column;
  (c) the raising-operator matrix has the same shape, the same nnz, and the same
      ROW SPACE (checked by flint rank of E, of E', and of the stack) after
      undoing the column permutation and signs;
  (d) the vectorised evaluation rows equal wk9_s36_stabred.point_rows entrywise
      on the same random stream.

usage: python3 wk9_s45_validate.py [--full]
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from wk8_s30_core import monomials, exps
from wk9_s36_stabred import orbit_setup, reduced_rows, point_rows, DET4, N_DET, PAD34, N_PAD, P1, P2
from wk9_s42_orbits import orbit_setup_fast, reduced_rows_fast
from wk9_s42_sparse import rows_to_csr
from wk9_s45_build import monomials_array, orbit_setup_arr, raising_rows_arr, ev_rows_arr, log
from flint import nmod_mat
from scipy import sparse

CELLS = [((8, 4, 4, 4, 4), 6), ((10, 8, 7, 1, 1, 1), 7), ((11, 11, 2, 2, 1, 1), 7),
         ((4, 4, 4, 4, 4), 5), ((22, 2, 2, 2, 2, 2), 8), ((9, 9, 8, 1, 1), 7),
         ((8, 8, 8, 2, 2), 7), ((12, 4, 4, 4, 4), 7), ((13, 5, 4, 1, 1), 6),
         ((10, 10, 2, 2, 2, 2), 7), ((12, 10, 3, 1, 1, 1), 7), ((19, 5, 5, 1, 1, 1), 8),
         ((21, 3, 2, 2, 2, 2), 8), ((16, 10, 3, 1, 1, 1), 8), ((11, 9, 2, 2, 2, 2), 7),
         ((12, 12, 2, 2, 2, 2), 8)]

def rk(X, p):
    X = sparse.csr_matrix(X).tocoo()
    M = nmod_mat(int(X.shape[0]), int(X.shape[1]), p)
    for a, b, v in zip(X.row, X.col, X.data): M[int(a), int(b)] = int(v) % p
    return M.rank()

def check_cell(lam, delta, n=4, p=P1, rank_cap=1600, verbose=True):
    r = len(lam)
    res = dict(lam=list(lam), delta=delta)
    # (a) monomials
    B = monomials(n, r, delta, lam)
    M = monomials_array(n, r, delta, lam)
    assert M.shape[0] == len(B), ("N_S differs", lam, delta, M.shape[0], len(B))
    assert np.array_equal(M, np.array(B, dtype=np.int32).reshape(len(B), delta)), \
        ("monomial array differs from wk8_s30_core.monomials (content or order)", lam, delta)
    res['N_S'] = int(M.shape[0])
    # (b) orbits
    basis, vecs, group, arr42 = orbit_setup_fast(n, r, delta, lam, verbose=False, arrays=True)
    arr = orbit_setup_arr(n, r, delta, lam, M=M, verbose=False)
    assert arr['n_chi'] == arr42['n_chi'], ("n_chi differs", lam, delta, arr['n_chi'], arr42['n_chi'])
    res['n_chi'] = int(arr['n_chi']); res['stab'] = int(arr['stab'])
    c45, c42 = arr['col_of'], arr42['col_of']
    assert np.array_equal(c45 >= 0, c42 >= 0), ("dropped-orbit sets differ", lam, delta)
    sel = c45 >= 0
    # the orbit partition must agree: c45 and c42 induce the same equivalence
    perm = np.full(arr['n_chi'], -1, dtype=np.int64)
    perm[c45[sel]] = c42[sel]
    assert np.array_equal(perm[c45[sel]], c42[sel]) and len(np.unique(perm)) == arr['n_chi'], \
        ("orbit partitions differ", lam, delta)
    # signs agree up to one global sign per orbit
    s45, s42 = arr['sgn'], arr42['sgn']
    gs = np.zeros(arr['n_chi'], dtype=np.int64)
    gs[c45[sel]] = (s45[sel] * s42[sel])
    assert np.all(np.abs(gs) == 1) and np.array_equal(s45[sel] * s42[sel], gs[c45[sel]]), \
        ("orbit signs differ by more than a global sign per orbit", lam, delta)
    # (c) raising operators
    E45, nf45 = raising_rows_arr(n, r, delta, lam, arr, verbose=False)
    E42, nf42 = reduced_rows_fast(n, r, delta, lam, basis, vecs, verbose=False, arr=arr42)
    rows36, nf36 = reduced_rows(n, r, delta, lam, vecs, verbose=False)
    E36 = rows_to_csr(rows36, arr42['n_chi'])
    assert (E45.shape[0], E45.nnz) == (E42.shape[0], E42.nnz) == (E36.shape[0], E36.nnz), \
        ("row count / nnz differ", lam, delta, (E45.shape[0], E45.nnz), (E42.shape[0], E42.nnz), (E36.shape[0], E36.nnz))
    assert nf45 == nf42 == nf36, ("obstructed-row counts differ", lam, delta, nf45, nf42, nf36)
    res['nrows'] = int(E45.shape[0]); res['nnz'] = int(E45.nnz); res['nfixed'] = int(nf45)
    # put E45 into the s42 column labelling and signs, then compare row spaces
    P = sparse.csr_matrix((gs, (np.arange(arr['n_chi']), perm)), shape=(arr['n_chi'],) * 2, dtype=np.int64)
    E45p = (E45 @ P).tocsr()
    if arr['n_chi'] <= rank_cap:
        r1, r2, r3 = rk(E45p, p), rk(E42, p), rk(sparse.vstack([E45p, E42, E36]), p)
        assert r1 == r2 == r3, ("row spaces differ", lam, delta, r1, r2, r3)
        res['rank'] = int(r1); res['rowspace'] = 'equal (rank %d)' % r1
    else:
        res['rowspace'] = 'sizes equal (rank check skipped, n_chi > %d)' % rank_cap
    # (d) evaluation rows
    K = 4
    for tag, (f, N) in (('det', (DET4, N_DET)), ('pad', (PAD34, N_PAD))):
        seed = 11 if tag == 'det' else 29
        ev36 = np.array(point_rows(f, N, n, r, basis, vecs, K, seed, 40, p), dtype=np.int64)
        ev45 = ev_rows_arr(f, N, n, r, arr, K, seed, 40, p)
        # ev45 is in the s45 column labelling with the s45 signs
        ev45p = np.zeros_like(ev45)
        ev45p[:, perm] = (ev45 * gs[None, :]) % p
        assert np.array_equal(ev45p % p, ev36 % p), ("evaluation rows differ", lam, delta, tag)
    res['ev'] = 'identical (det and pad, K=%d)' % K
    if verbose:
        log(f"  V5 {lam} d{delta}: N_S={res['N_S']} n_chi={res['n_chi']} rows={res['nrows']} "
            f"nnz={res['nnz']} obstructed={res['nfixed']}; orbits+signs OK; {res['rowspace']}; ev {res['ev']}")
    monomials.cache_clear()
    return res

if __name__ == '__main__':
    out = []
    for lam, delta in CELLS:
        out.append(check_cell(lam, delta))
    print(json.dumps(out, indent=None))
    with open(os.path.join(HERE, '..', 'results', 's45_v5.jsonl'), 'w') as f:
        for o in out: f.write(json.dumps(o) + "\n")
    log(f"V5: {len(out)}/{len(CELLS)} cells identical to the s36/s42 build")
