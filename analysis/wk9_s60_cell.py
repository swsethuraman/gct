#!/usr/bin/env python3
"""
Session 60 -- one length-5 cell, both sides, by the route its size dictates.

    mult_det = a - nullity_Q [E; ev_det]          (Lemma 1, docs/sparse_det_route.md)
    mult_red = a - nullity_Q  E_red                (Theorem 1 (star), docs/reducible_ideal.md:
                                                    HWV ∩ I(R_5) = ker E ∩ span M_red)
             = a - nullity_Q [E; ev_red]           (the brief's instrument: l.c points)

with E the stacked simple raising operators on the chi_lam-isotypic reduction
V_chi (analysis/wk9_s45_build.py, unchanged, at r = 5), ev_det the evaluation
rows at K = a + 8 random det_4 pencils, ev_red the same at K random reducible
points l(s).c(s), and E_red the columns of E whose monomials have, for every
variable i, a factor c_alpha with alpha_i = 0.  Since rank_p <= rank_Q, a zero
nullity modulo ONE prime proves the corresponding mult = a over Q; both house
primes are run at every cell (concurrently, on the two cores).

Routes, chosen by n_chi (PREREG_s60.md sec. 1):
  dense  (n_chi <= dense_cap): the exact highest-weight kernel by python-flint
         (nullspace of E when n_chi <= 2500, else of the certified random
         compression Agg = P.E with n_chi + 64 rows, s41 semantics), a asserted
         equal to the plethysm value, every kernel vector checked against the
         full sparse E; then mult_det / mult_red(star) / mult_red(points) as
         ranks of small matrices; gct-cert/1 full_rank certificates written.
  sparse (n_chi >  dense_cap): the session-42/45 Wiedemann certificates
         (wk9_s45_cell.nullity_stacked, unchanged) on [E; ev_det], on E_red and,
         when --red-points, on [E; ev_red].

usage: python3 analysis/wk9_s60_cell.py delta lam1 ... lam5 [--route auto|dense|sparse]
          [--dense-cap 4000] [--red-points always|dense|never] [--certs DIR] [--out FILE]
          [--seed-det 11] [--seed-red 29] [--bound 40] [--npts K] [--levels cheap|s42|full]
prints one JSON line (RESULT ...) and appends it to --out.
"""
import sys, os, time, json, gzip, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('WIED_BIN', '/home/claude/wied60')
os.environ.setdefault('WIED_WORK', '/home/claude/s60/work')
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import exps, restrict, det_form, P1, P2
from wk9_s45_build import build_cell, ev_rows_arr, log, _rss_gb, _grouping
from wk9_s45_cell import nullity_stacked, LEVELS, check_kernel_full
from wk9_s42_sparse import check_kernel_py
from wk9_s42_census import a_weyl

N = 4
R = 5
PRIMES = (P1, P2)
RED_PTS_CAP = 12000     # sparse-route cells above this n_chi get the reducible side by (star) only
DET4, N_DET = det_form(4)
CONVENTIONS = {"coefficient": "c_alpha(F) = coefficient of s^alpha in F",
               "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}"}
EXPS3 = None


# ------------------------------------------------------------------ points
def det_pencils(K, seed, bound):
    """K random det_4 pencils as lists of 5 integer 4x4 matrices (rows)."""
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        out.append([[[rnd.randint(-bound, bound) for _ in range(4)] for _ in range(4)] for _ in range(R)])
    return out


def det_coeffs(pencil):
    """coefficient dict of det_4(sum_i s_i A_i); A_i = pencil[i] (4x4 rows)."""
    As = [[pencil[i][a][b] for a in range(4) for b in range(4)] for i in range(R)]
    return restrict(DET4, N_DET, N, R, As)


def reducible_points(K, seed, bound):
    """K random reducible points (l, cubic) with l a length-5 integer vector
    and cubic a dict {alpha (|alpha| = 3): coeff}, entries in [-bound, bound]."""
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        lin = [rnd.randint(-bound, bound) for _ in range(R)]
        cub = {al: rnd.randint(-bound, bound) for al in exps(3, R)}
        out.append((lin, cub))
    return out


def red_coeffs(pt):
    lin, cub = pt
    out = {}
    for a3, cc in cub.items():
        if cc == 0: continue
        for i in range(R):
            if lin[i] == 0: continue
            a4 = list(a3); a4[i] += 1; k = tuple(a4)
            out[k] = out.get(k, 0) + lin[i] * cc
    return {k: v for k, v in out.items() if v}


