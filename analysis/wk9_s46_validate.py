#!/usr/bin/env python3
"""
Session 46 -- V4: the generator build against the session-45 build.

For each cell:
  * the isotypic reduction: n_chi, the dropped-orbit count, col_of entrywise,
    sgn entrywise (both routes anchor +1 at the minimum-index representative, so
    the signs must agree exactly, not merely up to a per-orbit global sign);
  * the raising operators: shape, nnz, and the matrix entrywise; plus, where the
    cell is small enough, rank over both house primes of E45, E46 and
    vstack(E45, E46) -- equal ranks certify equal row space independently of the
    entrywise check;
  * a global-sign-only comparison is ALSO reported, so that a hypothetical
    convention difference would be visible as such rather than as a failure.

usage: python3 wk9_s46_validate.py [--rank-cap N] delta lam... [-- delta lam...]
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from scipy import sparse
from wk9_s45_build import monomials_array, orbit_setup_arr, raising_rows_arr, log, _rss_gb
from wk9_s46_gen import orbit_setup_gen, raising_rows_gen, group_order, stab_generators

def rank_p(A, p):
    from flint import nmod_mat
    A = sparse.csr_matrix(A)
    D = np.zeros(A.shape, dtype=np.int64)
    D[:] = A.toarray() % p
    return nmod_mat(A.shape[0], A.shape[1], [int(x) for x in D.reshape(-1)], p).rank()

def compare(lam, delta, n=4, rank_cap=1200, verbose=True):
    lam = tuple(lam); r = len(lam)
    out = dict(lam=list(lam), delta=delta, stab=group_order(lam),
               ngen=len(stab_generators(lam)))
    t0 = time.time()
    M = monomials_array(n, r, delta, lam, verbose=False)
    out['N_S'] = int(M.shape[0])
    t = time.time(); a45 = orbit_setup_arr(n, r, delta, lam, M=M, verbose=False)
    out['orbit_secs_s45'] = round(time.time() - t, 2)
    t = time.time(); a46 = orbit_setup_gen(n, r, delta, lam, M=M, verbose=False)
    out['orbit_secs_s46'] = round(time.time() - t, 2)
    out['rounds'] = a46['rounds']
    out['n_chi_s45'] = a45['n_chi']; out['n_chi_s46'] = a46['n_chi']
    out['dropped_s45'] = a45['dropped']; out['dropped_s46'] = a46['dropped']
    out['col_of_equal'] = bool(np.array_equal(a45['col_of'], a46['col_of']))
    out['sgn_equal'] = bool(np.array_equal(a45['sgn'], a46['sgn']))
    if not out['sgn_equal']:
        # is it only a per-orbit global sign?
        c = a45['col_of']; live = c >= 0
        ratio = a45['sgn'][live] * a46['sgn'][live]
        byorb = np.full(a45['n_chi'], 0, dtype=np.int64)
        byorb[c[live]] = ratio
        out['sgn_equal_up_to_global'] = bool(np.all(ratio == byorb[c[live]]))
    else:
        out['sgn_equal_up_to_global'] = True
    out['speedup_orbits'] = (round(out['orbit_secs_s45'] / out['orbit_secs_s46'], 2)
                             if out['orbit_secs_s46'] > 0 else None)
    ok = out['col_of_equal'] and out['sgn_equal'] and out['n_chi_s45'] == out['n_chi_s46'] \
         and out['dropped_s45'] == out['dropped_s46']
    t = time.time(); E45, f45 = raising_rows_arr(n, r, delta, lam, a45, verbose=False)
    out['rows_secs_s45'] = round(time.time() - t, 2)
    t = time.time(); E46, f46 = raising_rows_gen(n, r, delta, lam, a46, verbose=False)
    out['rows_secs_s46'] = round(time.time() - t, 2)
    out['shape_s45'] = list(E45.shape); out['shape_s46'] = list(E46.shape)
    out['nnz_s45'] = int(E45.nnz); out['nnz_s46'] = int(E46.nnz)
    out['nfixed_s45'] = int(f45); out['nfixed_s46'] = int(f46)
    same_shape = E45.shape == E46.shape
    out['E_entrywise_equal'] = bool(same_shape and (E45 != E46).nnz == 0)
    ok = ok and out['E_entrywise_equal'] and f45 == f46
    if E45.shape[1] <= rank_cap and same_shape:
        from wk9_s36_stabred import P1, P2
        rr = {}
        for p in (P1, P2):
            r45 = rank_p(E45, p); r46 = rank_p(E46, p)
            rst = rank_p(sparse.vstack([E45, E46]), p)
            rr[str(p)] = dict(r45=r45, r46=r46, rstack=rst, equal=bool(r45 == r46 == rst))
            ok = ok and (r45 == r46 == rst)
        out['rank_rowspace'] = rr
    else:
        out['rank_rowspace'] = 'entrywise identical (n_chi above the dense rank cap)'
    out['ok'] = bool(ok)
    out['secs'] = round(time.time() - t0, 1)
    out['hwm_gb'] = round(_rss_gb(), 2)
    if verbose:
        log(f"  {lam} d{delta}: |Stab|={out['stab']} ngen={out['ngen']} N_S={out['N_S']} "
            f"n_chi={out['n_chi_s46']} orbits {out['orbit_secs_s45']}s -> {out['orbit_secs_s46']}s "
            f"(x{out['speedup_orbits']}) rows {out['rows_secs_s45']}s -> {out['rows_secs_s46']}s "
            f"{'OK' if ok else 'MISMATCH'}")
    return out

if __name__ == '__main__':
    args = sys.argv[1:]
    rank_cap = 1200; outp = None
    cells = []
    cur = []
    i = 0
    while i < len(args):
        if args[i] == '--rank-cap': rank_cap = int(args[i + 1]); i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        elif args[i] == '--': 
            if cur: cells.append(cur); cur = []
            i += 1
        else: cur.append(int(args[i])); i += 1
    if cur: cells.append(cur)
    res = []
    allok = True
    for c in cells:
        r = compare(tuple(c[1:]), c[0], rank_cap=rank_cap)
        res.append(r); allok = allok and r['ok']
        if outp:
            with open(outp, 'a') as f: f.write(json.dumps(r) + "\n")
    print(json.dumps(dict(ok=allok, cells=res)))
    sys.exit(0 if allok else 1)
