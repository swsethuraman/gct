"""Week 1 — refined conductors along minimal boundary equations, and the
floor(delta^2/4) theorem verified to delta = 100.
World A ray: multiply by I (degree 2, weight det^4): (delta, a, b) -> (delta+2, a+4, b+4).
World B ray: multiply by the canonical degree-6 det^6 semiinvariant T on sigma_3:
             (delta, lam) -> (delta+6, lam+(6,6,6)).
"""
import math, cmath, itertools
from collections import Counter

# ---------------- World A machinery ----------------
def hist2(dmax, d=4):
    W = d*dmax
    arr = [[0]*(W+1) for _ in range(dmax+1)]
    arr[0][0] = 1
    for e in range(d+1):
        for deg in range(1, dmax+1):
            row, prow = arr[deg], arr[deg-1]
            for w in range(e, d*deg+1):
                v = prow[w-e]
                if v: row[w] += v
    return arr

DMAX_A = 100
h2 = hist2(DMAX_A)

def multA(deg, a, b):
    if deg < 0 or b < 0 or a < b or a+b != 4*deg: return 0
    return h2[deg][b] - (h2[deg][b-1] if b-1 >= 0 else 0)

def closureA(deg, a, b):
    return multA(deg, a, b) - multA(deg-3, a-6, b-6)

I_ = 1j
H_A = [(I_**p, I_**q) for p in range(4) for q in range(4)]
for p in range(4):
    for q in range(4):
        z = cmath.exp(1j*math.pi*(p+q)/4.0)
        H_A.append((z, -z))

def schur2(a, b, xx, yy):
    m = a - b
    if abs(xx - yy) > 1e-9:
        v = (xx**(m+1) - yy**(m+1)) / (xx - yy)
    else:
        v = (m+1) * xx**m
    return (xx*yy)**b * v

def orbitA(a, b):
    s = sum(schur2(a, b, xx, yy) for (xx, yy) in H_A) / 32
    r = round(s.real)
    assert abs(s - r) < 1e-6, (a, b, s)
    return r

# ---- floor(delta^2/4) to delta = 100 ----
ok = True
for d in range(0, 101):
    tot_orb = sum(orbitA(4*d-b, b) for b in range(0, 2*d+1))
    tot_clo = h2[d][2*d] - (h2[d-3][2*d-6] if d >= 3 else 0)
    if tot_orb - tot_clo != (d*d)//4:
        ok = False; print("FAIL at", d, tot_orb - tot_clo, (d*d)//4)
print("total deficit == floor(delta^2/4) for ALL delta <= 100:", ok)

# ---- refined I-conductors, delta <= 20 ----
MMI = 12
rows = []
condI_hist = Counter()
maxcond_by_delta = {}
for d in range(0, 21):
    mc = 0
    for b in range(0, 2*d+1):
        a = 4*d - b
        cm = closureA(d, a, b); od = orbitA(a, b)
        assert 0 <= cm <= od
        if od > cm:
            prof = [closureA(d+2*m, a+4*m, b+4*m) for m in range(MMI+1)]
            for i in range(MMI):
                assert prof[i] <= prof[i+1], (d, (a, b), prof)
            cI = next((m for m in range(MMI+1) if prof[m] == od), None)
            assert cI is not None, (d, (a, b), prof, od)
            # consistency with Delta-conductor: c_Delta = ceil(c_I / 3)
            profD = [closureA(d+6*m, a+12*m, b+12*m) for m in range(5)]
            cD = next((m for m in range(5) if profD[m] == od), None)
            assert cD == -(-cI // 3), (d, (a, b), cI, cD)
            # test the pole-law bound: c_I <= floor((a-b)/8)
            bound = (a - b) // 8
            rows.append((d, (a, b), cm, od, od-cm, cI, bound))
            condI_hist[cI] += 1
            mc = max(mc, cI)
    maxcond_by_delta[d] = mc
print("\nWorld A refined conductor histogram (I-units), delta <= 20:", dict(sorted(condI_hist.items())))
print("max I-conductor by delta:", {d: m for d, m in maxcond_by_delta.items() if m})
viol = [r for r in rows if r[5] > r[6]]
print("violations of c_I <= floor((a-b)/8):", len(viol))
tight = sum(1 for r in rows if r[5] == r[6])
print(f"tightness: c_I == floor((a-b)/8) on {tight}/{len(rows)} deficit weights")
print("sample delta=8..10 rows (delta, (a,b), closure, orbit, deficit, c_I, floor((a-b)/8)):")
for r in rows:
    if 8 <= r[0] <= 10 and r[1][1] <= 2:
        print("  ", r)

# ---------------- World B machinery ----------------
def hist3(dmax):
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4-e1)]
    arr = [[[0]*(3*deg+1) for _ in range(3*deg+1)] for deg in range(dmax+1)]
    arr[0][0][0] = 1
    for (e1, e2) in gens:
        for deg in range(1, dmax+1):
            cur, prev = arr[deg], arr[deg-1]
            lim, plim = 3*deg, 3*(deg-1)
            for w1 in range(e1, lim+1):
                p1 = w1 - e1
                if p1 > plim: continue
                prow = prev[p1]; crow = cur[w1]
                for w2 in range(e2, lim+1):
                    p2 = w2 - e2
                    if p2 > plim: continue
                    v = prow[p2]
                    if v: crow[w2] += v
    return arr

