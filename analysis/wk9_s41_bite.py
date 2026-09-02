#!/usr/bin/env python3
"""
Session 41 -- the sceptical / referee battery (wk9_s36_bite.py adapted to the s41 pickles) for a cell with mult < a.

Given a banked cell (pickle from wk9_s41_cell.py), for each prime:
  1. recompute the evaluation rows on the HWV kernel at 3a+24 FRESH points of
     the biting side (seed 907) and take U = null(ev . K): the vanishing HWVs;
  2. expand each vanishing HWV to full monomial coordinates and EXHIBIT it
     (support size, a few leading coefficients, saved in full);
  3. evaluate the vanishing HWV at four independent point families, each built
     by a code path that does NOT go through wk8_s30_core.restrict():
       (a) true padded permanent  x0 . per_3(X), X a 3x3 matrix of random
           linear forms in s_1..s_r, expanded symbolically (fresh seed);
       (b) l . (random cubic)  -- the reducible locus with an arbitrary cubic;
       (c) generic quartics;
       (d) det_4 pencils.
     Expected for a pad bite: (a) = 0 at every point; (c), (d) nonzero.
     (b) = 0 means the equation is a REDUCIBILITY equation (l . anything);
     (b) != 0 would mean it sees the permanent's structure (only possible at
     r >= 6, docs/s35_review.md section 1).

usage: python3 wk9_s41_bite.py <cell pickle> <side det|pad> [npts]
"""
import sys, os, pickle, random, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import (orbit_setup, point_rows, expand, exps, DET4, N_DET,
                             PAD34, N_PAD, P1, P2, log, nmod_mat)

# ---- a tiny multivariate polynomial class (dict exponent-tuple -> int)
def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, 0) + v
        if o[k] == 0: del o[k]
    return o
def pmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            o[k] = o.get(k, 0) + va * vb
    return {k: v for k, v in o.items() if v}
def linform(rnd, r, bound):
    return {tuple(1 if t == i else 0 for t in range(r)): rnd.randint(-bound, bound) for i in range(r)}
def per3(X):
    tot = {}
    for perm in itertools.permutations(range(3)):
        term = {tuple([0] * len(next(iter(X[0][0])))): 1}
        for i in range(3): term = pmul(term, X[i][perm[i]])
        tot = padd(tot, term)
    return tot
def random_form(rnd, r, deg, bound):
    return {al: rnd.randint(-bound, bound) for al in exps(deg, r)}

def family(kind, rnd, r, bound=40):
    if kind == 'truepad':
        l = linform(rnd, r, bound)
        X = [[linform(rnd, r, bound) for _ in range(3)] for _ in range(3)]
        return pmul(l, per3(X))
    if kind == 'l_cubic':
        return pmul(linform(rnd, r, bound), random_form(rnd, r, 3, bound))
    if kind == 'generic':
        return random_form(rnd, r, 4, bound)
    if kind == 'det':
        # det_4(sum s_i A_i) expanded symbolically
        As = [[rnd.randint(-bound, bound) for _ in range(16)] for _ in range(r)]
        M = [[{tuple(1 if t == i else 0 for t in range(r)): As[i][4 * a + b] for i in range(r)}
              for b in range(4)] for a in range(4)]
        tot = {}
        for perm in itertools.permutations(range(4)):
            sgn = 1
            for i in range(4):
                for j in range(i + 1, 4):
                    if perm[i] > perm[j]: sgn = -sgn
            term = {tuple([0] * r): sgn}
            for i in range(4): term = pmul(term, M[i][perm[i]])
            tot = padd(tot, term)
        return tot
    raise ValueError(kind)

def eval_full(full, coeffs, A, prime):
    tot = 0
    for m, cf in full.items():
        v = cf
        for k in m:
            c = coeffs.get(A[k], 0) % prime
            if c == 0: v = 0; break
            v = v * c % prime
        tot = (tot + v) % prime
    return tot

