#!/usr/bin/env python3
"""
Session 66 -- section 3C : the reducible exceptional image over an incidence
locus Z of the base locus, at contact order q, by s59's identity

    dim{[g_q / s_5]} at a generic V-point  =  rank d(g_1..g_q) - rank d(g_1..g_{q-1}, pi g_q)

where now M_0 = M_0(theta) ranges over a PARAMETRISED family Z (an incidence
locus or a special locus), and the Jacobian is taken with respect to theta and
the jets M_1..M_q.  theta-derivatives by dual numbers through the family
builder (the builders are written over an abstract ring, wk10_s66_core).

Order 1 needs only pi g_1 = 0 (M_1 generic in ker(pi dPhi)).  Order 2 needs
M_1 in ker dPhi with pi e_2(M_0;M_1) in pi(im dPhi) -- automatic at smooth
points of the base scheme (there every kernel direction extends to a curve in
the base locus, and the order-2 leading forms are then the order-1 ones
again), NOT automatic at incidence points, where it is the quadric system
Q_2^pi (the audit's '23 quadrics' at c21 cap c32 = 35 - rank(pi dPhi)).  This
module computes the order-1 image over Z and exports Q_2^pi (and Q_2) in
kernel coordinates for the CAS stage (wk10_s66_cas.py).
"""
import sys, random, argparse, json, zlib
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *

# ----------------------------------------------------------------------
# families : spec -> (theta0 (list of ints), builder(theta, Rg) -> pencil)
def _mat(theta, off, r, c):
    return [[theta[off + i*c + j] for j in range(c)] for i in range(r)]

