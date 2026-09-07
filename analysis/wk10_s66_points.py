#!/usr/bin/env python3
"""
Session 66 -- point constructions for the tangent table.

A 'point spec' names a locus of B_5 and builds, from a seed and a prime,
  (a) the pencil M_0 (five 4x4 matrices over F_p),
  (b) for every component of B_5 known to pass through M_0, a list of tangent
      vectors at M_0 (each a pencil), obtained from that component's own
      parametrisation re-expressed at M_0, plus the group directions,
  (c) for components whose parametrisation may not be submersive at M_0, a
      'curve' : the same parametrisation over F_p[eps]/eps^K along a random
      direction into the component's generic locus, for the limit tangent space.

Every tangent vector is later checked to annihilate dPhi (KC2).
"""
import sys, random, zlib
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *

# ----------------------------------------------------------------------
# linear-algebra helpers over F_p ints
def mat_inv(A, p):
    m = len(A)
    M = nmod_mat(m, m, [int(x) % p for row in A for x in row], p)
    Mi = M.inv()
    return [[int(Mi[i, j]) for j in range(m)] for i in range(m)]

def complete_basis(vecs, rng, p, dim=4):
    """extend a list of independent vectors (len dim) to a basis; return the
    matrix g whose COLUMNS are the basis (first columns = vecs)."""
    cols = [list(v) for v in vecs]
    while len(cols) < dim:
        cand = [rng.randint(1, p-1) for _ in range(dim)]
        test = cols + [cand]
        if rank_mod(test, dim, p) == len(test):
            cols.append(cand)
    g = [[cols[j][i] % p for j in range(dim)] for i in range(dim)]
    return g

def common_kernel(pen, p):
    rows = [pen[k][a] for k in range(R) for a in range(n)]        # 20 x 4
    A = nmod_mat(len(rows), n, [int(x) % p for r in rows for x in r], p)
    return kernel_basis(A)                                          # list of 4-vectors

def common_cokernel(pen, p):
    """functionals v with v^T B_k = 0 for all k : nullspace of [B_1 .. B_5]^T stacked."""
    rows = []
    for k in range(R):
        for b in range(n):
            rows.append([pen[k][a][b] for a in range(n)])            # column b of B_k
    A = nmod_mat(len(rows), n, [int(x) % p for r in rows for x in r], p)
    return kernel_basis(A)

def image_span(pen, p):
    """basis of sum_k im B_k."""
    cols = [[pen[k][a][b] for a in range(n)] for k in range(R) for b in range(n)]
    A = nmod_mat(len(cols), n, [int(x) % p for c in cols for x in c], p)
    rr = A.rref()[0]
    out = []
    for i in range(A.nrows()):
        row = [int(rr[i, j]) for j in range(n)]
        if any(row): out.append(row)
    return out

def col_span(M, p):
    """basis of the column span of a matrix M (list of rows)."""
    cols = [[M[a][j] for a in range(len(M))] for j in range(len(M[0]))]
    A = nmod_mat(len(cols), len(M), [int(x) % p for c in cols for x in c], p)
    rr = A.rref()[0]
    out = []
    for i in range(A.nrows()):
        row = [int(rr[i, j]) for j in range(len(M))]
        if any(row): out.append(row)
    return out

def hyperplane_basis(v, rng, p):
    """basis (3 vectors) of v^perp in C^4."""
    A = nmod_mat(1, n, [int(x) % p for x in v], p)
    return kernel_basis(A)

def comp_tangent(name, g, h, pen, p):
    """tangent vectors of a compression component at pen, flag given by
    g (columns: U-adapted basis of the source) and h (columns: W-adapted basis
    of the target) : directions h E_ab g^{-1} on every slot, plus group dirs."""
    Rg = Fp(p)
    gi = mat_inv(g, p)
    mask = comp_mask(name)
    tang = []
    for k in range(R):
        for (a, b) in mask:
            E = mat_zero(Rg, n, n); E[a][b] = 1
            d = pencil_zero(Rg); d[k] = mat_mul(Rg, mat_mul(Rg, h, E), gi)
            tang.append(d)
    tang += group_directions(Rg, pen)
    return tang