def point_record(kind, pt):
    if kind == 'det_pencil':
        return {"type": "det_pencil", "pencil": pt}
    lin, cub = pt
    return {"type": "reducible", "l": list(lin),
            "cubic": [[list(al), int(c)] for al, c in sorted(cub.items()) if c]}


# --------------------------------------------------------- evaluation rows
def ev_rows_from_coeffs(arr, coeff_dicts, prime, chunk=2_000_000):
    """chi-coordinate evaluation rows from explicit coefficient dicts (the
    numpy kernel of wk9_s45_build.ev_rows_arr, with the point already expanded)."""
    A = exps(N, R); L = len(A)
    M = arr['M']; sgn = arr['sgn']; n_chi = arr['n_chi']
    mem, starts = _grouping(arr)
    out = []
    for co in coeff_dicts:
        cv = np.zeros(L, dtype=np.int64)
        for a, al in enumerate(A):
            cv[a] = co.get(al, 0) % prime
        row = np.zeros(n_chi, dtype=np.int64)
        for b0 in range(0, len(mem), chunk):
            mm = mem[b0:b0 + chunk]
            term = cv[M[mm, 0]].copy()
            for k in range(1, M.shape[1]):
                term *= cv[M[mm, k]]
                term %= prime
            term *= sgn[mm]
            term %= prime
            s0 = np.searchsorted(starts, b0, side='right') - 1
            s1 = np.searchsorted(starts, b0 + len(mm), side='left')
            loc = np.maximum(starts[s0:s1] - b0, 0)
            np.add.at(row, np.arange(s0, s1), np.add.reduceat(term, loc) % prime)
            del term, mm, loc
        out.append((row % prime).astype(np.int64))
    return np.array(out, dtype=np.int64).reshape(len(coeff_dicts), n_chi)


# ------------------------------------------------------------ (star) columns
def red_mask(arr, chunk=500_000):
    """boolean over chi-columns: True iff the column's monomials have, for
    every i in [5], a factor c_alpha with alpha_i = 0 (Theorem (star)); the
    condition is Stab-invariant so it is constant on every orbit (asserted)."""
    A = np.array(exps(N, R), dtype=np.int8)          # L x 5
    M = arr['M']; col_of = arr['col_of']; n_chi = arr['n_chi']
    Nn = M.shape[0]
    cnt_red = np.zeros(n_chi, dtype=np.int64); cnt_all = np.zeros(n_chi, dtype=np.int64)
    for b0 in range(0, Nn, chunk):
        b1 = min(b0 + chunk, Nn)
        Z = (A[M[b0:b1]] == 0)                        # (b x delta x 5)
        red = Z.any(axis=1).all(axis=1)               # (b,)
        c = col_of[b0:b1]; ok = c >= 0
        cnt_all += np.bincount(c[ok], minlength=n_chi)
        cnt_red += np.bincount(c[ok & red], minlength=n_chi)
        del Z, red
    assert np.all((cnt_red == 0) | (cnt_red == cnt_all)), "red condition not constant on an orbit"
    return cnt_red > 0


# ------------------------------------------------------------- dense kernel
def _split_matmul_mod(Amat, Bmat, p):
    """(A @ B) mod p for int64 arrays with entries in [0, p), p < 2^31, and
    inner dimension < 2^16 (16-bit limb split keeps every partial sum < 2^63)."""
    assert Amat.shape[1] < 65536
    Blo = Bmat & 0xFFFF; Bhi = Bmat >> 16
    t0 = (Amat @ Blo) % p
    t1 = (Amat @ Bhi) % p
    return (t0 + t1 * 65536) % p


def rank_mod_p(Mat, p):
    Mat = np.asarray(Mat, dtype=np.int64) % p
    if Mat.size == 0: return 0
    return nmod_mat(Mat.shape[0], Mat.shape[1], Mat.ravel().tolist(), p).rank()


