"""P3 (reserve): exact rational rank of the second Koszul differential D_7 at det_4 and z*per_3 (16 variables).

ker D_7 = { antisymmetric 16x16 matrices A of linear forms whose every column lies in the linear
syzygy space L = { (l_1..l_16) in S_1^16 : sum_i l_i d_i F = 0 } }  (D_7(sum_{i<j} a_ij e_i^e_j) = sum_j (sum_i a_ij d_i F) e_j).
L is the exact rational left kernel of M_4(F) (flint.fmpz_mat.nullspace on M_4^T). Parametrise the
columns by L and impose antisymmetry: dim ker D_7 = 16 dim L - rank(antisymmetry system), exactly over Q.
Then rank_Q D_7 = 1920 - dim ker. Also exact D_6 for both (constant antisymmetric matrices with columns
in the constant syzygy space). All ranks exact over Q (fmpz_mat).
"""
import itertools, json, math, os, time
from collections import defaultdict
import flint

T0 = time.perf_counter()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p3_koszul2_exact.json')
NV = 16
res = {'script': 'p3_koszul2_exact.py', 'checks': []}

def monomials(nvars, deg):
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

def poly_det4():
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
    F = defaultdict(int)
    for perm in itertools.permutations(range(3)):
        e = [0] * NV
        e[0] += 1
        for a in range(3):
            e[1 + 3 * a + perm[a]] += 1
        F[tuple(e)] += 1
    return dict(F)

def partial(F, i):
    G = defaultdict(int)
    for e, cf in F.items():
        if e[i] > 0:
            e2 = list(e); e2[i] -= 1
            G[tuple(e2)] += cf * e[i]
    return dict(G)

def syzygy_space(F, deg):
    """Exact rational basis of { (l_1..l_16) in S_deg^16 : sum_i l_i d_i F = 0 }, as integer vectors
    indexed by (i, monomial of degree deg). Returns (basis rows as lists, index of (i, m))."""
    parts = [partial(F, i) for i in range(NV)]
    mons = list(monomials(NV, deg))
    cols = {e: t for t, e in enumerate(monomials(NV, deg + 3))}
    rowidx = {}
    mat = []
    for i in range(NV):
        for m in mons:
            rowidx[(i, m)] = len(mat)
            row = [0] * len(cols)
            for e, cf in parts[i].items():
                row[cols[tuple(a + b for a, b in zip(e, m))]] += cf
            mat.append(row)
    M = flint.fmpz_mat(mat)               # rows (i,m), columns monomials of degree deg+3
    X, nullity = M.transpose().nullspace()  # columns of X span the left kernel of M
    basis = []
    for s in range(nullity):
        basis.append([int(X[r, s]) for r in range(M.nrows())])
    return basis, rowidx, mons, M.rank()

def koszul2_kernel_dim(F, k):
    deg = k - 6
    basis, rowidx, mons, rankM = syzygy_space(F, deg)
    dL = len(basis)
    # unknowns lambda[j][s], j = 0..15, s = 0..dL-1: column j of A = sum_s lambda[j][s] basis[s]
    # constraints: for all i <= j and every monomial m: A[i][j](m) + A[j][i](m) = 0
    #   A[i][j](m) = sum_s lambda[j][s] basis[s][rowidx[(i,m)]]
    nunk = NV * dL
    rows = []
    for i in range(NV):
        for j in range(i, NV):
            for m in mons:
                row = [0] * nunk
                for s in range(dL):
                    v = basis[s][rowidx[(i, m)]]
                    if v:
                        row[j * dL + s] += v
                    w = basis[s][rowidx[(j, m)]]
                    if w:
                        row[i * dL + s] += w
                if any(row):
                    rows.append(row)
    rk = flint.fmpz_mat(rows).rank() if rows else 0
    return nunk - rk, dL, rankM, (len(rows), nunk)

out = {}
for name, F in (('det4', poly_det4()), ('zper3', poly_zper3())):
    for k in (6, 7):
        kd, dL, rankM, shape = koszul2_kernel_dim(F, k)
        nrows = math.comb(NV, 2) * math.comb(k - 6 + NV - 1, NV - 1)
        out[f'{name}_k{k}'] = {'dim_ker_D_k': kd, 'rank_D_k_exact_Q': nrows - kd, 'rows_of_D_k': nrows,
                                'dim_syzygy_space_L': dL, 'rank_M_{}'.format(k - 3): rankM, 'antisym_system_shape': shape}
        print(name, k, out[f'{name}_k{k}'], f't={time.perf_counter()-T0:.1f}s', flush=True)
res['results'] = out
res['checks'].append({'name': 'rank_Q M_4: det4 226, zper3 155 (exact over Q, matches (A1),(A2))', 'pass': out['det4_k7']['rank_M_4'] == 226 and out['zper3_k7']['rank_M_4'] == 155})
res['checks'].append({'name': 'D_6 exact ranks: det4 120, zper3 105 (matches P1 mod p)', 'pass': out['det4_k6']['rank_D_k_exact_Q'] == 120 and out['zper3_k6']['rank_D_k_exact_Q'] == 105})
res['checks'].append({'name': 'D_7 exact rank at det4 is >= the P1 Gram lower bound 1904', 'pass': out['det4_k7']['rank_D_k_exact_Q'] >= 1904, 'value': out['det4_k7']['rank_D_k_exact_Q']})
res['checks'].append({'name': 'D_7 exact rank at zper3 is >= the P1 Gram lower bound 1650', 'pass': out['zper3_k7']['rank_D_k_exact_Q'] >= 1650, 'value': out['zper3_k7']['rank_D_k_exact_Q']})
res['second_differential_blind_in_degree_7'] = out['zper3_k7']['rank_D_k_exact_Q'] <= out['det4_k7']['rank_D_k_exact_Q']
res['second_differential_gives_det_equations_in_degree_7'] = out['det4_k7']['rank_D_k_exact_Q'] < 1920
res['wall_seconds'] = time.perf_counter() - T0
res['all_checks_pass'] = all(c['pass'] for c in res['checks'])
with open(OUT, 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({c['name']: c['pass'] for c in res['checks']}, indent=1))
print('blind_in_degree_7 =', res['second_differential_blind_in_degree_7'], '; det equations from D_7 =', res['second_differential_gives_det_equations_in_degree_7'])
print('ALL PASS' if res['all_checks_pass'] else 'SOME CHECK FAILED', f'{res["wall_seconds"]:.1f}s')