# ----------------------------------------------------------------------
# P-side helpers
def prim_conj(Rg, phi, u, h, g, p):
    """(phi, u) -> (h phi Lambda^2 g, u g^{-1}) : pencil becomes h M g."""
    phi2 = mat_mul(Rg, h, mat_mul(Rg, phi, lambda2(Rg, g)))
    gi = mat_inv(g, p)
    u2 = [[sum_ring(Rg, [Rg.mul(gi[a][b], u[k][b]) for b in range(n)]) for a in range(n)]
          for k in range(R)]
    return phi2, u2

def prim_curve(phi, u, rng, p, K=4):
    """the P-parametrisation over F_p[eps]/eps^K along a random direction."""
    Rg = FpEps(p, K)
    phiE = [[Rg.lift(phi[a][s], rng.randint(1, p-1)) for s in range(6)] for a in range(n)]
    uE = [[Rg.lift(u[k][c], rng.randint(1, p-1)) for c in range(n)] for k in range(R)]
    pen, tang = prim_point(Rg, phiE, uE)
    return pen, tang

def sp_frame_from_prim(phi, u, Y, rng, p):
    """M_0 = M_phi(u(s)) with im u = span(Y) (Y : list of 3 vectors).  Return
    SP parameters (phi43, x, c, P=I, Q) with pen = [phi43 N(x) | c] Q."""
    Rg = Fp(p)
    g = complete_basis(Y, rng, p)                # columns y_1,y_2,y_3,e4'
    gi = mat_inv(g, p)
    # x_k : coordinates of u_k in the basis g (first three coords; the 4th must be 0)
    x = []
    for k in range(R):
        coords = [sum(gi[i][b]*u[k][b] for b in range(n)) % p for i in range(n)]
        assert coords[3] == 0, "u_k not in span(Y)"
        x.append(coords[:3])
    # phi43 e_k = phi(y_i ^ y_j) for (i,j,k) cyclic : phi43 column k
    def phi_wedge(yi, yj):
        # Pluecker coords of yi ^ yj over PAIRS, then phi applied
        w = [(yi[b]*yj[c] - yi[c]*yj[b]) % p for (b, c) in PAIRS]
        return [sum(phi[a][s]*w[s] for s in range(6)) % p for a in range(n)]
    # M_phi(y) t = phi(t ^ y) in the s59 convention, so M_phi(u) y_j = sum_i x_i phi(y_j ^ y_i)
    cols = [phi_wedge(Y[2], Y[1]), phi_wedge(Y[0], Y[2]), phi_wedge(Y[1], Y[0])]
    phi43 = [[cols[k][a] for k in range(3)] for a in range(n)]
    # c_k = B_k g e_4 = M_phi(u_k) y4
    y4 = [g[a][3] for a in range(n)]
    c = []
    for k in range(R):
        Mk = M_phi(Rg, phi, u[k])
        c.append([sum(Mk[a][b]*y4[b] for b in range(n)) % p for a in range(n)])
    I4 = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return dict(phi=phi43, x=x, c=c, P=I4, Q=gi)

def sp_curve(par, rng, p, K=4, c_free=True):
    Rg = FpEps(p, K)
    phiE = [[Rg.lift(par['phi'][a][j], rng.randint(1, p-1)) for j in range(3)] for a in range(n)]
    xE = [[Rg.lift(par['x'][k][j], rng.randint(1, p-1)) for j in range(3)] for k in range(R)]
    cE = [[Rg.lift(par['c'][k][a], rng.randint(1, p-1) if c_free else 0) for a in range(n)] for k in range(R)]
    PE = [[Rg.from_int(par['P'][a][b]) for b in range(n)] for a in range(n)]
    QE = [[Rg.from_int(par['Q'][a][b]) for b in range(n)] for a in range(n)]
    return sp_point(Rg, phiE, xE, cE, PE, QE)

