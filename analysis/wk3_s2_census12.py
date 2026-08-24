"""Week 3, session 2 — (A) delta = 12 census via conjugate-partition MN;
(B) symmetric Kronecker tables sg(lam, (d^3), (d^3)) for d <= 3 with parity anchors;
(C) stabilizer diagnostics of the two boundary components."""
import itertools, math, sys
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict, Counter
import numpy as np

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
    c = Counter(mu); r = 1
    for k, m in c.items(): r *= k**m*math.factorial(m)
    return r

# ---------- (A) plethysm census ----------
H3 = {(1,1,1): Fraction(1,6), (2,1): Fraction(1,2), (3,): Fraction(1,3)}
def h3_scaled(k):
    return {tuple(sorted((k*a for a in part), reverse=True)): c for part, c in H3.items()}
def h_pleth_h3(delta):
    total = defaultdict(Fraction)
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            new = defaultdict(Fraction)
            sc = h3_scaled(part)
            for m1, c1 in term.items():
                for m2, c2 in sc.items():
                    new[tuple(sorted(m1+m2, reverse=True))] += c1*c2
            term = new
        zm = zval(mu)
        for m, c in term.items():
            total[m] += c/zm
    return total

def eps(nu, n):
    return (-1)**(n - len(nu))

def census(delta, k):
    """dim of degree-delta SL9-invariants (weight det^k, 3delta = 9k),
    via <h_delta[h_3], s_{(k^9)}> = sum c_nu eps(nu) chi^{(9^k)}(nu)."""
    n = 3*delta
    P = h_pleth_h3(delta)
    lamc = tuple([9]*k)          # conjugate of (k^9)
    val = Fraction(0)
    for nu, c in P.items():
        val += c*eps(nu, n)*chi(lamc, nu)
    assert val.denominator == 1
    return int(val)

for delta, k in [(3, 1), (6, 2), (9, 3), (12, 4)]:
    a = census(delta, k)
    note = " (odd weight: vanishes on the closure regardless)" if k % 2 else ""
    print(f"(A) ambient invariants of cubics in 9 vars, degree {delta} (det^{k}): dim = {a}{note}")

# ---------- (B) symmetric Kronecker ----------
def sq_class(nu):
    out = []
    for p in nu:
        if p % 2 == 0: out += [p//2, p//2]
        else: out.append(p)
    return tuple(sorted(out, reverse=True))

def kron_and_sym(n, mu):
    fact = math.factorial(n)
    parts_n = list(partitions(n))
    res = []
    for lam in parts_n:
        if len(lam) > 9: continue
        g = sum((fact//zval(nu))*chi(lam, nu)*chi(mu, nu)**2 for nu in parts_n)
        assert g % fact == 0
        g //= fact
        tw = sum((fact//zval(nu))*chi(lam, nu)*chi(mu, sq_class(nu)) for nu in parts_n)
        assert tw % fact == 0
        tw //= fact
        sg = (g + tw)
        assert sg % 2 == 0
        sg //= 2
        if g: res.append((lam, g, sg))
    return res

print("\n(B) orbit skeleton of det3: (lam, plain Kronecker g, symmetric sg):")
for d in (1, 2, 3):
    rows = kron_and_sym(3*d, tuple([d]*3))
    nz = [(l, g, s) for (l, g, s) in rows]
    print(f"  delta={d}:")
    for l, g, s in nz:
        print(f"    {l}: g={g}, sg={s}")
anch = [r for r in kron_and_sym(9, (3,3,3)) if r[0] == (1,)*9]
print("  parity anchor sg((1^9),(3^3),(3^3)) =", anch[0][2] if anch else 0, "(must be 0)")

# ---------- (C) boundary-component stabilizers ----------
import sympy as sp
X = sp.symbols('x1:10')
M_tr = sp.Matrix(3, 3, lambda i, j: X[3*i+j]); M_tr[2, 2] = -X[0]-X[4]
P1 = sp.expand(M_tr.det())
P2 = sp.expand(X[3]*X[0]**2 + X[4]*X[1]**2 + X[5]*X[2]**2
               + X[6]*X[0]*X[1] + X[7]*X[1]*X[2] + X[8]*X[0]*X[2])
mons9 = [m for m in itertools.combinations_with_replacement(range(9), 3)]
mon_ix = {m: i for i, m in enumerate(mons9)}
def act_matrix(f):
    rows = []
    for s in range(9):
        for t in range(9):
            d = sp.expand(X[s]*sp.diff(f, X[t]))
            Pd = sp.Poly(d, *X)
            v = np.zeros(len(mons9))
            for mono, cf in Pd.terms():
                if cf == 0 or sum(mono) != 3: continue
                idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
                v[mon_ix[idx]] = float(cf)
            rows.append(v)
    return np.array(rows)
def null_space(M, tol=1e-8):
    U, s, Vh = np.linalg.svd(M.T @ M)
    # eigen-null of Gram
    w, V = np.linalg.eigh(M @ M.T) if False else (None, None)
    U2, s2, Vh2 = np.linalg.svd(M)
    rank = int((s2 > tol*max(M.shape)*s2[0]).sum())
    return Vh2[rank:, :].T
for name, f in [("P1 (traceless det)", P1), ("P2 (universal quadric)", P2)]:
    A = act_matrix(f)
    ns = null_space(A)                      # stabilizer subalgebra inside gl9 (81-dim coords)
    dim = ns.shape[1]
    mats = [ns[:, i].reshape(9, 9) for i in range(dim)]
    G = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            G[i, j] = np.trace(mats[i] @ mats[j])
    rk = np.linalg.matrix_rank(G, tol=1e-6)
    print(f"\n(C) stab({name}): dim = {dim}, trace-form rank = {rk}",
          "(degenerate => nonreductive directions present)" if rk < dim else "(nondegenerate)")
