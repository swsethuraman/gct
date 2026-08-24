"""Week 2, session 5 — unipotent eigencounts at the conic+tangent stabilizer,
the W2-normal weight inside the cusp cone, and the first comparison with d2.
"""
import itertools, math, cmath
from fractions import Fraction
from collections import defaultdict
import numpy as np

# ---------- rebuild S and T (pure python, as before) ----------
mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
midx = {m: i for i, m in enumerate(mons)}
from itertools import combinations_with_replacement as cwr
def apply_V(mono, kind):
    out = {}
    for pos in range(len(mono)):
        I, J, K = mons[mono[pos]]
        if kind == 1:
            if I >= 1 and J+1 <= 3: src = (I-1, J+1, K); w = J+1
            else: continue
        else:
            if J >= 1 and K+1 <= 3: src = (I, J-1, K+1); w = K+1
            else: continue
        if sum(src) != 3: continue
        new = list(mono); new[pos] = midx[src]; new.sort()
        t = tuple(new)
        out[t] = out.get(t, 0) + w
    return out
def build_invariant(degree, weight):
    cand = []
    for combo in cwr(range(10), degree):
        w = [0,0,0]
        for idx in combo:
            for t in range(3): w[t] += mons[idx][t]
        if tuple(w) == weight: cand.append(combo)
    eq = {}; trip = []
    for kind in (1,2):
        for ci, combo in enumerate(cand):
            for tgt, w in apply_V(combo, kind).items():
                key = (kind, tgt)
                if key not in eq: eq[key] = len(eq)
                trip.append((eq[key], ci, w))
    nr, nc = len(eq), len(cand)
    M = [[Fraction(0)]*nc for _ in range(nr)]
    for r, c, w in trip: M[r][c] += w
    rank = 0; piv = []
    for col in range(nc):
        pr_ = None
        for r in range(rank, nr):
            if M[r][col] != 0: pr_ = r; break
        if pr_ is None: continue
        M[rank], M[pr_] = M[pr_], M[rank]
        row = M[rank]; pc = row[col]
        M[rank] = [a/pc for a in row]; row = M[rank]
        for r in range(nr):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a-f*b for a, b in zip(M[r], row)]
        piv.append(col); rank += 1
    free = [c for c in range(nc) if c not in piv]
    assert len(free) == 1
    sol = [Fraction(0)]*nc; sol[free[0]] = Fraction(1)
    for r, col in enumerate(piv): sol[col] = -M[r][free[0]]
    from math import gcd
    den = 1
    for v in sol: den = den*v.denominator//gcd(den, v.denominator)
    ints = [int(v*den) for v in sol]
    g = 0
    for v in ints: g = gcd(g, abs(v))
    return cand, [v//g for v in ints]
candS, Sco = build_invariant(4, (4,4,4))
candT, Tco = build_invariant(6, (6,6,6))

# ---------- W2-normal weight inside the cusp cone ----------
w1 = {(2,1,0): 1, (0,2,1): 1}   # x^2 y + y^2 z
def grad(cand, co, assign):
    g = {}
    for m in mons:
        tot = 0
        for combo, cf in zip(cand, co):
            if cf == 0: continue
            cnt = combo.count(midx[m])
            if cnt == 0: continue
            p = cf*cnt
            rest = list(combo); rest.remove(midx[m])
            for idx in rest:
                v = assign.get(mons[idx], 0)
                if v == 0: p = 0; break
                p *= v
            tot += p
        g[m] = tot
    return g
gS = grad(candS, Sco, w1); gT = grad(candT, Tco, w1)
print("grad S at w1 nonzero:", {m: v for m, v in gS.items() if v})
print("grad T at w1 nonzero:", {m: v for m, v in gT.items() if v})
# tangent of G.w1 (from session 5: dim 7); ker(dS) cap ker(dT); tau-weights
import sympy as sp
xs, ys, zs = sp.symbols('x y z')
f1 = xs**2*ys + ys**2*zs
V3 = [xs, ys, zs]
vecs = []
for s_ in range(3):
    for t_ in range(3):
        d = sp.expand(V3[s_]*sp.diff(f1, V3[t_]))
        Pd = sp.Poly(d, xs, ys, zs)
        vecs.append([Pd.coeff_monomial(xs**m[0]*ys**m[1]*zs**m[2]) for m in mons])
A = sp.Matrix([[sp.Rational(v) for v in row] for row in vecs])
orb = A.T  # columns = orbit tangent vectors... use rowspace properly
orbM = sp.Matrix.hstack(*[sp.Matrix(row) for row in vecs])
print("dim g.w1 =", orbM.rank())
gSv = sp.Matrix([[sp.Rational(gS[m]) for m in mons]])
gTv = sp.Matrix([[sp.Rational(gT[m]) for m in mons]])
Kmat = sp.Matrix.vstack(gSv, gTv)
ker = Kmat.nullspace()
K = sp.Matrix.hstack(*ker)
print("dim ker(dS) cap ker(dT) =", K.shape[1])
tau = (1, -2, 4)
def wt_of(idx):
    i, j, k = mons[idx]
    return i*tau[0] + j*tau[1] + k*tau[2]
def weight_dims(B):
    cols = [B.col(i) for i in range(B.shape[1])]
    out = {}
    for w in sorted(set(wt_of(i) for i in range(10))):
        idxs = [i for i in range(10) if wt_of(i) == w]
        if cols:
            proj = sp.Matrix.hstack(*[sp.Matrix([c[i] for i in idxs]) for c in cols])
            out[w] = proj.rank()
        else: out[w] = 0
    return out
kw = weight_dims(K); ow = weight_dims(orbM)
print("tau-weight dims of ker:", {k: v for k, v in kw.items() if v})
print("tau-weight dims of g.w1:", {k: v for k, v in ow.items() if v})
print("NORMAL weight(s) of W2 in the cusp cone:", {k: kw.get(k,0)-ow.get(k,0) for k in kw if kw.get(k,0)-ow.get(k,0)})

# ---------- unipotent eigencount model u(lam; k) ----------
NU = [[0,0,-2],[1,0,0],[0,0,0]]
NU2 = [[-a for a in row] for row in np.array(NU).T.tolist()]  # tr(NU) I - NU^T = -NU^T
TAU_V = (1, -2, 4)
TAU_W = (2, 5, -1)

def basis(p, q):
    B = []
    for al in itertools.product(range(p+1), repeat=2):
        if sum(al) > p: continue
        a = (al[0], al[1], p-al[0]-al[1])
        for be in itertools.product(range(q+1), repeat=2):
            if sum(be) > q: continue
            b = (be[0], be[1], q-be[0]-be[1])
            B.append((a, b))
    return B

def tau_weight(ab):
    a, b = ab
    return sum(a[i]*TAU_V[i] for i in range(3)) + sum(b[i]*TAU_W[i] for i in range(3))

def delta_op(p, q):
    Bsrc = basis(p, q); Btgt = basis(p-1, q-1)
    tix = {m: i for i, m in enumerate(Btgt)}
    M = np.zeros((len(Btgt), len(Bsrc)))
    for j, (a, b) in enumerate(Bsrc):
        for i in range(3):
            if a[i] and b[i]:
                na = list(a); na[i] -= 1
                nb = list(b); nb[i] -= 1
                M[tix[(tuple(na), tuple(nb))], j] += a[i]*b[i]
    return M, Bsrc, Btgt

def nu_op(p, q):
    B = basis(p, q); bix = {m: i for i, m in enumerate(B)}
    M = np.zeros((len(B), len(B)))
    for j, (a, b) in enumerate(B):
        for col in range(3):
            if a[col]:
                for row in range(3):
                    c = NU[row][col]
                    if c:
                        na = list(a); na[col] -= 1; na[row] += 1
                        M[bix[(tuple(na), b)], j] += a[col]*c
            if b[col]:
                for row in range(3):
                    c = NU2[row][col]
                    if c:
                        nb = list(b); nb[col] -= 1; nb[row] += 1
                        M[bix[(a, tuple(nb))], j] += b[col]*c
    return M, B

def u_profile(lam):
    p, q, l3 = lam[0]-lam[1], lam[1]-lam[2], lam[2]
    D, Bsrc, _ = delta_op(p, q) if p >= 1 and q >= 1 else (np.zeros((0, len(basis(p,q)))), basis(p,q), None)
    Nu, B = nu_op(p, q)
    assert B == Bsrc or D.shape[0] == 0
    # kernel of Delta = the irrep S_(p+q, q, 0)
    if D.shape[0]:
        ns = null_space(D)
    else:
        ns = np.eye(len(B))
    dimW = round(ns.shape[1])
    wdim = (lam[0]-lam[1]+1)*(lam[1]-lam[2]+1)*(lam[0]-lam[2]+2)//2
    assert dimW == wdim, (lam, dimW, wdim)
    prof = {}
    wts = np.array([tau_weight(m) for m in B])
    for k in sorted(set(wts.tolist())):
        sel = (wts == k)
        # restrict kernel to weight-k: vectors in span(ns) supported on sel:
        # solve ns @ c with rows off-sel = 0
        off = ns[~sel, :]
        cbasis = null_space(off) if off.shape[0] else np.eye(ns.shape[1])
        if cbasis.shape[1] == 0: continue
        Kk = ns @ cbasis               # weight-k kernel vectors
        # nu-killed within:
        img = Nu @ Kk
        r = np.linalg.matrix_rank(img, tol=1e-8)
        u = Kk.shape[1] - r
        if u: prof[k + 3*l3] = u
    return prof

def null_space(M, tol=1e-8):
    if M.size == 0:
        return np.eye(M.shape[1])
    U, s, Vh = np.linalg.svd(M)
    rank = int((s > tol*max(M.shape)*s[0]).sum()) if s.size else 0
    return Vh[rank:, :].T

# ---------- d2 corner and comparison ----------
def hist3(dmax):
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4-e1)]
    arr = [[[0]*(3*d+1) for _ in range(3*d+1)] for d in range(dmax+1)]
    arr[0][0][0] = 1
    for (e1, e2) in gens:
        for d in range(1, dmax+1):
            cur, prev = arr[d], arr[d-1]
            lim, plim = 3*d, 3*(d-1)
            for A_ in range(e1, lim+1):
                pA = A_-e1
                if pA > plim: continue
                prow, crow = prev[pA], cur[A_]
                for B_ in range(e2, lim+1):
                    pB = B_-e2
                    if pB > plim: continue
                    v = prow[pB]
                    if v: crow[B_] += v
    return arr