# ----------------------------------------------------------------------
def build_point(spec, seed, p):
    """returns dict(pen, comps={name: tangent vectors}, curves={name: (pen_eps, tang_eps)},
    info={...})"""
    Rg = Fp(p); rng = random.Random(seed * 1000003 + zlib.crc32(spec.encode()) % 1000)
    comps = {}; curves = {}; info = {}
    if spec in ('P_gen', 'PT_gen'):
        pt = prim_random(Rg, rng, p)
        pen, tang = prim_point(Rg, pt['phi'], pt['u'], transpose=(spec == 'PT_gen'))
        comps['P' if spec == 'P_gen' else 'PT'] = tang
    elif spec in ('SP_gen', 'SPT_gen'):
        pt = sp_random(Rg, rng, p)
        pen, tang = sp_point(Rg, pt['phi'], pt['x'], pt['c'], pt['P'], pt['Q'],
                             transpose=(spec == 'SPT_gen'))
        comps['SP' if spec == 'SP_gen' else 'SPT'] = tang
    elif spec == 'P_coker':
        pt = prim_random(Rg, rng, p, phi_rank=3)
        pen, tang = prim_point(Rg, pt['phi'], pt['u'])
        comps['P'] = tang
        cok = common_cokernel(pen, p); assert len(cok) == 1, cok
        W = hyperplane_basis(cok[0], rng, p)
        # coker mask has row 0 zero : convention h(e_1,e_2,e_3) = W  -> W in columns 1..3
        extra = complete_basis(W, rng, p)          # columns: W then one extra
        cols = [[extra[a][3] for a in range(n)]] + [[extra[a][j] for a in range(n)] for j in range(3)]
        h = [[cols[j][a] for j in range(n)] for a in range(n)]
        g = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        comps['coker'] = comp_tangent('coker', g, h, pen, p)
        curves['P'] = prim_curve(pt['phi'], pt['u'], rng, p)
        info['rank_phi'] = 3
    elif spec == 'P_ker':
        pt = prim_kerinc(Rg, rng, p)
        pen, tang = prim_point(Rg, pt['phi'], pt['u'])
        comps['P'] = tang
        kerv = common_kernel(pen, p); assert len(kerv) == 1, kerv
        g = complete_basis(kerv, rng, p)           # g e_0 = a  (ker mask: column 0 zero)
        h = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        comps['ker'] = comp_tangent('ker', g, h, pen, p)
        cok = common_cokernel(pen, p); assert len(cok) == 1
        W = hyperplane_basis(cok[0], rng, p)
        extra = complete_basis(W, rng, p)
        cols = [[extra[a][3] for a in range(n)]] + [[extra[a][j] for a in range(n)] for j in range(3)]
        h2 = [[cols[j][a] for j in range(n)] for a in range(n)]
        comps['coker'] = comp_tangent('coker', h, h2, pen, p)
        curves['P'] = prim_curve(pt['phi'], pt['u'], rng, p)
    elif spec in ('P_SP', 'P_c32'):
        # u of rank 3 with image Y = <e_0,e_1,e_2> in a standard frame, then conjugated
        phi0 = rand_mat(Rg, rng, n, 6, 1, p-1, p)
        if spec == 'P_c32':
            for a in range(n): phi0[a][PAIRS.index((0, 1))] = 0     # phi(e_0 ^ e_1) = 0
        v = rand_mat(Rg, rng, R, 3, 1, p-1, p)
        u0 = [[v[k][0], v[k][1], v[k][2], 0] for k in range(R)]
        h = rand_mat(Rg, rng, n, n, 1, p-1, p); g = rand_mat(Rg, rng, n, n, 1, p-1, p)
        phi, u = prim_conj(Rg, phi0, u0, h, g, p)
        pen, tang = prim_point(Rg, phi, u)
        comps['P'] = tang
        gi = mat_inv(g, p)
        Y = [[gi[a][j] for a in range(n)] for j in range(3)]       # g^{-1} e_j
        spar = sp_frame_from_prim(phi, u, Y, rng, p)
        pen2, tang2 = sp_point(Rg, spar['phi'], spar['x'], spar['c'], spar['P'], spar['Q'])
        assert pencil_vec(pen2) == pencil_vec(pen), "SP frame does not reproduce the pencil"
        comps['SP'] = tang2
        curves['P'] = prim_curve(phi, u, rng, p)
        curves['SP'] = sp_curve(spar, rng, p)
        if spec == 'P_c32':
            # c32 flag : U_3 = Y, W_2 = phi(Lambda^2 Y)
            gY = complete_basis(Y, rng, p)
            # phi(y_i ^ y_j) for the three pairs ; span should be 2-dim
            def phi_wedge(yi, yj):
                w = [(yi[b]*yj[c] - yi[c]*yj[b]) % p for (b, c) in PAIRS]
                return [sum(phi[a][s]*w[s] for s in range(6)) % p for a in range(n)]
            vecs = [phi_wedge(Y[0], Y[1]), phi_wedge(Y[0], Y[2]), phi_wedge(Y[1], Y[2])]
            A = nmod_mat(3, n, [int(x) for vv in vecs for x in vv], p)
            assert A.rank() == 2, A.rank()
            rr = A.rref()[0]
            W2 = [[int(rr[i, j]) for j in range(n)] for i in range(2)]
            hW = complete_basis(W2, rng, p)          # columns W2 then extra (c32 mask: W = <e_0,e_1>)
            comps['c32'] = comp_tangent('c32', gY, hW, pen, p)
            info['W2_rank'] = 2
    elif spec == 'P_c21':
        phi0 = rand_mat(Rg, rng, n, 6, 1, p-1, p)
        v = rand_mat(Rg, rng, R, 2, 1, p-1, p)
        u0 = [[v[k][0], v[k][1], 0, 0] for k in range(R)]
        h = rand_mat(Rg, rng, n, n, 1, p-1, p); g = rand_mat(Rg, rng, n, n, 1, p-1, p)
        phi, u = prim_conj(Rg, phi0, u0, h, g, p)
        pen, tang = prim_point(Rg, phi, u)
        comps['P'] = tang
        gi = mat_inv(g, p)
        U2 = [[gi[a][j] for a in range(n)] for j in range(2)]
        def phi_wedge(yi, yj):
            w = [(yi[b]*yj[c] - yi[c]*yj[b]) % p for (b, c) in PAIRS]
            return [sum(phi[a][s]*w[s] for s in range(6)) % p for a in range(n)]
        W1 = [phi_wedge(U2[0], U2[1])]
        gU = complete_basis(U2, rng, p); hW = complete_basis(W1, rng, p)
        comps['c21'] = comp_tangent('c21', gU, hW, pen, p)
        # SP frames : any Y_3 containing U_2 (a P^1 of them) -- take three
        for t in range(3):
            extra = [rng.randint(1, p-1) for _ in range(n)]
            Y = [U2[0], U2[1], extra]
            spar = sp_frame_from_prim(phi, u, Y, rng, p)
            pen2, tang2 = sp_point(Rg, spar['phi'], spar['x'], spar['c'], spar['P'], spar['Q'])
            assert pencil_vec(pen2) == pencil_vec(pen)
            comps[f'SP{t}'] = tang2
            if t == 0: curves['SP0'] = sp_curve(spar, rng, p)
        curves['P'] = prim_curve(phi, u, rng, p)
    elif spec in ('P_tan', 'P_meet'):
        pt = prim_random(Rg, rng, p, phi_special=('tan' if spec == 'P_tan' else 'meet'))
        pen, tang = prim_point(Rg, pt['phi'], pt['u'])
        comps['P'] = tang
        curves['P'] = prim_curve(pt['phi'], pt['u'], rng, p)
        if spec == 'P_meet':
            # the cokernel vector is linear of rank 3 here : the point lies on SP^T
            par = sp_frame_from_pencil(pencil_T(pen), rng, p)
            assert par is not None, "P_meet point not on SP^T"
            pen2, tang2 = sp_point(Rg, par['phi'], par['x'], par['c'], par['P'], par['Q'])
            assert pencil_vec(pencil_T(pen2)) == pencil_vec(pen)
            comps['SPT'] = [pencil_T(t) for t in tang2]
            penE, tangE = sp_curve(par, rng, p)
            curves['SPT'] = (pencil_T(penE), [pencil_T(t) for t in tangE])
    elif spec == 'SP_c32':
        pt = sp_random(Rg, rng, p, phi_rank=2)
        pen, tang = sp_point(Rg, pt['phi'], pt['x'], pt['c'], pt['P'], pt['Q'])
        comps['SP'] = tang
        # flag : U_3 = Q^{-1}<e_0,e_1,e_2>, W_2 = P (im phi)
        Qi = mat_inv(pt['Q'], p)
        gY = [[Qi[a][j] for j in range(n)] for a in range(n)]          # columns Q^{-1} e_j
        imphi = col_span(pt['phi'], p)
        assert len(imphi) == 2, len(imphi)
        W2 = [[sum(pt['P'][a][b]*w[b] for b in range(n)) % p for a in range(n)] for w in imphi]
        hW = complete_basis(W2, rng, p)
        comps['c32'] = comp_tangent('c32', gY, hW, pen, p)
        curves['SP'] = sp_curve(pt, rng, p)
    elif spec == 'SP_c21':
        pt = sp_random(Rg, rng, p, x_rank=2)
        pen, tang = sp_point(Rg, pt['phi'], pt['x'], pt['c'], pt['P'], pt['Q'])
        comps['SP'] = tang
        Qi = mat_inv(pt['Q'], p)
        # U_2 = Q^{-1} (im x padded) ; W_1 = P phi (x_1 cross x_2)
        X = [pt['x'][k] for k in range(R)]
        A = nmod_mat(R, 3, [int(v) for row in X for v in row], p); rr = A.rref()[0]
        xb = [[int(rr[i, j]) for j in range(3)] for i in range(2)]
        U2 = [[sum(Qi[a][b]*(xb[i][b] if b < 3 else 0) for b in range(n)) % p for a in range(n)] for i in range(2)]
        cr = [(xb[0][1]*xb[1][2] - xb[0][2]*xb[1][1]) % p,
              (xb[0][2]*xb[1][0] - xb[0][0]*xb[1][2]) % p,
              (xb[0][0]*xb[1][1] - xb[0][1]*xb[1][0]) % p]
        w = [sum(pt['phi'][a][j]*cr[j] for j in range(3)) % p for a in range(n)]
        W1 = [[sum(pt['P'][a][b]*w[b] for b in range(n)) % p for a in range(n)]]
        gU = complete_basis(U2, rng, p); hW = complete_basis(W1, rng, p)
        comps['c21'] = comp_tangent('c21', gU, hW, pen, p)
        curves['SP'] = sp_curve(pt, rng, p)
    elif spec == 'SP_ker':
        pt = sp_random(Rg, rng, p)
        w = [rng.randint(1, p-1) for _ in range(3)]
        # c_k = phi N(x_k) w  -> common kernel (-w, 1) before Q
        for k in range(R):
            Nk = skewN(Rg, pt['x'][k]); L = mat_mul(Rg, pt['phi'], Nk)
            pt['c'][k] = [sum(L[a][j]*w[j] for j in range(3)) % p for a in range(n)]
        pen, tang = sp_point(Rg, pt['phi'], pt['x'], pt['c'], pt['P'], pt['Q'])
        comps['SP'] = tang
        kerv = common_kernel(pen, p); assert len(kerv) == 1, kerv
        g = complete_basis(kerv, rng, p)
        h = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        comps['ker'] = comp_tangent('ker', g, h, pen, p)
        curves['SP'] = sp_curve(pt, rng, p)
    elif spec == 'SP_coker':
        pt = sp_random(Rg, rng, p)
        cp = rand_mat(Rg, rng, R, 3, 1, p-1, p)
        for k in range(R):
            pt['c'][k] = [sum(pt['phi'][a][j]*cp[k][j] for j in range(3)) % p for a in range(n)]
        pen, tang = sp_point(Rg, pt['phi'], pt['x'], pt['c'], pt['P'], pt['Q'])
        comps['SP'] = tang
        cok = common_cokernel(pen, p); assert len(cok) == 1, cok
        W = hyperplane_basis(cok[0], rng, p)
        extra = complete_basis(W, rng, p)
        cols = [[extra[a][3] for a in range(n)]] + [[extra[a][j] for a in range(n)] for j in range(3)]
        h2 = [[cols[j][a] for j in range(n)] for a in range(n)]
        g = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        comps['coker'] = comp_tangent('coker', g, h2, pen, p)
        curves['SP'] = sp_curve(pt, rng, p)
    elif spec in ('c21_c32', 'ker_coker', 'c21_gen', 'ker_gen', 'coker_gen', 'c32_gen'):
        # audit calibration points, in the standard frames then conjugated
        if spec == 'c21_c32':
            mask = [ab for ab in comp_mask('c21') if ab in comp_mask('c32')]
            names = ['c21', 'c32']
        elif spec == 'ker_coker':
            mask = [ab for ab in comp_mask('ker') if ab in comp_mask('coker')]
            names = ['ker', 'coker']
        else:
            nm = spec.split('_')[0]; mask = comp_mask(nm); names = [nm]
        Pm = rand_mat(Rg, rng, n, n, 1, p-1, p); Qm = rand_mat(Rg, rng, n, n, 1, p-1, p)
        Bs = []
        for k in range(R):
            B = mat_zero(Rg, n, n)
            for (a, b) in mask: B[a][b] = rng.randint(1, p-1)
            Bs.append(B)
        pen = pencil_conj(Rg, Pm, Bs, Qm)
        Qi = mat_inv(Qm, p)
        # standard flags : source basis columns of Q^{-1}, target basis columns of P
        g = Qi; h = Pm
        for nm in names:
            comps[nm] = comp_tangent(nm, g, h, pen, p)
        info['mask'] = len(mask)
    else:
        raise ValueError(spec)
    return dict(pen=pen, comps=comps, curves=curves, info=info)

