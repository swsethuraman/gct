"""P1: sixteen-variable certificates for Theorem A (Macaulay ranks of det_4 vs z*per_3).

(a) exact Hilbert function u(j) = dim (C[y]/P)_j, P = ideal of the nine 2x2 permanents of a
    3x3 matrix of variables, j = 0..JMAX, by exact integer rank (flint.fmpz_mat, rank over Q)
    of the multigraded blocks of the spanning set { monomial * p_ab,cd };
(b) inequality (A4): r_k(pad) <= r_k(det) for k = 0..10 from formulas (A1)-(A3) with exact u(j);
    forward differences e_i = Delta^i Q(11) of the polynomial Q for the k >= 11 certificate;
(c) MEASURED: rank M_3, M_4 at det_4 and z*per_3 mod p (nmod_mat), cross-check of (A1)-(A2);
(d) MEASURED: rank of the second Koszul differential D_k, k = 6, 7 at det_4, z*per_3, random quartic
    (degree 7 through a random projection: a lower bound; 1920 = full row rank is exact).
Pure Python integers + python-flint; one process; no BLAS.
"""
import itertools, json, math, os, random, sys, time
from collections import defaultdict
import flint

T0 = time.perf_counter()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p1_ambient_macaulay.json')
P = 2**31 - 1
JMAX = 9
res = {'script': 'p1_ambient_macaulay.py', 'prime': P, 'JMAX': JMAX, 'checks': []}

def binom(n, k):
    return math.comb(n, k) if n >= 0 and 0 <= k <= n else 0

def p16(m):  # dim S_m in 16 variables
    return binom(m + 15, 15)

def c7(m):   # dim C[z,w]_m, 7 variables
    return binom(m + 6, 6)

def d9(m):   # dim C[y]_m, 9 variables
    return binom(m + 8, 8)

# ---------- (a) exact Hilbert function of the permanental ideal ----------
def monomials(nvars, deg):
    """All exponent tuples of total degree deg in nvars variables."""
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

# y variables indexed y[3*a+b], a = row, b = column
PERMS = []  # list of (index1, index2, index3, index4) pairs of monomials: p = y[a,c1] y[b,c2] + y[a,c2] y[b,c1]
for a, b in itertools.combinations(range(3), 2):
    for c1, c2 in itertools.combinations(range(3), 2):
        PERMS.append(((3 * a + c1, 3 * b + c2), (3 * a + c2, 3 * b + c1)))

def margins(e):
    r = (e[0] + e[1] + e[2], e[3] + e[4] + e[5], e[6] + e[7] + e[8])
    c = (e[0] + e[3] + e[6], e[1] + e[4] + e[7], e[2] + e[5] + e[8])
    return r + c

u = []
dimP = []
for j in range(JMAX + 1):
    mons = list(monomials(9, j))
    assert len(mons) == d9(j)
    blocks = defaultdict(dict)  # multidegree -> {monomial: column index}
    for e in mons:
        blk = blocks[margins(e)]
        blk[e] = len(blk)
    if j < 2:
        dimP.append(0); u.append(d9(j) - 0)
        continue
    rows_by_block = defaultdict(list)
    for m in monomials(9, j - 2):
        for (i1, i2), (i3, i4) in PERMS:
            e1 = list(m); e1[i1] += 1; e1[i2] += 1; e1 = tuple(e1)
            e2 = list(m); e2[i3] += 1; e2[i4] += 1; e2 = tuple(e2)
            key = margins(e1)
            assert margins(e2) == key
            rows_by_block[key].append((e1, e2))
    total_rank = 0
    nblocks = 0
    for key, rows in rows_by_block.items():
        blk = blocks[key]
        ncol = len(blk)
        mat = [[0] * ncol for _ in rows]
        for r, (e1, e2) in enumerate(rows):
            mat[r][blk[e1]] += 1
            mat[r][blk[e2]] += 1
        total_rank += flint.fmpz_mat(mat).rank()
        nblocks += 1
    dimP.append(total_rank)
    u.append(d9(j) - total_rank)
    print(f'j={j} dimP={total_rank} u={u[-1]} blocks={nblocks} t={time.perf_counter()-T0:.1f}s', flush=True)
res['u'] = u
res['dimP'] = dimP
res['checks'].append({'name': 'u(0..2) = 1, 9, 36', 'pass': u[:3] == [1, 9, 36]})
res['checks'].append({'name': 'dim P_3 = 77 (four linear syzygies of the cofactors)', 'pass': dimP[3] == 77, 'value': dimP[3]})

# ---------- (b) inequality (A4) for k <= 10 and the k >= 11 certificate ----------
def r_det(k):
    return 16 * p16(k - 3) - 30 * p16(k - 4) + 16 * p16(k - 5) - p16(k - 8)

def dimPS(m):
    if m < 0:
        return 0
    assert m <= JMAX
    return sum(dimP[j] * c7(m - j) for j in range(0, m + 1))

