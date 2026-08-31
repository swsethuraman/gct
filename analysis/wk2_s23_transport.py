"""Week 2, session 23 -- attainment in the World-B transport formula.

Exact arithmetic throughout (Python integers and Z[zeta_3] as pairs).

THE REDUCTION (derived by hand, pre-registered in results/PREREG_transport.md).
The transversal family f_s = x^2 y + s y^3 + z^3 has Waring lines

    l1 = k rho^-1 (x + rho^3 y),  l2 = -k rho^-1 (x - rho^3 y),  l3 = z,
    k = 6^{-1/3},  s = rho^6 / 3,

so the matrix of Waring lines is  M(rho) = A . diag(rho^-1, rho^2, 1)  with A
CONSTANT.  Hence f_s = tau(rho) . (B.v) with tau(rho) = diag(rho, rho^-2, 1)
the cusp stabiliser torus and B = A^{-1} a fixed matrix: the whole transversal
family is one torus orbit of one point of the open orbit.  Therefore, for F in
the lambda-isotypic component of C[G.v],

    F(f_s) = sum_nu rho^nu . <phi, pi_nu(B w)>,   w in S_lambda^H,

and the pole order along the boundary is (1/6) max { nu : pi_nu(B S_lambda^H)
!= 0 }.  The maximal tau-weight of S_lambda is mu_max = lambda_1 - 2 lambda_3,
which recovers the block-order upper bound; ATTAINMENT is the statement that
the component at nu* = 6 floor(mu_max/6) is nonzero.

MODEL.  S_lambda = ( C[e1,e2,e3,f12,f13,f23] / (Pi) )_{(p,q)} (x) det^r with
Pi = e1 f23 - e2 f13 + e3 f12, p = l1-l2, q = l2-l3, r = l3.  The ideal is
principal, so {Pi} is a Groebner basis and normal forms are the monomials not
divisible by e1 f23.  S_lambda^H is spanned by the S_3-symmetrisations of the
monomials satisfying the mu_3^3 condition n_i = a_i + sum_j q_ij + r = 0 mod 3.
"""

from fractions import Fraction
from itertools import permutations, product
from math import comb

# ---------------------------------------------------------------------------
# Z[zeta_3] = Z[x]/(x^2 + x + 1), elements as pairs (c0, c1) meaning c0 + c1 z
# ---------------------------------------------------------------------------

def zadd(u, v): return (u[0] + v[0], u[1] + v[1])
def zsub(u, v): return (u[0] - v[0], u[1] - v[1])

def zmul(u, v):
    # (a+bz)(c+dz) = ac + (ad+bc) z + bd z^2,  z^2 = -1 - z
    a, b = u; c, d = v
    ac = a * c; bd = b * d
    return (ac - bd, a * d + b * c - bd)

ZERO = (0, 0)
ONE = (1, 0)
ZETA = [(1, 0), (0, 1), (-1, -1)]        # 1, z, z^2


def elementary_of(mat):
    """e1, e2, e3 of a 3x3 matrix over Z[zeta_3] given as 3x3 of pairs."""
    def det2(i0, i1, j0, j1):
        return zsub(zmul(mat[i0][j0], mat[i1][j1]), zmul(mat[i0][j1], mat[i1][j0]))
    e1 = zadd(zadd(mat[0][0], mat[1][1]), mat[2][2])
    e2 = zadd(zadd(det2(0, 1, 0, 1), det2(0, 2, 0, 2)), det2(1, 2, 1, 2))
    e3 = zadd(zsub(zmul(mat[0][0], det2(1, 2, 1, 2)),
                   zmul(mat[0][1], det2(1, 2, 0, 2))),
              zmul(mat[0][2], det2(1, 2, 0, 1)))
    return e1, e2, e3


def H_elements():
    """The 162 elements of H = stab(x^3+y^3+z^3) in GL_3, as 3x3 Z[zeta_3]."""
    out = []
    for perm in permutations(range(3)):
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    sc = (ZETA[a], ZETA[b], ZETA[c])
                    M = [[ZERO] * 3 for _ in range(3)]
                    # column j of the permutation matrix sends e_j -> e_{perm[j]}
                    for j in range(3):
                        M[perm[j]][j] = sc[j]
                    out.append(M)
    assert len(out) == 162
    return out


