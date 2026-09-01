#!/usr/bin/env python3
"""Session 30 -- the calibration battery.  Nothing is measured until this passes."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import measure, det_form, per_form, per_padded, build_R, nullspace, P1
from wk8_s30_pleth import amb, a_of, parts

ok = True
def ck(nm, got, want):
    global ok
    g = got == want; ok &= g
    print(("PASS " if g else "FAIL ") + nm + ("   got=%s want=%s" % (got, want)
          if not g else ""))

# --- 1. THE WITNESS (kill criterion)
f1, N1 = per_padded(1, 4)
w = measure(f1, N1, 4, 2, 2, (4, 4))
ck("witness {l^3 m} lam=(4,4) delta=2 : mult = 0", w['mult'], 0)
basis, R = build_R(4, 2, 2, (4, 4))
kb = nullspace(R, len(basis), P1)[0]
ck("witness kernel == (12,-3,1)", [x % P1 for x in kb], [12 % P1, (-3) % P1, 1])

# --- 2. session 29's discriminating battery, rebuilt from session 24's closed forms
G = ({(4, 0): 1}, 2)
bad, ncells, ndisc = [], 0, 0
for d in range(1, 8):
    for b in range(0, 2 * d + 1):
        lam = (4 * d - b, b); a = a_of(lam, d, 4, 2)
        if a == 0: continue
        ncells += 1
        mt = measure(f1, N1, 4, 2, d, lam, a_expect=a)['mult']
        mg = measure(G[0], G[1], 4, 2, d, lam, a_expect=a)['mult']
        wt = 1 if (b <= d and b != 1) else 0
        wg = 1 if b == 0 else 0
        if wt < a or wg < a: ndisc += 1
        if (mt, mg) != (wt, wg): bad.append((d, b, a, mt, wt, mg, wg))
ck("discriminating battery: %d World A cells, %d with mult < a" % (ncells, ndisc),
   bad, [])

# --- 3. session 26's five cells and the n=3, delta<=4 row
d3, N3 = det_form(3); p3, _ = per_form(3)
S26 = [((12, 6), 6, 2, 2), ((15, 6), 7, 2, 2), ((9, 4, 2), 5, 2, 2),
       ((12, 4, 2), 6, 2, 2), ((13, 6, 2), 7, 3, 3)]
bad = []
for lam, delta, aw, mw in S26:
    m = measure(d3, N3, 3, max(2, len(lam)), delta, lam, a_expect=aw)
    mp = measure(p3, N3, 3, max(2, len(lam)), delta, lam, a_expect=aw)
    if (m['mult'], mp['mult']) != (mw, mw): bad.append((lam, delta, m, mp))
ck("session 26's five cells", bad, [])

bad, cells = [], 0
for delta in range(1, 5):
    for lam, av in sorted(amb(delta, 3, 9).items()):
        cells += 1
        m = measure(d3, N3, 3, max(2, len(lam)), delta, lam, a_expect=av)
        if m['mult'] != av: bad.append((delta, lam, av, m))
ck("mult_det = a at all %d weights, n=3, delta<=4" % cells, bad, [])

print()
print("CALIBRATION PASSED" if ok else "*** CALIBRATION FAILED -- STOP ***")
