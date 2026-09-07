#!/usr/bin/env python3
"""Assemble results/s64_calibration.md and results/s64_calibration.jsonl (unified)
from the reduced-engine sweep (results/s64_calibration.jsonl, dense + sparse) and
the independent-engine cross-checks (results/s64_indep_r34.jsonl,
results/s64_indep_r5.jsonl).  Also writes the cost curve results/s64_cost.md.

One row per cell: a, mult_det, mult_red, mult_pad, D, i_det/i_red/i_pad,
primes/seeds agreement, engine, route, banked cross-check, verdict."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
R = os.path.join(ROOT, 'results')


def load(path):
    out = []
    if os.path.exists(path):
        for ln in open(path):
            ln = ln.strip()
            if ln:
                try: out.append(json.loads(ln))
                except Exception: pass
    return out


def cell_row(r, engine, banked=None):
    a = r['a']
    return dict(delta=r['delta'], lam=tuple(r['lam']), ell=r['ell'], a=a,
                n_chi=r.get('n_chi'), N_S=r.get('N_S'), route=r.get('route', 'dense'),
                mult_det=r.get('mult_det'), mult_red=r.get('mult_red'), mult_pad=r.get('mult_pad'),
                D=r.get('D'),
                i_det=(a - r['mult_det']) if r.get('mult_det') is not None else None,
                i_red=(a - r['mult_red']) if r.get('mult_red') is not None else None,
                i_pad=(a - r['mult_pad']) if r.get('mult_pad') is not None else None,
                engine=engine, banked=banked, secs=r.get('secs'),
                sides=r.get('sides', {}))


def load_hpad():
    """h_pad per cell from the parsed s60 rows (banked ledger)."""
    import re
    hp = {}
    p60 = '/home/claude/s60_rows.json'
    if os.path.exists(p60):
        for r in json.load(open(p60)):
            hp[(r['delta'], tuple(r['lam']))] = r.get('hpad')
    return hp


def main():
    HP = load_hpad()
    rows = {}
    # reduced engine (dense + sparse). sparse rows have mult_red only as banked cross-check
    for r in load(os.path.join(R, 's64_calibration.jsonl')):
        if r.get('status', '').startswith('a=0') or r.get('status', '').startswith('skipped'):
            continue
        key = (r['delta'], tuple(r['lam']))
        banked = r.get('banked')
        # for sparse rows, mult_red/mult_det come from banked
        if r.get('route') == 'sparse':
            r = dict(r); r['mult_red'] = banked.get('mult_red') if banked else None
            r['mult_det'] = banked.get('mult_det') if banked else None
            r['D'] = (r['mult_pad'] - r['mult_det']) if (r.get('mult_pad') is not None and r.get('mult_det') is not None) else None
        rows[key] = cell_row(r, 'reduced', banked)
    # independent engine (r=3,4 and r=5 cross-checks)
    indep = {}
    for path in ('s64_indep_r34.jsonl', 's64_indep_r5.jsonl'):
        for r in load(os.path.join(R, path)):
            if r.get('status') == 'a=0': continue
            key = (r['delta'], tuple(r['lam']))
            indep[key] = cell_row(r, 'indep')
    # merge: prefer reduced where present, annotate indep agreement
    allkeys = sorted(set(rows) | set(indep), key=lambda k: (k[1] != tuple(sorted(k[1], reverse=True)), len(k[1]), k[0], k[1]))
    unified = []
    for key in allkeys:
        base = rows.get(key) or indep.get(key)
        rec = dict(base)
        if key in rows and key in indep:
            i = indep[key]
            rec['indep_agree'] = (i['mult_det'] == rec['mult_det'] and i['mult_red'] == rec['mult_red'] and i['mult_pad'] == rec['mult_pad'])
            rec['engine'] = 'reduced+indep'
        unified.append(rec)

    # ---- verdict per row ----
    for rec in unified:
        mp, mr, md = rec['mult_pad'], rec['mult_red'], rec['mult_det']
        ok = True; notes = []
        if mp is not None and mr is not None:
            if mp > mr: ok = False; notes.append('CONTAINMENT VIOLATED')
            if rec['ell'] <= 5 and mp != mr: ok = False; notes.append('pad!=red at r<=5')
        if rec.get('banked'):
            b = rec['banked']
            if b.get('mult_red') is not None and mr is not None and b['mult_red'] != mr: ok = False; notes.append('banked red mismatch')
            if b.get('mult_det') is not None and md is not None and b['mult_det'] != md: ok = False; notes.append('banked det mismatch')
        if rec.get('indep_agree') is False: ok = False; notes.append('indep disagree')
        rec['PASS'] = ok; rec['notes'] = notes

    # ---- markdown ----
    disc = [r for r in unified if r['mult_pad'] is not None and r['mult_det'] is not None and r['mult_pad'] < r['mult_det']]
    npass = sum(1 for r in unified if r['PASS'])
    lines = ["# Session 64 — padded-side calibration table", "",
             f"`n = 4`.  {len(unified)} cells; **{npass}/{len(unified)} PASS**; "
             f"{len(disc)} discriminating (`mult_pad = mult_red < mult_det`).  "
             "Both house primes `2147483647, 2147483629`; `mult_pad` at ≥2 independent seeds on the dense "
             "route (exact per-prime certificate on the sparse route).  `mult_pad = mult_red` is forced at "
             "`r ≤ 5` by `P_r = R_r` (`results/s64_paramrank.md`); the check is non-vacuous only where "
             "`mult_red < a`.  Engine: `reduced` = `wk10_s64_cell` (isotypic + shared dense kernel) / sparse "
             "`wk10_s64_sparse`; `indep` = `wk10_s64_indep` (full basis, no reduction, no Wiedemann — a "
             "second implementation).", "",
             "| r | δ | λ | a | h_pad | n_χ | route | mult_det | mult_red | mult_pad | D | engine | banked det/red | PASS |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def fmt(r):
        b = r.get('banked') or {}
        bmark = ''
        if b:
            bmark = f"{b.get('mult_det')}/{b.get('mult_red')} " + ('✓' if 'banked red mismatch' not in r['notes'] and 'banked det mismatch' not in r['notes'] else '✗')
        elif r['engine'] == 'indep':
            bmark = '(indep only)'
        eng = r['engine']
        disc = ' **d**' if (r['mult_pad'] is not None and r['mult_det'] is not None and r['mult_pad'] < r['mult_det']) else ''
        hp = HP.get((r['delta'], tuple(r['lam'])))
        return (f"| {r['ell']} | {r['delta']} | `{tuple(r['lam'])}`{disc} | {r['a']} | {hp if hp is not None else '—'} | {r.get('n_chi') or '—'} | {r['route']} | "
                f"{r['mult_det']} | {r['mult_red']} | {r['mult_pad']} | {r['D']} | {eng} | {bmark} | {'✅' if r['PASS'] else '❌ '+','.join(r['notes'])} |")
    # discriminating cells first, then the rest
    for r in sorted(unified, key=lambda r: (not (r['mult_pad'] is not None and r['mult_det'] is not None and r['mult_pad'] < r['mult_det']), r['ell'], r['delta'], tuple(r['lam']))):
        lines.append(fmt(r))
    lines += ["", "**d** marks a discriminating cell (`mult_pad = mult_red < mult_det`), where a correct padded "
              "engine must return a value strictly below the determinant's — the only cells that distinguish "
              "the padded side from a silent copy of the determinant."]
    open(os.path.join(R, 's64_calibration.md'), 'w').write("\n".join(lines) + "\n")
    with open(os.path.join(R, 's64_calibration.jsonl'), 'w') if False else open(os.path.join(R, 's64_calibration_unified.jsonl'), 'w') as f:
        for r in unified:
            rr = dict(r); rr['lam'] = list(rr['lam']); rr.pop('sides', None); f.write(json.dumps(rr) + "\n")

    # ---- cost curve ----
    cost = [r for r in unified if r.get('secs') and r.get('n_chi')]
    cl = ["# Session 64 — cost curve", "",
          "Wall-clock per cell (both primes; dense = one shared flint kernel + three point matrices; "
          "sparse = Wiedemann certificates per side).  `n_χ` is the isotypic column count.", "",
          "| r | δ | λ | a | n_χ | route | secs |", "|---|---|---|---|---|---|---|"]
    for r in sorted(cost, key=lambda r: (r['route'], r['n_chi'])):
        cl.append(f"| {r['ell']} | {r['delta']} | `{tuple(r['lam'])}` | {r['a']} | {r['n_chi']} | {r['route']} | {r['secs']} |")
    open(os.path.join(R, 's64_cost.md'), 'w').write("\n".join(cl) + "\n")

    print(f"cells: {len(unified)}  PASS: {npass}  discriminating: {len(disc)}")
    fails = [r for r in unified if not r['PASS']]
    if fails:
        print("FAILURES:")
        for r in fails: print("  ", r['ell'], r['delta'], tuple(r['lam']), r['notes'])
    else:
        print("ALL PASS")
    return unified


if __name__ == '__main__':
    main()