_HE = None
def H_invariants_dim(lam):
    """m(lambda) = dim S_lambda^H, exact, by averaging the character."""
    global _HE
    if _HE is None:
        _HE = [elementary_of(M) for M in H_elements()]
    l1, l2, l3 = lam
    top = l1 + 2
    tot = ZERO
    for (e1, e2, e3) in _HE:
        h = [ZERO] * (top + 3)
        h[0] = ONE
        if top >= 1: h[1] = e1
        if top >= 2: h[2] = zsub(zmul(e1, h[1]), e2)
        for j in range(3, top + 1):
            h[j] = zadd(zsub(zmul(e1, h[j - 1]), zmul(e2, h[j - 2])), zmul(e3, h[j - 3]))
        def hh(k): return h[k] if 0 <= k <= top else ZERO
        # s_lambda = det( h_{lam_i - i + j} )_{i,j=1..3}
        rows = [[hh(lam[i] - i + j) for j in range(3)] for i in range(3)]
        d = zsub(zmul(rows[0][0], zsub(zmul(rows[1][1], rows[2][2]), zmul(rows[1][2], rows[2][1]))),
                 zmul(rows[0][1], zsub(zmul(rows[1][0], rows[2][2]), zmul(rows[1][2], rows[2][0]))))
        d = zadd(d, zmul(rows[0][2], zsub(zmul(rows[1][0], rows[2][1]), zmul(rows[1][1], rows[2][0]))))
        tot = zadd(tot, d)
    assert tot[1] % 162 == 0 and tot[0] % 162 == 0, (lam, tot)
    assert tot[1] == 0, (lam, tot)
    return tot[0] // 162


# ---------------------------------------------------------------------------
# Ambient / closure multiplicities (exact integer DP) -- the banked route
# ---------------------------------------------------------------------------

_H3 = {}
def hist3(dmax):
    if dmax in _H3: return _H3[dmax]
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4 - e1)]
    arr = [[[0] * (3 * d + 1) for _ in range(3 * d + 1)] for d in range(dmax + 1)]
    arr[0][0][0] = 1
    for (e1, e2) in gens:
        for d in range(1, dmax + 1):
            cur, prev = arr[d], arr[d - 1]
            lim, plim = 3 * d, 3 * (d - 1)
            for A_ in range(e1, lim + 1):
                pA = A_ - e1
                if pA > plim: continue
                prow, crow = prev[pA], cur[A_]
                for B_ in range(e2, lim + 1):
                    pB = B_ - e2
                    if pB > plim: continue
                    v = prow[pB]
                    if v: crow[B_] += v
    _H3[dmax] = arr
    return arr

_P3 = []
for _p in permutations((0, 1, 2)):
    _s = 1
    for _i in range(3):
        for _j in range(_i + 1, 3):
            if _p[_i] > _p[_j]: _s = -_s
    _P3.append((_p, _s))


def multB(d, lam, h3):
    """mult of S_lam in Sym^d(Sym^3 C^3)."""
    if d < 0 or lam[2] < 0 or lam[0] < lam[1] or lam[1] < lam[2] or sum(lam) != 3 * d:
        return 0
    l = (lam[0] + 2, lam[1] + 1, lam[2]); tot = 0
    for pp, s_ in _P3:
        t = (l[pp[0]] - 2, l[pp[1]] - 1, l[pp[2]])
        if min(t) < 0 or t[0] > 3 * d or t[1] > 3 * d: continue
        tot += s_ * h3[d][t[0]][t[1]]
    return tot


def closureB(d, lam, h3):
    """mult of S_lam in C[Omega-bar]_d = C[W]_d / S.C[W]_{d-4}."""
    return multB(d, lam, h3) - multB(d - 4, (lam[0] - 4, lam[1] - 4, lam[2] - 4), h3)


def conductor_table(lam, h3, kmax=12):
    """Least k with def(lam + 6k.1, delta + 6k) = 0, from the multiplicity tables."""
    d = sum(lam) // 3
    m = H_invariants_dim(lam)
    for k in range(kmax + 1):
        lk = (lam[0] + 6 * k, lam[1] + 6 * k, lam[2] + 6 * k)
        if closureB(d + 6 * k, lk, h3) == m:
            return k, m
    return None, m


# ---------------------------------------------------------------------------
# The top-weight criterion
# ---------------------------------------------------------------------------

WT = {'e1': 1, 'e2': -2, 'e3': 0, 'f12': -1, 'f13': 1, 'f23': -2, 'det': -1}
# monomial key = (a1, a2, a3, q12, q13, q23);  det^r implicit

def mono_weight(mon, r):
    a1, a2, a3, q12, q13, q23 = mon
    return a1 - 2 * a2 - q12 + q13 - 2 * q23 - r


