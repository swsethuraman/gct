#!/usr/bin/env python3
"""
Session 63 -- measure the SUPPORT |S| of the highest-weight (source) vectors at
buildable LMR-family cells, to decide the Gram/Schur (C2) route at r = 9.

The integrator notes (S2, note to 62/63) make |S| -- the size of the union of
the supports of the transported source vectors -- the single number that prices
session 63: the C2 Gram block costs ~ a*|S|^2 + a^2*|S|.  |S| at the LMR cell is
out of reach to build directly (n_chi ~ 3.1e7), so we measure how |S| scales at
small cells of the SAME family and read off whether the source vectors are
sparse (|S| << n_chi) or dense (|S| ~ n_chi).

For each cell we build the chi-isotypic reduction (wk9_s45_build.build_cell),
take the kernel of the stacked raising operators E over a house prime (that
kernel is the a-dim HWV space), and report:
  n_chi                    the reduced weight-space dimension
  |S| = supp(kernel)       number of chi-columns nonzero in SOME kernel vector
  max per-vector support   the largest single HWV support
  |S| / n_chi              the density that decides the extrapolation

usage: python3 analysis/wk10_s63_support.py            # the family sweep
       python3 analysis/wk10_s63_support.py K M [K M...]  # specific (k,m)
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk9_s45_build import build_cell

P1 = 2147483647


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


DENSE_ENTRIES_CAP = 60_000_000    # ~0.5 GB int64; the compressed matrix built in one shot


def _rref_kernel_support(C, p):
    """C: (rows x n) int64 numpy, entries in [0,p). Row-reduce mod p in place and
    return (nullity, support_cols, per_vec_supports) of the kernel of C, using
    only O(rows*n) memory (no python-flint tolist)."""
    C = C % p
    rows, n = C.shape
    pivots = []       # (col) in pivot order
    pivrow_of_col = {}
    r = 0
    for c in range(n):
        if r >= rows:
            break
        # find pivot at or below r in column c
        col = C[r:, c]
        nz = np.nonzero(col)[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            C[[r, pr]] = C[[pr, r]]
        inv = pow(int(C[r, c]), p - 2, p)
        C[r] = (C[r] * inv) % p
        # eliminate this column from all other rows
        colvals = C[:, c].copy()
        colvals[r] = 0
        nzr = np.nonzero(colvals)[0]
        if nzr.size:
            C[nzr] = (C[nzr] - np.outer(colvals[nzr], C[r])) % p
        pivots.append(c); pivrow_of_col[c] = r
        r += 1
    pivot_cols = set(pivots)
    free_cols = [c for c in range(n) if c not in pivot_cols]
    nul = len(free_cols)
    # kernel basis: one vector per free column f; x_f = 1, x_pivotcol = -C[pivrow, f]
    supp = set()
    per_vec = []
    for f in free_cols:
        s = {f}
        for c in pivots:
            v = int(C[pivrow_of_col[c], f]) % p
            if v != 0:
                s.add(c)
        per_vec.append(len(s)); supp |= s
    return nul, np.array(sorted(supp), dtype=np.int64), per_vec


def kernel_support(E, n_chi, a, p=P1, seed=20260907):
    """basis of ker(E) mod p (dim = a); return (nul, support_cols, per_vec_supports).
    Exact dense nullspace when E fits; else one random row-compression to
    n_chi+64 rows built as a single dense numpy array (rank(P E) = rank E once the
    nullity hits a, s41 semantics).  Raises if n_chi too large for the cap."""
    FLINT_ENTRIES_CAP = 120_000_000   # ~ tolist of this many python ints; fits 7 GB
    Em = sparse.csr_matrix(E)
    nrows = Em.shape[0]
    if nrows * n_chi <= FLINT_ENTRIES_CAP:
        D = np.zeros((nrows, n_chi), dtype=np.int64)
        coo = Em.tocoo(); D[coo.row, coo.col] = coo.data % p
        Mf = nmod_mat(nrows, n_chi, D.ravel().tolist(), p); del D
    else:
        rs = n_chi + 64
        if rs * n_chi > FLINT_ENTRIES_CAP:
            raise MemoryError(f"n_chi={n_chi}: compressed {rs}x{n_chi} exceeds flint cap ({FLINT_ENTRIES_CAP})")
        rng = np.random.default_rng(seed)
        C = np.zeros((rs, n_chi), dtype=np.int64)             # rs x n_chi accumulator
        blk = max(1, 40_000_000 // n_chi)                     # keep R_blk small
        for b0 in range(0, nrows, blk):
            b1 = min(b0 + blk, nrows)
            Rblk = rng.integers(1, p, (rs, b1 - b0), dtype=np.int64)   # rs x bs
            C = (C + (Rblk @ Em[b0:b1])) % p                  # sparse rmatmul -> dense
            del Rblk
        Mf = nmod_mat(rs, n_chi, np.ascontiguousarray(C).ravel().tolist(), p); del C
    X, nul = Mf.nullspace()
    K = np.array([[int(X[i, j]) for i in range(n_chi)] for j in range(nul)], dtype=np.int64).reshape(nul, n_chi)
    Kp = K % p
    supp_cols = np.nonzero((Kp != 0).any(axis=0))[0]
    per_vec = [int((Kp[j] != 0).sum()) for j in range(nul)]
    return nul, supp_cols, per_vec


def measure(k, m):
    lam = (3 * k + 2 * m, k) + (2,) * m
    delta = k + m
    t0 = time.time()
    B = build_cell(lam, delta, n=4, verbose=False)
    nul, supp, per_vec = kernel_support(B['E'], B['n_chi'], None, P1)
    S = int(len(supp))
    row = dict(k=k, m=m, lam=list(lam), delta=delta, r=len(lam),
               a=int(nul), N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(B['n_chi']),
               nrows=int(B['nrows']), nnz=int(B['nnz']),
               S=S, S_over_nchi=round(S / B['n_chi'], 4),
               max_vec_supp=int(max(per_vec)) if per_vec else 0,
               mean_vec_supp=round(float(np.mean(per_vec)), 1) if per_vec else 0,
               secs=round(time.time() - t0, 1), hwm_gb=round(B['hwm_gb'], 2))
    log(f"  (k={k},m={m}) lam={lam} d={delta}: a={nul} n_chi={B['n_chi']} "
        f"|S|={S} (|S|/n_chi={row['S_over_nchi']}) max_supp={row['max_vec_supp']} "
        f"({row['secs']}s, {row['hwm_gb']}GB)")
    return row


if __name__ == '__main__':
    args = [int(x) for x in sys.argv[1:]]
    if args:
        pairs = list(zip(args[0::2], args[1::2]))
    else:
        pairs = [(4, 2), (5, 3), (5, 4), (6, 4), (7, 4), (6, 5)]
    out = os.path.join(ROOT, 'results', 's63_support.jsonl')
    fh = open(out, 'a')
    for k, m in pairs:
        try:
            row = measure(k, m)
            fh.write(json.dumps(row) + "\n"); fh.flush()
        except Exception as e:
            log(f"  (k={k},m={m}) FAILED: {e}")
    fh.close()
