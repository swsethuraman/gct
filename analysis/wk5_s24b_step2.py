#!/usr/bin/env python3
"""Session 24b -- STEP 2: the permanent's deficit at n = m = 3 (Sym^3 C^9)."""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import partitions, m_det, plethysm_schur
from wk5_s24b_per import m_per3

DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3
SPOT = 3   # spot-check route 1 against route 2 on this many weights per degree

print("STEP 2.  Same ambient Sym^3 C^9, no padding: det_3 against per_3.")
print("mult <= min(m, ambient); the ambient plethysm is 0/1 in this range, so")
print("def is pinned exactly wherever the ambient vanishes.\n")

for delta in range(1, DMAX + 1):
    amb = plethysm_schur(delta, 3, 9)
    t0 = time.time()
    rows = []
    sum_mdet = sum_mper = 0
    for lam in partitions(3 * delta):
        if len(lam) > 9: continue
        md = m_det(lam, 3, delta)
        mp = m_per3(lam, delta, 2)          # route 2 (fast) for the sweep
        a = amb.get(lam, 0)
        if md or mp or a:
            rows.append((lam, md, mp, a))
        sum_mdet += md; sum_mper += mp
    print("delta = %d   (%d partitions, %.1fs)" % (delta, len(rows), time.time()-t0))
    print("   lam                m_det  m_per  ambient   P=m_per-m_det   def_det  def_per")
    for lam, md, mp, a in rows:
        # mult is 0 where ambient is 0; where ambient is 1, mult is 0 or 1
        if a == 0:
            dd, dp = str(md), str(mp)
        else:
            dd, dp = "%d|%d" % (md-1, md), "%d|%d" % (mp-1, mp)
        print("   %-18s %5d %6d %8d %14d   %7s %8s"
              % (str(lam), md, mp, a, mp - md, dd, dp))
    print("   sum m_det = %d , sum m_per = %d , sum ambient = %d"
          % (sum_mdet, sum_mper, sum(amb.values())))
    print("   => total deficit det = %d (if every ambient piece survives)"
          % (sum_mdet - sum(amb.values())))
    print("   => total deficit per = %d (same proviso)"
          % (sum_mper - sum(amb.values())))
    print("   weights with m_per < m_det (screen passes here):",
          [lam for lam, md, mp, a in rows if mp < md] or "NONE")
    # two-route spot check
    import random
    random.seed(24)
    sample = rows[:SPOT] + random.sample(rows, min(SPOT, len(rows)))
    for lam, md, mp, a in sample:
        r1 = m_per3(lam, delta, 1)
        assert r1 == mp, ("ROUTE MISMATCH", lam, r1, mp)
    print("   two-route check: Jacobi-Trudi == Schur-Weyl on %d sampled weights"
          % len(sample))
    print()
