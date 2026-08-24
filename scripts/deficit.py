import math, cmath, itertools

TOL = 1e-6
def iround(x):
    r = round(x.real) if isinstance(x, complex) else round(x)
    err = abs(x - r)
    assert err < TOL, (x, r, err)
    return int(r)

# ================= weight histograms =================
def hist2(dmax, d=4):
    # arr[deg][b] = dim of weight (d*deg-b, b) space of Sym^deg(Sym^d C^2)
    W = d*dmax
    arr = [[0]*(W+1) for _ in range(dmax+1)]
    arr[0][0] = 1
    for e in range(d+1):                     # generator with y-degree e
        for deg in range(1, dmax+1):
            row, prow = arr[deg], arr[deg-1]
            for w in range(e, d*deg+1):
                v = prow[w-e]
                if v: row[w] += v
    return arr

def hist3(dmax):
    # arr[deg][w1][w2] = dim of weight (w1,w2,3deg-w1-w2) space of Sym^deg(Sym^3 C^3)
    gens = [(e1, e2) for e1 in range(4) for e2 in range(4-e1)]  # e3 implicit
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

# ================= irrep multiplicities =================
def multA(h, deg, a, b):
    # mult of S_(a,b) in Sym^deg(Sym^4 C^2); labels: a>=b>=0, a+b=4deg
    if deg < 0 or b < 0 or a < b or a+b != 4*deg: return 0
    m1 = h[deg][b]
    m2 = h[deg][b-1] if b-1 >= 0 else 0
    return m1 - m2

PERMS3 = []
for p in itertools.permutations((0,1,2)):
    sg = 1
    for i in range(3):
        for j in range(i+1,3):
            if p[i] > p[j]: sg = -sg
    PERMS3.append((p, sg))
RHO = (2,1,0)

def multB(h, deg, lam):
    # mult of S_lam in Sym^deg(Sym^3 C^3); lam dominant, lam3>=0, |lam|=3deg
    if deg < 0 or lam[2] < 0 or lam[0] < lam[1] or lam[1] < lam[2]: return 0
    if sum(lam) != 3*deg: return 0
    l = (lam[0]+RHO[0], lam[1]+RHO[1], lam[2]+RHO[2])
    tot = 0
    for p, sg in PERMS3:
        t = (l[p[0]]-RHO[0], l[p[1]]-RHO[1], l[p[2]]-RHO[2])
        if t[0] < 0 or t[1] < 0 or t[2] < 0: continue
        if t[0] > 3*deg or t[1] > 3*deg: continue
        tot += sg * h[deg][t[0]][t[1]]
    return tot

# ================= closure multiplicities =================
def closureA(h, deg, a, b):
    # C[sigma2-cone]_deg = Sym/(catalecticant C3, weight det^6, degree 3)
    return multA(h, deg, a, b) - multA(h, deg-3, a-6, b-6)

def closureB(h, deg, lam):
    # C[sigma3-cone]_deg = Sym/(Aronhold S, weight det^4, degree 4)
    return multB(h, deg, lam) - multB(h, deg-4, (lam[0]-4, lam[1]-4, lam[2]-4))

# ================= orbit dimensions via Peter-Weyl =================
def h_series_2(x, y, top):
    e1, e2 = x+y, x*y
    hs = [1+0j]*(top+1)
    if top >= 1: hs[1] = e1
    for j in range(2, top+1):
        hs[j] = e1*hs[j-1] - e2*hs[j-2]
    return hs

def schur2(a, b, x, y):
    m = a - b
    hs = h_series_2(x, y, m)
    return (x*y)**b * hs[m]

H_A = []   # 32 elements as eigenvalue pairs + det
I = 1j
for p in range(4):
    for q in range(4):
        H_A.append((I**p, I**q))                # diag
for p in range(4):
    for q in range(4):
        z = cmath.exp(1j*math.pi*(p+q)/4.0)     # sqrt(i^{p+q})
        H_A.append((z, -z))                     # antidiag
assert len(H_A) == 32

def orbitA(a, b):
    s = 0
    for (x, y) in H_A:
        s += schur2(a, b, x, y)
    return iround(s/32)

