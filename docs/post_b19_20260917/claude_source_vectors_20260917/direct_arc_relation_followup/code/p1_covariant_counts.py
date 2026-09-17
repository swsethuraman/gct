"""Pilot 1: two exact character counts (pure Python integers, no numpy).

(1) m = dim Cov, Cov = Hom_{GL(A)xGL(B)}(Sym^2 Lambda^5(A (x) B), Lambda^2 A (x) Lambda^2 B (x) det_A^2 det_B^2)
    = the space of quadratic GL x GL-covariants D -> X in A^2 (x) B^2 (Lambda^2-parts) of the 5-wedge D.
    Route (i): plethysm/LR: Lambda^5(A(x)B) = sum_{mu |- 5} S_mu A (x) S_mu' B; Sym^2 of the sum; multiplicity of
               S_3322 A (x) S_3322 B via the S_4 alternant on 4-variable characters.
    Route (ii): weight pairs: weight multiset of Lambda^5(A(x)B) (5-subsets of the 16 weights), Sym^2 weight
               multiplicities, double alternant.
(2) N_top = dim Hom_L(Sym^2(Lambda^2(W_{-1}+W_{+1}) (x) Lambda^3 W_0), Lambda^2 A (x) Lambda^2 B (x) det_A^2 det_B^2)
    for the grading-preserving Levi L (variables x1,x2,x3, alpha, beta, c; L-trivial characters = powers of
    phi = alpha beta c^3 det^2). Route (a): invariants of S^* (x) T by the alternant over all twists phi^k.
    Route (b): decompose S and T into GL_3 x (C*)^3 irreducibles and match up to phi-twists.
Controls: dimension sums (4368, 3081, 36), small plethysm identities."""
import itertools, json, sys, time
from fractions import Fraction
T0 = time.perf_counter()
OUT = sys.argv[1] if len(sys.argv) > 1 else 'results/p1_covariant_counts.json'
rec = dict(checks={}, m={}, N_top={}, stage_times={})
def save(stage):
    rec['stage_times'][stage] = time.perf_counter() - T0
    json.dump(rec, open(OUT, 'w'), indent=1); print('stage', stage, round(rec['stage_times'][stage], 2), flush=True)

def padd(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0: del r[k]
    return r
def pmul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2)); r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v}
def pscale(p, mono): return {tuple(a + b for a, b in zip(k, mono)): v for k, v in p.items()}
def adams2(p): return {tuple(2 * a for a in k): v for k, v in p.items()}
def pdual(p): return {tuple(-a for a in k): v for k, v in p.items()}
def dim_of(p): return sum(p.values())
def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s
def h_list(monos, nmax):
    nv = len(monos[0]); one = {tuple([0] * nv): 1}
    H = [one] + [dict() for _ in range(nmax)]
    for m in monos:
        powers = [one]
        for j in range(1, nmax + 1): powers.append(pmul(powers[-1], {m: 1}))
        newH = []
        for n in range(nmax + 1):
            acc = {}
            for j in range(n + 1): acc = padd(acc, pmul(powers[j], H[n - j]))
            newH.append(acc)
        H = newH
    return H
def schur(lam, monos):
    lam = [x for x in lam if x > 0]; l = len(lam); nv = len(monos[0])
    if l == 0: return {tuple([0] * nv): 1}
    H = h_list(monos, max(lam) + l)
    def h(n): return H[n] if 0 <= n < len(H) else ({tuple([0] * nv): 1} if n == 0 else {})
    total = {}
    for p in itertools.permutations(range(l)):
        term = {tuple([0] * nv): 1}
        for i in range(l):
            term = pmul(term, h(lam[i] - i + p[i]))
            if not term: break
        total = padd(total, term, perm_sign(p))
    return total
def e2(monos):
    r = {}
    for i in range(len(monos)):
        for j in range(i + 1, len(monos)):
            k = tuple(a + b for a, b in zip(monos[i], monos[j])); r[k] = r.get(k, 0) + 1
    return r
def mult_hw(char, nu, xidx, fixed):
    """multiplicity of the GL_k irreducible nu (torus positions xidx) with the other positions fixed."""
    k = len(nu); rho = tuple(range(k - 1, -1, -1)); total = 0; nv = len(next(iter(char)))
    for sigma in itertools.permutations(range(k)):
        srho = tuple(rho[sigma[i]] for i in range(k)); target = [0] * nv
        for i, pos in enumerate(xidx): target[pos] = nu[i] + rho[i] - srho[i]
        for pos, e in fixed.items(): target[pos] = e
        total += perm_sign(sigma) * char.get(tuple(target), 0)
    return total
