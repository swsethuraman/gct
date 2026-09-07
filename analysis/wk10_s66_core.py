#!/usr/bin/env python3
"""
Session 66 -- core : the r = 5 base locus B_5 = {M : det M(s) == 0} of
Phi : X_5 = Hom(C^5, M_4) -> Sym^4 C^5, its component types, tangent spaces,
the first-order kernel ker dPhi, and the second-order quadrics.

Everything is exact over F_p (python-flint nmod_mat for every rank); dPhi by
dual numbers on the 70 quartic coefficients, reusing wk9_s59_core.det_arc.

Component types (pencil M(s) = sum_k s_k B_k, B_k 4x4):

  ker   : B_k e = 0            (common kernel, flag P^3)               dim 63
  coker : im B_k <= W_3        (common cokernel)                       dim 63
  c21   : B_k(U_2) <= W_1                                              dim 57
  c32   : B_k(U_3) <= W_2                                              dim 57
  SP    : B_k = [ phi N(x_k) | c_k ],  phi : C^3 -> C^4, N(x) the 3x3
          skew matrix (N(x) y = x cross y), c_k in C^4 (7-dim space S_phi),
          conjugated to general position by (P, Q)                     dim 49
  SPT   : transposes of SP                                             dim 49
  P     : B_k = M_phi(u_k),  M_phi(y)_{ab} = sum_c phi[a][b][c] y_c with
          phi antisymmetric in (b,c)  (the s59 'prim' convention; kernel of
          M_phi(y) is y)                                               dim 43
  PT    : transposes of P                                              dim 43

A point of a type is a dict of parameter blocks; the pencil and its tangent
vectors are multilinear in the blocks, so directional derivatives are obtained
by substituting the direction for one block (no dual numbers needed there).
All parametrisation code is written over an abstract ring `Rg` (add, mul, neg,
zero, one, from_int) so the same code runs over F_p and over F_p[eps]/eps^K
(for limit tangent spaces along a curve).
"""
import sys, random, itertools
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk9_s59_core import (R, n, NQ, QIDX, S5DEG0, S5POS, det_arc,
                          pencils_to_entry, rank_mod, quartic_vec)

P1, P2, P3 = 2147483647, 2147483629, 2147483587
HOUSE = [P1, P2]

# ----------------------------------------------------------------------
# rings
class Fp:
    def __init__(self, p): self.p = p
    def zero(self): return 0
    def one(self): return 1
    def from_int(self, a): return a % self.p
    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def mul(self, a, b): return (a * b) % self.p
    def neg(self, a): return (-a) % self.p
    def is_zero(self, a): return a % self.p == 0

class FpEps:
    """F_p[eps]/eps^K ; elements are tuples of length K."""
    def __init__(self, p, K): self.p = p; self.K = K
    def zero(self): return (0,)*self.K
    def one(self): return (1,) + (0,)*(self.K-1)
    def from_int(self, a): return (a % self.p,) + (0,)*(self.K-1)
    def eps(self): return (0, 1) + (0,)*(self.K-2)
    def lift(self, a0, a1=0):
        """a0 + eps a1"""
        return (a0 % self.p, a1 % self.p) + (0,)*(self.K-2)
    def add(self, a, b): return tuple((x + y) % self.p for x, y in zip(a, b))
    def sub(self, a, b): return tuple((x - y) % self.p for x, y in zip(a, b))
    def neg(self, a): return tuple((-x) % self.p for x in a)
    def mul(self, a, b):
        K, p = self.K, self.p
        out = [0]*K
        for i, x in enumerate(a):
            if x == 0: continue
            for j in range(K - i):
                y = b[j]
                if y: out[i+j] = (out[i+j] + x*y) % p
        return tuple(out)
    def is_zero(self, a): return all(x % self.p == 0 for x in a)
    def val(self, a):
        for i, x in enumerate(a):
            if x % self.p: return i
        return self.K

