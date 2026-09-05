"""
Session 50 — LMR divisibility evaluator.

Tests, for a quartic form P in N variables and a (k+3)-plane F (given by a
16xF integer matrix B):

    P | det_{k+3}( B^T H_P(By) B )     as polynomials in y_1..y_{k+3},

where H_P is the NxN Hessian of P.  Zero remainder <=> the LMR degree-2n(n-1)
equation vanishes at P.

Method (exact over F_p): specialise y_2..y_{k+3} to random field elements a,
leaving t = y_1.  Then
    p_a(t) = P(x(t))                 deg <= d          (d=4)
    g_a(t) = det( M0 + M1 t + M2 t^2 )   deg <= (k+3)(d-2)
with M_j = B^T H_j B and H(x(t)) = H0 + H1 t + H2 t^2.  r_a = g_a mod p_a.
P | G  <=>  r_a == 0 for all a (checked at many random a, >=2 primes).
A single r_a != 0 certifies P does NOT divide G over Q.

No dependence on the worker pipeline; only python-flint.
"""
import random
from flint import nmod_poly, nmod_mat

# ---------- forms as monomial lists: list of (coeff:int, exps:tuple(N)) ----------

def _emono(N, coeff, pairs):
    e = [0] * N
    for (i, k) in pairs:
        e[i] += k
    return (coeff, tuple(e))

def det_form(idx):
    """Determinant of the matrix whose (r,c) entry is variable idx[r][c]. n = len(idx)."""
    import itertools
    n = len(idx)
    terms = []
    for perm in itertools.permutations(range(n)):
        sign = _perm_sign(perm)
        pairs = [(idx[r][perm[r]], 1) for r in range(n)]
        terms.append(_emono_from_pairs(sign, pairs))
    return terms

def per_form(idx):
    import itertools
    n = len(idx)
    terms = []
    for perm in itertools.permutations(range(n)):
        pairs = [(idx[r][perm[r]], 1) for r in range(n)]
        terms.append(_emono_from_pairs(1, pairs))
    return terms

def _emono_from_pairs(coeff, pairs):
    # exps built later once N known; store as (coeff, dict) then normalise
    d = {}
    for (i, k) in pairs:
        d[i] = d.get(i, 0) + k
    return (coeff, d)

def _perm_sign(perm):
    perm = list(perm); s = 1
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s

def normalise(terms_dictform, N):
    """Turn (coeff, {var:exp}) list into (coeff, tuple exps len N), merging."""
    from collections import defaultdict
    acc = defaultdict(int)
    for coeff, d in terms_dictform:
        e = [0]*N
        for i, k in d.items():
            e[i] += k
        acc[tuple(e)] += coeff
    return [(c, e) for e, c in acc.items() if c != 0]

def scale_var_product(terms_dictform, extra_var):
    """Multiply every monomial by variable extra_var (for x0 * per3 padding)."""
    out = []
    for coeff, d in terms_dictform:
        d2 = dict(d); d2[extra_var] = d2.get(extra_var, 0) + 1
        out.append((coeff, d2))
    return out

# ---------- derivatives / Hessian on monomial-tuple forms ----------

def deriv(terms, i):
    out = []
    for c, e in terms:
        if e[i] > 0:
            e2 = list(e); c2 = c * e2[i]; e2[i] -= 1
            out.append((c2, tuple(e2)))
    return out

def hessian_monlists(terms, N):
    grad = [deriv(terms, i) for i in range(N)]
    H = [[None]*N for _ in range(N)]
    for i in range(N):
        gi = grad[i]
        for j in range(N):
            H[i][j] = deriv(gi, j)
    return H

def eval_monlist(ml, xnum, p):
    s = 0
    for c, e in ml:
        term = c % p
        if term == 0:
            continue
        for k, ek in enumerate(e):
            if ek:
                term = term * pow(xnum[k], ek, p) % p
        s = (s + term) % p
    return s

def hessian_at(H, xnum, p, N):
    return [[eval_monlist(H[i][j], xnum, p) for j in range(N)] for i in range(N)]

# ---------- Lagrange interpolation over F_p ----------

def lagrange(nodes, vals, p):
    """Return nmod_poly interpolating (nodes[i] -> vals[i])."""
    P = nmod_poly([0], p)
    n = len(nodes)
    for i in range(n):
        num = nmod_poly([vals[i] % p], p)
        den = 1
        for j in range(n):
            if j == i:
                continue
            num = num * nmod_poly([(-nodes[j]) % p, 1], p)
            den = den * ((nodes[i] - nodes[j]) % p) % p
        inv = pow(den, p-2, p)
        num = num * nmod_poly([inv], p)
        P = P + num
    return P

# ---------- the divisibility test ----------

def eval_form(terms, xnum, p):
    s = 0
    for c, e in terms:
        term = c % p
        for k, ek in enumerate(e):
            if ek:
                term = term * pow(xnum[k], ek, p) % p
        s = (s + term) % p
    return s