def family(spec, rng, p):
    """standard frames (no conjugation: the image dimension is GL_4 x GL_4
    invariant); u, x, c random so the pencil is generic relative to s_5."""
    rnd = lambda m: [rng.randint(1, p-1) for _ in range(m)]
    if spec == 'P':
        theta0 = rnd(24 + 20)
        def build(th, Rg):
            phi = _mat(th, 0, n, 6); u = _mat(th, 24, R, n)
            return prim_point(Rg, phi, u)[0]
    elif spec == 'P_coker':                     # phi = psi rho, rank 3
        theta0 = rnd(12 + 18 + 20)
        def build(th, Rg):
            psi = _mat(th, 0, n, 3); rho = _mat(th, 12, 3, 6); u = _mat(th, 30, R, n)
            return prim_point(Rg, mat_mul(Rg, psi, rho), u)[0]
    elif spec == 'P_ker':                       # ker phi = e_0 ^ C^4 : phi supported on slots with b >= 1
        slots = [si for si, (b, c) in enumerate(PAIRS) if b >= 1]
        theta0 = rnd(n*len(slots) + 20)
        def build(th, Rg):
            phi = [[Rg.zero()]*6 for _ in range(n)]
            t = 0
            for a in range(n):
                for si in slots:
                    phi[a][si] = th[t]; t += 1
            u = _mat(th, t, R, n)
            return prim_point(Rg, phi, u)[0]
    elif spec == 'P_SP':                        # u = v w, rank 3
        theta0 = rnd(24 + 15 + 12)
        def build(th, Rg):
            phi = _mat(th, 0, n, 6); v = _mat(th, 24, R, 3); w = _mat(th, 39, 3, n)
            return prim_point(Rg, phi, mat_mul(Rg, v, w))[0]
    elif spec == 'P_c21':                       # u = v w, rank 2
        theta0 = rnd(24 + 10 + 8)
        def build(th, Rg):
            phi = _mat(th, 0, n, 6); v = _mat(th, 24, R, 2); w = _mat(th, 34, 2, n)
            return prim_point(Rg, phi, mat_mul(Rg, v, w))[0]
    elif spec == 'P_c32':                       # im u = <e_0,e_1,e_2>, phi(e_0^e_1) = 0
        s01 = PAIRS.index((0, 1))
        theta0 = rnd(n*5 + 15)
        def build(th, Rg):
            phi = [[Rg.zero()]*6 for _ in range(n)]
            t = 0
            for a in range(n):
                for si in range(6):
                    if si == s01: continue
                    phi[a][si] = th[t]; t += 1
            v = _mat(th, t, R, 3)
            u = [[v[k][0], v[k][1], v[k][2], Rg.zero()] for k in range(R)]
            return prim_point(Rg, phi, u)[0]
    elif spec in ('P_tan', 'P_meet'):           # phi rows in the annihilator of K
        Rg0 = Fp(p)
        def pl(b, c):
            v = [0]*6; v[PAIRS.index((b, c))] = 1; return v
        e12, e13, e24 = pl(0, 1), pl(0, 2), pl(1, 3)
        k1 = e12; k2 = e13 if spec == 'P_meet' else [x + y for x, y in zip(e13, e24)]
        Km = nmod_mat(2, 6, [x % p for x in k1] + [x % p for x in k2], p)
        NS, nul = Km.nullspace(); assert nul == 4
        ann = [[int(NS[i, j]) for i in range(6)] for j in range(4)]
        theta0 = rnd(n*4 + 20)
        def build(th, Rg):
            phi = []
            for a in range(n):
                row = [Rg.zero()]*6
                for j in range(4):
                    for i in range(6):
                        if ann[j][i]:
                            row[i] = Rg.add(row[i], Rg.mul(th[a*4 + j], Rg.from_int(ann[j][i])))
                phi.append(row)
            u = _mat(th, 16, R, n)
            return prim_point(Rg, phi, u)[0]
    elif spec == 'SP':
        theta0 = rnd(12 + 15 + 20)
        def build(th, Rg):
            phi = _mat(th, 0, n, 3); x = _mat(th, 12, R, 3); c = _mat(th, 27, R, n)
            I4 = [[Rg.one() if i == j else Rg.zero() for j in range(n)] for i in range(n)]
            return sp_point(Rg, phi, x, c, I4, I4)[0]
    elif spec == 'SP_c32':                      # phi = psi rho rank 2
        theta0 = rnd(8 + 6 + 15 + 20)
        def build(th, Rg):
            psi = _mat(th, 0, n, 2); rho = _mat(th, 8, 2, 3)
            x = _mat(th, 14, R, 3); c = _mat(th, 29, R, n)
            I4 = [[Rg.one() if i == j else Rg.zero() for j in range(n)] for i in range(n)]
            return sp_point(Rg, mat_mul(Rg, psi, rho), x, c, I4, I4)[0]
    elif spec == 'SP_c21':                      # x = v w rank 2
        theta0 = rnd(12 + 10 + 6 + 20)
        def build(th, Rg):
            phi = _mat(th, 0, n, 3); v = _mat(th, 12, R, 2); w = _mat(th, 22, 2, 3)
            c = _mat(th, 28, R, n)
            I4 = [[Rg.one() if i == j else Rg.zero() for j in range(n)] for i in range(n)]
            return sp_point(Rg, phi, mat_mul(Rg, v, w), c, I4, I4)[0]
    elif spec == 'SP_ker':                      # c_k = phi N(x_k) w
        theta0 = rnd(12 + 15 + 3)
        def build(th, Rg):
            phi = _mat(th, 0, n, 3); x = _mat(th, 12, R, 3); w = th[27:30]
            c = []
            for k in range(R):
                L = mat_mul(Rg, phi, skewN(Rg, x[k]))
                c.append([sum_ring(Rg, [Rg.mul(L[a][j], w[j]) for j in range(3)]) for a in range(n)])
            I4 = [[Rg.one() if i == j else Rg.zero() for j in range(n)] for i in range(n)]
            return sp_point(Rg, phi, x, c, I4, I4)[0]
    elif spec == 'SP_coker':                    # c = phi c'
        theta0 = rnd(12 + 15 + 15)
        def build(th, Rg):
            phi = _mat(th, 0, n, 3); x = _mat(th, 12, R, 3); cp = _mat(th, 27, R, 3)
            c = [[sum_ring(Rg, [Rg.mul(phi[a][j], cp[k][j]) for j in range(3)]) for a in range(n)]
                 for k in range(R)]
            I4 = [[Rg.one() if i == j else Rg.zero() for j in range(n)] for i in range(n)]
            return sp_point(Rg, phi, x, c, I4, I4)[0]
    elif spec in ('ker', 'coker', 'c21', 'c32', 'c21_c32', 'ker_coker', 'ker_c21', 'c32_coker'):
        if '_' in spec:
            a_, b_ = spec.split('_')
            mask = [ab for ab in comp_mask(a_) if ab in comp_mask(b_)]
        else:
            mask = comp_mask(spec)
        theta0 = rnd(R*len(mask))
        def build(th, Rg):
            pen = []
            for k in range(R):
                B = mat_zero(Rg, n, n)
                for i, (a, b) in enumerate(mask): B[a][b] = th[k*len(mask) + i]
                pen.append(B)
            return pen
    else:
        raise ValueError(spec)
    return theta0, build

# ----------------------------------------------------------------------
def pencil_int(pen_ring, part=0):
    return [[[ (x[part] if isinstance(x, tuple) else (x if part == 0 else 0)) for x in row]
             for row in B] for B in pen_ring]

