"""P2: five-variable certificates for Theorem B (Macaulay ranks r_k = rank M_k for k = 3..9).

Points: F_det = det(sum x_i A_i) with seeded integer A_i (a point of D45); F_prod = ell*C generic
integer product (a point of P5); F_padpt = x_1 * per_3(L x) with L a 9x5 integer matrix (an actual
five-variable padding restriction, a point of P5); F_smooth = random integer quartic (ambient control).
Exact rank over Q (flint.fmpz_mat.rank) for every point and every k <= 9 (matrices at most 1050 x 715).
A rank at a point is a lower bound on the generic rank of the closure containing that point; that is
the direction Theorem B(ii),(iii) uses for F_det. Controls: F_smooth must attain the generic maximum
rho_k = 5 dim S_{k-3} - 10 dim S_{k-6} + 10 dim S_{k-9}; the two P5 points must not exceed padUB(k).
"""
import itertools, json, math, os, random, time
from collections import defaultdict
import flint

T0 = time.perf_counter()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p2_quinary_macaulay.json')
NV = 5
KS = list(range(3, 10))
rng = random.Random(20260917)
res = {'script': 'p2_quinary_macaulay.py', 'seed': 20260917, 'checks': []}

def binom(n, k):
    return math.comb(n, k) if n >= 0 and 0 <= k <= n else 0

def dimS(m):
    return binom(m + NV - 1, NV - 1)

def monomials(nvars, deg):
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

# ---- tiny exact polynomial arithmetic on exponent dicts ----
def padd(A, B):
    C = defaultdict(int)
    for e, v in A.items():
        C[e] += v
    for e, v in B.items():
        C[e] += v
    return {e: v for e, v in C.items() if v}

def pmul(A, B):
    C = defaultdict(int)
    for e1, v1 in A.items():
        for e2, v2 in B.items():
            C[tuple(a + b for a, b in zip(e1, e2))] += v1 * v2
    return {e: v for e, v in C.items() if v}

def pscale(A, s):
    return {e: s * v for e, v in A.items()} if s else {}

def linear(coeffs):
    L = {}
    for i, c in enumerate(coeffs):
        if c:
            e = [0] * NV; e[i] = 1
            L[tuple(e)] = c
    return L

def det_of_pencil(As):
    """det(sum_i x_i A_i), A_i 4x4 integer matrices, via Leibniz."""
    n = 4
    entries = [[linear([As[i][r][c] for i in range(NV)]) for c in range(n)] for r in range(n)]
    F = {}
    for perm in itertools.permutations(range(n)):
        sgn = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    sgn = -sgn
        term = {tuple([0] * NV): sgn}
        for r in range(n):
            term = pmul(term, entries[r][perm[r]])
        F = padd(F, term)
    return F

def per3_of_forms(rows):
    """per_3 of a 3x3 matrix of linear forms."""
    F = {}
    for perm in itertools.permutations(range(3)):
        term = {tuple([0] * NV): 1}
        for r in range(3):
            term = pmul(term, rows[r][perm[r]])
        F = padd(F, term)
    return F

def random_form(deg, lo=-4, hi=4):
    return {e: rng.randint(lo, hi) for e in monomials(NV, deg) if True}

def partial(F, i):
    G = defaultdict(int)
    for e, cf in F.items():
        if e[i] > 0:
            e2 = list(e); e2[i] -= 1
            G[tuple(e2)] += cf * e[i]
    return dict(G)

def macaulay_rank_exact(F, k):
    cols = {e: t for t, e in enumerate(monomials(NV, k))}
    parts = [partial(F, i) for i in range(NV)]
    mons = list(monomials(NV, k - 3))
    mat = []
    for i in range(NV):
        for m in mons:
            row = [0] * len(cols)
            for e, cf in parts[i].items():
                row[cols[tuple(a + b for a, b in zip(e, m))]] += cf
            mat.append(row)
    return flint.fmpz_mat(mat).rank(), (len(mat), len(cols))

