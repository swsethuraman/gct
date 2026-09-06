#!/usr/bin/env python3
"""
Session 60 -- the ledger and the summary tables from the banked records.

Reads results/s60_cells.jsonl (one record per cell) and the census, writes
results/s60_ledger.md (one row per cell, both sides, instrument and proof status)
and prints the per-degree coverage / outcome tables used in docs/s60_report.md.

usage: python3 analysis/wk9_s60_report.py [--cells results/s60_cells.jsonl] [--ledger results/s60_ledger.md]
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def arg(args, name, default):
    return args[args.index(name) + 1] if name in args else default


def load(path):
    recs = {}
    for ln in open(path):
        ln = ln.strip()
        if not ln: continue
        r = json.loads(ln)
        recs[(tuple(r['lam']), r['delta'])] = r      # later records supersede (re-runs)
    return recs


def side_str(r, sd):
    s = r.get('sides', {}).get(sd)
    if not s: return '—'
    m = s['mult']
    st = s.get('status', '')
    if 'proved' in st: tag = 'proved'
    elif 'bounded' in st: tag = 'bounded'
    elif 'exact kernel' in st: tag = 'exact'
    elif 'DISAGREE' in st: tag = 'PRIMES DISAGREE'
    else: tag = 'measured'
    return f"{m} ({tag})"


if __name__ == '__main__':
    args = sys.argv[1:]
    cells_path = arg(args, '--cells', os.path.join(ROOT, 'results/s60_cells.jsonl'))
    ledger_path = arg(args, '--ledger', os.path.join(ROOT, 'results/s60_ledger.md'))
    C = json.load(open(os.path.join(ROOT, 'results/s60_census.json')))
    C10 = json.load(open(os.path.join(ROOT, 'results/s60_census_d10.json')))
    census = {}
    for d, o in list(C.items()) + list(C10.items()):
        for c in o['cells']: census[(tuple(c['lam']), c['delta'])] = c
    recs = load(cells_path)
    meas = {k: r for k, r in recs.items() if r.get('status') == 'measured'}
    defer = {k: r for k, r in recs.items() if r.get('status') == 'DEFER'}
    # ---------------------------------------------------------------- ledger
    L = ["# Session 60 — ledger: the balanced length-5 complement, both sides", "",
         "One row per measured cell (`n = 4`, `r = 5`).  `a` = ambient multiplicity (Weyl alternation = s54 plethysm);",
         "`h_pad` = normalisation bound (`mult_red <= h_pad`, proved).  `mult_det` at `a+8` det_4 pencils; `mult_red(★)`",
         "point-free by Theorem (★) on the red columns of `E`; `mult_red(pts)` at `a+8` reducible `ℓ·c` points (—: not run,",
         "(★) alone above `n_chi = 20000` on the sparse route).  Tags: *proved* = nullity 0 at both primes (or, on the",
         "reducible side, nullity certified `<= a − h_pad` at both primes, meeting the theorem's `>=`); *exact* = explicit",
         "kernel at both primes (dense route); *measured* = nullity exhibited at both primes; *bounded* = extraction budget",
         "reached, the value is an upper bound on `mult`.  `D = mult_red − mult_det`; a refutation of `R_5 ⊆ D_5` is `D > 0`.",
         "Route: dense = exact flint kernel (`n_chi <= 4000`), sparse = session-45 Wiedemann certificates.", "",
         "| δ | λ | a | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | D | primes | s | certs |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    ncert = 0
    for (lam, d), r in sorted(meas.items(), key=lambda kv: (kv[0][1], -kv[1]['a'] if False else kv[1].get('n_chi', 0), kv[0][0])):
        certs = sum(len(pp.get('certs', [])) for pp in r.get('per_prime', {}).values())
        ncert += certs
        agree = all(s.get('primes_agree') for s in r.get('sides', {}).values())
        L.append(f"| {d} | `{lam}` | {r['a']} | {r.get('h_pad')} | {r['N_S']} | {r['stab']} | {r['n_chi']} | {r['route']} | "
                 f"{side_str(r, 'det')} | {side_str(r, 'red_star')} | {side_str(r, 'red_pts')} | {r.get('D')} | "
                 f"{'agree' if agree else 'DISAGREE'} | {r['secs']} | {certs} |")
    if defer:
        L += ["", "## Deferred (timeout or failure), with sizes", "",
              "| δ | λ | a | h_pad | N_S | n_chi | rc | s | tail |", "|---|---|---|---|---|---|---|---|---|"]
        for (lam, d), r in sorted(defer.items(), key=lambda kv: (kv[0][1], kv[1].get('n_chi') or 0)):
            L.append(f"| {d} | `{lam}` | {r.get('a')} | {r.get('h_pad')} | {r.get('N_S')} | {r.get('n_chi')} | {r.get('rc')} | {r.get('secs')} | `{' / '.join(str(x)[:80] for x in r.get('tail', []))}` |")
    with open(ledger_path, 'w') as f:
        f.write("\n".join(L) + "\n")
    # ---------------------------------------------------------------- summary
    print(f"measured {len(meas)} cells, deferred {len(defer)}, certificates {ncert}")
    print("\n| δ | complement | informative | dead | measured (inf.) | measured (dead) | D>0 | D=0 | D<0 | mult_det<a | mult_red<a | mult_red<min(a,h_pad) | dense/sparse | cheapest unmeasured informative (n_chi) | largest measured n_chi | wall h |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for d in (6, 7, 8, 9, 10):
        o = (C.get(str(d)) or C10.get(str(d)))
        cs = o['cells']
        inf = [c for c in cs if c['red'] == 'informative']; dead = [c for c in cs if c['red'] == 'dead']
        m = [r for (lam, dd), r in meas.items() if dd == d]
        mi = [r for r in m if census[(tuple(r['lam']), d)]['red'] == 'informative']
        md = [r for r in m if census[(tuple(r['lam']), d)]['red'] == 'dead']
        Dp = sum(1 for r in m if (r.get('D') or 0) > 0); D0 = sum(1 for r in m if r.get('D') == 0); Dm = sum(1 for r in m if (r.get('D') if r.get('D') is not None else 0) < 0)
        bd = sum(1 for r in m if r['mult_det'] is not None and r['mult_det'] < r['a'])
        br = sum(1 for r in m if r['mult_red'] is not None and r['mult_red'] < r['a'])
        bh = sum(1 for r in m if r['mult_red'] is not None and r.get('h_pad') is not None and r['mult_red'] < r['h_pad'] and r['mult_red'] < r['a'])
        routes = f"{sum(1 for r in m if r['route']=='dense')}/{sum(1 for r in m if r['route']=='sparse')}"
        unmeasured = [c for c in inf if (tuple(c['lam']), d) not in meas]
        cheapest = min(unmeasured, key=lambda c: c['key']) if unmeasured else None
        ch = f"`{tuple(cheapest['lam'])}` ({cheapest['n_chi']}{'' if cheapest['n_chi_exact'] else '~'}, a={cheapest['a']})" if cheapest else 'none — degree complete'
        big = max((r['n_chi'] for r in m), default=0)
        wall = round(sum(r['secs'] for r in m) / 3600, 2)
        print(f"| {d} | {len(cs)} | {len(inf)} | {len(dead)} | {len(mi)} | {len(md)} | {Dp} | {D0} | {Dm} | {bd} | {br} | {bh} | {routes} | {ch} | {big} | {wall} |")
    # bites list
    bites = [r for r in meas.values() if r['mult_red'] is not None and r['mult_red'] < r['a']]
    print(f"\ncells with mult_red < a: {len(bites)}; of which mult_red < h_pad: {sum(1 for r in bites if r['mult_red'] < r['h_pad'])}")
    for r in sorted(bites, key=lambda r: (r['delta'], r['n_chi'])):
        print(f"  δ={r['delta']} {tuple(r['lam'])} a={r['a']} h_pad={r['h_pad']} mult_det={r['mult_det']} mult_red={r['mult_red']} (pts {r['mult_red_pts']}) D={r['D']} [{r['route']}]")
    dets = [r for r in meas.values() if r['mult_det'] is not None and r['mult_det'] < r['a']]
    print(f"cells with mult_det < a: {len(dets)}")
    for r in dets: print("  ", r['delta'], r['lam'], r['a'], r['mult_det'])
    ref = [r for r in meas.values() if r.get('refute')]
    print(f"refutations (mult_red > mult_det): {len(ref)}")
    nk = [r for r in meas.values() if not r.get('ok', True)]
    print(f"self-check failures: {len(nk)}")
    mx = max(meas.values(), key=lambda r: r['secs']) if meas else None
    if mx: print(f"longest cell: δ={mx['delta']} {tuple(mx['lam'])} n_chi={mx['n_chi']} a={mx['a']} {mx['secs']} s, HWM {mx['hwm_gb']} GB")
    print(f"total wall of measured cells: {round(sum(r['secs'] for r in meas.values())/3600, 2)} h; max HWM {max((r['hwm_gb'] for r in meas.values()), default=0)} GB")
