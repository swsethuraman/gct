#!/usr/bin/env python3
"""Session 42 -- is a degree-delta bite a MINIMAL generator of I(R_r)?  By Pieri,
S_lam occurs in I_{delta-1} . C[W]_1 only through a constituent S_mu of
I(R_r)_{delta-1} with lam/mu a horizontal 4-strip; if every such mu has
mult_red(mu, delta-1) = a(mu, delta-1) (or a = 0), S_lam is not in the ideal
generated below degree delta.  Predecessor values are taken from the banked
files where present and computed by the sparse route otherwise (length-5
predecessors at r = 5, Corollary D).
usage: python3 wk9_s42_gencheck.py delta lam...   (appends to results/s42_gencheck.jsonl)"""
import sys, os, json, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); R = os.path.join(HERE, '..', 'results')
from wk9_s42_redengine import measure_cell
from wk8_s30_pleth import a_of

def predecessors(lam, k=4):
    r = len(lam); out = []
    def rec(i, cur, s):
        if i == r:
            if s == sum(lam) - k: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        for v in range(lo, lam[i] + 1): rec(i + 1, cur + [v], s + v)
    rec(0, [], 0)
    return out

def known():
    vals = {}
    for fn in glob.glob(os.path.join(R, 's42_cells_*.jsonl')) + [os.path.join(R, f) for f in ('s42_gen8_checks.jsonl', 's42_hz_checks.jsonl', 's42_gencheck_cells.jsonl')]:
        if not os.path.exists(fn): continue
        for line in open(fn):
            if line.strip():
                d = json.loads(line)
                if d.get('status') in ('proved', 'measured') or 'nullity' in d:
                    vals[(tuple(d['lam']), d['delta'])] = d
    import re
    for line in open(os.path.join(R, 's36_red_table.md')):
        m = re.match(r"\| `\((.*?)\)` \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", line)
        if m:
            lam = tuple(int(x) for x in m.group(1).split(',')); a = int(m.group(4)); mr = int(m.group(7))
            vals.setdefault((lam, int(m.group(2))), dict(lam=list(lam), delta=int(m.group(2)), a=a, mult_red=mr, nullity=a - mr, status='s36'))
    return vals

if __name__ == '__main__':
    delta = int(sys.argv[1]); lam = tuple(int(x) for x in sys.argv[2:])
    vals = known()
    rows = []; free = True
    for mu in predecessors(lam):
        mu0 = tuple(x for x in mu if x)
        a = a_of(mu0, delta - 1, 4, len(mu0))
        if a == 0:
            rows.append(dict(mu=mu, a=0, verdict='not a constituent')); continue
        d = vals.get((mu0, delta - 1))
        if d is None:
            t = time.time()
            d = measure_cell(mu0, delta - 1, route='sparse', verbose=False)
            with open(os.path.join(R, 's42_gencheck_cells.jsonl'), 'a') as f: f.write(json.dumps(d) + "\n")
        ok = (d['nullity'] == 0)
        free &= ok
        rows.append(dict(mu=mu, a=a, nullity=d['nullity'], mult_red=d['mult_red'], verdict=('free of the ideal (proved)' if ok else 'IN THE IDEAL'), src=d.get('status')))
    res = dict(lam=list(lam), delta=delta, predecessors=rows, minimal_generator=free)
    print(json.dumps(res))
    with open(os.path.join(R, 's42_gencheck.jsonl'), 'a') as f: f.write(json.dumps(res) + "\n")