def r_pad(k):
    return p16(k - 3) - p16(k - 4) + dimPS(k - 1)

def Q(k):
    return 15 * p16(k - 3) - 29 * p16(k - 4) + 16 * p16(k - 5) - p16(k - 8) - p16(k - 1)

def U(m):
    return sum(u[j] * c7(m - j) for j in range(0, m + 1)) if m >= 0 else 0

table = []
ok_small = True
for k in range(0, 11):
    rp, rd = r_pad(k), r_det(k)
    lhs = Q(k) + U(k - 1)
    assert rd - rp == lhs, (k, rd - rp, lhs)   # (A4) is the same inequality, rewritten
    table.append({'k': k, 'r_pad': rp, 'r_det': rd, 'Q': Q(k), 'U': U(k - 1), 'ok': rp <= rd})
    ok_small &= rp <= rd
res['table_k_le_10'] = table
res['checks'].append({'name': 'r_pad(k) <= r_det(k) for k = 0..10 (exact)', 'pass': ok_small})
res['checks'].append({'name': 'hand values Q(11) = 7582, Q(12) = 392122', 'pass': Q(11) == 7582 and Q(12) == 392122, 'value': [Q(11), Q(12)]})

# forward differences at 11
vals = [Q(11 + i) for i in range(0, 18)]
e = []
for i in range(0, 17):
    e.append(sum((-1) ** (i - t) * math.comb(i, t) * vals[t] for t in range(0, i + 1)))
res['forward_differences_Q_at_11'] = e
res['checks'].append({'name': 'all e_i = Delta^i Q(11) >= 0 for i = 0..15 (Newton certificate: Q(k) >= 0 for all k >= 11)', 'pass': all(x >= 0 for x in e[:16])})
res['checks'].append({'name': 'Delta^14, Delta^15, Delta^16 Q(11) = 0 (Q has degree 13)', 'pass': e[14] == 0 and e[15] == 0 and e[16] == 0, 'value': e[13:17]})
if not all(x >= 0 for x in e[:16]):
    res['fallback_Q_nonneg_11_to_200'] = all(Q(k) >= 0 for k in range(11, 201))
print('forward differences', e, flush=True)

# ---------- (c) Macaulay ranks mod p in 16 variables ----------
NV = 16
def poly_det4():
    # variables x[4*i+j] = entry (i,j)
    F = defaultdict(int)
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sgn = -sgn
        e = [0] * NV
        for i in range(4):
            e[4 * i + perm[i]] += 1
        F[tuple(e)] += sgn
    return dict(F)

def poly_zper3():
    # z = x0, y[3a+b] = x[1 + 3a + b], w = x10..x15 idle
    F = defaultdict(int)
    for perm in itertools.permutations(range(3)):
        e = [0] * NV
        e[0] += 1
        for a in range(3):
            e[1 + 3 * a + perm[a]] += 1
        F[tuple(e)] += 1
    return dict(F)

def poly_random(seed):
    rng = random.Random(seed)
    F = {}
    for e in monomials(NV, 4):
        F[e] = rng.randint(-3, 3)
    return F

def partial(F, i):
    G = defaultdict(int)
    for e, cf in F.items():
        if e[i] > 0:
            e2 = list(e); e2[i] -= 1
            G[tuple(e2)] += cf * e[i]
    return dict(G)

def macaulay_rank_modp(F, k):
    cols = {e: t for t, e in enumerate(monomials(NV, k))}
    parts = [partial(F, i) for i in range(NV)]
    mons = list(monomials(NV, k - 3))
    nrows = NV * len(mons)
    entries = [0] * (nrows * len(cols))
    ncol = len(cols)
    r = 0
    for i in range(NV):
        for m in mons:
            base = r * ncol
            for e, cf in parts[i].items():
                e2 = tuple(a + b for a, b in zip(e, m))
                entries[base + cols[e2]] = (entries[base + cols[e2]] + cf) % P
            r += 1
    M = flint.nmod_mat(nrows, ncol, entries, P)
    return M.rank(), (nrows, ncol)

Fdet, Fpad = poly_det4(), poly_zper3()
Frand = poly_random(20260917)
mac = {}
for k in (3, 4):
    for name, F in (('det4', Fdet), ('zper3', Fpad), ('random', Frand)):
        rk, shape = macaulay_rank_modp(F, k)
        mac[f'{name}_k{k}'] = {'rank_mod_p': rk, 'shape': shape}
        print(f'M_{k}({name}) rank mod p = {rk} shape {shape} t={time.perf_counter()-T0:.1f}s', flush=True)
