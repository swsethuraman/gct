"""B18-05 Step 2: root-local reduction of the eleven equations on the product
family F = l * Gamma (Gamma a cubic on V/zeta), and the symbolic Psi identity.

Part A (exact rational, at actual z*per3 padding points): checks every lemma
used by the reduction as a polynomial divisibility statement modulo Gamma, and
rebuilds all eleven E values from the root-local model (A mod Gamma only).
Part B (sympy): with the three roots of Gamma and the three values A(t_i) as
free symbols, verifies Psi == 0 and kappa.E == 0 identically, and measures the
kernel of the model E space.

Run only through analysis/b15_bound.py.  Writes only results/b18_05/.
"""
from fractions import Fraction as Q
from pathlib import Path
import json, os, random, sys, time
import sympy as sp
from flint import fmpz_mat

sys.path.insert(0, 'analysis')
from b18_05_psi import (Quartic, zper3, equations, interp, pev, pmul, prem, matvec, matmul,
                        transpose, adj, det, line_point, qm, q, KAPPA, W, rand_matrix)

OUT = Path('results/b18_05')
START = time.perf_counter()


def emit(stage, **kw):
    kw['seconds'] = round(time.perf_counter() - START, 3)
    print(json.dumps(dict(stage=stage, **kw)), flush=True)


# ---- univariate polynomial helpers over Q (coefficient lists, low degree first) ----
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def psub(a, b):
    return padd(a, [-x for x in b])


def pscale(a, c):
    return ptrim([c * x for x in a])


def pdivmod(a, b):
    a = ptrim(a); b = ptrim(b)
    if len(a) < len(b):
        return [Q(0)], a
    qq = [Q(0)] * (len(a) - len(b) + 1)
    r = list(a)
    for i in range(len(a) - len(b), -1, -1):
        c = r[i + len(b) - 1] / b[-1]
        qq[i] = c
        for j, y in enumerate(b):
            r[i + j] -= c * y
    return ptrim(qq), ptrim(r[:len(b) - 1] or [Q(0)])


def pmod(a, m):
    return pdivmod(a, m)[1]


def pgcd(a, b):
    a = ptrim(a); b = ptrim(b)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, pdivmod(a, b)[1]
    return pscale(a, 1 / a[-1])


