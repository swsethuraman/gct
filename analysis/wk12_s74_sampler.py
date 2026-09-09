#!/usr/bin/env python3
"""Session 74 -- a second filling sampler for the birth streams (one-columns first).

The house sampler (wk11_s69_circuit.random_filling) draws the two tall columns,
then the 2-columns weighted by remaining legs, and leaves the one-columns to the
remainder.  This one draws the one-column legs FIRST (each cell a letter chosen
uniformly among letters with legs left, at most three one-column legs per
letter so no letter is pure-u), then the tall columns with k shared letters
among the letters that still have legs, then the 2-columns as the house sampler
does.  Same shape lambda' = (h, h, 2^n2, 1^n1), same validity checks (Filling).
It is a different distribution over the same set of fillings; the certificate
at a rung (rank b_d at both primes) does not depend on which sampler produced a
basis element.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s69_circuit import Filling                                   # noqa: E402


def random_filling_ones_first(h, n, delta, n2, n1, rng, k=None, max_tries=2000, max_one_per_letter=3):
    assert 2 * h + 2 * n2 + n1 == n * delta
    letters = list(range(delta))
    for _ in range(max_tries):
        rem = [n] * delta
        one = []
        ones_of = [0] * delta
        ok = True
        for _c in range(n1):
            avail = [l for l in letters if rem[l] > 0 and ones_of[l] < max_one_per_letter]
            if not avail:
                ok = False
                break
            l = rng.choice(avail)
            one.append(l)
            rem[l] -= 1
            ones_of[l] += 1
        if not ok:
            continue
        cand = [l for l in letters if rem[l] > 0]
        if len(cand) < h:
            continue
        C1 = rng.sample(cand, h)
        for l in C1:
            rem[l] -= 1
        cand2 = [l for l in letters if rem[l] > 0]
        if k is None:
            if len(cand2) < h:
                continue
            C2 = rng.sample(cand2, h)
        else:
            sh_pool = [l for l in C1 if rem[l] > 0]
            rest = [l for l in cand2 if l not in C1]
            if len(sh_pool) < k or len(rest) < h - k:
                continue
            C2 = rng.sample(sh_pool, k) + rng.sample(rest, h - k)
            rng.shuffle(C2)
        for l in C2:
            rem[l] -= 1
        if min(rem) < 0:
            continue
        two = []
        for _e in range(n2):
            avail = [l for l in letters if rem[l] > 0]
            if len(avail) < 2:
                ok = False
                break
            w = [rem[l] for l in avail]
            a = rng.choices(avail, weights=w)[0]
            avail2 = [l for l in avail if l != a]
            w2 = [rem[l] for l in avail2]
            b = rng.choices(avail2, weights=w2)[0]
            rem[a] -= 1
            rem[b] -= 1
            two.append((a, b))
        if not ok or any(rem):
            continue
        rng.shuffle(one)
        try:
            return Filling(h, n, delta, C1, C2, two, one)
        except AssertionError:
            continue
    raise RuntimeError("no filling found (ones-first)")


def mutate_filling(F, rng, n_swaps=None, max_tries=200):
    """A random local move on a filling: swap the letters of two cells in different
    columns (keeping every column letter-distinct), n_swaps times.  Same shape,
    same content (four legs per letter); a different filling, in general a
    different class.  Used as a bandit arm once a rung has stalled: the rare
    directions may sit near classes already found."""
    if n_swaps is None:
        n_swaps = rng.choice([1, 1, 2, 3])
    cols = [list(F.C1), list(F.C2)] + [list(e) for e in F.two] + [[l] for l in F.one]
    done = 0
    for _ in range(max_tries):
        if done >= n_swaps:
            break
        c1, c2 = rng.sample(range(len(cols)), 2)
        i1 = rng.randrange(len(cols[c1]))
        i2 = rng.randrange(len(cols[c2]))
        a, b = cols[c1][i1], cols[c2][i2]
        if a == b or b in cols[c1] or a in cols[c2]:
            continue
        cols[c1][i1], cols[c2][i2] = b, a
        done += 1
    if done == 0:
        raise RuntimeError("no valid swap found")
    C1, C2 = cols[0], cols[1]
    two = [tuple(c) for c in cols[2:2 + F.n2]]
    one = [c[0] for c in cols[2 + F.n2:]]
    return Filling(F.h, F.n, F.delta, C1, C2, two, one)