res['macaulay_ranks_mod_p'] = mac
res['checks'].append({'name': 'M_3: det4 16, zper3 10 (mod p, lower bounds; formulas give 16, 10)', 'pass': mac['det4_k3']['rank_mod_p'] == 16 and mac['zper3_k3']['rank_mod_p'] == 10})
res['checks'].append({'name': 'M_4: det4 226, zper3 155 (mod p, lower bounds; formulas (A1),(A2) give 226, 155)', 'pass': mac['det4_k4']['rank_mod_p'] == r_det(4) and mac['zper3_k4']['rank_mod_p'] == r_pad(4), 'formula': [r_det(4), r_pad(4)]})
res['checks'].append({'name': 'random quartic attains the generic maxima 16, 256 (control)', 'pass': mac['random_k3']['rank_mod_p'] == 16 and mac['random_k4']['rank_mod_p'] == 256})

# ---------- (d) second Koszul differential D_k, k = 6, 7 ----------
def koszul2_rows(F, k):
    """Sparse rows of D_k : Lambda^2 C^16 (x) S_{k-6} -> C^16 (x) S_{k-3}; row = dict column->value."""
    parts = [partial(F, i) for i in range(NV)]
    colmons = {e: t for t, e in enumerate(monomials(NV, k - 3))}
    ncm = len(colmons)
    rowmons = list(monomials(NV, k - 6))
    rows = []
    for (i, j) in itertools.combinations(range(NV), 2):
        for m in rowmons:
            row = defaultdict(int)
            for e, cf in parts[i].items():   # + m d_i F  e_j
                row[j * ncm + colmons[tuple(a + b for a, b in zip(e, m))]] += cf
            for e, cf in parts[j].items():   # - m d_j F  e_i
                row[i * ncm + colmons[tuple(a + b for a, b in zip(e, m))]] -= cf
            rows.append({c: v % P for c, v in row.items() if v % P})
    return rows, NV * ncm

def koszul2_rank_exact_modp(F, k):
    rows, ncol = koszul2_rows(F, k)
    entries = [0] * (len(rows) * ncol)
    for r, row in enumerate(rows):
        base = r * ncol
        for c, v in row.items():
            entries[base + c] = v
    return flint.nmod_mat(len(rows), ncol, entries, P).rank(), (len(rows), ncol), 'exact mod p'

def koszul2_rank_gram_modp(F, k):
    """rank(D D^T) mod p <= rank(D) mod p <= rank(D) over Q; equality with the row count certifies full row rank."""
    rows, ncol = koszul2_rows(F, k)
    n = len(rows)
    bycol = defaultdict(list)
    for r, row in enumerate(rows):
        for c, v in row.items():
            bycol[c].append((r, v))
    gram = [[0] * n for _ in range(n)]
    for c, lst in bycol.items():
        for a in range(len(lst)):
            ra, va = lst[a]
            for b in range(a, len(lst)):
                rb, vb = lst[b]
                gram[ra][rb] += va * vb
    entries = [0] * (n * n)
    for a in range(n):
        for b in range(a, n):
            v = gram[a][b] % P
            entries[a * n + b] = v
            entries[b * n + a] = v
    return flint.nmod_mat(n, n, entries, P).rank(), (n, ncol), 'lower bound (Gram matrix mod p)'

def poly_random_sparse(seed, nterms):
    rng = random.Random(seed)
    allm = list(monomials(NV, 4))
    F = {}
    for e in rng.sample(allm, nterms):
        F[e] = rng.randint(-3, 3) or 1
    return F

Fsparse = poly_random_sparse(20260918, 300)
kos = {}
for name, F in (('det4', Fdet), ('zper3', Fpad), ('random', Frand)):
    rk, shape, kind = koszul2_rank_exact_modp(F, 6)
    kos[f'{name}_k6'] = {'rank': rk, 'shape': shape, 'kind': kind}
    print(f'D_6({name}) rank = {rk} {shape} {kind} t={time.perf_counter()-T0:.1f}s', flush=True)
for name, F in (('det4', Fdet), ('zper3', Fpad), ('random_sparse300', Fsparse)):
    rk, shape, kind = koszul2_rank_gram_modp(F, 7)
    kos[f'{name}_k7'] = {'rank': rk, 'shape': shape, 'kind': kind}
    print(f'D_7({name}) rank >= {rk} {shape} {kind} t={time.perf_counter()-T0:.1f}s', flush=True)
res['koszul2_ranks'] = kos
res['checks'].append({'name': 'D_6, D_7 full row rank at det4 (then no determinant equation from the second differential in degrees 6, 7)', 'pass': kos['det4_k6']['rank'] == 120 and kos['det4_k7']['rank'] == 1920, 'value': [kos['det4_k6']['rank'], kos['det4_k7']['rank']]})
res['wall_seconds'] = time.perf_counter() - T0
res['all_checks_pass'] = all(c['pass'] for c in res['checks'])
with open(OUT, 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({c['name']: c['pass'] for c in res['checks']}, indent=1))
print('ALL PASS' if res['all_checks_pass'] else 'SOME CHECK FAILED', f'{res["wall_seconds"]:.1f}s')
