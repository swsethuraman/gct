#!/usr/bin/env python3
"""
Session 46 -- one cell, through session 45's validated solve path, with the
generator isotypic reduction of wk9_s46_gen in place of the |Stab|-pass one.

Nothing in the certificate chain changes.  wk9_s45_cell.measure_cell is used
unchanged; the single substitution is its build function, and V4
(analysis/wk9_s46_validate.py, results/s46_buildvalidation.md) is the evidence
that the substitution is an identity on every object the chain consumes:
identical n_chi, col_of, sgn, dropped orbits, E entrywise, and row space.

usage: python3 wk9_s46_cell.py delta lam1 ... [--side det|pad|both]
       [--levels cheap|s42|full] [--full-check] [--kern] [--npts K] [--out FILE]
       [--seed0 S] [--bound B]
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied46')
os.environ.setdefault('WIED_WORK', '/home/claude/s46/work')
import wk9_s45_cell as C
from wk9_s46_gen import build_cell_gen

# the one substitution, and it is the whole of this module
C.build_cell = build_cell_gen

measure_cell = C.measure_cell
LEVELS = C.LEVELS

if __name__ == '__main__':
    args = sys.argv[1:]
    sides = ('det',); lv = 'cheap'; full = False; kern = False; outp = None
    npts = None; seed0 = 1; bound = 40
    pos = []; i = 0
    while i < len(args):
        if args[i] == '--side':
            sides = ('det', 'pad') if args[i + 1] == 'both' else (args[i + 1],); i += 2
        elif args[i] == '--levels': lv = args[i + 1]; i += 2
        elif args[i] == '--npts': npts = int(args[i + 1]); i += 2
        elif args[i] == '--seed0': seed0 = int(args[i + 1]); i += 2
        elif args[i] == '--bound': bound = int(args[i + 1]); i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        elif args[i] == '--full-check': full = True; i += 1
        elif args[i] == '--kern': kern = True; i += 1
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    res = measure_cell(lam, delta, sides=sides, levels=LEVELS[lv], full_check=full,
                       want_kern=kern, npts=npts, seed0=seed0, bound=bound)
    res['build'] = 'wk9_s46_gen'
    kv = {}
    for sd in res.get('sides', {}):
        if 'kern' in res['sides'][sd]: kv[sd] = res['sides'][sd].pop('kern')
    print(json.dumps(res))
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(res) + "\n")
    if kv:
        import pickle
        os.makedirs('/home/claude/s46', exist_ok=True)
        pickle.dump(dict(res=res, kern=kv),
                    open(f"/home/claude/s46/kern_{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
