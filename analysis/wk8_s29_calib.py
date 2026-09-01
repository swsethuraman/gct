#!/usr/bin/env python3
"""Session 29 -- calibration battery.  Nothing new is trusted until this passes."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import measure, det_form, per_form, per_padded
from wk8_s29_pleth import amb, a_of, parts

ok = True
def ck(nm, got, want):
    global ok
    g = got == want; ok &= g
    print(("PASS " if g else "FAIL ") + nm + "   got=%s want=%s" % (got, want))

d3, N3 = det_form(3); p3, _ = per_form(3)
d4, N4 = det_form(4); pd, Np = per_padded(3, 4)

# 1. a from the raising-operator kernel == plethysm
bad = []
for (n, rmax, dmax) in ((3, 4, 5), (4, 4, 5)):
    for delta in range(1, dmax + 1):
        A = amb(delta, n, 16)
        for lam in parts(n * delta):
            if len(lam) > rmax: continue
            r = max(2, len(lam))
            g = measure(d3 if n == 3 else d4, N3 if n == 3 else N4,
                        n, r, delta, lam)['a']
            if g != A.get(lam, 0): bad.append((n, delta, lam, g, A.get(lam, 0)))
ck("kernel dim == plethysm, n=3 and n=4, length<=4, delta<=5", bad, [])

# 2. a((delta^4), delta) row
ck("a((d^4),d), d=1..8", [a_of((d,) * 4, d, 4, 4) for d in range(1, 9)],
   [0, 0, 0, 1, 0, 1, 1, 3])

# 3. session 26's five cells (n=3)
S26 = [((12, 6), 6, 2, 2), ((15, 6), 7, 2, 2), ((9, 4, 2), 5, 2, 2),
       ((12, 4, 2), 6, 2, 2), ((13, 6, 2), 7, 3, 3)]
bad3 = []
for lam, delta, aw, mw in S26:
    m = measure(d3, N3, 3, max(2, len(lam)), delta, lam)
    mp = measure(p3, N3, 3, max(2, len(lam)), delta, lam)
    if (m['a'], m['mult'], mp['mult']) != (aw, mw, mw):
        bad3.append((lam, delta, m, mp))
ck("session 26's five cells (a, mult_det, mult_per)", bad3, [])

# 4. mult = a at all n=3 weights with a>0 and delta<=4  (the paper's 1,6,31 row)
bad4, cells = [], 0
for delta in range(1, 5):
    for lam, av in sorted(amb(delta, 3, 9).items()):
        cells += 1
        m = measure(d3, N3, 3, max(2, len(lam)), delta, lam)
        if not (m['a'] == av and m['mult'] == av): bad4.append((delta, lam, av, m))
ck("mult_det = a at all %d weights, n=3, delta<=4" % cells, bad4, [])

# 5. the 19-cell table at n=4, delta=5: mult = a on both sides
A5 = amb(5, 4, 16)
cells19 = sorted([(l, v) for l, v in A5.items() if v >= 2 and len(l) >= 4],
                 key=lambda x: (-x[1], x[0]))
ck("the delta=5 gate has 19 cells with a>=2 and ell>=4", len(cells19), 19)
bad5 = []
for lam, av in cells19:
    md = measure(d4, N4, 4, 4, 5, lam); mp = measure(pd, Np, 4, 4, 5, lam, seed=29)
    if not (md['a'] == av and md['mult'] == av and mp['mult'] == av):
        bad5.append((lam, av, md['mult'], mp['mult']))
ck("all 19 give mult_det = mult_pad = a", bad5, [])

print()
print("CALIBRATION PASSED" if ok else "*** CALIBRATION FAILED -- STOP ***")
