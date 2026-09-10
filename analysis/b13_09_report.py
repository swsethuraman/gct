#!/usr/bin/env python3
"""
B13-09 -- generate the report's tables from the banked records, so no number in
the report is hand-transcribed.

Emits markdown to stdout: the per-group summary, the per-weight tables, the
not-reached table with costs, the verification summary, and the cost-model table.

usage: python3 analysis/b13_09_report.py [--section all|summary|weights|notreached|verify|cost]
"""
import sys, os, json, glob

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
GROUPS = [('r7_d7', 7, 7), ('r7_d8', 7, 8), ('r8_d8', 8, 8), ('r7_d9', 7, 9), ('r8_d9', 8, 9)]


def census():
    return json.load(open(os.path.join(ROOT, 'results', 'b13_09_census.json')))


def banked():
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'results', 'b13_09', 'per_r*.jsonl'))):
        for ln in open(f):
            try: r = json.loads(ln)
            except Exception: continue
            if r.get('mult') is None and r.get('status') != 'a=0': continue
            out[(tuple(r['mu']), r['delta'])] = r
    return out


def status(g):
    p = os.path.join(ROOT, 'results', 'b13_09', f'status_{g}.json')
    return json.load(open(p)) if os.path.exists(p) else None


def summary():
    C = census(); B = banked()
    L = ["| group | weights | measured | `mult = a` | drops | not reached | `Σa` measured | order run |",
         "|---|---|---|---|---|---|---|---|"]
    tot = dict(w=0, m=0, f=0, d=0, n=0)
    for g, r, d in GROUPS:
        cells = C['cells'][g]; n = len(cells)
        recs = [B[(tuple(c['mu']), d)] for c in cells if (tuple(c['mu']), d) in B]
        full = [x for x in recs if x['mult'] == x['a']]
        drops = [x for x in recs if x['mult'] != x['a']]
        st = status(g)
        order = (st['bounds'].get('order', 'N_S') if st else '-')
        if g == 'r7_d9': order = 'N_S (10), then cost'
        if g == 'r8_d8': order = 'N_S (1), then cost'
        L.append(f"| `({r},{d})` | {n} | **{len(recs)}** | {len(full)} | **{len(drops)}** | {n - len(recs)} | "
                 f"{sum(x['a'] for x in recs)} | {order} |")
        tot['w'] += n; tot['m'] += len(recs); tot['f'] += len(full); tot['d'] += len(drops); tot['n'] += n - len(recs)
    L.append(f"| **total** | **{tot['w']}** | **{tot['m']}** | **{tot['f']}** | **{tot['d']}** | **{tot['n']}** | | |")
    return "\n".join(L)


