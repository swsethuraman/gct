#!/usr/bin/env python3
"""Session 73 -- the a-ladder of (3 delta - 17, 7, 2^5) at n = 3 by two independent
engines, and the stable value a_inf((7, 2^5)) of Proposition S at n = 3 by a third.

  a(delta)  : tools/verify/pleth.ambient_multiplicity (from-scratch box DP, Weyl alternation)
              and analysis/wk9_s42_census.a_weyl (the house Kostant tail DP), delta = 8..20;
              the house engine alone to delta = 40.
  a_inf     : mult of S_tail(C^6) in Sym(Sym^2 C^6 + Sym^3 C^6)
            = sum_w sgn(w) K_inf(tail + rho' - w(rho')),
              K_inf(mu) = # multisets of monomials of degree 2 or 3 in 6 variables with
              exponent sum mu (unbounded knapsack in the box tail + rho').

Writes results/s73_aladder.json.
"""
import itertools
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))


def exps(n, r):
    if r == 1:
        return [(n,)]
    return [(a,) + rest for a in range(n, -1, -1) for rest in exps(n - a, r - 1)]


def sgn(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def a_inf(tail, degrees=(2, 3)):
    r = len(tail)
    rho = tuple(range(r - 1, -1, -1))
    box = tuple(tail[i] + rho[i] for i in range(r))
    monos = [al for d in degrees for al in exps(d, r)]
    T = np.zeros(tuple(b + 1 for b in box), dtype=object)
    T[(0,) * r] = 1
    states = list(itertools.product(*[range(b + 1) for b in box]))      # lexicographic = increasing
    for al in monos:
        if any(al[i] > box[i] for i in range(r)):
            continue
        for mu in states:                                               # mu - al precedes mu: unbounded
            src = tuple(mu[i] - al[i] for i in range(r))
            if all(x >= 0 for x in src):
                T[mu] += T[src]
    tot = 0
    for w in itertools.permutations(range(r)):
        mu = tuple(tail[i] + rho[i] - rho[w[i]] for i in range(r))
        if any(x < 0 for x in mu):
            continue
        tot += sgn(w) * int(T[mu])
    return tot


def main():
    from pleth import ambient_multiplicity
    from wk9_s42_census import a_weyl
    out = dict(family="(3 delta - 17, 7, 2^5), n = 3, r = 7", a_two_engines={}, a_house_to_40={}, secs={})
    cache = {}
    for d in range(8, 21):
        lam = (3 * d - 17, 7, 2, 2, 2, 2, 2)
        t = time.time()
        a1 = ambient_multiplicity(lam, d, n=3)
        a2 = a_weyl(lam, d, 3, cache)
        out['a_two_engines'][d] = dict(lam=list(lam), pleth=a1, house=a2, agree=(a1 == a2))
        out['secs'][d] = round(time.time() - t, 1)
        print(d, lam, a1, a2, flush=True)
    for d in range(21, 41):
        lam = (3 * d - 17, 7, 2, 2, 2, 2, 2)
        out['a_house_to_40'][d] = a_weyl(lam, d, 3, cache)
    t = time.time()
    out['a_inf'] = dict(tail=[7, 2, 2, 2, 2, 2], degrees=[2, 3], value=a_inf((7, 2, 2, 2, 2, 2)), secs=round(time.time() - t, 1))
    print("a_inf((7,2^5)) =", out['a_inf']['value'])
    with open(os.path.join(ROOT, 'results', 's73_aladder.json'), 'w') as fh:
        json.dump(out, fh, indent=1)


if __name__ == '__main__':
    main()
