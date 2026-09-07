#!/usr/bin/env python3
"""
Session 66 -- the rank-<=2 loci, where dPhi == 0 (the next incidence in the
audit's order after the primitive incidences).

A pencil of generic matrix rank <= 2 has adj M_0(s) == 0, so dPhi_{M_0} == 0:
every direction is a first-order kernel direction, the first-order theory is
void, and every arc from M_0 has contact order >= 2 with leading form
e_2(M_0; M_1), M_1 FREE (80 parameters).  This is where P cap ker and SP cap ker
live (any P- or SP-pencil with a common kernel has rank <= 2, since the kernel
then contains both the moving vector and the common one), and it is the one
place in B_5 where the exceptional fibre is a quadratic image of all of X_5.

Types (bounded matrix rank 2 in M_4) :  the compressions (2,0) [A(U_2)=0, dim 44],
(4,2) [im A <= W_2, dim 44], (3,1) [A(U_3) <= W_1, dim 41, self-transpose], and
the padded 3x3 skew type {P N(x) Q} (dim 30).

Over (2,0): e_2 = det[X | Y_2] with X = the two nonzero columns of M_0 and Y_2
the two columns of M_1 in the kernel directions -- an honest determinant, so
the order-2 image over (2,0) lies in Phi(X_5) and its reducible part in the
exact locus (<= 31).  Same for (4,2) by transposition.  Over (3,1), with
M_0 = [w l(s)^T | y(s)] (rank-1 block plus a free column), the rank-1 update
formula gives  e_2 = l^T adj([Y | y]) w = dPhi_{[Y|y]}(w l^T) : the tangent
vector of D_5 at the generic pencil N = [Y|y] along the rank-1 direction w l^T.

This module measures, over (3,1) (and (2,0) as a control):
  (i)  the dimension of the full order-2 image  {e_2(M_0(theta); M_1)}  (Jacobian
       rank over theta and M_1 at a generic point);
  (ii) the reducible order-2 image at V-points {pi e_2 = 0} constructed from
       M_1' (the s_1..s_4 slices) inside a compression space of the 4-pencil
       base locus containing M_0' = M_0|_{s_5=0} :
         (a) the (3,1) space itself,  (b) c32 with U_3 and W_2 in W_1,
         (c) c21 with U_2 in U_3 and W_1 ;
       by s59's identity rank d(g_2) - rank d(pi g_2) over (theta, M_1).
       These V-points need not be generic points of the V-variety, so the
       values are lower bounds for the components through them and are
       labelled as such.
"""
import sys, json, argparse, random, zlib
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import all_g, pencil_int, solve_aug

def family31(rng, p):
    """M_0(s) = [ e_0 l(s)^T | y(s) ] : theta = (l 5x3, y 5x4)."""
    theta0 = [rng.randint(1, p-1) for _ in range(15 + 20)]
    def build(th, Rg):
        pen = []
        for k in range(R):
            B = mat_zero(Rg, n, n)
            for b in range(3): B[0][b] = th[k*3 + b]
            for a in range(n): B[a][3] = th[15 + k*4 + a]
            pen.append(B)
        return pen
    return theta0, build

def family20(rng, p):
    """M_0(s) = [ 0 | 0 | X(s) ] : columns 0,1 zero (kernel U_2 = <e_0,e_1>)."""
    theta0 = [rng.randint(1, p-1) for _ in range(R*8)]
    def build(th, Rg):
        pen = []
        for k in range(R):
            B = mat_zero(Rg, n, n)
            for a in range(n):
                for b in (2, 3): B[a][b] = th[k*8 + a*2 + (b-2)]
            pen.append(B)
        return pen
    return theta0, build

def rand_pencil(rng, p, mask=None):
    pen = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                if mask is None or (a, b) in mask:
                    pen[k][a][b] = rng.randint(1, p-1)
    return pen

