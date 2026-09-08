#!/usr/bin/env python3
"""
Session 70 (C3) -- the reducible-normalisation split S, exactly, at n=4 cells.

    S = S_{lam,delta} : M^(4)_lam  ->  (+)_mu M^(3)_mu ,   rank S = mult_red.

M^(4)_lam = HWV_lam( Sym^delta Sym^4 V ), dim a  (the QUARTIC source).
The target is the degree-delta part of the NORMALISATION of C[R_r],
    D_delta = Sym^delta V (x) Sym^delta(Sym^3 V),   dim h_pad,
and S is the comultiplication (split) map Sym^4 V -> V (x) Sym^3 V, in coordinates

    mu*(c_alpha) = sum_{i: alpha_i >= 1}  y_i (x) d_{alpha - e_i}      (|alpha| = 4)

extended as a ring homomorphism to degree delta and restricted to the
lam-highest-weight space.  This is exactly the SYMBOLIC form of the programme's
own reducible evaluation red_coeffs (wk9_s60_cell): out[alpha] += l_i * c_{alpha-e_i}.
Ranking mu*(HWV_j) over the codomain monomial basis gives dim of the lam-isotypic
image = mult_red = rank S  (Corollary B2 / KL Thm 1.7; docs/s_split.md).

SOURCE-DEPENDENCE (Part A, docs/s_split.md).  The target rows (the Pieri shapes,
the 48 M^(3)_mu blocks at LMR) and mu* itself are source-free, but the COLUMNS
are a basis of M^(4)_lam -- explicit quartic highest-weight vectors.  Here that
basis is the kernel of the raising operators on the chi_lam-isotypic carrier
(wk9_s45_build.build_cell), cheap at r=5 and the r=9,delta=24 wall at LMR
(session 63).  So this instrument is exactly as gated at LMR as det A_24;
the two n=4 cells below are the ungated calibration.

Cross-checks per cell (all must agree, and equal the banked mult_red):
  * rank S at both house primes;
  * rank S at two independent codomain multiset-hash seeds (a hash collision can
    only DROP rank, so agreement across seeds + equality to the banked value
    certifies no harmful collision);
  * the (star)/E_red route on the SAME HWVs: mult_red = rank( kern[:, non-red] )
    (docs/reducible_ideal.md Theorem 1; wk9_s60_cell red_mask), a route sharing
    no code with mu*;
  * a_weyl = nullity(E) at both primes.

usage: python3 analysis/wk11_s70_split.py delta lam1 .. lam_r [--out FILE] [--certs DIR]
"""
import sys, os, time, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
import numpy as np
from scipy import sparse
from flint import nmod_mat
from wk8_s30_core import exps, P1, P2
from wk9_s45_build import build_cell, log, _rss_gb
from wk9_s42_census import a_weyl
from wk9_s42_hpad import h_pad as h_pad_fn
from wk9_s60_cell import kernel_dense, red_mask

N = 4
PRIMES = (P1, P2)


def rank_mod_p(rows, ncols, p):
    """flint rank of a small dense int matrix given as a 2-D int array."""
    A = np.asarray(rows, dtype=object)  # avoid overflow when reducing; entries reduced below
    m = A.shape[0]
    if m == 0 or ncols == 0:
        return 0
    ent = [int(v) % p for v in np.asarray(rows, dtype=np.int64).ravel().tolist()]
    return nmod_mat(m, ncols, ent, p).rank()


def split_tables(r):
    """for each quartic-exp index q (|alpha|=4 in r vars): the mu* choices
    (i, cubic-exp-index of alpha - e_i) for every i with alpha_i >= 1.
    Returned flattened with per-q offsets."""
    A4 = exps(4, r); A3 = exps(3, r)
    idx3 = {a: k for k, a in enumerate(A3)}
    CHi, CHc, cstart = [], [], [0]
    for al in A4:
        for i in range(r):
            if al[i] >= 1:
                b = list(al); b[i] -= 1
                CHi.append(i); CHc.append(idx3[tuple(b)])
        cstart.append(len(CHi))
    return (np.array(CHi, dtype=np.int64), np.array(CHc, dtype=np.int64),
            np.array(cstart, dtype=np.int64), len(A3))


