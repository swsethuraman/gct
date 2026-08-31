#!/usr/bin/env python3
"""Session 25 -- QUESTION A, part 2: how much of the paper's det_3 deficit is
ambient-forced, and an audit of the BIP claim in docs/easy_counts.md."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import parts, m_det, amb_row, a_of

print("PAPER AUDIT -- det_3, Sym^delta(Sym^3 C^9)")
print("At delta <= 4 every ambient multiplicity is 0 or 1, and the paper's own")
print("published totals (1, 6, 31) equal sum m_det - sum a, i.e. mult = a on the")
print("whole ambient support: the degree-<=4 part of the ideal is zero.")
print()
print(" delta | sum m_det | sum a | total def | forced (a=0) | unforced | % forced")
for delta in (2, 3, 4):
    A = amb_row(delta, 3, 9)
    tot_m = tot_a = forced = unforced = 0
    for lam in parts(3 * delta):
        if len(lam) > 9: continue
        md = m_det(lam, 3, delta); a = A.get(lam, 0)
        tot_m += md; tot_a += a
        if a == 0: forced += md
        else:      unforced += md - a
    print("   %2d  |  %6d   | %4d  |   %5d   |    %5d     |  %5d   |  %5.1f%%"
          % (delta, tot_m, tot_a, tot_m - tot_a, forced, unforced,
             100.0 * forced / (tot_m - tot_a)))
print()
print("the delta=2 row, weight by weight:")
for lam in parts(6):
    if len(lam) > 9: continue
    md, a = m_det(lam, 3, 2), a_of(lam, 2, 3, 9)
    if md or a:
        print("   lam=%-10s m_det=%d  a=%d  mult=%d  def=%d  %s"
              % (str(lam), md, a, a, md - a,
                 "FORCED (a=0: mult=0 for every closure in the ambient)" if a == 0 else ""))
print()
print("=> def_det((2,2,2),2) = 1, the base point of the conductor result, is")
print("   ambient arithmetic: a((2,2,2),2) = 0, so mult = 0 for EVERY orbit")
print("   closure in Sym^3 C^9 and def = m there by definition.")
print()

print("EASY-COUNTS AUDIT -- the BIP claim at (n,delta) = (5,2)")
print("docs/easy_counts.md: 'the 34 live weights with m_det = 0 < m_per are")
print("exactly the weights where BIP forces def_per = m_per'.")
A52 = amb_row(2, 5, 25)
print("  ambient Sym^2(Sym^5 C^25) constituents:", sorted(A52.items()))
n0 = sum(1 for lam in parts(10) if len(lam) <= 25 and m_det(lam, 5, 2) == 0
         and A52.get(lam, 0) == 0)
nA = sum(1 for lam in parts(10) if len(lam) <= 25 and m_det(lam, 5, 2) == 0
         and A52.get(lam, 0) >= 1)
print("  weights with m_det = 0 and a = 0 : %d" % n0)
print("  weights with m_det = 0 and a >= 1: %d" % nA)
print("  m_det on the ambient support:", {lam: m_det(lam, 5, 2) for lam in A52})
