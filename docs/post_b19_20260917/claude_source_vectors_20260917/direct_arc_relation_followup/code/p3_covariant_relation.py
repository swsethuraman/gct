"""Pilot 3: exact two-column covariant analysis of q3, q7, n02 and the kernel vector of C on U.

Objects. A same-pairing paired contraction factors as P_{pi,rho} = B(X_{H1}, X_{H2}) where X_H is the partial
contraction of two column tensors with the four epsilon blocks internal to one column pair (free legs: a-legs of
the two pi-leftover slots, b-legs of the two rho-leftover slots), and B(X,X') = sum eps[a1..a4] eps[b1..b4]
X[a1,a2,b1,b2] X'[a3,a4,b3,b4].  q = P_{pi,rho} + P_{rho,pi} = B(X_H1,X_H2) + B(X_H1t,X_H2t) (t = pi/rho swapped).
Every X_H is a quadratic GL x GL covariant of the 5-wedge (an element of the 4-dimensional space Cov, pilot 1).
Top parts: the skew-degree-6 part of X_H at Y equals X_H at the point Y* = (nu1, nu2, nu3, Z1, Z2) of the locus S*
(REPORT.md B.2), so the tops are the covariants restricted to S*.  On the slice cone(V) chosen in
results/slice_choice.json (transversal to the 18-dimensional group G' = L~ x| U_-, tangent rank 23), a linear relation
among restricted covariants holds identically on S* iff it holds at the 50 poised slice points (exact integers).

Stages (JSON saved after each):
 A. Y0 = sealed P6 point 0: X_H for the 12 halves and extra patterns, three primes, CRT (bound 331776*(120*3^5)^2);
    factorization control against the sealed values q3(Y0)=260975, q7(Y0)=301718, n02(Y0)=386346 (mod P);
    exact rank of the patterns (= dim Cov = 4 expected), basis choice, exact coordinates of every half.
 B. Slice: the 4 basis covariants at the 50 poised points of S*, two primes, CRT (bound 331776*(120*2*2)^2);
    exact rank r_top of the 4 restricted covariants; all patterns at slice point 0 (ell ratios, consistency).
 C. If r_top = 1: exact ell(H) for the halves, exact K-vectors K(q) = sum ell(H)X_H' + ell(H')X_H over the two
    orientations, exact rank of {K3, K7, Kn}; if 2, the exact rational kernel vector (alpha*, beta*), its reduction
    mod P against the recorded residues, transverse values on n* from the recorded integer rows, controls.
Deadline 55 s (wrapper 60 s)."""
import hashlib, itertools, json, sys, time, types
from fractions import Fraction
from pathlib import Path
HERE = Path(__file__).resolve().parent; SESSION = HERE.parent; ROOT = SESSION.parents[2]
PILOTS_HIST = ROOT / 'work/descent_followup_claude_20260916/pilots'
sys.path.insert(0, str(PILOTS_HIST))
import paired_runner as pr
import numpy as np
from sympy import isprime
T0 = time.perf_counter(); DEADLINE = 55.0
SMOKE = (len(sys.argv) > 2 and sys.argv[2] == '--smoke')
OUT = SESSION / ('results/p3_covariant_relation.json' if not SMOKE else 'results/_smoke_p3.json')
P = 524287
rec = dict(pilot='p3_covariant_relation', prime_P=P, stages={}, checks={}, log=[])
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(stage):
    rec['stages'][stage] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1, default=str) + '\n'); print('stage', stage, round(rec['stages'][stage], 2), flush=True)
def left(): return DEADLINE - (time.perf_counter() - T0)

# ---------------------------------------------------------------- carrier module copies for other primes
CARRIER_SRC = pr.SRC.read_text()
def carrier_for(p):
    if p == P: return pr.c
    src = CARRIER_SRC.replace('P = 524287  # 2**19 - 1, Mersenne prime', 'P = %d' % p)
    assert 'P = %d' % p in src
    mod = types.ModuleType('carrier_%d' % p); mod.__file__ = str(pr.SRC)
    exec(compile(src, str(pr.SRC), 'exec'), mod.__dict__)
    assert mod.P == p and 4 ** 12 * p * p < 2 ** 63
    return mod
