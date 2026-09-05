#!/usr/bin/env python3
"""
Session 59 -- general order-q reducible exceptional image.

Arc M_0 + t M_1 + ... + t^q M_q, M_0 in a bounded-rank-3 stratum E. Leading
order forced to q : g_1 == ... == g_{q-1} == 0 ; leading quartic g_q in W
(pi g_q == 0). Reducible family [g_q/s_5] has dimension, at a generic V-point,

    rank d(g_1,...,g_q)  -  rank d(g_1,...,g_{q-1}, pi g_q).

V-point built iteratively : M_1 generic in {g_1==0} (homogeneous) ; for
2<=j<=q-1 solve g_j==0 for M_j (linear : tr(adj M_0 M_j) = -[g_j with M_j=0]) ;
M_q solves pi g_q==0. Each solve uses the augmented-nullspace trick. The order-3
solvability probe (wk9_s59_order3probe) shows the j=2 cancellation is solvable at
generic M_1 (codim 0), so the route runs at least to q=3.

Calibrates to the order-2 row 29,29,28,28,24 and reports q=3.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk9_s59_core import (R, n, NQ, S5DEG0, det_arc, pencils_to_entry,
                          rank_mod, quartic_vec, stratum_E_basis, STRATA)

P1, P2 = 2147483647, 2147483629

def m0_from(Eb, cpar, p, dual=None):
    m = len(Eb)
    M = [[[0]*n for _ in range(n)] for _ in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for j in range(m):
            c = cpar[k][j] % p
            for a in range(n):
                for b in range(n):
                    if Eb[j][a][b]:
                        M[k][a][b] = (M[k][a][b] + c*Eb[j][a][b]) % p
    if dual and dual[0] == 'c':
        _, k, j = dual
        for a in range(n):
            for b in range(n):
                if Eb[j][a][b]:
                    D[k][a][b] = (D[k][a][b] + Eb[j][a][b]) % p
    return M, D

def jets_from(mlist, p, dual=None):
    """mlist[j] integer pencil for M_j (j=0..q). dual=('m',j,k,a,b)."""
    Ms = []; Ds = []
    for j, Mj in enumerate(mlist):
        M = [[[Mj[k][a][b] % p for b in range(n)] for a in range(n)] for k in range(R)]
        D = [[[0]*n for _ in range(n)] for _ in range(R)]
        if dual and dual[0] == 'm' and dual[1] == j:
            _, _, k, a, b = dual; D[k][a][b] = 1
        Ms.append(M); Ds.append(D)
    return Ms, Ds

def all_g(Eb, cpar, mlist, p, q, dual=None):
    """return [g_1,...,g_q] as 70-vectors (value or dual part)."""
    if dual and dual[0] == 'c':
        M0, D0 = m0_from(Eb, cpar, p, dual)
    else:
        M0, D0 = m0_from(Eb, cpar, p)
    Ms, Ds = jets_from(mlist, p, dual if (dual and dual[0]=='m') else None)
    # mlist[j] is the order-j jet M_j (j=1..q) ; mlist[0] is unused. Orders:
    # [M0 (order 0)] + [mlist[1] (order 1), ..., mlist[q] (order q)].
    entry = pencils_to_entry([M0]+Ms[1:], p, duals=[D0]+Ds[1:])
    det = det_arc(entry, p, q)
    part = 1 if dual else 0
    return [quartic_vec(det.get(j, {}), p, part=part) for j in range(1, q+1)]

def solve_aug(cols, const, nrows, p):
    """solve sum_j x_j cols[j] = -const  (cols[j] length nrows). return particular
    x (len ncol) or None ; via augmented nullspace."""
    ncol = len(cols)
    Aug = nmod_mat(nrows, ncol+1,
        [ (int(cols[j][r]) if j < ncol else (const[r] % p))
          for r in range(nrows) for j in range(ncol+1)], p)
    X, naug = Aug.nullspace()
    for t in range(naug):
        last = int(X[ncol, t]) % p
        if last != 0:
            inv = pow(last, p-2, p)
            return [(int(X[r, t])*inv) % p for r in range(ncol)]
    return None

def build_Vpoint(Eb, p, q, rng, lo=1, hi=None):
    if hi is None: hi = p-1
    m = len(Eb)
    cpar = [[rng.randint(lo, hi) for _ in range(m)] for _ in range(R)]
    mlist = [[[[0]*n for _ in range(n)] for _ in range(R)] for _ in range(q+1)]
    # M_0 is implicit in cpar ; mlist[0] unused (kept zero, M_0 from cpar)
    # --- M_1 : g_1 == 0 (homogeneous) : pick generic nullspace element ---
    cols = []; idx = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                g = all_g(Eb, cpar, mlist, p, q, dual=('m', 1, k, a, b))
                cols.append(g[0]); idx.append((k, a, b))       # g_1 column
    A = nmod_mat(NQ, len(cols), [int(cols[j][r]) for r in range(NQ) for j in range(len(cols))], p)
    Xns, nul1 = A.nullspace()
    for t in range(nul1):
        w = rng.randint(1, p-1)
        for r, (k, a, b) in enumerate(idx):
            mlist[1][k][a][b] = (mlist[1][k][a][b] + w*int(Xns[r, t])) % p
    # --- M_j (2<=j<=q-1) : g_j == 0 (inhomogeneous, linear in M_j) ---
    for j in range(2, q):
        gconst = all_g(Eb, cpar, mlist, p, q)               # M_j=0 : g_j constant part
        const = gconst[j-1]                                  # g_j (index j-1 in 0-based list)
        cols = []; idx = []
        for k in range(R):
            for a in range(n):
                for b in range(n):
                    g = all_g(Eb, cpar, mlist, p, q, dual=('m', j, k, a, b))
                    cols.append(g[j-1]); idx.append((k, a, b))
        part = solve_aug(cols, const, NQ, p)
        if part is None: return None
        for r, (k, a, b) in enumerate(idx):
            mlist[j][k][a][b] = part[r] % p
        # add random kernel of the M_j map to keep g_j==0 but be generic
        Amat = nmod_mat(NQ, len(cols), [int(cols[jj][r]) for r in range(NQ) for jj in range(len(cols))], p)
        Xk, nk = Amat.nullspace()
        for t in range(nk):
            w = rng.randint(1, p-1)
            for r, (k, a, b) in enumerate(idx):
                mlist[j][k][a][b] = (mlist[j][k][a][b] + w*int(Xk[r, t])) % p
    # --- M_q : pi g_q == 0 (35 conditions, linear in M_q) ---
    gconst = all_g(Eb, cpar, mlist, p, q)
    const = [gconst[q-1][i] for i in S5DEG0]
    cols = []; idx = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                g = all_g(Eb, cpar, mlist, p, q, dual=('m', q, k, a, b))
                cols.append([g[q-1][i] for i in S5DEG0]); idx.append((k, a, b))
    part = solve_aug(cols, const, len(S5DEG0), p)
    if part is None: return None
    for r, (k, a, b) in enumerate(idx):
        mlist[q][k][a][b] = part[r] % p
    Amat = nmod_mat(len(S5DEG0), len(cols), [int(cols[jj][r]) for r in range(len(S5DEG0)) for jj in range(len(cols))], p)
    Xk, nk = Amat.nullspace()
    for t in range(nk):
        w = rng.randint(1, p-1)
        for r, (k, a, b) in enumerate(idx):
            mlist[q][k][a][b] = (mlist[q][k][a][b] + w*int(Xk[r, t])) % p
    return cpar, mlist, nul1

def orderq_dim(name, p, q, seed=5, lo=1, hi=None):
    rng = random.Random(seed)
    Eb = stratum_E_basis(name, rng, p); m = len(Eb)
    vp = build_Vpoint(Eb, p, q, rng, lo, hi)
    if vp is None:
        return dict(name=name, q=q, dimE=m, reducible=None, note="V-point failed")
    cpar, mlist, nul1 = vp
    # verify V-point : g_1..g_{q-1} == 0 and pi g_q == 0
    gv = all_g(Eb, cpar, mlist, p, q)
    ok = all(not any(gv[j]) for j in range(q-1)) and not any(gv[q-1][i] for i in S5DEG0)
    # Jacobian
    params = [('c', k, j) for k in range(R) for j in range(m)]
    for jj in range(1, q+1):
        params += [('m', jj, k, a, b) for k in range(R) for a in range(n) for b in range(n)]
    rows_full = []; rows_con = []
    for pr in params:
        if pr[0] == 'c':
            g = all_g(Eb, cpar, mlist, p, q, dual=('c',)+pr[1:])
        else:
            g = all_g(Eb, cpar, mlist, p, q, dual=('m',)+pr[1:])
        full = []
        for j in range(q): full += g[j]                       # g_1..g_q  (70q)
        con = []
        for j in range(q-1): con += g[j]                      # g_1..g_{q-1}
        con += [g[q-1][i] for i in S5DEG0]                    # pi g_q  (35)
        rows_full.append(full); rows_con.append(con)
    rk_full = rank_mod(rows_full, 70*q, p)
    rk_con  = rank_mod(rows_con, 70*(q-1)+len(S5DEG0), p)
    return dict(name=name, q=q, dimE=m, Vpoint_ok=ok, nul1=nul1,
                rank_full=rk_full, rank_con=rk_con, reducible=rk_full-rk_con)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--q', type=int, default=3)
    ap.add_argument('--strata', default=','.join(STRATA))
    ap.add_argument('--seed', type=int, default=5)
    ap.add_argument('--wide', action='store_true')
    ap.add_argument('--out', default='results/s59_orderq.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    lo, hi = (10**9, 10**9+4000) if a.wide else (1, None)
    res = {}
    for p in primes:
        res[str(p)] = {}
        for name in a.strata.split(','):
            r = orderq_dim(name, p, a.q, seed=a.seed, lo=lo, hi=hi)
            res[str(p)][name] = r
            print(f"[p={p}] q={a.q} {name:5s} Vok={r.get('Vpoint_ok')} "
                  f"reducible={r['reducible']} (order1/2 = 29,29,28,28,24 ; "
                  f"exact 31 ; target 35)", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