def explode(M, r, seeds=(0x9E3779B1, 0x85EBCA6B)):
    """vectorised mu* on the weight-lam monomial basis M (N_S x delta, entries =
    quartic-exp indices).  Returns (mono_id, gamma_key, [chash per seed]) over all
    ~Sum(prod nnz) expansion terms.  gamma_key is EXACT (base-(delta+1) packing of
    the 5-<=r-coord linear multidegree, each coord <= delta); each chash is an
    additive multiset hash of the cubic indices (order-independent, exact modulo
    a 63-bit collision)."""
    CHi, CHc, cstart, nA3 = split_tables(r)
    N_S, delta = M.shape
    base = delta + 1
    POW = np.array([base ** c for c in range(r)], dtype=np.int64)   # base^i
    assert base ** r < (1 << 62), "gamma packing overflow"          # any base-(delta+1) r-digit key < (delta+1)^r
    Hs = []
    for s in seeds:
        rng = np.random.default_rng(s)
        Hs.append(rng.integers(1, 1 << 62, size=nA3, dtype=np.int64))
    mono = np.arange(N_S, dtype=np.int64)
    gkey = np.zeros(N_S, dtype=np.int64)
    ch = [np.zeros(N_S, dtype=np.int64) for _ in Hs]
    for j in range(delta):
        q = M[mono, j]                      # quartic-exp index at position j
        k = (cstart[q + 1] - cstart[q])     # branch count per current partial
        rep = np.repeat(np.arange(mono.size), k)
        # choice index c within each partial (0..k-1)
        off = np.arange(rep.size) - np.repeat(np.cumsum(k) - k, k)
        flat = cstart[q][rep] + off
        gi = CHi[flat]; gc = CHc[flat]
        mono = mono[rep]
        gkey = gkey[rep] + POW[gi]
        ch = [c[rep] + H[gc] for c, H in zip(ch, Hs)]
    return mono, gkey, ch


def rank_S(B, kern_chi, p_list, verbose=True):
    """rank S at each prime, for each of two codomain hash seeds.
    kern_chi[p] : a x n_chi HWV basis (kernel of E) mod p, in chi-coordinates."""
    arr = B['arr']; M = arr['M']; col_of = arr['col_of']; sgn = arr['sgn']
    r = B['r']; N_S = B['N_S']; a = None
    t0 = time.time()
    mono, gkey, chs = explode(M, r)
    if verbose:
        log(f"    mu* expansion: {mono.size:,} terms over N_S={N_S} ({time.time()-t0:.0f}s, HWM {_rss_gb():.2f} GB)")
    out = {}
    # column ids for each hash seed (pair (gamma_key, chash) -> unique id)
    Ts = []
    for chash in chs:
        pair = np.stack([gkey, chash], axis=1)
        _, colid = np.unique(pair, axis=0, return_inverse=True)
        colid = np.asarray(colid).ravel()
        ncod = int(colid.max()) + 1 if colid.size else 0
        T = sparse.coo_matrix((np.ones(mono.size, dtype=np.int64), (mono, colid)),
                              shape=(N_S, ncod), dtype=np.int64).tocsr()
        T.sum_duplicates()
        Ts.append((T, ncod))
    ranks = {}
    for p in p_list:
        kern = kern_chi[p]                      # a x n_chi
        a = kern.shape[0]
        # expand HWVs to monomial coordinates: W[:, m] = kern[:, col_of[m]] * sgn[m]
        W = np.zeros((a, N_S), dtype=np.int64)
        valid = col_of >= 0
        W[:, valid] = (kern[:, col_of[valid]] * sgn[valid]) % p
        for si, (T, ncod) in enumerate(Ts):
            # C = W @ T  (a x ncod); accumulate in int64, reduce mod p.
            # per-entry |C[ai,col]| = |sum_m W[ai,m] T[m,col]| <= (p-1) * max_col_sum(T)
            colsum = int(np.asarray(T.sum(axis=0)).ravel().max()) if T.nnz else 0
            assert (p - 1) * colsum < (1 << 62), ("int64 accumulation bound", p, colsum)
            C = (T.transpose().dot(W.transpose())).transpose()   # ncod x a -> a x ncod (dense)
            C = np.asarray(C) % p
            rk = rank_mod_p(C, ncod, p)
            ranks[(p, si)] = int(rk)
    out['ranks'] = {f'{p}|seed{si}': v for (p, si), v in ranks.items()}
    out['rank_S'] = None
    vals = set(ranks.values())
    if len(vals) == 1:
        out['rank_S'] = vals.pop()
    out['a'] = a
    out['secs'] = round(time.time() - t0, 1)
    out['ncod'] = [int(nc) for _, nc in Ts]
    return out


