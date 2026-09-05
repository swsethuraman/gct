"""The ambient multiplicity a(lambda, delta) = mult of S_lambda(C^r) in
Sym^delta(Sym^n C^r), from scratch, by the Weyl alternation over weight
multiplicities:

    a(lambda) = sum_{w in S_r} sgn(w) * m( lambda + rho - w(rho) ),

rho = (r-1, ..., 1, 0), m(mu) = the number of multisets of size delta of
exponent tuples of degree n in r variables whose componentwise sum is mu (the
dimension of the mu-weight space of Sym^delta(Sym^n C^r)).  m is computed by an
unbounded-knapsack DP on a numpy array indexed by (count, mu), restricted to
the box 0 <= mu_i <= lambda_i + r - i that contains every mu the alternation
needs.  This shares nothing with analysis/wk8_s30_pleth.py (Frobenius
plethysm) or the census's Kostant tail DP.
"""
import itertools
import numpy as np


def exponent_tuples(n, r):
    if r == 1:
        return [(n,)]
    out = []
    for a in range(n, -1, -1):
        for rest in exponent_tuples(n - a, r - 1):
            out.append((a,) + rest)
    return out


def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def weight_multiplicities(n, r, delta, box):
    """T[k, mu] for 0 <= k <= delta and 0 <= mu_i <= box[i]; object dtype to keep
    the counts exact (they can exceed int64 for long weights)."""
    shape = (delta + 1,) + tuple(b + 1 for b in box)
    T = np.zeros(shape, dtype=object)
    T[(0,) + (0,) * r] = 1
    for alpha in exponent_tuples(n, r):
        if any(alpha[i] > box[i] for i in range(r)):
            continue
        src = tuple(slice(0, box[i] + 1 - alpha[i]) for i in range(r))
        dst = tuple(slice(alpha[i], box[i] + 1) for i in range(r))
        for k in range(delta):          # increasing k: multiplicities accumulate
            T[(k + 1,) + dst] += T[(k,) + src]
    return T


def ambient_multiplicity(lam, delta, n=4, max_entries=60_000_000):
    """a(lambda, delta); returns None if the DP box would exceed max_entries."""
    lam = tuple(lam)
    r = len(lam)
    if sum(lam) != n * delta or any(lam[i] < lam[i + 1] for i in range(r - 1)) or lam[-1] < 0:
        return 0
    rho = [r - 1 - i for i in range(r)]
    box = [lam[i] + rho[i] for i in range(r)]
    entries = (delta + 1)
    for b in box:
        entries *= (b + 1)
    if entries > max_entries:
        return None
    T = weight_multiplicities(n, r, delta, box)
    total = 0
    for w in itertools.permutations(range(r)):
        mu = [lam[i] + rho[i] - rho[w[i]] for i in range(r)]
        if any(x < 0 for x in mu):
            continue
        total += perm_sign(w) * int(T[(delta,) + tuple(mu)])
    return total


if __name__ == "__main__":
    import sys
    delta = int(sys.argv[1])
    lam = tuple(int(x) for x in sys.argv[2:])
    print(ambient_multiplicity(lam, delta))