SPECS_ORDER = ['c21_c32', 'ker_coker', 'c21_gen', 'ker_gen',
               'P_gen', 'PT_gen', 'SP_gen', 'SPT_gen',
               'P_coker', 'P_SP', 'P_c21', 'P_c32', 'P_ker', 'P_tan', 'P_meet',
               'SP_c32', 'SP_c21', 'SP_ker', 'SP_coker']

if __name__ == '__main__':
    print("wk10_s66_points loaded;", len(SPECS_ORDER), "specs")

# ----------------------------------------------------------------------
# SP frame recovered from a pencil with a LINEAR kernel vector of rank 3
def linear_kernel_vector(pen, p):
    """kappa_1..kappa_5 in C^4 with M(s) kappa(s) == 0, kappa(s) = sum s_k kappa_k :
    solve B_j kappa_k + B_k kappa_j = 0 (j<k), B_k kappa_k = 0.  Returns the
    solution space (list of 20-vectors)."""
    rows = []
    for j in range(R):
        for k in range(j, R):
            for a in range(n):
                row = [0]*(R*n)
                for b in range(n):
                    if j == k:
                        row[k*n + b] = (row[k*n + b] + pen[k][a][b]) % p
                    else:
                        row[k*n + b] = (row[k*n + b] + pen[j][a][b]) % p
                        row[j*n + b] = (row[j*n + b] + pen[k][a][b]) % p
                rows.append(row)
    A = nmod_mat(len(rows), R*n, [int(x) % p for r in rows for x in r], p)
    return kernel_basis(A)