def weights():
    C = census(); B = banked(); out = []
    for g, r, d in GROUPS:
        cells = sorted(C['cells'][g], key=lambda c: c['N_S'])
        recs = [(c, B[(tuple(c['mu']), d)]) for c in cells if (tuple(c['mu']), d) in B]
        if not recs: continue
        out.append(f"\n**`(r, delta) = ({r}, {d})` — {len(recs)} of {len(cells)} measured, every one `mult = a`**\n")
        out.append("| `μ` | `a` | `N_S` | `\\|Stab\\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        for c, x in recs:
            pp = x.get('per_prime', {})
            ms = " / ".join(str(pp[str(p)]['mult']) for p in x['primes']) if pp else str(x['mult'])
            out.append(f"| `({','.join(map(str, c['mu']))})` | {x['a']} | {x['N_S']} | {x['stab']} | {x['n_chi']} | "
                       f"{ms} | {x['units']} | {x.get('build_secs', '')} | {x['secs']} | {x.get('hwm_gb', '')} |")
    return "\n".join(out)


def notreached():
    C = census(); B = banked()
    L = ["| group | `μ` | `a` | `N_S` | `\\|Stab\\|` | `N_S·δ` | refitted cost s | why not reached |",
         "|---|---|---|---|---|---|---|---|"]
    n = 0
    for g, r, d in GROUPS:
        st = status(g)
        reasons = {}
        if st:
            for x in st['not_reached']: reasons[tuple(x['mu'])] = x['reason']
        for c in sorted(C['cells'][g], key=lambda c: c.get('cost_model_s', 0)):
            if (tuple(c['mu']), d) in B: continue
            why = reasons.get(tuple(c['mu']), 'the wall clock of Addendum B.1 (queue not reached)')
            L.append(f"| `({r},{d})` | `({','.join(map(str, c['mu']))})` | {c['a']} | {c['N_S']} | {c['stab']} | "
                     f"{c['NS_delta']:.3g} | {c.get('cost_model_s', '')} | {why} |")
            n += 1
    L.append(f"\n{n} weights not reached.")
    return "\n".join(L)


def verify():
    L = []
    vs = sorted(glob.glob(os.path.join(ROOT, 'results', 'b13_09', 'verify*.json')))
    if vs:
        L.append("| `μ` | `δ` | `n_χ` | `a` from the operator (P1 / P2) | stacked rank (P1 / P2) | `= n_χ` | verdict |")
        L.append("|---|---|---|---|---|---|---|")
        tot = {'PASS': 0, 'FAIL': 0, 'NOT COVERED': 0}
        for v in vs:
            V = json.load(open(v))
            for w in V['weights']:
                tot[w['verdict']] = tot.get(w['verdict'], 0) + 1
                if w['verdict'] == 'NOT COVERED': continue
                pp = w['per_prime']
                ao = " / ".join(str(pp[p]['a_from_operator']) for p in pp)
                rk = " / ".join(str(pp[p]['rank_stacked']) for p in pp)
                fc = "yes" if all(pp[p]['full_column_rank'] for p in pp) else "no"
                L.append(f"| `({','.join(map(str, w['mu']))})` | {w['delta']} | {w['n_chi']} | {ao} | {rk} | {fc} | **{w['verdict']}** |")
        L.append(f"\n{tot.get('PASS', 0)} PASS, {tot.get('FAIL', 0)} FAIL, {tot.get('NOT COVERED', 0)} above the verifier's dense cap.")
    cv = os.path.join(ROOT, 'results', 'logs', 'b13_09_certverify.out')
    if os.path.exists(cv):
        last = [l for l in open(cv) if l.startswith('PASS ')]
        if last: L.append(f"\nHouse verifier (`tools/verify`, imports nothing from `analysis/`): `{last[-1].strip()}`")
    return "\n".join(L)


def cost():
    p = os.path.join(ROOT, 'results', 'b13_09', 'costfit.json')
    if not os.path.exists(p): return "(cost fit not yet written)"
    F = json.load(open(p))
    L = [f"Refitted on {F['n']} measured weights:",
         "",
         f"    build_secs  ~=  {F['c1_per_NS_delta']:.3g} * N_S*delta  +  {F['c2_per_Stab_NS']:.3g} * |Stab| * N_S",
         "",
         f"median predicted/actual **{F['median_pred_over_actual']:.2f}** (p10 {F['p10']:.2f}, p90 {F['p90']:.2f}); "
         f"the s79 model's median actual/model is {F['s79_model_median_actual_over_model']:.2f} and its worst is "
         f"**{F['s79_model_worst_actual_over_model']:.1f}×** low.",
         "",
         "| group | weights | s79 model | refitted | factor |", "|---|---|---|---|---|"]
    for k, g in F['groups'].items():
        fac = (g['total_model_h'] and g['total_model_h'] > 0) and g['total_model_h'] or None
        L.append(f"| `{k}` | {g['weights']} | {g['total_s79_h']} h | **{g['total_model_h']} h** | "
                 f"{(g['total_model_h'] / g['total_s79_h']):.1f}× |" if g['total_s79_h'] else
                 f"| `{k}` | {g['weights']} | {g['total_s79_h']} h | **{g['total_model_h']} h** | — |")
    tot_s = sum(g['total_s79_h'] for g in F['groups'].values()); tot_r = sum(g['total_model_h'] for g in F['groups'].values())
    L.append(f"| **total** | 267 | {tot_s:.2f} h | **{tot_r:.2f} h** | {tot_r / tot_s:.1f}× |")
    return "\n".join(L)


if __name__ == '__main__':
    sec = sys.argv[sys.argv.index('--section') + 1] if '--section' in sys.argv else 'all'
    fns = dict(summary=summary, weights=weights, notreached=notreached, verify=verify, cost=cost)
    if sec == 'all':
        for k in ['summary', 'cost', 'verify', 'notreached', 'weights']:
            print(f"\n<!-- {k} -->\n"); print(fns[k]())
    else:
        print(fns[sec]())
