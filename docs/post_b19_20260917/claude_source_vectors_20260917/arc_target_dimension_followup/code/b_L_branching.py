"""b_L = dim F^L for d = 5, lambda = (4^5): the L-invariants of the forbidden (skew-degree 11 and 12)
part of S_lambda(W), W = Mat_4, L = grading-preserving Levi (B19-01 Prop. 6.1):
    L = {(diag(alpha, g), diag(beta, c g^T)) : g in GL_3, alpha beta c^3 det(g)^2 = 1}.
Pieces as GL_3 x (C*)^3 modules (weights x1,x2,x3; scalars alpha, beta, c):
    W_{-1} = a (alpha beta) + r (alpha c, std);  W_0 = v (c, Lambda^2 std);  W_{+1} = c-vec (beta, std) + Sigma (c, Sym^2 std).
Invariant condition (REPORT.md section 3.2): GL_3 type (10,10,10), (alpha,beta,c)-exponents (5,5,15).

Formulation I  (B19-01 section 6.3 recipe): sum over (mu, kappa, tau) of c^lambda_{mu kappa tau} times the
   multiplicity of det^10 x alpha^5 beta^5 c^15 in s_mu(W_{-1}) s_kappa(W_0) s_tau(W_{+1}) (Jacobi-Trudi
   characters, S_3 alternant extraction). LR coefficients by alternant extraction in 5 variables AND by the
   combinatorial Littlewood-Richardson rule (independent implementation), asserted equal.
Formulation II (independent of I): weight-space count. Multiplicity of det^10 in the graded piece
   = sum_{sigma in S_3} sgn(sigma) sum_{omega : x-weight = (10,10,10)+rho-sigma(rho), (5,5,15), #v = n} K_{lambda, omega},
   K = Kostka numbers (SSYT counts) over the 16 adapted basis weights.
Controls: graded decomposition identity sum_{|kappa|=n} c^lambda_{mu kappa tau} dim_4(mu) dim_3(kappa) dim_9(tau)
   = [u^n] s_lambda(1,1,1,1,u,u,u,1^9) for n = 11, 12 (Jacobi-Trudi in one variable); SYT count by the hook
   formula against the Kostka routine; small LR / plethysm identities; a small full decomposition identity.
Pure Python, exact integers, no numpy. JSON written after every stage."""
import itertools, json, math, sys, time
from functools import lru_cache
from fractions import Fraction
T0 = time.perf_counter()
LAM = (4, 4, 4, 4, 4)
OUT = sys.argv[1] if len(sys.argv) > 1 else 'results/b_L_branching.json'
rec = dict(cell=dict(d=5, lam=list(LAM)), checks={}, formulation_I={}, formulation_II={}, stage_times={})
def save(stage):
    rec['stage_times'][stage] = time.perf_counter() - T0
    json.dump(rec, open(OUT, 'w'), indent=1)
    print('stage', stage, round(rec['stage_times'][stage], 2), 's', flush=True)

# ----------------------------------------------------------------- polynomials as dicts
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

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def schur(lam, monos):
    lam = [x for x in lam if x > 0]
    l = len(lam); nv = len(monos[0])
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

def mult_hw(char, nu, xidx, fixed):
    """Multiplicity of the GL_k irreducible nu in `char` (dict over exponent tuples), GL_k torus variables at
    positions xidx, other variables fixed to given exponents. Direct dictionary lookups."""
    k = len(nu); rho = tuple(range(k - 1, -1, -1)); total = 0
    nv = len(next(iter(char)))
    for sigma in itertools.permutations(range(k)):
        srho = tuple(rho[sigma[i]] for i in range(k))
        target = [0] * nv
        for i, pos in enumerate(xidx): target[pos] = nu[i] + rho[i] - srho[i]
        for pos, e in fixed.items(): target[pos] = e
        total += perm_sign(sigma) * char.get(tuple(target), 0)
    return total

def mult_hw_product(p, q, nu, k):
    """Multiplicity of nu (k variables, all positions) in the product p*q without forming the product."""
    rho = tuple(range(k - 1, -1, -1)); total = 0
    for sigma in itertools.permutations(range(k)):
        srho = tuple(rho[sigma[i]] for i in range(k))
        target = tuple(nu[i] + rho[i] - srho[i] for i in range(k))
        acc = 0
        for m, cf in p.items():
            rest = tuple(t - a for t, a in zip(target, m))
            if min(rest) < 0: continue
            acc += cf * q.get(rest, 0)
        total += perm_sign(sigma) * acc
    return total

