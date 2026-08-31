#!/usr/bin/env python3
"""
Session 24 -- World A census: all GL_2-orbit closures in Sym^4 C^2.

Exact integer arithmetic throughout.  For every orbit closure X we produce
  mult_X(lambda)  = mult_lambda C[X]_delta
  m_X(lambda)     = dim (S_lambda^*)^{H_X}   (Peter-Weyl / orbit side)
  def_X           = m_X - mult_X
each by two independent routes, and then search all ordered pairs (A,B) for
DEFICIT-DRIVEN obstructions:  mult_B > mult_A  while  m_B <= m_A.

Weight convention: lambda = (a,b), a+b = 4*delta, a >= b >= 0.  We index by b.
C[W]_delta = Sym^delta(Sym^4 V); z_i has weight (4-i, i).
"""
from functools import lru_cache
from fractions import Fraction
import itertools, sys

DMAX = 14

# ---------------------------------------------------------------- plethysm
@lru_cache(maxsize=None)
def Mrow(delta):
    """dict b -> #monomials of degree delta in z_0..z_4 with y-weight b."""
    cur = {0: 1}
    for _ in range(delta):
        nxt = {}
        # multiply by (z_0+...+z_4) is wrong; do proper monomial count via DP
        pass
    # DP over the 5 generators
    cur = {0: 1}
    for i in range(5):          # generator z_i contributes i to b, any power
        nxt = {}
        for b, c in cur.items():
            nxt[b] = nxt.get(b, 0) + c
        cur = nxt
    # the above is wrong too; do it cleanly:
    return _Mrow(delta)

@lru_cache(maxsize=None)
def _Mrow(delta):
    # number of (n0..n4) >=0 with sum = delta and sum i*ni = b
    dp = {(0, 0): 1}
    for i in range(5):
        ndp = {}
        for (n, b), c in dp.items():
            k = 0
            while n + k <= delta:
                key = (n + k, b + i * k)
                ndp[key] = ndp.get(key, 0) + c
                k += 1
        dp = ndp
    out = {}
    for (n, b), c in dp.items():
        if n == delta:
            out[b] = out.get(b, 0) + c
    return out

def M(delta, b):
    if delta < 0 or b < 0 or b > 4 * delta:
        return 0
    return _Mrow(delta).get(b, 0)

def P(delta, b):
    """mult of S_(4delta-b, b) in Sym^delta(Sym^4 V)."""
    if delta < 0 or b < 0 or 2 * b > 4 * delta:
        return 0
    return M(delta, b) - M(delta, b - 1)

# --------------------------------------------------- hypersurface closures
def mult_hyp(delta, b, e, w):
    """C[W]/(F), deg F = e, weight of F = det^w  (i.e. lambda_F=(w,w))."""
    return P(delta, b) - P(delta - e, b - w)

MULT = {
    'Iz':  lambda d, b: mult_hyp(d, b, 2, 4),    # {I=0},  equianharmonic
    'Jz':  lambda d, b: mult_hyp(d, b, 3, 6),    # {J=0},  harmonic  (World A)
    'Ac':  lambda d, b: mult_hyp(d, b, 6, 12),   # {I^3-cJ^2=0}, generic j
    'D':   lambda d, b: mult_hyp(d, b, 6, 12),   # {disc=0} = A_27
    # closed forms below are ROUTE 2; route 1 is the exact substitution rank
    # in wk5_s24_param.py, and the two are asserted equal in wk5_s24_checks.py.
    #   C[Q]_delta = Sym^{2delta}(Sym^2 V) for delta >= 2, but is SHORT by one
    #   copy of S_(2,2) at delta = 1 (the cone {q^2} is not projectively normal).
    'Q':   lambda d, b: (0 if (d == 1 and b == 2) else
                         (1 if (b % 2 == 0 and 2 * b <= 4 * d) else 0)),
    'tau': lambda d, b: 1 if (b <= d and b != 1) else 0,
    'Gam': lambda d, b: 1 if b == 0 else 0,
}

# ------------------------------------------------------- Peter-Weyl counts
def N_Jz(a, b):
    """m for H = mu_4^2 |x S_2 (stabiliser of x^4+y^4).  Route: monomial
    character count on S_lambda^* = Sym^{a-b} V^* (x) det^{-b}."""
    s = a - b
    idx = [i for i in range(s + 1) if (i + b) % 4 == 0 and (s - i + b) % 4 == 0]
    n = 0
    for i in idx:
        j = s - i
        if i < j:
            n += 1
        elif i == j:
            n += 1 if b % 2 == 0 else 0
    return n

