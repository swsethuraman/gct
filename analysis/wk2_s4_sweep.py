"""Week 2, session 4 — block-order lemma + systematic sweep + orphan test."""
import sympy as sp
import itertools, math, cmath, random
from itertools import permutations

rho = sp.Symbol('rho')
c13 = sp.Pow(6, sp.Rational(-1, 3)) / rho
ph = sp.Pow(-1, sp.Rational(1, 3))
LH = [
    [c13, c13*rho**3, sp.Integer(0)],
    [ph*c13, -ph*c13*rho**3, sp.Integer(0)],
    [sp.Integer(0), sp.Integer(0), sp.Integer(1)],
]
def wedge(u, v):
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
def det3(u, v, w):
    return sum(u[i]*wedge(v, w)[i] for i in range(3))
def vec_order(vec):
    orders = []
    for comp in vec:
        if comp == 0: continue
        e = sp.expand(sp.radsimp(sp.powsimp(comp*rho**200, force=True)))
        P = sp.Poly(e, rho)
        orders.append(min(m[0] for m in P.monoms()) - 200)
    return min(orders)

print("block-order lemma (rho-orders; T-unit = 6):")
print("  lhat1:", vec_order(LH[0]), " lhat2:", vec_order(LH[1]), " lhat3:", vec_order(LH[2]))
print("  w12:", vec_order(wedge(LH[0], LH[1])), " w13:", vec_order(wedge(LH[0], LH[2])),
      " w23:", vec_order(wedge(LH[1], LH[2])))
DET = det3(LH[0], LH[1], LH[2])
print("  det:", vec_order([DET]))

random.seed(37)
def rand_dual(): return [sp.Integer(random.randint(-3, 3)) for _ in range(3)]
def dot(u, th): return sum(u[i]*th[i] for i in range(3))
def rho_order(expr):
    e = sp.expand(sp.radsimp(sp.powsimp(expr, force=True)))
    e = sp.expand(e*rho**600)
    P = sp.Poly(e, rho)
    if P.is_zero: return None
    return min(m[0] for m in P.monoms()) - 600

PAIRS = [(0,1), (0,2), (1,2)]
def class_pole(aa, qq, r, trials=3):
    best = None
    for _ in range(trials):
        ds = [rand_dual() for _ in range(sum(aa))]
        dw = [rand_dual() for _ in range(sum(qq))]
        tot = 0
        for sg in permutations((0,1,2)):
            sgn = 1
            for i in range(3):
                for j in range(i+1,3):
                    if sg[i] > sg[j]: sgn = -sgn
            term = (sgn**r)*DET**r
            si = 0
            for line in range(3):
                for _ in range(aa[line]):
                    term = term*dot(LH[sg[line]], ds[si]); si += 1
            wi = 0
            for (i, j), q in zip(PAIRS, qq):
                for _ in range(q):
                    term = term*dot(wedge(LH[sg[i]], LH[sg[j]]), dw[wi]); wi += 1
            tot = tot + term
        o = rho_order(tot)
        if o is not None:
            p = sp.Rational(-o, 6)
            if best is None or p > best: best = p
    return best

def max_pole(lam):
    a, b, r = lam[0]-lam[1], lam[1]-lam[2], lam[2]
    best = None
    for aa in itertools.product(range(a+1), repeat=3):
        if sum(aa) != a: continue
        for qq in itertools.product(range(b+1), repeat=3):
            if sum(qq) != b: continue
            n = [aa[i] + sum(q for (u,v), q in zip(PAIRS, qq) if i in (u,v)) + r for i in range(3)]
            if any(x % 3 for x in n): continue
            p = class_pole(aa, qq, r)
            if p is None: continue
            # pole must be an integer for a legitimate single-valued class
            if p != int(p):
                # generic-contraction can see a non-symmetrized shadow; treat as bound only
                p = sp.floor(p)
            if best is None or p > best: best = int(p)
    return best

