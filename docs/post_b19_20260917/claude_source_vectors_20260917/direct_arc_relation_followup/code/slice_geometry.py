"""Slice geometry for the top-part identity test (pure linear algebra, exact integers / mod P ranks).

W' = W_{-1} + W_{+1} with basis order: a, r1, r2, r3, c1, c2, c3, S11, S22, S33, S12, S13, S23 (13).
G' = L~ x| U_-  acts on W' (= W / W_0):
  L~ = GL_3 x (C*)^3 (no determinant constraint): alpha: scales a, r; beta: scales a, c; c: scales r, Sigma;
       g = E_kl in gl_3: r -> E r, c -> E c, Sigma -> E Sigma + Sigma E^T.
  U_-: left multiplication by I + E_k0 (k = 1..3): c_k += a, Sigma_kn += r_n/2 (n != k), Sigma_kk += r_k;
       right multiplication by I + E_0n: r_n += a, Sigma_kn += c_k/2 (k != n), Sigma_nn += c_n.
  (Both fix every skew block matrix nu_k, hence omega = nu_1^nu_2^nu_3, and preserve W_0.)
The cone S* of decomposable bivectors Z_1 ^ Z_2 in Lambda^2 W' has dimension 23.  For a slice
Sigma = cone(V) with V = span of chosen basis vectors, G'.Sigma is dense in S* iff at some point Omega of Sigma the
tangent directions {X.Omega : X in Lie(G')} + T_Omega(Sigma) span T_Omega(S*) (dimension 23).
Poised set: N points (s,t) with s,t in {-1,0,1}^dimV such that the N x C(m+1,2) matrix of quadratic monomials in the
Pluecker coordinates pi_ij(s,t) has rank N = dim S_22(V) = m^2 (m^2 - 1) / 12 (m = dim V)."""
import itertools, json, random
from fractions import Fraction
NAMES = ['a', 'r1', 'r2', 'r3', 'c1', 'c2', 'c3', 'S11', 'S22', 'S33', 'S12', 'S13', 'S23']
I = {n: i for i, n in enumerate(NAMES)}
def sig(k, l): return 'S%d%d' % (min(k, l), max(k, l))
def gen_matrices():
    """13x13 matrices (as dict of Fractions) of the 18 Lie algebra generators acting on W'."""
    gens = {}
    def M(): return [[Fraction(0)] * 13 for _ in range(13)]
    m = M(); m[I['a']][I['a']] = 1
    for k in (1, 2, 3): m[I['r%d' % k]][I['r%d' % k]] = 1
    gens['alpha'] = m
    m = M(); m[I['a']][I['a']] = 1
    for k in (1, 2, 3): m[I['c%d' % k]][I['c%d' % k]] = 1
    gens['beta'] = m
    m = M()
    for k in (1, 2, 3): m[I['r%d' % k]][I['r%d' % k]] = 1
    for k in (1, 2, 3):
        for l in range(k, 4): m[I[sig(k, l)]][I[sig(k, l)]] = 1
    gens['c'] = m
    for k in (1, 2, 3):
        for l in (1, 2, 3):
            m = M()
            m[I['r%d' % k]][I['r%d' % l]] += 1; m[I['c%d' % k]][I['c%d' % l]] += 1
            # Sigma -> E_kl Sigma + Sigma E_lk : (E Sigma)_{k n} = Sigma_{l n}; (Sigma E^T)_{n k} = Sigma_{n l}
            for n in (1, 2, 3):
                m[I[sig(k, n)]][I[sig(l, n)]] += 1
                m[I[sig(n, k)]][I[sig(n, l)]] += 1
            # symmetric coordinates: Sigma_{kn} and Sigma_{nk} are the same coordinate; the map above adds both
            # contributions to the symmetric coordinate sig(k,n), which is what E Sigma + Sigma E^T does on Sym^2.
            gens['g%d%d' % (k, l)] = m
    for k in (1, 2, 3):
        m = M(); m[I['c%d' % k]][I['a']] += 1
        for n in (1, 2, 3):
            m[I[sig(k, n)]][I['r%d' % n]] += Fraction(1, 1) if n == k else Fraction(1, 2)
        gens['Lk0_%d' % k] = m
    for n in (1, 2, 3):
        m = M(); m[I['r%d' % n]][I['a']] += 1
        for k in (1, 2, 3):
            m[I[sig(k, n)]][I['c%d' % k]] += Fraction(1, 1) if k == n else Fraction(1, 2)
        gens['R0n_%d' % n] = m
    return gens
