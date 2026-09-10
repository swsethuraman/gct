#!/usr/bin/env python3
"""
B13-05 -- the top cells (ell(mu) = delta) of Sym^delta(Sym^3 C^delta) as catalecticant minors.

For a strict partition nu of delta, the shifted diagram S(nu) = {(i,j): 1<=i<=len(nu), i<=j<=i+nu_i-1}
has delta cells; lam = weight of the wedge of the quadratic monomials e_i e_j over S(nu)
(= Frobenius (nu | nu-1)), and mu = lam + (1^delta) is a top cell.  The highest-weight vector is

    h_mu(c) = det [ <c, e_i e_j e_k> ]_{(i,j) in S(nu), k = 1..delta},   <c, x^alpha> = alpha! c_alpha,

a delta x delta maximal minor of the catalecticant Cat_{1,2}(c): V -> Sym^2 V^* (rows = the shifted
diagram, columns = all delta variables).  Since a(mu, delta) = 1 at every top cell in range (census),
h_mu spans the weight-mu highest-weight space once it is a nonzero polynomial, and

    i(mu, delta) = 0  <=>  h_mu(per_3(sum s_i A_i)) != 0 at ONE pencil        (an exact integer determinant).

Validation (PREREG addendum A1): (a) at delta <= 5 the expanded polynomial is killed exactly by the house
raising operators (wk8_s30_core.build_R) and is nonzero; (b) nonvanishing at a random rational cubic at
every top cell delta <= 9; (c) at delta <= 6 the value at a per_3 pencil is nonzero (the record has I = 0).

usage: python3 analysis/wk13_b13_05_topcells.py [--dmax 9] [--out results/b13_05_topcells.json]
board_numbering: batch13
"""
import sys, os, time, json, random, argparse, itertools
from math import factorial
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flint import fmpz_mat, nmod_mat
from wk8_s30_core import exps, monomials, build_R, restrict, per_form, P1, P2
from wk8_s30_pleth import amb

PER3, N_PER3 = per_form(3)


def strict_partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: return [()]
    out = []
    for k in range(min(n, mx), 0, -1):
        for rest in strict_partitions(n - k, k - 1):
            out.append((k,) + rest)
    return out


def shifted_diagram(nu):
    return [(i, j) for i, part in enumerate(nu) for j in range(i, i + part)]     # 0-indexed cells (i <= j)


def weight_of_diagram(S, delta):
    lam = [0] * delta
    for (i, j) in S:
        lam[i] += 1; lam[j] += 1
    return tuple(lam)


def top_cell(nu, delta):
    S = shifted_diagram(nu)
    assert len(S) == delta
    lam = weight_of_diagram(S, delta)
    mu = tuple(x + 1 for x in lam)
    assert all(mu[i] >= mu[i + 1] for i in range(delta - 1)), (nu, mu)
    return S, lam, mu


def alpha_of(i, j, k, delta):
    a = [0] * delta; a[i] += 1; a[j] += 1; a[k] += 1
    return tuple(a)


def fact_alpha(alpha):
    f = 1
    for x in alpha: f *= factorial(x)
    return f


def det_matrix(S, delta, coeffs):
    """the delta x delta integer matrix [alpha! c_alpha] with rows S (shifted diagram), columns k."""
    rows = []
    for (i, j) in S:
        row = []
        for k in range(delta):
            al = alpha_of(i, j, k, delta)
            row.append(fact_alpha(al) * int(coeffs.get(al, 0)))
        rows.append(row)
    return rows


def det_exact(rows):
    d = len(rows)
    M = fmpz_mat(d, d, [x for r in rows for x in r])
    return int(M.det())


def pencil(delta, rnd, bound):
    return [[rnd.randint(-bound, bound) for _ in range(9)] for _ in range(delta)]


def per3_coeffs(As, delta):
    return restrict(PER3, N_PER3, 3, delta, As)


def random_cubic(delta, rnd, bound):
    return {al: rnd.randint(-bound, bound) for al in exps(3, delta)}


def expand_polynomial(S, delta):
    """h_mu as a dict {sorted tuple of exponent-vectors (multiset of delta cubic monomials): integer coefficient},
    by the Leibniz expansion of the determinant.  Only used for the small-delta exact HWV check."""
    poly = {}
    for perm in itertools.permutations(range(delta)):
        sgn = 1
        for a in range(delta):
            for b in range(a + 1, delta):
                if perm[a] > perm[b]: sgn = -sgn
        mons = []
        coef = sgn
        for r, (i, j) in enumerate(S):
            al = alpha_of(i, j, perm[r], delta)
            mons.append(al); coef *= fact_alpha(al)
        key = tuple(sorted(mons))
        poly[key] = poly.get(key, 0) + coef
    return {k: v for k, v in poly.items() if v}


