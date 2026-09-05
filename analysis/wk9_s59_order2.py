#!/usr/bin/env python3
"""
Session 59 -- section 2B : the order-2 (q=2) reducible exceptional image.

Arc M(t,s) = M_0 + t M_1 + t^2 M_2, M_0 in a bounded-rank-3 stratum E.
det = g_1 t + g_2 t^2 + ... (g_0 = det M_0 == 0). Require the leading order be
q=2 : g_1 == 0 ; and g_2 in W : pi g_2 == 0. Track [c] = [g_2 / s_5].

The dimension of the reducible family reached is, at a generic point of the
constraint variety {g_1 == 0, pi g_2 == 0} (a V-point):

    dim{[c]} = rank d(g_1, g_2)  -  rank d(g_1, pi g_2)

    (= dim of the c-image on the tangent to the constraints ; identity
     dim B(ker A) = rank[A;B] - rank A, with A = d(g_1, pi g_2), B = dc, and
     (pi g_2, c) reparametrising g_2 so [A;B] = d(g_1, g_2)).

At order 1 the same identity with no g_1-constraint gives the calibrated
29,29,28,28,24. Here the leading term is pushed to t^2, so M_1 != 0 contributes
the second-order (Hessian-of-det) term e_2(M_0;M_1) that order 1 cannot see.

Compared against the exact 31 and the target 35.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk9_s59_core import (R, n, NQ, QIDX, S5DEG0, det_arc, pencils_to_entry,
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

def gen_from(par, p, dual=None, tag='m1'):
    M = [[[par[k][a][b] % p for b in range(n)] for a in range(n)] for k in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    if dual and dual[0] == tag:
        _, k, a, b = dual; D[k][a][b] = 1
    return M, D

def g12(Eb, cpar, m1, m2, p, dual=None):
    """return (g1_vec70, g2_vec70) value-parts, or dual-parts if dual set."""
    M0, D0 = m0_from(Eb, cpar, p, dual if (dual and dual[0]=='c') else None)
    M1, D1 = gen_from(m1, p, dual if (dual and dual[0]=='m1') else None, 'm1')
    M2, D2 = gen_from(m2, p, dual if (dual and dual[0]=='m2') else None, 'm2')
    entry = pencils_to_entry([M0, M1, M2], p, duals=[D0, D1, D2])
    det = det_arc(entry, p, 2)
    part = 1 if dual else 0
    g1 = quartic_vec(det.get(1, {}), p, part=part)
    g2 = quartic_vec(det.get(2, {}), p, part=part)
    return g1, g2

def build_Vpoint(Eb, p, rng, lo=1, hi=None):
    if hi is None: hi = p-1
    m = len(Eb)
    cpar = [[rng.randint(lo, hi) for _ in range(m)] for _ in range(R)]
    zero = [[[0]*n for _ in range(n)] for _ in range(R)]
    # --- solve M_1 : g_1 == 0 (linear in M_1's 80 entries) ---
    cols = []; idx = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                g1, _ = g12(Eb, cpar, zero, zero, p, dual=('m1', k, a, b))
                cols.append(g1); idx.append((k, a, b))
    ncol = len(cols)
    A = nmod_mat(NQ, ncol, [int(cols[j][r]) for r in range(NQ) for j in range(ncol)], p)
    Xns, nul1 = A.nullspace()
    m1 = [[[0]*n for _ in range(n)] for _ in range(R)]
    for t in range(nul1):
        w = rng.randint(1, p-1)
        for r, (k, a, b) in enumerate(idx):
            m1[k][a][b] = (m1[k][a][b] + w*int(Xns[r, t])) % p
    # --- solve M_2 : pi g_2 == 0 (linear in M_2 ; constant from M_1) ---
    g1c, g2c = g12(Eb, cpar, m1, zero, p)          # M_2 = 0 : constant part
    const = [g2c[i] for i in S5DEG0]
    cols2 = []; idx2 = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                _, g2 = g12(Eb, cpar, m1, zero, p, dual=('m2', k, a, b))
                cols2.append([g2[i] for i in S5DEG0]); idx2.append((k, a, b))
    ncol2 = len(cols2); nr = len(S5DEG0)
    # solve  sum_j x_j cols2[j] = -const  (underdetermined 35 x 80) via the
    # augmented-nullspace trick : a null vector of [A | -b] (nr x (ncol2+1))
    # with last coord != 0 gives a particular solution after scaling.
    Aug = nmod_mat(nr, ncol2 + 1,
        [ (int(cols2[j][r]) if j < ncol2 else (const[r] % p))    # last col = +const
          for r in range(nr) for j in range(ncol2 + 1)], p)
    Xaug, naug = Aug.nullspace()
    part = None
    for t in range(naug):
        last = int(Xaug[ncol2, t]) % p
        if last != 0:
            inv = pow(last, p - 2, p)
            part = [(int(Xaug[r, t]) * inv) % p for r in range(ncol2)]  # A x = -const
            break
    if part is None:
        return None                     # -const not in column space (rank shortfall)
    m2 = [[[0]*n for _ in range(n)] for _ in range(R)]
    for r, (k, a, b) in enumerate(idx2):
        m2[k][a][b] = part[r] % p
    # add a random kernel element of A (keeps pi g_2 == 0) for genericity
    Amat = nmod_mat(nr, ncol2, [int(cols2[j][r]) for r in range(nr) for j in range(ncol2)], p)
    Xk, nulk = Amat.nullspace()
    for t in range(nulk):
        w = rng.randint(1, p-1)
        for r, (k, a, b) in enumerate(idx2):
            m2[k][a][b] = (m2[k][a][b] + w*int(Xk[r, t])) % p
    return cpar, m1, m2, nul1, nulk

def order2_dim(name, p, seed=5, lo=1, hi=None):
    rng = random.Random(seed)
    Eb = stratum_E_basis(name, rng, p); m = len(Eb)
    vp = build_Vpoint(Eb, p, rng, lo, hi)
    if vp is None:
        return dict(name=name, dimE=m, order2_reducible=None, note="V-point solve failed")
    cpar, m1, m2, nul1, nulk = vp
    # verify V-point : g_1 == 0 and pi g_2 == 0
    g1v, g2v = g12(Eb, cpar, m1, m2, p)
    ok_g1 = not any(g1v)
    ok_pig2 = not any(g2v[i] for i in S5DEG0)
    # Jacobian columns : each a (g1[70] , g2[70]) = 140-vector
    params = [('c', k, j) for k in range(R) for j in range(m)] + \
             [('m1', k, a, b) for k in range(R) for a in range(n) for b in range(n)] + \
             [('m2', k, a, b) for k in range(R) for a in range(n) for b in range(n)]
    rows_full = []   # 140 cols : g1 (70) ++ g2 (70)
    rows_con  = []   # 105 cols : g1 (70) ++ pi g2 (35)
    for pr in params:
        g1d, g2d = g12(Eb, cpar, m1, m2, p, dual=pr)
        rows_full.append(g1d + g2d)
        rows_con.append(g1d + [g2d[i] for i in S5DEG0])
    rk_full = rank_mod(rows_full, 140, p)
    rk_con  = rank_mod(rows_con, 105, p)
    return dict(name=name, dimE=m, nul1=nul1, nulk=nulk,
                Vpoint_ok=(ok_g1 and ok_pig2),
                rank_full=rk_full, rank_con=rk_con,
                order2_reducible=rk_full - rk_con)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--strata', default=','.join(STRATA))
    ap.add_argument('--seed', type=int, default=5)
    ap.add_argument('--wide', action='store_true', help='wide points (KC4 certification)')
    ap.add_argument('--out', default='results/s59_order2.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    lo, hi = (1, None)
    if a.wide: lo, hi = (10**9, 10**9 + 4000)
    res = {}
    for p in primes:
        res[str(p)] = {}
        for name in a.strata.split(','):
            r = order2_dim(name, p, seed=a.seed, lo=lo, hi=hi)
            res[str(p)][name] = r
            print(f"[p={p}] {name:5s} dimE={r['dimE']:2d} Vok={r.get('Vpoint_ok')} "
                  f"nul1={r.get('nul1')} nulk={r.get('nulk')} "
                  f"order2_reducible={r['order2_reducible']} "
                  f"(exact 31, target 35)", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
