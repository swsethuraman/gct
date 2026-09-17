"""B20-02 pilot: exact Koszul homology profile of quinary quartics (N = 5).

For each point F and internal grading k, the rank of every Koszul differential
d_j^{(k)} : K_j(k) = Lambda^j C^5 (x) S_{k-3j}  ->  K_{j-1}(k),   d_j(e_I (x) m) = sum_t (-1)^t f_{i_t} m e_{I \\ i_t},
f_i = d_i F, and the derived dim H_j(F)_k = dim K_j(k) - rank d_j - rank d_{j+1}.
Generic ranks rho_j(k) = sum_{i>=j} (-1)^{i-j} dim K_i(k) (report Lemma 6.1).

Ranks: exact over Q (flint.fmpz_mat.rank) when rows*cols <= EXACT_LIMIT, else modulo two
large primes (flint.nmod_mat.rank), reported as floors on the rational rank (safe direction).

Usage: b20_02_koszul5.py --kmin 3 --kmax 10 --points det_P2,det_own,prod,padpt,smooth --out <json>
"""
import argparse, hashlib, itertools, json, math, os, random, sys, time
from collections import defaultdict
import flint

T0 = time.perf_counter()
NV = 5
PRIMES = (2147483647, 4294967291)  # 2^31 - 1 and the largest prime below 2^32
SEED_OWN = 2026091702

ap = argparse.ArgumentParser()
ap.add_argument('--kmin', type=int, default=3)
ap.add_argument('--kmax', type=int, default=10)
ap.add_argument('--points', default='det_P2,det_own,prod,padpt,smooth')
ap.add_argument('--exact-limit', type=int, default=320_000)
ap.add_argument('--n-primes', type=int, default=1, help='number of primes for modular floors (1 or 2)')
ap.add_argument('--kmax-nondet', type=int, default=None, help='kmax for points other than det_P2 (default: kmax)')
ap.add_argument('--out', required=True)
ap.add_argument('--p2', default=os.path.join('results', 'b20_02', 'inputs', 'p2_quinary_macaulay.json'))
args = ap.parse_args()
EXACT_LIMIT = args.exact_limit
PRIMES = PRIMES[:max(1, min(2, args.n_primes))]
DEADLINE = float(os.environ.get('CI73_DEADLINE', '0') or 0)
NEED_SECONDS = {9: 4.0, 10: 8.0, 11: 16.0, 12: 34.0}
def seconds_left():
    return (DEADLINE - time.monotonic()) if DEADLINE else 1e9

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()

# ---------------- pinned input ----------------
P2_EXPECTED = '05272bfc0b0be15c4c870637ab3f371d79be53bf044f9fbe4c15a704c40c193e'
p2_hash = sha256(args.p2)
if p2_hash != P2_EXPECTED:
    print('PIN MISMATCH for', args.p2, p2_hash, file=sys.stderr)
    sys.exit(3)
with open(args.p2) as fh:
    P2 = json.load(fh)

res = {'script': 'analysis/b20_02_koszul5.py', 'argv': sys.argv[1:], 'NV': NV,
       'inputs_sha256': {args.p2.replace('\\', '/'): p2_hash},
       'primes': list(PRIMES), 'exact_limit_entries': EXACT_LIMIT, 'seed_own': SEED_OWN,
       'deadline_guard_seconds_needed': NEED_SECONDS, 'skipped_rows_deadline': [],
       'flint_version': flint.__version__, 'python': sys.version.split()[0], 'checks': []}

# ---------------- polynomial helpers (exponent-tuple dicts, integer coefficients) ----------------
def monomials(nvars, deg):
    if deg < 0:
        return
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

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

def linear(coeffs):
    out = {}
    for i, c in enumerate(coeffs):
        if c:
            e = [0] * NV; e[i] = 1
            out[tuple(e)] = c
    return out

def det_of_pencil(As):
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
    F = {}
    for perm in itertools.permutations(range(3)):
        term = {tuple([0] * NV): 1}
        for r in range(3):
            term = pmul(term, rows[r][perm[r]])
        F = padd(F, term)
    return F

