#!/usr/bin/env python3
"""Session 27 -- C: measure the nineteen gate cells at n=4, delta=5."""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk7_s27_rank import measure, det_form, per_padded
from wk7_s27_pleth import amb

f4, N4 = det_form(4)
fp, Np = per_padded(3)
A = amb(5, 4, 16)
cells = sorted([(l, v) for l, v in A.items() if v >= 2 and len(l) >= 4],
               key=lambda x: (-x[1], x[0]))
print("lam                a  |basis| mult_det        mult_pad         D   verdict")
rows, hits = [], []
for lam, a in cells:
    t0 = time.time()
    # two primes always; exact Q additionally where the weight space is small.
    # NB a rank attaining `a` is a CERTIFICATE: rank_p <= rank_Q <= a, so
    # mult_p = a forces mult_Q = a.  Exact Q is only needed if a cell falls short.
    md = measure(f4, N4, 4, 4, 5, lam)
    mp = measure(fp, Np, 4, 4, 5, lam, seed=29)
    assert md['a'] == a == mp['a'], (lam, a, md, mp)
    small = md['nbasis'] <= 200
    if small:
        md = measure(f4, N4, 4, 4, 5, lam, exact=True)
        mp = measure(fp, Np, 4, 4, 5, lam, exact=True, seed=29)
    for m in (md, mp):
        assert m['mult'] == m['mult_p2'], (lam, m)
        if small: assert m['mult'] == m['mult_QQ'], (lam, m)
        if m['mult'] < a:
            m2 = measure(f4 if m is md else fp, N4 if m is md else Np,
                         4, 4, 5, lam, npts=3 * a + 12, seed=101)
            assert m2['mult'] == m['mult'], ("short rank unstable", lam, m, m2)
    D = mp['mult'] - md['mult']
    rows.append((lam, a, md['nbasis'], md['mult'], mp['mult'], D))
    if D > 0: hits.append(rows[-1])
    print("%-16s %2d %6d   %d (=a? %-3s)  %d (=a? %-3s) %+3d  %s   [%.1fs]"
          % (str(lam), a, md['nbasis'], md['mult'], md['mult'] == a,
             mp['mult'], mp['mult'] == a, D,
             "OBSTRUCTION" if D > 0 else "no obstruction", time.time() - t0))
    sys.stdout.flush()
print()
nd = sum(1 for r in rows if r[3] < r[1]); npd = sum(1 for r in rows if r[4] < r[1])
print("weights with mult_det   < a : %d of %d" % (nd, len(rows)))
print("weights with mult_pad   < a : %d of %d" % (npd, len(rows)))
print("weights with D > 0          : %d" % len(hits))
print("weights with D = 0          : %d" % sum(1 for r in rows if r[5] == 0))
print("weights with D < 0          : %d" % sum(1 for r in rows if r[5] < 0))
if hits:
    print("\n*** MULTIPLICITY OBSTRUCTION(S) FOUND -- STOP AND VERIFY ***")
    for h in hits: print("   ", h)