DMAX_B = 46
h3 = hist3(DMAX_B)
PERMS3 = []
for p in itertools.permutations((0, 1, 2)):
    sg = 1
    for i in range(3):
        for j in range(i+1, 3):
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
        tot += sg * h3[deg][t_[0]][t_[1]]
    return tot

def closureB(deg, lam):
    return multB(deg, lam) - multB(deg-4, (lam[0]-4, lam[1]-4, lam[2]-4))

assert closureB(6, (6, 6, 6)) == 1   # the canonical T-semiinvariant on sigma_3

W3 = cmath.exp(2j*math.pi/3)
H_B = []
def cycles_of(sigma):
    seen = [False]*3; cyc = []
    for i in range(3):
        if not seen[i]:
            cchain = []; j = i
            while not seen[j]:
                seen[j] = True; cchain.append(j); j = sigma[j]
            cyc.append(cchain)
    return cyc
for sigma in itertools.permutations((0, 1, 2)):
    cyc = cycles_of(sigma)
    for a_ in range(3):
        for b_ in range(3):
            for c_ in range(3):
                scal = (W3**a_, W3**b_, W3**c_)
                evs = []
                for cy in cyc:
                    prod = 1+0j
                    for i in cy: prod *= scal[i]
                    L = len(cy)
                    r = cmath.exp(cmath.log(prod)/L)
                    evs += [r*cmath.exp(2j*math.pi*k/L) for k in range(L)]
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
    r1 = (hh(lam[0]), hh(lam[0]+1), hh(lam[0]+2))
    r2 = (hh(lam[1]-1), hh(lam[1]), hh(lam[1]+1))
    r3 = (hh(lam[2]-2), hh(lam[2]-1), hh(lam[2]))
    return (r1[0]*(r2[1]*r3[2]-r2[2]*r3[1]) - r1[1]*(r2[0]*r3[2]-r2[2]*r3[0])
            + r1[2]*(r2[0]*r3[1]-r2[1]*r3[0]))

def orbitB(lam):
    s = sum(schur3(lam, evs) for evs in H_B) / 162
    r = round(s.real)
    assert abs(s - r) < 1e-6, (lam, s)
    return r

def dominants(n):
    out = []
    for l1 in range(0, n+1):
        for l2 in range(0, min(l1, n-l1)+1):
            l3 = n-l1-l2
            if 0 <= l3 <= l2: out.append((l1, l2, l3))
    return out

MMT = 6
condT_hist = Counter(); nrows = 0; unreached = 0
maxT_by_delta = {}
for d in range(0, 11):
    mc = 0
    for lam in dominants(3*d):
        if d + 6*MMT > DMAX_B: break
        cm = closureB(d, lam); od = orbitB(lam)
        assert 0 <= cm <= od, (d, lam, cm, od)
        if od > cm:
            nrows += 1
            prof = [closureB(d+6*m, tuple(v+6*m for v in lam)) for m in range(MMT+1)]
            for i in range(MMT):
                assert prof[i] <= prof[i+1], (d, lam, prof)
            cT = next((m for m in range(MMT+1) if prof[m] == od), None)
            if cT is None:
                unreached += 1
            else:
                condT_hist[cT] += 1
                mc = max(mc, cT)
    maxT_by_delta[d] = mc
print("\nWorld B refined conductor histogram (T-units), delta <= 10:", dict(sorted(condT_hist.items())))
print("B deficit weights:", nrows, "; profiles not stabilized by m=6:", unreached)
print("max T-conductor by delta:", {d: m for d, m in maxT_by_delta.items() if m})
print("(every stabilized profile reaching the orbit value doubles as evidence that {T != 0} on sigma_3 is exactly the Fermat orbit)")