def pinv_mod(a, m):
    """Inverse of a modulo m (extended Euclid); requires gcd(a, m) = 1."""
    r0, r1 = ptrim(m), pmod(a, m)
    s0, s1 = [Q(0)], [Q(1)]
    while not (len(r1) == 1 and r1[0] == 0):
        qq, r2 = pdivmod(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, psub(s0, pmul(qq, s1))
    assert len(r0) == 1 and r0[0] != 0, 'not invertible'
    return pmod(pscale(s0, 1 / r0[0]), m)


def pderiv(a):
    return ptrim([i * a[i] for i in range(1, len(a))] or [Q(0)])


def is_zero(a):
    return all(x == 0 for x in a)


def pad(a, n):
    return list(a) + [Q(0)] * (n - len(a))


# ---- Part A ----
def poly_matrix(F, deg, nodes=None):
    """Entries of H(t) as polynomials (degree <= deg) by interpolation."""
    nodes = nodes or list(range(deg + 1))
    Hs = [F.hess(line_point(t)) for t in nodes]
    return [[interp([Q(t) for t in nodes], [Hs[k][i][j] for k in range(len(nodes))]) for j in range(10)]
            for i in range(10)]


def part_a(L, label):
    F = Quartic(zper3(), L)
    r = equations(F)
    E_true = r['E']; s = r['s']; p = r['p']; N = r['N']
    u = [[row[0] for row in Nd] for Nd in N]
    # split data: l = row 0 of LQ (covector), Gamma = per3(rows 1..9 of LQ . y)/c
    LQ = F.MQ
    l_raw = [Q(x) for x in LQ[0]]
    l0 = l_raw[0]
    l_mon = [x / l0 for x in l_raw]                  # monic split: l' = l/l0
    t1 = -l_mon[1]                                    # z(t) = l'(t e_t + e_1) = t - t1
    zeta = [q(x) for x in (qm(LQ).inv() * qm([[1] + [0] * 9]).transpose()).entries()]
    zeta = [Q(str(v)) for v in zeta]
    nu = sum(a * b for a, b in zip(l_mon, zeta))     # l'(zeta) = 1/l0
    zeta0 = zeta[0]; zetaW = zeta[1:]
    zpoly = [-t1, Q(1)]
    Gamma, rem = pdivmod(p, zpoly)
    assert is_zero(rem) and len(Gamma) == 4 and Gamma[3] == 1
    g2, g1, g0 = Gamma[2], Gamma[1], Gamma[0]
    checks = {}
    checks['depression_gamma2_eq_t1'] = (g2 == t1)
    checks['s2_s3_s4_from_roots'] = (s[0] == g1 - t1 ** 2 and s[1] == g0 - t1 * g1 and s[2] == -t1 * g0)
    checks['nu_eq_4zeta0'] = (nu == 4 * zeta0)
    U = [sum(a * b for a, b in zip(zetaW, u[d])) for d in range(3)]
    Z = [sum(zetaW[i] * N[d][i][j] * zetaW[j] for i in range(9) for j in range(9)) for d in range(3)]
    checks['U2_eq_2zeta0t1'] = (U[0] == 2 * zeta0 * t1)
    checks['U3_eq_2/3zeta0(g1+t1^2)'] = (U[1] == Q(2, 3) * zeta0 * (g1 + t1 ** 2))
    checks['Z2_eq_-6zeta0^2'] = (Z[0] == -6 * zeta0 ** 2)
    checks['Z3_eq_-8/3zeta0^2t1'] = (Z[1] == -Q(8, 3) * zeta0 ** 2 * t1)
    # polynomial matrices in t
    Hp = poly_matrix(F, 2)
    # zeta^T H zeta == 0 and zeta^T H x == 3 nu Gamma as polynomials
    zHz = [Q(0)]
    for i in range(10):
        for j in range(10):
            zHz = padd(zHz, pscale(Hp[i][j], zeta[i] * zeta[j]))
    checks['zeta_H_zeta_zero'] = is_zero(zHz)
    xpoly = [[Q(0), Q(1)]] + [[Q(1)]] + [[Q(0)]] * 8   # x(t) = t e_t + e_1
    zHx = [Q(0)]
    for i in range(10):
        for j in range(10):
            zHx = padd(zHx, pscale(pmul(Hp[i][j], xpoly[j]), zeta[i]))
    checks['zeta_H_x_eq_3nuGamma'] = (ptrim(zHx) == ptrim(pscale(Gamma, 3 * nu)))
    # kernel vector k(t) = 3 z(t) zeta - nu x(t), check Gamma | H k
    k = [psub(pscale(zpoly, 3 * zeta[i]), pscale(xpoly[i], nu)) for i in range(10)]
    Hk_ok = True
    for i in range(10):
        acc = [Q(0)]
        for j in range(10):
            acc = padd(acc, pmul(Hp[i][j], k[j]))
        Hk_ok &= is_zero(pmod(acc, Gamma))
    checks['Gamma_divides_Hk'] = Hk_ok
    k0 = k[0]; kW = k[1:]
    checks['k0_eq_-zeta0(t+3t1)'] = (ptrim(k0) == ptrim([-3 * zeta0 * t1, -zeta0]))
    # scalar polynomials from equations(): reconstruct A, J2, J3, Q22, DH, T2 by interpolation
    nodes = list(range(21))
    vals = {kk: [] for kk in ('A', 'J2', 'J3', 'Q22', 'DH', 'T2')}
    adjH_nodes = []
    for t in nodes:
        Ht = F.hess(line_point(t))
        B = [row[1:] for row in Ht[1:]]; v = Ht[0][1:]
        aB = adj(B); aH = adj(Ht); adjH_nodes.append(aH)
        vals['A'].append(det(B))
        vals['J2'].append(-sum(u[0][i] * aB[i][j] * v[j] for i in range(9) for j in range(9)))
        vals['J3'].append(-sum(u[1][i] * aB[i][j] * v[j] for i in range(9) for j in range(9)))
        vals['Q22'].append(sum(u[0][i] * aH[i + 1][j + 1] * u[0][j] for i in range(9) for j in range(9)))
        vals['DH'].append(det(Ht))
        vals['T2'].append(sum(aH[i + 1][j + 1] * N[0][j][i] for i in range(9) for j in range(9)))
    P = {kk: interp([Q(t) for t in nodes], vs) for kk, vs in vals.items()}
    adjH = [[interp([Q(t) for t in nodes], [adjH_nodes[m][i][j] for m in range(21)]) for j in range(10)] for i in range(10)]
    # vanishing orders at t1 (rank-2 point): z^7 | A, z^6 | J_d, z^7 | T2, z^8 | DH
    def order_at_t1(poly):
        n = 0; cur = ptrim(poly)
        while not is_zero(cur):
            qq, rr = pdivmod(cur, zpoly)
            if not is_zero(rr):
                break
            cur = qq; n += 1
        return n
    checks['orders_at_t1'] = {kk: order_at_t1(P[kk]) for kk in P}
    checks['orders_ok'] = (checks['orders_at_t1']['A'] >= 7 and checks['orders_at_t1']['J2'] >= 6
                           and checks['orders_at_t1']['J3'] >= 6 and checks['orders_at_t1']['T2'] >= 7
                           and checks['orders_at_t1']['DH'] >= 8 and checks['orders_at_t1']['Q22'] >= 7)
    # (F4) at roots of Gamma: k0^2 adj(H) == A k k^T mod Gamma
    A = P['A']
    k0sq = pmul(k0, k0)
    f4 = True
    for i in range(10):
        for j in range(10):
            f4 &= is_zero(pmod(psub(pmul(k0sq, adjH[i][j]), pmul(A, pmul(k[i], k[j]))), Gamma))
    checks['k0^2adjH_eq_AkkT_mod_Gamma'] = f4
    uk = [[Q(0)] for _ in range(3)]
    for d in range(3):
        acc = [Q(0)]
        for i in range(9):
            acc = padd(acc, pscale(kW[i], u[d][i]))
        uk[d] = acc
    kNk = []
    for d in range(3):
        acc = [Q(0)]
        for i in range(9):
            for j in range(9):
                acc = padd(acc, pscale(pmul(kW[i], kW[j]), N[d][i][j]))
        kNk.append(acc)
    checks['J2k0_eq_Auk2_mod_Gamma'] = is_zero(pmod(psub(pmul(P['J2'], k0), pmul(A, uk[0])), Gamma))
    checks['J3k0_eq_Auk3_mod_Gamma'] = is_zero(pmod(psub(pmul(P['J3'], k0), pmul(A, uk[1])), Gamma))
    checks['T2k0^2_eq_AkN2k_mod_Gamma'] = is_zero(pmod(psub(pmul(P['T2'], k0sq), pmul(A, kNk[0])), Gamma))
    checks['Q22k0^2_eq_Auk2^2_mod_Gamma'] = is_zero(pmod(psub(pmul(P['Q22'], k0sq), pmul(A, pmul(uk[0], uk[0]))), Gamma))
    # k^T H' k with H' = [[24t, 4u2^T],[4u2, 4tN2+6N3]]
    tpoly = [Q(0), Q(1)]
    kHk = padd(padd(pscale(pmul(tpoly, k0sq), 24), pscale(pmul(k0, uk[0]), 8)),
               padd(pscale(pmul(tpoly, kNk[0]), 4), pscale(kNk[1], 6)))
    DHprime = pderiv(P['DH'])
    checks["DH'k0^2_eq_AkH'k_mod_Gamma"] = is_zero(pmod(psub(pmul(DHprime, k0sq), pmul(A, kHk)), Gamma))
    # closed forms of the invariant polynomials predicted by the family relations
    nu_ = nu
    uk2_pred = psub(pscale(zpoly, 3 * U[0]), [nu_ * s[0]])
    uk3_pred = psub(pscale(zpoly, 3 * U[1]), [nu_ * s[1]])
    checks['uk_closed_forms'] = (ptrim(uk[0]) == ptrim(uk2_pred) and ptrim(uk[1]) == ptrim(uk3_pred))
    kN2_pred = padd(padd(pscale(pmul(zpoly, zpoly), 9 * Z[0]), pscale(zpoly, -6 * nu_ * U[0])), [nu_ ** 2 * s[0]])
    kN3_pred = padd(padd(pscale(pmul(zpoly, zpoly), 9 * Z[1]), pscale(zpoly, -6 * nu_ * U[1])), [nu_ ** 2 * s[1]])
    checks['kNk_closed_forms'] = (ptrim(kNk[0]) == ptrim(kN2_pred) and ptrim(kNk[1]) == ptrim(kN3_pred))
    # genericity at this point
    pprime = pderiv(p)
    checks['p_squarefree'] = (len(pgcd(p, pprime)) == 1)
    checks['gcd(A,Gamma)=1'] = (len(pgcd(A, Gamma)) == 1)
    checks['gcd(k0,Gamma)=1'] = (len(pgcd(k0, Gamma)) == 1)
    checks['Gamma(t1)!=0'] = (pev(Gamma, t1) != 0)
    checks['zeta0!=0'] = (zeta0 != 0)
    # ---- rebuild E from the root-local model: only A mod Gamma, roots, zeta0 ----
    inv_z = pinv_mod(zpoly, Gamma)
    inv_k0 = pinv_mod(k0, Gamma)
    inv_pp = pinv_mod(pprime, Gamma)
    Am = pmod(A, Gamma)
    def red(*fs):
        acc = [Q(1)]
        for f in fs:
            acc = pmod(pmul(acc, f), Gamma)
        return pad(acc, 3)
    rA = red(Am, inv_z)
    rJ2 = red(Am, uk2_pred, inv_k0, inv_z)
    rJ3 = red(Am, uk3_pred, inv_k0, inv_z)
    rQ = red(Am, uk2_pred, uk2_pred, inv_k0, inv_k0, inv_z)
    kHk_pred = padd(padd(pscale(pmul(tpoly, k0sq), 24), pscale(pmul(k0, uk2_pred), 8)),
                    padd(pscale(pmul(tpoly, kN2_pred), 4), pscale(kN3_pred, 6)))
    rT2 = red(Am, kN2_pred, inv_k0, inv_k0, inv_z)
    qD = red(Am, kHk_pred, inv_k0, inv_k0, inv_pp)
    r2 = red(qD, inv_z)
    Spoly = pad(pmul(pmul(p, zpoly), r2), 8)
    R1 = lambda r: r[0] - t1 * r[1]
    R2 = lambda r: r[1] - t1 * r[2]
    R3 = lambda r: r[2]
    E_model = [R1(rA), s[0] * R3(rA), R2(rJ2), R3(rJ3), R3(rQ), Spoly[3], s[0] * Spoly[5],
               s[1] * Spoly[6], s[2] * Spoly[7], R1(rT2), s[0] * R3(rT2)]
    checks['E_model_equals_E_true'] = (E_model == E_true)
    checks['E_true_all_nonzero'] = all(e != 0 for e in E_true)
    checks['psi_true'] = str(sum(a * b for a, b in zip(W, E_true)))
    ok = all(v is True for kk, v in checks.items() if isinstance(v, bool))
    emit('part_a', label=label, all_checks_pass=ok, checks={kk: (v if not isinstance(v, dict) else v) for kk, v in checks.items()})
    return dict(label=label, L=L, t1=str(t1), zeta0=str(zeta0), nu=str(nu), Gamma=[str(x) for x in Gamma],
                checks=checks, all_checks_pass=ok)


# ---- Part B: symbolic identity, denominator-free in a sparse polynomial ring ----
def part_b():
    """Model: roots t2,t3,t4 of Gamma (t1 = -(t2+t3+t4)), zeta0 free, A_i = A(t_i) free.
    Every E_j is sum_i A_i * E_j^(i) / D_i with D_i = k0_i^2 z_i^2 G_i^2 and E_j^(i) a
    polynomial in (t2,t3,t4,zeta0).  Psi == 0 iff sum_j w_j E_j^(i) == 0 for each i."""
    from sympy import QQ
    from sympy.polys.rings import ring
    R, t2, t3, t4, z0 = ring('t2,t3,t4,z0', QQ)
    roots = [t2, t3, t4]
    t1 = -(t2 + t3 + t4)
    g1 = t2 * t3 + t2 * t4 + t3 * t4; g0 = -t2 * t3 * t4
    s2 = g1 - t1 ** 2; s3 = g0 - t1 * g1; s4 = -t1 * g0
    nu = 4 * z0
    U2 = 2 * z0 * t1; U3 = QQ(2, 3) * z0 * (g1 + t1 ** 2)
    Z2 = -6 * z0 ** 2; Z3 = -QQ(8, 3) * z0 ** 2 * t1
    # (t - t1)^2 Gamma(t) coefficients, low degree first
    def pmul_r(a, b):
        out = [R.zero] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return out
    zc = [-t1, R.one]
    Gc = [g0, g1, t1, R.one]
    pz2G = pmul_r(pmul_r(zc, zc), Gc)          # degree 5
    per_root = []
    for i in range(3):
        j, k = [m for m in range(3) if m != i]
        ti, tj, tk = roots[i], roots[j], roots[k]
        zi = ti - t1
        Gi = (ti - tj) * (ti - tk)
        k0 = 3 * zi * z0 - nu * ti
        uk2 = 3 * zi * U2 - nu * s2
        uk3 = 3 * zi * U3 - nu * s3
        kN2 = 9 * zi ** 2 * Z2 - 6 * nu * zi * U2 + nu ** 2 * s2
        kN3 = 9 * zi ** 2 * Z3 - 6 * nu * zi * U3 + nu ** 2 * s3
        kHk = 24 * ti * k0 ** 2 + 8 * k0 * uk2 + 4 * ti * kN2 + 6 * kN3
        c = [tj * tk, -(tj + tk), R.one]      # (t - tj)(t - tk)
        # remainder coefficients times D_i = k0^2 zi^2 Gi^2
        rA = [cm * k0 ** 2 * zi * Gi for cm in c]
        rJ2 = [uk2 * cm * k0 * zi * Gi for cm in c]
        rJ3 = [uk3 * cm * k0 * zi * Gi for cm in c]
        rQ = [uk2 ** 2 * cm * zi * Gi for cm in c]
        rT2 = [kN2 * cm * zi * Gi for cm in c]
        r2 = [kHk * cm for cm in c]
        S = [R.zero] * 8
        for m1, x in enumerate(pz2G):
            for m2, y in enumerate(r2):
                S[m1 + m2] += x * y
        R1 = lambda r: r[0] - t1 * r[1]
        R2 = lambda r: r[1] - t1 * r[2]
        R3 = lambda r: r[2]
        E = [R1(rA), s2 * R3(rA), R2(rJ2), R3(rJ3), R3(rQ), S[3], s2 * S[5], s3 * S[6], s4 * S[7],
             R1(rT2), s2 * R3(rT2)]
        per_root.append(E)
    psi_zero = all(sum((wj * e for wj, e in zip(W, E)), R.zero) == R.zero for E in per_root)
    kap_zero = all(sum((kj * e for kj, e in zip(KAPPA, E)), R.zero) == R.zero for E in per_root)
    emit('part_b_identity', psi_identically_zero=psi_zero, kappa_identically_zero=kap_zero,
         terms_per_root=[[len(e.terms()) for e in E] for E in per_root])
    # exact kernel of the model: c with sum_j c_j E_j^(i) == 0 for all i  <=>  c annihilates every
    # monomial-coefficient row.
    rows = []
    for E in per_root:
        monos = set()
        for e in E:
            monos.update(dict(e.terms()).keys())
        for m in sorted(monos):
            rows.append([Q(str(dict(e.terms()).get(m, QQ(0)))) for e in E])
    M = qm(rows)
    Rr, rk = M.rref()
    piv = []; j = 0
    for i in range(rk):
        while Rr[i, j] == 0:
            j += 1
        piv.append(j)
    ker = []
    for j in range(11):
        if j not in piv:
            v = [Q(0)] * 11; v[j] = Q(1)
            for i, kk in enumerate(piv):
                v[kk] = -q(Rr[i, j])
            ker.append(v)
    span_ok = False
    if rk == 9:
        Mk = qm([[Q(x) for x in KAPPA], [Q(x) for x in W]] + ker)
        span_ok = (Mk.rank() == 2)
    emit('part_b_kernel', model_rank=rk, coefficient_rows=len(rows), kernel=[[str(x) for x in v] for v in ker],
         kernel_is_span_kappa_w=span_ok)
    return dict(psi_identically_zero=psi_zero, kappa_identically_zero=kap_zero, model_rank=rk,
                coefficient_rows=len(rows), kernel=[[str(x) for x in v] for v in ker],
                kernel_is_span_kappa_w=span_ok)


def main():
    assert all(os.environ.get(k) == '1' for k in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'])
    OUT.mkdir(parents=True, exist_ok=True)
    b1704 = json.loads(Path('../B15-04/results/b17_04/padding_points.json').read_text())
    pts = [('b17_04_seed_170400', b1704[0]['L'])]
    rg = random.Random(180500)
    L = rand_matrix(rg, 10, 10, 10 ** 4)
    assert int(fmpz_mat(L).det()) != 0
    pts.append(('b18_05_seed_180500', L))
    rg = random.Random(180999)
    L = rand_matrix(rg, 10, 10, 30)
    assert int(fmpz_mat(L).det()) != 0
    pts.append(('b18_05_seed_180999', L))
    A_res = [part_a(L, label) for label, L in pts]
    (OUT / 'proof_certificate.json').write_text(json.dumps(dict(part_a=A_res, part_b='NOT REACHED'), indent=1) + chr(10))
    B_res = part_b()
    out = dict(part_a=A_res, part_b=B_res, wall_seconds=time.perf_counter() - START)
    (OUT / 'proof_certificate.json').write_text(json.dumps(out, indent=1) + '\n')
    emit('complete', wall=out['wall_seconds'], all_a=all(r['all_checks_pass'] for r in A_res),
         psi_zero=B_res['psi_identically_zero'])


if __name__ == '__main__':
    main()