# ----------------------------------------------------------------------
# small linear algebra over a ring
def mat_zero(Rg, r, c): return [[Rg.zero() for _ in range(c)] for _ in range(r)]
def mat_mul(Rg, A, B):
    r, m, c = len(A), len(B), len(B[0])
    out = mat_zero(Rg, r, c)
    for i in range(r):
        Ai = A[i]
        for k in range(m):
            a = Ai[k]
            if Rg.is_zero(a): continue
            Bk = B[k]; oi = out[i]
            for j in range(c):
                if not Rg.is_zero(Bk[j]):
                    oi[j] = Rg.add(oi[j], Rg.mul(a, Bk[j]))
    return out
def mat_add(Rg, A, B):
    return [[Rg.add(a, b) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def mat_T(A): return [list(col) for col in zip(*A)]
def mat_scale(Rg, c, A): return [[Rg.mul(c, a) for a in row] for row in A]
def rand_mat(Rg, rng, r, c, lo=1, hi=None, p=None):
    if hi is None: hi = p - 1
    return [[Rg.from_int(rng.randint(lo, hi)) for _ in range(c)] for _ in range(r)]

def pencil_zero(Rg): return [mat_zero(Rg, n, n) for _ in range(R)]
def pencil_add(Rg, A, B): return [mat_add(Rg, a, b) for a, b in zip(A, B)]
def pencil_conj(Rg, P, pen, Q): return [mat_mul(Rg, mat_mul(Rg, P, B), Q) for B in pen]
def pencil_T(pen): return [mat_T(B) for B in pen]
def pencil_vec(pen):
    """flatten a pencil (over Fp ints) to a length-80 list: index k*16+a*4+b."""
    return [pen[k][a][b] for k in range(R) for a in range(n) for b in range(n)]
def vec_pencil(v):
    return [[[v[k*16 + a*4 + b] for b in range(n)] for a in range(n)] for k in range(R)]

# ----------------------------------------------------------------------
# the 3x3 skew matrix N(x) y = x cross y   (N(x) x = 0)
def skewN(Rg, x):
    z = Rg.zero()
    x1, x2, x3 = x
    return [[z, Rg.neg(x3), x2],
            [x3, z, Rg.neg(x1)],
            [Rg.neg(x2), x1, z]]

# ----------------------------------------------------------------------
# parametrisations.  Each returns (pencil, tangent_vectors) where the tangents
# are the directional derivatives along every parameter of the family
# (multilinear substitution), PLUS the group directions (GL_4 x GL_4 on the
# matrices, GL_5 on s) which every component contains.

PAIRS = [(b, c) for b in range(n) for c in range(b+1, n)]     # 6 Pluecker slots

def M_phi(Rg, phi, y):
    """phi[a][slot] (a in 0..3, slot in PAIRS), y in C^4 ->
       M(y)_{ab} = sum_c phit[a][b][c] y_c,  phit antisymmetric in (b,c)."""
    M = mat_zero(Rg, n, n)
    for a in range(n):
        for si, (b, c) in enumerate(PAIRS):
            v = phi[a][si]
            if Rg.is_zero(v): continue
            # phit[a][b][c] = v, phit[a][c][b] = -v
            M[a][b] = Rg.add(M[a][b], Rg.mul(v, y[c]))
            M[a][c] = Rg.sub(M[a][c], Rg.mul(v, y[b]))
    return M

def group_directions(Rg, pen):
    """GL_4 x GL_4 x GL_5 infinitesimal directions at a pencil: 16+16+25."""
    dirs = []
    for a in range(n):
        for b in range(n):
            E = mat_zero(Rg, n, n); E[a][b] = Rg.one()
            dirs.append([mat_mul(Rg, E, B) for B in pen])      # left
    for a in range(n):
        for b in range(n):
            E = mat_zero(Rg, n, n); E[a][b] = Rg.one()
            dirs.append([mat_mul(Rg, B, E) for B in pen])      # right
    for j in range(R):
        for k in range(R):
            d = pencil_zero(Rg); d[k] = pen[j]                 # s_j -> s_j + eps s_k... B_k += B_j
            dirs.append(d)
    return dirs

# ---- compression types --------------------------------------------------
def comp_mask(name):
    """standard mask of the 4x4 space E for a compression type."""
    if name == 'ker':    return [(a, b) for a in range(n) for b in range(1, n)]
    if name == 'coker':  return [(a, b) for a in range(1, n) for b in range(n)]
    if name == 'c21':    return [(a, b) for a in range(n) for b in range(n)
                                 if not (b in (0, 1) and a in (1, 2, 3))]
    if name == 'c32':    return [(a, b) for a in range(n) for b in range(n)
                                 if not (b in (0, 1, 2) and a in (2, 3))]
    raise ValueError(name)

def comp_point(Rg, name, Bcoef, P, Q):
    """Bcoef[k] : dict {(a,b): value} on the mask ; pencil = P B_k Q."""
    mask = comp_mask(name)
    Bs = []
    for k in range(R):
        B = mat_zero(Rg, n, n)
        for (a, b) in mask: B[a][b] = Bcoef[k][(a, b)]
        Bs.append(B)
    pen = pencil_conj(Rg, P, Bs, Q)
    tang = []
    for k in range(R):                    # delta B_k on the mask
        for (a, b) in mask:
            E = mat_zero(Rg, n, n); E[a][b] = Rg.one()
            d = pencil_zero(Rg); d[k] = mat_mul(Rg, mat_mul(Rg, P, E), Q)
            tang.append(d)
    for a in range(n):                    # delta P, delta Q
        for b in range(n):
            E = mat_zero(Rg, n, n); E[a][b] = Rg.one()
            tang.append([mat_mul(Rg, mat_mul(Rg, E, B), Q) for B in Bs])
            tang.append([mat_mul(Rg, mat_mul(Rg, P, B), E) for B in Bs])
    tang += group_directions(Rg, pen)
    return pen, tang

def comp_random(Rg, name, rng, p, lo=1, hi=None):
    mask = comp_mask(name)
    Bcoef = [{ab: Rg.from_int(rng.randint(lo, hi or p-1)) for ab in mask} for _ in range(R)]
    P = rand_mat(Rg, rng, n, n, lo, hi, p); Q = rand_mat(Rg, rng, n, n, lo, hi, p)
    return dict(Bcoef=Bcoef, P=P, Q=Q)

# ---- P (primitive, k = 4) -------------------------------------------------
def prim_point(Rg, phi, u, transpose=False):
    """phi[a][slot] 4x6, u[k] in C^4 (k = 0..4).  pencil B_k = M_phi(u_k)."""
    pen = [M_phi(Rg, phi, u[k]) for k in range(R)]
    tang = []
    for a in range(n):                    # delta phi
        for si in range(6):
            dphi = [[Rg.zero()]*6 for _ in range(n)]
            dphi[a][si] = Rg.one()
            tang.append([M_phi(Rg, dphi, u[k]) for k in range(R)])
    for k in range(R):                    # delta u
        for c in range(n):
            du = [Rg.zero()]*n; du[c] = Rg.one()
            d = pencil_zero(Rg); d[k] = M_phi(Rg, phi, du)
            tang.append(d)
    if transpose:
        pen = pencil_T(pen); tang = [pencil_T(t) for t in tang]
    tang += group_directions(Rg, pen)
    return pen, tang

def prim_random(Rg, rng, p, lo=1, hi=None, u_rank=4, phi_rank=4, phi_special=None):
    """random (phi, u).  u_rank < 4 : u = v . w with v 5 x r, w r x 4.
    phi_rank = 3 : phi = psi . rho, psi 4x3, rho 3x6 (image a hyperplane).
    phi_special in {'tan','meet','kerline'} : kernel of phi in special position
    (built in a standard basis, then conjugated by a random (g on C^4)):
       'meet'    : ker phi = < e1^e2 , e1^e3 >  (two 2-planes sharing a line)
       'tan'     : ker phi = < e1^e2 , e1^e3 + e2^e4 >  (line tangent to the
                   Klein quadric at e1^e2 : (e1^e3+e2^e4)^2 = 2 e1^e3^e2^e4 != 0,
                   so a single decomposable point, doubled)
       'kerline' : ker phi = < e1^e2 , e1^e3 > is 'meet'; the ker-incidence
                   (common kernel a) needs rank 3 with ker = a ^ C^4, built
                   separately by prim_kerinc."""
    hi = hi or p - 1
    if phi_special is None:
        if phi_rank == 4:
            phi = rand_mat(Rg, rng, n, 6, lo, hi, p)
        else:
            psi = rand_mat(Rg, rng, n, phi_rank, lo, hi, p)
            rho = rand_mat(Rg, rng, phi_rank, 6, lo, hi, p)
            phi = mat_mul(Rg, psi, rho)
    else:
        # kernel K spanned by two 2-vectors k1, k2 (in Pluecker coords over PAIRS)
        def pl(b, c):
            v = [Rg.zero()]*6
            if b < c: v[PAIRS.index((b, c))] = Rg.one()
            else: v[PAIRS.index((c, b))] = Rg.neg(Rg.one())
            return v
        e12 = pl(0, 1); e13 = pl(0, 2); e24 = pl(1, 3)
        if phi_special == 'meet':
            k1, k2 = e12, e13
        elif phi_special == 'tan':
            k1 = e12; k2 = [Rg.add(x, y) for x, y in zip(e13, e24)]
        else:
            raise ValueError(phi_special)
        # a random phi0 : 4 x 6 with phi0 k1 = phi0 k2 = 0 : pick 4 random
        # rows in the 4-dim annihilator of <k1,k2>  (solve over F_p ints)
        p_ = p
        Kmat = nmod_mat(2, 6, [int(x if isinstance(x, int) else x[0]) for x in k1] +
                              [int(x if isinstance(x, int) else x[0]) for x in k2], p_)
        # annihilator : rows r with Kmat r^T = 0  -> nullspace of Kmat
        NS, nul = Kmat.nullspace()
        assert nul == 4
        basis = [[int(NS[i, j]) for i in range(6)] for j in range(nul)]
        phi0 = []
        for a in range(n):
            coef = [rng.randint(lo, hi) for _ in range(nul)]
            row = [sum(coef[j]*basis[j][i] for j in range(nul)) % p_ for i in range(6)]
            phi0.append([Rg.from_int(x) for x in row])
        # conjugate by a random g on C^4 : phi(y^t) -> phi(g y ^ g t) , i.e.
        # phi . Lambda^2 g ; and by a random h on the target : h . phi
        g = rand_mat(Rg, rng, n, n, lo, hi, p); h = rand_mat(Rg, rng, n, n, lo, hi, p)
        L2g = lambda2(Rg, g)
        phi = mat_mul(Rg, h, mat_mul(Rg, phi0, L2g))
    if u_rank == 4:
        u = rand_mat(Rg, rng, R, n, lo, hi, p)
    else:
        v = rand_mat(Rg, rng, R, u_rank, lo, hi, p)
        w = rand_mat(Rg, rng, u_rank, n, lo, hi, p)
        u = mat_mul(Rg, v, w)
    return dict(phi=phi, u=u)

def lambda2(Rg, g):
    """Lambda^2 g on Pluecker coordinates over PAIRS : (g y ^ g t)_{bc}."""
    L = mat_zero(Rg, 6, 6)
    for si, (b, c) in enumerate(PAIRS):        # output slot
        for sj, (i, j) in enumerate(PAIRS):    # input slot e_i ^ e_j
            # (g e_i ^ g e_j)_{bc} = g_bi g_cj - g_ci g_bj
            L[si][sj] = Rg.sub(Rg.mul(g[b][i], g[c][j]), Rg.mul(g[c][i], g[b][j]))
    return L

def prim_kerinc(Rg, rng, p, lo=1, hi=None):
    """P cap ker : rank-3 phi with ker phi = a ^ C^4.  Standard a = e_1 :
    ker phi = < e1^e2, e1^e3, e1^e4 > ; phi supported on e2^e3, e2^e4, e3^e4 ;
    then conjugated by random (h, g)."""
    hi = hi or p - 1
    phi0 = [[Rg.zero()]*6 for _ in range(n)]
    for a in range(n):
        for si, (b, c) in enumerate(PAIRS):
            if b >= 1:
                phi0[a][si] = Rg.from_int(rng.randint(lo, hi))
    g = rand_mat(Rg, rng, n, n, lo, hi, p); h = rand_mat(Rg, rng, n, n, lo, hi, p)
    phi = mat_mul(Rg, h, mat_mul(Rg, phi0, lambda2(Rg, g)))
    u = rand_mat(Rg, rng, R, n, lo, hi, p)
    return dict(phi=phi, u=u)

# ---- SP (semi-primitive, k = 3) -------------------------------------------
def sp_point(Rg, phi, x, c, P, Q, transpose=False):
    """phi 4x3, x[k] in C^3, c[k] in C^4 ; B_k = P [ phi N(x_k) | c_k ] Q."""
    def block(ph, xk, ck):
        Nk = skewN(Rg, xk)
        L = mat_mul(Rg, ph, Nk)                       # 4 x 3
        return [[L[a][0], L[a][1], L[a][2], ck[a]] for a in range(n)]
    Bs = [block(phi, x[k], c[k]) for k in range(R)]
    pen = pencil_conj(Rg, P, Bs, Q)
    tang = []
    for a in range(n):                    # delta phi
        for j in range(3):
            dphi = mat_zero(Rg, n, 3); dphi[a][j] = Rg.one()
            z4 = [Rg.zero()]*n
            tang.append(pencil_conj(Rg, P, [block(dphi, x[k], z4) for k in range(R)], Q))
    for k in range(R):                    # delta x_k
        for j in range(3):
            dx = [Rg.zero()]*3; dx[j] = Rg.one()
            d = pencil_zero(Rg); d[k] = block(phi, dx, [Rg.zero()]*n)
            tang.append(pencil_conj(Rg, P, d, Q))
    for k in range(R):                    # delta c_k
        for a in range(n):
            dc = [Rg.zero()]*n; dc[a] = Rg.one()
            d = pencil_zero(Rg); d[k] = block(phi, [Rg.zero()]*3, dc)
            tang.append(pencil_conj(Rg, P, d, Q))
    for a in range(n):                    # delta P, delta Q (moves U, W)
        for b in range(n):
            E = mat_zero(Rg, n, n); E[a][b] = Rg.one()
            tang.append([mat_mul(Rg, mat_mul(Rg, E, B), Q) for B in Bs])
            tang.append([mat_mul(Rg, mat_mul(Rg, P, B), E) for B in Bs])
    if transpose:
        pen = pencil_T(pen); tang = [pencil_T(t) for t in tang]
    tang += group_directions(Rg, pen)
    return pen, tang

def sp_random(Rg, rng, p, lo=1, hi=None, phi_rank=3, x_rank=3, c_mode='free'):
    hi = hi or p - 1
    if phi_rank == 3:
        phi = rand_mat(Rg, rng, n, 3, lo, hi, p)
    else:
        phi = mat_mul(Rg, rand_mat(Rg, rng, n, phi_rank, lo, hi, p),
                      rand_mat(Rg, rng, phi_rank, 3, lo, hi, p))
    if x_rank == 3:
        x = rand_mat(Rg, rng, R, 3, lo, hi, p)
    else:
        x = mat_mul(Rg, rand_mat(Rg, rng, R, x_rank, lo, hi, p),
                    rand_mat(Rg, rng, x_rank, 3, lo, hi, p))
    if c_mode == 'free':
        c = rand_mat(Rg, rng, R, n, lo, hi, p)
    elif c_mode == 'through_x':           # c_k = psi x_k  (rank <= 3, factoring through x)
        psi = rand_mat(Rg, rng, n, 3, lo, hi, p)
        c = [[sum_ring(Rg, [Rg.mul(psi[a][j], x[k][j]) for j in range(3)]) for a in range(n)]
             for k in range(R)]
    else:
        raise ValueError(c_mode)
    P = rand_mat(Rg, rng, n, n, lo, hi, p); Q = rand_mat(Rg, rng, n, n, lo, hi, p)
    return dict(phi=phi, x=x, c=c, P=P, Q=Q)

def sum_ring(Rg, xs):
    s = Rg.zero()
    for x in xs: s = Rg.add(s, x)
    return s

# ----------------------------------------------------------------------
# dPhi at a pencil (over F_p ints) : 70 x 80 matrix, columns = one-hot N
def dPhi_matrix(pen, p):
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                D = [[[0]*n for _ in range(n)] for _ in range(R)]
                D[k][a][b] = 1
                entry = pencils_to_entry([pen], p, duals=[D])
                det = det_arc(entry, p, 0)
                cols.append(quartic_vec(det.get(0, {}), p, part=1))
    # cols[j] is the 70-vector dPhi(e_j) ; return as 70 x 80 nmod_mat
    flat = [int(cols[j][i]) for i in range(NQ) for j in range(80)]
    return nmod_mat(NQ, 80, flat, p)

def det_value(pen, p):
    entry = pencils_to_entry([pen], p)
    det = det_arc(entry, p, 0)
    return quartic_vec(det.get(0, {}), p, part=0)

def kernel_basis(A):
    """nullspace of nmod_mat A : list of column vectors (as int lists)."""
    X, nul = A.nullspace()
    r = A.ncols()
    return [[int(X[i, j]) for i in range(r)] for j in range(nul)]

def apply(A, v, p):
    """A (nmod_mat r x c) times vector v (list) -> list."""
    c = A.ncols()
    V = nmod_mat(c, 1, [int(x) % p for x in v], p)
    W = A * V
    return [int(W[i, 0]) for i in range(A.nrows())]

def span_rank(vectors, ncols, p):
    return rank_mod(vectors, ncols, p) if vectors else 0

def in_kernel_count(dP, vectors, p):
    """how many of the vectors annihilate dPhi (must be all)."""
    bad = 0
    for v in vectors:
        w = apply(dP, v, p)
        if any(w): bad += 1
    return len(vectors) - bad, bad

# ----------------------------------------------------------------------
# limit tangent space along a curve : columns J(eps) over F_p[eps]/eps^K ;
# returns the reduction mod eps of the saturated column module (a basis of
# lim_{eps->0} colspan J(eps)), of dimension = generic rank.
def limit_colspace(cols, nrows, p, K):
    """cols : list of column vectors, entries K-tuples (FpEps).  Smith-type
    elimination with minimal-valuation pivoting; row ops tracked on Rinv so
    that the limit space = first r columns of Rinv mod eps."""
    Rg = FpEps(p, K)
    m = len(cols)
    A = [[cols[j][i] for j in range(m)] for i in range(nrows)]   # nrows x m
    Rinv = [[Rg.one() if i == j else Rg.zero() for j in range(nrows)] for i in range(nrows)]
    def inv_unit(a):
        # inverse of a unit in F_p[eps]/eps^K
        a0inv = pow(a[0], p-2, p)
        # Newton / series inversion
        out = [0]*K; out[0] = a0inv
        for t in range(1, K):
            s = 0
            for i in range(1, t+1):
                s = (s + a[i]*out[t-i]) % p
            out[t] = (-a0inv * s) % p
        return tuple(out)
    def shift_div(a, v):
        # divide a by eps^v (assumes val(a) >= v)
        return tuple(list(a[v:]) + [0]*v)
    pivots = []
    used_rows = set(); used_cols = set()
    for step in range(min(nrows, m)):
        # find entry of minimal valuation among unused rows/cols
        best = None
        for i in range(nrows):
            if i in used_rows: continue
            for j in range(m):
                if j in used_cols: continue
                v = Rg.val(A[i][j])
                if v < K and (best is None or v < best[0]):
                    best = (v, i, j)
                    if v == 0: break
            if best is not None and best[0] == 0: break
        if best is None: break
        v, pi, pj = best
        used_rows.add(pi); used_cols.add(pj); pivots.append((pi, pj, v))
        piv = A[pi][pj]
        unit = shift_div(piv, v)            # piv = eps^v * unit
        uinv = inv_unit(unit)
        # eliminate column pj from other rows : row_i -= (A[i][pj]/piv) row_pi
        for i in range(nrows):
            if i == pi: continue
            a = A[i][pj]
            if Rg.is_zero(a): continue
            f = Rg.mul(shift_div(a, v), uinv)          # a / piv  (val(a) >= v)
            Ai, Api = A[i], A[pi]
            for j in range(m):
                if not Rg.is_zero(Api[j]):
                    Ai[j] = Rg.sub(Ai[j], Rg.mul(f, Api[j]))
            # Rinv : column pi += f * column i   (R' = (I - f e_i e_pi^T) R)
            for r_ in range(nrows):
                if not Rg.is_zero(Rinv[r_][i]):
                    Rinv[r_][pi] = Rg.add(Rinv[r_][pi], Rg.mul(f, Rinv[r_][i]))
        # eliminate row pi from other columns (column ops do not affect Rinv)
        for j in range(m):
            if j == pj: continue
            a = A[pi][j]
            if Rg.is_zero(a): continue
            f = Rg.mul(shift_div(a, v), uinv)
            for i in range(nrows):
                if not Rg.is_zero(A[i][pj]):
                    A[i][j] = Rg.sub(A[i][j], Rg.mul(f, A[i][pj]))
    # limit space : columns pi of Rinv (pivot rows) reduced mod eps
    lim = []
    for (pi, pj, v) in pivots:
        lim.append([Rinv[r_][pi][0] % p for r_ in range(nrows)])
    return lim, pivots

# ----------------------------------------------------------------------
# second-order data : e_2(M_0 ; N) = t^2 coefficient of det(M_0 + t N)
def e2_vec(pen, N, p):
    entry = pencils_to_entry([pen, N], p)
    det = det_arc(entry, p, 2)
    return quartic_vec(det.get(2, {}), p, part=0)

def quadric_space(pen, dP, kerB, p, verbose=False):
    """Q_2 = { sum_j c_j e_{2,j} |_{ker dPhi} : c perp im dPhi }.
    kerB : basis of ker dPhi (list of 80-vectors), k = len(kerB).
    Returns dim Q_2, the list of quadrics (as symmetric k x k int matrices) and
    the polarised matrices B_j (70 of them, k x k)."""
    k = len(kerB)
    Ns = [vec_pencil(v) for v in kerB]
    # values e2(N_i) and e2(N_i + N_j)
    e2_single = [e2_vec(pen, Ns[i], p) for i in range(k)]
    # polarisation B(N_i,N_j) = e2(N_i+N_j) - e2(N_i) - e2(N_j) ; B(N_i,N_i) = 2 e2(N_i)
    # upper-triangular storage : q(z) = sum_i Q[i][i] z_i^2 + sum_{i<i2} Q[i][i2] z_i z_i2
    Bmat = [[[0]*k for _ in range(k)] for _ in range(NQ)]     # Bmat[j][i][i'] coefficient
    for i in range(k):
        for j in range(NQ):
            Bmat[j][i][i] = e2_single[i][j] % p
    for i in range(k):
        for i2 in range(i+1, k):
            Nsum = pencil_add(Fp(p), Ns[i], Ns[i2])
            e = e2_vec(pen, Nsum, p)
            for j in range(NQ):
                b = (e[j] - e2_single[i][j] - e2_single[i2][j]) % p
                Bmat[j][i][i2] = b; Bmat[j][i2][i] = b
        if verbose and i % 10 == 0:
            print(f"   polarisation row {i}/{k}", flush=True)
    # c perp im dPhi : left nullspace of dP (70 x 80) = nullspace of dP^T
    dPT = dP.transpose()
    cs = kernel_basis(dPT)                                  # each a 70-vector
    quads = []
    for c in cs:
        Qm = [[0]*k for _ in range(k)]
        for j in range(NQ):
            cj = c[j] % p
            if cj == 0: continue
            Bj = Bmat[j]
            for i in range(k):
                row = Bj[i]; Qi = Qm[i]
                for i2 in range(i, k):
                    if row[i2]:
                        Qi[i2] = (Qi[i2] + cj*row[i2]) % p
        quads.append(Qm)
    # dimension : rank of the upper-triangular coefficient vectors
    ut = [[Qm[i][i2] for i in range(k) for i2 in range(i, k)] for Qm in quads]
    dimQ2 = span_rank(ut, k*(k+1)//2, p)
    return dimQ2, quads, len(cs)

def quad_eval(Qm, z, p):
    """z^T Q z with Q upper-triangular-stored (only i<=i2 filled)."""
    k = len(z); s = 0
    for i in range(k):
        zi = z[i] % p
        if not zi: continue
        row = Qm[i]
        for i2 in range(i, k):
            if row[i2]:
                s = (s + zi*row[i2]*z[i2]) % p
    return s

# ----------------------------------------------------------------------
if __name__ == '__main__':
    print("wk10_s66_core loaded")