def kernel_dense(E, nc, p, a_expect, margin=64, chunk=64, seed=101, exact_cap=2500):
    """the highest-weight kernel mod p as an (a x nc) int64 array, s41 semantics:
    exact nullspace of E below exact_cap, else of Agg = P.E (nc + margin random
    rows); rank(Agg) <= rank_p(E) <= rank_Q(E) = nc - a so nullity(Agg) = a
    forces ker(Agg) = ker_p(E); every vector is then checked against the full
    sparse E."""
    t0 = time.time()
    nrows = E.shape[0]
    Em = E.tocsr(); Em.sort_indices()
    if nc <= exact_cap and nrows * nc <= 6_000_000:
        D = np.zeros((nrows, nc), dtype=np.int64)
        coo = Em.tocoo()
        D[coo.row, coo.col] = coo.data % p
        Mf = nmod_mat(nrows, nc, D.ravel().tolist(), p); del D
        route = 'exact'
    else:
        rs = nc + margin
        ET = Em.T.tocsr()
        maxabs = int(np.abs(ET.data).max()); colfill = int(np.diff(ET.indptr).max())
        assert maxabs * (p - 1) * colfill < (1 << 62), ("int64 bound", maxabs, colfill)
        rng = np.random.default_rng(seed * 1000003 + p % 1000003 + nc)
        Mf = nmod_mat(rs, nc, p)
        for k0 in range(0, rs, chunk):
            cs = min(chunk, rs - k0)
            Pc = rng.integers(0, p, (nrows, cs), dtype=np.int64)
            C = np.ascontiguousarray(((ET @ Pc) % p).T)      # cs x nc
            del Pc
            for k in range(cs):                               # per-entry assignment: no list of rs*nc ints
                row = C[k].tolist(); i = k0 + k
                for j, v in enumerate(row):
                    if v: Mf[i, j] = v
            del C
        route = 'compressed'
    X, nul = Mf.nullspace()
    kern = np.array([[int(X[i, j]) for i in range(nc)] for j in range(nul)], dtype=np.int64).reshape(nul, nc)
    del Mf, X
    assert nul == a_expect, ("dense kernel: nullity != a (plethysm)", nul, a_expect, route)
    chk = check_kernel_py if int(np.abs(Em.data).max(initial=0)) < 65536 else check_kernel_full
    for v in kern:
        assert chk(Em, nc, p, v.tolist()), "dense kernel vector fails E v = 0 on the full sparse E"
    log(f"    dense kernel [{route}] p={p}: nullity {nul} = a, rank {nc - nul}, "
        f"all vectors verified on the full E ({time.time()-t0:.0f}s, HWM {_rss_gb():.2f} GB)")
    return kern, route


# ---------------------------------------------------------- certificates
def expand_vector(arr, vec, p):
    """chi-coordinate vector (length n_chi, mod p) -> canonical term list
    [[alpha_1..alpha_delta], coeff] over the monomial basis, coeff in [1, p-1]."""
    A = exps(N, R)
    M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']
    vec = np.asarray(vec, dtype=np.int64) % p
    sel = np.nonzero(col_of >= 0)[0]
    vals = (vec[col_of[sel]] * sgn[sel]) % p
    nz = vals != 0
    terms = []
    for m, c in zip(sel[nz].tolist(), vals[nz].tolist()):
        terms.append([[list(A[k]) for k in M[m].tolist()], int(c)])
    return {"terms": terms}


def nullspace_mod_p(Mat, p):
    """basis of {c : Mat c = 0} mod p as a list of int64 arrays (Mat is m x n)."""
    Mat = np.asarray(Mat, dtype=np.int64) % p
    m, n = Mat.shape
    if m == 0:
        return [np.eye(n, dtype=np.int64)[j] for j in range(n)]
    X, nul = nmod_mat(m, n, Mat.ravel().tolist(), p).nullspace()
    return [np.array([int(X[i, j]) for i in range(n)], dtype=np.int64) for j in range(nul)]


def write_hwv_cert(path, lam, delta, a, p, vectors_terms, claims, title, notes=None):
    cert = {"format": "gct-cert/1", "kind": "hwv", "title": title,
            "produced_by": "analysis/wk9_s60_cell.py (session 60)",
            "cell": {"n": N, "r": R, "lambda": [int(x) for x in lam], "delta": int(delta), "a": int(a)},
            "conventions": dict(CONVENTIONS), "modulus": int(p),
            "vectors": vectors_terms, "claims": claims}
    if notes: cert["notes"] = notes
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        json.dump(cert, f, separators=(',', ':'))
    return os.path.getsize(path)


