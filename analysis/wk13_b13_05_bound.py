#!/usr/bin/env python3
"""
B13-05 -- the orbit-stabiliser bound on the cubic side.

    X = closure(GL_9 . per_3) subset Sym^3 C^9,  D_r^{per_3} = its length-<=r part.
    H' = T x| F  subset  Stab_{GL_9}(per_3),  T = {A -> D1 A D2 : det D1 det D2 = 1},
    F = (S_3 x S_3) x| Z_2 (row perms, column perms, transpose), |F| = 72.

    mult(mu, delta) = a - i  <=  b(mu, delta) := dim S_mu(C^9)^{H'}          (PROVED, report S3)

    b(mu) = (1/72) sum_{f in F} tr(f | S_mu^T),
    tr(f | S_mu^T) = sum_{nu in MS(delta), f.nu = nu} < s_mu , prod_{cycles c of f} p_{l_c}[h_{nu_c}] >
      (Cauchy identity; nu = 3x3 magic square with line sums delta; nu_c the common value on cycle c)

    f = id term:  b_T(mu) = sum_{nu in MS(delta)} K_{mu, nu}   (Kostka numbers, independent DP)

Checks (PREREG_b13_05 section 2, I3.1 - I3.4) are in wk13_b13_05_checks.py.
board_numbering: batch13
"""
import sys, os, time, json, itertools, argparse
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import parts, zr, chi, amb

# ------------------------------------------------------------------ the finite group F on the 9 positions
def positions():
    return [(i, j) for i in range(3) for j in range(3)]     # p = 3 i + j


def group_F():
    """all 72 elements as permutations of range(9) (tuples: f[p] = image of p), with labels."""
    out = []
    for sig in itertools.permutations(range(3)):
        for tau in itertools.permutations(range(3)):
            for t in (0, 1):
                f = [0] * 9
                for i in range(3):
                    for j in range(3):
                        ii, jj = sig[i], tau[j]
                        if t: ii, jj = jj, ii
                        f[3 * i + j] = 3 * ii + jj
                out.append((tuple(f), dict(rows=sig, cols=tau, transpose=t)))
    fs = [f for f, _ in out]
    assert len(set(fs)) == 72
    # closure check: a group
    S = set(fs)
    for f in fs:
        for g in fs:
            assert tuple(f[g[p]] for p in range(9)) in S
    return out


def cycles_of(f):
    seen = [False] * 9; cyc = []
    for p in range(9):
        if seen[p]: continue
        c = []; q = p
        while not seen[q]:
            seen[q] = True; c.append(q); q = f[q]
        cyc.append(tuple(c))
    return cyc


def per3_invariance_check():
    """each element of F preserves per_3 as a polynomial (exact, on the monomial dict) -- the PROVED containment F subset Stab."""
    from wk8_s30_core import per_form
    P, N = per_form(3)
    for f, lab in group_F():
        Q = {}
        for beta, c in P.items():
            nb = [0] * 9
            for p in range(9): nb[f[p]] += beta[p]
            Q[tuple(nb)] = Q.get(tuple(nb), 0) + c
        assert Q == P, ('F element does not preserve per_3', lab)
    return True


def magic_squares(delta):
    out = []
    for a in range(delta + 1):
        for b in range(delta + 1 - a):
            c = delta - a - b
            for d in range(delta + 1):
                for e in range(delta + 1 - d):
                    ff = delta - d - e
                    g, h, i = delta - a - d, delta - b - e, delta - c - ff
                    if min(g, h, i) < 0: continue
                    if g + h + i != delta: continue
                    out.append((a, b, c, d, e, ff, g, h, i))
    return out


# ------------------------------------------------------------------ symmetric functions in the p-basis
def h_in_p(m):
    return {rho: Fraction(1, zr(rho)) for rho in parts(m)} if m > 0 else {(): Fraction(1)}


def pleth_by_p(F, ell):
    """p_ell[F]: every part k -> ell*k."""
    if ell == 1: return dict(F)
    return {tuple(ell * k for k in tau): c for tau, c in F.items()}


def mul_p(F, G):
    out = {}
    for x, cx in F.items():
        for y, cy in G.items():
            k = tuple(sorted(x + y, reverse=True))
            out[k] = out.get(k, Fraction(0)) + cx * cy
    return out


@lru_cache(maxsize=None)
def cycle_factor(ell, m):
    """p_ell[h_m] in the p-basis."""
    return tuple(sorted(pleth_by_p(h_in_p(m), ell).items()))