def rho(k):  # generic maximum (Koszul count), valid while the partials of a smooth quartic are a regular sequence
    return 5 * dimS(k - 3) - 10 * dimS(k - 6) + 10 * dimS(k - 9)

def padUB(k):
    return dimS(k) - (binom(k + 3, 3) - binom(k, 3))

# ---- points ----
As = [[[rng.randint(-5, 5) for _ in range(4)] for _ in range(4)] for _ in range(NV)]
F_det = det_of_pencil(As)
ell = linear([rng.randint(-4, 4) or 1 for _ in range(NV)])
C = random_form(3)
F_prod = pmul(ell, C)
L = [[rng.randint(-4, 4) for _ in range(NV)] for _ in range(9)]
rows = [[linear(L[3 * a + b]) for b in range(3)] for a in range(3)]
x1 = linear([1, 0, 0, 0, 0])
F_padpt = pmul(x1, per3_of_forms(rows))
F_smooth = random_form(4)
res['pencil_A'] = As
res['ell'] = [ell.get(tuple(1 if j == i else 0 for j in range(NV)), 0) for i in range(NV)]
res['L'] = L
res['n_terms'] = {'F_det': len(F_det), 'F_prod': len(F_prod), 'F_padpt': len(F_padpt), 'F_smooth': len(F_smooth)}
res['checks'].append({'name': 'F_det has all 70 monomials (pencil not degenerate)', 'pass': len(F_det) == 70})

table = {}
for k in KS:
    row = {'k': k, 'dimS': dimS(k), 'rho_generic_max': rho(k), 'padUB': padUB(k)}
    for name, F in (('F_det', F_det), ('F_prod', F_prod), ('F_padpt', F_padpt), ('F_smooth', F_smooth)):
        rk, shape = macaulay_rank_exact(F, k)
        row[name] = rk
        row[name + '_shape'] = shape
    table[k] = row
    print(json.dumps(row), f't={time.perf_counter()-T0:.1f}s', flush=True)
res['table'] = table

# expected determinantal profile from Remark 3.3 (Dimca + measured def_3 = 1, def_4 = 0, GN def_2 = 5, def_1 = 15):
# c_k = 30, 45, 51, 45, 31, 20, 20 for k = 3..9  ->  r_k = 5, 25, 75, 165, 299, 475, 695
expected_det = {3: 5, 4: 25, 5: 75, 6: 165, 7: 299, 8: 475, 9: 695}
res['checks'].append({'name': 'F_smooth attains rho_k for every k (ambient control)', 'pass': all(table[k]['F_smooth'] == rho(k) for k in KS)})
res['checks'].append({'name': 'F_det attains rho_k for k = 3, 4, 5, 6 (Theorem B (ii) and the k = 6 certificate)', 'pass': all(table[k]['F_det'] == rho(k) for k in (3, 4, 5, 6))})
res['checks'].append({'name': 'F_det = 299 at k = 7 (cap: rank drop by exactly one at this point)', 'pass': table[7]['F_det'] == 299})
res['checks'].append({'name': 'F_det matches the Remark 3.3 profile at k = 8, 9 (475, 695; MEASURED consistency, not used in the proof)', 'pass': all(table[k]['F_det'] == expected_det[k] for k in (8, 9)), 'value': [table[8]['F_det'], table[9]['F_det']]})
res['checks'].append({'name': 'both P5 points obey padUB(k) for every k (else the (ell, C) argument is wrong)', 'pass': all(table[k]['F_prod'] <= padUB(k) and table[k]['F_padpt'] <= padUB(k) for k in KS)})
res['checks'].append({'name': 'F_det rank strictly exceeds padUB(k) for every k >= 6 (the inequality of Theorem B at this point)', 'pass': all(table[k]['F_det'] > padUB(k) for k in KS if k >= 6)})
res['wall_seconds'] = time.perf_counter() - T0
res['all_checks_pass'] = all(c['pass'] for c in res['checks'])
with open(OUT, 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({c['name']: c['pass'] for c in res['checks']}, indent=1))
print('ALL PASS' if res['all_checks_pass'] else 'SOME CHECK FAILED', f'{res["wall_seconds"]:.1f}s')
