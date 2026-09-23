"""R27-K4: exact checks supporting the review of B26-10A section 2.3.

COMPUTED, exhaustive up to the stated bounds; no sampling, no randomness.

Check A (coefficient action). For a generic form F of degree d in N variables
with symbolic coefficients, the dual action of g = I + t E_ij on the
coefficient functional c_alpha is the coefficient of y^alpha in
F(y + t y_j e_i). Its t-derivative at t = 0 is compared with
    E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)  if alpha_j > 0, else 0.

Check B (R1/R2 of the length-restriction lemma). For every partition
lambda of d*delta with l(lambda) <= r, compare
  (i)  the weight-(lambda,0^(N-r)) coefficient monomials of Sym^delta(Sym^d C^N)
       with the pullbacks of the weight-lambda monomials of Sym^delta(Sym^d C^r);
  (ii) the dimensions of the simultaneous kernels of E_(i,i+1), i < N resp. i < r
       (highest-weight spaces), computed by exact rational rank.
"""
import itertools
import sys
from collections import Counter

import sympy as sp


def exps(N, d):
    """All exponent vectors of size d in N variables."""
    out = []
    for c in itertools.combinations_with_replacement(range(N), d):
        v = [0] * N
        for k in c:
            v[k] += 1
        out.append(tuple(v))
    return out


def check_A(N, d):
    y = sp.symbols(f"y0:{N}")
    t = sp.Symbol("t")
    A = exps(N, d)
    c = {a: sp.Symbol("c_" + "".join(map(str, a))) for a in A}
    F = sum(c[a] * sp.prod([y[k] ** a[k] for k in range(N)]) for a in A)
    bad = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            G = sp.expand(sp.diff(F.subs(y[i], y[i] + t * y[j]), t).subs(t, 0))
            P = sp.Poly(G, *y)
            for a in A:
                lhs = P.coeff_monomial(sp.prod([y[k] ** a[k] for k in range(N)]))
                if a[j] > 0:
                    b = list(a); b[i] += 1; b[j] -= 1
                    rhs = (a[i] + 1) * c[tuple(b)]
                else:
                    rhs = 0
                if sp.expand(lhs - rhs) != 0:
                    bad += 1
    return bad


def weight_basis(N, d, delta, mu):
    """Multisets of delta exponent vectors (size d, N vars) summing to mu."""
    A = [a for a in exps(N, d) if all(a[k] <= mu[k] for k in range(N))]
    res = []

    def rec(start, left, rem, cur):
        if left == 0:
            if all(x == 0 for x in rem):
                res.append(tuple(cur))
            return
        for idx in range(start, len(A)):
            a = A[idx]
            if all(a[k] <= rem[k] for k in range(N)):
                rec(idx, left - 1, [rem[k] - a[k] for k in range(N)], cur + [a])

    rec(0, delta, list(mu), [])
    return res


def raise_image(mono, i):
    """E_(i,i+1) applied, as a derivation, to a coefficient monomial."""
    out = Counter()
    cnt = Counter(mono)
    for a, m in cnt.items():
        if a[i + 1] == 0:
            continue
        b = list(a); b[i] += 1; b[i + 1] -= 1
        b = tuple(b)
        new = list(mono)
        new.remove(a)
        new.append(b)
        out[tuple(sorted(new))] += m * (a[i] + 1)
    return out


def hwv_dim(N, d, delta, mu):
    src = [tuple(sorted(m)) for m in weight_basis(N, d, delta, mu)]
    if not src:
        return 0, src
    rows = []
    for i in range(N - 1):
        if mu[i + 1] == 0:
            # no factor has a positive (i+1)-exponent, so E_(i,i+1) kills the space
            continue
        tgt = list(mu); tgt[i] += 1; tgt[i + 1] -= 1
        tb = {tuple(sorted(m)): k for k, m in enumerate(weight_basis(N, d, delta, tgt))}
        block = [[0] * len(src) for _ in tb]
        for col, m in enumerate(src):
            for img, coef in raise_image(m, i).items():
                block[tb[img]][col] += coef
        rows.extend(block)
    if not rows:
        return len(src), src
    M = sp.Matrix(rows)
    return len(src) - M.rank(), src


def partitions(n, maxlen, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    if maxlen == 0:
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, maxlen - 1, p):
            yield (p,) + rest


def check_B(N, d, r, delta):
    rows = []
    for lam in partitions(d * delta, r):
        mu_N = tuple(list(lam) + [0] * (N - len(lam)))
        mu_r = tuple(list(lam) + [0] * (r - len(lam)))
        hN, sN = hwv_dim(N, d, delta, mu_N)
        hr, sr = hwv_dim(r, d, delta, mu_r)
        pull = sorted(tuple(sorted(tuple(list(a) + [0] * (N - r)) for a in m)) for m in sr)
        same_basis = sorted(sN) == pull
        rows.append((lam, len(sN), len(sr), hN, hr, same_basis))
    return rows


def main():
    print("python", sys.version.split()[0], "sympy", sp.__version__)
    for (N, d) in [(3, 4), (3, 3), (2, 5)]:
        print(f"CHECK A N={N} d={d}: mismatches={check_A(N, d)}")
    total = 0
    fails = 0
    for (N, d, rs, deltas) in [(4, 4, (1, 2, 3), (1, 2, 3)),
                               (5, 4, (4,), (1, 2)),
                               (4, 3, (2, 3), (1, 2, 3)),
                               (5, 5, (3,), (1, 2))]:
        for r in rs:
            for delta in deltas:
                for lam, nN, nr, hN, hr, sb in check_B(N, d, r, delta):
                    total += 1
                    ok = (nN == nr) and (hN == hr) and sb
                    fails += (not ok)
                    print(f"B N={N} d={d} r={r} delta={delta} lam={lam} "
                          f"wt={nN}/{nr} hwv={hN}/{hr} basis_pullback={sb} {'OK' if ok else 'FAIL'}")
    print(f"CHECK B cells={total} failures={fails}")


if __name__ == "__main__":
    main()
