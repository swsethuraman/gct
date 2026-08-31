#!/usr/bin/env python3
"""
Session 24b -- STEP 1, optimised.

The screen needs a weight with  m_perpad(lam) <= m_det(lam)  AND
m_perpad(lam) > 0 (else no obstruction is possible there at all).
So a necessary condition is  m_det(lam) >= 1.  m_det is a symmetric
rectangular Kronecker coefficient and is CHEAP; m_perpad is the expensive
one.  So: enumerate the support of m_det first, intersect with the row bound
ell(lam) <= m^2+1, and evaluate m_perpad only there.  This is exhaustive --
every weight outside the det support has m_det = 0 < m_perpad and therefore
fails the screen automatically.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import partitions, m_det
from wk5_s24b_per import m_perpad

def run(n, m, delta, route=2):
    N, u = n * delta, m * m + 1
    t0 = time.time()
    det_support = []
    nlam = 0
    for lam in partitions(N):
        if len(lam) > n * n: continue
        nlam += 1
        md = m_det(lam, n, delta)
        if md >= 1 and len(lam) <= u:
            det_support.append((lam, md))
    t1 = time.time()
    cand, pw, hits = [], 0, []
    for lam, md in det_support:
        mp = m_perpad(lam, delta, n, route)
        cand.append((lam, md, mp))
        if mp > md: pw += 1
        elif mp > 0: hits.append((lam, md, mp))
    print("=== n=%d m=%d delta=%d : lam |- %d, ell(lam) <= %d ; EXHAUSTIVE"
          % (n, m, delta, N, n * n))
    print("    partitions scanned                          : %d" % nlam)
    print("    with m_det >= 1 and ell <= %2d (screen candidates): %d   [%.0fs]"
          % (u, len(det_support), t1 - t0))
    print("    of those, m_perpad >  m_det (screen fails)   : %d" % pw)
    print("    of those, 0 < m_perpad <= m_det (SCREEN PASSES): %d   [%.0fs]"
          % (len(hits), time.time() - t1))
    if cand:
        mg = min(mp - md for _, md, mp in cand)
        print("    smallest margin m_perpad - m_det over candidates: %d" % mg)
        print("    lam                          m_det   m_perpad   P")
        for lam, md, mp in sorted(cand, key=lambda r: r[2] - r[1])[:12]:
            print("    %-27s %6d %9d %5d" % (str(lam), md, mp, mp - md))
    if hits:
        print("    *** CANDIDATE WEIGHTS:", hits)
    print()
    return hits

if __name__ == '__main__':
    for c in eval(sys.argv[1]):
        run(*c)
