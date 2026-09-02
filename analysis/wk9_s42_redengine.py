#!/usr/bin/env python3
"""
Session 42 -- the reducible-locus multiplicity engine (Route A).

mult_red(lam, delta) = mult of S_lam in C[R_r]_delta, R_r = {l . c} in Sym^4 C^r,
                     = a - dim( HWV_lam ∩ span M_★ )              (Cor. A, docs/reducible_ideal.md)
                     = a - nullity_Q( E_red ),

where E is the stack of simple raising operators on the chi_lam-isotypic
reduction V_chi (docs/stabiliser_reduction.md; orbit_setup / reduced_rows of
wk9_s36_stabred.py, imported unchanged) and E_red its restriction to the
columns indexed by orbits of M_★ monomials (an orbit is entirely in M_★ or
entirely out -- asserted).  M_★ = weight-lam monomials with, for every i, a
factor c_alpha with alpha_i = 0; only indices with lam_i >= delta constrain.

Certificates (one-sided, docs/reducible_engine.md section A):
    rank_p <= rank_Q   =>   nullity_p(E_red) >= nullity_Q(E_red)
                       =>   a - nullity_p(E_red) <= mult_red <= a.
So nullity_p = 0 PROVES mult_red = a; nullity_p = k > 0 gives mult_red >= a - k
(proved) and mult_red = a - k (measured, two primes), promoted to proved only
by exhibited rational kernel vectors (wk9_s42_lift.py).

Routes to nullity_p(E_red):
    exact       flint nullspace on E_red                (n_red <= EXACT_CAP; kernel vectors)
    compressed  Agg = P . E_red, P random (n_red + 64 rows), flint rref(inplace) rank
                (one dense copy, 8 n_red^2 bytes); nullity(Agg) >= nullity_p(E_red),
                so a compressed nullity 0 is a proof; k > 0 is re-run at a second P
    sparse      wk9_s42_sparse.py (Wiedemann certificates, C helper)

a is ALWAYS the plethysm value (wk8_s30_pleth); the kernel dimension of the
full E is asserted equal to it on validation cells (--full-check).

usage: python3 wk9_s42_redengine.py delta lam1 lam2 ... [--route exact|compressed|sparse|auto]
                                    [--full-check] [--out results/s42_cells.jsonl] [--kern]
"""
import sys, os, time, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s36_stabred import orbit_setup, reduced_rows, exps, monomials, P1, P2, log
from wk8_s30_pleth import a_of
from flint import nmod_mat

EXACT_CAP = 2500          # flint nullspace (3 copies) below this
DENSE_CAP = 26000         # flint rref(inplace) (1 copy) below this; ~5.4 GB at the cap

# ------------------------------------------------------------- the red split
def is_star(m, A, cons):
    """(★): for every constrained index i some factor has alpha_i = 0."""
    return all(any(A[k][i] == 0 for k in m) for i in cons)

def split_red(lam, delta, vecs, A):
    r = len(lam)
    cons = [i for i in range(r) if lam[i] >= delta]
    red, nonred = [], []
    for j, vec in enumerate(vecs):
        it = iter(vec)
        m0 = next(it)
        s0 = is_star(m0, A, cons)
        # an orbit is entirely star or entirely not (Stab permutes indices within blocks,
        # and the condition is symmetric under permutations preserving lam)
        for m in it:
            assert is_star(m, A, cons) == s0, ("orbit not homogeneous for (★)", lam, m0, m)
        (red if s0 else nonred).append(j)
    return cons, red, nonred

def restrict_rows(rows, cols):
    """rows as {col: val} over the sub-columns `cols` (reindexed 0..len(cols)-1)."""
    pos = {c: k for k, c in enumerate(cols)}
    out = []
    for d in rows:
        nd = {pos[c]: v for c, v in d.items() if c in pos}
        if nd: out.append(nd)
    return out