def all_g(build, theta, jets, q, p, dual=None):
    """[g_1..g_q] as 70-vectors : value parts, or dual parts if dual = ('t', i)
    (theta direction) or ('m', j, k, a, b) (jet entry)."""
    if dual and dual[0] == 't':
        Rg = FpEps(p, 2)
        th = [Rg.lift(t, 1 if i == dual[1] else 0) for i, t in enumerate(theta)]
        penE = build(th, Rg)
        M0 = pencil_int(penE, 0); D0 = pencil_int(penE, 1)
    else:
        M0 = pencil_int(build(theta, Fp(p)), 0); D0 = None
    Ms = [M0] + [ [[[jets[j][k][a][b] % p for b in range(n)] for a in range(n)] for k in range(R)]
                 for j in range(q)]
    Ds = [D0] + [None]*q
    if dual and dual[0] == 'm':
        _, j, k, a, b = dual
        D = [[[0]*n for _ in range(n)] for _ in range(R)]; D[k][a][b] = 1
        Ds[j] = D
    entry = pencils_to_entry(Ms, p, duals=Ds if any(d is not None for d in Ds) else None)
    det = det_arc(entry, p, q)
    part = 1 if dual else 0
    return [quartic_vec(det.get(j, {}), p, part=part) for j in range(1, q+1)]

def solve_aug(cols, const, nrows, p):
    """x with sum_j x_j cols[j] = -const ; None if impossible."""
    m = len(cols)
    Aug = nmod_mat(nrows, m+1, [int(cols[j][r]) if j < m else int(const[r]) % p
                                for r in range(nrows) for j in range(m+1)], p)
    X, nul = Aug.nullspace()
    for t in range(nul):
        last = int(X[m, t]) % p
        if last:
            inv = pow(last, p-2, p)
            return [(int(X[r, t]) * inv) % p for r in range(m)]
    return None

def order1_image(spec, p, seed, verbose=True):
    """order-1 reducible image over the family Z : rank d(g_1) - rank d(pi g_1)
    at a generic V-point (theta generic, M_1 generic with pi g_1 = 0)."""
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    assert not any(det_value(M0, p)), "det not zero on the family"
    dP = dPhi_matrix(M0, p)
    rk = dP.rank()
    # M_1 generic in ker(pi dPhi) : rows S5DEG0 of dP
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    X, nul = piP.nullspace()
    m1v = [0]*80
    for t in range(nul):
        w = rng.randint(1, p-1)
        for r in range(80): m1v[r] = (m1v[r] + w*int(X[r, t])) % p
    M1 = vec_pencil(m1v)
    g1 = all_g(build, theta, [M1], 1, p)[0]
    assert not any(g1[i] for i in S5DEG0), "V-point : pi g_1 != 0"
    nonzero = any(g1)
    # Jacobian over theta and M_1
    rows_full = []; rows_con = []
    for i in range(len(theta)):
        g = all_g(build, theta, [M1], 1, p, dual=('t', i))[0]
        rows_full.append(g); rows_con.append([g[j] for j in S5DEG0])
    for k in range(R):
        for a in range(n):
            for b in range(n):
                g = all_g(build, theta, [M1], 1, p, dual=('m', 1, k, a, b))[0]
                rows_full.append(g); rows_con.append([g[j] for j in S5DEG0])
    rf = rank_mod(rows_full, NQ, p); rc = rank_mod(rows_con, len(S5DEG0), p)
    rec = dict(spec=spec, p=p, seed=seed, ntheta=len(theta), rank_dPhi=rk, dim_ker=80-rk,
               dim_ker_pi=nul, g1_nonzero=nonzero, rank_full=rf, rank_con=rc,
               order1_reducible=rf - rc)
    if verbose:
        print(f"[{spec} p={p} seed={seed}] rank dPhi={rk} ker={80-rk} ker(pi dPhi)={nul} "
              f"g1!=0:{nonzero}  rank_full={rf} rank_con={rc}  order-1 reducible = {rf-rc}", flush=True)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default='ker,coker,c21,c32,P,SP,ker_coker,c21_c32,ker_c21,c32_coker,'
                    'P_coker,P_ker,P_SP,P_c21,P_c32,P_tan,P_meet,SP_c32,SP_c21,SP_ker,SP_coker')
    ap.add_argument('--primes', default='both')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s66_order1.json')
    a = ap.parse_args()
    primes = HOUSE if a.primes == 'both' else [int(x) for x in a.primes.split(',')]
    res = []
    for spec in a.specs.split(','):
        for p in primes:
            for seed in [int(x) for x in a.seeds.split(',')]:
                res.append(order1_image(spec, p, seed))
                json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)
