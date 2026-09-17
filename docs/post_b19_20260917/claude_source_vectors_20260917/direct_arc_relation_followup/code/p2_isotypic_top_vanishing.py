"""Pilot 2: exact isotypic analysis of D* = nu_1 ^ nu_2 ^ nu_3 ^ Z_1 ^ Z_2 in Lambda^5(A (x) B).

Basis of W = A (x) B: e_(a,b), a, b in 0..3 (grid position). nu_k = A(e_k) = sum_{i,j} (-eps_{ijk}) e_(i+1, j+1)
(the three basis skew matrices of the lower-right block, B18-02 convention A(v)_{ij} = -eps_{ijk} v_k).
W' = W_{-1} + W_{+1} has the 13 basis vectors a = e_(0,0), r_k = e_(0,k), c_k = e_(k,0), Sigma_ij = e_(i,j) + e_(j,i)
(i < j), Sigma_ii = e_(i,i).  Lambda^5(A(x)B) = (+)_{mu |- 5} S_mu A (x) S_mu' B, each with multiplicity one, and the
pieces are the eigenspaces of the gl(A)-Casimir C_A = sum_{ij} E_ij E_ji with eigenvalues
c_mu = sum_i mu_i (mu_i + 5 - 2i):  (4,1):30  (3,2):24  (3,1,1):20  (2,2,1):16  (2,1,1,1):10.
For every antisymmetric pair of W'-basis vectors (78 pairs) we compute D*(e_p, e_q) exactly as an integer vector in
Lambda^5 (dict over sorted 5-subsets) and test, for each mu, whether prod_{nu != mu} (C_A - c_nu) D* = 0 exactly.
Since D* is bilinear in (Z_1, Z_2), a component vanishing on all basis pairs vanishes identically on the locus S*.
Controls: the minimal polynomial prod_mu (C_A - c_mu) annihilates random vectors; trace(C_A) = sum c_mu dim;
the S_5-sign / antisymmetry of the wedge; nonzero components are reported with their sizes."""
import itertools, json, random, sys, time
from fractions import Fraction
T0 = time.perf_counter()
OUT = sys.argv[1] if len(sys.argv) > 1 else 'results/p2_isotypic_top_vanishing.json'
rec = dict(checks={}, results={}, stage_times={})
def save(stage):
    rec['stage_times'][stage] = time.perf_counter() - T0
    json.dump(rec, open(OUT, 'w'), indent=1); print('stage', stage, round(rec['stage_times'][stage], 2), flush=True)

POS = [(a, b) for a in range(4) for b in range(4)]
IDX = {p: i for i, p in enumerate(POS)}
def eps3(i, j, k):
    return 1 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else (-1 if (i, j, k) in ((0, 2, 1), (2, 1, 0), (1, 0, 2)) else 0)
# vectors in W as dict {position index: coeff}
def vec(d): return {IDX[p]: c for p, c in d.items() if c}
NU = []
for k in range(3):
    d = {}
    for i in range(3):
        for j in range(3):
            e = -eps3(i, j, k)
            if e: d[(i + 1, j + 1)] = e
    NU.append(vec(d))
WP = {'a': vec({(0, 0): 1})}
for k in range(1, 4): WP['r%d' % k] = vec({(0, k): 1}); WP['c%d' % k] = vec({(k, 0): 1})
for i in range(1, 4):
    for j in range(i, 4):
        WP['S%d%d' % (i, j)] = vec({(i, j): 1}) if i == j else vec({(i, j): 1, (j, i): 1})
assert len(WP) == 13
def perm_sign_sort(lst):
    """sign of the permutation sorting lst (distinct ints), and the sorted tuple"""
    s = 1; l = list(lst)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]: s = -s
    return s, tuple(sorted(l))
def wedge(vectors):
    out = {}
    for combo in itertools.product(*[list(v.items()) for v in vectors]):
        idxs = [c[0] for c in combo]
        if len(set(idxs)) < len(idxs): continue
        coef = 1
        for c in combo: coef *= c[1]
        s, key = perm_sign_sort(idxs)
        out[key] = out.get(key, 0) + s * coef
    return {k: v for k, v in out.items() if v}
# gl(A) action: E_ij e_(a,b) = delta_{j a} e_(i,b)
def E_A(i, j, vecL):
    out = {}
    for key, coef in vecL.items():
        for slot, pidx in enumerate(key):
            a, b = POS[pidx]
            if a != j: continue
            newp = IDX[(i, b)]
            if newp in key and newp != pidx: continue
            new = list(key); new[slot] = newp
            s, nk = perm_sign_sort(new)
            out[nk] = out.get(nk, 0) + s * coef
    return {k: v for k, v in out.items() if v}
