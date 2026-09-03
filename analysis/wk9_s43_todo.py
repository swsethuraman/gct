#!/usr/bin/env python3
"""
Session 43 -- rebuild the reachable-but-unmeasured list from results/sixrow_census.md
directly (the brief: do not trust results/s41_coverage.md's counts; re-derive them and
report any disagreement as a finding).

Sources of "measured":
  (a) the census's own `s36` column (cells banked by session 36), and
  (b) the rows of results/s41_ledger.md (cells banked by session 41),
  (c) results/s36_ledger.md, as an independent check on (a).

Output: results/s43_todo.md, ascending in n_chi, plus a JSON pickle for the sweep.
usage: python3 wk9_s43_todo.py [--frontier 20000] [--out results/s43_todo.md] [--pkl /root/s43/todo.pkl]
"""
import sys, os, re, json, pickle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
CENSUS = os.path.join(ROOT, 'results', 'sixrow_census.md')
S41LED = os.path.join(ROOT, 'results', 's41_ledger.md')
S36LED = os.path.join(ROOT, 'results', 's36_ledger.md')
S36AONE = os.path.join(ROOT, 'results', 's36_aone.md')


def cells_of(path=CENSUS):
    """parse the two obstruction-eligible tables (lam_1 >= delta) of the census"""
    delta = None
    onset_only = False
    out = {7: [], 8: []}
    for ln in open(path):
        m = re.match(r'^##+ `δ = (\d)`', ln)
        if m:
            delta = int(m.group(1))
            onset_only = ln.startswith('###')
            continue
        if not ln.startswith('| `('):
            continue
        if delta is None or onset_only:
            continue
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        # lam | a | m_det | forced | balance | N_S | Stab | n_chi | asm | null | inpl | r15500 | r20000 | s36
        lam = tuple(int(x) for x in c[0].strip('`').strip('()').split(','))
        nchi_raw = c[7]
        approx = '~' if nchi_raw.startswith('~') else ''
        out[delta].append(dict(
            lam=lam, delta=delta, a=int(c[1]), m_det=int(c[2]),
            forced=(c[3] == 'yes'), bal=int(c[4]), N_S=int(c[5]), stab=int(c[6]),
            n_chi=int(nchi_raw.lstrip('~')), approx=approx,
            gb_inpl=float(c[10]), r15500=(c[11] == 'yes'), r20000=(c[12] == 'yes'),
            s36=c[13] if len(c) > 13 else ''))
    return out


def ledger_cells(path, deltas=(7, 8)):
    out = set()
    if not os.path.exists(path):
        return out
    for ln in open(path):
        if not ln.startswith('|'):
            continue
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        if path.endswith('s41_ledger.md'):
            if c[0] not in ('7', '8'):
                continue
            lam = tuple(int(x) for x in c[1].strip('`').strip('()').split(','))
            out.add((lam, int(c[0])))
        elif path.endswith('s36_aone.md'):  # | ell | delta | lam | a | ...
            if len(c) < 4 or not c[0].isdigit() or not c[1].isdigit():
                continue
            lam = tuple(int(x) for x in c[2].strip('`').strip('()').split(','))
            if len(lam) == 6 and int(c[1]) in deltas:
                out.add((lam, int(c[1])))
        else:  # s36 ledger: | stratum | lam | delta | ell | ...
            if len(c) < 4 or not c[2].isdigit():
                continue
            lam = tuple(int(x) for x in c[1].strip('`').strip('()').split(','))
            if len(lam) == 6 and int(c[2]) in deltas:
                out.add((lam, int(c[2])))
    return out