def sp_frame_from_pencil(pen, rng, p):
    """pen with a unique linear kernel vector kappa(s) whose values span a 3-space U.
    Returns SP parameters (phi43, x, c, P=I, Q=g^{-1}) reproducing pen, or None."""
    Rg = Fp(p)
    ks = linear_kernel_vector(pen, p)
    if len(ks) != 1: return None
    kap = [[ks[0][k*n + b] % p for b in range(n)] for k in range(R)]       # kappa_k
    A = nmod_mat(R, n, [int(x) for row in kap for x in row], p)
    if A.rank() != 3: return None
    rr = A.rref()[0]
    Y = [[int(rr[i, j]) for j in range(n)] for i in range(3)]
    g = complete_basis(Y, rng, p); gi = mat_inv(g, p)
    x = []
    for k in range(R):
        coords = [sum(gi[i][b]*kap[k][b] for b in range(n)) % p for i in range(n)]
        assert coords[3] == 0
        x.append(coords[:3])
    # L_k = B_k g : first three columns = phi43 N(x_k) ; solve for phi43 (12 unknowns)
    L = [mat_mul(Rg, pen[k], g) for k in range(R)]
    rows = []; rhs = []
    for k in range(R):
        Nk = skewN(Rg, x[k])
        for a in range(n):
            for j in range(3):
                # (phi43 N(x_k))[a][j] = sum_i phi43[a][i] Nk[i][j]
                row = [0]*12
                for i in range(3): row[a*3 + i] = Nk[i][j] % p
                rows.append(row); rhs.append(L[k][a][j] % p)
    sol = None
    Aug = nmod_mat(len(rows), 13, [int(rows[r][j]) if j < 12 else (-rhs[r]) % p
                                   for r in range(len(rows)) for j in range(13)], p)
    X, nul = Aug.nullspace()
    for t in range(nul):
        last = int(X[12, t]) % p
        if last:
            inv = pow(last, p-2, p); sol = [(int(X[j, t])*inv) % p for j in range(12)]; break
    if sol is None: return None
    phi43 = [[sol[a*3 + i] for i in range(3)] for a in range(n)]
    c = [[L[k][a][3] % p for a in range(n)] for k in range(R)]
    I4 = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    par = dict(phi=phi43, x=x, c=c, P=I4, Q=gi)
    pen2, _ = sp_point(Rg, phi43, x, c, I4, gi)
    if pencil_vec(pen2) != pencil_vec(pen): return None
    return par