def partitions_in_box(n, maxparts, maxpart):
    def rec(n, maxparts, maxpart):
        if n == 0: yield (); return
        if maxparts == 0: return
        for k in range(min(n, maxpart), 0, -1):
            for rest in rec(n - k, maxparts - 1, k): yield (k,) + rest
    return list(rec(n, maxparts, maxpart))

def dim_gl(lam, n):
    lam = [x for x in lam if x > 0]
    if not lam: return 1
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])]
    num = Fraction(1)
    for i, row in enumerate(lam):
        for j in range(row):
            hook = row - j + conj[j] - i - 1
            num *= Fraction(n + j - i, hook)
    assert num.denominator == 1
    return int(num)

# ----------------------------------------------------------------- LR coefficients, two ways
Y5 = [tuple(1 if i == j else 0 for j in range(5)) for i in range(5)]
schur5 = {}
def s5(lam):
    if lam not in schur5: schur5[lam] = schur(lam, Y5)
    return schur5[lam]

def lr3_alternant(lam, mu, ka, ta):
    return mult_hw_product(pmul(s5(mu), s5(ta)), s5(ka), lam, 5)

@lru_cache(maxsize=None)
def lr2_comb(lam, mu, nu):
    """Combinatorial LR rule: LR tableaux of shape lam/mu, content nu (semistandard; reverse reading word lattice)."""
    lam = tuple(lam); mu = tuple(mu) + (0,) * (len(lam) - len(mu)); nu = tuple(x for x in nu if x > 0)
    if any(m > l for m, l in zip(mu, lam)): return 0
    if sum(lam) - sum(mu) != sum(nu): return 0
    cells = [(i, j) for i in range(len(lam)) for j in range(mu[i], lam[i])]
    if not cells: return 1 if not nu else 0
    order = sorted(cells, key=lambda c: (c[0], -c[1]))
    T = {}; count = [0]; cnt = [0] * (len(nu) + 1)
    def rec(idx):
        if idx == len(order):
            count[0] += 1; return
        i, j = order[idx]
        for k in range(1, len(nu) + 1):
            if cnt[k] + 1 > nu[k - 1]: continue
            if k > 1 and cnt[k] + 1 > cnt[k - 1]: continue
            if (i, j + 1) in T and T[(i, j + 1)] < k: continue
            if (i - 1, j) in T and T[(i - 1, j)] >= k: continue
            T[(i, j)] = k; cnt[k] += 1
            rec(idx + 1)
            del T[(i, j)]; cnt[k] -= 1
    rec(0)
    return count[0]

def lr3_comb(lam, mu, ka, ta):
    total = 0
    for th in partitions_in_box(sum(mu) + sum(ka), len(lam), lam[0]):
        a = lr2_comb(th, mu, ka)
        if a: total += a * lr2_comb(lam, th, ta)
    return total

# ----------------------------------------------------------------- small controls
X3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
s21 = schur((2, 1), X3); s2 = schur((2,), X3)
rec['checks']['S21xS21_contains_S222_expect_1'] = mult_hw(pmul(s21, s21), (2, 2, 2), [0, 1, 2], {})
rec['checks']['S2xS2xS2_contains_S222_expect_1'] = mult_hw(pmul(pmul(s2, s2), s2), (2, 2, 2), [0, 1, 2], {})
rec['checks']['dim_S21_C3_expect_8'] = sum(s21.values())
rec['checks']['lr_alt_444_44_to_4^5_expect_1'] = lr3_alternant(LAM, (4, 4, 4), (4, 4), ())
rec['checks']['lr_alt_444_431_to_4^5_expect_0'] = lr3_alternant(LAM, (4, 4, 4), (4, 3, 1), ())
rec['checks']['lr_comb_444_44_to_4^5_expect_1'] = lr2_comb(LAM, (4, 4, 4), (4, 4))
rec['checks']['lr_comb_222_21_21_expect_1'] = lr2_comb((2, 2, 2), (2, 1), (2, 1))
# small full decomposition identity: S_(2,2)(C^1 + C^2 + C^3) = sum c dim dim dim = dim S_(2,2)(C^6) = 105
tot = 0
for mu in [m for n in range(5) for m in partitions_in_box(n, 1, 2)]:
    for ka in [k for n in range(5) for k in partitions_in_box(n, 2, 2)]:
        nt = 4 - sum(mu) - sum(ka)
        if nt < 0: continue
        for ta in partitions_in_box(nt, 2, 2):
            c = lr3_comb((2, 2), mu, ka, ta)
            tot += c * dim_gl(mu, 1) * dim_gl(ka, 2) * dim_gl(ta, 3)