def partial(F, i):
    G = defaultdict(int)
    for e, cf in F.items():
        if e[i] > 0:
            e2 = list(e); e2[i] -= 1
            G[tuple(e2)] += cf * e[i]
    return dict(G)

def dimS(m):
    return math.comb(m + NV - 1, NV - 1) if m >= 0 else 0

def dimK(j, k):
    return math.comb(NV, j) * dimS(k - 3 * j)

def rho(j, k):
    return sum((-1) ** (i - j) * dimK(i, k) for i in range(j, NV + 1))

# ---------------- points ----------------
rng = random.Random(SEED_OWN)
points = {}
A_p2 = P2['pencil_A']
points['det_P2'] = det_of_pencil(A_p2)
A_own = [[[rng.randint(-5, 5) for _ in range(4)] for _ in range(4)] for _ in range(NV)]
points['det_own'] = det_of_pencil(A_own)
ell = linear(P2['ell'])
C_cubic = {e: rng.randint(-4, 4) for e in monomials(NV, 3)}
C_cubic = {e: v for e, v in C_cubic.items() if v}
points['prod'] = pmul(ell, C_cubic)
T = P2['L']  # the 9 x 5 integer matrix of the P2 padding point; called T in the report (G13)
rows = [[linear(T[3 * a + b]) for b in range(3)] for a in range(3)]
points['padpt'] = pmul(linear([1, 0, 0, 0, 0]), per3_of_forms(rows))
F_smooth = {e: rng.randint(-4, 4) for e in monomials(NV, 4)}
points['smooth'] = {e: v for e, v in F_smooth.items() if v}
res['points_definition'] = {
    'det_P2': {'pencil_A': A_p2, 'source': 'P2 pencil_A (pinned)'},
    'det_own': {'pencil_A': A_own, 'source': 'random.Random(%d), first draws' % SEED_OWN},
    'prod': {'ell': P2['ell'], 'C_cubic': [[list(e), v] for e, v in sorted(C_cubic.items())]},
    'padpt': {'x1_times_per3_of_T_x': True, 'T_9x5': T, 'source': 'P2 L (pinned), called T here'},
    'smooth': {'F': [[list(e), v] for e, v in sorted(points['smooth'].items())]},
}
res['n_terms'] = {name: len(F) for name, F in points.items()}
res['checks'].append({'name': 'det_P2 has all 70 monomials', 'pass': len(points['det_P2']) == 70})
res['checks'].append({'name': 'det_own has all 70 monomials', 'pass': len(points['det_own']) == 70})

# ---------------- Koszul differentials ----------------
def koszul_matrix(parts, j, k):
    """Matrix of d_j^{(k)}: rows = basis of K_j(k), cols = basis of K_{j-1}(k). Returns (rows, cols, entries)."""
    subsets_j = list(itertools.combinations(range(NV), j))
    subsets_jm1 = list(itertools.combinations(range(NV), j - 1))
    mons_src = list(monomials(NV, k - 3 * j))
    mons_tgt = list(monomials(NV, k - 3 * (j - 1)))
    if not mons_src:
        return 0, len(subsets_jm1) * len(mons_tgt), {}
    col_of = {}
    for a, I in enumerate(subsets_jm1):
        for b, m in enumerate(mons_tgt):
            col_of[(I, m)] = a * len(mons_tgt) + b
    entries = defaultdict(int)
    r = 0
    for I in subsets_j:
        for m in mons_src:
            for t, i in enumerate(I):
                sgn = -1 if t % 2 else 1
                Irem = I[:t] + I[t + 1:]
                for e, cf in parts[i].items():
                    mm = tuple(a + b for a, b in zip(e, m))
                    entries[(r, col_of[(Irem, mm)])] += sgn * cf
            r += 1
    return len(subsets_j) * len(mons_src), len(subsets_jm1) * len(mons_tgt), {kk: v for kk, v in entries.items() if v}