def write_full_rank_cert(path, lam, delta, a, p, variety, point_recs, basis_terms, title, notes=None):
    cert = {"format": "gct-cert/1", "kind": "full_rank", "title": title,
            "produced_by": "analysis/wk9_s60_cell.py (session 60)",
            "cell": {"n": N, "r": R, "lambda": [int(x) for x in lam], "delta": int(delta), "a": int(a)},
            "conventions": dict(CONVENTIONS), "prime": int(p), "variety": variety,
            "points": point_recs, "basis": basis_terms}
    if notes: cert["notes"] = notes
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        json.dump(cert, f, separators=(',', ':'))
    return os.path.getsize(path)


# ------------------------------------------------------------------ the cell
_SHARED = {}


def nullity_floor(E, EV, nc, p, k0=0, want_kern=True, seed0=1, tag='cell', levels=LEVELS['cheap'],
                  verbose=True, maxbad=8, max_extract=12):
    """nullity_p of F = [E; EV] when a LOWER BOUND k0 on it is already a theorem
    (reducible side: nullity(E_red) = a - mult_red >= a - h_pad, Corollary B2).
    Same certificates as wk9_s45_cell.nullity_stacked -- the C helper stacks
    k_extra random dense rows R and a NONSINGULAR verdict for [F; R] proves
    nullity(F) <= k_extra -- but every run uses k_extra = max(k0, #exhibited
    kernel vectors), so when the theorem's floor is the truth ONE sequence
    settles it: nullity <= k0 (certificate) and >= k0 (theorem) give equality.
    A kernel vector found instead is checked against the full F and raises the
    exhibited count; extraction stops after max_extract vectors and the cell is
    then reported with bounds only (status 'bounded').
    Returns (k, kern, level, diag, exact)."""
    from wk9_s42_sparse import build_bin, compress, write_csr_mat, run_wied
    build_bin()
    WORK = os.environ['WIED_WORK']; os.makedirs(WORK, exist_ok=True)
    path = os.path.join(WORK, f'{tag}_{p}_{os.getpid()}.csr')
    E = sparse.csr_matrix(E)
    EV = sparse.csr_matrix(EV) if EV is not None else sparse.csr_matrix((0, nc), dtype=np.int64)
    Full = sparse.vstack([E, EV]).tocsr()
    rng = np.random.default_rng(seed0 * 7919 + p % 1000 + nc)
    kern = []; seed = seed0; bad = 0; t0 = time.time(); diag = []
    try:
        for li, (sample, group) in enumerate(levels):
            Ec = E if sample is None else compress(E, sample, group, rng)
            F = sparse.vstack([Ec, EV]).tocsr()
            nrows, nnz = write_csr_mat(F, p, path)
            if verbose:
                log(f"    level {li} ({sample},{group}): {nrows} rows, nnz {nnz} (full: {Full.shape[0]} rows, nnz {Full.nnz}); floor k0={k0}")
            escalate = False
            while not escalate:
                kx = max(k0, len(kern))
                st, payload, dg = run_wied(path, p, seed, kx)
                if verbose:
                    log(f"    wied[{tag} p={p} lvl={li} seed={seed} k_extra={kx} exhibited={len(kern)}]: {st} "
                        f"{' | '.join(dg)} ({time.time()-t0:.0f}s)")
                diag.append(dict(level=li, seed=seed, k_extra=int(kx), exhibited=len(kern), status=st,
                                 note=' | '.join(dg), rows=int(nrows), nnz=int(nnz)))
                seed += 1
                if st == 'NONSINGULAR':
                    return kx, (kern if want_kern else None), li, diag, True
                if st == 'KERNEL':
                    y = payload
                    assert len(y) == nc
                    chk = check_kernel_py if int(np.abs(Full.data).max(initial=0)) < 65536 else check_kernel_full
                    if not chk(Full, nc, p, y):
                        if verbose: log("    (kernel vector of the compressed matrix is not in ker F: escalate)")
                        escalate = True; continue
                    cand = kern + [y]
                    rk = nmod_mat(len(cand), nc, [v for vec in cand for v in vec], p).rank()
                    if rk == len(cand):
                        kern.append(y)
                        if len(kern) >= max_extract:
                            if verbose: log(f"    (extraction budget {max_extract} reached; reporting bounds)")
                            return len(kern), (kern if want_kern else None), li, diag, False
                    else:
                        bad += 1
                        if verbose: log("    (dependent kernel vector; retry)")
                else:
                    bad += 1
                if bad > maxbad:
                    raise RuntimeError(("sparse route inconclusive", tag, p, len(kern), bad))
        raise RuntimeError(("sparse route: escalation exhausted", tag, p, len(kern)))
    finally:
        try: os.remove(path)
        except OSError: pass


