#!/usr/bin/env python3
"""Batch-14 strategy session (Claude) -- which LMR product targets are reached by a
single Cartan product of the rung-13/14 padded relations.

Lemma T (batch-14 memo; s57's Lemma L argument with any highest-weight vector w
of weight mu in A_k in place of u): multiplication by w injects I(X) cap M_{lam,delta}
into I(X) cap M_{lam+mu,delta+k}.  So if

    nu - lam_source  is dominant   and   a(nu - lam_source, delta_nu - delta_source) >= 1,

then every relation of I(P) at the source cell transports to nu, and
i_pad(nu) >= i_pad(source).  Those targets are decided by Lemma T alone; the rest
need the transport ranks that avenue 2 of the memo computes.

Sources checked: the rung-13 cell (21,17,2^7) at delta 13, the rung-14 cell
(25,17,2^7) at delta 14, and the LMR cell (65,17,2^7) at delta 24.
Targets: every component of results/b13_06/components.json with at most ten rows
(31 at delta 25, 208 at delta 26; the 97 eleven-row components already have
mult_pad = 0 by B13-06's length argument).

RESULT recorded in the memo (this script reproduces it in under a second):
    delta 25: 5 of 31 components are reached -- 1 of them is the LMR Cartan
        product (69,17,2^7), so 4 of the 30 non-ladder components are reached
        and 26 are not;
    delta 26: 26 of 208 are reached -- 3 of them are the LMR Cartan products, so
        23 of the 205 non-Cartan components are reached and 182 are not;
    every ten-row component at delta 25 is unreached, as it must be: a ten-row
    nu minus a nine-row source is never dominant when nu_9 = 2.

CONTROLS (they can fail):
  * the four Cartan products of the LMR module -- (69,17,2^7)_25, (73,17,2^7)_26,
    (71,19,2^7)_26, (69,21,2^7)_26 -- must be reached from the LMR cell;
  * no ten-row component may be reached from any of the three nine-row sources.

usage:
    python3 analysis/b14_claude_reach.py [--out results/b14_claude_reach.json]
"""
import argparse, json, os, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
from wk9_s42_census import a_weyl              # noqa: E402

CENSUS = os.path.join(ROOT, 'results', 'b13_06', 'components.json')
SOURCES = {'rung13': ((21, 17, 2, 2, 2, 2, 2, 2, 2), 13),
           'rung14': ((25, 17, 2, 2, 2, 2, 2, 2, 2), 14),
           'lmr': ((65, 17, 2, 2, 2, 2, 2, 2, 2), 24)}
CARTAN_CONTROL = {(69, 17, 2, 2, 2, 2, 2, 2, 2), (73, 17, 2, 2, 2, 2, 2, 2, 2),
                  (71, 19, 2, 2, 2, 2, 2, 2, 2), (69, 21, 2, 2, 2, 2, 2, 2, 2)}

_cache = {}


def a_of(mu, k, n=4):
    mu = tuple(x for x in mu if x)
    if not mu:
        return 1 if k == 0 else 0
    key = (mu, k, n)
    if key not in _cache:
        _cache[key] = a_weyl(mu, k, n, {})
    return _cache[key]


def reaches(nu, lam, dlam, dnu, width):
    """does a single highest-weight product carry the source cell to nu?"""
    nu = list(nu) + [0] * (width - len(nu))
    lam = list(lam) + [0] * (width - len(lam))
    mu = [nu[i] - lam[i] for i in range(width)]
    if min(mu) < 0 or any(mu[i] < mu[i + 1] for i in range(width - 1)):
        return False
    return a_of(mu, dnu - dlam) >= 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, 'results', 'b14_claude_reach.json'))
    args = ap.parse_args()
    t0 = time.time()
    rows = [r for r in json.load(open(CENSUS))['rows']
            if r['degree'] in (25, 26) and len(r['partition']) <= 10]

    out, counts = [], Counter()
    for r in rows:
        nu = tuple(r['partition'])
        reach = {name: reaches(nu, lam, dl, r['degree'], 10)
                 for name, (lam, dl) in SOURCES.items()}
        out.append({'nu': list(nu), 'degree': r['degree'], 'length': len(nu), 'reached_by': reach})
        counts[(r['degree'], reach['rung13'] or reach['rung14'])] += 1

    for degree in (25, 26):
        tot = sum(n for (d, _), n in counts.items() if d == degree)
        hit = counts[(degree, True)]
        cartan = sum(1 for o in out if o['degree'] == degree and tuple(o['nu']) in CARTAN_CONTROL)
        print(f'degree {degree}: {tot} components (<=10 rows); reached by a Cartan product '
              f'of the rung-13/14 relations: {hit}, of which {cartan} are the LMR Cartan '
              f'products themselves -> {hit - cartan} of the {tot - cartan} non-Cartan '
              f'components reached, {tot - hit} not')

    ctrl_cartan = all(any(o['reached_by'].values()) for o in out
                      if tuple(o['nu']) in CARTAN_CONTROL)
    ctrl_ten = not any(any(o['reached_by'].values()) for o in out if o['length'] == 10)
    print(f'CONTROL Cartan products of LMR all reached: {"PASS" if ctrl_cartan else "FAIL"}')
    print(f'CONTROL no ten-row target reached from a nine-row source: '
          f'{"PASS" if ctrl_ten else "FAIL"}')

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({'sources': {k: {'lam': list(v[0]), 'delta': v[1]} for k, v in SOURCES.items()},
               'targets': out}, open(args.out, 'w'), indent=1)
    print(f'{len(out)} targets -> {args.out}, {time.time() - t0:.1f}s')
    return 0 if (ctrl_cartan and ctrl_ten) else 1


if __name__ == '__main__':
    sys.exit(main())