def rank_of(nrows, ncols, entries):
    if nrows == 0 or ncols == 0:
        return {'rank': 0, 'method': 'empty'}
    if nrows * ncols <= EXACT_LIMIT:
        M = flint.fmpz_mat(nrows, ncols)
        for (r, c), v in entries.items():
            M[r, c] = v
        return {'rank': M.rank(), 'method': 'exact_Q_fmpz'}
    ranks = []
    for p in PRIMES:
        M = flint.nmod_mat(nrows, ncols, p)
        for (r, c), v in entries.items():
            M[r, c] = v % p
        ranks.append(M.rank())
    return {'rank': max(ranks), 'rank_mod_p': ranks, 'method': 'floor_mod_p'}

# ---------------- main loop ----------------
table = {}
for name in args.points.split(','):
    F = points[name]
    parts = [partial(F, i) for i in range(NV)]
    table[name] = {}
    kmax_here = args.kmax if (name == 'det_P2' or args.kmax_nondet is None) else args.kmax_nondet
    for k in range(args.kmin, kmax_here + 1):
        if seconds_left() < NEED_SECONDS.get(k, 2.0) + 3.0:
            res['skipped_rows_deadline'].append([name, k, round(seconds_left(), 1)])
            print('SKIP (deadline guard)', name, k, f'left={seconds_left():.1f}s', flush=True)
            continue
        row = {'k': k, 'dimK': [dimK(j, k) for j in range(NV + 1)], 'rho': [None] + [rho(j, k) for j in range(1, NV + 1)]}
        ranks = {}
        for j in range(1, NV + 1):
            if dimK(j, k) == 0:
                ranks[j] = {'rank': 0, 'method': 'zero_space'}
                continue
            nr, nc, ent = koszul_matrix(parts, j, k)
            info = rank_of(nr, nc, ent)
            info['shape'] = [nr, nc]
            info['nnz'] = len(ent)
            ranks[j] = info
        row['rank'] = {j: ranks[j]['rank'] for j in ranks}
        row['method'] = {j: ranks[j]['method'] for j in ranks}
        row['shape'] = {j: ranks[j].get('shape') for j in ranks}
        row['rank_mod_p'] = {j: ranks[j].get('rank_mod_p') for j in ranks if 'rank_mod_p' in ranks[j]}
        # dim H_j = dim K_j - rank d_j - rank d_{j+1}; rank d_0 = 0, rank d_6 = 0
        rk = {0: 0, NV + 1: 0}
        rk.update(row['rank'])
        row['dimH'] = [dimK(j, k) - rk[j] - rk[j + 1] for j in range(NV + 1)]
        row['rank_minus_rho'] = {j: row['rank'][j] - rho(j, k) for j in row['rank']}
        row['all_modular'] = any(v == 'floor_mod_p' for v in row['method'].values())
        table[name][k] = row
        res['table'] = table
        with open(args.out, 'w') as fh:
            json.dump(res, fh, indent=1)
        print(name, k, 'rank', row['rank'], 'rho', row['rho'][1:], 'dimH', row['dimH'], f't={time.perf_counter()-T0:.1f}s', flush=True)
res['table'] = table

# ---------------- checks (emitted, not typed: G16) ----------------
def all_k(name, pred):
    return all(pred(table[name][k]) for k in table[name])

for name in table:
    res['checks'].append({'name': f'{name}: no rank exceeds rho_j(k) for any j, k (Lemma 6.1 sanity)',
                          'pass': all_k(name, lambda r: all(v <= 0 for v in r['rank_minus_rho'].values()))})