def trace_function(f, delta):
    """G_f = sum over magic squares nu fixed by f of prod_c p_{l_c}[h_{nu_c}], in the p-basis (dict tau -> Fraction),
    grouped by the multiset of (l_c, nu_c).  Also returns the number of fixed squares."""
    cyc = cycles_of(f)
    groups = {}
    nfix = 0
    for nu in magic_squares(delta):
        if any(nu[c[0]] != nu[q] for c in cyc for q in c): continue
        nfix += 1
        key = tuple(sorted((len(c), nu[c[0]]) for c in cyc))
        groups[key] = groups.get(key, 0) + 1
    G = {}
    for key, cnt in groups.items():
        prod = {(): Fraction(1)}
        for (ell, m) in key:
            prod = mul_p(prod, dict(cycle_factor(ell, m)))
        for tau, c in prod.items():
            G[tau] = G.get(tau, Fraction(0)) + cnt * c
    return G, nfix, groups


def inner_with_schur(mu, G):
    """<s_mu, G> for G in the p-basis: sum_tau G[tau] chi^mu(tau)."""
    tot = Fraction(0)
    for tau, c in G.items():
        if c: tot += c * chi(mu, tau)
    return tot


# ------------------------------------------------------------------ Kostka numbers (independent route for the f = id term)
@lru_cache(maxsize=None)
def kostka(mu, nu):
    """number of SSYT of shape mu and content nu (nu a tuple, processed from the last entry: remove a horizontal strip of size nu[-1])."""
    mu = tuple(x for x in mu if x)
    if not nu:
        return 1 if not mu else 0
    if sum(mu) != sum(nu): return 0
    k = nu[-1]; rest = nu[:-1]
    if k == 0: return kostka(mu, rest)
    tot = 0
    # enumerate lam subset mu with mu/lam a horizontal strip of size k: lam_i in [mu_{i+1}, mu_i]
    L = len(mu)
    def rec(i, left, cur):
        nonlocal tot
        if i == L:
            if left == 0: tot += kostka(tuple(cur), rest)
            return
        lo = mu[i + 1] if i + 1 < L else 0
        hi = mu[i]
        for lam_i in range(max(lo, hi - left), hi + 1):
            rec(i + 1, left - (hi - lam_i), cur + [lam_i])
    rec(0, k, [])
    return tot


def b_T_kostka(mu, delta, groups_id=None):
    """sum over magic squares of K_{mu, nu} = sum over entry-multisets m of (#squares with multiset m) * K_{mu, m}."""
    if groups_id is None:
        groups_id = {}
        for nu in magic_squares(delta):
            key = tuple(sorted(nu, reverse=True))
            groups_id[key] = groups_id.get(key, 0) + 1
    tot = 0
    for m, cnt in groups_id.items():
        # sort content ascending so that the recursion removes the largest entries last? any order is valid; use descending removed first = small last
        tot += cnt * kostka(tuple(mu), tuple(sorted(m)))
    return tot


# ------------------------------------------------------------------ dimension of S_mu(C^9) (hook-content) -- for the sum rule
def dim_schur(mu, n=9):
    mu = tuple(x for x in mu if x)
    if len(mu) > n: return 0
    num = Fraction(1)
    for i, row in enumerate(mu):
        for j in range(row):
            content = j - i
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(mu)) if mu[k] > j)
            num *= Fraction(n + content, arm + leg + 1)
    assert num.denominator == 1
    return int(num)


def burnside_count(f, delta):
    """#monomials of Sym^{3 delta}(C^9 (x) C^9) with magic right-content, fixed by f acting on the right index."""
    cyc = cycles_of(f)
    tot = 0
    for nu in magic_squares(delta):
        if any(nu[c[0]] != nu[q] for c in cyc for q in c): continue
        prod = 1
        for c in cyc:
            prod *= comb(nu[c[0]] + 8, 8)
        tot += prod
    return tot


# ------------------------------------------------------------------ the bound, per degree
def conjugacy_classes(elems):
    """classes of F under conjugation inside F; returns list of (representative, size)."""
    fs = [f for f, _ in elems]
    inv = {f: tuple(sorted(range(9), key=lambda p: f[p])) for f in fs}
    def conj(g, f):  # g f g^-1
        gi = inv[g]
        return tuple(g[f[gi[p]]] for p in range(9))
    seen = set(); classes = []
    for f in fs:
        if f in seen: continue
        cl = {conj(g, f) for g in fs}
        seen |= cl
        classes.append((f, len(cl)))
    assert sum(s for _, s in classes) == 72
    return classes


