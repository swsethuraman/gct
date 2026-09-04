#!/usr/bin/env python3
"""Session 46 -- the ledger table from results/s46_cells.jsonl."""
import sys, os, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
R = os.path.join(HERE, '..', 'results')

def hpad_table():
    out = {}
    for fn in ('s46_census7_hpad.json', 's46_census8_hpad.json'):
        p = os.path.join(R, fn)
        if not os.path.exists(p): continue
        for r in json.load(open(p)): out[(tuple(r['lam']), r['delta'])] = r['h_pad']
    return out

def seqinfo(d):
    out = {}
    for sd in d.get('sides', {}).values():
        for pr, pp in sd.get('per_prime', {}).items():
            for dg in pp.get('diag', []):
                m = re.search(r'SEQ n=(\d+) nrows=(\d+) nnz=(\d+) k=\d+ len=\d+ secs=([\d.]+)', dg.get('note', ''))
                if m and dg.get('status') == 'NONSINGULAR':
                    out[pr] = dict(rows=int(m.group(2)), nnz_c=int(m.group(3)), seq=float(m.group(4)),
                                   level=dg['level'])
    return out

if __name__ == '__main__':
    H = hpad_table()
    rows = [json.loads(l) for l in open(os.path.join(R, 's46_cells.jsonl'))]
    seen = {}
    for d in rows: seen[(tuple(d['lam']), d['delta'])] = d
    rows = sorted(seen.values(), key=lambda d: d['n_chi'])
    lvsets = dict(cheap=['(3,2)', '(12,2)', 'uncompr'], s42=['(12,2)', 'uncompr'], full=['uncompr'])
    print("| δ | λ | elig | bal | `a` | `h_pad` | `N_S` | \\|Stab\\| | `n_χ` | rows | `nnz` | `nnz_c` | level | nullity | `mult_det` | `D` | build s | seq s | wall s | HWM GB |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    tot_a = 0
    for d in rows:
        lam = tuple(d['lam']); dl = d['delta']
        si = seqinfo(d); pr = sorted(si, reverse=True)
        s0 = si[pr[0]] if pr else {}
        lv = lvsets['s42' if d['nrows'] / d['n_chi'] > 10 else 'cheap'][s0.get('level', 0)]
        k = d['sides']['det']['nullity']; mult = d['sides']['det']['mult']
        h = H.get((lam, dl))
        D = (f"**−{mult}** (exact, `h_pad = 0`)" if h == 0 else
             (f"≤ {h - mult}" if h is not None and h < mult else "≤ 0"))
        tot_a += d['a']
        print(f"| {dl} | `{lam}` | {'yes' if lam[0] >= dl else 'onset'} | {lam[0]-lam[-1]} | {d['a']} | {h} | "
              f"{d['N_S']} | {d['stab']} | {d['n_chi']} | {d['nrows']} | {d['nnz']} | {s0.get('nnz_c','')} | "
              f"`{lv}` | {k} | **{mult}** = a | {D} | {d['build_secs']} | {s0.get('seq','')} | {d['secs']} | {d['build_hwm_gb']} |")
    print()
    print(f"**{len(rows)} cells, ambient units Σa = {tot_a}, `mult_det = a` proved at "
          f"{sum(1 for d in rows if d['sides']['det']['nullity'] == 0)} of them.**")