# ------------------------------------------------------------------ ranks
def _mat(rows, nc, p):
    M = nmod_mat(len(rows), nc, p)
    for i, d in enumerate(rows):
        for c, v in d.items():
            M[i, c] = v % p
    return M

def nullity_exact(rows, nc, p):
    if nc == 0: return 0, []
    if not rows: return nc, [[1 if i == j else 0 for i in range(nc)] for j in range(nc)]
    M = _mat(rows, nc, p)
    X, nul = M.nullspace()
    kern = [[int(X[i, j]) for i in range(nc)] for j in range(nul)]
    del M, X
    return nul, kern

def rank_compressed(rows, nc, p, margin=64, pseed=101):
    """rank of Agg = P . M, P random over F_p with nc + margin rows.
    rank(Agg) <= rank_p(M).  Assembled in chunks as (M^T @ P_chunk)^T by scipy
    sparse int64 (bound asserted), written into one flint nmod_mat, rref in
    place."""
    import numpy as np
    from scipy import sparse
    if nc == 0: return 0
    if not rows: return 0
    t0 = time.time()
    nrows = len(rows)
    rs = nc + margin
    ri = np.fromiter((r for r, d in enumerate(rows) for _ in d), dtype=np.int64)
    ci = np.fromiter((c for d in rows for c in d), dtype=np.int64)
    vv = np.fromiter((v for d in rows for v in d.values()), dtype=np.int64)
    maxabs = int(np.abs(vv).max())
    MT = sparse.csr_matrix((vv, (ci, ri)), shape=(nc, nrows), dtype=np.int64)   # raw small entries
    colfill = int(np.diff(MT.indptr).max())
    assert maxabs * (p - 1) * colfill < (1 << 62), ("int64 bound", maxabs, colfill)
    del ri, ci, vv
    rng = np.random.default_rng(pseed * 1000003 + p % 1000003 + nc)
    chunk = max(8, min(256, int(3e8 // (8 * nrows))))
    M = nmod_mat(rs, nc, p)
    for k0 in range(0, rs, chunk):
        cs = min(chunk, rs - k0)
        Pc = rng.integers(0, p, (nrows, cs), dtype=np.int64)
        # |entries of MT| <= maxabs, Pc < p, colfill terms: maxabs (p-1) colfill < 2^62 asserted
        C = (MT @ Pc) % p
        del Pc
        CT = np.ascontiguousarray(C.T); del C
        for k in range(cs):
            rl = CT[k].tolist()
            for j, v in enumerate(rl):
                if v: M[k0 + k, j] = v
        del CT
    del MT
    log(f"    Agg {rs}x{nc} assembled ({time.time()-t0:.0f}s; nrows {nrows}, max|M| {maxabs}, colfill {colfill})")
    _, rk = M.rref(inplace=True)
    del M
    log(f"    rref: rank {rk}, nullity {nc - rk} ({time.time()-t0:.0f}s)")
    return rk

# --------------------------------------------------------------- the cell
def build(lam, delta, verbose=True):
    """isotypic reduction + red split; returns dict of structures."""
    lam = tuple(lam); r = len(lam); n = 4
    assert sum(lam) == n * delta and all(lam[i] >= lam[i + 1] for i in range(r - 1)) and lam[-1] > 0
    t0 = time.time()
    A = exps(n, r)
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose)
    rows, nfx = reduced_rows(n, r, delta, lam, vecs, verbose)
    cons, red, nonred = split_red(lam, delta, vecs, A)
    rows_red = restrict_rows(rows, red)
    if verbose:
        log(f"  built: N_S={len(basis)} |Stab|={len(group)} n_chi={len(vecs)} n_red={len(red)} "
            f"n_nonred={len(nonred)} rows={len(rows)} rows_red={len(rows_red)} cons={cons} ({time.time()-t0:.0f}s)")
    return dict(lam=lam, delta=delta, r=r, A=A, basis=basis, vecs=vecs, group=group, rows=rows,
                rows_red=rows_red, cons=cons, red=red, nonred=nonred, N_S=len(basis),
                stab=len(group), n_chi=len(vecs), n_red=len(red), build_secs=time.time() - t0)

def nullity_route(rows, nc, p, route, want_kern=False, pseed=101):
    """returns (nullity_p, kern or None, route_used)."""
    if route == 'auto':
        route = 'exact' if (nc <= EXACT_CAP or want_kern) else 'compressed'
    if route == 'exact':
        nul, kern = nullity_exact(rows, nc, p)
        return nul, kern, 'exact'
    if route == 'compressed':
        rk = rank_compressed(rows, nc, p, pseed=pseed)
        nul = nc - rk
        if nul > 0:
            rk2 = rank_compressed(rows, nc, p, pseed=pseed + 7)
            nul = min(nul, nc - rk2)
        return nul, None, 'compressed'
    if route == 'sparse':
        from wk9_s42_sparse import nullity_sparse
        nul, kern = nullity_sparse(rows, nc, p, want_kern=want_kern)
        return nul, kern, 'sparse'
    raise ValueError(route)

def measure_cell(lam, delta, route='auto', full_check=False, want_kern=False, primes=(P1, P2), verbose=True):
    t0 = time.time()
    B = build(lam, delta, verbose)
    a = a_of(lam, delta, 4, len(lam))
    out = dict(lam=list(B['lam']), delta=delta, ell=B['r'], a=a, N_S=B['N_S'], stab=B['stab'],
               n_chi=B['n_chi'], n_red=B['n_red'], n_nonred=len(B['nonred']), cons=B['cons'],
               nrows=len(B['rows']), nrows_red=len(B['rows_red']), primes={}, kern=None)
    if a == 0:
        out.update(mult_red=0, status='a=0', secs=time.time() - t0)
        return out
    nuls = {}
    kerns = {}
    for p in primes:
        if full_check:
            nulE, _, rt = nullity_route(B['rows'], B['n_chi'], p, route if route != 'exact' or B['n_chi'] <= 6000 else 'compressed')
            assert nulE == a, ("nullity_p(E) != a (plethysm)", lam, delta, p, nulE, a)
            if verbose: log(f"  p={p}: full-E nullity {nulE} = a  [{rt}]")
        nul, kern, rt = nullity_route(B['rows_red'], B['n_red'], p, route, want_kern=want_kern)
        assert nul <= a, ("nullity_p(E_red) > a -- impossible over Q; unlucky prime or bug", lam, delta, p, nul, a)
        nuls[p] = nul; kerns[p] = kern
        out['primes'][str(p)] = dict(nullity=nul, route=rt)
        if verbose: log(f"  p={p}: nullity_p(E_red) = {nul}  -> mult_red >= {a - nul}  [{rt}] ({time.time()-t0:.0f}s)")
    assert len(set(nuls.values())) == 1, ("primes disagree on nullity", lam, delta, nuls)
    k = nuls[primes[0]]
    out['nullity'] = k
    out['mult_red'] = a - k
    out['status'] = 'proved (nullity 0)' if k == 0 else f'measured (nullity {k}, two primes); mult_red >= {a-k} proved'
    if want_kern and kerns[primes[0]] is not None:
        out['kern'] = {str(p): kerns[p] for p in primes}
    out['secs'] = time.time() - t0
    monomials.cache_clear()
    return out

if __name__ == '__main__':
    args = sys.argv[1:]
    route = 'auto'; full = False; outp = None; want_kern = False
    pos = []
    i = 0
    while i < len(args):
        if args[i] == '--route': route = args[i + 1]; i += 2
        elif args[i] == '--full-check': full = True; i += 1
        elif args[i] == '--kern': want_kern = True; i += 1
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res = measure_cell(lam, delta, route=route, full_check=full, want_kern=want_kern)
    kern = res.pop('kern', None)
    print(json.dumps(res))
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
    if kern is not None:
        import pickle
        os.makedirs('/root/s42', exist_ok=True)
        pickle.dump(dict(res=res, kern=kern), open(f"/root/s42/kern_{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