def _side_floor(tag, E, EV, nc, p, levels, seed0, k0, want_kern=True):
    k, kern, lvl, diag, exact = nullity_floor(E, EV, nc, p, k0=k0, want_kern=want_kern, seed0=seed0, tag=tag, levels=levels)
    return dict(nullity=int(k), level=int(lvl), diag=diag, kern=kern, exact=bool(exact), floor=int(k0))


def _side_sparse(tag, E, EV, nc, p, levels, seed0, want_kern):
    k, kern, lvl, diag = nullity_stacked(E, sparse.csr_matrix(EV) if EV is not None else sparse.csr_matrix((0, nc), dtype=np.int64),
                                         nc, p, want_kern=want_kern, seed0=seed0, tag=tag, levels=levels)
    return dict(nullity=int(k), level=int(lvl), diag=diag, kern=(kern if want_kern else None))


def _prime_job(args):
    p, opts = args
    B = _SHARED['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']; a = opts['a']; K = opts['K']
    lam = B['lam']; delta = B['delta']
    t0 = time.time()
    out = dict(prime=p, sides={})
    # evaluation rows (det always; red points when requested)
    t = time.time()
    EVd = ev_rows_from_coeffs(arr, [det_coeffs(pt) for pt in opts['det_pts']], p)
    EVr = ev_rows_from_coeffs(arr, [red_coeffs(pt) for pt in opts['red_pts']], p) if opts['red_points'] else None
    out['ev_secs'] = round(time.time() - t, 1)
    red = _SHARED['red']; nred = int(red.sum())
    out['n_red'] = nred
    if opts['route'] == 'dense':
        t = time.time()
        kern, kroute = kernel_dense(E, nc, p, a, exact_cap=opts['exact_cap'])
        out['kernel_secs'] = round(time.time() - t, 1); out['kernel_route'] = kroute
        G = _split_matmul_mod(EVd % p, kern.T % p, p)              # K x a
        md = rank_mod_p(G, p)
        nonred = np.nonzero(~red)[0]
        mstar = rank_mod_p(kern[:, nonred], p) if len(nonred) else 0
        out['sides']['det'] = dict(mult=int(md), nullity=int(a - md), instrument='dense kernel + det pencils', exact=True)
        out['sides']['red_star'] = dict(mult=int(mstar), nullity=int(a - mstar), instrument='dense kernel + (star)', exact=True)
        if opts['hpad'] is not None:
            assert mstar <= opts['hpad'], ('mult_red exceeds the normalisation bound h_pad', mstar, opts['hpad'])
        mr = None
        if EVr is not None:
            Gr = _split_matmul_mod(EVr % p, kern.T % p, p)
            mr = rank_mod_p(Gr, p)
            out['sides']['red_pts'] = dict(mult=int(mr), nullity=int(a - mr), instrument='dense kernel + l.c points', exact=True)
        # certificates: both primes when the verifier can recompute the kernel (N_S <= 3000);
        # one prime (P1) with the mod-p basis recorded when it cannot, and none when the basis
        # would be too large for the repository (N_S * a > 400k terms), which the record notes.
        big = B['N_S'] > 3000
        skip = big and (p != PRIMES[0] or B['N_S'] * a > 400_000)
        if opts['certs'] and skip:
            out['certs'] = []; out['cert_skipped'] = ('second prime' if p != PRIMES[0] else 'basis too large (N_S*a > 400k)')
        if opts['certs'] and not skip:
            t = time.time()
            basis = None
            if big:
                basis = [expand_vector(arr, v, p) for v in kern]
            tagl = '_'.join(map(str, lam)) + f'_d{delta}'
            files = []
            det_recs = [point_record('det_pencil', pt) for pt in opts['det_pts']]
            red_recs = [point_record('reducible', pt) for pt in opts['red_pts']]
            # determinant side: full_rank when mult_det = a, else the ideal vectors as an hwv certificate
            if md == a:
                fn = os.path.join(opts['certs'], f'{tagl}_det_pencil_p{p}.json.gz')
                sz = write_full_rank_cert(fn, lam, delta, a, p, 'det_pencil', det_recs, basis,
                                          title=f"mult_det_pencil({tuple(lam)}, {delta}) = a = {a}, mod {p}, length-5 balanced complement (session 60)",
                                          notes=("basis recorded: N_S exceeds the verifier's kernel cap" if basis else None))
                files.append([os.path.relpath(fn, ROOT), sz])
            else:
                cs = nullspace_mod_p(G.T, p)                       # a x K -> combos killed by every det point
                vecs = [expand_vector(arr, (c @ kern) % p, p) for c in cs]
                claims = {"independent": True, "vanishes_at": det_recs,
                          "fresh_points": {"seed": 20260905, "count": max(6, len(vecs) + 2),
                                           "vanishes_on": ["det_pencil"], "nonvanishing_on": ["generic"]}}
                fn = os.path.join(opts['certs'], f'{tagl}_det_ideal_p{p}.json.gz')
                sz = write_hwv_cert(fn, lam, delta, a, p, vecs, claims,
                                    title=f"{len(vecs)} highest-weight vector(s) of weight {tuple(lam)}, degree {delta}, in I(D_5^det4) mod {p} (session 60: mult_det = {md} < a = {a})")
                files.append([os.path.relpath(fn, ROOT), sz])
            # reducible side: full_rank when mult_red = a (by (star) and by points), else the (star)-supported ideal vectors
            if EVr is not None and mstar == a and mr == a:
                fn = os.path.join(opts['certs'], f'{tagl}_reducible_p{p}.json.gz')
                sz = write_full_rank_cert(fn, lam, delta, a, p, 'reducible', red_recs, basis,
                                          title=f"mult_reducible({tuple(lam)}, {delta}) = a = {a}, mod {p}, length-5 balanced complement (session 60)",
                                          notes=("basis recorded: N_S exceeds the verifier's kernel cap" if basis else None))
                files.append([os.path.relpath(fn, ROOT), sz])
            elif mstar < a:
                cs = nullspace_mod_p(kern[:, nonred].T, p) if len(nonred) else [np.eye(a, dtype=np.int64)[j] for j in range(a)]
                vecs = [expand_vector(arr, (c @ kern) % p, p) for c in cs]
                claims = {"independent": True, "star_support": {"k": 1}, "vanishes_at": red_recs,
                          "fresh_points": {"seed": 20260905, "count": max(6, len(vecs) + 2),
                                           "vanishes_on": ["reducible", "padded_permanent"],
                                           "nonvanishing_on": (["det_pencil", "generic"] if md == a else ["generic"])}}
                if md == a:
                    claims["nonvanishing_at"] = det_recs
                fn = os.path.join(opts['certs'], f'{tagl}_red_ideal_p{p}.json.gz')
                sz = write_hwv_cert(fn, lam, delta, a, p, vecs, claims,
                                    title=f"{len(vecs)} highest-weight vector(s) of weight {tuple(lam)}, degree {delta}, in I(R_5) by (star) mod {p} (session 60: mult_red = {mstar} < a = {a}, h_pad = {opts['hpad']})")
                files.append([os.path.relpath(fn, ROOT), sz])
            out['certs'] = files; out['cert_secs'] = round(time.time() - t, 1)
        if opts['want_kern']:
            out['kern'] = kern.tolist()
    else:
        levels = opts['levels']
        tag = 'c' + '_'.join(map(str, lam)) + f'd{delta}'
        k0 = opts['k0']
        t = time.time()
        sd = _side_sparse(tag + '_det', E, EVd, nc, p, levels, opts['seed0'], True)
        sd['secs'] = round(time.time() - t, 1); sd['instrument'] = 'sparse [E; ev_det]'
        sd['mult'] = a - sd['nullity']; sd['exact'] = True
        kd = sd.pop('kern')
        if kd: out['kern_det'] = kd
        out['sides']['det'] = sd
        if opts['hpad'] == 0:
            out['sides']['red_star'] = dict(mult=0, nullity=int(a), instrument='theorem: h_pad = 0 (Corollary B2)', exact=True, secs=0.0)
        else:
            # (star): E restricted to the red columns, with the theorem's floor a - h_pad on the nullity
            t = time.time()
            Ered = E[:, np.nonzero(red)[0]].tocsr(); Ered.eliminate_zeros()
            nzr = np.diff(Ered.indptr) > 0
            Ered = Ered[np.nonzero(nzr)[0]]
            ss = _side_floor(tag + '_star', Ered, None, nred, p, levels, opts['seed0'] + 100, k0)
            ss['secs'] = round(time.time() - t, 1); ss['instrument'] = 'sparse (star) E_red' + (f' with floor a-h_pad={k0}' if k0 else '')
            ss['mult'] = a - ss['nullity']; ss['rows'] = int(Ered.shape[0]); ss['nnz'] = int(Ered.nnz)
            ks = ss.pop('kern')
            if ks: out['kern_star'] = ks
            out['sides']['red_star'] = ss
            del Ered
            if EVr is not None:
                t = time.time()
                sr = _side_floor(tag + '_redpts', E, EVr, nc, p, levels, opts['seed0'] + 200, k0)
                sr['secs'] = round(time.time() - t, 1); sr['instrument'] = 'sparse [E; ev_red]' + (f' with floor a-h_pad={k0}' if k0 else '')
                sr['mult'] = a - sr['nullity']
                kr = sr.pop('kern')
                if kr: out['kern_redpts'] = kr
                out['sides']['red_pts'] = sr
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(_rss_gb(), 2)
    return out


