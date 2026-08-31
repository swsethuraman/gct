#!/usr/bin/env python3
"""Session 27 -- calibration.  Kill criterion 2: my rank implementation must
reproduce session 26's five cells and mult = a at the 20 weights with a > 0 and
delta <= 4 at n = 3, before anything new is measured."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk7_s27_rank import measure, det_form, per_form
from wk7_s27_pleth import amb, a_of, parts

ok = True
def ck(name, got, want):
    global ok
    g = got == want; ok &= g
    print(("PASS " if g else "FAIL ") + name + "   got=%s want=%s" % (got, want))

fdet, Nd = det_form(3)
fper, Np = per_form(3)

# --- 1. the HWV kernel dimension must equal the plethysm coefficient
print("1. a from the raising-operator kernel vs the plethysm, n=3:")
bad = []
for delta in range(1, 6):
    A = amb(delta, 3, 9)
    for lam in parts(3 * delta):
        if len(lam) > 4: continue          # length <= 4 keeps it cheap
        r = max(2, len(lam))
        got = measure(fdet, Nd, 3, r, delta, lam)['a']
        want = A.get(lam, 0)
        if got != want: bad.append((delta, lam, got, want))
ck("kernel dim == plethysm on all length-<=4 weights, delta<=5", bad, [])

# --- 2. mult = a at every weight with a > 0 and delta <= 4  (the paper's row)
print("2. mult_det = a at every weight with a>0 and delta<=4 (n=3):")
cells, bad2 = 0, []
for delta in range(1, 5):
    for lam, av in sorted(amb(delta, 3, 9).items()):
        cells += 1
        r = max(2, len(lam))
        m = measure(fdet, Nd, 3, r, delta, lam, exact=True)
        if not (m['a'] == av and m['mult'] == av and m['mult_p2'] == av
                and m.get('mult_QQ') == av):
            bad2.append((delta, lam, av, m))
ck("all %d weights give mult = a (three routes)" % cells, bad2, [])

# --- 3. session 26's five cells
print("3. session 26's five measured cells:")
S26 = [((12,6),6,2,2,0), ((15,6),7,2,2,0), ((9,4,2),5,2,2,1),
       ((12,4,2),6,2,2,1), ((13,6,2),7,3,3,1)]
bad3 = []
for lam, delta, a_w, mult_w, def_w in S26:
    r = max(2, len(lam))
    m = measure(fdet, Nd, 3, r, delta, lam, exact=True)
    mp = measure(fper, Np, 3, r, delta, lam)
    got = (m['a'], m['mult'], mp['mult'])
    print("   lam=%-10s delta=%d : a=%d mult_det=%d (p2=%d, QQ=%s) mult_per=%d"
          % (str(lam), delta, m['a'], m['mult'], m['mult_p2'],
             m.get('mult_QQ'), mp['mult']))
    if (m['a'], m['mult']) != (a_w, mult_w): bad3.append((lam, delta, got))
ck("all five cells reproduce session 26's a and mult_det", bad3, [])

print()
print("CALIBRATION PASSED" if ok else "*** CALIBRATION FAILED -- STOP ***")