if __name__ == '__main__':
    out = pickle.load(open(sys.argv[1], 'rb'))
    side = sys.argv[2]
    npts = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    lam = out['lam']; r = len(lam); delta = out.get('delta', sum(lam) // 4); a = out['a']; n = 4
    from wk9_s36_red import is_red
    A = exps(n, r)
    basis, vecs, group = orbit_setup(n, r, delta, lam, verbose=False)
    assert len(vecs) == out['n_chi']
    forms = dict(det=(DET4, N_DET), pad=(PAD34, N_PAD))
    f, N = forms[side]
    report = [f"# Sceptical battery — cell {lam}, delta {delta}, side {side}: mult_{side} = {out['mult_'+side]} < a = {a}\n"]
    for prime in (P1, P2):
        kern = out['per_prime'][prime]['kern']
        K = 3 * a + 24
        ev = point_rows(f, N, n, r, basis, vecs, K, 907, 40, prime)
        nchi = len(kern[0])
        rows = [[sum(e[i] * kv[i] for i in range(nchi) if kv[i]) % prime for kv in kern] for e in ev]
        Mev = nmod_mat(K, a, [v for rw in rows for v in rw], prime)
        rk = Mev.rank()
        X, nul = Mev.nullspace()
        report.append(f"\n## prime {prime}: rank of {K} fresh {side}-point evaluations on the HWV space = {rk} "
                      f"(mult_{side} confirmed = {rk}); vanishing subspace dim {nul}\n")
        for j in range(nul):
            u = [int(X[i, j]) for i in range(a)]
            vchi = [sum(u[k] * kern[k][i] for k in range(a)) % prime for i in range(nchi)]
            full = expand(vecs, vchi, prime)
            # normalise: leading (smallest multiset) coefficient = 1
            m0 = min(full); inv = pow(full[m0], prime - 2, prime)
            full = {m: v * inv % prime for m, v in full.items()}
            # signed representative for readability
            def srep(v): return v if v <= prime // 2 else v - prime
            report.append(f"### vanishing HWV #{j+1}: support {len(full)} of N_S = {len(basis)} monomials "
                          f"(chi-coordinates nonzero: {sum(1 for v in vchi if v)} of {nchi}); normalised at its first monomial\n")
            items = sorted(full.items())[:8]
            for m, v in items:
                report.append(f"- `{' '.join('c'+str(A[k]) for k in m)}` : {srep(v)}")
            report.append("")
            fn = os.path.join(HERE, '..', 'results', 's41_cells',
                              f"{'_'.join(map(str, lam))}_d{delta}_{side}_p{prime}_vec{j+1}.txt")
            os.makedirs(os.path.dirname(fn), exist_ok=True)
            with open(fn, 'w') as fh:
                fh.write(f"# weight {lam} delta {delta} HWV vanishing on the {side} side, mod {prime}; "
                         f"monomial = multiset of exponent tuples alpha of c_alpha (coefficient of x^alpha / alpha!)\n")
                for m, v in sorted(full.items()):
                    fh.write(f"{[A[k] for k in m]} {srep(v)}\n")
            report.append(f"(full vector: `results/s41_cells/{os.path.basename(fn)}`)\n")
            nstar = sum(1 for m in full if is_red(m, A, r))
            report.append(f"(★) check: {nstar} of {len(full)} monomials satisfy the reducible-locus condition — "
                          + ("**the vector lies in I(X_6) by (★): a reducibility equation**" if nstar == len(full)
                             else "**the vector does NOT lie in I(X_6)** (some monomial has, for some variable, every factor touching it)") + "\n")
            report.append("| family (independent symbolic construction, seed 2036) | points | nonzero values |")
            report.append("|---|---|---|")
            for kind in ('truepad', 'l_cubic', 'generic', 'det'):
                rnd = random.Random(2036 + prime % 97)
                nz = 0
                for _ in range(npts):
                    F = family(kind, rnd, r)
                    if eval_full(full, F, A, prime): nz += 1
                report.append(f"| {kind} | {npts} | {nz} |")
            report.append("")
    txt = "\n".join(report)
    print(txt)
    fn = os.path.join(HERE, '..', 'results', 's41_cells', f"{'_'.join(map(str, lam))}_d{delta}_{side}_battery.md")
    open(fn, 'w').write(txt)
