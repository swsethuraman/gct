#!/usr/bin/env python3
"""
Session 25 -- QUESTION C (cheap part): where does the PADDED problem first
become live?  A multiplicity obstruction needs a >= 2; the padded permanent's
Peter-Weyl count vanishes unless ell(lam) <= m^2+1 (session 24b's row bound).
So the padded live locus is  {lam : a(lam,delta) >= 2 and ell(lam) <= m^2+1}.
This needs only the ambient plethysm -- no permanent computation at all.
"""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import amb_row, m_det

for (n, m) in ((4, 3), (5, 3), (5, 4), (6, 3)):
    u = m * m + 1
    print("n=%d, m=%d  (row bound ell <= %d)" % (n, m, u))
    for delta in range(2, 7 if n == 4 else 5):
        A = amb_row(delta, n, n * n)
        ge2 = [(l, v) for l, v in A.items() if v >= 2]
        live = [(l, v) for l, v in ge2 if len(l) <= u]
        print("   delta=%d : ambient support %4d ; a>=2 : %4d ; of those ell<=%d : %d %s"
              % (delta, len(A), len(ge2), u, len(live),
                 ("  -> " + str([(l, v, m_det(l, n, delta)) for l, v in live][:4])
                  + " (lam, a, m_det)") if live else ""))
        sys.stdout.flush()
    print()