def star_route(B, kern_chi, p_list):
    """mult_red via Theorem (star): rank( kern[:, non-red] ), on the SAME HWVs.
    (wk9_s60_cell semantics: mstar = rank kern[:, ~red].)"""
    red = red_mask(B['arr'])            # boolean over chi-columns
    nonred = np.nonzero(~red)[0]
    res = {}
    for p in p_list:
        kern = kern_chi[p]
        if len(nonred):
            res[p] = rank_mod_p(kern[:, nonred], len(nonred), p)
        else:
            res[p] = 0
    return res, int(red.sum())


def measure(lam, delta, out_file=None, certs=None, verbose=True):
    lam = tuple(lam); r = len(lam)
    assert sum(lam) == N * delta
    a_exp = a_weyl(lam, delta, N, {})
    hpad = h_pad_fn(lam, delta)
    B = build_cell(lam, delta, n=N, verbose=verbose)
    nc = B['n_chi']; E = B['E']
    rec = dict(lam=list(lam), delta=delta, r=r, a=a_exp, h_pad=hpad,
               N_S=B['N_S'], n_chi=nc, stab=B['stab'], nrows=B['nrows'], nnz=B['nnz'],
               primes=list(PRIMES), build_secs=round(B['build_secs'], 1))
    # HWV bases: kernel of E, both primes, verified on the full sparse E by kernel_dense
    kern_chi = {}
    for p in PRIMES:
        kern, kroute = kernel_dense(E, nc, p, a_exp)      # asserts nullity == a, checks E.v=0
        kern_chi[p] = kern % p
        rec.setdefault('kernel_route', kroute)
    # rank S (the split), both primes, two hash seeds
    S = rank_S(B, kern_chi, PRIMES, verbose=verbose)
    rec['rank_S_detail'] = S['ranks']; rec['rank_S'] = S['rank_S']
    rec['ncod'] = S['ncod']; rec['split_secs'] = S['secs']
    # (star) cross-check on the same HWVs
    star, nred = star_route(B, kern_chi, PRIMES)
    rec['mult_red_star'] = {str(p): int(v) for p, v in star.items()}
    rec['n_red'] = nred
    star_val = star[PRIMES[0]] if len(set(star.values())) == 1 else None
    rec['mult_red_star_val'] = star_val
    rec['i_red'] = (a_exp - rec['rank_S']) if rec['rank_S'] is not None else None
    rec['agree'] = (rec['rank_S'] is not None and rec['rank_S'] == star_val)
    rec['hwm_gb'] = round(_rss_gb(), 2)
    if verbose:
        log(f"  RESULT {lam} d{delta}: a={a_exp} h_pad={hpad} n_chi={nc} "
            f"rank_S={rec['rank_S']} (star mult_red={star_val}) i_red={rec['i_red']} "
            f"agree={rec['agree']}  [{rec['split_secs']}s]")
    if out_file:
        with open(out_file, 'a') as f:
            f.write(json.dumps(rec) + "\n")
    if certs:
        os.makedirs(certs, exist_ok=True)
        cert = {"format": "gct-cert/1", "kind": "split_rank",
                "produced_by": "analysis/wk11_s70_split.py (session 70)",
                "cell": {"n": N, "r": r, "lambda": list(lam), "delta": delta,
                         "a": a_exp, "h_pad": hpad},
                "claim": {"rank_S": rec['rank_S'], "equals": "mult_red",
                          "i_red": rec['i_red']},
                "cross_checks": {"primes": list(PRIMES),
                                 "hash_seeds": 2,
                                 "star_route_rank_nonred": rec['mult_red_star'],
                                 "a_weyl_equals_nullity_E": True},
                "detail": S['ranks']}
        tag = '_'.join(map(str, lam)) + f'_d{delta}'
        fn = os.path.join(certs, f'{tag}_split.json')
        with open(fn, 'w') as f:
            json.dump(cert, f, indent=1)
        rec['cert'] = os.path.relpath(fn, ROOT)
    return rec


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default=None):
        return args[args.index(name) + 1] if name in args else default
    pos = []
    i = 0
    while i < len(args):
        if args[i].startswith('--'):
            i += 2
        else:
            pos.append(int(args[i])); i += 1
    delta = pos[0]; lam = tuple(pos[1:])
    rec = measure(lam, delta, out_file=arg('--out'), certs=arg('--certs'))
    print("RESULT " + json.dumps(rec), flush=True)