def bound_for_degree(delta, mus, verbose=True, want_id_char=False):
    """b(mu) for each mu in mus.  Returns dict mu -> dict(b, b_T, id_char (optional), traces per class)."""
    elems = group_F()
    classes = conjugacy_classes(elems)
    ident = tuple(range(9))
    # trace functions per class representative (f != id), and the id-term groups for the Kostka route
    tf = {}
    for f, size in classes:
        if f == ident: continue
        G, nfix, groups = trace_function(f, delta)
        tf[f] = (G, size, nfix, groups)
    groups_id = {}
    for nu in magic_squares(delta):
        key = tuple(sorted(nu, reverse=True)); groups_id[key] = groups_id.get(key, 0) + 1
    G_id = None
    if want_id_char:
        G_id, _, _ = trace_function(ident, delta)
    out = {}
    t0 = time.time()
    for k, mu in enumerate(mus):
        mu = tuple(mu)
        bT = b_T_kostka(mu, delta, groups_id)
        tot = Fraction(bT)
        traces = {'id': bT}
        for f, (G, size, nfix, groups) in tf.items():
            tr = inner_with_schur(mu, G)
            assert tr.denominator == 1, (mu, f, tr)
            traces[f] = int(tr)
            tot += size * tr
        b = tot / 72
        assert b.denominator == 1, ('b not integral', mu, delta, tot)
        rec = dict(b=int(b), b_T=int(bT), traces=traces)
        if want_id_char:
            v = inner_with_schur(mu, G_id); assert v.denominator == 1
            rec['id_char'] = int(v)
        out[mu] = rec
        if verbose and (k + 1) % 200 == 0:
            print(time.strftime('%H:%M:%S'), f'  delta={delta}: {k+1}/{len(mus)} weights, {time.time()-t0:.0f}s', flush=True)
    return out, classes


def all_partitions(n, maxrows):
    return [lam for lam in parts(n) if len(lam) <= maxrows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--deltas', default='1,2,3,4,5,6,7,8,9')
    ap.add_argument('--census', default='results/b13_05_census.json')
    ap.add_argument('--out', default='results/b13_05_bound.json')
    ap.add_argument('--all-mu', action='store_true', help='compute b for every mu |- 3 delta with <= 9 rows (needed for the sum rule)')
    ap.add_argument('--id-char', action='store_true', help='also compute the f=id term by the character route (check I3.1)')
    args = ap.parse_args()
    assert per3_invariance_check()
    print(time.strftime('%H:%M:%S'), 'F subset Stab(per_3): every one of the 72 elements preserves per_3 -- checked exactly', flush=True)
    cen = json.load(open(args.census))
    a_of = {(r['delta'], tuple(r['mu'])): r['a'] for r in cen['rows']}
    results = dict(board_numbering='batch13', session='B13-05', group="H' = T x| ((S3 x S3) x| Z2), |F| = 72",
                   formula='b(mu) = (1/72) sum_f tr(f|S_mu^T); tr(f|S_mu[nu]) = <s_mu, prod_c p_{l_c}[h_{nu_c}]>; f=id by Kostka',
                   degrees={})
    for delta in [int(x) for x in args.deltas.split(',')]:
        t0 = time.time()
        if args.all_mu:
            mus = all_partitions(3 * delta, 9)
        else:
            mus = sorted({tuple(r['mu']) for r in cen['rows'] if r['delta'] == delta})
        res, classes = bound_for_degree(delta, mus, want_id_char=args.id_char)
        # sum rule
        lhs = sum(res[mu]['b'] * dim_schur(mu) for mu in res) if args.all_mu else None
        rhs = sum(burnside_count(f, delta) for f, _ in group_F())
        assert rhs % 72 == 0
        rhs //= 72
        rows = []
        viol = []
        for mu in mus:
            a = a_of.get((delta, tuple(mu)), 0)
            b = res[mu]['b']
            rec = dict(mu=list(mu), ell=len(mu), a=a, b=b, b_T=res[mu]['b_T'], margin=b - a)
            if args.id_char: rec['id_char'] = res[mu]['id_char']
            rows.append(rec)
            if a > b: viol.append(rec)
        results['degrees'][delta] = dict(n_mu=len(mus), all_mu=args.all_mu, sum_rule_lhs=lhs, sum_rule_rhs=rhs,
                                          sum_rule_ok=(lhs == rhs) if lhs is not None else None,
                                          classes=[dict(rep=list(f), size=s) for f, s in classes],
                                          rows=rows, bites=[r for r in rows if r['a'] > r['b']], secs=round(time.time() - t0, 1))
        nb = len(results['degrees'][delta]['bites'])
        print(time.strftime('%H:%M:%S'), f'delta={delta}: {len(mus)} weights; sum rule lhs={lhs} rhs={rhs} ok={lhs == rhs if lhs is not None else "n/a"}; '
              f'cells with b < a: {nb}; {time.time()-t0:.1f}s', flush=True)
        for r in results['degrees'][delta]['bites']:
            print('   BITE:', r, flush=True)
        with open(args.out, 'w') as fh:
            json.dump(results, fh, indent=0)
    print(time.strftime('%H:%M:%S'), 'wrote', args.out, flush=True)


if __name__ == '__main__':
    main()