def matpoly_from_H(H, B, a, p, N, F, dform):
    """
    x(t) = B @ [t, a_2..a_F], H(x(t)) = H0 + H1 t + H2 t^2 (H quadratic).
    Return M0,M1,M2 (F x F) with M_j = B^T H_j B, each an nmod_mat.
    """
    # H(x(t)) is degree (dform-2) in t (Hessian entries have degree dform-2,
    # x(t) linear in t).  The 3-node fit below assumes degree <= 2, i.e.
    # dform <= 4.  Guard against silent truncation for higher-degree forms.
    assert dform <= 4, ("matpoly_from_H uses a quadratic-in-t fit valid only for "
                        "dform<=4; for dform>=5 the Hessian is higher degree in t "
                        "and must be interpolated at dform-1 nodes.")
    def xnum(t):
        col = [t] + list(a)              # length F
        return [sum(B[r][c]*col[c] for c in range(F)) % p for r in range(N)]
    Hm1 = hessian_at(H, xnum((-1) % p), p, N)
    H0  = hessian_at(H, xnum(0), p, N)
    Hp1 = hessian_at(H, xnum(1), p, N)
    inv2 = pow(2, p-2, p)
    def combine(f):
        return [[ f(Hm1[i][j], H0[i][j], Hp1[i][j]) for j in range(N)] for i in range(N)]
    HH0 = H0
    HH1 = combine(lambda m,z,p1: (p1 - m) * inv2 % p)
    HH2 = combine(lambda m,z,p1: ((p1 + m) * inv2 - z) % p)
    def BTHB(Hk):
        # M = B^T Hk B  (F x F)
        # first T = Hk @ B  (N x F)
        T = [[ sum(Hk[r][s]*B[s][c] for s in range(N)) % p for c in range(F)] for r in range(N)]
        M = [[ sum(B[r][c2]*T[r][c] for r in range(N)) % p for c in range(F)] for c2 in range(F)]
        return M
    return BTHB(HH0), BTHB(HH1), BTHB(HH2)

def det_at_t(M0, M1, M2, t, p, F):
    ent = [[ (M0[i][j] + M1[i][j]*t + M2[i][j]*t*t) % p for j in range(F)] for i in range(F)]
    flat = [ent[i][j] for i in range(F) for j in range(F)]
    return int(nmod_mat(F, F, flat, p).det())

def remainder_one(terms, H, B, a, p, N, F, dform):
    """Return (r_coeffs list, pdeg, gdeg) for one specialisation a."""
    M0, M1, M2 = matpoly_from_H(H, B, a, p, N, F, dform)
    edeg = (F) * (dform - 2)          # (k+3)(d-2); F = k+3
    # g_a(t) = det(M(t)), degree <= edeg
    gnodes = list(range(edeg + 1))
    gvals = [det_at_t(M0, M1, M2, t, p, F) for t in gnodes]
    g = lagrange(gnodes, gvals, p)
    # p_a(t) = P(x(t)), degree <= dform
    def xnum(t):
        col = [t] + list(a)
        return [sum(B[r][c]*col[c] for c in range(F)) % p for r in range(N)]
    pnodes = list(range(dform + 1))
    pvals = [eval_form(terms, xnum(t), p) for t in pnodes]
    pa = lagrange(pnodes, pvals, p)
    if pa.degree() < 1:
        return None, pa.degree(), g.degree()   # degenerate line, skip
    r = g % pa
    return r, pa.degree(), g.degree()

def test_divisibility(terms, N, B, F, dform, p, nsamples=6, seed=0):
    """
    Returns dict with: verdict ('DIVIDES'/'NOT_DIVIDES'/'G_ZERO'),
    per-sample remainders, whether G is identically 0.
    """
    H = hessian_monlists(terms, N)
    rng = random.Random(seed)
    results = []
    any_nonzero_r = False
    all_g_zero = True
    for s in range(nsamples):
        a = [rng.randrange(1, p) for _ in range(F-1)]
        r, pdeg, gdeg = remainder_one(terms, H, B, a, p, N, F, dform)
        if r is None:
            continue
        rz = r.is_zero()
        gzero = (gdeg < 0)          # g identically zero on this line
        if not gzero:
            all_g_zero = False
        if not rz:
            any_nonzero_r = True
        results.append(dict(a=a, r_is_zero=bool(rz),
                            r_coeffs=[int(c) for c in r.coeffs()],
                            pdeg=pdeg, gdeg=gdeg))
    if all_g_zero:
        verdict = 'G_ZERO'
    elif any_nonzero_r:
        verdict = 'NOT_DIVIDES'
    else:
        verdict = 'DIVIDES'
    return dict(verdict=verdict, results=results, p=p, seed=seed,
                any_nonzero_r=any_nonzero_r, all_g_zero=all_g_zero)

# ---------- Hessian-rank audit (Katz): rank of H_P at a random point of {P=0} ----------

def rank_H_at_point(terms, N, p, point):
    """Rank of the NxN Hessian at an explicit point."""
    H = hessian_monlists(terms, N)
    Hx = hessian_at(H, point, p, N)
    flat = [Hx[i][j] for i in range(N) for j in range(N)]
    return int(nmod_mat(N, N, flat, p).rank())

def rank_H_generic(terms, N, p, seed=0):
    rng = random.Random(seed)
    point = [rng.randrange(1, p) for _ in range(N)]
    return rank_H_at_point(terms, N, p, point), point

def line_root_on_zero(terms, N, p, rng, active):
    """
    Return a point on {P=0}: fix random values on `active` variables, then solve
    the univariate P=0 in active[0] for an F_p root.
    """
    for _ in range(500):
        x = [0]*N
        for i in active:
            x[i] = rng.randrange(0, p)
        j = active[0]
        deg = max(sum(e) for _, e in terms)
        nodes = list(range(deg+1))
        vals = []
        for t in nodes:
            xx = list(x); xx[j] = t
            vals.append(eval_form(terms, xx, p))
        poly = lagrange(nodes, vals, p)
        rts = poly.roots()
        if rts:
            x[j] = int(rts[0][0])
            if eval_form(terms, x, p) == 0:
                return x
    return None