def jac_ranks(build, theta, M1, p, rows_of=None):
    """rank d(g_2) and rank d(pi g_2) over (theta, M_1) at (theta, M_1)."""
    zero = pencil_zero(Fp(p))
    full = []; con = []
    params = [('t', i) for i in range(len(theta))] + \
             [('m', 1, k, a, b) for k in range(R) for a in range(n) for b in range(n)]
    for pr in params:
        g1, g2 = all_g(build, theta, [M1, zero], 2, p, dual=pr)
        full.append(g2); con.append([g2[i] for i in S5DEG0])
    return rank_mod(full, NQ, p), rank_mod(con, len(S5DEG0), p)

def run31(p, seed, verbose=True):
    rng = random.Random(seed*104729 + 31)
    theta, build = family31(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    assert not any(det_value(M0, p))
    dP = dPhi_matrix(M0, p); assert dP.rank() == 0, "dPhi should vanish on the rank-2 locus"
    rec = dict(type='(3,1)', p=p, seed=seed, rank_dPhi=0)
    # (i) full order-2 image at a generic M_1
    M1 = rand_pencil(rng, p)
    g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
    assert not any(g1) and any(g2)
    rf, rc = jac_ranks(build, theta, M1, p)
    rec['order2_full_image'] = rf
    if verbose: print(f"[(3,1) p={p} seed={seed}] full order-2 image dim = {rf}", flush=True)
    # (ii) reducible : V-points of three compression types for M_1' (slices 0..3), slice 4 free
    Fpp = Fp(p)
    def vpoint(kind):
        M1 = [[[0]*n for _ in range(n)] for _ in range(R)]
        if kind == 'a':                     # (3,1) space : row 0 in cols 0..2, col 3 free
            mask = [(0, 0), (0, 1), (0, 2)] + [(a, 3) for a in range(n)]
        elif kind == 'b':                   # c32 : cols 0..2 in W_2 = <e_0, e_1>, col 3 free
            mask = [(a, b) for a in (0, 1) for b in (0, 1, 2)] + [(a, 3) for a in range(n)]
        elif kind == 'c':                   # c21 : U_2 = <e_0,e_1> into W_1 = <e_0>
            mask = [(0, 0), (0, 1)] + [(a, b) for a in range(n) for b in (2, 3)]
        for k in range(4):
            for (a, b) in mask: M1[k][a][b] = rng.randint(1, p-1)
        for a in range(n):
            for b in range(n): M1[4][a][b] = rng.randint(1, p-1)
        return M1
    rec['reducible'] = {}
    for kind in 'abc':
        M1 = vpoint(kind)
        g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
        okV = (not any(g1)) and (not any(g2[i] for i in S5DEG0))
        nz = any(g2)
        rf, rc = jac_ranks(build, theta, M1, p)
        rec['reducible'][kind] = dict(Vpoint_ok=okV, g2_nonzero=nz, rank_full=rf, rank_con=rc, dim=rf - rc)
        if verbose: print(f"   V-point type {kind}: ok={okV} g2!=0={nz}  rank_full={rf} rank_con={rc}  reducible order-2 image >= {rf-rc}", flush=True)
    return rec

def run20(p, seed, verbose=True):
    rng = random.Random(seed*104729 + 20)
    theta, build = family20(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    assert not any(det_value(M0, p))
    dP = dPhi_matrix(M0, p); assert dP.rank() == 0
    M1 = rand_pencil(rng, p)
    rf, rc = jac_ranks(build, theta, M1, p)
    rec = dict(type='(2,0)', p=p, seed=seed, rank_dPhi=0, order2_full_image=rf)
    if verbose: print(f"[(2,0) p={p} seed={seed}] full order-2 image dim = {rf}  (dim D_5 = 50; exact locus expected)", flush=True)
    # reducible : M_1 with columns 0,1 (kernel directions) chosen so that the 4-variable
    # determinant det[X' | Y_2'] vanishes : e.g. Y_2' with image in a hyperplane
    # containing im X' ... simplest V-points: Y_2 columns in U_2-compression of
    # the 4-pencil [X|Y_2] -> take Y_2'(s') = X'(s') A (columns in the span of X's)
    M1 = rand_pencil(rng, p)
    A = [[rng.randint(1, p-1) for _ in range(2)] for _ in range(2)]
    for k in range(4):
        for a in range(n):
            for b in (0, 1):
                M1[k][a][b] = sum(M0[k][a][2 + j]*A[j][b] for j in range(2)) % p
    g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
    okV = (not any(g1)) and (not any(g2[i] for i in S5DEG0))
    rf, rc = jac_ranks(build, theta, M1, p)
    rec['reducible'] = dict(Vpoint_ok=okV, g2_nonzero=any(g2), rank_full=rf, rank_con=rc, dim=rf - rc)
    if verbose: print(f"   V-point: ok={okV} g2!=0={any(g2)}  reducible order-2 image >= {rf-rc}", flush=True)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s66_rank2.json')
    a = ap.parse_args()
    primes = HOUSE if a.primes == 'both' else [int(x) for x in a.primes.split(',')]
    res = []
    for p in primes:
        for seed in [int(x) for x in a.seeds.split(',')]:
            res.append(run20(p, seed)); res.append(run31(p, seed))
            json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

# ----------------------------------------------------------------------
# Exactness identities on the rank-<=2 compression loci (verified numerically here,
# proved in the report by Laplace expansion / the rank-1 update formula):
#   (3,1)  M_0 = [ e_0 l(s)^T | y(s) ],  M_1 = [ Y | y_1 ] :
#          e_2(M_0; M_1) = det( N~ ),  N~ = the pencil with row 0 = (l_0, l_1, l_2, 0)
#          and rows 1..3 = rows 1..3 of [ Y | y ]       -- an exact 4x4 determinant.
#   (2,0)  M_0 = [ 0 | 0 | X(s) ],  M_1 = [ Y_2 | * ] :
#          e_2(M_0; M_1) = det( [ Y_2 | X ] )          -- an exact 4x4 determinant.
def verify_exactness(p, seed, verbose=True):
    rng = random.Random(seed*7 + 99)
    out = {}
    # (3,1)
    theta, build = family31(rng, p)
    M0 = pencil_int(build(theta, Fp(p))); M1 = rand_pencil(rng, p)
    g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
    Nt = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for b in range(3): Nt[k][0][b] = M0[k][0][b]           # row 0 = l(s), (0,3) = 0
        for a in (1, 2, 3):
            for b in range(3): Nt[k][a][b] = M1[k][a][b]       # rows 1..3 of Y
            Nt[k][a][3] = M0[k][a][3]                          # rows 1..3 of y
    out['(3,1)'] = (g2 == det_value(Nt, p))
    # (2,0)
    theta, build = family20(rng, p)
    M0 = pencil_int(build(theta, Fp(p))); M1 = rand_pencil(rng, p)
    g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
    Nt = [[[0]*n for _ in range(n)] for _ in range(R)]
    for k in range(R):
        for a in range(n):
            for b in (0, 1): Nt[k][a][b] = M1[k][a][b]         # Y_2 : columns 0,1 of M_1
            for b in (2, 3): Nt[k][a][b] = M0[k][a][b]         # X   : columns 2,3 of M_0
    out['(2,0)'] = (g2 == det_value(Nt, p))
    if verbose: print(f"[exactness p={p} seed={seed}] e_2 = explicit determinant : {out}", flush=True)
    return out

# ----------------------------------------------------------------------
# the padded 3x3 skew type (rank 2, dim 30) : M_0 = P diag(N(x(s)), 0) Q, in the
# standard frame theta = x (5x3).  Order-2 image and the reducible image at the
# V-points m, b proportional to s_5 (and m, c proportional to s_5).
def family_skew(rng, p):
    theta0 = [rng.randint(1, p-1) for _ in range(15)]
    def build(th, Rg):
        pen = []
        for k in range(R):
            x = [th[k*3 + j] for j in range(3)]
            N3 = skewN(Rg, x)
            B = mat_zero(Rg, n, n)
            for a in range(3):
                for b in range(3): B[a][b] = N3[a][b]
            pen.append(B)
        return pen
    return theta0, build

def run_skew(p, seed, verbose=True):
    rng = random.Random(seed*104729 + 7)
    theta, build = family_skew(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    assert not any(det_value(M0, p))
    dP = dPhi_matrix(M0, p); assert dP.rank() == 0
    rec = dict(type='skew-padded', p=p, seed=seed, rank_dPhi=0)
    # group directions must be added to theta for the image dimension : the family
    # in the standard frame is 15-dim, the locus 30-dim (frames).  The image of the
    # standard-frame family already carries the GL_4 x GL_4 action through M_1
    # (conjugating M_0 and M_1 together only rescales e_2), so the frame is WLOG.
    M1 = rand_pencil(rng, p)
    rf, rc = jac_ranks(build, theta, M1, p)
    rec['order2_full_image'] = rf
    if verbose: print(f"[skew p={p} seed={seed}] full order-2 image dim = {rf}", flush=True)
    rec['reducible'] = {}
    for kind in ('mb', 'mc'):
        M1 = rand_pencil(rng, p)
        # m = corner (3,3), b = column 3 rows 0..2, c = row 3 cols 0..2 : make them
        # proportional to s_5 (zero in slices 0..3)
        for k in range(4):
            M1[k][3][3] = 0
            if kind == 'mb':
                for a in range(3): M1[k][a][3] = 0
            else:
                for b in range(3): M1[k][3][b] = 0
        g1, g2 = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
        okV = (not any(g1)) and (not any(g2[i] for i in S5DEG0))
        rf, rc = jac_ranks(build, theta, M1, p)
        rec['reducible'][kind] = dict(Vpoint_ok=okV, g2_nonzero=any(g2), rank_full=rf, rank_con=rc, dim=rf - rc)
        if verbose: print(f"   V-point ({kind} ~ s_5): ok={okV} g2!=0={any(g2)} rank_full={rf} rank_con={rc} reducible order-2 image = {rf-rc}", flush=True)
    return rec

if __name__ == '__main__' and '--skew' in sys.argv:
    pass

# ----------------------------------------------------------------------
# skew-padded type, complete order-2 V-variety and order-3 arcs.
# In the standard frame M_0 = diag(N(x(s)), 0) and, writing M_1 in blocks
# [[A, b],[c^T, m]] (A 3x3, b, c in C^3, m scalar; all linear in s),
#     e_2(M_0; M_1) = m (x^T A x) - (x^T b)(c^T x) = m q - beta gamma.
# pi e_2 = 0 <=> m'q' = beta'gamma' in F[s_1..s_4]; m' linear and the ring a UFD, so
# the V-variety is the union of FOUR explicit components:
#   (i)   m' = 0, beta' = 0   <=> M_1' e_3 = 0      (common kernel with M_0')
#   (ii)  m' = 0, gamma' = 0  <=> e_3^T M_1' = 0    (common cokernel)
#   (iii) M_1' = v w(s')^T, v = (beta'', 1) fixed   (rank-1 pencil, fixed column)
#   (iv)  M_1' = w(s') v^T                          (rank-1 pencil, fixed row)
# The same factorisation in five variables describes {e_2 == 0}, the directions
# from which an arc can have contact order 3:  the four types with the
# conditions imposed on all five slices.
def skew_vpoint(kind, rng, p):
    M1 = rand_pencil(rng, p)
    if kind in ('i', 'ii'):
        for k in range(4):
            M1[k][3][3] = 0
            for a in range(3):
                if kind == 'i': M1[k][a][3] = 0
                else: M1[k][3][a] = 0
    elif kind in ('iii', 'iv'):
        v = [rng.randint(1, p-1) for _ in range(3)] + [1]
        for k in range(4):
            w = [rng.randint(1, p-1) for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    M1[k][a][b] = (v[a]*w[b] if kind == 'iii' else w[a]*v[b]) % p
    return M1

def skew_e2zero_dir(kind, rng, p):
    """M_1 with e_2(M_0; M_1) == 0 in all five variables (same four types, all slices)."""
    M1 = rand_pencil(rng, p)
    if kind in ('i', 'ii'):
        for k in range(R):
            M1[k][3][3] = 0
            for a in range(3):
                if kind == 'i': M1[k][a][3] = 0
                else: M1[k][3][a] = 0
    else:
        v = [rng.randint(1, p-1) for _ in range(3)] + [1]
        for k in range(R):
            w = [rng.randint(1, p-1) for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    M1[k][a][b] = (v[a]*w[b] if kind == 'iii' else w[a]*v[b]) % p
    return M1

def run_skew_full(p, seed, verbose=True):
    rng = random.Random(seed*104729 + 8)
    theta, build = family_skew(rng, p)
    M0 = pencil_int(build(theta, Fp(p)))
    assert dPhi_matrix(M0, p).rank() == 0
    zero = pencil_zero(Fp(p))
    rec = dict(type='skew-padded', p=p, seed=seed, order2={}, order3={})
    for kind in ('i', 'ii', 'iii', 'iv'):
        M1 = skew_vpoint(kind, rng, p)
        g1, g2 = all_g(build, theta, [M1, zero], 2, p)
        okV = (not any(g1)) and (not any(g2[i] for i in S5DEG0))
        rf, rc = jac_ranks(build, theta, M1, p)
        rec['order2'][kind] = dict(Vpoint_ok=okV, g2_nonzero=any(g2), rank_full=rf, rank_con=rc, dim=rf-rc)
        if verbose: print(f"[skew p={p} seed={seed}] order-2 component ({kind}): ok={okV} g2!=0={any(g2)} "
                          f"rank_full={rf} rank_con={rc} reducible image = {rf-rc}", flush=True)
    # order 3 : M_1 with e_2 == 0 (four types), M_2 solving pi g_3 = 0 (affine-linear in M_2)
    for kind in ('i', 'ii', 'iii', 'iv'):
        M1 = skew_e2zero_dir(kind, rng, p)
        g1, g2, g3c = all_g(build, theta, [M1, zero, zero], 3, p)
        assert not any(g1) and not any(g2), "e_2 not zero for this direction"
        const = [g3c[i] for i in S5DEG0]
        cols = []
        for k in range(R):
            for a in range(n):
                for b in range(n):
                    g = all_g(build, theta, [M1, zero, zero], 3, p, dual=('m', 2, k, a, b))[2]
                    cols.append([g[i] for i in S5DEG0])
        part = solve_aug(cols, const, len(S5DEG0), p)
        if part is None:
            rec['order3'][kind] = dict(note='pi g_3 = 0 unsolvable at a generic M_1 of this type')
            if verbose: print(f"   order-3 ({kind}): pi g_3 = 0 not solvable for generic M_1 of this type", flush=True)
            continue
        m2v = [v % p for v in part]
        X, nul = nmod_mat(len(S5DEG0), 80, [int(cols[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
        for t in range(nul):
            w = rng.randint(1, p-1)
            for r_ in range(80): m2v[r_] = (m2v[r_] + w*int(X[r_, t])) % p
        M2 = vec_pencil(m2v)
        g1, g2, g3 = all_g(build, theta, [M1, M2, zero], 3, p)
        okV = (not any(g1)) and (not any(g2)) and (not any(g3[i] for i in S5DEG0))
        # identity over (theta, M_1, M_2) : rank d(g_2, g_3) - rank d(g_2, pi g_3)   (g_1 == 0 identically)
        full = []; con = []
        params = [('t', i) for i in range(len(theta))] + \
                 [('m', j, k, a, b) for j in (1, 2) for k in range(R) for a in range(n) for b in range(n)]
        for pr in params:
            gg = all_g(build, theta, [M1, M2, zero], 3, p, dual=pr)
            full.append(gg[1] + gg[2]); con.append(gg[1] + [gg[2][i] for i in S5DEG0])
        rf = rank_mod(full, 2*NQ, p); rc = rank_mod(con, NQ + len(S5DEG0), p)
        rec['order3'][kind] = dict(Vpoint_ok=okV, g3_nonzero=any(g3), rank_full=rf, rank_con=rc, dim=rf-rc)
        if verbose: print(f"   order-3 ({kind}): ok={okV} g3!=0={any(g3)} rank_full={rf} rank_con={rc} reducible image = {rf-rc}", flush=True)
    return rec
