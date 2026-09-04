#!/usr/bin/env python3
"""Exact N_S and n_chi for every six-row cell of a given degree, cached to
results/s46_census<delta>.jsonl (append-only; re-running skips what is there)."""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
R = os.path.join(HERE, '..', 'results')
from wk9_s46_census import census_cell
from wk9_s46_reach import partitions, census_a

if __name__ == '__main__':
    delta = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    path = os.path.join(R, f's46_census{delta}.jsonl')
    have = set()
    if os.path.exists(path):
        for l in open(path):
            d = json.loads(l); have.add(tuple(d['lam']))
    a_tab = census_a()
    todo = [lam for lam in partitions(4 * delta, 6, 4 * delta)
            if (lam, delta) in a_tab and lam not in have]
    print(f"{len(todo)} cells to do at delta={delta} ({len(have)} cached)", file=sys.stderr)
    for k, lam in enumerate(todo):
        t = time.time()
        N_S, n_chi, stab, _ = census_cell(lam, delta)
        a, m_det = a_tab[(lam, delta)]
        rec = dict(lam=list(lam), delta=delta, N_S=N_S, n_chi=n_chi, stab=stab, a=a,
                   m_det=m_det, bal=lam[0] - lam[-1], elig=lam[0] >= delta,
                   secs=round(time.time() - t, 2))
        with open(path, 'a') as f: f.write(json.dumps(rec) + "\n")
        if k % 25 == 0: print(f"  {k}/{len(todo)} {lam} n_chi={n_chi} ({time.time()-t:.1f}s)", file=sys.stderr)
    print("done", file=sys.stderr)