def primes_below(x, n):
    out = []; q = x - 1
    while len(out) < n:
        if isprime(q): out.append(q)
        q -= 1
    return out
EXTRA_PRIMES = primes_below(600000, 2)          # < 600000 so that balanced-residue float64 dot products of 4^8 terms stay below 2^53
PRIMES3 = [P] + EXTRA_PRIMES; PRIMES2 = [P, EXTRA_PRIMES[0]]
MODS = {p: carrier_for(p) for p in PRIMES3}
rec['primes'] = dict(P=P, extra=EXTRA_PRIMES)

# ---------------------------------------------------------------- CRT
def crt(residues, primes):
    M = 1
    for p in primes: M *= p
    x = 0
    for r, p in zip(residues, primes):
        Mi = M // p; x += r * Mi * pow(Mi, -1, p)
    x %= M
    return x - M if x > M // 2 else x
def crt_vec(res_by_prime, primes, bound):
    M = 1
    for p in primes: M *= p
    assert M > 2 * bound, (M, bound)
    return [crt([int(res_by_prime[p][k]) for p in primes], primes) for k in range(len(res_by_prime[primes[0]]))]

# ---------------------------------------------------------------- exact column tensor (int64, no modulus)
def exact_column_tensor(Y):
    """D[c_1..c_5] = det[(Y_i)_{c_k}] as exact int64 (|D| <= 5! * max|entry|^5 < 2^63 for the points used)."""
    mats = [np.asarray(Y[i], dtype=np.int64).reshape(16) for i in range(5)]
    memo = {}
    def D(rows):
        if rows in memo: return memo[rows]
        if len(rows) == 1:
            memo[rows] = mats[rows[0]].copy(); return memo[rows]
        acc = np.zeros((16,) * len(rows), dtype=np.int64)
        for idx, i in enumerate(rows):
            term = np.multiply.outer(mats[i], D(rows[:idx] + rows[idx + 1:]))
            acc = acc + term if idx % 2 == 0 else acc - term
        memo[rows] = acc; return acc
    return D((0, 1, 2, 3, 4))
