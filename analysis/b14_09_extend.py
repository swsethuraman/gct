#!/usr/bin/env python3
"""
B14-09, beyond the assignment -- what the same instrument gives for free.

Slot 9 asks for `n_chi` at 58 cells.  The instrument costs milliseconds per
cell, so three further tables cost minutes and are produced here.  Each is
labelled in the report as EXPLORATORY (outside the assignment) except (1), which
is a correction to a figure the assignment's own inputs carry.

  1. all 402 six-row degree-10 weights, so the degree has a complete measured
     n_chi record rather than 344 measured and 58 unknown.  This also settles
     B13-08's "17 of the 95 exceed 2^21", which its own report and
     `matmul_mod_wide`'s docstring derive from `N_S/|Stab| >= 2^21` -- the
     quotient `nchi_2_21_guard` says is neither bound.

  2. `results/b13_05_final.json` carries a field `n_chi_lb` on all 222 open
     cells, equal to `N_S/|Stab|` and labelled a LOWER BOUND.  B13-05's cost
     table, and the ">= 1,100 CPU-hours" figure the batch-14 board retires,
     were computed on it.  Every one of the 222 is measured exactly here and
     the label is tested: an `n_chi` below the recorded `n_chi_lb` falsifies it
     on banked data.

  3. the ratio `n_chi / (N_S/|Stab|)` over every banked record in the tree, so
     the size of the error the quotient makes is on record as a number.

usage: python3 analysis/b14_09_extend.py [--out results/b14_09/extended.json]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
import b14_09_sizing as S

WIDE = 1 << 21


def all_402():
    q = json.load(open(os.path.join(ROOT, 'results/s79_per6_queue.json')))
    cells = q['10'] if isinstance(q, dict) and '10' in q else q
    out = []
    for e in cells:
        mu = tuple(e['mu']) if isinstance(e, dict) else tuple(e)
        a = e.get('a') if isinstance(e, dict) else None
        z = S.n_chi_exact(mu, 10, n=3)
        out.append(dict(mu=list(mu), a=a, N_S=z['N_S'], stab=z['stab'], n_chi=z['n_chi'],
                        NS_over_stab=z['N_S'] / z['stab'],
                        ratio=round(z['n_chi'] / (z['N_S'] / z['stab']), 4),
                        wide_measured=bool(z['n_chi'] >= WIDE),
                        wide_by_quotient=bool(z['N_S'] / z['stab'] >= WIDE)))
        if isinstance(e, dict) and 'N_S' in e:
            assert z['N_S'] == e['N_S'], ('N_S disagrees with the frozen queue', mu)
    return out


def b13_05_open():
    d = json.load(open(os.path.join(ROOT, 'results/b13_05_final.json')))
    out = []
    for o in d['open']:
        mu = tuple(o['mu']); de = o['delta']; r = len(mu)
        z = S.n_chi_exact(mu, de, n=3)
        assert z['N_S'] == o['N_S'], ('N_S disagrees with b13_05_final', mu, de)
        assert z['stab'] == o['stab'], ('|Stab| disagrees with b13_05_final', mu, de)
        out.append(dict(mu=list(mu), delta=de, ell=o.get('ell'), a=o.get('a'),
                        N_S=z['N_S'], stab=z['stab'], n_chi=z['n_chi'],
                        recorded_n_chi_lb=o['n_chi_lb'],
                        below_the_recorded_lower_bound=bool(z['n_chi'] < o['n_chi_lb']),
                        ratio=round(z['n_chi'] / o['n_chi_lb'], 4) if o['n_chi_lb'] else None))
    return out


def corpus_ratio():
    H = S.harvest()
    rows = []
    for k, v in H.items():
        n, r, mu, de = k
        if not v['stab']:
            continue
        q = v['N_S'] / v['stab']
        rows.append(dict(n=n, r=r, mu=list(mu), delta=de, N_S=v['N_S'], stab=v['stab'],
                         n_chi=v['n_chi'], ratio=round(v['n_chi'] / q, 4), src=v['src']))
    rows.sort(key=lambda d: d['ratio'])
    return rows


def main():
    t0 = time.time()
    a402 = all_402()
    b05 = b13_05_open()
    rat = corpus_ratio()
    wm = [c for c in a402 if c['wide_measured']]
    wq = [c for c in a402 if c['wide_by_quotient']]
    mis = [c for c in a402 if c['wide_measured'] != c['wide_by_quotient']]
    below = [c for c in b05 if c['below_the_recorded_lower_bound']]
    doc = dict(
        session='B14-09', note='outside the assignment except where the report says otherwise',
        degree10_all_402=dict(
            cells=a402, count=len(a402),
            wide_measured=len(wm), wide_by_quotient=len(wq),
            routed_wrongly_by_quotient=[dict(mu=c['mu'], n_chi=c['n_chi'], quotient=c['NS_over_stab']) for c in mis],
            ratio_min=min(c['ratio'] for c in a402), ratio_max=max(c['ratio'] for c in a402),
            n_chi_min=min(c['n_chi'] for c in a402), n_chi_max=max(c['n_chi'] for c in a402),
            sum_n_chi=sum(c['n_chi'] for c in a402)),
        b13_05_open_222=dict(
            cells=b05, count=len(b05),
            below_the_recorded_lower_bound=len(below),
            examples_below=below[:10],
            ratio_min=min(c['ratio'] for c in b05 if c['ratio']),
            ratio_max=max(c['ratio'] for c in b05 if c['ratio']),
            sum_recorded_lb=sum(c['recorded_n_chi_lb'] for c in b05),
            sum_measured=sum(c['n_chi'] for c in b05)),
        corpus_ratio=dict(count=len(rat), min=rat[0], max=rat[-1],
                          below_one=sum(1 for r in rat if r['ratio'] < 1),
                          above_one=sum(1 for r in rat if r['ratio'] > 1),
                          equal=sum(1 for r in rat if r['ratio'] == 1),
                          rows=rat),
        secs=round(time.time() - t0, 1))
    dest = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv
                        else 'results/b14_09/extended.json')
    json.dump(doc, open(dest, 'w'), indent=1)
    g = doc['degree10_all_402']; b = doc['b13_05_open_222']; c = doc['corpus_ratio']
    print(f"402 degree-10 cells sized: n_chi {g['n_chi_min']:,}..{g['n_chi_max']:,}, "
          f"wide by measurement {g['wide_measured']}, by quotient {g['wide_by_quotient']}, "
          f"routed wrongly {len(g['routed_wrongly_by_quotient'])}")
    print(f"B13-05's 222 open cells: {b['below_the_recorded_lower_bound']} of 222 have n_chi BELOW the "
          f"recorded n_chi_lb; ratio {b['ratio_min']}..{b['ratio_max']}; "
          f"sum measured {b['sum_measured']:,} vs sum of the recorded 'lower bound' {b['sum_recorded_lb']:,}")
    print(f"corpus ratio over {c['count']} banked records: {c['min']['ratio']}..{c['max']['ratio']} "
          f"({c['below_one']} below 1, {c['above_one']} above, {c['equal']} equal)")
    print(f"[{doc['secs']}s] -> {os.path.relpath(dest, ROOT)}")


if __name__ == '__main__':
    main()
