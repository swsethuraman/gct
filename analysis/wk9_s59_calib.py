#!/usr/bin/env python3
"""
Session 59 -- calibration. Reproduce the s54 anchors with the s59 arc machinery
BEFORE any higher-order work (brief section 5):
    dim D_5 = 50                       (tangent at a generic determinantal point)
    order-1 image dim  50,50,47,47,49  over ker,coker,c21,c32,prim  (fills D_5)
    order-1 reducible  29,29,28,28,24  (border, all < 31 = exact locus)
If these do not reproduce, stop and fix the machinery.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from wk9_s59_core import (R, n, NQ, QIDX, QEXP, S5DEG0, S5POS,
                          det_arc, pencils_to_entry, rank_mod, quartic_vec,
                          stratum_E_basis, random_pencil_in_E, random_pencil,
                          STRATA)

P1, P2 = 2147483647, 2147483629

# ---- build M_0 (in E) from c-params ; M_1.. generic from d-params -----------
def m0_from_params(Ebasis, cpar, p, dual_key=None):
    """cpar[k][j]; M_0[k][a][b] = sum_j cpar[k][j] E_j[a][b].
    dual_key=('c',k,j) sets that param's eps-part to 1 (returns duals array too)."""
    m = len(Ebasis)
    M = [[[0]*n for _ in range(n)] for _ in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for j in range(m):
            c = cpar[k][j] % p
            for a in range(n):
                for b in range(n):
                    if Ebasis[j][a][b]:
                        M[k][a][b] = (M[k][a][b] + c*Ebasis[j][a][b]) % p
    if dual_key and dual_key[0] == 'c':
        _, k, j = dual_key
        for a in range(n):
            for b in range(n):
                if Ebasis[j][a][b]:
                    D[k][a][b] = (D[k][a][b] + Ebasis[j][a][b]) % p
    return M, D

def generic_from_params(dpar, p, dual_key=None, tag='d'):
    """dpar[k][a][b] generic pencil; dual_key=(tag,k,a,b)."""
    M = [[[dpar[k][a][b] % p for b in range(n)] for a in range(n)] for k in range(R)]
    D = [[[0]*n for _ in range(n)] for _ in range(R)]
    if dual_key and dual_key[0] == tag:
        _, k, a, b = dual_key
        D[k][a][b] = 1
    return M, D

def gk_vector(Ms_and_duals, p, tcap, kwant, part):
    """Ms_and_duals = list of (Mj, Dj). Build entry, det, return g_kwant part-vec."""
    Ms = [x[0] for x in Ms_and_duals]
    Ds = [x[1] for x in Ms_and_duals]
    entry = pencils_to_entry(Ms, p, duals=Ds)
    det = det_arc(entry, p, tcap)
    if kwant not in det: return [0]*NQ
    return quartic_vec(det[kwant], p, part=part)

# ---- calibration 1 : dim D_5 = 50 = rank of dPhi at a generic pencil --------
def dim_D5(p, seed=1):
    rng = random.Random(seed)
    dpar = [[[rng.randint(1, p-1) for _ in range(n)] for _ in range(n)] for _ in range(R)]
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                M, D = generic_from_params(dpar, p, dual_key=('d', k, a, b))
                entry = pencils_to_entry([M], p, duals=[D])
                det = det_arc(entry, p, 0)             # order 0 : det M(s) itself
                cols.append(quartic_vec(det.get(0, {}), p, part=1))
    return rank_mod(cols, NQ, p)

# ---- calibration 2 & 3 : order-1 image + reducible border over a stratum ----
from flint import nmod_mat

def _g1_vec(Eb, cpar, dpar, p, dual_key=None):
    """g_1 = coeff of t^1 in det(M_0 + t M_1); optional single dual param."""
    if dual_key and dual_key[0] == 'c':
        M0, D0 = m0_from_params(Eb, cpar, p, dual_key=dual_key)
    else:
        M0, D0 = m0_from_params(Eb, cpar, p)
    if dual_key and dual_key[0] == 'd':
        M1, D1 = generic_from_params(dpar, p, dual_key=dual_key)
    else:
        M1, D1 = generic_from_params(dpar, p)
    entry = pencils_to_entry([M0, M1], p, duals=[D0, D1])
    det = det_arc(entry, p, 1)
    return det.get(1, {})

def make_V_point_order1(Eb, cpar, p, rng):
    """given M_0 (cpar), solve M_1 (80 params) so that g_1 in W (pi g_1 = 0)."""
    # columns : one per M_1 param ; rows : the 35 s_5-degree-0 coords of g_1.
    cols = []
    idxs = []
    zdpar = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                sp = _g1_vec(Eb, cpar, zdpar, p, dual_key=('d', k, a, b))
                v = quartic_vec(sp, p, part=1)
                cols.append([v[i] for i in S5DEG0]); idxs.append((k, a, b))
    nc = len(cols)
    A = nmod_mat(len(S5DEG0), nc,
                 [int(cols[j][r]) for r in range(len(S5DEG0)) for j in range(nc)], p)
    Xns, nul = A.nullspace()
    dpar = [[[0]*n for _ in range(n)] for _ in range(R)]
    for t in range(nul):
        w = rng.randint(1, p-1)
        for r, (k, a, b) in enumerate(idxs):
            dpar[k][a][b] = (dpar[k][a][b] + w*int(Xns[r, t])) % p
    return dpar, nul

def order1_stratum(name, p, seed=2):
    rng = random.Random(seed)
    Eb = stratum_E_basis(name, rng, p)
    m = len(Eb)
    cpar = [[rng.randint(1, p-1) for _ in range(m)] for _ in range(R)]     # M_0 in E
    dpar, nul = make_V_point_order1(Eb, cpar, p, rng)                      # M_1 : g_1 in W
    # Jacobian of g_1 wrt (cpar, dpar) at this V-point ; each column a 70-vec.
    cols = []
    params = [('c', k, j) for k in range(R) for j in range(m)] + \
             [('d', k, a, b) for k in range(R) for a in range(n) for b in range(n)]
    for pr in params:
        sp = _g1_vec(Eb, cpar, dpar, p, dual_key=pr)
        cols.append(quartic_vec(sp, p, part=1))
    dG = cols
    rk_full = rank_mod(dG, NQ, p)                             # tangent dim at V-point
    piG = [[row[i] for i in S5DEG0] for row in dG]
    rk_pi = rank_mod(piG, len(S5DEG0), p)
    # image dim (order-1, at a generic non-V point) for the separate anchor:
    return dict(name=name, dimE=m, Vnull=nul, tangent_at_V=rk_full,
                order1_reducible=rk_full - rk_pi)

def order1_image(name, p, seed=7):
    """order-1 image dim at a GENERIC point (anchor: fills D_5)."""
    rng = random.Random(seed)
    Eb = stratum_E_basis(name, rng, p)
    m = len(Eb)
    cpar = [[rng.randint(1, p-1) for _ in range(m)] for _ in range(R)]
    dpar = [[[rng.randint(1, p-1) for _ in range(n)] for _ in range(n)] for _ in range(R)]
    cols = []
    params = [('c', k, j) for k in range(R) for j in range(m)] + \
             [('d', k, a, b) for k in range(R) for a in range(n) for b in range(n)]
    for pr in params:
        sp = _g1_vec(Eb, cpar, dpar, p, dual_key=pr)
        cols.append(quartic_vec(sp, p, part=1))
    return rank_mod(cols, NQ, p)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--out', default='results/s59_calib.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    res = {'dim_D5': {}, 'order1': {}}
    for p in primes:
        d = dim_D5(p)
        res['dim_D5'][str(p)] = d
        print(f"[p={p}] dim D_5 = {d}   (expect 50)", flush=True)
    for p in primes:
        res['order1'][str(p)] = {}
        for name in STRATA:
            r = order1_stratum(name, p)
            img = order1_image(name, p)
            r['order1_image'] = img
            res['order1'][str(p)][name] = r
            print(f"[p={p}] {name:5s} dimE={r['dimE']:2d} "
                  f"order1_image={img:2d} (expect 50/50/47/47/49) "
                  f"reducible={r['order1_reducible']:2d} (expect 29/29/28/28/24) "
                  f"[tangent@V={r['tangent_at_V']}, Vnull={r['Vnull']}]",
                  flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
