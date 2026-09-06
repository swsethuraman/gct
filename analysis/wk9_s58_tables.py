#!/usr/bin/env python3
"""Session 58 -- render the cost-curve tables of docs/s58_report.md from the JSON records."""
import json, os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
d = json.load(open(os.path.join(ROOT, 'results', 's58_costcurve.json')))
e = {r['N']: r for r in json.load(open(os.path.join(ROOT, 'results', 's58_engine_curve.json')))}
def th(x): return "{:,}".format(x).replace(',', ' ')
print("| δ | N | `sk` | `g` | `A` | cold | warm | #β | s39 C engine: build + cell | engine memo |")
print("|---|---|---|---|---|---|---|---|---|---|")
for r in d['fixed_tail']:
    N = r['N']
    eng = ("%.1f s + %.2f s" % (e[N]['build_s'], e[N]['cell_s'])) if N in e else ("beyond `NMAX = 64`" if N == 68 else "")
    memo = ("%.1f M" % (e[N]['memo_after_cell'] / 1e6)) if N in e else ("—" if N == 68 else "")
    b = "**" if N == 96 else ""
    print("| %s%d%s | %s%d%s | %s%s%s | %s%s%s | %s%s%s | %.1f s | %.2f s | %s | %s | %s |" % (
        b, r['delta'], b, b, N, b, b, th(r['sk']), b, b, th(r['g']), b, b, th(r['A']), b, r['cold'], r['warm'], th(r['betas']), eng, memo))
print()
print("| `m` | `λ` | `sk` | cold | warm | terms | inner ops |")
print("|---|---|---|---|---|---|---|")
for r in d['growing_tail']:
    if r['m'] in (4, 8, 12, 16, 20, 24, 28) and not (r['m'] == 8 and r['lam'][1] == 4):
        print("| %d | (%s) | %s | %.2f s | %.2f s | %d | %s |" % (r['m'], ','.join(map(str, r['lam'])), th(r['sk']), r['cold'], r['warm'], r['terms'], th(r['inner_ops'])))
print()
hp = d['house_python']
print("| route | " + " | ".join("N = %d" % r['N'] if i == 0 else str(r['N']) for i, r in enumerate(hp)) + " | growth per +4 |")
print("|---|" + "---|" * (len(hp) + 1))
ratio = hp[-1]['time'] / hp[-2]['time']; mratio = hp[-1]['memo'] / hp[-2]['memo']
print("| house Python `m_det`, peaked cell `(N−8,2⁴)` | " + " | ".join(("%.2f s" % r['time']) if r['time'] < 1 else ("%.1f s" % r['time']) for r in hp) +
      " | ×%.1f (memo ×%.1f: %s entries at %d) |" % (ratio, mratio, th(hp[-1]['memo']), hp[-1]['N']))
w = [r['warm'] for r in d['fixed_tail']]
print("\nwarm range: %.2f–%.2f s; cold at N=96: %.1f s" % (min(w), max(w), d['fixed_tail'][-1]['cold']))