def measure_cell(lam, delta, route='auto', dense_cap=4000, red_points='dense', certs=None,
                 seed_det=11, seed_red=29, bound=40, npts=None, levels='auto', want_kern=False,
                 parallel=True, seed0=1, exact_cap=2500, verbose=True, a_given=None, hpad=None):
    lam = tuple(lam)
    assert len(lam) == R and sum(lam) == N * delta
    t0 = time.time()
    B = build_cell(lam, delta, n=N, verbose=verbose)
    # a by the Weyl alternation (wk9_s42_census.a_weyl; the census asserted it equal to
    # s54's Frobenius plethysm at every delta <= 9 cell); the Frobenius route amb() costs
    # 25 s and 0.4 GB at delta = 8 and does not fit at delta = 10.
    a = a_weyl(lam, delta, N, {})
    if a_given is not None:
        assert a == a_given, ('a: census value disagrees with the Weyl alternation', lam, delta, a_given, a)
    K = npts if npts else a + 8
    nc = B['n_chi']
    if route == 'auto':
        route = 'dense' if nc <= dense_cap else 'sparse'
    if levels == 'auto':
        levels = 'cheap' if B['nrows'] <= 10 * nc else 's42'
    red = red_mask(B['arr'])
    out = dict(lam=list(lam), delta=delta, ell=R, a=a, K=K, N_S=B['N_S'], stab=B['stab'], n_chi=nc,
               n_red=int(red.sum()), nrows=B['nrows'], nnz=B['nnz'], nfixed=B['nfixed'],
               build_secs=round(B['build_secs'], 1), build_hwm_gb=round(B['hwm_gb'], 2),
               route=route, levels=(levels if route == 'sparse' else None),
               seeds=dict(det=seed_det, red=seed_red, wied=seed0), bound=bound, primes=list(PRIMES))
    if a == 0:
        out.update(status='a=0', secs=round(time.time() - t0, 1)); return out
    # the l.c-points instrument on the sparse route costs as much as the determinant side; it is
    # run at every dense-route cell and at sparse cells up to RED_PTS_CAP, (star) alone above
    want_red_pts = (red_points == 'always' and nc <= RED_PTS_CAP) or (red_points == 'dense' and route == 'dense')
    det_pts = det_pencils(K, seed_det, bound)
    red_pts = reducible_points(K, seed_red, bound)
    if certs: os.makedirs(certs, exist_ok=True)
    k0 = max(0, a - hpad) if hpad is not None else 0
    opts = dict(a=a, K=K, route=route, det_pts=det_pts, red_pts=red_pts, red_points=want_red_pts,
                certs=certs, levels=LEVELS[levels], seed0=seed0, want_kern=want_kern, exact_cap=exact_cap,
                hpad=hpad, k0=k0)
    out['h_pad'] = hpad; out['floor_red_nullity'] = k0
    _SHARED['B'] = B; _SHARED['red'] = red
    jobs = [(p, opts) for p in PRIMES]
    if parallel:
        import multiprocessing as mp
        with mp.get_context('fork').Pool(2) as pool:
            res = pool.map(_prime_job, jobs)
    else:
        res = [_prime_job(j) for j in jobs]
    _SHARED.clear()
    out['per_prime'] = {str(r['prime']): {k: v for k, v in r.items() if k not in ('prime', 'kern', 'kern_det', 'kern_star', 'kern_redpts')} for r in res}
    kerns = {str(r['prime']): {k: v for k, v in r.items() if k in ('kern', 'kern_det', 'kern_star', 'kern_redpts')} for r in res}
    # combine
    sides = {}
    for sd in ('det', 'red_star', 'red_pts'):
        vals = {r['prime']: r['sides'][sd]['mult'] for r in res if sd in r['sides']}
        if not vals: continue
        agree = len(set(vals.values())) == 1
        exact = all(r['sides'][sd].get('exact', True) for r in res if sd in r['sides'])
        sides[sd] = dict(mult=(vals[PRIMES[0]] if agree else None), per_prime={str(p): v for p, v in vals.items()},
                         primes_agree=agree, exact=exact, instrument=res[0]['sides'][sd]['instrument'])
        if not agree:
            sides[sd]['status'] = 'PRIMES DISAGREE'
        elif not exact:
            sides[sd]['status'] = 'bounded: mult <= %d (exhibited kernel), extraction budget reached' % vals[PRIMES[0]]
        elif vals[PRIMES[0]] == a:
            sides[sd]['status'] = 'proved (nullity 0 at both primes)'
        elif sd != 'det' and hpad is not None and vals[PRIMES[0]] == hpad:
            sides[sd]['status'] = 'proved (nullity = a - h_pad at both primes: certificate <= meets theorem >=)'
        elif route == 'dense':
            sides[sd]['status'] = 'measured (exact kernel, both primes): mult = %d' % vals[PRIMES[0]]
        else:
            sides[sd]['status'] = 'measured (nullity %d, two primes); mult >= %d proved' % (a - vals[PRIMES[0]], vals[PRIMES[0]])
    out['sides'] = sides
    out['mult_det'] = sides['det']['mult']
    out['mult_red_star'] = sides['red_star']['mult']
    out['mult_red_pts'] = sides['red_pts']['mult'] if 'red_pts' in sides else None
    out['mult_red'] = out['mult_red_star']
    out['star_eq_pts'] = (out['mult_red_pts'] == out['mult_red_star']) if out['mult_red_pts'] is not None else None
    out['D'] = (out['mult_red'] - out['mult_det']) if (out['mult_red'] is not None and out['mult_det'] is not None) else None
    out['refute'] = bool(out['D'] is not None and out['D'] > 0)
    out['ok'] = all(s['primes_agree'] for s in sides.values()) and (out['star_eq_pts'] in (None, True))
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(max(_rss_gb(), max(r['hwm_gb'] for r in res)), 2)
    if verbose:
        log(f"  RESULT {lam} d{delta}: a={a} n_chi={nc} route={route} mult_det={out['mult_det']} "
            f"mult_red(star)={out['mult_red_star']} mult_red(pts)={out['mult_red_pts']} D={out['D']}"
            f"{'  *** REFUTE ***' if out['refute'] else ''}  ({out['secs']}s, HWM {out['hwm_gb']} GB)")
    return out, kerns



