#!/usr/bin/env python3
"""
Session 34 -- regenerate the GEN-marked blocks of docs/d7_sweep.md from
results/d7_ledger.md + results/d7_cells.json.  Tables are generated, not typed.
Usage: wk9_s34_report.py [--stdout]
"""
import os, re, json, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def rows():
    out = []
    for ln in open(os.path.join(ROOT, 'results', 'd7_ledger.md')):
        m = re.match(r'\| \((\d+(?:, \d+)*)\) \| (\d+) \| (\d+) \| (\d+) \| (\d+|—) \| (\d+|—) \| ([+\-]\d+|—) \| ?([^|]*)\|', ln)
        if m:
            lam = tuple(int(x) for x in m.group(1).split(', '))
            out.append(dict(lam=lam, ell=int(m.group(2)), a=int(m.group(3)),
                            ns=int(m.group(4)),
                            md=None if m.group(5) == "—" else int(m.group(5)),
                            mp=None if m.group(6) == "—" else int(m.group(6)),
                            D=None if m.group(7) == "—" else int(m.group(7)),
                            flag=m.group(8).strip()))
    return out

def gen():
    R = rows()
    meas = [r for r in R if r['md'] is not None and 'EXT' not in r['flag']]
    ext = [r for r in R if r['md'] is not None and 'EXT' in r['flag']]
    defer = [r for r in R if r['md'] is None]
    d = json.load(open(os.path.join(ROOT, 'results', 'd7_cells.json')))
    cells = d['cells']
    for c in cells: c['lam'] = tuple(c['lam'])
    feas = [c for c in cells if c['feas_s34']]
    munits = sum(r['a'] for r in meas)
    funits = sum(c['a'] for c in feas)
    units = sum(c['a'] for c in cells)
    completed_defer = {r['lam'] for r in meas} & {r['lam'] for r in defer}

    T = []
    T.append("**The feasible 46, in banked order** (%d measured, %d deferred%s):\n" %
             (len(meas), len([r for r in defer if r['lam'] not in completed_defer]),
              "; a DEFER row followed by a measured row means the cell was "
              "deferred, then completed when memory allowed" if completed_defer else ""))
    T.append("\n| lam | ell | a | `N_S` | `mult_det` | `mult_pad` | `D` | balance | flag |")
    T.append("\n|---|---|---|---|---|---|---|---|---|\n")
    for r in R:
        if 'EXT' in r['flag']: continue
        T.append("| `%s` | %d | %d | %d | %s | %s | %s | %d | %s |\n"
                 % (str(r['lam']), r['ell'], r['a'], r['ns'],
                    "—" if r['md'] is None else r['md'],
                    "—" if r['mp'] is None else r['mp'],
                    "—" if r['D'] is None else "%+d" % r['D'],
                    r['lam'][0] - r['lam'][-1], r['flag'] or ""))
    if ext:
        T.append("\n**Extension beyond the pre-registered frontier** (flag `EXT`, "
                 "admitted by the observed-constant rule of PREREG_s34.md §4, "
                 "after the feasible set was exhausted):\n")
        T.append("\n| lam | ell | a | `N_S` | `mult_det` | `mult_pad` | `D` | balance |\n")
        T.append("|---|---|---|---|---|---|---|---|\n")
        for r in ext:
            T.append("| `%s` | %d | %d | %d | %d | %d | %+d | %d |\n"
                     % (str(r['lam']), r['ell'], r['a'], r['ns'], r['md'], r['mp'],
                        r['D'], r['lam'][0] - r['lam'][-1]))
    table = "".join(T)

    allmeas = meas + ext
    aunits = sum(r['a'] for r in allmeas)
    C = []
    C.append("**Coverage: %d of the 46 feasible cells (%.0f%%), carrying %d of their %d ambient units (%.0f%%)"
             % (len(meas), 100.0 * len(meas) / len(feas), munits, funits, 100.0 * munits / funits))
    if ext:
        C.append("; plus %d extension cell(s) beyond the frontier, for %d of the census's %d units (%.1f%%) overall"
                 % (len(ext), aunits, units, 100.0 * aunits / units))
    else:
        C.append(" — %d of the census's %d units (%.1f%%)" % (munits, units, 100.0 * munits / units))
    C.append(".**\n\n")
    C.append("| axis | measured | feasible 46 | full census (433) |\n|---|---|---|---|\n")
    def rng(key, cs):
        if not cs: return "—"
        vs = [c[key] if key in c else c['lam'][0] - c['lam'][-1] for c in cs]
        return "%d – %d" % (min(vs), max(vs))
    def rngr(key):
        vs = [r[key] if key != 'balance' else r['lam'][0] - r['lam'][-1] for r in allmeas]
        return "%d – %d" % (min(vs), max(vs))
    C.append("| `N_S` | %s | %s | %s |\n" % (rngr('ns'), rng('ns', feas), rng('ns', cells)))
    C.append("| `a` | %s | %s | %s |\n" % (rngr('a'), rng('a', feas), rng('a', cells)))
    C.append("| balance | %s | %s | %s |\n" % (rngr('balance'), rng('balance', feas), rng('balance', cells)))
    C.append("| `ell` | %s | 5 – 5 | 5 – 7 |\n" % rngr('ell'))
    bites = [r for r in allmeas if r['md'] < r['a'] or r['mp'] < r['a']]
    C.append("\nEvery banked row: prime-pair agreement, `a` = plethysm value, "
             "`rank(R) = N_S − a`, `N_S` = census DP value — all asserted in-run.  ")
    if bites:
        C.append("**Cells below the ambient cap: %d** — see the sceptical-branch records in `results/d7_kernels/`.\n"
                 % len(bites))
    else:
        C.append("No cell fell below the ambient cap on either side, so the sceptical "
                 "re-run branch was never entered.\n")
    coverage = "".join(C)
    return table, coverage

if __name__ == '__main__':
    table, coverage = gen()
    if '--stdout' in sys.argv:
        print(table); print("\n----\n"); print(coverage); sys.exit(0)
    p = os.path.join(ROOT, 'docs', 'd7_sweep.md')
    txt = open(p).read()
    txt = re.sub(r'<!--GEN:TABLE-->.*?<!--/GEN:TABLE-->',
                 '<!--GEN:TABLE-->\n' + table + '<!--/GEN:TABLE-->', txt, flags=re.S)
    txt = re.sub(r'<!--GEN:COVERAGE-->.*?<!--/GEN:COVERAGE-->',
                 '<!--GEN:COVERAGE-->\n' + coverage + '<!--/GEN:COVERAGE-->', txt, flags=re.S)
    open(p, 'w').write(txt)
    print("docs/d7_sweep.md GEN blocks regenerated")
