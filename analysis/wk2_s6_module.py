"""Week 2, session 6 — (1) automated scan of threshold/congruence sum-laws
d2 =? sum_{k <= a l1 + b l2 + g l3 + c, k = r mod m} u(lam; k) on the corner;
(2) the module structure of the gap G = M / C[cusp cone]: new-generator
dimensions g_delta for delta <= 3."""
import itertools, math
from collections import defaultdict
import numpy as np

# ---------------- u-profiles and d2 (from session 5) ----------------
NU = [[0,0,-2],[1,0,0],[0,0,0]]
NU2 = [[0,-1,0],[0,0,0],[2,0,0]]
TAU_V = (1,-2,4); TAU_W = (2,5,-1)
def basis(p, q):
    B = []
    for a0 in range(p+1):
        for a1 in range(p-a0+1):
            a = (a0, a1, p-a0-a1)
            for b0 in range(q+1):
                for b1 in range(q-b0+1):
                    B.append((a, (b0, b1, q-b0-b1)))
    return B
def tau_weight(ab):
    a, b = ab
    return sum(a[i]*TAU_V[i] for i in range(3)) + sum(b[i]*TAU_W[i] for i in range(3))
def null_space(M, tol=1e-8):
    if M.size == 0: return np.eye(M.shape[1])
    U, s, Vh = np.linalg.svd(M, full_matrices=True)
    rank = int((s > tol*max(M.shape)*(s[0] if s.size else 1)).sum()) if s.size else 0
    return Vh[rank:, :].T
def delta_op(p, q):
    Bs = basis(p, q); Bt = basis(p-1, q-1)
    tix = {m: i for i, m in enumerate(Bt)}
    M = np.zeros((len(Bt), len(Bs)))
    for j, (a, b) in enumerate(Bs):
        for i in range(3):
            if a[i] and b[i]:
                na = list(a); na[i] -= 1; nb = list(b); nb[i] -= 1
                M[tix[(tuple(na), tuple(nb))], j] += a[i]*b[i]
    return M, Bs
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
    Bs = basis(p, q)
    D = delta_op(p, q)[0] if (p >= 1 and q >= 1) else np.zeros((0, len(Bs)))
    Nu, B = nu_op(p, q)
    ns = null_space(D)
    prof = {}
    wts = np.array([tau_weight(m) for m in B])
    for k in sorted(set(wts.tolist())):
        sel = (wts == k)
        off = ns[~sel, :]
        cb = null_space(off) if off.shape[0] else np.eye(ns.shape[1])
        if cb.shape[1] == 0: continue
        Kk = ns @ cb
        r = np.linalg.matrix_rank(Nu @ Kk, tol=1e-8)
        u = Kk.shape[1] - r
        if u: prof[k + 3*l3] = int(u)
    return prof

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

corner = sorted({(l1, l2, l3) for l1 in range(1, 7) for l2 in range(l1+1)
                 for l3 in range(l2+1) if (l1+l2+l3) % 3 == 0 and l1+l2+l3 > 0})
data = []
for lam in corner:
    d = sum(lam)//3
    data.append((lam, mH0(lam) - rB(d, lam), u_profile(lam)))

# ---- (1) scan ----
hits = []
for al in (-3, -2, -1, 0, 1, 2, 3):
    for be in (-3, -2, -1, 0, 1, 2, 3):
        for ga in (-3, -2, -1, 0, 1, 2, 3):
            for c in range(-12, 13, 3):
                for m, rr in [(1, 0), (3, 0), (6, 0), (6, 3), (3, 1), (3, 2)]:
                    ok = True
                    for lam, d2, prof in data:
                        B = al*lam[0] + be*lam[1] + ga*lam[2] + c
                        ssum = sum(u for k, u in prof.items() if k <= B and (k - rr) % m == 0)
                        if ssum != d2: ok = False; break
                    if ok: hits.append((al, be, ga, c, m, rr))
print(f"(1) scan over threshold/congruence sum-laws: {len(hits)} exact fits", hits[:8])

# ---------------- (2) module structure of the gap ----------------
import sympy as sp
mons3 = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
A9 = sp.symbols('a1 b1 c1 a2 b2 c2 a3 b3 c3')
x, y, z = sp.symbols('x y z')
l1 = A9[0]*x + A9[1]*y + A9[2]*z
l2 = A9[3]*x + A9[4]*y + A9[5]*z
l3 = A9[6]*x + A9[7]*y + A9[8]*z
F = sp.expand(l1**2*l2 + l3**3)
PF = sp.Poly(F, x, y, z)
E = []
for (i, j, k) in mons3:
    Q = sp.Poly(PF.coeff_monomial(x**i*y**j*z**k), *A9)
    E.append({mo: int(cf) for mo, cf in Q.terms()})

def M_basis(delta):
    out = []
    for u in range(delta+1):
        v = delta - u
        for e1 in itertools.combinations_with_replacement(range(3), 2*u):
            pass
    # enumerate exponent triples directly
    out = []
    for u in range(delta+1):
        v = delta - u
        for x1 in range(2*u+1):
            for y1 in range(2*u-x1+1):
                for x2 in range(u+1):
                    for y2 in range(u-x2+1):
                        for x3 in range(3*v+1):
                            for y3 in range(3*v-x3+1):
                                out.append((x1, y1, 2*u-x1-y1, x2, y2, u-x2-y2, x3, y3, 3*v-x3-y3))
    return out

def dict_mul(P, mono):
    return {tuple(a+b for a, b in zip(m, mono)): c for m, c in P.items()}

print("\n(2) gap module G = M / C[cusp cone]: new-generator dimensions")
prev_dims = None
for delta in (1, 2, 3):
    MB = M_basis(delta)
    idx = {m: i for i, m in enumerate(MB)}
    if delta == 1:
        vecs = []
        for Em in E:
            v = np.zeros(len(MB))
            for mo, c in Em.items(): v[idx[mo]] = c
            vecs.append(v)
        rk = np.linalg.matrix_rank(np.array(vecs), tol=1e-8)
        g = len(MB) - rk
        print(f"  delta=1: dim M = {len(MB)}, dim image = {rk}, g_1 = {g} (expected 18 = dims of (3,0,0)+(2,1,0))")
        prevMB = MB
    else:
        vecs = []
        for Em in E:
            for mu in prevMB:
                P = dict_mul(Em, mu)
                v = np.zeros(len(MB))
                for mo, c in P.items(): v[idx[mo]] = c
                vecs.append(v)
        Mmat = np.array(vecs)
        rk = np.linalg.matrix_rank(Mmat, tol=1e-8)
        g = len(MB) - rk
        print(f"  delta={delta}: dim M = {len(MB)}, dim (W* . M_(delta-1)) = {rk}, g_{delta} = {g}",
              "-> generated in degree 1 so far" if g == 0 else "-> NEW GENERATORS appear")
        prevMB = MB
