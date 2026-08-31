"""Session 26 -- core routines, derived independently of scripts/ambient_screen.py.

Everything exact (Python integers and Fraction).

CONVENTIONS, fixed once and never dualised again
------------------------------------------------
V = C^9 = M_3(C) with basis e_1..e_9 (the matrix coordinates).
W = Sym^3 V^* = cubic forms on V, so a point of W is a cubic form F.
C[W]_delta = Sym^delta(W^*) = polynomials of degree delta in the COEFFICIENT
functionals c_alpha, where alpha runs over exponent vectors of degree 3 and
c_alpha(F) = the coefficient of the monomial y^alpha in F (y = the coordinate
functions on V, dual basis to e).

GL(V) acts on C[W] by (g.P)(F) = P(g^{-1}.F).  Under this action c_alpha
transforms exactly as e^alpha in Sym^3 V, so:

    weight(c_alpha) = alpha           (a non-negative vector, |alpha| = 3)
    E_ij . c_alpha  = alpha_j * c_{alpha - eps_j + eps_i}     (i != j)

and E_ij acts on products as a derivation.  A highest-weight vector of weight
lam is a weight-lam vector killed by E_{i,i+1} for all i.  NOTHING in this file
refers to S_lam or S_lam^*; the weights are read off the monomials directly.

Because every alpha has non-negative entries, a weight vector of weight
(lam_1..lam_r, 0..0) can only involve c_alpha supported on the first r
coordinates.  So all of the length-r work happens in r variables.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement as cwr
from math import factorial


# --------------------------------------------------------------- partitions
def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def z_of(rho):
    """z_rho = prod p^{m_p} m_p!  (so |C_rho| = N!/z_rho)."""
    z, cnt = 1, {}
    for p in rho:
        cnt[p] = cnt.get(p, 0) + 1
    for p, m in cnt.items():
        z *= (p ** m) * factorial(m)
    return z


# ------------------------------------------------- S_N characters (MN rule)
@lru_cache(maxsize=None)
def chi_sn(lam, rho):
    """chi^lam(rho) by Murnaghan-Nakayama, recursion on rim hooks."""
    lam = tuple(x for x in lam if x)
    if not rho:
        return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    total = 0
    L = len(lam)
    # remove a rim hook of size r in every possible way
    # standard: work with first-column hook lengths (beta numbers)
    beta = [lam[j] + (L - 1 - j) for j in range(L)]
    bset = set(beta)
    for i in range(L):
        b = beta[i] - r
        if b < 0 or b in bset:
            continue
        nb = sorted([x for j, x in enumerate(beta) if j != i] + [b], reverse=True)
        height = nb.index(b) - i
        new = tuple(nb[j] - (L - 1 - j) for j in range(L))
        if any(x < 0 for x in new):
            continue
        total += ((-1) ** height) * chi_sn(tuple(x for x in new if x), rest)
    return total


# ------------------------------------- m_det: the symmetric Kronecker count
def _tau_split(rho):
    """Keep odd parts; split each even part r into two parts r/2."""
    out = []
    for r in rho:
        if r % 2:
            out.append(r)
        else:
            out += [r // 2, r // 2]
    return tuple(sorted(out, reverse=True))


def m_det(lam, n=3, delta=None):
    """dim (S_lam(C^{n^2}))^{Stab(det_n)}.

    Stab(det_n) = {X -> AXB : det A det B = 1} |x <transpose>, of dimension
    2n^2-2.  On the identity component, S_lam(C^n (x) C^n) = sum_{mu,nu}
    g(lam,mu,nu) S_mu (x) S_nu, and a summand is invariant iff both factors are
    one-dimensional with matching det-power, i.e. mu = nu = (delta^n).  Hence
    the identity-component count is the rectangular Kronecker g(lam,rect,rect).

    On the transpose coset, k : X -> A X^T B has
        tr(k^{2m})   = tr(M^m)^2 ,   tr(k^{2m+1}) = tr(M^{2m+1}),   M = A B^T,
    with M Haar-distributed on SL_n; so p_rho(k) = p_{tau(rho)}(M) with tau as
    above, and integrating over SL_n picks the coefficient of s_{(delta^n)},
    giving chi^{(delta^n)}(tau(rho)).

    (Both halves rederived here; see docs/isotypic_rank.md.)
    """
    lam = tuple(x for x in lam if x)
    N = sum(lam)
    if delta is None:
        assert N % n == 0
        delta = N // n
    if N != n * delta or len(lam) > n * n:
        return 0
    rect = tuple([delta] * n)
    s = Fraction(0)
    for rho in partitions(N):
        c = chi_sn(lam, rho)
        if c:
            s += Fraction(c, z_of(rho)) * (chi_sn(rect, rho) ** 2
                                           + chi_sn(rect, _tau_split(rho)))
    s /= 2
    assert s.denominator == 1, (lam, s)
    return int(s)


# ------------------------------ ambient room, ROUTE 1: weight multiplicities
def cubic_exponents(r):
    """Exponent vectors alpha of degree 3 in r variables, lex-sorted."""
    out = []
    for c in cwr(range(r), 3):
        a = [0] * r
        for i in c:
            a[i] += 1
        out.append(tuple(a))
    return sorted(out, reverse=True)


def weight_counts(delta, r):
    """K[beta] = #{ degree-delta monomials in the c_alpha with weight beta }."""
    exps = cubic_exponents(r)
    cur = {(0,) * r: 1}
    # multisets of size delta: iterate over the exponent list, choosing
    # multiplicities, to avoid over-counting orderings
    for idx, a in enumerate(exps):
        nxt = {}
        rem_slots = delta
        for beta, cnt in cur.items():
            nxt[beta] = nxt.get(beta, 0) + cnt
        cur_full = dict(cur)
        # add k copies of a, k >= 1, tracking total degree separately
        # simpler: full DP over (used, beta)
        break
    # full DP
    dp = {(0, (0,) * r): 1}
    for a in exps:
        nd = {}
        for (used, beta), cnt in dp.items():
            k = 0
            while used + k <= delta:
                nb = tuple(beta[i] + k * a[i] for i in range(r))
                key = (used + k, nb)
                nd[key] = nd.get(key, 0) + cnt
                k += 1
        dp = nd
    return {beta: c for (used, beta), c in dp.items() if used == delta}


