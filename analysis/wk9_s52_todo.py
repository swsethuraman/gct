#!/usr/bin/env python3
"""
Session 52 -- the a = 1 work list.

Reads results/s52_cells*.jsonl (this session's census) and subtracts every
a = 1, ell = 6 cell already measured, by parsing the banked ledgers themselves
(results/s36_aone.md, s36_ledger.md, s41_ledger.md, s43_ledger.md,
s45_ledger.md, s46_ledger.md) rather than any coverage summary.  Prints the
remaining informative cells (h_pad >= 1) ascending in n_chi.

usage: python3 wk9_s52_todo.py [--jsonl results/s52_cells.jsonl ...]
"""
import sys, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LEDGERS = ['results/s36_aone.md', 'results/s36_ledger.md', 'results/s41_ledger.md',
           'results/s43_ledger.md', 'results/s45_ledger.md', 'results/s46_ledger.md']
LAMRE = re.compile(r'`\((\s*\d+(?:\s*,\s*\d+)*)\s*\)`')

def banked():
    """(lam, delta) pairs appearing as a measured row in any ledger.  A row is
    a markdown table row carrying a lam in backticked tuple form; delta is read
    from the row if a standalone delta column is present, else from every
    delta the file's header declares (conservative: marks the cell measured at
    each such delta only if the row also carries that delta)."""
    out = set()
    for path in LEDGERS:
        p = os.path.join(ROOT, path)
        if not os.path.exists(p): continue
        for ln in open(p, encoding='utf-8'):
            if not ln.lstrip().startswith('|'): continue
            m = LAMRE.search(ln)
            if not m: continue
            lam = tuple(int(x) for x in m.group(1).split(','))
            cells = [c.strip().strip('`*') for c in ln.strip().strip('|').split('|')]
            # delta = the integer cell equal to |lam|/4
            d = sum(lam) // 4
            if sum(lam) != 4 * d: continue
            if any(c.isdigit() and int(c) == d for c in cells):
                out.add((lam, d))
    return out

if __name__ == '__main__':
    files = [a for a in sys.argv[1:] if a.endswith('.jsonl')]
    if not files:
        files = [os.path.join(ROOT, 'results/s52_cells.jsonl')]
    B = banked()
    rows = []
    for f in files:
        for ln in open(f):
            r = json.loads(ln)
            if r['a'] != 1: continue
            rows.append(r)
    seen = set()
    uniq = []
    for r in rows:
        k = (tuple(r['lam']), r['delta'])
        if k in seen: continue
        seen.add(k); uniq.append(r)
    for r in uniq:
        r['banked'] = (tuple(r['lam']), r['delta']) in B
    for d in sorted(set(r['delta'] for r in uniq)):
        sub = [r for r in uniq if r['delta'] == d]
        el = [r for r in sub if r['eligible']]
        inf = [r for r in el if r['informative']]
        todo = [r for r in inf if not r['banked']]
        print(f"delta={d}: a=1 ell=6 {len(sub)}; eligible {len(el)}; informative(h_pad>=1) {len(inf)}; "
              f"already banked {len([r for r in inf if r['banked']])}; TODO {len(todo)}")
    todo = sorted([r for r in uniq if r['eligible'] and r['informative'] and not r['banked']],
                  key=lambda r: (r['nchi_lb'], r['delta']))
    print(f"\nTOTAL TODO {len(todo)}, n_chi_lb from {todo[0]['nchi_lb']} to {todo[-1]['nchi_lb']}" if todo else "\nTOTAL TODO 0")
    json.dump(todo, open(os.path.join(ROOT, 'results/s52_todo.json'), 'w'), indent=0)
    for r in todo[:15]:
        print(f"   d{r['delta']} {tuple(r['lam'])}  h_pad={r['h_pad']} N_S={r['N_S']} nchi~{r['nchi_lb']}")