def balanced(a, p):
    r = np.mod(a, p); r = np.where(r > p // 2, r - p, r); return r
EPS_SIGNED = ((pr.c.EPS4 + P // 2) % P) - P // 2          # +-1 entries
EPS_F = EPS_SIGNED.astype(np.float64)
# ---------------------------------------------------------------- two-column partial contraction (float64 BLAS, exact)
def half_tensor(mod, T, H):
    """X_H[a_x5, a_y5, b_x5', b_y5'] (256 entries, mod mod.P) from the EXACT int64 column tensor T (16^5) and half
    structure H = dict(pi=[blkA, blkB], rho=[blkA, blkB], pi_free=(x5, y5), rho_free=(x5p, y5p)); slots are (col, pos).
    Arithmetic: balanced residues |x| <= p/2 < 3e5 in float64; each tensordot sums at most 4^8 products, so every
    partial sum is below 4^8 * (3e5)^2 < 2^53 and is exact; residues are re-balanced after every step."""
    p = mod.P
    arr = balanced(T % p, p).astype(np.float64).reshape((4, 4) * 5)
    cols = sorted({s[0] for blk in H['pi'] + H['rho'] for s in blk} | {s[0] for s in H['pi_free']} | {s[0] for s in H['rho_free']})
    assert len(cols) == 2, cols
    X, Y = cols
    def labels(j):
        lab = []
        for k in range(5): lab += [('a', (j, k)), ('b', (j, k))]
        return lab
    maxint = [0]
    def contract(t1, l1, t2, l2):
        shared = [x for x in l1 if x in set(l2)]
        assert len(shared) <= 8
        ax1 = [l1.index(x) for x in shared]; ax2 = [l2.index(x) for x in shared]
        res = np.tensordot(t1, t2, axes=(ax1, ax2))
        res = balanced(res, p)
        lab = [x for x in l1 if x not in shared] + [x for x in l2 if x not in shared]
        maxint[0] = max(maxint[0], res.size)
        return res, lab
    cur = (arr, labels(X))
    for blk in H['pi']: cur = contract(cur[0], cur[1], EPS_F, [('a', s) for s in blk])
    for blk in H['rho']: cur = contract(cur[0], cur[1], EPS_F, [('b', s) for s in blk])
    cur = contract(cur[0], cur[1], arr, labels(Y))
    val, lab = cur
    val = np.mod(np.rint(val), p).astype(np.int64)
    want = [('a', H['pi_free'][0]), ('a', H['pi_free'][1]), ('b', H['rho_free'][0]), ('b', H['rho_free'][1])]
    assert sorted(lab) == sorted(want), (lab, want)
    perm = [lab.index(w) for w in want]
    return np.transpose(val, perm).reshape(256) % mod.P, maxint[0]
def B_pair(mod, X1, X2):
    """sum eps[a1,a2,a3,a4] eps[b1,b2,b3,b4] X1[a1,a2,b1,b2] X2[a3,a4,b3,b4] mod mod.P"""
    p = mod.P; E = ((mod.EPS4 + p // 2) % p) - p // 2            # signed Levi-Civita (+-1), avoids int64 overflow
    x1 = (X1 % p).reshape(4, 4, 4, 4).astype(np.int64); x2 = (X2 % p).reshape(4, 4, 4, 4).astype(np.int64)
    r = np.einsum('ijkl,mnop,ijmn,klop->', E, E, x1, x2, optimize=True)   # |terms| <= 576 * p^2 < 2^63
    return int(r) % p

# ---------------------------------------------------------------- source definitions and halves
p6 = json.loads((PILOTS_HIST / 'p6_basis.json').read_text())
n02d = json.loads((SESSION.parent / 'routeA_signfilter_20260917/certificates/n02_definition.json').read_text())
rec['inputs_sha256'] = {'p6_basis.json': sha(PILOTS_HIST / 'p6_basis.json'), 'n02_definition.json': sha(SESSION.parent / 'routeA_signfilter_20260917/certificates/n02_definition.json'),
                        'b18_02_carrier.py': sha(pr.SRC), 'paired_runner.py': sha(PILOTS_HIST / 'paired_runner.py'), 'slice_choice.json': sha(SESSION / 'results/slice_choice.json')}
def tup(blocks): return [tuple(tuple(s) for s in b) for b in blocks]
VEC = {}
for b in p6['basis']:
    VEC['q%d' % b['index']] = dict(pi=tup(b['pi']), rho=tup(b['rho']), pairing=tuple(tuple(x) for x in b['pairing']))
VEC['n02'] = dict(pi=tup(n02d['pi_ordered_blocks']), rho=tup(n02d['rho_ordered_blocks']), pairing=tuple(tuple(x) for x in n02d['pairing']))
SEALED_Y0 = {'q3': p6['basis_matrix_pair_by_point'][0][0], 'q7': p6['basis_matrix_pair_by_point'][1][0], 'n02': n02d['values']['P6_points_0_to_4'][0]}
def halves(v):
    pi, rho, pairing = v['pi'], v['rho'], v['pairing']
    out = {}
    for h, (X, Y) in enumerate(pairing):
        for blk in pi[2 * h:2 * h + 2] + rho[2 * h:2 * h + 2]: assert {s[0] for s in blk} == {X, Y}, (blk, X, Y)
        pf = (pi[4][2 * h], pi[4][2 * h + 1]); rf = (rho[4][2 * h], rho[4][2 * h + 1])
        assert {pf[0][0], pf[1][0]} == {X, Y} and {rf[0][0], rf[1][0]} == {X, Y}
        out['h%d' % (h + 1)] = dict(pi=pi[2 * h:2 * h + 2], rho=rho[2 * h:2 * h + 2], pi_free=pf, rho_free=rf)
        out['h%dt' % (h + 1)] = dict(pi=rho[2 * h:2 * h + 2], rho=pi[2 * h:2 * h + 2], pi_free=rf, rho_free=pf)
    return out
HALVES = {}
for name, v in VEC.items():
    for hn, H in halves(v).items(): HALVES[name + '_' + hn] = H
rng = np.random.default_rng(20260918)
EXTRA = {}
for n in range(6):
    px = [int(x) for x in rng.permutation(5)]; qx = [int(x) for x in rng.permutation(5)]
    pi = [((0, px[0]), (0, px[1]), (1, qx[0]), (1, qx[1])), ((0, px[2]), (0, px[3]), (1, qx[2]), (1, qx[3]))]; pf = ((0, px[4]), (1, qx[4]))
    px = [int(x) for x in rng.permutation(5)]; qx = [int(x) for x in rng.permutation(5)]
    rho = [((0, px[0]), (0, px[1]), (1, qx[0]), (1, qx[1])), ((0, px[2]), (0, px[3]), (1, qx[2]), (1, qx[3]))]; rf = ((0, px[4]), (1, qx[4]))
    EXTRA['x%d' % n] = dict(pi=pi, rho=rho, pi_free=pf, rho_free=rf)
PATTERNS = dict(HALVES); PATTERNS.update(EXTRA)
rec['patterns'] = {k: dict(pi=[[list(s) for s in b] for b in v['pi']], rho=[[list(s) for s in b] for b in v['rho']], pi_free=[list(s) for s in v['pi_free']], rho_free=[list(s) for s in v['rho_free']]) for k, v in PATTERNS.items()}
NAMES = list(PATTERNS)

# ---------------------------------------------------------------- exact linear algebra over Q
def rank_Q(rows):
    M = [[Fraction(x) for x in r] for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]; inv = 1 / M[rk][c]; M[rk] = [x * inv for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
        if rk == len(M): break
    return rk
def solve_coords(basis_vecs, target):
    """exact coordinates x with target = sum x_i basis_i (all long vectors); returns None if inconsistent."""
    n = len(basis_vecs); m = len(target)
    A = [[Fraction(basis_vecs[i][k]) for i in range(n)] + [Fraction(target[k])] for k in range(m)]
    rk = 0; pivcols = []
    for c in range(n):
        piv = next((i for i in range(rk, m) if A[i][c] != 0), None)
        if piv is None: continue
        A[rk], A[piv] = A[piv], A[rk]; inv = 1 / A[rk][c]; A[rk] = [x * inv for x in A[rk]]
        for i in range(m):
            if i != rk and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f * y for x, y in zip(A[i], A[rk])]
        pivcols.append(c); rk += 1
    if rk < n: return None
    if any(A[i][n] != 0 for i in range(rk, m)): return None
    return [A[i][n] for i in range(n)]
def frac_str(x): return '%d/%d' % (x.numerator, x.denominator)
def frac_mod(x, p): return (x.numerator % p) * pow(x.denominator % p, -1, p) % p

# ================================================================ Stage A: Y0
Y0 = np.array(p6['points_entries'][0], dtype=np.int64)
BOUND_Y0 = 331776 * (120 * 3 ** 5) ** 2
primesA = [P] if SMOKE else PRIMES3
valsA = {p: {} for p in primesA}; maxint = 0
T0exact = exact_column_tensor(Y0)
for p in primesA:
    mod = MODS[p]; T = T0exact
    for nm in NAMES:
        valsA[p][nm], mi = half_tensor(mod, T, PATTERNS[nm]); maxint = max(maxint, mi)
rec['max_intermediate_entries'] = int(maxint)
# factorization control mod P
fact = {}
for name in VEC:
    h = {k.split('_')[1]: valsA[P][k] for k in NAMES if k.startswith(name + '_')}
    v = (B_pair(pr.c, h['h1'], h['h2']) + B_pair(pr.c, h['h1t'], h['h2t'])) % P
    fact[name] = dict(recomputed_from_halves=v, sealed=SEALED_Y0[name], passed=(v == SEALED_Y0[name]))
rec['checks']['factorization_at_Y0'] = fact
save('A_values')
if SMOKE:
    # independent int64 path (sealed contract_pair, einsum mod P) for two halves
    net = pr.c.Net(); Tm = pr.c.column_tensor(Y0 % P, 5); arr = Tm.reshape((4, 4) * 5)
    def lab(j): return [x for k in range(5) for x in (('a', (j, k)), ('b', (j, k)))]
    agree = {}
    for nm in NAMES[:3]:
        H = PATTERNS[nm]; cols = sorted({s_[0] for blk in H['pi'] + H['rho'] for s_ in blk}); Xc, Yc = cols
        cur = (arr, lab(Xc))
        for blk in H['pi']: cur = net.contract_pair(cur, (pr.c.EPS4, [('a', s_) for s_ in blk]))
        for blk in H['rho']: cur = net.contract_pair(cur, (pr.c.EPS4, [('b', s_) for s_ in blk]))
        cur = net.contract_pair(cur, (arr, lab(Yc))); val, lb = cur
        want = [('a', H['pi_free'][0]), ('a', H['pi_free'][1]), ('b', H['rho_free'][0]), ('b', H['rho_free'][1])]
        v2 = np.transpose(val, [lb.index(w) for w in want]).reshape(256) % P
        agree[nm] = bool(np.array_equal(v2, valsA[P][nm]))
    print(json.dumps(dict(factorization=fact, float_vs_int64_paths_agree=agree))); sys.exit(0)
XA = {nm: crt_vec({p: valsA[p][nm] for p in PRIMES3}, PRIMES3, BOUND_Y0) for nm in NAMES}
rec['checks']['crt_bound_Y0'] = dict(bound=BOUND_Y0, modulus=PRIMES3[0] * PRIMES3[1] * PRIMES3[2])
half_names = [n for n in NAMES if n in HALVES]
rec['rank_Q_at_Y0'] = dict(halves=rank_Q([XA[n] for n in half_names]), all_patterns=rank_Q([XA[n] for n in NAMES]))
# basis: greedy over halves then extras
basis = []
for nm in half_names + [n for n in NAMES if n not in HALVES]:
    if rank_Q([XA[b] for b in basis] + [XA[nm]]) > len(basis): basis.append(nm)
    if len(basis) == 4: break
rec['basis_of_Cov'] = basis
coords = {}
for nm in NAMES:
    x = solve_coords([XA[b] for b in basis], XA[nm]); coords[nm] = None if x is None else [frac_str(c) for c in x]
rec['coordinates_in_basis'] = coords
rec['checks']['all_patterns_in_span_of_basis'] = all(v is not None for v in coords.values())
save('A_done')

# ================================================================ Stage B: slice
sl = json.loads((SESSION / 'results/slice_choice.json').read_text())
WNAMES = sl['names']; Avecs = sl['A']
def wprime_matrix(coeffs13):
    Z = np.zeros((4, 4), dtype=np.int64)
    for nm, c in zip(WNAMES, coeffs13):
        if c == 0: continue
        if nm == 'a': Z[0, 0] += c
        elif nm[0] == 'r': Z[0, int(nm[1])] += c
        elif nm[0] == 'c': Z[int(nm[1]), 0] += c
        else:
            i, j = int(nm[1]), int(nm[2]); Z[i, j] += c
            if i != j: Z[j, i] += c
    return Z
def eps3(i, j, k):
    return 1 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else (-1 if (i, j, k) in ((0, 2, 1), (2, 1, 0), (1, 0, 2)) else 0)
NU = []
for k in range(3):
    m = np.zeros((4, 4), dtype=np.int64)
    for i in range(3):
        for j in range(3): m[i + 1, j + 1] = -eps3(i, j, k)
    NU.append(m)
def star_point(s, t):
    Z1 = sum(int(s[k]) * wprime_matrix(Avecs[k]) for k in range(5)); Z2 = sum(int(t[k]) * wprime_matrix(Avecs[k]) for k in range(5))
    return np.stack(NU + [Z1, Z2]).astype(np.int64)
PTS = sl['poised_points']
maxZ = max(int(np.max(np.abs(star_point(s, t)[3:]))) for s, t in PTS)
BOUND_SL = 331776 * (120 * maxZ * maxZ) ** 2
rec['checks']['slice'] = dict(max_Z_entry=maxZ, crt_bound=BOUND_SL, modulus=PRIMES2[0] * PRIMES2[1], poised_rank=sl['poised_rank'], tangent_rank=sl['tangent_rank'], degenerate_subslice_rank=sl['degenerate_control_3dim_subslice_tangent_rank'])
assert PRIMES2[0] * PRIMES2[1] > 2 * BOUND_SL
tops = {b: [] for b in basis}          # exact 256-vectors per point, concatenated
tops_all_pt0 = {}
points_done = 0
for ip, (s, t) in enumerate(PTS):
    if left() < 1.5: rec['log'].append('deadline before slice point %d' % ip); break
    Ystar = star_point(s, t); res = {p: {} for p in PRIMES2}
    Tstar = exact_column_tensor(Ystar)
    for p in PRIMES2:
        mod = MODS[p]; T = Tstar
        names_here = sorted(set(half_names) | set(basis), key=NAMES.index) if ip == 0 else basis
        for nm in names_here: res[p][nm], _ = half_tensor(mod, T, PATTERNS[nm])
    for nm in (sorted(set(half_names) | set(basis), key=NAMES.index) if ip == 0 else basis):
        v = crt_vec({p: res[p][nm] for p in PRIMES2}, PRIMES2, BOUND_SL)
        if nm in basis: tops[nm] += v
        if ip == 0: tops_all_pt0[nm] = v
    points_done = ip + 1
    if ip % 10 == 9: save('B_progress')
rec['slice_points_done'] = points_done
r_top = rank_Q([tops[b] for b in basis])
rec['r_top_on_slice'] = dict(rank=r_top, points=points_done, complete=(points_done == len(PTS)))
# ell ratios at slice point 0 for every pattern relative to a reference with nonzero top
ref = next((b for b in basis if any(tops_all_pt0[b])), None)
ell = {}
consistent = True
if ref is not None:
    R = tops_all_pt0[ref]; k0 = next(k for k in range(256) if R[k] != 0)
    for nm in tops_all_pt0:
        V = tops_all_pt0[nm]; lam = Fraction(V[k0], R[k0])
        ok = all(Fraction(V[k]) == lam * R[k] for k in range(256))
        consistent &= ok; ell[nm] = dict(ell=frac_str(lam), proportional_at_point0=ok)
rec['ell_at_slice_point_0'] = dict(reference=ref, values=ell, all_proportional=consistent)
# nearby false identity control: t(b2) - (ell+1) t(ref) must be nonzero on the slice
if ref is not None and len(basis) > 1:
    b2 = [b for b in basis if b != ref][0]; lam = Fraction(ell[b2]['ell'].split('/')[0]) / Fraction(ell[b2]['ell'].split('/')[1]) if '/' in ell[b2]['ell'] else Fraction(ell[b2]['ell'])
    bad = [Fraction(x) - (lam + 1) * Fraction(y) for x, y in zip(tops[b2], tops[ref])]
    good = [Fraction(x) - lam * Fraction(y) for x, y in zip(tops[b2], tops[ref])]
    rec['checks']['false_identity_rejected'] = dict(corrupted_lambda_relation_nonzero=any(v != 0 for v in bad), true_lambda_relation_zero_on_all_points=all(v == 0 for v in good))
save('B_done')

# ================================================================ Stage C: K-vectors and the kernel vector
if r_top == 1 and points_done == len(PTS) and consistent:
    ellf = {nm: Fraction(int(ell[nm]['ell'].split('/')[0]), int(ell[nm]['ell'].split('/')[1])) for nm in ell}
    # cross-check ell via coordinates: ell(H) = sum x_i ell(basis_i)
    cc = True
    for nm in ell:
        x = [Fraction(int(c.split('/')[0]), int(c.split('/')[1])) for c in coords[nm]]
        cc &= (sum(xi * ellf[b] for xi, b in zip(x, basis)) == ellf[nm])
    rec['checks']['ell_linear_in_coordinates'] = cc
    def Kvec(name):
        h = {k.split('_')[1]: k for k in NAMES if k.startswith(name + '_')}
        out = [Fraction(0)] * 256
        for (u, w) in (('h1', 'h2'), ('h1t', 'h2t')):
            for k in range(256): out[k] += ellf[h[u]] * XA[h[w]][k] + ellf[h[w]] * XA[h[u]][k]
        return out
    K = {name: Kvec(name) for name in VEC}
    rK = rank_Q([K['q3'], K['q7'], K['n02']])
    rec['K_vectors'] = dict(rank_Q=rK, ell_products={name: frac_str(sum(ellf[k1] * ellf[k2] for k1, k2 in ((name + '_h1', name + '_h2'), (name + '_h1t', name + '_h2t')))) for name in VEC})
    # recorded degree-12 row ratios (mod P): q7/q3 = 101007, n02/q3 = 295818 must equal the ell-product ratios
    lp = {name: sum(ellf[k1] * ellf[k2] for k1, k2 in ((name + '_h1', name + '_h2'), (name + '_h1t', name + '_h2t'))) for name in VEC}
    rec['checks']['degree12_row_ratios'] = dict(q7_over_q3=frac_mod(lp['q7'] / lp['q3'], P) if lp['q3'] else None, expect_q7=101007, n02_over_q3=frac_mod(lp['n02'] / lp['q3'], P) if lp['q3'] else None, expect_n02=295818)
    if rK == 2:
        # kernel: x K3 + y K7 + z Kn = 0, normalised z = 1
        xy = solve_coords([K['q3'], K['q7']], [-v for v in K['n02']])
        if xy is not None:
            # -K(n02) = x K3 + y K7  =>  K(n02 + x q3 + y q7) = 0  =>  n* = n02 - alpha q3 - beta q7 with alpha = -x, beta = -y
            alpha, beta = -xy[0], -xy[1]
            rec['kernel_vector'] = dict(n_star='n02 - alpha q3 - beta q7', alpha=frac_str(alpha), beta=frac_str(beta), alpha_mod_P=frac_mod(alpha, P), beta_mod_P=frac_mod(beta, P), expected_residues=[265391, 275398],
                                        residues_match=(frac_mod(alpha, P) == 265391 and frac_mod(beta, P) == 275398))
            TROWS = {'q3': [456851, 30271, 120670], 'q7': [3402, 137059, 19278], 'n02': [156683, 233094, 389529]}
            den = alpha.denominator * beta.denominator
            Tn = [(den * TROWS['n02'][i] - (alpha * den).numerator * TROWS['q3'][i] - (beta * den).numerator * TROWS['q7'][i]) % P for i in range(3)]
            rec['kernel_vector']['transverse_den_times_T_mod_P'] = dict(zip(['C2', 'C4_S1S2', 'C4_S1S4'], Tn))
            rec['kernel_vector']['den_mod_P_nonzero'] = (den % P != 0)
            # S0 rows control with exact alpha, beta and with a corrupted alpha
            S0 = [[34725, 239889, 380115], [176113, 112168, 44818], [163934, 316261, 169076], [190461, 231336, 338217], [395778, 379744, 423266], [232316, 28953, 238815]]
            FULL = [[86170, 71919, 226580], [376209, 469277, 41046], [347334, 318883, 320901], [469768, 310015, 415152]]
            a_, b_ = frac_mod(alpha, P), frac_mod(beta, P)
            rec['checks']['recorded_rows_relation_with_exact_alpha_beta'] = dict(S0=[(a_ * r[0] + b_ * r[1] - r[2]) % P for r in S0], full=[(a_ * r[0] + b_ * r[1] - r[2]) % P for r in FULL])
            rec['checks']['corrupted_alpha_rejected'] = any(((a_ + 1) * r[0] + b_ * r[1] - r[2]) % P for r in S0 + FULL)
        else:
            rec['kernel_vector'] = 'inconsistent solve'
save('C_done')
rec['elapsed_s'] = time.perf_counter() - T0
save('done')
print(json.dumps({k: v for k, v in rec.items() if k not in ('patterns', 'coordinates_in_basis', 'log')}, indent=1, default=str)[:6000])
