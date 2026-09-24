#!/usr/bin/env python3
"""
Session 71 -- the hybrid route: a structural (initial-term) cover of the raising
operator, then the exact kernel on the small uncovered residual.

Given F (sparse, m x nc, integer entries) and a column order sigma, the rows of
F whose sigma-leading columns are pairwise distinct are linearly independent
(order them by leading column: the submatrix on those columns is triangular
with a nonzero diagonal), so

    #distinct leading columns  <=  rank F          (for every sigma, every field)

-- session 67's initial-term certifier, re-implemented here from its record.
Reaching nc certifies full column rank at O(nnz); a shortfall says nothing.

The hybrid (session 67 Part B's "only version worth a successor's time"):
let R_1 be the chosen cover rows, S their leading columns (in sigma order),
U the uncovered columns, T = R_1[:, S] (upper triangular, invertible mod p) and
X = T^{-1} R_1[:, U].  Every kernel vector y of F satisfies y_S = -X y_U, and

    nullity(F) = nullity(S_U),   S_U = F_o[:, U] - F_o[:, S] X   (F_o = the other rows),

the Schur complement on the residual.  S_U is projected by a random sparse +-1
matrix P with |U| + extra rows (rank(P S_U) <= rank(S_U), so nullity can only
go UP under projection), its kernel is computed exactly by python-flint, every
kernel vector is lifted (y_S by a triangular solve) and VERIFIED against the
full F.  When the number of verified vectors equals nullity(P S_U) the kernel
is exhibited exactly: nullity(F) >= #verified, nullity(F) <= nullity(P S_U).
A projection with surplus nullity is retried with more rows, never accepted.

Soundness never depends on the randomness (sigma, P): a certified cover is a
proof, a verified kernel vector is a proof, and the upper bound is a rank of an
explicit matrix.  Only whether a run is conclusive depends on the draw.
"""
import os, sys, time, ctypes, subprocess
import numpy as np
from scipy import sparse
from flint import nmod_mat

HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = None


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def lib():
    global _LIB
    if _LIB is None:
        so = os.environ.get('S71_SCHUR_SO', '/home/claude/s71/schur.so')
        src = os.path.join(HERE, 'wk11_s71_schur.c')
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            os.makedirs(os.path.dirname(so), exist_ok=True)
            subprocess.check_call(['gcc', '-O3', '-march=native', '-shared', '-fPIC', '-o', so, src])
        _LIB = ctypes.CDLL(so)
        i64 = ctypes.c_int64; u64 = ctypes.c_uint64; vp = ctypes.c_void_p
        _LIB.trisolve.argtypes = [i64, i64, vp, vp, vp, vp, vp, u64]; _LIB.trisolve.restype = ctypes.c_int
        _LIB.schur_project.argtypes = [i64, vp, vp, vp, vp, vp, vp, i64, i64, vp, u64, u64, ctypes.c_int]
        _LIB.schur_project.restype = ctypes.c_int
        _LIB.spmm_mod.argtypes = [i64, vp, vp, vp, vp, i64, vp, u64]; _LIB.spmm_mod.restype = ctypes.c_int
    return _LIB


def _ptr(a):
    return a.ctypes.data_as(ctypes.c_void_p)


# ------------------------------------------------------------------ orders
def column_orders(F, nc, seed):
    """the pre-registered orders: natural, reversed, column-fill ascending,
    column-fill descending, one random.  Each is (name, pos) with pos[col] =
    position of the column in the order."""
    fill = np.bincount(F.indices, minlength=nc)
    out = [('natural', np.arange(nc, dtype=np.int64)),
           ('reversed', np.arange(nc - 1, -1, -1, dtype=np.int64))]
    o = np.argsort(fill, kind='stable'); pos = np.empty(nc, dtype=np.int64); pos[o] = np.arange(nc); out.append(('fill_asc', pos))
    o = np.argsort(-fill, kind='stable'); pos = np.empty(nc, dtype=np.int64); pos[o] = np.arange(nc); out.append(('fill_desc', pos))
    rng = np.random.default_rng(seed)
    o = rng.permutation(nc); pos = np.empty(nc, dtype=np.int64); pos[o] = np.arange(nc); out.append(('random', pos))
    return out


