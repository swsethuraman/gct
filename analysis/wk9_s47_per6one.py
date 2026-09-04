#!/usr/bin/env python3
"""
Session 47 -- one delta=8 permanent weight by the injectivity certificate, banked
to its own jsonl so it can run in parallel with wk9_s47_per6.py --run on the
other core.  Merged into results/s47_per6_d8.md by wk9_s47_per6merge.py.

usage: python3 wk9_s47_per6one.py a mu1 mu2 ...
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s43_inject import inject_one

if __name__ == '__main__':
    a = int(sys.argv[1]); mu = tuple(int(v) for v in sys.argv[2:])
    res = inject_one(8, mu, a, verbose=True)
    res['units'] = None if res['mult'] is None else a - res['mult']
    with open(os.path.join(ROOT, 'results', 's47_per6_par.jsonl'), 'a') as f:
        f.write(json.dumps(res) + "\n")
    print(json.dumps({k: res[k] for k in ('lam','a','n_chi','mult','units','secs')}), flush=True)
    if res['mult'] is None:
        print(f"!!! NON-EMPTY permanent weight {mu} at delta=8", flush=True); sys.exit(4)
