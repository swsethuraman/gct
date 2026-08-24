"""Week 2, session 5 — level-2 normalization model for the cusp cone.
(A) Identity test: sum_{u+v=delta} mult_lam(Sym^{2u} x Sym^{u} x Sym^{3v})  ==  m_H0(lam)
    (m_H0 = #GT vectors with w1 = 2w2), for all dominant lam |- 3delta, delta <= 7.
(B) Pullback ranks: phi: (l1,l2,l3) -> l1^2 l2 + l3^3; the image of Sym^delta(W*)
    should have dim C(delta+9,9) for delta <= 3 and 714 at delta = 4 (S in the kernel).
"""
import itertools, math
from collections import defaultdict
import numpy as np

# ---------- (A) ----------
def sym_whist(k):
    out = {}
    for a in range(k+1):
        for b in range(k-a+1):
            out[(a, b)] = 1     # exponent of e3 = k-a-b
    return out

def conv(h1, h2, k2):
    out = defaultdict(int)
    for (a1, b1), v1 in h1.items():
        for (a2, b2), v2 in h2.items():
            out[(a1+a2, b1+b2)] += v1*v2
    return out

PERMS3 = []
for p in itertools.permutations((0,1,2)):
    sg = 1
    for i in range(3):
        for j in range(i+1,3):
            if p[i] > p[j]: sg = -sg
    PERMS3.append((p, sg))

def mult_from_hist(hist, total, lam):
    l = (lam[0]+2, lam[1]+1, lam[2])
    tot = 0
    for p, sg in PERMS3:
        t = (l[p[0]]-2, l[p[1]]-1, l[p[2]])
        if min(t) < 0: continue
        w3 = total - t[0] - t[1]
        if w3 != t[2]: continue
        tot += sg*hist.get((t[0], t[1]), 0)
    return tot

def model_mult(lam, delta):
    tot = 0
    n = 3*delta
    for u in range(delta+1):
        v = delta - u
        h = conv(conv(sym_whist(2*u), sym_whist(u), u), sym_whist(3*v), 3*v)
        tot += mult_from_hist(h, n, lam)
    return tot

def mH0(lam):
    l1, l2, l3 = lam
    cnt = 0
    for a in range(l2, l1+1):
        for b in range(l3, l2+1):
            for t in range(b, a+1):
                if t == 2*(a+b-t): cnt += 1
    return cnt

def dominants(n):
    out = []
    for l1 in range(n+1):
        for l2 in range(min(l1, n-l1)+1):
            l3 = n-l1-l2
            if 0 <= l3 <= l2: out.append((l1,l2,l3))
    return out

bad = tot = 0
for delta in range(0, 8):
    for lam in dominants(3*delta):
        tot += 1
        mm = model_mult(lam, delta); mh = mH0(lam)
        if mm != mh:
            bad += 1
            if bad <= 10: print("MODEL MISMATCH", delta, lam, "model", mm, "PW", mh)
print(f"(A) normalization-model identity: {tot} weights tested (delta <= 7), mismatches {bad}")

# ---------- (B) ----------
mons3 = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]

def phi_pullbacks():
    # 9 vars: (a1,b1,c1,a2,b2,c2,a3,b3,c3); return dict per W*-monomial:
    # E_m = coeff of x^i y^j z^k in l1^2 l2 + l3^3
    import sympy as sp
    A = sp.symbols('a1 b1 c1 a2 b2 c2 a3 b3 c3')
    x, y, z = sp.symbols('x y z')
    l1 = A[0]*x + A[1]*y + A[2]*z
    l2 = A[3]*x + A[4]*y + A[5]*z
    l3 = A[6]*x + A[7]*y + A[8]*z
    F = sp.expand(l1**2*l2 + l3**3)
    P = sp.Poly(F, x, y, z)
    out = []
    for (i, j, k) in mons3:
        c = P.coeff_monomial(x**i*y**j*z**k)
        Q = sp.Poly(c, *A)
        d = {}
        for mono, cf in Q.terms():
            d[mono] = int(cf)
        out.append(d)
    return out

E = phi_pullbacks()

def dict_mul(P, Q):
    R = defaultdict(int)
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = tuple(a+b for a, b in zip(m1, m2))
            R[m] += c1*c2
    return R

print("\n(B) pullback ranks:")
for delta in range(1, 5):
    rows = []
    index = {}
    for combo in itertools.combinations_with_replacement(range(10), delta):
        P = {(0,)*9: 1}
        for m in combo: P = dict_mul(P, E[m])
        rows.append(P)
        for mo in P:
            if mo not in index: index[mo] = len(index)
    ncol = len(index)
    M = np.zeros((len(rows), min(ncol, 4000)))
    if ncol <= 4000:
        for r, P in enumerate(rows):
            for mo, c in P.items(): M[r, index[mo]] = c
    else:
        rng = np.random.default_rng(5)
        proj = rng.choice([-1.0, 0.0, 0.0, 1.0], size=(ncol, 4000))
        big = np.zeros((len(rows), ncol))
        for r, P in enumerate(rows):
            for mo, c in P.items(): big[r, index[mo]] = c
        M = big @ proj
    rk = np.linalg.matrix_rank(M, tol=1e-7)
    full = math.comb(delta+9, 9)
    expect = full if delta <= 3 else full - 1
    print(f"  delta={delta}: rank {rk}, expected {expect} "
          f"({'full' if delta<=3 else 'full minus the Aronhold S in the kernel'})",
          "MATCH" if rk == expect else "MISMATCH")
