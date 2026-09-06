#!/usr/bin/env python3
"""Session 58 -- the reach of the reduction on larger tails (report section 6).
Times sk at lam = (N - m, tail) for tails of size 40..56; cold = box weights rebuilt."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wk9_s58_sk as S

S.log_pid('s58_reach')
CELLS = [((20, 8, 4, 4, 2, 2), 20), ((24, 8, 4, 4, 2, 2), 20), ((12, 8, 8, 8, 4, 4, 2, 2), 20),
         ((24, 12, 4, 4, 2, 2), 20), ((24, 12, 8, 4, 2, 2), 22), ((28, 12, 8, 4, 2, 2), 22)]
rows = []
for tail, delta in CELLS:
    m, N = sum(tail), 4 * delta
    lam = (N - m,) + tail
    S._BOX.clear(); st = {}
    t0 = time.time(); g, A, sk = S.sk_reduced(lam, delta, 4, st); t1 = time.time()
    t2 = time.time(); S.sk_reduced(lam, delta, 4); t3 = time.time()
    row = {'m': m, 'rows': len(tail), 'lam': list(lam), 'delta': delta, 'N': N, 'g': g, 'A': A, 'sk': sk,
           'cold': round(t1 - t0, 1), 'warm': round(t3 - t2, 2), 'terms': st['terms'], 'inner_ops': st['inner_ops'],
           'p_m': S.num_partitions(m), 'tail_states': len(S.sub_partitions(tail))}
    rows.append(row); print(json.dumps(row)); sys.stdout.flush()
    json.dump(rows, open(os.path.join(S.ROOT, 'results', 's58_reach.json'), 'w'), indent=1)
