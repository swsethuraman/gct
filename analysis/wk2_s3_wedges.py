"""Week 2, session 3 — general-lambda pole calculus in World B.
FFT class model on the transversal family f_s = x^2 y + s y^3 + z^3:
  lhat1 = c^{1/3}(1, rho^3, 0),  lhat2 = phase c^{1/3}(1, -rho^3, 0),  lhat3 = (0,0,1),
  c = 1/(6 sigma), sigma = rho^3, s = sigma^2/3.
Classes for weight lam: a = lam1-lam2 singles, b = lam2-lam3 wedges, r = lam3 dets,
line-exponents n_i = a_i + sum_j q_ij + r = 0 mod 3.  Pole in T-units = -ord_rho/6.
Compare max class pole with the recomputed conductor and floor((lam1-2lam3)/6).
"""
import sympy as sp
import itertools, math, cmath, random
from itertools import permutations

rho = sp.Symbol('rho')
c13 = sp.Pow(6, sp.Rational(-1, 3)) / rho
ph = sp.Pow(-1, sp.Rational(1, 3))
LH = [
    [c13 * 1, c13 * rho**3, sp.Integer(0)],
    [ph*c13 * 1, -ph*c13 * rho**3, sp.Integer(0)],
    [sp.Integer(0), sp.Integer(0), sp.Integer(1)],
]

def wedge(u, v):
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]

def det3(u, v, w):
    return sum(u[i]*wedge(v, w)[i] for i in range(3))

DET = det3(LH[0], LH[1], LH[2])

random.seed(23)
def rand_dual():
    return [sp.Integer(random.randint(-3, 3)) for _ in range(3)]

def dot(u, th):
    return sum(u[i]*th[i] for i in range(3))

def rho_order(expr):
    e = sp.expand(sp.radsimp(sp.powsimp(expr, force=True)))
    e = sp.expand(e * rho**600)
    P = sp.Poly(e, rho)
    if P.is_zero: return None
    return min(m[0] for m in P.monoms()) - 600

def class_pole(aa, qq, r, trials=3):
    """aa = (a1,a2,a3) single counts; qq = (q12,q13,q23) wedge counts; r = det power."""
    best = None
    pairs = [(0,1), (0,2), (1,2)]
    for _ in range(trials):
        duals_s = [rand_dual() for _ in range(sum(aa))]
        duals_w = [rand_dual() for _ in range(sum(qq))]
        tot = 0
        for sigma in permutations((0, 1, 2)):
            sgn = 1
            for i in range(3):
                for j in range(i+1, 3):
                    if sigma[i] > sigma[j]: sgn = -sgn
            term = (sgn**r) * DET**r
            si = 0
            for line in range(3):
                for _ in range(aa[line]):
                    term = term * dot(LH[sigma[line]], duals_s[si]); si += 1
            wi = 0
            for (i, j), q in zip(pairs, qq):
                for _ in range(q):
                    term = term * dot(wedge(LH[sigma[i]], LH[sigma[j]]), duals_w[wi]); wi += 1
            tot = tot + term
        o = rho_order(tot)
        if o is not None:
            p = sp.Rational(-o, 6)
            if best is None or p > best: best = p
    return best

def max_pole(lam):
    a, b, r = lam[0]-lam[1], lam[1]-lam[2], lam[2]
    pairs = [(0,1), (0,2), (1,2)]
    best = None; details = []
    for aa in itertools.product(range(a+1), repeat=3):
        if sum(aa) != a: continue
        for qq in itertools.product(range(b+1), repeat=3):
            if sum(qq) != b: continue
            n = [aa[i] + sum(q for (u, v), q in zip(pairs, qq) if i in (u, v)) + r for i in range(3)]
            if any(x % 3 for x in n): continue
            p = class_pole(aa, qq, r)
            if p is None: continue
            assert p == int(p), (lam, aa, qq, r, p)
            details.append(((aa, qq, r), int(p)))
            if best is None or int(p) > best: best = int(p)
    return best, details