for name in ('det_P2', 'det_own'):
    if name in table:
        res['checks'].append({'name': f'{name}: rank d_j = rho_j(k) for all j >= 2 and all k computed (Theorem 6.4 certificate)',
                              'pass': all_k(name, lambda r: all(r['rank_minus_rho'][j] == 0 for j in r['rank_minus_rho'] if j >= 2))})
        res['checks'].append({'name': f'{name}: dim H_j = 0 for all j >= 2 and all k computed',
                              'pass': all_k(name, lambda r: all(h == 0 for h in r['dimH'][2:]))})
        res['checks'].append({'name': f'{name}: gradings with exact-Q ranks for every j (unconditional certificate)',
                              'value': sorted(k for k in table[name] if not table[name][k]['all_modular'])})
        res['checks'].append({'name': f'{name}: gradings where only modular floors were used (floor = rho still certifies, Lemma 6.1)',
                              'value': sorted(k for k in table[name] if table[name][k]['all_modular'])})
if 'det_P2' in table:
    prof = {k: table['det_P2'][k]['rank'][1] for k in table['det_P2']}
    expected = {3: 5, 4: 25, 5: 75, 6: 165, 7: 299, 8: 475, 9: 695}
    res['checks'].append({'name': 'det_P2: rank d_1 matches the P2 certificate profile at the k in common (consistency with the pinned input)',
                          'pass': all(prof[k] == expected[k] for k in prof if k in expected), 'value': prof})
if 'smooth' in table:
    res['checks'].append({'name': 'smooth control attains rho_j(k) for every j >= 1 and every k (control that can fail)',
                          'pass': all_k('smooth', lambda r: all(v == 0 for v in r['rank_minus_rho'].values()))})
for name in ('prod', 'padpt'):
    if name in table:
        res['checks'].append({'name': f'{name}: gradings with rank d_2 < rho_2(k) (padding side strictly below the determinant maximum; modular values are floors)',
                              'value': sorted(k for k in table[name] if table[name][k]['rank_minus_rho'].get(2, 0) < 0)})
        res['checks'].append({'name': f'{name}: gradings with dim H_2 > 0 (exact where method is exact_Q_fmpz)',
                              'value': sorted(k for k in table[name] if table[name][k]['dimH'][2] > 0)})
        res['checks'].append({'name': f'{name}: gradings with dim H_3 > 0',
                              'value': sorted(k for k in table[name] if table[name][k]['dimH'][3] > 0)})

def _peak_memory():
    try:
        import ctypes as C
        from ctypes import wintypes as W
        class Counters(C.Structure):
            _fields_ = [("cb", W.DWORD), ("faults", W.DWORD)] + [(n, C.c_size_t) for n in ("peak_working_set", "working_set", "peak_paged_pool", "paged_pool", "peak_nonpaged_pool", "nonpaged_pool", "pagefile", "peak_pagefile")]
        v = Counters(); v.cb = C.sizeof(v)
        k = C.windll.kernel32; k.GetCurrentProcess.restype = W.HANDLE
        ps = C.windll.psapi; ps.GetProcessMemoryInfo.argtypes = [W.HANDLE, C.c_void_p, W.DWORD]
        ps.GetProcessMemoryInfo(k.GetCurrentProcess(), C.byref(v), v.cb)
        return {'peak_working_set': v.peak_working_set, 'peak_pagefile': v.peak_pagefile}
    except Exception as exc:  # pragma: no cover
        return {'error': repr(exc)}
res['process_peak_memory'] = _peak_memory()
res['wall_seconds'] = time.perf_counter() - T0
res['all_checks_pass'] = all(c['pass'] for c in res['checks'] if 'pass' in c)
n_pass = sum(1 for c in res['checks'] if c.get('pass') is True)
n_total = sum(1 for c in res['checks'] if 'pass' in c)
res['checks_passed_over_total'] = [n_pass, n_total]
os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
with open(args.out, 'w') as fh:
    json.dump(res, fh, indent=1)
for c in res['checks']:
    print(('PASS' if c.get('pass') else ('FAIL' if 'pass' in c else 'INFO')), c['name'], c.get('value', ''))
print(f'checks passed {n_pass}/{n_total}', flush=True)
print('peak memory', res['process_peak_memory'])
print('ALL PASS' if res['all_checks_pass'] else 'SOME CHECK FAILED', f'{res["wall_seconds"]:.1f}s')
