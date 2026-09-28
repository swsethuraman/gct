#!/usr/bin/env python3
"""
B28-01c -- independent verifier for the determinant-only hybrid driver, with
R28-01's repair P2.  The regenerating mathematics is B28-01a's frozen verifier
(analysis/b28_01_verify.py, 7978a73a...) unchanged; what changed is what a
certificate must contain before it is accepted:

  * the projection recipe is RECONSTRUCTED from p and U (base seed 20260908,
    attempt 0, pseed = base + 7919 attempt + p mod 1000, m = |U| + 64, 8
    projections); every recorded field must equal it, and the residual is formed
    from the reconstructed recipe, never from the certificate's;
  * FULL_RANK needs a complete a x a minor (a distinct row indices of the point
    set) whose determinant is nonzero mod p and equals the claim;
  * MODULAR_DEFICIENCY (lower bound r = rank VK < a) needs the candidates file:
    count a - r, shape and hash as certified, every vector nonzero, independent
    (rank of the U coordinates), E v = 0 on every row, zero at every saved point
    (regenerated evaluation rows), and equal to K c for the saved combinations;
    each candidate is reported separately;
  * the compiled solve is never rebuilt here (a missing .so is a refusal).

Shares NO code with the producer (the driver and the committed engine it imports:
wk9_s45_build, wk11_s71_hybrid, wk11_s71_schur.c, wk12_s79_cell6, wk8_s30_core).
Declared shared low-level libraries: numpy, scipy.sparse and python-flint
(nmod_mat rank / det over F_p).  Its only compiled code is its own
b28_01c_vfy.c (byte-identical to b28_01_vfy.c; an upper-triangular solve).

From the mathematical inputs (lambda, delta, a, p) it regenerates:
  * the weight-lambda degree-delta monomials in the exponent vectors of
    Sym^4 C^R (own enumeration: memoised feasibility, base-L positional keys);
  * the chi_lambda-isotypic columns (Young subgroup of lambda; chi = product of
    block signs over the blocks with an odd part) and the twisted signs;
  * E, the simple raising operators E_{i,i+1} c_alpha = (alpha_i + 1)
    c_{alpha + e_i - e_{i+1}} as derivations, one row per H-canonical,
    non-obstructed target (H = the stabiliser elements fixing i and i+1);
  * the triangular cover under the five preregistered orders;
  * the projected residual G = P F_o [-T^{-1} R_1[:,U] ; I] with the registered
    projection recipe, formed as the sparse product P F_o followed by
    PF_U - PF_S X (not the producer's per-row accumulation);
  * the determinant coefficients of det(s_1 A_1 + ... + s_R A_R) by Leibniz
    expansion, the chi-coordinate evaluation rows, and V K.
It then checks, trusting no stored rank:
  G1  every cover pivot is nonzero mod p and T is upper triangular   (rank E >= |S|)
  G2  rank_p G = |U| - a                                              (rank E >= n - a)
  K1  E K = 0 mod p on every row of E, K1' rank_p K[U,:] = a          (nullity E >= a)
  M1  rank_p (V K) = a and the complete claimed a x a minor is nonzero (FULL_RANK: mult_det = a over Q)
  D1-D6 the deficiency candidates, as above                           (MODULAR_DEFICIENCY: mult_det >= r only)
plus cross-checks against the producer's hashes (E, cover, G, V K) and the
pencils against their recorded generator.  Output is deterministic; times go
to a separate receipt.

verdict: FULL_RANK (exit 0), MODULAR_DEFICIENCY with lower bound r (exit 8), REJECT (exit 5).
usage: b28_01c_verify.py --lam .. --delta D --a A --prime P --dir DRIVER_OUT --out FILE
                         [--kernel FILE] [--pencils FILE]   (overrides, for corrupted controls)
                         [--fixture-npts N]                 (registered deficiency fixture only: N < a points)
"""
import sys, os, json, time, hashlib, argparse, itertools, random, ctypes
from functools import lru_cache
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_v] = '1'
import numpy as np
from scipy import sparse
from flint import nmod_mat

HERE = os.path.dirname(os.path.abspath(__file__))
NVAR = 4                     # Sym^4: det_4
BUDGET = 250_000_000         # bytes per dense solve block
SEED_ORDER = 20260908
# the registered projection recipe (B27-06 PREREGISTRATION.md item 4; one attempt per prime)
RECIPE_BASE_SEED, RECIPE_ATTEMPT, RECIPE_EXTRA, RECIPE_NPROJ = 20260908, 0, 64, 8


