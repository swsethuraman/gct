#!/usr/bin/env python3
"""Session 58 -- sk at the LMR weights of the other n (deliverable 4 context):
n=3 (19,7,2^5)/12, n=5 (151,31,2^9)/40, with the n x delta rectangle."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wk9_s58_sk as S
S.log_pid('s58_lmrfamily')
out = []
for n, lam, delta in [(3, (19, 7) + (2,) * 5, 12), (5, (151, 31) + (2,) * 9, 40)]:
    st = {}
    t0 = time.time(); g, A, sk = S.sk_reduced(lam, delta, n, st); t1 = time.time()
    row = {'n': n, 'lam': list(lam), 'delta': delta, 'N': n * delta, 'g': g, 'A': A, 'sk': sk, 'ak': (g - A) // 2,
           'time': round(t1 - t0, 1), 'terms': st['terms'], 'sizes': st['sizes'], 'inner_ops': st['inner_ops']}
    print(json.dumps(row)); sys.stdout.flush()
    out.append(row)
    json.dump(out, open(os.path.join(S.ROOT, 'results', 's58_lmrfamily.json'), 'w'), indent=1)