def normal_form(poly):
    """Reduce mod Pi = e1 f23 - e2 f13 + e3 f12  (leading term e1 f23)."""
    poly = dict(poly)
    while True:
        bad = None
        for mon, c in poly.items():
            if c and mon[0] >= 1 and mon[5] >= 1:
                bad = mon; break
        if bad is None: break
        c = poly.pop(bad)
        a1, a2, a3, q12, q13, q23 = bad
        # e1 f23 -> e2 f13 - e3 f12
        m1 = (a1 - 1, a2 + 1, a3, q12, q13 + 1, q23 - 1)
        m2 = (a1 - 1, a2, a3 + 1, q12 + 1, q13, q23 - 1)
        poly[m1] = poly.get(m1, 0) + c
        poly[m2] = poly.get(m2, 0) - c
    return {m: c for m, c in poly.items() if c}


def perm_shape(a, Q, pi):
    """Apply pi in S_3 (as a tuple with pi[i] = image of i) to a monomial.
    Returns (a', Q', sign) with sign the wedge-orientation sign only."""
    ap = [0, 0, 0]
    for i in range(3): ap[pi[i]] = a[i]
    qp = [0, 0, 0]              # order: (12), (13), (23)
    PAIRS = [(0, 1), (0, 2), (1, 2)]
    IDX = {(0, 1): 0, (0, 2): 1, (1, 2): 2}
    sign = 1
    for t, (i, j) in enumerate(PAIRS):
        u, v = pi[i], pi[j]
        if u < v: qp[IDX[(u, v)]] += Q[t]
        else:
            qp[IDX[(v, u)]] += Q[t]
            if Q[t] % 2: sign = -sign
    return tuple(ap), tuple(qp), sign


SGN = {}
for _p in permutations(range(3)):
    _s = 1
    for _i in range(3):
        for _j in range(_i + 1, 3):
            if _p[_i] > _p[_j]: _s = -_s
    SGN[_p] = _s


def B_weight_part(ap, qp, r, nu, coeff):
    """Terms of tau-weight exactly nu in B applied to coeff * e^ap f^qp det^r.
    B: e1 -> e1+e2, e2 -> -e1+e2, e3 -> e3, f12 -> 2 f12,
       f13 -> f13+f23, f23 -> -f13+f23, det -> 2 det.
    Every 'down' choice lowers the tau-weight by exactly 3."""
    a1, a2, a3 = ap
    q12, q13, q23 = qp
    Ntop = a1 + a2 - q12 + q13 + q23 - r
    D = Ntop - nu
    if D < 0 or D % 3: return {}
    T = D // 3
    out = {}
    base = coeff * (2 ** q12) * (2 ** r)
    for t1 in range(min(T, a1) + 1):
        for t2 in range(min(T - t1, a2) + 1):
            for t3 in range(min(T - t1 - t2, q13) + 1):
                t4 = T - t1 - t2 - t3
                if t4 < 0 or t4 > q23: continue
                c = base * comb(a1, t1) * comb(a2, t2) * comb(q13, t3) * comb(q23, t4)
                if (a2 - t2 + q23 - t4) % 2: c = -c
                mon = (a1 + a2 - t1 - t2, t1 + t2, a3,
                       q12, q13 + q23 - t3 - t4, t3 + t4)
                out[mon] = out.get(mon, 0) + c
    return out


def theta_B_weight(a, Q, r, nu):
    """pi_nu( B . Theta(a,Q) ) in the big space, as a monomial dict."""
    acc = {}
    for pi in permutations(range(3)):
        ap, qp, wsign = perm_shape(a, Q, pi)
        coeff = wsign * (SGN[pi] ** r if r % 2 else 1)
        part = B_weight_part(ap, qp, r, nu, coeff)
        for m, c in part.items():
            acc[m] = acc.get(m, 0) + c
    return {m: c for m, c in acc.items() if c}


def shapes(lam):
    """Admissible shapes: |a| = p, |Q| = q, n_i = 0 mod 3."""
    l1, l2, l3 = lam
    p, q, r = l1 - l2, l2 - l3, l3
    out = []
    for a1 in range(p + 1):
        for a2 in range(p - a1 + 1):
            a3 = p - a1 - a2
            for q12 in range(q + 1):
                for q13 in range(q - q12 + 1):
                    q23 = q - q12 - q13
                    n1 = a1 + q12 + q13 + r
                    n2 = a2 + q12 + q23 + r
                    n3 = a3 + q13 + q23 + r
                    if n1 % 3 or n2 % 3 or n3 % 3: continue
                    out.append(((a1, a2, a3), (q12, q13, q23)))
    return out