def say(*a):
    print(*a, file=sys.stderr, flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def peak_reset():
    try:
        with open('/proc/self/clear_refs', 'w') as f: f.write('5')
    except OSError:
        pass


def peak():
    with open('/proc/self/status') as f:
        for ln in f:
            if ln.startswith('VmHWM'): return int(ln.split()[1]) * 1024
    return -1


_SO = None
def so():
    global _SO
    if _SO is None:
        path = os.environ.get('B28_VFY_SO', os.path.join(HERE, 'b28_01c_vfy.so'))
        if not os.path.exists(path):
            say(f'REFUSED: {path} missing; the verifier does not compile after the launch hash check'); sys.exit(2)
        _SO = ctypes.CDLL(path)
        vp, i64, u64 = ctypes.c_void_p, ctypes.c_int64, ctypes.c_uint64
        _SO.vfy_upper_solve.argtypes = [i64, i64, vp, vp, vp, vp, vp, u64]
        _SO.vfy_upper_solve.restype = ctypes.c_int
    return _SO


def registered_recipe(p, nU):
    return dict(base_seed=RECIPE_BASE_SEED, attempt=RECIPE_ATTEMPT, extra=RECIPE_EXTRA, nproj=RECIPE_NPROJ,
                pseed=(RECIPE_BASE_SEED + 7919 * RECIPE_ATTEMPT + p % 1000) % (1 << 63), m=nU + RECIPE_EXTRA)


def P(a):
    return a.ctypes.data_as(ctypes.c_void_p)


# ---------------------------------------------------------------- the carrier
def exponent_vectors(R):
    return sorted(t for t in itertools.product(range(NVAR + 1), repeat=R) if sum(t) == NVAR)


def enumerate_monomials(lam, d):
    """sorted d-multisets of exponent-vector indices with total weight lam, in
    lexicographic order, as an (N x d) int32 array."""
    R = len(lam); A = exponent_vectors(R); L = len(A)

    @lru_cache(maxsize=None)
    def ok(rem, i, left):
        if left == 0: return not any(rem)
        return any(all(A[j][c] <= rem[c] for c in range(R)) and ok(tuple(rem[c] - A[j][c] for c in range(R)), j, left - 1)
                   for j in range(i, L))

    @lru_cache(maxsize=None)
    def kids(rem, i, left):
        out = []
        for j in range(i, L):
            if all(A[j][c] <= rem[c] for c in range(R)):
                nr = tuple(rem[c] - A[j][c] for c in range(R))
                if ok(nr, j, left - 1): out.append((j, nr))
        return out

    states = [(tuple(lam), 0)]
    pref = np.zeros((1, 0), dtype=np.int16); sid = np.zeros(1, dtype=np.int64)
    for lev in range(d):
        left = d - lev
        nxt_states = {}; cptr = [0]; cj = []; cs = []
        for (rem, i) in states:
            for j, nr in kids(rem, i, left):
                key = (nr, j)
                if key not in nxt_states: nxt_states[key] = len(nxt_states)
                cj.append(j); cs.append(nxt_states[key])
            cptr.append(len(cj))
        cptr = np.array(cptr, dtype=np.int64); cj = np.array(cj, dtype=np.int16); cs = np.array(cs, dtype=np.int64)
        cnt = cptr[sid + 1] - cptr[sid]
        tot = int(cnt.sum())
        rep = np.repeat(np.arange(len(sid)), cnt)
        start = np.repeat(np.cumsum(cnt) - cnt, cnt)
        flat = cptr[sid[rep]] + (np.arange(tot) - start)
        pref = np.concatenate([pref[rep], cj[flat][:, None]], axis=1)
        sid = cs[flat]
        states = [None] * len(nxt_states)
        for (nr, j), k in nxt_states.items(): states[k] = (nr, j)
        del rep, start, flat, cnt
    for (nr, j) in states: assert not any(nr)
    M = pref.astype(np.int32)
    return M, A


def keys_of(M, L):
    d = M.shape[1]
    assert L ** d < (1 << 63)
    k = np.zeros(M.shape[0], dtype=np.int64)
    for t in range(d):
        k = k * L + M[:, t]
    return k


def young_group(lam):
    """[(g, chi(g))]: g permutes the positions of each block of equal parts;
    chi(g) = product of sign(g|block) over the blocks whose part is odd."""
    R = len(lam); blocks = []
    s = 0
    while s < R:
        e = s
        while e + 1 < R and lam[e + 1] == lam[s]: e += 1
        blocks.append(list(range(s, e + 1))); s = e + 1
    def sgn(perm):
        inv = sum(1 for x in range(len(perm)) for y in range(x + 1, len(perm)) if perm[x] > perm[y])
        return -1 if inv % 2 else 1
    out = []
    for combo in itertools.product(*[list(itertools.permutations(b)) for b in blocks]):
        g = list(range(R)); ch = 1
        for b, img in zip(blocks, combo):
            for x, y in zip(b, img): g[x] = y
            if lam[b[0]] % 2: ch *= sgn([b.index(y) for y in img])
        out.append((tuple(g), ch))
    return out


def act_table(A, g):
    """index table of alpha -> g.alpha with (g.alpha)[g(c)] = alpha[c]."""
    ix = {a: k for k, a in enumerate(A)}
    tab = np.zeros(len(A), dtype=np.int32)
    for k, a in enumerate(A):
        b = [0] * len(a)
        for c in range(len(a)): b[g[c]] = a[c]
        tab[k] = ix[tuple(b)]
    return tab


def image_index(M, tab, skeys, L):
    im = np.sort(tab[M], axis=1)
    k = keys_of(im, L); del im
    pos = np.searchsorted(skeys, k)
    assert pos.max(initial=0) < len(skeys) and np.array_equal(skeys[pos], k), 'image outside the weight space'
    return pos


def carrier(lam, d):
    M, A = enumerate_monomials(lam, d)
    L = len(A)
    kk = keys_of(M, L)
    o = np.argsort(kk, kind='stable'); M = M[o]; kk = kk[o]
    assert np.all(np.diff(kk) > 0)
    N = M.shape[0]
    grp = young_group(lam)
    imgs = [(image_index(M, act_table(A, g), kk, L), ch) for g, ch in grp]
    rep = np.arange(N, dtype=np.int64)
    for im, _ in imgs: rep = np.minimum(rep, im)
    acc = np.zeros(N, dtype=np.int64)
    for im, ch in imgs: acc += ch * (im[rep] == np.arange(N))
    isrep = rep == np.arange(N)
    kept_rep = isrep & (acc != 0)
    colnum = np.full(N, -1, dtype=np.int64); colnum[kept_rep] = np.arange(int(kept_rep.sum()))
    col = colnum[rep]
    orbit = np.bincount(rep, minlength=N)
    assert np.all(np.abs(acc[col >= 0]) * orbit[rep[col >= 0]] == len(grp))
    assert not np.any(acc[col < 0])
    sgn = np.where(acc > 0, 1, -1).astype(np.int64); sgn[col < 0] = 0
    return dict(M=M, A=A, L=L, keys=kk, col=col, sgn=sgn, n=int(kept_rep.sum()), N_S=N, grp=grp)


def raising_matrix(lam, C):
    M, A, L, col, sgn, grp = C['M'], C['A'], C['L'], C['col'], C['sgn'], C['grp']
    R = len(lam); Aa = np.array(A, dtype=np.int64); ix = {a: k for k, a in enumerate(A)}
    blocks = []
    live = col >= 0
    for i in range(R - 1):
        j = i + 1
        sh = np.full(L, -1, dtype=np.int64)
        for k, a in enumerate(A):
            if a[j] > 0:
                b = list(a); b[j] -= 1; b[i] += 1; sh[k] = ix[tuple(b)]
        tk, tc, tv = [], [], []
        for t in range(M.shape[1]):
            s = sh[M[:, t]]
            sel = live & (s >= 0)
            Mt = M[sel].copy(); Mt[:, t] = s[sel]; Mt.sort(axis=1)
            tk.append(keys_of(Mt, L)); del Mt
            tc.append(col[sel]); tv.append(sgn[sel] * (Aa[M[sel, t], i] + 1))
        tk = np.concatenate(tk); tc = np.concatenate(tc); tv = np.concatenate(tv)
        ut, inv = np.unique(tk, return_inverse=True); del tk
        # decode targets, test H-canonicity and chi-obstruction
        Tm = np.zeros((len(ut), M.shape[1]), dtype=np.int32); r = ut.copy()
        for t in range(M.shape[1] - 1, -1, -1):
            Tm[:, t] = r % L; r //= L
        Hs = [(g, ch) for g, ch in grp if g[i] == i and g[j] == j]
        canon = np.ones(len(ut), dtype=bool); obst = np.zeros(len(ut), dtype=bool)
        for g, ch in Hs:
            kg = keys_of(np.sort(act_table(A, g)[Tm], axis=1), L)
            canon &= ut <= kg
            if ch == -1: obst |= kg == ut
        del Tm
        # obstructed targets must cancel
        ob = obst[inv]
        if ob.any():
            X = sparse.coo_matrix((tv[ob], (inv[ob], tc[ob])), shape=(len(ut), C['n'])).tocsr(); X.sum_duplicates(); X.eliminate_zeros()
            assert X.nnz == 0, 'chi-obstructed target rows do not cancel'
        keep = canon & ~obst
        rid = np.full(len(ut), -1, dtype=np.int64); rid[keep] = np.arange(int(keep.sum()))
        rr = rid[inv]; s = rr >= 0
        Ei = sparse.coo_matrix((tv[s], (rr[s], tc[s])), shape=(int(keep.sum()), C['n']), dtype=np.int64).tocsr()
        Ei.sum_duplicates(); Ei.eliminate_zeros()
        Ei = Ei[np.nonzero(np.diff(Ei.indptr) > 0)[0]]
        blocks.append(Ei)
        del tc, tv, inv, rr, s
    E = sparse.vstack(blocks).tocsr(); E.sort_indices()
    return E


def csr_sha(E):
    h = hashlib.sha256()
    for arr in (E.indptr.astype('<i8'), E.indices.astype('<i8'), E.data.astype('<i8')):
        h.update(np.ascontiguousarray(arr).tobytes())
    h.update(json.dumps(list(E.shape)).encode())
    return h.hexdigest()


# ---------------------------------------------------------------- the cover
def orders(E, n):
    fill = np.bincount(E.indices, minlength=n)
    def pos_of(perm):
        pos = np.empty(n, dtype=np.int64); pos[perm] = np.arange(n); return pos
    return [('natural', np.arange(n, dtype=np.int64)), ('reversed', n - 1 - np.arange(n, dtype=np.int64)),
            ('fill_asc', pos_of(np.argsort(fill, kind='stable'))), ('fill_desc', pos_of(np.argsort(-fill, kind='stable'))),
            ('random', pos_of(np.random.default_rng(SEED_ORDER).permutation(n)))]


def cover_of(E, n, pos):
    lens = np.diff(E.indptr); rows = np.nonzero(lens > 0)[0]
    lead = np.minimum.reduceat(pos[E.indices], E.indptr[rows])
    o = np.lexsort((rows, lens[rows], lead))
    lo = lead[o]; first = np.ones(len(o), dtype=bool); first[1:] = lo[1:] != lo[:-1]
    chosen = rows[o][first]; Spos = lo[first]
    inv = np.empty(n, dtype=np.int64); inv[pos] = np.arange(n)
    S = inv[Spos]
    cov = np.zeros(n, dtype=bool); cov[S] = True
    U = np.nonzero(~cov)[0]; U = U[np.argsort(pos[U], kind='stable')]
    return chosen, S, U


# ---------------------------------------------------------------- residual
def splitmix_projection(nrows, m, pseed, nproj):
    """the recorded projection: row r of F_o is added with sign +-1 into rows
    t_q (q < nproj) of G, from z = pseed ^ (0xD1B54A32D192ED03 (r+1)) and the
    splitmix64 finaliser; sign = bit 40 (1 -> +, 0 -> -)."""
    with np.errstate(over='ignore'):
        r = np.arange(nrows, dtype=np.uint64)
        z = np.uint64(pseed) ^ (np.uint64(0xD1B54A32D192ED03) * (r + np.uint64(1)))
        T, C, V = [], [], []
        for _ in range(nproj):
            z = z + np.uint64(0x9E3779B97F4A7C15)
            x = z.copy()
            x = (x ^ (x >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
            x = (x ^ (x >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
            x = x ^ (x >> np.uint64(31))
            T.append((x % np.uint64(m)).astype(np.int64)); C.append(np.arange(nrows, dtype=np.int64))
            V.append(np.where(((x >> np.uint64(40)) & np.uint64(1)) == 1, 1, -1).astype(np.int64))
    Pm = sparse.coo_matrix((np.concatenate(V), (np.concatenate(T), np.concatenate(C))), shape=(m, nrows), dtype=np.int64).tocsr()
    Pm.sum_duplicates()
    return Pm


def residual(E, n, rows, S, U, p, proj):
    nS, nU = len(S), len(U)
    posS = np.full(n, -1, dtype=np.int64); posS[S] = np.arange(nS)
    R1 = E[rows]
    T = R1[:, S].tocsr(); T.sort_indices()
    TU = R1[:, U].tocsc()
    Tc = T.tocoo()
    lower = Tc.col < Tc.row
    upper_ok = not np.any(Tc.data[lower] % p)
    diag = np.asarray(T.diagonal(), dtype=np.int64) % p
    pivots_ok = bool(np.all(diag != 0))
    covered_cols_ok = bool(np.array_equal(np.sort(np.concatenate([S, U])), np.arange(n)))
    res = dict(T_upper_triangular=bool(upper_ok), cover_pivots_nonzero=pivots_ok, S_U_partition=covered_cols_ok)
    if not (upper_ok and pivots_ok and covered_cols_ok):
        return None, res
    up = sparse.triu(T, k=1).tocsr(); up.sort_indices()
    up_ptr = up.indptr.astype(np.int64); up_idx = up.indices.astype(np.int64); up_val = (up.data % p).astype(np.uint64)
    dinv = np.array([pow(int(x), -1, p) for x in diag], dtype=np.uint64)
    mask = np.ones(E.shape[0], dtype=bool); mask[rows] = False
    Fo = E[np.nonzero(mask)[0]]
    Pm = splitmix_projection(Fo.shape[0], proj['m'], proj['pseed'], proj['nproj'])
    PF = (Pm @ Fo).tocsc()
    PFS = PF[:, S].tocsr(); PFU = PF[:, U].tocsr()
    del PF
    rs = np.asarray(abs(PFS).sum(axis=1)).ravel()
    bound = int(rs.max() if rs.size else 0) * (p - 1) + int(abs(PFU).max() if PFU.nnz else 0)
    assert bound < (1 << 63), ('int64 bound for PF_S X fails', bound)
    m = proj['m']
    G = np.zeros((m, nU), dtype=np.int64)
    w = max(1, BUDGET // (8 * max(nS, 1)))
    for b0 in range(0, nU, w):
        b1 = min(nU, b0 + w)
        Y = np.ascontiguousarray(TU[:, b0:b1].toarray() % p).astype(np.uint64)
        rc = so().vfy_upper_solve(nS, b1 - b0, P(up_ptr), P(up_idx), P(up_val), P(dinv), P(Y), p)
        assert rc == 0, ('vfy_upper_solve', rc)
        G[:, b0:b1] = (PFU[:, b0:b1].toarray() - PFS @ Y.astype(np.int64)) % p
        del Y
    res.update(PF_bound_log2=round(float(np.log2(max(bound, 1))), 3), solve_block=int(w))
    return G, res


# ---------------------------------------------------------------- evaluation
def det_coefficients(pencil, A):
    """coefficients of s^alpha in det(sum_i s_i A_i), 4 x 4, Leibniz expansion."""
    R = len(pencil)
    tot = {}
    for perm in itertools.permutations(range(4)):
        sg = -1 if sum(1 for x in range(4) for y in range(x + 1, 4) if perm[x] > perm[y]) % 2 else 1
        poly = {(0,) * R: sg}
        for r in range(4):
            lin = [pencil[i][r][perm[r]] for i in range(R)]
            nxt = {}
            for e, c in poly.items():
                for i in range(R):
                    if lin[i]:
                        f = list(e); f[i] += 1; f = tuple(f)
                        nxt[f] = nxt.get(f, 0) + c * lin[i]
            poly = nxt
        for e, c in poly.items(): tot[e] = tot.get(e, 0) + c
    return [tot.get(a, 0) for a in A]


def eval_rows(C, coeff_lists, p):
    M, col, sgn, n = C['M'], C['col'], C['sgn'], C['n']
    live = np.nonzero(col >= 0)[0]
    Ml = M[live]; cl = col[live]; sl = sgn[live] % p
    out = np.zeros((len(coeff_lists), n), dtype=np.int64)
    for r, co in enumerate(coeff_lists):
        cv = np.array([c % p for c in co], dtype=np.int64)
        t = cv[Ml[:, 0]].copy()
        for k in range(1, Ml.shape[1]):
            t = (t * cv[Ml[:, k]]) % p
        t = (t * sl) % p
        np.add.at(out[r], cl, t)
    return out % p


def times_mod(V, K, p, chunk=1 << 15):
    """(V K) mod p, V (r x n), K (n x a), entries in [0, p): 16-bit limbs of V,
    inner dimension in chunks of 2^15, every int64 partial sum < 2^62."""
    assert p < (1 << 31)
    out = np.zeros((V.shape[0], K.shape[1]), dtype=np.int64)
    for c0 in range(0, V.shape[1], chunk):
        Kc = np.asarray(K[c0:c0 + chunk], dtype=np.int64)
        Vc = V[:, c0:c0 + chunk]
        lo = (Vc & 0xFFFF) @ Kc; hi = (Vc >> 16) @ Kc
        out = (out + lo % p + (hi % p) * 65536) % p
    return out


def fl_rank(X, p):
    X = np.asarray(X, dtype=np.int64) % p
    if X.size == 0: return 0
    return nmod_mat(X.shape[0], X.shape[1], X.ravel().tolist(), p).rank()


def EX_zero(E, X, p):
    """E X == 0 mod p on every row, X (n x c) with entries in [0, p): 16-column chunks, 16-bit limbs."""
    for c0 in range(0, X.shape[1], 16):
        Xc = np.asarray(X[:, c0:c0 + 16], dtype=np.int64)
        r = ((E @ (Xc & 0xFFFF)) % p + ((E @ (Xc >> 16)) % p) * 65536) % p
        if np.any(r): return False
    return True


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=int, nargs='+', required=True)
    ap.add_argument('--delta', type=int, required=True)
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--prime', type=int, required=True)
    ap.add_argument('--dir', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--kernel', default='')
    ap.add_argument('--pencils', default='')
    ap.add_argument('--fixture-npts', type=int, default=None)
    args = ap.parse_args()
    lam = tuple(args.lam); d = args.delta; a = args.a; p = args.prime
    if args.fixture_npts is not None: assert 0 < args.fixture_npts < a, 'a fixture point count must be below a'
    tag = '_'.join(map(str, lam)) + f'_d{d}'
    cell = json.load(open(os.path.join(args.dir, f'{tag}_cell.json')))
    cert = json.load(open(os.path.join(args.dir, f'{tag}_p{p}_cert.json')))
    ph = []; t0 = time.perf_counter()
    def start(): peak_reset(); return time.perf_counter()
    def stop(name, t): ph.append(dict(phase=name, secs=round(time.perf_counter() - t, 3), peak_rss_bytes=peak())); say('  [verify]', ph[-1])
    chk = {}; val = {}; cand_report = None

    t = start()
    C = carrier(lam, d)
    E = raising_matrix(lam, C)
    n = C['n']
    stop('build', t)
    val.update(N_S=C['N_S'], n_chi=n, rows_E=int(E.shape[0]), nnz_E=int(E.nnz), E_sha256=csr_sha(E))
    chk['n_chi_matches_frozen'] = n == cell['n_chi'] == cert['n_chi']
    chk['E_matches_producer'] = val['E_sha256'] == cell['E_sha256']
    assert int(np.abs(E.data).max()) < (1 << 16)

    t = start()
    best = None; stats = {}
    for name, pos in orders(E, n):
        rows, S, U = cover_of(E, n, pos)
        stats[name] = int(len(S))
        if best is None or len(S) > len(best[1]): best = (rows, S, U, name)
    rows, S, U, oname = best
    stop('cover', t)
    val.update(cover_order=oname, cover_stats=stats, cover_size=int(len(S)), nU=int(len(U)))
    chk['cover_matches_producer'] = (oname == cell['cover']['order'] and stats == cell['cover']['stats']
                                     and sha(np.asarray(S, dtype='<i8').tobytes()) == cell['cover']['S_sha256']
                                     and sha(np.asarray(U, dtype='<i8').tobytes()) == cell['cover']['U_sha256'])

    t = start()
    proj = registered_recipe(p, len(U))                      # P2: reconstructed, never read from the certificate
    hyb = cert.get('hybrid', {})
    recorded = {k: v for k, v in hyb.get('projection', {}).items() if k != 'generator'}
    chk['projection_recipe_registered'] = bool(recorded == proj and hyb.get('G_shape') == [proj['m'], len(U)])
    val['projection_recipe'] = proj
    G, rres = residual(E, n, rows, S, U, p, proj)
    chk['G1_cover_pivots'] = bool(rres['T_upper_triangular'] and rres['cover_pivots_nonzero'] and rres['S_U_partition'])
    if G is not None:
        val['G_sha256'] = sha(G.astype('<u4').tobytes())
        chk['G_matches_producer'] = val['G_sha256'] == hyb.get('G_sha256')
        rG = fl_rank(G, p); val['rank_G'] = int(rG)
        chk['G2_residual_rank'] = rG == len(U) - a
        del G
    else:
        chk['G_matches_producer'] = False; chk['G2_residual_rank'] = False
    val['residual'] = rres
    stop('schur', t)

    t = start()
    kf = args.kernel or os.path.join(args.dir, cert['K']['file'])
    K = np.fromfile(kf, dtype='<u4').reshape(n, a) if os.path.getsize(kf) == 4 * n * a else None
    chk['K_file_matches_cert'] = K is not None and sha(K.tobytes()) == cert['K']['sha256']
    if K is not None:
        chk['K1_EK_zero_all_rows'] = EX_zero(E, K, p)
        rKU = fl_rank(K[U], p); val['rank_K_U'] = int(rKU)
        chk['K1b_rank_K'] = rKU == a
    else:
        chk['K1_EK_zero_all_rows'] = False; chk['K1b_rank_K'] = False
    stop('lift_check', t)

    # the deficiency candidates, when the certificate claims a deficiency (P2)
    ev = cert.get('evaluation', {})
    claim = ev.get('mult_det')
    cd = cert.get('candidates') or {}
    Cv = None; Cb = None
    if isinstance(claim, int) and 0 <= claim < a:
        cnt = a - claim
        try:
            cpath = os.path.join(args.dir, cd['file']); bpath = os.path.join(args.dir, cd['combinations']['file'])
            if os.path.getsize(cpath) == 4 * cnt * n and cd.get('shape') == [cnt, n]:
                Cv = np.fromfile(cpath, dtype='<u4').reshape(cnt, n)
            if os.path.getsize(bpath) == 4 * cnt * a and cd['combinations'].get('shape') == [cnt, a]:
                Cb = np.fromfile(bpath, dtype='<u4').reshape(cnt, a)
        except (KeyError, TypeError, OSError):
            pass

    t = start()
    pf = args.pencils or os.path.join(args.dir, f'{tag}_pencils.json')
    pj = json.load(open(pf))
    pts = pj['pencils']; R = len(lam)
    rnd = random.Random(pj['seed'])
    regen = [[[[rnd.randint(-pj['bound'], pj['bound']) for _ in range(4)] for _ in range(4)] for _ in range(R)] for _ in range(a + 8)]
    chk['pencils_match_generator'] = (pts == regen and pj['bound'] == 40 and pj['seed'] == 11 and len(pts) == a + 8)
    if args.fixture_npts is not None:
        pts = pts[:args.fixture_npts]
    npts = len(pts)
    chk['point_count_registered'] = ev.get('npts') == npts
    kind = None
    if K is not None:
        X = K if Cv is None else np.hstack([K, np.ascontiguousarray(Cv.T)])     # V K and V C^T from the same rows
        parts = []
        for c0 in range(0, npts, 8):
            V = eval_rows(C, [det_coefficients(pc, C['A']) for pc in pts[c0:c0 + 8]], p)
            parts.append(times_mod(V, X, p)); del V
        VX = np.vstack(parts) % p
        VK = np.ascontiguousarray(VX[:, :a]); VC = VX[:, a:]
        val['VK_sha256'] = sha(VK.astype('<u4').tobytes())
        chk['VK_matches_producer'] = val['VK_sha256'] == ev.get('VK_sha256')
        mult = fl_rank(VK, p); val['mult_det_mod_p'] = int(mult)
        chk['mult_det_matches_claim'] = mult == claim
        if mult == a:
            kind = 'FULL_RANK'
            mr = ev.get('minor_rows')
            complete = (isinstance(mr, list) and len(mr) == a and len(set(mr)) == a
                        and all(isinstance(x, int) and 0 <= x < npts for x in mr) and isinstance(ev.get('minor_det_mod_p'), int))
            dm = int(nmod_mat(a, a, VK[mr].astype(np.int64).ravel().tolist(), p).det()) if complete else 0
            val['minor_det_mod_p'] = dm
            chk['M1_claimed_minor_nonzero'] = bool(complete and dm != 0 and dm == ev['minor_det_mod_p'])
            chk['outcome_label_matches'] = cert.get('outcome') == 'FULL_RANK'
        else:
            kind = 'MODULAR_DEFICIENCY'
            cnt = a - mult
            chk['outcome_label_matches'] = cert.get('outcome') == 'MODULAR_DEFICIENCY' and cert.get('mult_det_lower_bound') == mult
            chk['D1_candidates_file'] = bool(Cv is not None and Cb is not None and Cv.shape[0] == cnt
                                             and sha(Cv.astype('<u4').tobytes()) == cd.get('sha256')
                                             and sha(Cb.astype('<u4').tobytes()) == (cd.get('combinations') or {}).get('sha256'))
            if Cv is not None and Cv.shape[0] == cnt:
                KCb = None
                if Cb is not None:                            # K c for every saved combination, exact 16-bit limbs
                    Cbt = np.asarray(Cb.T, dtype=np.int64); K64 = K.astype(np.int64)
                    KCb = (((K64 & 0xFFFF) @ Cbt) % p + (((K64 >> 16) @ Cbt) % p) * 65536) % p
                    del K64
                per = []
                for i in range(cnt):
                    v = np.ascontiguousarray(Cv[i:i + 1].T)
                    c = dict(index=i, nonzero=bool(np.any(v)), E_equations_all_rows=bool(EX_zero(E, v, p)),
                             zero_at_every_saved_point=bool(not np.any(VC[:, i])),
                             equals_K_times_combination=bool(KCb is not None and np.array_equal(KCb[:, i], Cv[i].astype(np.int64))))
                    c['valid'] = all(c[k] for k in ('nonzero', 'E_equations_all_rows', 'zero_at_every_saved_point', 'equals_K_times_combination'))
                    per.append(c)
                rC = fl_rank(Cv[:, U], p); val['rank_candidates_U'] = int(rC)
                chk['D2_nonzero'] = all(c['nonzero'] for c in per)
                chk['D3_independent'] = rC == cnt
                chk['D4_E_equations'] = all(c['E_equations_all_rows'] for c in per)
                chk['D5_zero_at_saved_points'] = all(c['zero_at_every_saved_point'] for c in per)
                chk['D6_combinations'] = all(c['equals_K_times_combination'] for c in per)
                cand_report = per
            else:
                for k in ('D2_nonzero', 'D3_independent', 'D4_E_equations', 'D5_zero_at_saved_points', 'D6_combinations'): chk[k] = False
    stop('evaluation', t)

    verdict = kind if (kind is not None and all(chk.values())) else 'REJECT'
    out = dict(schema='b28-01c-verify/1', tag=tag, prime=p, a=a, verdict=verdict, checks=chk, values=val,
               inputs=dict(kernel_file_sha256=(sha(open(kf, 'rb').read()) if os.path.exists(kf) else None),
                           pencils_file_sha256=sha(open(pf, 'rb').read()), npts=npts))
    if args.fixture_npts is not None: out['fixture_npts'] = args.fixture_npts
    if verdict == 'MODULAR_DEFICIENCY':
        out['mult_det_lower_bound'] = int(val['mult_det_mod_p'])
        out['meaning'] = 'modular, finite-sample lower bound mult_det >= r; the candidates are unproved; no characteristic-zero statement'
    if cand_report is not None: out['candidates'] = cand_report
    with open(args.out, 'w') as f: json.dump(out, f, indent=1, sort_keys=True)
    with open(args.out.replace('.json', '') + '_receipt.json', 'w') as f:
        json.dump(dict(schema='b28-01c-verify-receipt/1', tag=tag, prime=p, phases=ph, total_secs=round(time.perf_counter() - t0, 3)), f, indent=1)
    say(f"  VERIFY {tag} p={p}: {verdict} {chk}")
    sys.exit({'FULL_RANK': 0, 'MODULAR_DEFICIENCY': 8}.get(verdict, 5))


if __name__ == '__main__':
    main()
