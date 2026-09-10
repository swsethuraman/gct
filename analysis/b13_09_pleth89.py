#!/usr/bin/env python3
"""
B13-09 -- the independent symmetric-function plethysm a(mu, 9) for every mu |- 27
with at most 8 rows (wk8_s30_pleth.amb(9, 3, 8): Murnaghan-Nakayama on the
power-sum expansion of Sym^9(Sym^3)), run once, separately, because it is slow;
merged into results/b13_09_census.json by analysis/b13_09_census_merge.py, which
asserts it equals the Weyl-alternation value at every (8, 9) census weight.

usage: python3 analysis/b13_09_pleth89.py [--out results/b13_09_pleth89.json]
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk8_s30_pleth import amb

if __name__ == '__main__':
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(ROOT, 'results', 'b13_09_pleth89.json')
    t0 = time.time()
    A = amb(9, 3, 8)
    res = dict(board_numbering='batch13', session='B13-09', delta=9, n=3, maxrows=8, secs=round(time.time() - t0, 1),
               a={','.join(map(str, lam)): int(v) for lam, v in sorted(A.items())})
    json.dump(res, open(out, 'w'), indent=1)
    print(f"amb(9,3,8): {len(A)} constituents with a >= 1, sum a*1 = {sum(A.values())}, {res['secs']}s -> {out}", file=sys.stderr)
