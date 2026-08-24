"""Week 1, session 3 — (1) World A grand identity to delta=60;
(2) World B full deficit/conductor map and the formula test."""
import math, cmath, itertools
from collections import Counter

# ---------- World A ----------
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
h2 = hist2(60)
def multA(deg, a, b):
    if deg < 0 or b < 0 or a < b or a+b != 4*deg: return 0
    return h2[deg][b] - (h2[deg][b-1] if b-1 >= 0 else 0)
def closureA(deg, a, b):
    return multA(deg, a, b) - multA(deg-3, a-6, b-6)
def orbit_model(a, b):
    n = a - b
    if n < 0: return 0
    cnt = 0
    for p in range(n, (n-1)//2, -1):
        q = n - p
        if (p+b) % 4 == 0 and (q+b) % 4 == 0:
            if p == q and b % 2 == 1: continue
            cnt += 1
    return cnt
ok = True
for d in range(0, 61):
    for b in range(0, 2*d+1):
        a = 4*d - b
        deficit = orbit_model(a, b) - closureA(d, a, b)
        P = max(0, (a - 3*b)//8)
        if deficit != P:
            ok = False; print("GRAND IDENTITY FAIL:", d, (a,b), deficit, P)
print("WORLD A GRAND IDENTITY  [deficit == max(0, floor((a-3b)/8)) for all weights, delta <= 60]:", ok)
print("  corollaries: closure mult = N(lambda) - floor((a-3b)/8)+ ; conductor = deficit; support b <= delta-2;")
print("  max conductor floor(delta/2); total deficit = sum floor((delta-b)/2) = floor(delta^2/4).")

# ---------- World B ----------
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
        tot += sg * h3[deg][t_[0]][t_[1]]
    return tot
def closureB(deg, lam):
    return multB(deg, lam) - multB(deg-4, (lam[0]-4, lam[1]-4, lam[2]-4))
W3 = cmath.exp(2j*math.pi/3)
H_B = []
def cycles_of(sigma):
    seen = [False]*3; cyc = []
    for i in range(3):
        if not seen[i]:
            ch = []; j = i
            while not seen[j]:
                seen[j] = True; ch.append(j); j = sigma[j]
            cyc.append(ch)
    return cyc
for sigma in itertools.permutations((0,1,2)):
    cyc = cycles_of(sigma)
    for a_ in range(3):
        for b_ in range(3):
            for c_ in range(3):
                scal = (W3**a_, W3**b_, W3**c_)
                evs = []
                for cy in cyc:
                    pr = 1+0j
                    for i in cy: pr *= scal[i]
                    L = len(cy); r = cmath.exp(cmath.log(pr)/L)
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
    return (hh(lam[0])*(hh(lam[1])*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-1))
            - hh(lam[0]+1)*(hh(lam[1]-1)*hh(lam[2])-hh(lam[1]+1)*hh(lam[2]-2))
            + hh(lam[0]+2)*(hh(lam[1]-1)*hh(lam[2]-1)-hh(lam[1])*hh(lam[2]-2)))
def orbitB(lam):
    s = sum(schur3(lam, evs) for evs in H_B)/162
    r = round(s.real); assert abs(s-r) < 1e-6, (lam, s)
    return r
def dominants(n):
    out = []
    for l1 in range(0, n+1):
        for l2 in range(0, min(l1, n-l1)+1):
            l3 = n-l1-l2
            if 0 <= l3 <= l2: out.append((l1,l2,l3))
    return out

# full map
MMT = 6
data = []   # (delta, lam, deficit, cond)
for d in range(0, 11):
    for lam in dominants(3*d):
        cm = closureB(d, lam); od = orbitB(lam)
        defc = od - cm
        assert defc >= 0
        if defc > 0:
            prof = [closureB(d+6*m, tuple(v+6*m for v in lam)) for m in range(MMT+1)]
            cT = next(m for m in range(MMT+1) if prof[m] == od)
        else:
            cT = 0
        data.append((d, lam, defc, cT))

# candidate: floor((l1 - 2 l3)/6)+  (intrinsic transport with w_N = 6)
fails_d = sum(1 for (d,l,df,ct) in data if max(0,(l[0]-2*l[2])//6) != df)
fails_c = sum(1 for (d,l,df,ct) in data if max(0,(l[0]-2*l[2])//6) != ct)
n_rows = len(data)
print(f"\nWORLD B: rows (all dominants, delta <= 10): {n_rows}")
print(f"naive transport floor((l1-2l3)/6)+ : mismatches vs deficit {fails_d}, vs conductor {fails_c}")
ex = [(d,l,df,ct, max(0,(l[0]-2*l[2])//6)) for (d,l,df,ct) in data if max(0,(l[0]-2*l[2])//6) != df][:8]
print("first mismatches (delta, lam, deficit, cond, predicted):")
for e in ex: print("  ", e)

# exhaustive linear-floor search: floor((al1+bl2+gl3)/w)+ matching DEFICIT on all rows
survivors_d, survivors_c, survivors_s = [], [], []
for w in range(1, 13):
    for al in range(0, 7):
        for be in range(-6, 7):
            for ga in range(-6, 7):
                okd = okc = oks = True
                for (d, l, df, ct) in data:
                    val = al*l[0] + be*l[1] + ga*l[2]
                    pred = val//w if val > 0 else 0
                    if pred < 0: pred = 0
                    if okd and pred != df: okd = False
                    if okc and pred != ct: okc = False
                    if oks and ((pred >= 1) != (df > 0)): oks = False
                    if not (okd or okc or oks): break
                if okd: survivors_d.append((al,be,ga,w))
                if okc: survivors_c.append((al,be,ga,w))
                if oks: survivors_s.append((al,be,ga,w))
print(f"\nexhaustive linear-floor search (|coef|<=6, w<=12):")
print(f"  formulas matching ALL deficits:   {len(survivors_d)}  {survivors_d[:5]}")
print(f"  formulas matching ALL conductors: {len(survivors_c)}  {survivors_c[:5]}")
print(f"  formulas matching support only:   {len(survivors_s)}  {survivors_s[:6]}")

# how often deficit == conductor in B?
neq = sum(1 for (d,l,df,ct) in data if df != ct and df > 0)
print(f"\nrows with deficit != conductor in B: {neq} of {sum(1 for r in data if r[2]>0)} deficit rows")
mx = max((df for (_,_,df,_) in data), default=0)
print("max single deficit in range:", mx)
