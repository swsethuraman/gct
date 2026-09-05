#!/usr/bin/env python3
"""
Session 54 -- census of length-5 weights for the R_5 vs D_5^{det_4} test.

Only weights of length EXACTLY 5 can distinguish R_5 from D_5^{det_4}:
a length-k highest-weight vector sees only the restriction to a k-plane
(restriction lemma, washout_lemma.md sec 1), and for k <= 4 that restriction
lands in D_4^{det_4}, which already contains R_4 (exact block construction,
s27/s32). So mult_red <= mult_det automatically at length <= 4; the test is at
length exactly 5.
"""
import sys, time, json
sys.path.insert(0, 'analysis')
from wk8_s30_pleth import a_of, amb

N = 4   # n=4 (quartic), r=5

def length5_weights(delta):
    A = amb(delta, N, 5)
    out = []
    for lam, a in A.items():
        L = tuple(x for x in lam if x)
        if len(L) == 5 and a > 0:
            out.append((L, int(a)))
    out.sort()
    return out

if __name__ == '__main__':
    deltas = [int(x) for x in sys.argv[1:]] or [6, 7, 8, 9]
    allcells = {}
    for delta in deltas:
        t0 = time.time()
        ws = length5_weights(delta)
        dt = time.time() - t0
        print(f"=== delta={delta}: {len(ws)} length-5 weights a>0 (|lam|={4*delta}), "
              f"sum a={sum(a for _,a in ws)}, {dt:.1f}s ===", flush=True)
        for lam, a in ws:
            print(f"  a={a:3d}  lam={lam}", flush=True)
        allcells[delta] = ws
    with open('results/s54_length5_census.json', 'w') as f:
        json.dump({str(k): v for k, v in allcells.items()}, f)
    print("wrote results/s54_length5_census.json", flush=True)