def main():
    frontier = int(sys.argv[sys.argv.index('--frontier') + 1]) if '--frontier' in sys.argv else 20000
    out_md = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(ROOT, 'results', 's43_todo.md')
    pkl = sys.argv[sys.argv.index('--pkl') + 1] if '--pkl' in sys.argv else '/root/s43/todo.pkl'

    cen = cells_of()
    s41 = ledger_cells(S41LED)
    s36l = ledger_cells(S36LED) | ledger_cells(S36AONE)

    findings = []
    for d in (7, 8):
        n = len(cen[d])
        units = sum(x['a'] for x in cen[d])
        claimed = {7: (258, 954), 8: (591, 10054)}[d]
        if (n, units) != claimed:
            findings.append(f"delta={d}: census header claims {claimed[0]} cells / {claimed[1]} units; "
                            f"the table itself has {n} cells / {units} units")

    todo = {7: [], 8: []}
    stats = {}
    for d in (7, 8):
        reach = [x for x in cen[d] if x['approx'] == '' and x['n_chi'] <= frontier]
        # cross-check the census reach flag against the raw n_chi
        for x in cen[d]:
            flag = x['r20000']
            calc = (x['approx'] == '' and x['n_chi'] <= 20000)
            if flag != calc:
                findings.append(f"delta={d} {x['lam']}: census `reach 20000` = {flag} but n_chi = "
                                f"{x['approx']}{x['n_chi']}")
        s36_flagged = set(x['lam'] for x in cen[d] if x['s36'])
        if s36_flagged != set(l for (l, dd) in s36l if dd == d):
            only_col = sorted(s36_flagged - set(l for (l, dd) in s36l if dd == d))
            only_led = sorted(set(l for (l, dd) in s36l if dd == d) - s36_flagged)
            if only_col or only_led:
                findings.append(f"delta={d}: census `s36` column vs the s36 ledgers differ; "
                                f"in column only: {only_col}; in ledger only: {only_led}")
        for x in reach:
            x['measured'] = bool(x['s36']) or (x['lam'], d) in s41
            x['by'] = ('s36' if x['s36'] else '') + ('s41' if (x['lam'], d) in s41 else '')
        meas = [x for x in reach if x['measured']]
        un = [x for x in reach if not x['measured']]
        un.sort(key=lambda x: (x['n_chi'], x['lam']))
        todo[d] = un
        stats[d] = dict(cells=len(cen[d]), units=sum(x['a'] for x in cen[d]),
                        reach=len(reach), reach_units=sum(x['a'] for x in reach),
                        measured=len(meas), measured_units=sum(x['a'] for x in meas),
                        todo=len(un), todo_units=sum(x['a'] for x in un))

    # compare with the counts s41_coverage.md asserts
    cov_claim = {7: dict(reach=58, measured=52), 8: dict(reach=65, measured=22)}
    for d in (7, 8):
        for k, v in cov_claim[d].items():
            if stats[d][k] != v:
                findings.append(f"delta={d}: results/s41_coverage.md says {k} = {v}; re-derived {stats[d][k]}")

    os.makedirs(os.path.dirname(pkl), exist_ok=True)
    pickle.dump(todo, open(pkl, 'wb'))

    L = []
    L.append("# Session 43 — the reachable-but-unmeasured six-row cells (`n = 4`, `ℓ(λ) = 6`, `λ_1 ≥ δ`, `a ≥ 1`)\n")
    L.append(f"Re-derived from `results/sixrow_census.md` by `analysis/wk9_s43_todo.py` at frontier "
             f"`n_χ ≤ {frontier}` (exact `n_χ` only; cells carrying the `~` bound are not counted reachable).  "
             f"`measured` = the census `s36` column (cross-checked against `results/s36_ledger.md`) or a row of "
             f"`results/s41_ledger.md`.  Order below is ascending `n_χ`, which is the order the sweep takes.\n")
    L.append("## Coverage arithmetic, re-derived\n")
    L.append("| δ | eligible cells | units | fit at 20000 | units | measured (s36+s41) | units | **unmeasured, in reach** | units |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for d in (7, 8):
        s = stats[d]
        L.append(f"| {d} | {s['cells']} | {s['units']} | {s['reach']} | {s['reach_units']} | {s['measured']} | "
                 f"{s['measured_units']} | **{s['todo']}** | {s['todo_units']} |")
    tot = sum(stats[d]['todo'] for d in (7, 8))
    tot_u = sum(stats[d]['todo_units'] for d in (7, 8))
    L.append(f"\n**Total to measure: {tot} cells, {tot_u} ambient units.**\n")
    if findings:
        L.append("## Disagreements with the inherited counts (findings)\n")
        for f in findings:
            L.append(f"- {f}")
        L.append("")
    else:
        L.append("## Disagreements with the inherited counts\n\nNone.  The re-derived counts agree with "
                 "`results/s41_coverage.md` and with the census header at both degrees.\n")
    for d in (7, 8):
        L.append(f"## `δ = {d}` — {stats[d]['todo']} cells to measure ({stats[d]['todo_units']} units)\n")
        L.append("| # | lam | a | m_det | balance | N_S | Stab | n_chi | pred GB |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        for i, x in enumerate(todo[d], 1):
            pred = 0.5 if x['n_chi'] <= 800 else 1.4e-8 * x['n_chi'] ** 2 + 0.4
            L.append(f"| {i} | `{x['lam']}` | {x['a']} | {x['m_det']} | {x['bal']} | {x['N_S']} | {x['stab']} | "
                     f"{x['n_chi']} | {pred:.2f} |")
        L.append("")
    open(out_md, 'w').write("\n".join(L))
    print(json.dumps(dict(stats=stats, findings=findings, total=tot, total_units=tot_u), indent=1))


if __name__ == '__main__':
    main()
