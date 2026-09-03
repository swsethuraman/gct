#!/usr/bin/env python3
"""Session 42 -- fill the sweep numbers into docs/reducible_engine.md (idempotent on the placeholders)."""
import os, json, glob, re
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, '..', 'results'); D = os.path.join(HERE, '..', 'docs')
cells = {}
for fn in sorted(glob.glob(os.path.join(R, 's42_cells_*.jsonl'))):
    for line in open(fn):
        if line.strip():
            c = json.loads(line); k = (tuple(c['lam']), c['delta'])
            if k not in cells or cells[k].get('status') in ('beyond', 'failed'): cells[k] = c
census = json.load(open(os.path.join(R, 's42_census.json')))
weyl = json.load(open(os.path.join(R, 's42_census_weyl.json'))) if os.path.exists(os.path.join(R, 's42_census_weyl.json')) else []
def reached(delta, src):
    return [c for c in src if c['delta'] == delta and (tuple(c['lam']), delta) in cells and cells[(tuple(c['lam']), delta)].get('status') in ('proved', 'measured')]
r7, r8 = reached(7, census), reached(8, census)
r9 = reached(9, [c for c in weyl if c.get('a')])
allr = r7 + r8 + r9
maxnred = max(cells[(tuple(c['lam']), c['delta'])]['n_red'] for c in allr)
bites = [c for c in allr if cells[(tuple(c['lam']), c['delta'])]['nullity'] > 0]
lifts = {(tuple(c['lam']), c['delta']) for c in (json.loads(l) for l in open(os.path.join(R, 's42_lifts.jsonl'))) if 'PROVED' in c['verdict']}
def stat(rs):
    return (len(rs), sum(1 for c in rs if cells[(tuple(c['lam']), c['delta'])]['status'] == 'proved'),
            sum(1 for c in rs if cells[(tuple(c['lam']), c['delta'])]['status'] == 'measured'), sum(c['a'] for c in rs))
s7, s8, s9 = stat(r7), stat(r8), stat(r9)
secs = sum(cells[(tuple(c['lam']), c['delta'])].get('secs', 0) for c in allr)
summary = (f"{len(allr)} cells reached: `δ = 7`: {s7[0]} of 398 ({s7[1]} proved `mult_red = a`, {s7[2]} measured/lifted bites; {s7[3]} of 1127 ambient units); "
           f"`δ = 8`: {s8[0]} of 1479 ({s8[1]} proved, {s8[2]} bites; {s8[3]} of 14361 units); `δ = 9`: {s9[0]} of the 400 sized cells ({s9[1]} proved, {s9[2]} bites).  "
           f"Largest cell reached: `n_red = {maxnred}`.  Bites among reached cells: {len(bites)} — "
           + ', '.join(f"`{tuple(c['lam'])}`_{c['delta']} (a={c['a']}, h_pad={c['h_pad']}, mult_red={cells[(tuple(c['lam']), c['delta'])]['mult_red']}"
                       + (", lifted" if (tuple(c['lam']), c['delta']) in lifts else "") + ")" for c in bites)
           + f".  Every other reached cell has `mult_red = a` proved (nullity 0 at both primes).  Total engine time on reached cells ≈ {secs/3600:.1f} h.")
doc = open(os.path.join(D, 'reducible_engine.md')).read()
doc = doc.replace('SWEEP_TOTAL', str(s7[0] + s8[0])).replace('SWEEP_D7', str(s7[0])).replace('SWEEP_D8', str(s8[0])).replace('SWEEP_MAXNRED', str(maxnred)).replace('SWEEP_D9', str(s9[0]))
doc = doc.replace('SWEEP_SUMMARY', summary)
open(os.path.join(D, 'reducible_engine.md'), 'w').write(doc)
print(summary)
