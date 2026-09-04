#!/usr/bin/env python3
"""
Session 47 -- what survives the refutation of the exactness conjecture.

The conjecture (h_pad < a => mult_red = h_pad) is false: (15,12,6,1,1,1)_9 has
a = 21, h_pad = 19, mult_red = 18.  So h_pad does NOT predict the pad-side unit
count at a firing cell.

What is still proved, at every cell of the region including cells no rank
computation can reach, is Corollary B2:

    mult_red <= h_pad     =>     units(lam, delta) := a - mult_red  >=  a - h_pad,

a free LOWER bound on the number of pad-side units, in milliseconds.  Plus
mult_pad <= mult_red (transfer lemma), so a - mult_pad >= a - h_pad too.

This script emits that table over the whole census: every cell with
0 < h_pad < a, with its proved lower bound on the units, and it flags the
cells where the bound is known to be attained (the record) and where it is
known NOT to be attained (the counterexample).

usage: python3 wk9_s47_units.py [--md results/s47_units.md]
"""
import json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)


def census():
    out = []
    for fn in ('s42_census.json', 's42_census_weyl.json'):
        for x in json.load(open(os.path.join(ROOT, 'results', fn))):
            if x.get('a') and x.get('h_pad') is not None:
                out.append(x)
    return out


def known():
    from wk9_s47_deficit import record
    k = {(r['lam'], r['delta']): r for r in record()}
    import json as _j
    p = os.path.join(ROOT, 'results', 's47_cells.jsonl')
    if os.path.exists(p):
        for L in open(p):
            L = L.strip()
            if not L: continue
            r = _j.loads(L)
            k[(tuple(r['lam']), r['delta'])] = dict(
                lam=tuple(r['lam']), delta=r['delta'], a=r['a'], h_pad=r['h_pad'],
                mult_red=r['mult_red'], d=min(r['a'], r['h_pad']) - r['mult_red'],
                e=r['h_pad'] - r['a'], src='s47')
    return k


def rows():
    K = known()
    out = []
    for x in census():
        a, h = x['a'], x['h_pad']
        if not (0 < h < a): continue
        lam = tuple(x['lam'])
        r = dict(lam=lam, delta=x['delta'], ell=x['ell'], a=a, h_pad=h,
                 lb=a - h, N_S=x.get('N_S'))
        m = K.get((lam, x['delta']))
        r['mult_red'] = m['mult_red'] if m else None
        r['units'] = (a - m['mult_red']) if m else None
        r['attained'] = None if not m else (m['mult_red'] == h)
        out.append(r)
    out.sort(key=lambda z: (-z['lb'], z['delta'], z['lam']))
    return out


if __name__ == '__main__':
    rs = rows()
    meas = [r for r in rs if r['mult_red'] is not None]
    print(f"cells with 0 < h_pad < a: {len(rs)}   measured: {len(meas)}")
    print(f"  bound attained (units == a - h_pad): {sum(1 for r in meas if r['attained'])}")
    print(f"  bound NOT attained (units > a - h_pad): {sum(1 for r in meas if r['attained'] is False)}")
    print(f"  lower bound distribution: {dict(sorted(Counter(r['lb'] for r in rs).items()))}")
    if '--md' in sys.argv:
        path = sys.argv[sys.argv.index('--md') + 1]
        L = ["# Proved lower bounds on the pad-side units, from the normalisation bound alone\n",
             "Session 47.  The exactness conjecture is **false** — `(15,12,6,1,1,1)_9` has",
             "`a = 21`, `h_pad = 19`, `mult_red = 18` — so `h_pad` does **not** give the unit",
             "count at a firing cell.  What survives is Corollary B2 as an inequality:\n",
             "> `mult_red ≤ h_pad`, hence `units := a − mult_red ≥ a − h_pad`, **proved**, at",
             "> every cell of the region — including every cell no rank computation can reach,",
             "> in milliseconds.  With the transfer lemma (`mult_pad ≤ mult_red`) the same",
             "> number bounds the pad-side units below.\n",
             f"**{len(rs)} cells** with `0 < h_pad < a` (the `h_pad = 0` cells are omitted: there",
             "`mult_red = 0` outright, so `units = a`, and they are listed in",
             "`results/mult_red_table.md`).  `lb = a − h_pad` is the proved lower bound.",
             "`measured` is the record where it exists.\n",
             "| `λ` | `δ` | `ℓ` | `a` | `h_pad` | `units ≥` | measured `mult_red` | bound attained |",
             "|---|---|---|---|---|---|---|---|"]
        for r in rs:
            att = '—' if r['attained'] is None else ('yes' if r['attained'] else '**no**')
            mr = '—' if r['mult_red'] is None else str(r['mult_red'])
            L.append("| `%s` | %d | %d | %d | %d | **%d** | %s | %s |" % (
                str(r['lam']).replace(' ', ''), r['delta'], r['ell'], r['a'], r['h_pad'],
                r['lb'], mr, att))
        open(path, 'w').write("\n".join(L) + "\n")
        print('wrote', path)