PAIRS = [(i, j) for i in range(13) for j in range(i + 1, 13)]
PI = {p: k for k, p in enumerate(PAIRS)}
def wedge2(u, v):
    w = [Fraction(0)] * 78
    for (i, j), k in PI.items(): w[k] = u[i] * v[j] - u[j] * v[i]
    return w
def matvec(m, v): return [sum(m[i][j] * v[j] for j in range(13)) for i in range(13)]
def rank_frac(rows):
    M = [list(r) for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
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
def density_rank(Vnames, Z1, Z2):
    gens = gen_matrices()
    dirs = []
    for gname, m in gens.items():
        dirs.append([x + y for x, y in zip(wedge2(matvec(m, Z1), Z2), wedge2(Z1, matvec(m, Z2)))])
    for n in Vnames:
        e = [Fraction(0)] * 13; e[I[n]] = Fraction(1)
        dirs.append(wedge2(e, Z2)); dirs.append(wedge2(Z1, e))
    return rank_frac(dirs), len(dirs)
def vec_from(coeffs, Vnames):
    z = [Fraction(0)] * 13
    for cf, n in zip(coeffs, Vnames): z[I[n]] += cf
    return z
def plucker(s, t):
    m = len(s); return [s[i] * t[j] - s[j] * t[i] for i in range(m) for j in range(i + 1, m)]
def poised_points(m, N, seed):
    rng = random.Random(seed)
    npl = m * (m - 1) // 2
    monos = [(i, j) for i in range(npl) for j in range(i, npl)]
    pts = []; rows = []
    tries = 0
    while len(pts) < N and tries < 5000:
        tries += 1
        s = [rng.choice((-1, 0, 1)) for _ in range(m)]; t = [rng.choice((-1, 0, 1)) for _ in range(m)]
        p = plucker(s, t)
        if all(x == 0 for x in p): continue
        row = [Fraction(p[i] * p[j]) for i, j in monos]
        if rank_frac(rows + [row]) > len(rows): rows.append(row); pts.append((s, t))
    return pts, rank_frac(rows) if rows else 0
if __name__ == '__main__':
    out = {}
    for Vnames in (['a', 'r1', 'c2', 'S12'], ['r1', 'c1', 'S23', 'a'], ['a', 'r1', 'r2', 'c3', 'S12'], ['a', 'r1', 'c2', 'S12', 'S33'], ['r1', 'r2', 'c1']):
        Z1 = vec_from([1, 1, 0, 1, 0][:len(Vnames)], Vnames); Z2 = vec_from([0, 1, 1, -1, 1][:len(Vnames)], Vnames)
        rk, nd = density_rank(Vnames, Z1, Z2)
        m = len(Vnames); dimS22 = m * m * (m * m - 1) // 12
        pts, prk = poised_points(m, dimS22, 20260917)
        out['+'.join(Vnames)] = dict(dim_V=m, tangent_rank=rk, directions=nd, dense=(rk == 23), dim_S22=dimS22, poised_points_found=len(pts), poised_rank=prk)
        print(Vnames, 'tangent rank', rk, '/ 23 from', nd, 'directions; dim S22 =', dimS22, 'poised', len(pts), prk)
    json.dump(out, open('results/slice_geometry_precheck.json', 'w'), indent=1)