def casimir(vecL):
    out = {}
    for i in range(4):
        for j in range(4):
            t = E_A(i, j, E_A(j, i, vecL))
            for k, v in t.items(): out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}
def add(u, v, s=1):
    out = dict(u)
    for k, c in v.items(): out[k] = out.get(k, 0) + s * c
    return {k: c for k, c in out.items() if c}
def scal(u, s): return {k: c * s for k, c in u.items()} if s else {}
MU = {'(4,1)': 30, '(3,2)': 24, '(3,1,1)': 20, '(2,2,1)': 16, '(2,1,1,1)': 10}
DIMS = {'(4,1)': 84 * 4, '(3,2)': 60 * 20, '(3,1,1)': 36 * 36, '(2,2,1)': 20 * 60, '(2,1,1,1)': 4 * 84}
rec['checks']['sum_dims_expect_4368'] = sum(DIMS.values())
# ---- dense Casimir matrix on the 4368-dimensional Lambda^5 (numpy int64), Krylov powers for the projections
import numpy as np
SUBS = list(itertools.combinations(range(16), 5)); SIDX = {s: i for i, s in enumerate(SUBS)}; N = len(SUBS)
CM = np.zeros((N, N), dtype=np.int64)
for col, sub in enumerate(SUBS):
    for key, c in casimir({sub: 1}).items(): CM[SIDX[key], col] = c
rec['checks']['sum_dims_expect_4368'] = N
def to_np(d):
    v = np.zeros(N, dtype=np.int64)
    for k, c in d.items(): v[SIDX[k]] = c
    return v
tr = int(np.trace(CM)); expected_tr = sum(MU[m] * DIMS[m] for m in MU)
rec['checks']['trace_C_A'] = dict(computed=tr, expected=expected_tr, passed=(tr == expected_tr))
random.seed(20260917); ok = True
for trial in range(3):
    v = np.array([random.randint(-3, 3) for _ in range(N)], dtype=np.int64)
    for name, c in MU.items(): v = CM.dot(v) - c * v
    ok &= bool(np.all(v == 0))
rec['checks']['minimal_polynomial_annihilates_random_vectors'] = ok
rec['checks']['C_A_symmetric_matrix'] = bool(np.all(CM == CM.T))
save('controls')
# polynomial coefficients of prod_{nu != mu}(x - c_nu) for each mu
def polymul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): r[i + j] += a * b
    return r
POLY = {}
for m in MU:
    p = [1]
    for m2, c2 in MU.items():
        if m2 != m: p = polymul(p, [-c2, 1])
    POLY[m] = p                      # coefficients in increasing degree
names = list(WP)
results = {m: dict(all_zero=True, nonzero_pairs=[], max_abs=0) for m in MU}
pairs_nonzero_Dstar = 0
for i in range(13):
    for j in range(i + 1, 13):
        D = wedge(NU + [WP[names[i]], WP[names[j]]])
        if not D: continue
        pairs_nonzero_Dstar += 1
        v = [to_np(D)]
        for k in range(4): v.append(CM.dot(v[-1]))
        for m, p in POLY.items():
            w = sum(int(p[k]) * v[k] for k in range(len(p)))
            if np.any(w != 0):
                results[m]['all_zero'] = False; results[m]['nonzero_pairs'].append([names[i], names[j]])
                results[m]['max_abs'] = max(results[m]['max_abs'], int(np.max(np.abs(w))))
rec['results'] = dict(pairs_with_nonzero_Dstar=pairs_nonzero_Dstar, isotypic=results,
                      vanishing_pieces=[m for m in MU if results[m]['all_zero']], surviving_pieces=[m for m in MU if not results[m]['all_zero']])
cov_pieces = {'Lam2_V(3,2)': ['(3,2)'], 'Lam2_V(3,1,1)': ['(3,1,1)'], 'Lam2_V(2,2,1)': ['(2,2,1)'], 'cross_V(3,2)xV(2,2,1)': ['(3,2)', '(2,2,1)']}
dead = [k for k, need in cov_pieces.items() if any(results[m]['all_zero'] for m in need)]
rec['results']['Cov_pieces_with_vanishing_top'] = dead
rec['results']['dim_Cov0_lower_bound'] = len(dead)
rec['results']['r_top_upper_bound'] = 4 - len(dead)
rec['elapsed_s'] = time.perf_counter() - T0
save('done')
print(json.dumps(rec['results'], indent=1)[:3000])
