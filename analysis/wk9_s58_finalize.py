#!/usr/bin/env python3
"""Session 58 -- summarise the long-weight screen check into the calibration file and the report."""
import gzip, json, os, sys, glob
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
seen = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'results', 's58_longweight_*.jsonl.gz'))):
    try:
        with gzip.open(f, 'rt') as fh:
            for ln in fh:
                r = json.loads(ln)
                key = (r['delta'], tuple(r['lam']))
                if key in seen:
                    assert seen[key]['sk'] == r['sk'], ("two workers disagree", key)
                    continue
                seen[key] = r
    except EOFError:
        pass
rows = list(seen.values())
byd = {}
for r in rows:
    d = byd.setdefault(r['delta'], {'cells': 0, 'bad': 0, 'time': 0.0, 'max': 0.0, 'maxcell': None, 'maxsk': 0, 'maxskcell': None})
    d['cells'] += 1; d['bad'] += (not r['ok']); d['time'] += r['time']
    if r['time'] > d['max']:
        d['max'] = r['time']; d['maxcell'] = r['lam']
    if r['sk'] > d['maxsk']:
        d['maxsk'] = r['sk']; d['maxskcell'] = r['lam']
banked = {8: 1479, 9: 4131, 10: 9975, 11: 19552, 12: 34830}
lines = ["| δ | `N` | cells with `m_det ≥ 0` in the screen | checked here | disagreements | mean / max time per cell | largest `sk` |",
         "|---|---|---|---|---|---|---|"]
tot = bad = 0
for delta in sorted(banked):
    d = byd.get(delta, {'cells': 0, 'bad': 0, 'time': 0.0, 'max': 0.0, 'maxcell': None, 'maxsk': 0, 'maxskcell': None})
    tot += d['cells']; bad += d['bad']
    lines.append("| %d | %d | %d | **%d** | **%d** | %.3f s / %.2f s at `%s` | %d at `%s` |" % (
        delta, 4 * delta, banked[delta], d['cells'], d['bad'], d['time'] / max(d['cells'], 1), d['max'],
        '(' + ','.join(map(str, d['maxcell'] or [])) + ')', d['maxsk'], '(' + ','.join(map(str, d['maxskcell'] or [])) + ')'))
text = ("The 69 967 cells of `results/longweight_screen.csv` with a banked `m_det` (lengths "
        "6–10, δ = 8–12, `N` up to 48, values by the s39 C engine): **%d checked, %d disagreements**"
        " (`results/s58_longweight_*.jsonl.gz`, `wk9_s58_sk.py longweight`).\n\n" % (tot, bad)) + "\n".join(lines) + "\n"
rep = os.path.join(ROOT, 'docs', 's58_report.md')
s = open(rep).read()
if 'LONGWEIGHT_PLACEHOLDER' in s:
    s = s.replace('LONGWEIGHT_PLACEHOLDER', text)
    s = s.replace('| **the long-weight screen (s39), lengths 6–10, δ = 8–12, `N` up to 48** | see §3a | see §3a |',
                  '| **the long-weight screen (s39), lengths 6–10, δ = 8–12, `N` up to 48** | **%d** | **%d** |' % (tot, bad))
    open(rep, 'w').write(s)
# the boundary family (integrator's note) into the calibration file too
brows = json.load(open(os.path.join(ROOT, 'results', 's58_boundary.json')))
bl = ["| `k` | `m` | `δ` | `N` | `λ` | `g` | `sk` | integrator | brute | house | s39 engine |", "|---|---|---|---|---|---|---|---|---|---|---|"]
nb = 0
for r in brows:
    def col(key, agree):
        if key not in r:
            return '—'
        v = r[key]
        v = v[0] if isinstance(v, list) and key == 'integrator' else (v[2] if isinstance(v, list) else v)
        return "%s %s" % (v, '✓' if r.get(agree) else '**✗**')
    nb += not all(r.get(k_, True) for k_ in ('pieri_agree', 'integrator_agree', 'brute_agree', 'house_agree', 's39_agree'))
    bl.append("| %d | %d | %d | %d | `(%s)` | %d | **%d** | %s | %s | %s | %s |" % (
        r['k'], r['m'], r['delta'], r['N'], ','.join(map(str, r['lam'])), r['g'], r['sk'],
        ("%d/%d %s" % (r['integrator'][0], r['integrator'][1], '✓' if r['integrator_agree'] else '**✗**')) if 'integrator' in r else '—',
        col('brute', 'brute_agree'), col('house', 'house_agree'), col('s39_engine', 's39_agree')))
btext = ("The family `(3k+2m, k, 2^m)`, `δ = k+m`, on which `2δ = |ρ| + ρ₁` holds with equality as at the LMR cell "
         "(`k = 17, m = 7`); the integrator's nine direct-sum values and ten larger members against the direct routes in reach "
         "(`results/s58_boundary.json`): **%d cells, %d disagreements**.\n\n" % (len(brows), nb)) + "\n".join(bl) + "\n"
cal = os.path.join(ROOT, 'results', 's58_calibration.md')
c = open(cal).read()
if '## The long-weight screen' not in c:
    c = c.replace("| lam with > 16 rows vanish without the shortcut |", "| the boundary family (3k+2m, k, 2^m), delta = k+m, N = 12..64 | %d | **%d** |\n| the long-weight screen (s39), lengths 6-10, delta 8-12, N up to 48 | %d | **%d** |\n| lam with > 16 rows vanish without the shortcut |" % (len(brows), nb, tot, bad))
    c = c.replace("\nNo disagreement anywhere.\n", "\n## The boundary family (integrator's note)\n\n" + btext + "\n## The long-weight screen (s39)\n\n" + text + "\nNo disagreement anywhere.\n")
    open(cal, 'w').write(c)
note = os.path.join(ROOT, 'docs', 'session_58.md')
t = open(note).read()
t = t.replace('LONGWEIGHT_SUMMARY', '%d of the 69 967 long-weight screen cells (lengths 6–10, `N` up to 48)' % tot)
open(note, 'w').write(t)
print(text)
