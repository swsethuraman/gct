"""B18-05: exact evaluation of the eleven-equation space E on actual padding.

Independent evaluator (no import of the B17-04 or Hessian11 code).  A quartic
is given as a monomial dictionary P in n variables plus an n-by-10 matrix M;
F(y) = P(M Q y)/c with Q the B17-04 depression.  The ten-variable Hessian of F
along the chart line y(t) = t*e_t + e_1 is (MQ)^T Hess P(MQ y(t)) (MQ)/c,
evaluated exactly at 21 integer nodes; every t-polynomial is recovered by
exact interpolation and checked at an extra node.  All arithmetic is rational.

Run only through analysis/b15_bound.py (60 s / 512 MiB, one process, one BLAS
thread).  Writes only results/b18_05/.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json, os, random, sys, time
from flint import fmpq_mat, fmpq, fmpz_mat

OUT = Path('results/b18_05')
START = time.perf_counter()
KAPPA = [12, -10, 4, 3, 0, 0, 0, 0, 0, 0, 0]
W = [216, -212, 64, 0, 0, -1, 1, 1, 13, 4, 2]
NAMES = ['R1(A)', 's2R3(A)', 'R2(J2)', 'R3(J3)', 'R3(Q22)', 'S3', 's2S5', 's3S6', 's4S7', 'R1(T2)', 's2R3(T2)']


def qm(rows):
    return fmpq_mat([[fmpq(Q(x).numerator, Q(x).denominator) for x in r] for r in rows])


def q(x):
    return Q(str(x))


def det(rows):
    return q(qm(rows).det())


def adj(rows):
    n = len(rows); M = qm(rows); d = M.det()
    if d != 0:
        Inv = M.inv()
        return [[q(Inv[i, j] * d) for j in range(n)] for i in range(n)]
    return [[(-1) ** (i + j) * det([[rows[a][b] for b in range(n) if b != i] for a in range(n) if a != j])
             for j in range(n)] for i in range(n)]


# ---- polynomials in t as coefficient lists of Fractions ----
def interp(nodes, vals):
    """Newton interpolation through (nodes[i], vals[i]); returns coefficients."""
    n = len(nodes); coef = [Q(v) for v in vals]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (nodes[i] - nodes[i - j])
    poly = [Q(0)] * n
    acc = [Q(1)]
    for k in range(n):
        for i, b in enumerate(acc):
            poly[i] += coef[k] * b
        acc = [Q(0)] + acc
        for i in range(len(acc) - 1):
            acc[i] -= nodes[k] * acc[i + 1]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def pev(a, t):
    r = Q(0)
    for c in reversed(a):
        r = r * t + c
    return r


def pmul(a, b):
    z = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z


def prem(a, p):
    a = list(a) + [Q(0)] * max(0, len(p) - 1 - len(a))
    for i in range(len(a) - 1, len(p) - 2, -1):
        x = a[i] / p[-1]
        if x:
            for j, y in enumerate(p):
                a[i - len(p) + 1 + j] -= x * y
    r = a[:len(p) - 1]
    return r + [Q(0)] * (len(p) - 1 - len(r))


# ---- monomial-dictionary polynomials ----
def eval_poly(P, w):
    tot = Q(0)
    for mono, c in P.items():
        v = Q(c)
        for i, e in mono:
            v *= w[i] ** e
        tot += v
    return tot


def grad_hess(P, w):
    n = len(w); g = [Q(0)] * n; K = [[Q(0)] * n for _ in range(n)]
    for mono, c in P.items():
        d = dict(mono)
        for i, ei in d.items():
            v = Q(c) * ei
            for k, ek in d.items():
                v *= w[k] ** (ek - (k == i))
            g[i] += v
            for j in d:
                e2 = dict(d); e2[i] -= 1
                if e2[j] == 0:
                    continue
                v2 = Q(c) * ei * e2[j]
                e2[j] -= 1
                for k, ek in e2.items():
                    v2 *= w[k] ** ek
                K[i][j] += v2
    return g, K


def matvec(M, y):
    return [sum(Q(M[i][j]) * y[j] for j in range(len(y))) for i in range(len(M))]


def matmul(A, B):
    return [[sum(Q(A[i][k]) * Q(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


class Quartic:
    """F(y) = P(M Q y)/c on C^10, y = (t, x_1..x_9)."""

    def __init__(self, P, M):
        self.P = P; self.M = M
        et = [Q(1)] + [Q(0)] * 9
        self.c = eval_poly(P, matvec(M, et))
        assert self.c != 0, 'off chart: c = 0'
        g, _ = grad_hess(P, matvec(M, et))
        a1 = matvec(transpose(M), g)[1:]  # d/dx_i G(e_t) = [t^3 x_i] G
        self.a1 = a1
        Qm = [[Q(0)] * 10 for _ in range(10)]
        Qm[0][0] = Q(1)
        for i in range(1, 10):
            Qm[0][i] = -3 * a1[i - 1]; Qm[i][i] = 12 * self.c
        self.Q = Qm
        self.MQ = matmul(M, Qm)

    def value(self, y):
        return eval_poly(self.P, matvec(self.MQ, y)) / self.c

    def hess(self, y):
        _, K = grad_hess(self.P, matvec(self.MQ, y))
        MQt = transpose(self.MQ)
        H = matmul(matmul(MQt, K), self.MQ)
        return [[x / self.c for x in r] for r in H]


def line_point(t):
    return [Q(t), Q(1)] + [Q(0)] * 8


def equations(F, nodes=tuple(range(21)), check_node=23):
    """Return E (11 values), the pieces, and consistency checks."""
    Hm, H0, Hp = [F.hess(line_point(t)) for t in (-1, 0, 1)]
    N2 = [[(Hp[i][j] + Hm[i][j] - 2 * H0[i][j]) / 4 for j in range(1, 10)] for i in range(1, 10)]
    N3 = [[(Hp[i][j] - Hm[i][j]) / 12 for j in range(1, 10)] for i in range(1, 10)]
    N4 = [[H0[i][j] / 12 for j in range(1, 10)] for i in range(1, 10)]
    N = [N2, N3, N4]
    s = [Nd[0][0] for Nd in N]
    u = [[r[0] for r in Nd] for Nd in N]
    p = [s[2], s[1], s[0], Q(0), Q(1)]
    # chart checks: monic depressed, p(t) = F(t,e), h and v blocks
    for t in (-2, 3, 5):
        Ht = F.hess(line_point(t))
        assert F.value(line_point(t)) == pev(p, t)
        assert Ht[0][0] == 12 * t * t + 2 * s[0]
        for i in range(9):
            assert Ht[0][i + 1] == 4 * t * u[0][i] + 3 * u[1][i]
            for j in range(9):
                assert Ht[i + 1][j + 1] == 2 * t * t * N2[i][j] + 6 * t * N3[i][j] + 12 * N4[i][j]
    vals = {k: [] for k in ('A', 'J2', 'J3', 'Q22', 'DH', 'T2')}
    all_nodes = list(nodes) + [check_node]
    for t in all_nodes:
        Ht = F.hess(line_point(t))
        B = [r[1:] for r in Ht[1:]]
        v = Ht[0][1:]
        adjB = adj(B)
        adjH = adj(Ht)
        vals['A'].append(det(B))
        vals['J2'].append(-sum(u[0][i] * adjB[i][j] * v[j] for i in range(9) for j in range(9)))
        vals['J3'].append(-sum(u[1][i] * adjB[i][j] * v[j] for i in range(9) for j in range(9)))
        vals['Q22'].append(sum(u[0][i] * adjH[i + 1][j + 1] * u[0][j] for i in range(9) for j in range(9)))
        vals['DH'].append(det(Ht))
        vals['T2'].append(sum(adjH[i + 1][j + 1] * N2[j][i] for i in range(9) for j in range(9)))
    polys = {}
    for k, vs in vals.items():
        poly = interp([Q(t) for t in nodes], vs[:len(nodes)])
        assert pev(poly, Q(check_node)) == vs[-1], k
        polys[k] = poly
    R = {k: prem(polys[k], p) for k in ('A', 'J2', 'J3', 'Q22', 'T2')}
    S = prem(polys['DH'], pmul(p, p))
    E = [R['A'][1], s[0] * R['A'][3], R['J2'][2], R['J3'][3], R['Q22'][3],
         S[3], s[0] * S[5], s[1] * S[6], s[2] * S[7], R['T2'][1], s[0] * R['T2'][3]]
    kappa_E = sum(k * e for k, e in zip(KAPPA, E))
    ambient_identity = kappa_E - (S[3] - s[0] * S[5] - s[1] * S[6] + (s[0] ** 2 - s[2]) * S[7])
    psi_direct = (204 * R['A'][1] - 202 * s[0] * R['A'][3] + 60 * R['J2'][2] - 3 * R['J3'][3]
                  + 4 * R['T2'][1] + 2 * s[0] * R['T2'][3] + (s[0] ** 2 + 12 * s[2]) * S[7])
    w_E = sum(k * e for k, e in zip(W, E))
    return dict(E=E, s=s, p=p, S=S, R=R, kappa_E=kappa_E, w_E=w_E, psi_direct=psi_direct,
                ambient_identity_residual=ambient_identity, N=N,
                polydeg={k: len(v) - 1 for k, v in polys.items()})


# ---- source polynomials ----
def zper3():
    """Independent z times per3, ten variables: 0 = z, 1..9 = entries row major."""
    P = {}
    for perm in permutations(range(3)):
        mono = ((0, 1),) + tuple((1 + 3 * i + perm[i], 1) for i in range(3))
        P[tuple(sorted(mono))] = 1
    return P


def det4():
    P = {}
    for perm in permutations(range(4)):
        sgn = (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        mono = tuple(sorted((4 * i + perm[i], 1) for i in range(4)))
        P[mono] = sgn
    return P


def z_cubic(rng, lo=-5, hi=5):
    """z times a random cubic in nine independent variables 1..9."""
    P = {}
    for i in range(1, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                c = rng.randint(lo, hi)
                if c:
                    d = {}
                    for v in (i, j, k):
                        d[v] = d.get(v, 0) + 1
                    mono = tuple(sorted(((0, 1),) + tuple(d.items())))
                    P[mono] = c
    return P


def rand_matrix(rng, rows, cols, bound):
    return [[rng.randint(-bound, bound) for _ in range(cols)] for _ in range(rows)]


def rank_and_kernel(rows):
    M = qm(rows)
    Rr, rk = M.rref()
    piv = []
    j = 0
    for i in range(rk):
        while Rr[i, j] == 0:
            j += 1
        piv.append(j)
    ker = []
    for j in range(11):
        if j not in piv:
            v = [Q(0)] * 11; v[j] = Q(1)
            for i, k in enumerate(piv):
                v[k] = -q(Rr[i, j])
            ker.append(v)
    return rk, ker


def emit(stage, **kw):
    kw['seconds'] = round(time.perf_counter() - START, 3)
    print(json.dumps(dict(stage=stage, **kw)), flush=True)


def main():
    assert all(os.environ.get(k) == '1' for k in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'])
    OUT.mkdir(parents=True, exist_ok=True)
    report = {}
    # ---- control 1: reproduce B17-04 seeds 170400..170402 exactly ----
    b1704 = json.loads(Path('../B15-04/results/b17_04/padding_points.json').read_text())
    repro = []
    for pt in b1704[:3]:
        F = Quartic(zper3(), pt['L'])
        assert F.c == pt['c'] and [int(x) for x in F.a1] == pt['a1']
        r = equations(F)
        theirs = [int(x) for x in pt['E_values']]
        mine = r['E']
        assert all(x.denominator == 1 for x in mine)
        assert [int(x) for x in mine] == theirs, ('mismatch', pt['seed'])
        assert r['kappa_E'] == 0 and r['ambient_identity_residual'] == 0 and r['w_E'] == r['psi_direct']
        repro.append(dict(seed=pt['seed'], match=True, w_E=str(r['w_E'])))
    report['control_reproduce_b17_04'] = repro
    emit('control_repro', points=repro)
    # ---- control 2: determinant points give E = 0 ----
    rng = random.Random(1805)
    detctrl = []
    for k in range(2):
        M = rand_matrix(rng, 16, 10, 7)
        F = Quartic(det4(), M)
        r = equations(F)
        detctrl.append(dict(all_zero=all(e == 0 for e in r['E']), ambient_residual=str(r['ambient_identity_residual'])))
        assert detctrl[-1]['all_zero']
    report['control_det4'] = detctrl
    emit('control_det4', result=detctrl)
    # ---- control 3: generic quartic gives w_E != 0 (w is not an ambient relation) ----
    Pgen = {}
    for _ in range(60):
        idx = sorted(rng.randrange(10) for _ in range(4))
        d = {}
        for v in idx:
            d[v] = d.get(v, 0) + 1
        Pgen[tuple(sorted(d.items()))] = rng.randint(-4, 4)
    Pgen[((0, 4),)] = 1
    F = Quartic(Pgen, [[int(i == j) for j in range(10)] for i in range(10)])
    r = equations(F)
    report['control_generic_quartic'] = dict(w_E_nonzero=r['w_E'] != 0, kappa_E_nonzero=r['kappa_E'] != 0,
                                             ambient_residual=str(r['ambient_identity_residual']))
    emit('control_generic', **report['control_generic_quartic'])
    # ---- main: fresh actual padding points with large entries ----
    main_pts = []
    rows = []
    for seed in range(180500, 180506):
        rg = random.Random(seed)
        L = rand_matrix(rg, 10, 10, 10 ** 4)
        dL = int(fmpz_mat(L).det()); assert dL != 0
        F = Quartic(zper3(), L)
        r = equations(F)
        assert r['kappa_E'] == 0 and r['ambient_identity_residual'] == 0 and r['w_E'] == r['psi_direct']
        rows.append(r['E'])
        main_pts.append(dict(seed=seed, L=L, det_L=str(dL), c=str(F.c), a1=[str(x) for x in F.a1],
                             E=[str(x) for x in r['E']], kappa_E=str(r['kappa_E']), w_E=str(r['w_E']),
                             psi_direct=str(r['psi_direct']),
                             finite_degree27_w_E=str(r['w_E'] * F.c ** 27)))
        emit('padding_point', seed=seed, c=str(F.c), w_E_is_zero=(r['w_E'] == 0),
             w_E_digits=len(str(abs(r['w_E'].numerator))))
    rk, ker = rank_and_kernel(rows)
    report['padding_points'] = main_pts
    report['padding_sample_rank'] = rk
    report['padding_sample_kernel'] = [[str(x) for x in v] for v in ker]
    emit('padding_rank', rank=rk, kernel=report['padding_sample_kernel'])
    # ---- broader family: z times a generic nine-variable cubic ----
    fam = []
    rows2 = []
    for seed in range(180600, 180608):
        rg = random.Random(seed)
        P = z_cubic(rg)
        L = rand_matrix(rg, 10, 10, 50)
        if int(fmpz_mat(L).det()) == 0:
            continue
        F = Quartic(P, L)
        r = equations(F)
        rows2.append(r['E'])
        fam.append(dict(seed=seed, kappa_E=str(r['kappa_E']), w_E_zero=(r['w_E'] == 0)))
    rk2, ker2 = rank_and_kernel(rows2)
    report['z_times_generic_cubic'] = dict(points=fam, sample_rank=rk2, sample_kernel=[[str(x) for x in v] for v in ker2])
    emit('z_generic_cubic', rank=rk2, kernel=report['z_times_generic_cubic']['sample_kernel'])
    report['wall_seconds'] = time.perf_counter() - START
    (OUT / 'psi_evaluation.json').write_text(json.dumps(report, indent=1) + '\n')
    emit('complete', wall=report['wall_seconds'])


if __name__ == '__main__':
    main()