def cover(F, nc, pos):
    """rows with pairwise distinct leading columns under the order `pos`
    (one row per leading column, the sparsest).  Returns dict(rows, S, U,
    pos, size) with S the covered columns in increasing position and rows[i]
    the row whose leading column is S[i]."""
    F = F.tocsr(); F.sort_indices()
    nz = np.diff(F.indptr) > 0
    if not nz.any():
        return dict(rows=np.zeros(0, np.int64), S=np.zeros(0, np.int64), U=np.arange(nc), pos=pos, size=0)
    starts = F.indptr[:-1][nz]
    p = pos[F.indices]
    minpos = np.minimum.reduceat(p, starts)                 # per nonempty row
    rows = np.nonzero(nz)[0]
    nnz_row = np.diff(F.indptr)[nz]
    order = np.lexsort((nnz_row, minpos))
    ms = minpos[order]
    first = np.r_[True, ms[1:] != ms[:-1]]
    chosen = rows[order[first]]
    Spos = ms[first]
    inv = np.empty(nc, dtype=np.int64); inv[pos] = np.arange(nc)
    S = inv[Spos]
    covered = np.zeros(nc, dtype=bool); covered[S] = True
    Ucols = np.nonzero(~covered)[0]
    Upos = pos[Ucols]; Ucols = Ucols[np.argsort(Upos)]
    return dict(rows=chosen, S=S, U=Ucols, pos=pos, size=int(len(S)))


def best_cover(F, nc, seed=20260908, names=None):
    stats = {}
    best = None
    for name, pos in column_orders(F, nc, seed):
        if names and name not in names: continue
        c = cover(F, nc, pos)
        stats[name] = c['size']
        if best is None or c['size'] > best['size']:
            best = c; best['order'] = name
    best['stats'] = stats
    return best


# ------------------------------------------------------------- the residual
def _split_rows(F, rows, colS, colU, p):
    """rows of F (CSR) split into the S part (T, columns re-indexed to S positions,
    data mod p as uint32 with the diagonal inverses) and the U part (CSR int32,
    columns re-indexed to U positions)."""
    R = F[rows].tocsr(); R.sort_indices()
    inS = colS[R.indices] >= 0
    nS = len(rows); nU = int((colU >= 0).sum())
    rowid = np.repeat(np.arange(nS), np.diff(R.indptr))
    Tr = rowid[inS]; Tc = colS[R.indices[inS]]; Tv = (R.data[inS] % p).astype(np.int64)
    T = sparse.csr_matrix((Tv, (Tr, Tc)), shape=(nS, nS), dtype=np.int64); T.sort_indices()
    diag = np.asarray(T.diagonal(), dtype=np.int64)
    assert np.all(diag != 0), "cover diagonal vanishes mod p"
    assert T.nnz == int(inS.sum())
    dinv = np.array([pow(int(d), -1, p) for d in diag], dtype=np.uint32)
    Ur = rowid[~inS]; Uc = colU[R.indices[~inS]]
    assert np.all(Uc >= 0)
    TU = sparse.csr_matrix((R.data[~inS].astype(np.int32), (Ur, Uc)), shape=(nS, nU), dtype=np.int32); TU.sort_indices()
    return T, dinv, TU


def trisolve(T, dinv, B, p):
    """B := T^{-1} B in place (B uint32, C contiguous)."""
    nS, m = B.shape
    assert B.dtype == np.uint32 and B.flags['C_CONTIGUOUS']
    indptr = T.indptr.astype(np.int64); indices = T.indices.astype(np.int32); data = T.data.astype(np.uint32)
    rc = lib().trisolve(nS, m, _ptr(indptr), _ptr(indices), _ptr(data), _ptr(dinv), _ptr(B), p)
    assert rc == 0, ("trisolve", rc)
    return B


def spmm_mod(A, X, p):
    """A (CSR int32 data, global columns) times X (dense uint32, n x m) mod p."""
    A = A.tocsr(); n, m = X.shape
    assert A.shape[1] == n and X.dtype == np.uint32 and X.flags['C_CONTIGUOUS']
    indptr = A.indptr.astype(np.int64); indices = A.indices.astype(np.int32); data = A.data.astype(np.int32)
    Y = np.zeros((A.shape[0], m), dtype=np.uint32)
    rc = lib().spmm_mod(A.shape[0], _ptr(indptr), _ptr(indices), _ptr(data), _ptr(X), m, _ptr(Y), p)
    assert rc == 0
    return Y


def matmul_mod(A, B, p, blk=64):
    """(A @ B) mod p for arrays with entries in [0, p), p < 2^31, inner dimension
    < 2^21: 16-bit limb split, each partial product exact in float64; B is taken
    in column blocks so its float64 limbs never exceed a block."""
    A = np.asarray(A, dtype=np.int64) % p
    assert A.shape[1] < (1 << 21)
    Alo = (A & 0xFFFF).astype(np.float64); Ahi = (A >> 16).astype(np.float64)
    out = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
    for c0 in range(0, B.shape[1], blk):
        Bc = np.asarray(B[:, c0:c0 + blk], dtype=np.int64) % p
        Blo = (Bc & 0xFFFF).astype(np.float64); Bhi = (Bc >> 16).astype(np.float64)
        ll = (Alo @ Blo).astype(np.int64) % p; lh = (Alo @ Bhi).astype(np.int64) % p
        hl = (Ahi @ Blo).astype(np.int64) % p; hh = (Ahi @ Bhi).astype(np.int64) % p
        mid = ((lh + hl) % p) * 65536 % p
        top = (hh * ((1 << 32) % p)) % p
        out[:, c0:c0 + blk] = (ll + mid + top) % p
    return out


