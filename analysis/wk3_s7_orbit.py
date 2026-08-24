"""Week 3, session 7 — the first deficit table of det_3.
For each delta and each lambda |- 3*delta (<= 9 rows):
  amb(lam)  = mult of S_lam in Sym^delta(Sym^3 C^9)   [plethysm, MN]
  orb(lam)  = mult of S_lam* in C[GL9 . det3]         [symmetric Kronecker sg]
Then closure <= min(amb, orb) forces:
  orb - amb > 0  =>  deficit def(lam, delta) >= orb - amb   (first proven deficits)
  amb - orb > 0  =>  ideal of the orbit closure contains >= amb - orb copies of S_lam
                     (first proven equation modules)
Validations: delta=1 anchor; total-dimension identity; parity anchor sg((1^9)) = 0.
"""
import math, sys
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

sys.setrecursionlimit(100000)

@lru_cache(maxsize=None)
def chi(lam, mu):
    if sum(lam) == 0: return 1
    t, rest = mu[0], mu[1:]
    k = len(lam)
    beta = [lam[i] + (k-1-i) for i in range(k)]
    S = set(beta); tot = 0
    for f in beta:
        g = f - t
        if g >= 0 and g not in S:
            between = sum(1 for x in S if g < x < f)
            nb = sorted((S - {f}) | {g}, reverse=True)
            kk = len(nb)
            nl = tuple(x - (kk-1-i) for i, x in enumerate(nb))
            nl = tuple(p for p in nl if p > 0)
            tot += (-1)**between * chi(nl, rest)
    return tot

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n-k, k):
            yield (k,) + rest

def zval(mu):
    from collections import Counter
    cc = Counter(mu); r = 1
    for k, m in cc.items(): r *= k**m*math.factorial(m)
    return r

H3 = {(1,1,1): Fraction(1,6), (2,1): Fraction(1,2), (3,): Fraction(1,3)}
def h3_scaled(k):
    return {tuple(sorted((k*a for a in part), reverse=True)): c for part, c in H3.items()}
def dict_mul_p(P, Q):
    R = defaultdict(Fraction)
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = tuple(sorted(m1+m2, reverse=True))
            R[m] += c1*c2
    return R
def h_pleth_h3(delta):
    total = defaultdict(Fraction)
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            term = dict_mul_p(term, h3_scaled(part))
        zm = zval(mu)
        for m, c in term.items():
            total[m] += c/zm
    return total

def sq_class(nu):
    out = []
    for p in nu:
        if p % 2 == 0: out += [p//2, p//2]
        else: out.append(p)
    return tuple(sorted(out, reverse=True))

def dim9(lam):
    """dim of S_lam(C^9), hook content formula."""
    lam = list(lam)
    num, den = 1, 1
    for i, li in enumerate(lam):
        for j in range(li):
            num *= 9 + j - i
            arm = li - j - 1
            leg = sum(1 for i2 in range(i+1, len(lam)) if lam[i2] > j)
            den *= arm + leg + 1
    return num // den

MAXD = int(sys.argv[1]) if len(sys.argv) > 1 else 7

for delta in range(1, MAXD+1):
    n = 3*delta
    P = h_pleth_h3(delta)
    mu = tuple([delta]*3)
    parts_n = [p for p in partitions(n)]
    fact = math.factorial(n)
    # precompute chi(mu, nu) and chi(mu, sq(nu))
    rows = []
    dimtot = 0
    for lam in parts_n:
        if len(lam) > 9: continue
        amb = sum(cf*chi(lam, nu) for nu, cf in P.items())
        assert amb.denominator == 1
        amb = int(amb)
        if amb: dimtot += amb*dim9(lam)
        g = sum((fact//zval(nu))*chi(lam, nu)*chi(mu, nu)**2 for nu in parts_n)
        assert g % fact == 0
        g //= fact
        tw = sum((fact//zval(nu))*chi(lam, nu)*chi(mu, sq_class(nu)) for nu in parts_n)
        assert tw % fact == 0
        tw //= fact
        assert (g + tw) % 2 == 0
        orb = (g + tw)//2
        assert orb >= 0 and amb >= 0
        if amb or orb: rows.append((lam, amb, orb))
    # validation: total dimension
    target = math.comb(164 + delta, delta)
    print(f"delta={delta}: sum amb*dim = {dimtot} vs dim Sym^{delta}(Sym^3C^9) = {target}",
          "OK" if dimtot == target else "FAIL")
    exc_def = [(l, a, o) for l, a, o in rows if o > a]
    exc_eqn = [(l, a, o) for l, a, o in rows if a > o]
    print(f"  weights: {len(rows)};  orbit>amb (proven deficits): {len(exc_def)};  amb>orb (proven equations): {len(exc_eqn)}")
    for l, a, o in exc_def[:12]:
        print(f"    DEFICIT  {l}: amb={a} orb={o}  def>={o-a}")
    for l, a, o in exc_eqn[:12]:
        print(f"    EQUATION {l}: amb={a} orb={o}  ideal mult>={a-o}")
    tot_def = sum(o-a for l, a, o in exc_def)
    tot_eqn = sum(a-o for l, a, o in exc_eqn)
    print(f"  total proven deficit >= {tot_def};  total proven equation mult >= {tot_eqn}")
    sys.stdout.flush()