rec['checks']['small_identity_S22_C6'] = dict(sum=tot, expect=dim_gl((2, 2), 6), passed=(tot == dim_gl((2, 2), 6)))
save('small_controls')

# ----------------------------------------------------------------- graded decomposition identity for n = 11, 12
U = [(0,)] * 13 + [(1,)] * 3            # 13 weight-1 basis vectors, 3 of weight u (the v's)
s_lam_u = schur(LAM, U)
rec['checks']['graded_identity'] = {}
for n in (11, 12):
    lhs = 0; ntr = 0
    kas = partitions_in_box(n, 3, 4)
    for ka in kas:
        for m in range(0, 21 - n):
            for mu in partitions_in_box(m, 4, 4):
                for ta in partitions_in_box(20 - n - m, 5, 4):
                    c = lr3_alternant(LAM, mu, ka, ta)
                    if c: ntr += 1; lhs += c * dim_gl(mu, 4) * dim_gl(ka, 3) * dim_gl(ta, 9)
    rhs = s_lam_u.get((n,), 0)
    rec['checks']['graded_identity'][str(n)] = dict(kappas=[list(k) for k in kas], lhs_sum=lhs, rhs_coefficient_u_n=rhs, triples=ntr, passed=(lhs == rhs))
    print('graded identity n =', n, lhs, rhs, flush=True)
save('graded_identity')

# ----------------------------------------------------------------- Formulation I
def wt(x, al, be, c): return tuple(x) + (al, be, c)
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def addv(u, v): return tuple(a + b for a, b in zip(u, v))
W_m1 = [wt((0, 0, 0), 1, 1, 0)] + [wt(E[i], 1, 0, 1) for i in range(3)]
W_0 = [wt(addv(E[i], E[j]), 0, 0, 1) for i in range(3) for j in range(i + 1, 3)]
W_p1 = [wt(E[i], 0, 1, 0) for i in range(3)] + [wt(addv(E[i], E[j]), 0, 0, 1) for i in range(3) for j in range(i, 3)]
assert len(W_m1) == 4 and len(W_0) == 3 and len(W_p1) == 9
NU_TARGET = (10, 10, 10); FIXED = {3: 5, 4: 5, 5: 15}
tableI = []; bI = {11: 0, 12: 0}
for n in (11, 12):
    for ka in partitions_in_box(n, 3, 4):
        s_ka = schur(ka, W_0)
        for mu in partitions_in_box(5, 4, 4):
            s_mu = schur(mu, W_m1)
            for ta in partitions_in_box(15 - n, 5, 4):
                c_alt = lr3_alternant(LAM, mu, ka, ta); c_comb = lr3_comb(LAM, mu, ka, ta)
                assert c_alt == c_comb, (mu, ka, ta, c_alt, c_comb)
                if c_alt == 0: continue
                char = pmul(pmul(s_mu, s_ka), schur(ta, W_p1))
                I = mult_hw(char, NU_TARGET, [0, 1, 2], FIXED)
                # split by #a: alpha-exponent is 5 always; #a = 5 - #r where #r = x-degree contributed by r... use beta: #a = 5 - #c,
                # and #c + #Sigma = |tau|; record the multiplicity per beta-exponent split? (beta counts a and c together) -> split by
                # the a-degree via the character of S_mu(W_{-1}) alone is not separable here; per-pattern split is in Formulation II.
                tableI.append(dict(n=n, mu=list(mu), kappa=list(ka), tau=list(ta), c_lambda=c_alt, dim_S_mu_C4=dim_gl(mu, 4), dim_S_kappa_C3=dim_gl(ka, 3), dim_S_tau_C9=dim_gl(ta, 9), L_invariants=I, contribution=c_alt * I))
                bI[n] += c_alt * I
                print('I', n, mu, ka, ta, 'c=', c_alt, 'inv=', I, flush=True)
rec['formulation_I'] = dict(table=tableI, b_L_by_skew_degree={str(k): v for k, v in bI.items()}, b_L=bI[11] + bI[12])
print('Formulation I: b_L(11) =', bI[11], 'b_L(12) =', bI[12], 'b_L =', bI[11] + bI[12], flush=True)
save('formulation_I')