if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    pos = []
    i = 0
    while i < len(args):
        if args[i].startswith('--'):
            i += 2
        else:
            pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res, kerns = measure_cell(lam, delta, route=arg('--route', 'auto'), dense_cap=arg('--dense-cap', 4000),
                              red_points=arg('--red-points', 'dense'), certs=arg('--certs', ''),
                              seed_det=arg('--seed-det', 11), seed_red=arg('--seed-red', 29), bound=arg('--bound', 40),
                              npts=arg('--npts', 0) or None, levels=arg('--levels', 'auto'),
                              want_kern=('--kern' in args), seed0=arg('--seed0', 1), exact_cap=arg('--exact-cap', 2500),
                              a_given=(arg('--a', -1) if '--a' in args else None),
                              hpad=(arg('--hpad', -1) if '--hpad' in args else None))
    print("RESULT " + json.dumps(res), flush=True)
    outp = arg('--out', '')
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
    if any(kerns.values()):      # kernel vectors are kept whenever a side produced them (a bite), not only on --kern
        import pickle
        kd = arg('--kern-dir', '/home/claude/s60/kern'); os.makedirs(kd, exist_ok=True)
        pickle.dump(dict(res=res, kerns=kerns), open(os.path.join(kd, f"kern_{'_'.join(map(str, lam))}_d{delta}.pkl"), 'wb'))