def a_weights(lam, delta, r=None):
    """mult of S_lam in Sym^delta(Sym^3 C^r), by the Weyl alternating sum over
    weight multiplicities:  a = sum_{w in S_r} sgn(w) K(lam + rho - w rho)."""
    lam = tuple(x for x in lam if x)
    if r is None:
        r = max(len(lam), 1)
    if len(lam) > r or sum(lam) != 3 * delta:
        return 0
    lam = tuple(lam) + (0,) * (r - len(lam))
    K = weight_counts(delta, r)
    rho = tuple(r - 1 - i for i in range(r))
    from itertools import permutations
    tot = 0
    for perm in permutations(range(r)):
        sgn = 1
        for i in range(r):
            for j in range(i + 1, r):
                if perm[i] > perm[j]:
                    sgn = -sgn
        beta = tuple(lam[i] + rho[i] - rho[perm[i]] for i in range(r))
        if min(beta) < 0:
            continue
        tot += sgn * K.get(beta, 0)
    return tot


# --------------------------- ambient room, ROUTE 1b: symmetric-function plethysm
@lru_cache(maxsize=None)
def _pleth(delta, d=3):
    """h_delta[h_d] in the power-sum basis, as a tuple of (tau, coeff)."""
    inner = list(partitions(d))
    acc = {}
    for rho in partitions(delta):
        cur = {(): Fraction(1, z_of(rho))}
        for r in rho:
            nxt = {}
            for tau, c in cur.items():
                for sig in inner:
                    t2 = tuple(sorted(tau + tuple(r * s for s in sig), reverse=True))
                    nxt[t2] = nxt.get(t2, Fraction(0)) + c * Fraction(1, z_of(sig))
            cur = nxt
        for t, c in cur.items():
            acc[t] = acc.get(t, Fraction(0)) + c
    return tuple(sorted(acc.items()))


def a_pleth(lam, delta, d=3, nvars=9):
    """mult of S_lam in Sym^delta(Sym^d C^nvars), via power sums."""
    lam = tuple(x for x in lam if x)
    if sum(lam) != delta * d or len(lam) > nvars:
        return 0
    s = sum(c * chi_sn(lam, tau) for tau, c in _pleth(delta, d))
    assert s.denominator == 1, (lam, s)
    return int(s)


# ------------------ ambient room, ROUTE 1 (fast): Weyl alternating sum over
# ------------------ weight-multiplicity COUNTS (no plethysm identity used)
def _count_weight(delta, r, beta):
    """#{degree-delta monomials in the c_alpha with weight beta}, counted by
    recursion over the exponent list.  Same enumeration as weight_basis, but
    counting only."""
    exps = cubic_exponents(r)
    ne = len(exps)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def rec(idx, left, need):
        if left == 0:
            return 1 if all(x == 0 for x in need) else 0
        if idx == ne or sum(need) != 3 * left:
            return 0
        a = exps[idx]
        kmax = left
        for t in range(r):
            if a[t]:
                kmax = min(kmax, need[t] // a[t])
        tot = 0
        for k in range(kmax + 1):
            tot += rec(idx + 1, left - k, tuple(need[t] - k * a[t] for t in range(r)))
        return tot

    return rec(0, delta, tuple(beta))


def a_weyl(lam, delta, r=None):
    """a(lam,delta) = sum_{w in S_r} sgn(w) K(lam + rho - w.rho)."""
    from itertools import permutations
    lam = tuple(x for x in lam if x)
    if r is None:
        r = max(len(lam), 1)
    if len(lam) > r or sum(lam) != 3 * delta:
        return 0
    lam = tuple(lam) + (0,) * (r - len(lam))
    rho = tuple(r - 1 - i for i in range(r))
    tot = 0
    for perm in permutations(range(r)):
        sgn = 1
        for i in range(r):
            for j in range(i + 1, r):
                if perm[i] > perm[j]:
                    sgn = -sgn
        beta = tuple(lam[i] + rho[i] - rho[perm[i]] for i in range(r))
        if min(beta) < 0:
            continue
        tot += sgn * _count_weight(delta, r, beta)
    return tot
