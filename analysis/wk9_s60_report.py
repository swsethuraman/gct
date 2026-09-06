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
    closing = {k: r for k, r in recs.items() if r.get('closing')}
    recs = {k: r for k, r in recs.items() if not r.get('closing')}
    meas = {k: r for k, r in recs.items() if r.get('status') == 'measured'}
    impl = {k: r for k, r in recs.items() if r.get('status') == 'implied'}
    defer = {k: r for k, r in recs.items() if r.get('status') == 'DEFER'}
    # a tail is closed by ANY measured cell at or above its delta_close with mult_det = a (constancy from
    # delta_close upward, monotonicity downward) -- whether the closing sweep or the census sweep measured it
    tailc = {tuple(t['tail']): t for t in json.load(open(os.path.join(ROOT, 'results/s60_tail_census.json')))}
    closed_tails = {}
    for (lam, d), r in list(closing.items()) + list(meas.items()):
        rho = tuple(lam[1:]); t = tailc.get(rho)
        if r.get('status') == 'measured' and r.get('mult_det') == r.get('a') and t and t.get('delta_close') is not None and d >= t['delta_close']:
            if rho not in closed_tails or d < closed_tails[rho][1]:
                closed_tails[rho] = (r, d)
    closed_tails = {rho: v[0] for rho, v in closed_tails.items()}
    open_closing = {k: r for k, r in closing.items() if not (r.get('status') == 'measured' and r.get('mult_det') == r.get('a'))}
    # ---------------------------------------------------------------- ledger
    L = ["# Session 60 — ledger: the balanced length-5 complement, both sides", "",
         "One row per measured cell (`n = 4`, `r = 5`).  `a` = ambient multiplicity (Weyl alternation = s54 plethysm);",
         "`h_pad` = normalisation bound (`mult_red <= h_pad`, proved).  `mult_det` at `a+8` det_4 pencils; `mult_red(★)`",
         "point-free by Theorem (★) on the red columns of `E`; `mult_red(pts)` at `a+8` reducible `ℓ·c` points (—: not run,",
         "(★) alone above `n_chi = 20000` on the sparse route).  Tags: *proved* = nullity 0 at both primes (or, on the",
         "reducible side, nullity certified `<= a − h_pad` at both primes, meeting the theorem's `>=`); *exact* = explicit",
         "kernel at both primes (dense route); *measured* = nullity exhibited at both primes; *bounded* = extraction budget",
         "reached, the value is an upper bound on `mult`.  `D = mult_red − mult_det`; a refutation of `R_5 ⊆ D_5` is `D > 0`.",
         "Route: dense = exact flint kernel (`n_chi <= 4000`), sparse = session-45 Wiedemann certificates.",
         "`N_S` is the full weight-space dimension; `n_chi = dim V_chi` is the chi_lambda-isotypic reduction of",
         "`docs/stabiliser_reduction.md` (the column count of the matrix every certificate runs on), `n_chi ~ N_S/|Stab|`;",
         "the two are never the same quantity unless `Stab` is trivial.  Every `n_chi` on a measured row is exact.", "",
         "Ladder columns (integrator note, s60): `ρ = (λ_2..λ_5)`, `t = |ρ| = 4δ − λ_1`; along the ladder `λ_δ = (4δ−t, ρ)`",
         "the quantities `a, mult_det, mult_red, i_det, i_red` are non-decreasing in δ, constant from the first δ with `a_δ = a_∞ = a_t`",
         "(`δ_close`, from `results/s60_tail_census.md`) and in particular for `δ ≥ t` (multiplication by `u = c_(4,0,0,0,0)`).",
         "`reach` says what the row closes: below `δ_close`, this δ and every lower δ of the ladder; at or above it, the whole ladder in",
         "every degree (with `mult_det = a` the tail is dead for `D > 0` permanently).  Rows with route `ladder` are implied by the",
         "named source cell (no computation).", "",
         "| δ | λ | ρ | t | reach | a | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | D | primes | s | certs |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    ncert = 0
    allrows = dict(meas); allrows.update(impl)
    for (lam, d), r in sorted(allrows.items(), key=lambda kv: (kv[0][1], kv[1].get('n_chi') or 0, kv[0][0])):
        rho = tuple(lam[1:]); t = sum(rho)
        dc = (tailc.get(rho) or {}).get('delta_close')
        if d >= t: reach = 'δ>=t: whole ladder (stable range)'
        elif dc is not None and d >= dc: reach = f'δ>=δ_close={dc}: whole ladder (a_δ = a_∞)'
        else: reach = f'δ<δ_close={dc}: δ<= {d} of ladder'
        if r.get('status') == 'implied':
            src = r['source']
            mr = r.get('mult_red')
            mrs = f"{mr} (implied)" if mr is not None else f">= {r.get('mult_red_lower_bound')} (bounded by ladder)"
            L.append(f"| {d} | `{lam}` | `{rho}` | {t} | {reach} | {r['a']} | {r.get('h_pad')} | {r.get('N_S')} | {r.get('stab')} | {r.get('n_chi')} | ladder ← `{tuple(src['lam'])}` δ={src['delta']} | "
                     f"{r['a']} (implied) | {mrs} | — | {r.get('D') if r.get('D') is not None else '<= 0'} | — | 0 | 0 |")
            continue
        certs = sum(len(pp.get('certs', [])) for pp in r.get('per_prime', {}).values())
        ncert += certs
        agree = all(s.get('primes_agree') for s in r.get('sides', {}).values())
        L.append(f"| {d} | `{lam}` | `{rho}` | {t} | {reach} | {r['a']} | {r.get('h_pad')} | {r['N_S']} | {r['stab']} | {r['n_chi']} | {r['route']} | "
                 f"{side_str(r, 'det')} | {side_str(r, 'red_star')} | {side_str(r, 'red_pts')} | {r.get('D')} | "
                 f"{'agree' if agree else 'DISAGREE'} | {r['secs']} | {certs} |")
    if defer:
        L += ["", "## Deferred (timeout or failure), with sizes", "",
              "| δ | λ | a | h_pad | N_S | n_chi | rc | s | tail |", "|---|---|---|---|---|---|---|---|---|"]
        for (lam, d), r in sorted(defer.items(), key=lambda kv: (kv[0][1], kv[1].get('n_chi') or 0)):
            L.append(f"| {d} | `{lam}` | {r.get('a')} | {r.get('h_pad')} | {r.get('N_S')} | {r.get('n_chi')} | {r.get('rc')} | {r.get('secs')} | `{' / '.join(str(x)[:80] for x in r.get('tail', []))}` |")
    L += ["", "## Closing cells — one determinant-side rank per tail, the tail settled in every degree", "",
          "`(λ_close, δ_close)` is the first rung of the tail's ladder with `a = a_∞ = a_t` (proved stable value).  `mult_det = a` there",
          "gives `i_det = 0` at every rung of the ladder (downward by monotonicity, upward by stability), hence `D ≤ 0` at every",
          "degree: the tail is **closed**.  `i_red(∞) = a − mult_red` at the closing cell is the stable reducible-ideal dimension;",
          "`i_red = 0` there forces `i_red = 0` on the whole ladder (so `D = i_det = 0` everywhere on it).", "",
          "| tail ρ | t | δ_close | λ_close | a_∞ | h_pad | N_S | Stab | n_chi | route | mult_det | mult_red(★) | mult_red(pts) | i_red(∞) | census rungs settled (δ) | status | s |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for (lam, d), r in sorted(closing.items(), key=lambda kv: (kv[1].get('n_chi') or 0, kv[0][0])):
        if r.get('status') != 'measured':
            L.append(f"| `{tuple(r.get('tail', lam[1:]))}` | {r.get('t')} | {d} | `{lam}` | {r.get('a')} | {r.get('h_pad')} | {r.get('N_S')} | — | {r.get('n_chi')} | — | — | — | — | — | {r.get('rungs_settled')} | DEFER (rc {r.get('rc')}) | {r.get('secs')} |")
            continue
        st = 'tail closed (D <= 0 in every degree)' if r['mult_det'] == r['a'] else f"**det side bites at the stable rung: i_det(∞) = {r['a'] - r['mult_det']}**"
        ir = (r['a'] - r['mult_red']) if r.get('mult_red') is not None else None
        L.append(f"| `{tuple(r['tail'])}` | {r['t']} | {d} | `{lam}` | {r['a']} | {r.get('h_pad')} | {r['N_S']} | {r['stab']} | {r['n_chi']} | {r['route']} | "
                 f"{side_str(r, 'det')} | {side_str(r, 'red_star')} | {side_str(r, 'red_pts')} | {ir if ir is not None else '—'} | {r.get('rungs_settled')} | {st} | {r['secs']} |")
    with open(ledger_path, 'w') as f:
        f.write("\n".join(L) + "\n")
    # ---------------------------------------------------------------- summary
    ncert_all = sum(len(pp.get('certs', [])) for r in list(meas.values()) + list(closing.values()) for pp in r.get('per_prime', {}).values())
    print(f"measured {len(meas)} census cells + {sum(1 for r in closing.values() if r.get('status')=='measured')} closing cells, implied {len(impl)}, deferred {len(defer)}, certificates {ncert_all} ({ncert} at census cells)")
    by_census = sum(1 for rho, r in closed_tails.items() if not r.get('closing'))
    print(f"closing cells measured: {sum(1 for r in closing.values() if r.get('status')=='measured')}, tails closed: {len(closed_tails)} "
          f"({len(closed_tails) - by_census} by the closing sweep, {by_census} by a census cell that already sat at or above its tail's delta_close), "
          f"closing cells deferred: {sum(1 for r in closing.values() if r.get('status')=='DEFER')}, det bites at closing cells: {sum(1 for r in closing.values() if r.get('status')=='measured' and r['mult_det'] < r['a'])}, "
          f"closing cells with i_red(∞) = 0: {sum(1 for r in closing.values() if r.get('status')=='measured' and r.get('mult_red') == r.get('a'))}")
    print("\n| δ | complement | informative | dead | measured (inf.) | implied (inf.) | settled by a closed tail (inf. / dead) | open (inf.) | measured (dead) | D>0 | D=0 | D<0 | mult_det<a | mult_red<a | mult_red<min(a,h_pad) | dense/sparse | cheapest open informative (n_chi) | largest measured n_chi | wall h |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
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
        ii = [r for (lam, dd), r in impl.items() if dd == d]
        settled_inf = [c for c in inf if tuple(c['lam'][1:]) in closed_tails]
        settled_dead = [c for c in dead if tuple(c['lam'][1:]) in closed_tails]
        unmeasured = [c for c in inf if (tuple(c['lam']), d) not in meas and (tuple(c['lam']), d) not in impl and tuple(c['lam'][1:]) not in closed_tails]
        cheapest = min(unmeasured, key=lambda c: c['key']) if unmeasured else None
        ch = f"`{tuple(cheapest['lam'])}` ({cheapest['n_chi']}{'' if cheapest['n_chi_exact'] else '~'}, a={cheapest['a']})" if cheapest else 'none — degree complete'
        big = max((r['n_chi'] for r in m), default=0)
        wall = round(sum(r['secs'] for r in m) / 3600, 2)
        print(f"| {d} | {len(cs)} | {len(inf)} | {len(dead)} | {len(mi)} | {len(ii)} | {len(settled_inf)} / {len(settled_dead)} | {len(unmeasured)} | {len(md)} | {Dp} | {D0} | {Dm} | {bd} | {br} | {bh} | {routes} | {ch} | {big} | {wall} |")
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
    # ---------------------------------------------------------------- ladders
    import collections
    lad = collections.defaultdict(list)
    for (lam, d), r in list(meas.items()) + [(k, r) for k, r in closing.items() if r.get('status') == 'measured']: lad[tuple(lam[1:])].append((d, r))
    closed = [(lam, d) for (lam, d) in list(meas) + list(closing) if d >= sum(lam[1:])]
    print(f"\nladders (tails) touched by measured cells: {len(lad)}")
    print(f"ladders closed permanently: {len(closed_tails)}   (a_delta = a_inf(rho) at the closing cell, mult_det = a)")
    print(f"  of which in the theorem-guaranteed stable range (delta >= t): {len(closed)}")
    print(f"  -- closure at these degrees comes from early stabilisation, not from delta >= t")
    allc = set(census)
    settled = set(meas) | set(impl) | {k for k in allc if tuple(k[0][1:]) in closed_tails}
    settled_inf = [k for k in settled if census[k]['red'] == 'informative']
    print(f"cells of the census settled (measured + implied + on a closed tail): {len(settled)} of {len(allc)} ({len(settled_inf)} informative), beside {len(meas)} measured directly")
    viol = 0; checked = 0
    for rho, mem in lad.items():
        mem.sort()
        for (d1, r1), (d2, r2) in zip(mem, mem[1:]):
            checked += 1
            for key in ('a', 'mult_det', 'mult_red'):
                if r1.get(key) is not None and r2.get(key) is not None and r1[key] > r2[key]: viol += 1
            if r1.get('mult_red') is not None and r2.get('mult_red') is not None and (r1['a'] - r1['mult_red']) > (r2['a'] - r2['mult_red']): viol += 1
            if (r1['a'] - r1['mult_det']) > (r2['a'] - r2['mult_det']): viol += 1
    print(f"ladder monotonicity check on measured pairs (a, mult_det, mult_red, i_det, i_red non-decreasing in δ): {checked} consecutive pairs, {viol} violations")