# ----------------------------------------------------------------- Formulation II: Kostka weight count
@lru_cache(maxsize=None)
def kostka(shape, content):
    shape = tuple(x for x in shape if x > 0); content = tuple(x for x in content if x > 0)
    if sum(shape) != sum(content): return 0
    if not content: return 1 if not shape else 0
    m = content[-1]; rest = content[:-1]; l = len(shape); total = 0
    def rec(i, remaining, nu):
        nonlocal total
        if i == l:
            if remaining == 0: total += kostka(tuple(nu), rest)
            return
        lo = shape[i + 1] if i + 1 < l else 0
        for v in range(shape[i], lo - 1, -1):
            take = shape[i] - v
            if take > remaining: continue
            rec(i + 1, remaining - take, nu + [v])
    rec(0, m, [])
    return total

def kostka_sorted(shape, content):
    return kostka(shape, tuple(sorted((x for x in content if x > 0), reverse=True)))

rec['checks']['kostka_21_111_expect_2'] = kostka_sorted((2, 1), (1, 1, 1))
rec['checks']['kostka_lam_lam_expect_1'] = kostka_sorted(LAM, LAM)
hooks = 1
for i in range(5):
    for j in range(4): hooks *= (4 - j) + (5 - i) - 1
rec['checks']['SYT_count_hook_formula'] = math.factorial(20) // hooks
rec['checks']['kostka_lam_1^20'] = kostka_sorted(LAM, (1,) * 20)
rec['checks']['kostka_SYT_passed'] = rec['checks']['SYT_count_hook_formula'] == rec['checks']['kostka_lam_1^20']
save('kostka_controls')

def compositions(n, k, maxpart=4):
    if k == 0:
        if n == 0: yield ()
        return
    for v in range(min(n, maxpart), -1, -1):
        for rest in compositions(n - v, k - 1, maxpart): yield (v,) + rest

XW = {'r': E, 'v': [addv(E[0], E[1]), addv(E[0], E[2]), addv(E[1], E[2])], 'c': E,
      'S': [addv(E[0], E[0]), addv(E[1], E[1]), addv(E[2], E[2]), addv(E[0], E[1]), addv(E[0], E[2]), addv(E[1], E[2])]}
rho3 = (2, 1, 0); targets = {}
for sigma in itertools.permutations(range(3)):
    srho = tuple(rho3[sigma[i]] for i in range(3))
    targets[tuple(NU_TARGET[i] + rho3[i] - srho[i] for i in range(3))] = perm_sign(sigma)
bII = {11: 0, 12: 0}; by_pattern = {}; by_pattern_dims = {}
for n in (11, 12):
    for wa in range(0, 5):
        for wr in compositions(5 - wa, 3):
            nS = 15 - sum(wr) - n
            if nS < 0: continue
            for wc in compositions(5 - wa, 3):
                for wv in compositions(n, 3):
                    for wS in compositions(nS, 6):
                        xw = [0, 0, 0]
                        for grp, ws in (('r', wr), ('v', wv), ('c', wc), ('S', wS)):
                            for e, w in zip(XW[grp], ws):
                                for i in range(3): xw[i] += e[i] * w
                        xw = tuple(xw)
                        if xw not in targets: continue
                        K = kostka_sorted(LAM, (wa,) + wr + wv + wc + wS)
                        if K == 0: continue
                        key = (n, wa, sum(wr), n, sum(wc), nS)
                        by_pattern[key] = by_pattern.get(key, 0) + targets[xw] * K
                        if xw == NU_TARGET: by_pattern_dims[key] = by_pattern_dims.get(key, 0) + K
                        bII[n] += targets[xw] * K
rec['formulation_II'] = dict(b_L_by_skew_degree={str(k): v for k, v in bII.items()}, b_L=bII[11] + bII[12],
                             by_multidegree_pattern=[dict(n=k[0], a=k[1], r=k[2], v=k[3], c=k[4], Sigma=k[5], L_invariants=v, weight_10_10_10_space_dim=by_pattern_dims.get(k, 0)) for k, v in sorted(by_pattern.items())])
print('Formulation II: b_L(11) =', bII[11], 'b_L(12) =', bII[12], 'b_L =', bII[11] + bII[12], flush=True)
rec['agreement'] = dict(formulations_agree=(bI == bII), b_L_11=bI[11], b_L_12=bI[12], b_L=bI[11] + bI[12])
rec['elapsed_s'] = time.perf_counter() - T0
save('done')
print(json.dumps({k: v for k, v in rec.items() if k != 'formulation_I'}, indent=1)[:5000])