def h_series_3(evs, top):
    x, y, z = evs
    e1 = x+y+z; e2 = x*y+x*z+y*z; e3 = x*y*z
    hs = [0j]*(top+3)
    hs[0] = 1+0j
    if top >= 1: hs[1] = e1
    if top >= 2: hs[2] = e1*hs[1] - e2
    for j in range(3, top+1):
        hs[j] = e1*hs[j-1] - e2*hs[j-2] + e3*hs[j-3]
    return hs

def schur3(lam, evs):
    top = lam[0] + 2
    hs = h_series_3(evs, top)
    def hh(k): return hs[k] if k >= 0 else 0j
    r1 = (hh(lam[0]),   hh(lam[0]+1), hh(lam[0]+2))
    r2 = (hh(lam[1]-1), hh(lam[1]),   hh(lam[1]+1))
    r3 = (hh(lam[2]-2), hh(lam[2]-1), hh(lam[2]))
    det = (r1[0]*(r2[1]*r3[2]-r2[2]*r3[1])
         - r1[1]*(r2[0]*r3[2]-r2[2]*r3[0])
         + r1[2]*(r2[0]*r3[1]-r2[1]*r3[0]))
    return det

W3 = cmath.exp(2j*math.pi/3)
H_B = []  # 162 elements as eigenvalue triples
def cycles_of(sigma):
    seen = [False]*3; cyc = []
    for i in range(3):
        if not seen[i]:
            c = []; j = i
            while not seen[j]:
                seen[j] = True; c.append(j); j = sigma[j]
            cyc.append(c)
    return cyc
for sigma in itertools.permutations((0,1,2)):
    cyc = cycles_of(sigma)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                scal = (W3**a, W3**b, W3**c)
                evs = []
                for cy in cyc:
                    prod = 1+0j
                    for i in cy: prod *= scal[i]
                    L = len(cy)
                    r = cmath.exp(cmath.log(prod)/L)
                    for k in range(L):
                        evs.append(r*cmath.exp(2j*math.pi*k/L))
                H_B.append(tuple(evs))
assert len(H_B) == 162

def orbitB(lam):
    s = 0
    for evs in H_B:
        s += schur3(lam, evs)
    return iround(s/162)

# ================= boundary orbit (case A): x^3 y, stabilizer diag(t, t^-3) =================
def bndA(a, b):
    # dim of zero-weight space of S_(a,b) under t -> diag(t, t^-3): weights t^{4j-3(a+b)}, j=b..a
    n = 3*(a+b)
    if n % 4: return 0
    j = n // 4
    return 1 if b <= j <= a else 0

# ================= build =================
DMAX_A = 46
DMAX_B = 44
print("building histograms ...")
h2 = hist2(DMAX_A)
h3 = hist3(DMAX_B)

# ---- anchors, case A ----
assert multA(h2, 1, 4, 0) == 1
assert closureA(h2, 2, 6, 2) == 1            # Hessian survives
assert multA(h2, 3, 6, 6) == 1               # g3 = catalecticant exists upstairs
assert closureA(h2, 3, 6, 6) == 0            # ... and dies on sigma2
for deg in range(0, 11):
    tot = sum(multA(h2, deg, 4*deg-b, b)*(4*deg-2*b+1) for b in range(0, 2*deg+1))
    assert tot == math.comb(deg+4, 4), (deg, tot)
print("case A anchors OK")

# ---- anchors, case B ----
assert multB(h3, 4, (4,4,4)) == 1            # Aronhold S
assert closureB(h3, 4, (4,4,4)) == 0
assert multB(h3, 6, (6,6,6)) == 1            # T
assert closureB(h3, 6, (6,6,6)) == 1
assert multB(h3, 8, (8,8,8)) == 1            # S^2
assert multB(h3, 12, (12,12,12)) == 2        # S^3, T^2
assert closureB(h3, 12, (12,12,12)) == 1     # T^2 survives
def dimGL3(lam):
    return (lam[0]-lam[1]+1)*(lam[1]-lam[2]+1)*(lam[0]-lam[2]+2)//2