def m_Ac(a, b):
    """H = {diag(z,e): z^4=e^4=1, (ze)^2=1} |x S_2, order 16 (generic quartic)."""
    s = a - b
    idx = []
    for i in range(s + 1):
        # e = z^{-1}:   z^{ (s-2i) }  must be 1 for all z in mu_4
        if (s - 2 * i) % 4 != 0:
            continue
        # z=1, e=-1:   (-1)^{s-i+b} = 1
        if (s - i + b) % 2 != 0:
            continue
        idx.append(i)
    n = 0
    for i in idx:
        j = s - i
        if i < j:
            n += 1
        elif i == j:
            n += 1 if b % 2 == 0 else 0
    return n

def m_Q(a, b):
    """H = {diag(t,u): (tu)^2=1} |x S_2 (stabiliser of x^2y^2)."""
    s = a - b
    # torus diag(t,t^{-1}): weight on x^i y^{s-i} (x) det^{-b} is  -i+(s-i) = s-2i
    if s % 2 != 0:
        return 0
    i = s // 2
    # diag(1,-1):  (-1)^{-(s-i)-b} = (-1)^{s-i+b} = (-1)^{i+b} ; need even
    if (i + b) % 2 != 0:
        return 0
    # swap: fixes x^i y^i, det factor (-1)^b
    return 1 if b % 2 == 0 else 0

def m_D(a, b):
    """H_D = stabiliser of x^2(x^2-y^2) (root type 2+1+1).
    PGL_2-stabiliser = the involution swapping the two simple roots, order 2;
    with the mu_4 of scalars, |H_D| = 8, and it is DIAGONAL:
        H_D = {diag(al,be) : al^4 = 1, (al be)^2 = 1}
    -- exactly the diagonal part of H_{A_c}, so H_{A_c} = H_D |x S_2."""
    s = a - b
    n = 0
    for i in range(s + 1):
        if (s - 2 * i) % 4 != 0:      # alpha in mu_4
            continue
        if (s - i + b) % 2 != 0:      # epsilon = +-1
            continue
        n += 1
    return n

M_FUN = {
    'Jz':  N_Jz,
    'Ac':  m_Ac,
    'D':   m_D,
    'Q':   m_Q,
    'tau': None,   # filled below: [b <= delta]
    'Gam': None,   # [b == 0]
    'Iz':  None,   # by ray route
}

# ------------------------------------------------- ray route for m (generic)
def m_by_ray(name, delta, b, e, w, kmax=40):
    """m(lambda) = stable value of mult_{lambda + k(w,w)} in degree delta+ke."""
    f = MULT[name]
    seen = []
    for k in range(kmax):
        seen.append(f(delta + k * e, b + k * w))
        if len(seen) >= 6 and len(set(seen[-5:])) == 1:
            return seen[-1], k
    raise RuntimeError("ray did not stabilise: %s %s %s" % (name, delta, b))

# ---------------------------------------------------------------- assemble
def m_of(name, delta, b):
    a = 4 * delta - b
    if name == 'tau':
        return 1 if b <= delta else 0
    if name == 'Gam':
        return 1 if b == 0 else 0
    if name == 'Iz':
        return m_by_ray('Iz', delta, b, 3, 6)[0]     # boundary cut by J
    return M_FUN[name](a, b)

NAMES = ['Gam', 'tau', 'Q', 'Iz', 'Jz', 'Ac', 'D']
DIMS  = {'Gam': 2, 'tau': 3, 'Q': 3, 'Iz': 4, 'Jz': 4, 'Ac': 4, 'D': 4}

def build(dmax=DMAX):
    tab = {}
    for name in NAMES:
        for d in range(1, dmax + 1):
            for b in range(0, 2 * d + 1):
                mu = MULT[name](d, b)
                mm = m_of(name, d, b)
                tab[(name, d, b)] = (mm, mu, mm - mu)
    return tab

if __name__ == '__main__':
    tab = build()
    bad = [(k, v) for k, v in tab.items() if v[2] < 0]
    print("negative deficits (must be empty):", bad[:5], "count", len(bad))
    print("built", len(tab), "entries, delta <=", DMAX)
