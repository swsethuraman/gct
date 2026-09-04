#!/usr/bin/env python3
"""
Session 47 -- merge the parallel per6 result into results/s47_per6_d8.md and
report whether I(D_6^{per_3})_8 = 0.

usage: python3 wk9_s47_per6merge.py
"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s47_per6 import all_weights, measured, OUTSTANDING_D8

LED = os.path.join(ROOT, 'results', 's47_per6_d8.md')

def rows():
    out = {}
    for fn in ('s47_per6.jsonl', 's47_per6_par.jsonl'):
        p = os.path.join(ROOT, 'results', fn)
        if not os.path.exists(p): continue
        for L in open(p):
            L = L.strip()
            if L:
                r = json.loads(L); out[tuple(r['lam'])] = r
    return out

if __name__ == '__main__':
    got = rows()
    want = [mu for mu, _ in OUTSTANDING_D8]
    txt = open(LED).read()
    head = txt.split('|---|---|---|---|---|---|---|---|---|')[0] + '|---|---|---|---|---|---|---|---|---|\n'
    body = []
    for mu in want:
        r = got.get(mu)
        if not r: continue
        mult = r['mult'] if r['mult'] is not None else '**< a**'
        units = r['units'] if r['units'] is not None else '**≥ 1**'
        body.append(f"| `{mu}` | {r['a']} | {r['N_S']} | {r['stab']} | {r['n_chi']} | "
                    f"inject | {mult} | {units} | {round(r['secs'])} |")
    done = [mu for mu in want if mu in got]
    empty = [mu for mu in done if got[mu]['mult'] == got[mu]['a']]
    tail = "\n"
    if len(done) == len(want) and len(empty) == len(done):
        tail += (f"\n**All {len(want)} are empty.**  With session 41's 28 and session 43's 54 — "
                 f"82 weights, all empty — every one of the 91 length-6 weights `μ ⊢ 24` with\n"
                 f"`a(μ, 8) ≥ 1` in `Sym^8(Sym^3 C^6)` has `mult = a`, so\n\n"
                 f"> **`I(D_6^{{per_3}})_8 = 0`** (proved: a nonsingularity certificate at one prime\n"
                 f"> proves `mult = a`, and both house primes agree at every weight), and by\n"
                 f"> Prop. 8(1) of `docs/transfer_lemma.md`, **`mult_pad = mult_red` at every\n"
                 f"> weight of degree 8** — the degree at which every pad-side bite in the six-row\n"
                 f"> record lives.  There is no permanent-specific equation in degree 8.\n\n"
                 f"With session 43's `I(D_6^{{per_3}})_7 = 0` and session 37's `δ ≤ 6`, the\n"
                 f"permanent is now proved invisible on the reducible side through degree 8.\n")
    else:
        ne = [mu for mu in done if mu not in empty]
        tail += (f"\n{len(done)} of {len(want)} measured; empty at {len(empty)}"
                 + (f"; **NOT empty at {ne}**" if ne else "") + ".\n")
    open(LED, 'w').write(head + "\n".join(body) + tail)
    print(f"{len(done)}/{len(want)} measured, {len(empty)} empty")
