"""Week 1, session 4 — the Ogg-Shafarevich recursion.
World B: increments of the T-ray profile are multiplicities of C[sigma_3]/(T),
the ring of the cusp cone.  Test:
  r(lam, delta) := mult_lam C[sigma_3]/(T)  <=  m(lam) := #GT vectors of S_lam
                   with w1 = 2 w2   (= dim of H0-invariants, H0 = Gm x mu3),
with second-level deficit  d2 := m - r  >= 0  (primality evidence for (T)),
and  deficit(lam, delta) = sum_j [ m(lam+6j.1) - d2(lam+6j.1, delta+6j) ].
World A: same structure with the tangent-developable cone, m_A = Gm-invariant
count (0/1), steps by I (degree 2, weight det^4).
"""
import math, cmath, itertools
from collections import Counter

# ---------------- shared World B machinery ----------------
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
h3 = hist3(48)
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
def rB(deg, lam):
    # mult in C[sigma_3]/(T): subtract the T-shift
    return closureB(deg, lam) - closureB(deg-6, (lam[0]-6, lam[1]-6, lam[2]-6))

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

def mH0(lam):
    """# GT-basis vectors of S_lam with weight (w1,w2,w3) satisfying w1 == 2*w2
    (H0 = {diag(t, t^-2, gamma)}-invariants; the mu_3 condition is automatic)."""
    l1, l2, l3 = lam
    cnt = 0
    for a in range(l2, l1+1):
        for b in range(l3, l2+1):
            for t in range(b, a+1):
                w1, w2 = t, a + b - t
                if w1 == 2*w2:
                    cnt += 1
    return cnt

# ---------------- (1) base test: r <= m, tabulate d2 ----------------
viol = 0; d2_rows = []; zero_rows = 0; tot_rows = 0
for d in range(0, 13):
    for lam in dominants(3*d):
        r = rB(d, lam); m = mH0(lam)
        tot_rows += 1
        if r > m:
            viol += 1
            if viol <= 8: print("PRIMALITY VIOLATION r > m:", d, lam, r, m)
        else:
            d2 = m - r
            if d2 > 0: d2_rows.append((d, lam, r, m, d2))
            else: zero_rows += 1
print(f"(1) base: rows {tot_rows}, violations r>m: {viol}, exact r==m: {zero_rows}, d2>0 rows: {len(d2_rows)}")
print("    sample d2>0 rows (delta, lam, r, m, d2):")
for e in d2_rows[:14]: print("     ", e)
mx = max((e[4] for e in d2_rows), default=0)
print("    max d2 in range:", mx)

# ---------------- (2) O-S sum reproduces the deficit on all rows ----------------
bad = 0; nrows = 0
for d in range(0, 11):
    for lam in dominants(3*d):
        cm = closureB(d, lam); od = orbitB(lam)
        defc = od - cm
        if defc <= 0: continue
        nrows += 1
        s = 0
        for j in range(1, 7):
            lj = tuple(v + 6*j for v in lam)
            s += mH0(lj) - (mH0(lj) - rB(d+6*j, lj))   # = rB, written as m - d2
        if s != defc:
            bad += 1
            if bad <= 5: print("O-S SUM FAIL:", d, lam, defc, s)
print(f"(2) O-S sum  deficit == sum_j [m - d2] (shifted): verified on {nrows} rows, failures {bad}")
Ecorr = 0; Mtot = 0
for d in range(0, 11):
    for lam in dominants(3*d):
        if orbitB(lam) - closureB(d, lam) <= 0: continue
        for j in range(1, 7):
            lj = tuple(v + 6*j for v in lam)
            Mtot += mH0(lj)
            Ecorr += mH0(lj) - rB(d+6*j, lj)
print(f"    total eigencount mass {Mtot}, correction mass E (second-level deficit) {Ecorr}")

# ---------------- (3) structure of d2: support + floor search ----------------
# candidate torus of the next stratum (conic + tangent line, x^2 y + y^2 z):
# diag(s^-1, s^2, s^-4): weights (-1, 2, -4) sorted desc (2, -1, -4)
cand_fail = 0
for (d, lam, r, m, d2) in d2_rows:
    pass
survivors = []
rows_for_search = []
for d in range(0, 13):
    for lam in dominants(3*d):
        r = rB(d, lam); m = mH0(lam)
        rows_for_search.append((lam, m - r))
for w in range(1, 13):
    for al in range(-6, 7):
        for be in range(-6, 7):
            for ga in range(-6, 7):
                okv = True
                for (l, d2) in rows_for_search:
                    val = al*l[0] + be*l[1] + ga*l[2]
                    pred = val//w if val > 0 else 0
                    if pred < 0: pred = 0
                    if pred != d2: okv = False; break
                if okv: survivors.append((al, be, ga, w))
print(f"(3) exhaustive floor search on d2 values: survivors {len(survivors)} {survivors[:5]}")
supp = []
for w in range(1, 13):
    for al in range(-6, 7):
        for be in range(-6, 7):
            for ga in range(-6, 7):
                okv = True
                for (l, d2) in rows_for_search:
                    val = al*l[0] + be*l[1] + ga*l[2]
                    pred = val//w if val > 0 else 0
                    if (pred >= 1) != (d2 > 0): okv = False; break
                if okv: supp.append((al, be, ga, w))
print(f"    support-only survivors: {len(supp)} {supp[:6]}")

# ---------------- (4) World A: recursion bottoms out ----------------
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
h2 = hist2(40)
def multA(deg, a, b):
    if deg < 0 or b < 0 or a < b or a+b != 4*deg: return 0
    return h2[deg][b] - (h2[deg][b-1] if b-1 >= 0 else 0)
def closureA(deg, a, b):
    return multA(deg, a, b) - multA(deg-3, a-6, b-6)
def rA(deg, a, b):
    return closureA(deg, a, b) - closureA(deg-2, a-4, b-4)
def mA(a, b):
    n = 3*(a+b)
    if n % 4: return 0
    j = n//4
    return 1 if b <= j <= a else 0
violA = 0; d2A = Counter(); totA = 0
for d in range(0, 31):
    for b in range(0, 2*d+1):
        a = 4*d - b
        r = rA(d, a, b); m = mA(a, b)
        totA += 1
        if r > m: violA += 1
        else: d2A[m - r] += 1
print(f"\n(4) WORLD A recursion bottom: rows {totA}, violations r>m: {violA}, d2 histogram: {dict(d2A)}")