# ---- recompute actual conductors for the test weights ----
def hist3(dmax):
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4-e1)]
    arr = [[[0]*(3*deg+1) for _ in range(3*deg+1)] for deg in range(dmax+1)]
    arr[0][0][0] = 1
    for (e1, e2) in gens:
        for deg in range(1, dmax+1):
            cur, prev = arr[deg], arr[deg-1]
            lim, plim = 3*deg, 3*(deg-1)
            for w1 in range(e1, lim+1):
                p1 = w1-e1
                if p1 > plim: continue
                prow, crow = prev[p1], cur[w1]
                for w2 in range(e2, lim+1):
                    p2 = w2-e2
                    if p2 > plim: continue
                    v = prow[p2]
                    if v: crow[w2] += v
    return arr
h3 = hist3(46)
PERMS3 = []
for p in itertools.permutations((0,1,2)):
    sg = 1
    for i in range(3):
        for j in range(i+1,3):
            if p[i] > p[j]: sg = -sg
    PERMS3.append((p, sg))
def multB(deg, lam):
    if deg < 0 or lam[2] < 0 or lam[0] < lam[1] or lam[1] < lam[2]: return 0
    if sum(lam) != 3*deg: return 0
    l = (lam[0]+2, lam[1]+1, lam[2])
    tot = 0
    for p, sg in PERMS3:
        t_ = (l[p[0]]-2, l[p[1]]-1, l[p[2]])
        if min(t_) < 0 or t_[0] > 3*deg or t_[1] > 3*deg: continue
        tot += sg*h3[deg][t_[0]][t_[1]]
    return tot
def closureB(deg, lam):
    return multB(deg, lam) - multB(deg-4, (lam[0]-4, lam[1]-4, lam[2]-4))
W3c = cmath.exp(2j*math.pi/3)
H_B = []
def cycles_of(sg_):
    seen = [False]*3; cyc = []
    for i in range(3):
        if not seen[i]:
            ch = []; j = i
            while not seen[j]:
                seen[j] = True; ch.append(j); j = sg_[j]
            cyc.append(ch)
    return cyc
for sg_ in itertools.permutations((0,1,2)):
    cyc = cycles_of(sg_)
    for a_ in range(3):
        for b_ in range(3):
            for c_ in range(3):
                scal = (W3c**a_, W3c**b_, W3c**c_)
                evs = []
                for cy in cyc:
                    pr = 1+0j
                    for i in cy: pr *= scal[i]
                    L = len(cy); rr = cmath.exp(cmath.log(pr)/L)
                    evs += [rr*cmath.exp(2j*math.pi*k/L) for k in range(L)]
                H_B.append(tuple(evs))
def schur3(lam, evs):
    xx, yy, zz = evs
    e1, e2, e3 = xx+yy+zz, xx*yy+xx*zz+yy*zz, xx*yy*zz
    top = lam[0]+2
    hs = [0j]*(top+3); hs[0] = 1+0j
    if top >= 1: hs[1] = e1
    if top >= 2: hs[2] = e1*hs[1]-e2
    for j in range(3, top+1):
        hs[j] = e1*hs[j-1]-e2*hs[j-2]+e3*hs[j-3]
    def hh(k): return hs[k] if k >= 0 else 0j
    return (hh(lam[0])*(hh(lam[1])*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-1))
            - hh(lam[0]+1)*(hh(lam[1]-1)*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-2))
            + hh(lam[0]+2)*(hh(lam[1]-1)*hh(lam[2]-1)-hh(lam[1])*hh(lam[2]-2)))
def orbitB(lam):
    v = sum(schur3(lam, evs) for evs in H_B)/162
    r = round(v.real); assert abs(v-r) < 1e-6
    return r
def conductor(lam, delta):
    od = orbitB(lam)
    prof = [closureB(delta+6*m, tuple(x+6*m for x in lam)) for m in range(7)]
    if prof[0] == od: return 0
    return next(m for m in range(7) if prof[m] == od)

tests = [((8,3,1), 4), ((10,2,0), 4), ((11,2,2), 5), ((12,3,0), 5), ((9,6,0), 5)]
print("weight        delta  cond(table)  floor((l1-2l3)/6)  max class pole   verdict")
for lam, d in tests:
    ct = conductor(lam, d)
    fl = max(0, (lam[0]-2*lam[2])//6)
    mp, det = max_pole(lam)
    verdict = "MATCH" if mp == ct == fl else "MISMATCH"
    print(f"{str(lam):<13} {d:>3}   {ct:>6}        {fl:>6}            {mp:>6}        {verdict}")
    if verdict == "MISMATCH":
        print("   class detail:", det)