def check_kernel_mat(E, K, p, chunk=16):
    """E K == 0 mod p for CSR E with |entries| < 2^16 and K (nc x a) in [0, p),
    column blocks of `chunk` so the dense product stays small."""
    assert int(np.abs(E.data).max(initial=0)) < 65536
    K = np.asarray(K, dtype=np.int64) % p
    for c0 in range(0, K.shape[1], chunk):
        Kc = K[:, c0:c0 + chunk]
        lo = Kc & 0xFFFF; hi = Kc >> 16
        r = ((E @ lo) % p + ((E @ hi) % p) * 65536) % p
        if np.any(r): return False
    return True


def rank_mod_p(M, p):
    M = np.asarray(M, dtype=np.int64) % p
    if M.size == 0: return 0
    return nmod_mat(M.shape[0], M.shape[1], M.ravel().tolist(), p).rank()


def nullspace_mod_p(M, p):
    M = np.asarray(M, dtype=np.int64) % p
    m, n = M.shape
    X, nul = nmod_mat(m, n, M.ravel().tolist(), p).nullspace()
    return np.array([[int(X[i, j]) for i in range(n)] for j in range(nul)], dtype=np.int64).reshape(nul, n)


def rank_tall(K, p, seed=20260908, extra=32, exact_cap=30_000_000):
    """rank mod p of a tall (n x a) matrix K, exactly: a random sparse +-1
    projection Q with a + extra rows gives r = rank(Q K) <= rank K; if r = a
    that is a proof.  Otherwise the kernel C of Q K (a - r vectors) is checked
    exactly on K: K C = 0 exhibits nullity(K) >= a - r, so rank K <= r, hence
    rank K = r.  If the check fails (the projection lost rank) it is repeated
    with more rows; the dense flint rank is the last resort for small K."""
    n, a = K.shape
    if a == 0: return 0
    if n <= a + extra:
        return rank_mod_p(np.asarray(K, dtype=np.int64), p)
    rng = np.random.default_rng(seed + n + a)
    m = a + extra
    for attempt in range(4):
        per = 8 + 4 * attempt
        cols = np.repeat(np.arange(n), per); rws = rng.integers(0, m, size=n * per)
        sg = rng.choice(np.array([-1, 1], dtype=np.int64), size=n * per)
        Q = sparse.csr_matrix((sg, (rws, cols)), shape=(m, n), dtype=np.int64)
        QK = np.zeros((m, a), dtype=np.int64)
        for c0 in range(0, a, 64):                         # |Q K| entries: sums of < 2^31 terms, exact in int64
            QK[:, c0:c0 + 64] = (Q @ np.asarray(K[:, c0:c0 + 64], dtype=np.int64)) % p
        r = rank_mod_p(QK, p)
        if r == a: return a
        C = nullspace_mod_p(QK, p)                          # (a - r) x a combos: Q K c = 0
        assert C.shape[0] == a - r
        okv = True
        for r0 in range(0, n, 200_000):
            blkK = np.asarray(K[r0:r0 + 200_000], dtype=np.int64) % p
            if np.any(matmul_mod(blkK, C.T % p, p)):
                okv = False; break
        if okv: return r
        m += a + extra
    if n * a <= exact_cap:
        return rank_mod_p(np.asarray(K, dtype=np.int64), p)
    raise RuntimeError(("rank_tall: projection lost rank four times", n, a))


