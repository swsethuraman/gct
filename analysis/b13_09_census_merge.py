#!/usr/bin/env python3
"""
B13-09 -- merge the separate (8, 9) symmetric-function plethysm run
(analysis/b13_09_pleth89.py -> results/b13_09_pleth89.json, i.e. wk8_s30_pleth.amb(9,3,8))
into the census, asserting it equals the Weyl-alternation value at every (8, 9)
census weight, and asserting the converse direction too: every 8-row constituent
of Sym^9(Sym^3) that the plethysm reports with a >= 1 IS in the census (so the
census cannot have silently dropped a weight it could not place -- the failure
mode docs/batch13_worker_preamble.md names).

usage: python3 analysis/b13_09_census_merge.py [--census results/b13_09_census.json]
                                               [--pleth results/b13_09_pleth89.json]
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

if __name__ == '__main__':
    a = sys.argv[1:]
    cpath = a[a.index('--census') + 1] if '--census' in a else os.path.join(ROOT, 'results', 'b13_09_census.json')
    ppath = a[a.index('--pleth') + 1] if '--pleth' in a else os.path.join(ROOT, 'results', 'b13_09_pleth89.json')
    C = json.load(open(cpath)); P = json.load(open(ppath))
    assert P['delta'] == 9 and P['n'] == 3 and P['maxrows'] == 8, P
    pl = {tuple(int(x) for x in k.split(',')): v for k, v in P['a'].items()}
    rows = C['cells']['r8_d9']
    n = 0
    for r in rows:
        mu = tuple(r['mu'])
        assert len(mu) == 8 and mu[-1] > 0, mu
        ap = pl.get(mu, 0)
        assert ap == r['a'], ('plethysm and Weyl alternation disagree at an (8,9) census weight', mu, r['a'], ap)
        r['a_pleth'] = int(ap); n += 1
    # the other direction: no 8-row a>=1 weight of the plethysm is missing from the census
    pl8 = {mu for mu, v in pl.items() if v >= 1 and len(mu) == 8}
    cen8 = {tuple(r['mu']) for r in rows}
    missing = sorted(pl8 - cen8); extra = sorted(cen8 - pl8)
    assert not missing, ('the census is missing 8-row weights the plethysm reports', missing[:10], len(missing))
    assert not extra, ('the census carries 8-row weights the plethysm does not', extra[:10], len(extra))
    C['pleth_8_9'] = dict(source=os.path.relpath(ppath, ROOT), secs=P['secs'], constituents_le_8_rows=len(pl),
                          weights_of_length_exactly_8=len(pl8), checked=n,
                          both_directions='every (8,9) census weight matches amb(9,3,8), and every 8-row weight amb reports with a >= 1 is in the census')
    json.dump(C, open(cpath, 'w'), indent=1)
    print(f"(8,9): {n} weights cross-checked against amb(9,3,8); "
          f"{len(pl8)} weights of length exactly 8 with a >= 1 in the plethysm, all present in the census; "
          f"no extras.  merged -> {cpath}")