# deficits for support check (lightweight recompute)
def hist3(dmax):
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4-e1)]
    arr = [[[0]*(3*d+1) for _ in range(3*d+1)] for d in range(dmax+1)]
    arr[0][0][0] = 1
    for (e1, e2) in gens:
        for d in range(1, dmax+1):
            cur, prev = arr[d], arr[d-1]
            lim, plim = 3*d, 3*(d-1)
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
h3 = hist3(16)
P3 = []
for p in itertools.permutations((0,1,2)):
    s_ = 1
    for i in range(3):
        for j in range(i+1,3):
            if p[i] > p[j]: s_ = -s_
    P3.append((p, s_))
def multB(d, lam):
    if d < 0 or lam[2] < 0 or lam[0] < lam[1] or lam[1] < lam[2] or sum(lam) != 3*d: return 0
    l = (lam[0]+2, lam[1]+1, lam[2]); tot = 0
    for p, s_ in P3:
        t = (l[p[0]]-2, l[p[1]]-1, l[p[2]])
        if min(t) < 0 or t[0] > 3*d or t[1] > 3*d: continue
        tot += s_*h3[d][t[0]][t[1]]
    return tot
def closureB(d, lam):
    return multB(d, lam) - multB(d-4, (lam[0]-4, lam[1]-4, lam[2]-4))
W3c = cmath.exp(2j*math.pi/3); H_B = []
def cyc_of(sg):
    seen = [False]*3; out = []
    for i in range(3):
        if not seen[i]:
            ch = []; j = i
            while not seen[j]: seen[j] = True; ch.append(j); j = sg[j]
            out.append(ch)
    return out
for sg in itertools.permutations((0,1,2)):
    cyc = cyc_of(sg)
    for a_ in range(3):
        for b_ in range(3):
            for c_ in range(3):
                scal = (W3c**a_, W3c**b_, W3c**c_); evs = []
                for cy in cyc:
                    pr = 1+0j
                    for i in cy: pr *= scal[i]
                    L = len(cy); rr = cmath.exp(cmath.log(pr)/L)
                    evs += [rr*cmath.exp(2j*math.pi*k/L) for k in range(L)]
                H_B.append(tuple(evs))
def schur3(lam, evs):
    xx, yy, zz = evs
    e1, e2, e3 = xx+yy+zz, xx*yy+xx*zz+yy*zz, xx*yy*zz
    top = lam[0]+2; hs = [0j]*(top+3); hs[0] = 1+0j
    if top >= 1: hs[1] = e1
    if top >= 2: hs[2] = e1*hs[1]-e2
    for j in range(3, top+1): hs[j] = e1*hs[j-1]-e2*hs[j-2]+e3*hs[j-3]
    def hh(k): return hs[k] if k >= 0 else 0j
    return (hh(lam[0])*(hh(lam[1])*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-1))
            - hh(lam[0]+1)*(hh(lam[1]-1)*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-2))
            + hh(lam[0]+2)*(hh(lam[1]-1)*hh(lam[2]-1)-hh(lam[1])*hh(lam[2]-2)))
def orbitB(lam):
    v = sum(schur3(lam, evs) for evs in H_B)/162
    r = round(v.real); assert abs(v-r) < 1e-6
    return r

sweep = []
for l1 in range(0, 10):
    for l2 in range(0, l1+1):
        for l3 in range(0, l2+1):
            if (l1+l2+l3) % 3 == 0 and l1+l2+l3 > 0:
                sweep.append((l1, l2, l3))
specials = [(10,1,1), (13,1,1), (10,2,0), (12,3,0), (11,2,2), (9,6,0), (8,3,1)]
tested = mism = 0
orphan_report = []
for lam in sweep + specials:
    d = sum(lam)//3
    defc = orbitB(lam) - closureB(d, lam)
    fl = max(0, (lam[0]-2*lam[2])//6)
    mp = max_pole(lam)
    if mp is None: mp = -99
    target = fl if defc > 0 else 0
    okk = (mp == target) or (defc == 0 and mp <= 0)
    tested += 1
    if not okk:
        mism += 1
        print("MISMATCH:", lam, "deficit", defc, "formula", fl, "max pole", mp)
    if lam in ((10,1,1), (13,1,1)):
        orphan_report.append((lam, defc, fl, mp))
print(f"\nsweep: {tested} weights tested, mismatches {mism}")
print("orphan weights (lam, deficit, formula, max class pole):")
for e in orphan_report: print("  ", e)