for deg in range(0, 9):
    tot = 0
    for lam in dominants3(deg) if False else []:
        pass
    # inline dominant enumeration
    tot = 0
    n = 3*deg
    for l1 in range(0, n+1):
        for l2 in range(0, min(l1, n-l1)+1):
            l3 = n - l1 - l2
            if l3 < 0 or l3 > l2: continue
            m = multB(h3, deg, (l1,l2,l3))
            assert m >= 0, ((l1,l2,l3), deg, m)
            tot += m*dimGL3((l1,l2,l3))
    assert tot == math.comb(deg+9, 9), (deg, tot, math.comb(deg+9,9))
print("case B anchors OK")

def dominants(n):
    out = []
    for l1 in range(0, n+1):
        for l2 in range(0, min(l1, n-l1)+1):
            l3 = n - l1 - l2
            if 0 <= l3 <= l2: out.append((l1,l2,l3))
    return out

# ================= deficits and profiles, case A =================
print("\n=== CASE A: sigma_2(v_4(P^1)), v = x^4+y^4, |H| = 32 ===")
MM_A = 6
firstA = None
rowsA = []
for deg in range(0, 11):
    for b in range(0, 2*deg+1):
        a = 4*deg - b
        cm = closureA(h2, deg, a, b)
        assert cm >= 0
        od = orbitA(a, b)
        assert od >= cm, ("deficit negative!", deg, (a,b), cm, od)
        if od > cm:
            prof = [closureA(h2, deg+6*m, a+12*m, b+12*m) for m in range(MM_A+1)]
            for i in range(MM_A):
                assert prof[i] <= prof[i+1], ("non-monotone", deg, (a,b), prof)
            cond = next((m for m in range(MM_A+1) if prof[m] == od), None)
            rowsA.append((deg, (a,b), cm, od, od-cm, cond, prof, bndA(a,b), bndA(a+12,b+12)))
            if firstA is None: firstA = (deg, (a,b))
if not rowsA:
    print("no deficit found for deg <= 10")
else:
    print("first strict deficit:", firstA)
    print("deg  (a,b)      closure orbit deficit conductor profile  bnd(a,b) bnd(+12)")
    for r in rowsA:
        print(f"{r[0]:>3}  {str(r[1]):<10} {r[2]:>5} {r[3]:>5} {r[4]:>5}   {str(r[5]):>4}   {r[6]}  {r[7]} {r[8]}")

# polar sector, case A
print("\ncase A polar classes (b < 0, invisible in the closure), scan a+b=4d, d<=3:")
cnt = 0
for d in range(0, 4):
    for b in range(-12, 0):
        a = 4*d - b
        od = orbitA(a, b)
        if od != 0:
            print(f"  d={d} (a,b)=({a},{b}): orbit dim {od}")
            cnt += 1
print(f"  ({cnt} polar classes found in scan)")

# ================= deficits and profiles, case B =================
print("\n=== CASE B: sigma_3(v_3(P^2)) = {Aronhold=0}, v = Fermat cubic, |H| = 162 ===")
MM_B = 2
firstB = None
rowsB = []
totdef = {}
for deg in range(0, 9):
    td = 0
    for lam in dominants(3*deg):
        cm = closureB(h3, deg, lam)
        assert cm >= 0, (deg, lam, cm)
        od = orbitB(lam)
        assert od >= cm, ("deficit negative!", deg, lam, cm, od)
        if od > cm:
            prof = [closureB(h3, deg+12*m, (lam[0]+12*m, lam[1]+12*m, lam[2]+12*m)) for m in range(MM_B+1)]
            for i in range(MM_B):
                assert prof[i] <= prof[i+1], ("non-monotone", deg, lam, prof)
            cond = next((m for m in range(MM_B+1) if prof[m] == od), None)
            rowsB.append((deg, lam, cm, od, od-cm, cond, prof))
            td += od - cm
            if firstB is None: firstB = (deg, lam)
    totdef[deg] = td
print("total deficit by degree:", totdef)
if firstB is None:
    print("no deficit found for deg <= 8")
else:
    print("first strict deficit:", firstB)
    print("deg  lambda        closure orbit deficit conductor profile")
    for r in rowsB[:40]:
        print(f"{r[0]:>3}  {str(r[1]):<13} {r[2]:>5} {r[3]:>5} {r[4]:>5}   {str(r[5]):>4}   {r[6]}")
    if len(rowsB) > 40: print(f"  ... ({len(rowsB)} deficit rows total)")
print("\ndone.")