h3 = hist3(8)
P3 = []
for pp in itertools.permutations((0,1,2)):
    s_ = 1
    for i in range(3):
        for j in range(i+1,3):
            if pp[i] > pp[j]: s_ = -s_
    P3.append((pp, s_))
def multB(d, lam):
    if d < 0 or lam[2] < 0 or lam[0] < lam[1] or lam[1] < lam[2] or sum(lam) != 3*d: return 0
    l = (lam[0]+2, lam[1]+1, lam[2]); tot = 0
    for pp, s_ in P3:
        t = (l[pp[0]]-2, l[pp[1]]-1, l[pp[2]])
        if min(t) < 0 or t[0] > 3*d or t[1] > 3*d: continue
        tot += s_*h3[d][t[0]][t[1]]
    return tot
def closureB(d, lam):
    return multB(d, lam) - multB(d-4, (lam[0]-4, lam[1]-4, lam[2]-4))
def rB(d, lam):
    return closureB(d, lam) - closureB(d-6, (lam[0]-6, lam[1]-6, lam[2]-6))
def mH0(lam):
    l1, l2, l3 = lam
    return sum(1 for a in range(l2, l1+1) for b in range(l3, l2+1)
               for t in range(b, a+1) if t == 2*(a+b-t))

print("\ncorner comparison: lam, d2 = m - r, u-profile {tau-weight: dim of nu-killed}")
corner = [lam for d in range(1, 7) for lam in
          [(l1, l2, 3*d-l1-l2) for l1 in range(3*d+1) for l2 in range(min(l1, 3*d-l1)+1)]
          if lam[2] >= 0 and lam[1] >= lam[2] and lam[0] <= 6]
seen = set()
for lam in corner:
    if lam in seen: continue
    seen.add(lam)
    d = sum(lam)//3
    d2 = mH0(lam) - rB(d, lam)
    prof = u_profile(lam)
    print(f"  {lam} d2={d2}  u-profile={prof}")