def hwv_check(S, mu, delta):
    """express h_mu in the house monomial basis of the weight-mu space and apply the house raising rows exactly."""
    poly = expand_polynomial(S, delta)
    E = exps(3, delta); idx = {a: k for k, a in enumerate(E)}          # resolve letters by index in THIS module's ordering
    basis, R = build_R(3, delta, delta, mu)
    pos = {m: c for c, m in enumerate(basis)}
    vec = [0] * len(basis)
    for key, v in poly.items():
        m = tuple(sorted(idx[al] for al in key))
        assert m in pos, ('monomial not in the weight-mu basis', key)
        vec[pos[m]] += v
    nz = sum(1 for x in vec if x)
    bad = 0
    for row in R:
        s = sum(int(v) * vec[c] for c, v in row.items())
        if s != 0: bad += 1
    return dict(N_S=len(basis), nonzero_coeffs=nz, raising_rows=len(R), rows_violated=bad, n_terms=len(poly))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dmax', type=int, default=9)
    ap.add_argument('--npts', type=int, default=9)
    ap.add_argument('--seed', type=int, default=11)
    ap.add_argument('--bound', type=int, default=40)
    ap.add_argument('--hwv-check-dmax', type=int, default=5)
    ap.add_argument('--out', default='results/b13_05_topcells.json')
    args = ap.parse_args()
    out = dict(board_numbering='batch13', session='B13-05', instrument='I5: top cells as catalecticant maximal minors',
               points='per_3 pencils, seed %d, box +-%d, %d pencils per cell; exact integer determinants (fmpz_mat.det), also reduced mod both house primes' % (args.seed, args.bound, args.npts),
               cells=[])
    for delta in range(1, args.dmax + 1):
        A = amb(delta, 3, delta)
        tops_census = sorted(mu for mu in A if len(mu) == delta)
        nus = strict_partitions(delta)
        cells = []
        for nu in nus:
            S, lam, mu = top_cell(nu, delta)
            cells.append((nu, S, lam, mu))
        mus = sorted(mu for _, _, _, mu in cells)
        assert mus == tops_census, ('top cells from strict partitions != census', delta, mus, tops_census)
        assert all(A[mu] == 1 for mu in mus), ('a != 1 at a top cell', delta)
        print(time.strftime('%H:%M:%S'), f'delta={delta}: {len(nus)} strict partitions = {len(tops_census)} census top cells, all a = 1', flush=True)
        rnd = random.Random(args.seed + 1000 * delta)
        for nu, S, lam, mu in cells:
            t0 = time.time()
            rec = dict(delta=delta, nu=list(nu), lam=list(lam), mu=list(mu), a=1, cells=S)
            # (b) nonvanishing at a random rational cubic
            c = random_cubic(delta, rnd, 10 ** 6)
            dv = det_exact(det_matrix(S, delta, c))
            rec['random_cubic_det_nonzero'] = bool(dv != 0)
            # (a) exact HWV check at small delta
            if delta <= args.hwv_check_dmax:
                rec['hwv_check'] = hwv_check(S, mu, delta)
            # the per_3 pencils
            vals = []
            for t in range(args.npts):
                As = pencil(delta, rnd, args.bound)
                cf = per3_coeffs(As, delta)
                d = det_exact(det_matrix(S, delta, cf))
                vals.append(dict(pencil=As, det=str(d), det_mod=[d % P1, d % P2]))
            nnz = sum(1 for v in vals if int(v['det']) != 0)
            rec['pencils'] = vals
            rec['n_pencils_nonzero'] = nnz
            rec['i'] = 0 if nnz > 0 else None
            rec['status'] = ('CERTIFIED i = 0: h_mu != 0 at %d of %d per_3 pencils (exact integer determinant)' % (nnz, args.npts)) if nnz > 0 \
                else 'CANDIDATE i = 1: h_mu = 0 at all pencils -- verification protocol, not a result'
            rec['secs'] = round(time.time() - t0, 2)
            out['cells'].append(rec)
            hc = rec.get('hwv_check')
            print(time.strftime('%H:%M:%S'), f'  nu={nu} mu={mu}: random-cubic nonzero={rec["random_cubic_det_nonzero"]}'
                  + (f' HWV-check N_S={hc["N_S"]} rows_violated={hc["rows_violated"]} nonzero_coeffs={hc["nonzero_coeffs"]}' if hc else '')
                  + f' | per3 pencils nonzero {nnz}/{args.npts} -> {rec["status"][:16]} [{rec["secs"]}s]', flush=True)
        with open(args.out, 'w') as f:
            json.dump(out, f, indent=0)
    print(time.strftime('%H:%M:%S'), 'wrote', args.out, flush=True)


if __name__ == '__main__':
    main()