def hybrid_kernel(E, nc, p, a_expect, cov, seed=20260908, extra=64, nproj=8, retries=4, verbose=True, tag='',
                  ublock=None, vblock=64, mem_x=1.0e9):
    """the exact mod-p kernel of E (nc columns) through the cover `cov`.
    Returns (K (nc x a uint32, verified E K = 0), info).  X = T^{-1} R_1[:, U] is
    never held whole: it is formed in column blocks of U (`ublock`, sized so a
    block is at most `mem_x` bytes), each block's Schur columns projected and
    discarded; the kernel is lifted in blocks of `vblock` vectors."""
    t0 = time.time()
    E = E.tocsr(); E.sort_indices()
    rows = cov['rows']; S = cov['S']; U = cov['U']
    nS, nU = len(S), len(U)
    colS = np.full(nc, -1, dtype=np.int32); colS[S] = np.arange(nS, dtype=np.int32)
    colU = np.full(nc, -1, dtype=np.int32); colU[U] = np.arange(nU, dtype=np.int32)
    T, dinv, TU = _split_rows(E, rows, colS, colU, p)
    TUc = TU.tocsc()
    t1 = time.time()
    mem_x = float(os.environ.get('S71_MEM_X', mem_x))
    if ublock is None:
        ublock = nU if 4.0 * nS * nU <= mem_x else max(32, int(mem_x / (4.0 * nS)))
    nblocks = (nU + ublock - 1) // ublock if nU else 0
    mask = np.ones(E.shape[0], dtype=bool); mask[rows] = False
    Fo = E[np.nonzero(mask)[0]].tocsr(); Fo.sort_indices()
    indptr = Fo.indptr.astype(np.int64); indices = Fo.indices.astype(np.int32); data = (Fo.data % p).astype(np.uint32)
    info = dict(nS=int(nS), nU=int(nU), excess=int(nU - a_expect), nnzT=int(T.nnz), rows_other=int(Fo.shape[0]),
                order=cov.get('order'), cover_stats=cov.get('stats'), ublock=int(ublock), nblocks=int(nblocks), attempts=[])
    m = nU + extra
    K = None
    for attempt in range(retries):
        ta = time.time(); t_solve = 0.0; t_schur = 0.0
        G = np.zeros((m, nU), dtype=np.uint32)
        pseed = np.uint64((seed + 7919 * attempt + p % 1000) % (1 << 63))
        for b0 in range(0, nU, ublock):
            b1 = min(nU, b0 + ublock); blk = b1 - b0
            ts = time.time()
            Bb = np.ascontiguousarray((TUc[:, b0:b1].toarray().astype(np.int64) % p).astype(np.uint32))   # nS x blk
            trisolve(T, dinv, Bb, p)                                                                     # X block
            t_solve += time.time() - ts; ts = time.time()
            colUb = np.full(nc, -1, dtype=np.int32); colUb[U] = -2; colUb[U[b0:b1]] = np.arange(blk, dtype=np.int32)
            Gb = np.zeros((m, blk), dtype=np.uint32)
            rc = lib().schur_project(Fo.shape[0], _ptr(indptr), _ptr(indices), _ptr(data), _ptr(colS), _ptr(colUb),
                                     _ptr(Bb), blk, m, _ptr(Gb), p, pseed, nproj)
            assert rc == 0, ("schur_project", rc)
            G[:, b0:b1] = Gb
            del Bb, Gb, colUb
            t_schur += time.time() - ts
        t3 = time.time()
        yU = nullspace_mod_p(G.astype(np.int64), p)              # nul x nU
        nul = yU.shape[0]
        del G
        t4 = time.time()
        # lift in blocks of vectors: y_S = -T^{-1} (TU y_U)
        Kc = np.zeros((nc, nul), dtype=np.uint32)
        ok = True
        for v0 in range(0, nul, vblock):
            v1 = min(nul, v0 + vblock)
            yUt = np.ascontiguousarray(yU[v0:v1].T.astype(np.uint32))       # nU x vb
            w = spmm_mod(TU, yUt, p)                                         # nS x vb
            w = np.ascontiguousarray(((p - w.astype(np.int64)) % p).astype(np.uint32))
            yS = trisolve(T, dinv, w, p)
            Kc[S, v0:v1] = yS; Kc[U, v0:v1] = yUt
            if not check_kernel_mat(E, Kc[:, v0:v1].astype(np.int64), p): ok = False
        t5 = time.time()
        rk = rank_tall(Kc, p) if nul else 0
        info['attempts'].append(dict(attempt=attempt, m=int(m), nproj=int(nproj), projected_nullity=int(nul), verified=bool(ok),
                                     rank=int(rk), secs=dict(split=round(t1 - t0, 1), trisolve=round(t_solve, 1), schur=round(t_schur, 1),
                                                             nullspace=round(t4 - t3, 1), lift_verify=round(t5 - t4, 1), rank=round(time.time() - t5, 1))))
        if verbose:
            log(f"    hybrid{tag} p={p} attempt {attempt}: |S|={nS} |U|={nU} (a={a_expect}, excess {nU - a_expect}) m={m} blocks {nblocks}x{ublock} "
                f"projected nullity {nul}, verified={ok}, rank {rk} [split {t1-t0:.1f}s trisolve {t_solve:.1f}s schur {t_schur:.1f}s "
                f"null {t4-t3:.1f}s lift {t5-t4:.1f}s rank {time.time()-t5:.1f}s]")
        if ok and nul == a_expect and rk == a_expect:
            K = Kc; break
        if nul < a_expect:
            raise RuntimeError(("hybrid: projected nullity below a -- impossible if a is right", nul, a_expect))
        del Kc
        m += nU + extra; nproj += 4
    if K is None:
        raise RuntimeError(("hybrid: projection retries exhausted", tag, p, info))
    info['secs'] = round(time.time() - t0, 1)
    return K, info