def conj(lam):
    return tuple(sum(1 for x in lam if x > j) for j in range(lam[0])) if lam else ()
def dim_gl(lam, n):
    lam = [x for x in lam if x > 0]
    if not lam: return 1
    cj = [sum(1 for x in lam if x > j) for j in range(lam[0])]; num = Fraction(1)
    for i, row in enumerate(lam):
        for j in range(row): num *= Fraction(n + j - i, row - j + cj[j] - i - 1)
    assert num.denominator == 1; return int(num)

# ============================================================ (1) m
X4 = [tuple(1 if i == j else 0 for j in range(4)) for i in range(4)]
MUS = [(4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1)]           # mu |- 5 inside the 4x4 box
rec['checks']['sum_dim_Smu_Smuprime_expect_4368'] = sum(dim_gl(m, 4) * dim_gl(conj(m), 4) for m in MUS)
S = {m: schur(m, X4) for m in MUS}
S.update({conj(m): schur(conj(m), X4) for m in MUS if conj(m) not in S})
TARGET = (3, 3, 2, 2)
def sym2(p): return {k: v // 2 for k, v in padd(pmul(p, p), adams2(p)).items() if v}
def alt2(p): return {k: v // 2 for k, v in padd(pmul(p, p), adams2(p), -1).items() if v}
for p in (pmul(S[(4, 1)], S[(4, 1)]),):
    assert all(v % 2 == 0 for v in padd(p, adams2(S[(4, 1)])).values())
# small plethysm controls: Sym^2(Lambda^2 C^4) = S_22 + S_1111, Lambda^2(Lambda^2 C^4) = S_211
L2 = schur((1, 1), X4)
rec['checks']['Sym2_Lambda2_C4'] = dict(S22=mult_hw(sym2(L2), (2, 2, 0, 0), [0, 1, 2, 3], {}), S1111=mult_hw(sym2(L2), (1, 1, 1, 1), [0, 1, 2, 3], {}), S31=mult_hw(sym2(L2), (3, 1, 0, 0), [0, 1, 2, 3], {}), expect='S22=1,S1111=1,S31=0')
rec['checks']['Lambda2_Lambda2_C4_S211_expect_1'] = mult_hw(alt2(L2), (2, 1, 1, 0), [0, 1, 2, 3], {})
def M(p): return mult_hw(p, TARGET, [0, 1, 2, 3], {})
mi = 0; tab = []
for mu in MUS:
    mp = conj(mu)
    a_s, a_l = M(sym2(S[mu])), M(alt2(S[mu])); b_s, b_l = M(sym2(S[mp])), M(alt2(S[mp]))
    tab.append(dict(mu=list(mu), muprime=list(mp), Sym2_A=a_s, Sym2_B=b_s, Lam2_A=a_l, Lam2_B=b_l, contribution=a_s * b_s + a_l * b_l))
    mi += a_s * b_s + a_l * b_l
for i in range(len(MUS)):
    for j in range(i + 1, len(MUS)):
        mu, nu = MUS[i], MUS[j]
        a = M(pmul(S[mu], S[nu])); b = M(pmul(S[conj(mu)], S[conj(nu)]))
        tab.append(dict(mu=list(mu), nu=list(nu), A_side=a, B_side=b, contribution=a * b)); mi += a * b
rec['m']['route_i_plethysm'] = dict(value=mi, table=tab)
print('m (plethysm route) =', mi, flush=True); save('m_route_i')
# route (ii): weight pairs
basis = [(i, j) for i in range(4) for j in range(4)]
wts = {}
for sub in itertools.combinations(range(16), 5):
    w = [0] * 8
    for s in sub:
        i, j = basis[s]; w[i] += 1; w[4 + j] += 1
    w = tuple(w); wts[w] = wts.get(w, 0) + 1
rec['checks']['Lambda5_weight_total_expect_4368'] = sum(wts.values())
def sym2_mult(omega):
    tot = 0
    for e, me in wts.items():
        f = tuple(o - a for o, a in zip(omega, e))
        if f in wts: tot += me * wts[f]
    half = tuple(o // 2 for o in omega) if all(o % 2 == 0 for o in omega) else None
    if half in wts: tot += wts[half]
    assert tot % 2 == 0; return tot // 2
rho4 = (3, 2, 1, 0); mii = 0
perms = list(itertools.permutations(range(4)))
for s1 in perms:
    for s2 in perms:
        t1 = tuple(TARGET[i] + rho4[i] - rho4[s1[i]] for i in range(4)); t2 = tuple(TARGET[i] + rho4[i] - rho4[s2[i]] for i in range(4))
        mii += perm_sign(s1) * perm_sign(s2) * sym2_mult(t1 + t2)
rec['m']['route_ii_weight_pairs'] = mii; rec['m']['agree'] = (mi == mii); rec['m']['value'] = mi
print('m (weight-pair route) =', mii, flush=True); save('m_route_ii')

# ============================================================ (2) N_top
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def w6(x, al, be, c): return tuple(x) + (al, be, c)
def addv(u, v): return tuple(a + b for a, b in zip(u, v))
Wm1 = [w6((0, 0, 0), 1, 1, 0)] + [w6(E3[i], 1, 0, 1) for i in range(3)]
Wp1 = [w6(E3[i], 0, 1, 0) for i in range(3)] + [w6(addv(E3[i], E3[j]), 0, 0, 1) for i in range(3) for j in range(i, 3)]
W0 = [w6(addv(E3[i], E3[j]), 0, 0, 1) for i in range(3) for j in range(i + 1, 3)]
chi_L3W0 = tuple(sum(m[k] for m in W0) for k in range(6))            # Lambda^3 W_0 = product of the three weights
assert chi_L3W0 == (2, 2, 2, 0, 0, 3)
Q = e2(Wm1 + Wp1); assert dim_of(Q) == 78
Qt = pscale(Q, chi_L3W0)
Ssym = sym2(Qt); rec['checks']['dim_S_expect_3081'] = dim_of(Ssym)
A_L = [w6((0, 0, 0), 1, 0, 0)] + [w6(E3[i], 0, 0, 0) for i in range(3)]
B_L = [w6((0, 0, 0), 0, 1, 0)] + [w6(E3[i], 0, 0, 1) for i in range(3)]
detA = (1, 1, 1, 1, 0, 0); detB = (1, 1, 1, 0, 1, 3)
Tchar = pscale(pmul(e2(A_L), e2(B_L)), tuple(2 * a + 2 * b for a, b in zip(detA, detB)))
rec['checks']['dim_T_expect_36'] = dim_of(Tchar)
# route (a): invariants of S^* (x) T
prod = pmul(pdual(Ssym), Tchar)
na = 0; per_k = {}
for k in range(-8, 9):
    v = mult_hw(prod, (2 * k, 2 * k, 2 * k), [0, 1, 2], {3: k, 4: k, 5: 3 * k})
    if v: per_k[str(k)] = v
    na += v
rec['N_top']['route_a_invariants_of_Sdual_T'] = dict(value=na, by_twist_k=per_k)
print('N_top (route a) =', na, per_k, flush=True); save('Ntop_route_a')
# route (b): decompose S and T into irreducibles and match up to phi^k twists
def decompose(char):
    out = {}
    for mono in char:
        x = mono[:3]
        if not (x[0] >= x[1] >= x[2]): continue
        key = mono
        if key in out: continue
        v = mult_hw(char, x, [0, 1, 2], {3: mono[3], 4: mono[4], 5: mono[5]})
        if v: out[key] = v
    return out
dS = decompose(Ssym); dT = decompose(Tchar)
rec['checks']['decomposition_dims'] = dict(S=sum(v * dim_gl(k[:3], 3) for k, v in dS.items()), T=sum(v * dim_gl(k[:3], 3) for k, v in dT.items()))
nb = 0; matches = []
for kS, vS in dS.items():
    for k in range(-8, 9):
        kT = (kS[0] + 2 * k, kS[1] + 2 * k, kS[2] + 2 * k, kS[3] + k, kS[4] + k, kS[5] + 3 * k)
        if kT in dT:
            nb += vS * dT[kT]; matches.append(dict(S_irrep=list(kS), mult_S=vS, T_irrep=list(kT), mult_T=dT[kT], twist_k=k))
rec['N_top']['route_b_irreducible_matching'] = dict(value=nb, matches=matches)
rec['N_top']['agree'] = (na == nb); rec['N_top']['value'] = na
rec['N_top']['T_irreducibles'] = [dict(irrep=list(k), mult=v) for k, v in dT.items()]
print('N_top (route b) =', nb, 'matches', matches, flush=True)
rec['elapsed_s'] = time.perf_counter() - T0
save('done')
