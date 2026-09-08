#!/usr/bin/env python3
"""B_delta for Sol S5's twelve-channel precursor recursion (batch 11).

S5 claims the LMR source satisfies an exact one-block recursion

    (S^{lam_delta})^{K_delta} = sum over lam_delta/mu a horizontal 4-strip of
                                (S^mu)^{H_{delta-1}},
    M_{lam_delta} = ker(tau - I) on that precursor,

so the precursor dimension is

    B_delta = sum_{lam_delta/mu horizontal 4-strip} a_{delta-1}(mu)
            = [s_{lam_delta}] h_4 . h_{delta-1}[h_4].

S5 calls B_delta the decisive number and asks for it before any coding, with
gates: <= 10^4 GO, <= 10^5 GO with sparse matrices, <= 10^6 conditional,
> 10^6 the route is not the practical source engine.

This computes it with the repository's own census routine (a_weyl, the Kostant
tail alternation), independently of anything S5 ran, and checks a_delta <=
B_delta at every rung, which the recursion forces.
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
from wk9_s42_census import a_weyl


def lam_of(delta):
    """the LMR ladder rung: (4 delta - 31, 17, 2^7)."""
    return (4 * delta - 31, 17) + (2,) * 7


def horiz_strips(lam, k):
    """all mu with lam/mu a horizontal k-strip: mu interlaces lam, |lam|-|mu| = k."""
    r = len(lam)
    out = []

    def rec(i, cur, left):
        if i == r:
            if left == 0:
                mu = tuple(cur)
                while mu and mu[-1] == 0:
                    mu = mu[:-1]
                out.append(mu)
            return
        lo = lam[i + 1] if i + 1 < r else 0      # mu_i >= lam_{i+1}  (interlacing)
        hi = lam[i]                               # mu_i <= lam_i
        for v in range(max(lo, lam[i] - left), hi + 1):
            rec(i + 1, cur + [v], left - (lam[i] - v))

    rec(0, [], k)
    return sorted(set(out), reverse=True)


def main():
    deltas = [int(x) for x in sys.argv[1:]] or [12, 13, 14, 16, 18, 24]
    cache = {}
    rows = []
    for d in deltas:
        lam = lam_of(d)
        t0 = time.time()
        a_here = a_weyl(lam, d, 4, cache)
        mus = horiz_strips(lam, 4)
        parts = []
        for mu in mus:
            v = a_weyl(mu, d - 1, 4, cache)
            parts.append((mu, v))
        B = sum(v for _, v in parts)
        el = time.time() - t0
        rows.append(dict(delta=d, lam=list(lam), a=a_here, channels=len(mus),
                         B=B, parts=[[list(m), v] for m, v in parts], secs=round(el, 1)))
        print(f'delta={d:2d}  a={a_here:4d}  channels={len(mus):2d}  B={B}  '
              f'ratio B/a={B/a_here if a_here else float("nan"):.1f}  [{el:.0f}s]', flush=True)
        for m, v in parts:
            print(f'      {str(m):32s} a_{d-1} = {v}', flush=True)
        assert B >= a_here, f'B_{d} = {B} < a_{d} = {a_here}: the recursion forces B >= a'
    json.dump(rows, open(os.path.join(ROOT, 'results', 'wk11_int_bdelta.json'), 'w'), indent=1)
    print('RESULT ' + json.dumps([{k: r[k] for k in ('delta', 'a', 'channels', 'B')} for r in rows]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