def top_weight_max(lam, shp=None, lo=None):
    """max { nu : pi_nu(B S_lambda^H) != 0 }, scanning nu downwards from mu_max.
    Returns (nu_max, witness_shape) or (None, None) if S_lambda^H = 0 in the
    scanned range.  lo bounds how far down to scan."""
    l1, l2, l3 = lam
    mu_max = l1 - 2 * l3
    r = l3
    if shp is None: shp = shapes(lam)
    if lo is None: lo = mu_max - 12
    for nu in range(mu_max, lo - 1, -1):
        for (a, Q) in shp:
            pol = theta_B_weight(a, Q, r, nu)
            if not pol: continue
            if normal_form(pol):
                return nu, (a, Q)
    return None, None


def conductor_weight(lam, shp=None):
    """Conductor from the top-weight criterion (None if nothing in range)."""
    nu, wit = top_weight_max(lam, shp)
    if nu is None: return None, None
    return Fraction(nu, 6), wit


def attained(lam, shp=None):
    """Is the component at nu* = 6 floor(mu_max/6) nonzero?  Returns witness."""
    l1, l2, l3 = lam
    mu = l1 - 2 * l3
    nus = 6 * (mu // 6)
    if nus < 0: return None
    if shp is None: shp = shapes(lam)
    for (a, Q) in shp:
        pol = theta_B_weight(a, Q, l3, nus)
        if pol and normal_form(pol):
            return (a, Q)
    return None


# ---------------------------------------------------------------------------
# Restricted shape enumeration: only shapes that can possibly contribute at
# nu* = 6 floor(mu_max/6).  Justification (proved in docs/transport_formula.md):
#   * N_k = mu - a_k - 2 q_kbar is ALWAYS divisible by 3 (forced by n_i = 0
#     mod 3), so every achievable nu is divisible by 3;
#   * the S_3 symmetrisation retains exactly the drops T = u+w with
#     T = lambda_1 - a_k (mod 2), so every achievable nu is EVEN;
#   * hence achievable nu = N_k or N_k - 3, whichever is even, and reaching
#     nu* needs  s := a_k + 2 q_kbar  in {eps, eps-3},  eps = mu mod 6.
# By S_3-symmetry of Theta we may take k = 3.
# ---------------------------------------------------------------------------

def allowed_ab(lam):
    """(alpha, beta) = (a_3, q_12) pairs that can reach nu*."""
    l1, l2, l3 = lam
    p, q, r = l1 - l2, l2 - l3, l3
    mu = l1 - 2 * l3
    eps = mu % 6
    out = []
    for s in (eps, eps - 3):
        if s < 0: continue
        for beta in range(0, s // 2 + 1):
            alpha = s - 2 * beta
            if alpha <= p and beta <= q: out.append((alpha, beta))
    return out


def shapes_at(lam, alpha, beta):
    """Admissible shapes with a_3 = alpha, q_12 = beta."""
    l1, l2, l3 = lam
    p, q, r = l1 - l2, l2 - l3, l3
    A, Q = p - alpha, q - beta
    if A < 0 or Q < 0: return []
    out = []
    for a1 in range(A + 1):
        a2 = A - a1
        for q13 in range(Q + 1):
            q23 = Q - q13
            if (a1 + beta + q13 + r) % 3: continue
            if (a2 + beta + q23 + r) % 3: continue
            if (alpha + q13 + q23 + r) % 3: continue
            out.append(((a1, a2, alpha), (beta, q13, q23)))
    return out


def attained_fast(lam):
    """Same answer as attained(), restricted enumeration.  Returns a witness."""
    l1, l2, l3 = lam
    mu = l1 - 2 * l3
    if mu < 0: return None
    nus = 6 * (mu // 6)
    for (alpha, beta) in allowed_ab(lam):
        for (a, Q) in shapes_at(lam, alpha, beta):
            pol = theta_B_weight(a, Q, l3, nus)
            if pol and normal_form(pol):
                return (a, Q)
    return None


def conductor_fast(lam, drop_max=8):
    """c(lambda) from the weight criterion, scanning nu = 6.floor(mu/6) downwards
    in steps of 6.  Returns (c, witness) with c possibly negative (order of
    vanishing) -- the conductor is max(0, c)."""
    l1, l2, l3 = lam
    mu = l1 - 2 * l3
    p, q, r = l1 - l2, l2 - l3, l3
    for j in range(drop_max + 1):
        nu = 6 * (mu // 6) - 6 * j
        eps = mu - nu
        found = None
        for s in (eps, eps - 3):
            if s < 0: continue
            for beta in range(0, min(s // 2, q) + 1):
                alpha = s - 2 * beta
                if alpha > p: continue
                for (a, Q) in shapes_at(lam, alpha, beta):
                    pol = theta_B_weight(a, Q, r, nu)
                    if pol and normal_form(pol):
                        found = (a, Q); break
                if found: break
            if found: break
        if found: return nu // 6, found
    return None, None


# ---------------------------------------------------------------------------
# Fast exact m(lambda): group the 162 elements of H by their characteristic
# polynomial (e1,e2,e3) -- the character only sees that -- and memoise the
# complete homogeneous sequence once per class.
# ---------------------------------------------------------------------------

class MFast:
    def __init__(self, top):
        from collections import Counter
        cnt = Counter(elementary_of(M) for M in H_elements())
        self.classes = list(cnt.items())
        self.top = top
        self.H = []
        for (e1, e2, e3), _ in self.classes:
            h = [ZERO] * (top + 4)
            h[0] = ONE
            if top >= 1: h[1] = e1
            if top >= 2: h[2] = zsub(zmul(e1, h[1]), e2)
            for j in range(3, top + 1):
                h[j] = zadd(zsub(zmul(e1, h[j - 1]), zmul(e2, h[j - 2])),
                            zmul(e3, h[j - 3]))
            self.H.append(h)

    def m(self, lam):
        tot = ZERO
        for ((_, mult), h) in zip(self.classes, self.H):
            def hh(k): return h[k] if 0 <= k <= self.top else ZERO
            R = [[hh(lam[i] - i + j) for j in range(3)] for i in range(3)]
            d = zsub(zmul(R[0][0], zsub(zmul(R[1][1], R[2][2]), zmul(R[1][2], R[2][1]))),
                     zmul(R[0][1], zsub(zmul(R[1][0], R[2][2]), zmul(R[1][2], R[2][0]))))
            d = zadd(d, zmul(R[0][2], zsub(zmul(R[1][0], R[2][1]), zmul(R[1][1], R[2][0]))))
            tot = zadd(tot, (d[0] * mult, d[1] * mult))
        assert tot[1] == 0 and tot[0] % 162 == 0, (lam, tot)
        return tot[0] // 162


# ---------------------------------------------------------------------------
# The explicit attainment construction (the positive half of the theorem).
#
# Target nu* = 6(floor(mu/6) - [family]),  D = mu - nu*  (= eps, or 7 on the
# family lambda_1 = lambda_2, mu = 1 mod 6).  We build a shape whose slot 3 has
#     s_3 = a_3 + 2 q_12 = s  in {D, D-3},
# and whose OTHER two slots are pushed strictly out of range,
#     s_1 = a_1 + 2 q_23  and  s_2 = a_2 + 2 q_13   >=  s + 3   (s + 6 if T=1),
# so that the class k = 3 alone contributes at nu*, with no interference; and,
# when T = 1, with (a_1 - a_2, q_13 - q_23) != (0,0) so the T=1 coefficient
# does not vanish.
# ---------------------------------------------------------------------------

def construct(lam):
    """Explicit witness shape, or None.  Rules only -- no search over shapes."""
    l1, l2, l3 = lam
    p, q, r = l1 - l2, l2 - l3, l3
    mu = l1 - 2 * l3
    if mu < 0: return None
    fam = (p == 0 and mu % 6 == 1)
    D = 7 if fam else mu % 6
    for s in (D, D - 3):
        if s < 0: continue
        T = 0 if (mu - s) % 2 == 0 else 1
        sep = s + 3 + 3 * T            # required s_1, s_2
        for beta in range(0, min(s // 2, q) + 1):
            alpha = s - 2 * beta
            if alpha > p: continue
            A, Q = p - alpha, q - beta
            if A < 0 or Q < 0: continue
            c = (-beta - r) % 3
            # candidate splits: push the wedges apart first, then the singles
            cands = []
            base = Q // 2
            for d13 in range(0, 7):
                for q13 in (base + d13, base - d13):
                    if 0 <= q13 <= Q: cands.append((q13, Q - q13))
            for (q13, q23) in cands:
                for a1 in range(0, A + 1):
                    a2 = A - a1
                    if (a1 + q13) % 3 != c: continue
                    if a1 + 2 * q23 < sep or a2 + 2 * q13 < sep: continue
                    if T == 1 and a1 == a2 and q13 == q23: continue
                    return ((a1, a2, alpha), (beta, q13, q23))
    return None
