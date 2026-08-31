#!/usr/bin/env python3
"""Session 25 -- QUESTION A: the retroactive audit of session 24's cells."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_worldA import table, aA, NAMES, SUB, DMAX

T = table()

# ---- reconstruct session 24's cell set exactly: ordered pairs (A,B) with
#      B NOT contained in A, all weights delta <= 14.
cells = []
for A in NAMES:
    for B in NAMES:
        if A == B or A in SUB[B]:      # A in SUB[B]  <=>  B subset A
            continue
        for d in range(1, DMAX + 1):
            for b in range(0, 2 * d + 1):
                mA, uA, fA = T[(A, d, b)]
                mB, uB, fB = T[(B, d, b)]
                cells.append((A, B, d, b, mA, uA, fA, mB, uB, fB,
                              mB - mA, fB - fA, uB - uA, aA(d, b)))

fav = [c for c in cells if c[10] <= 0 and c[11] < 0]      # P <= 0 and Def < 0
zeros = [c for c in fav if c[12] == 0]                     # D = 0
print("session-24 cell set reproduced: %d ordered-pair cells" % len(cells))
print("favourable cells (P <= 0 and Def < 0): %d      [session 24: 1292]" % len(fav))
print("of these, D = 0                      : %d      [session 24: 742]" % len(zeros))
from collections import Counter
print("distribution of D over the favourable cells:",
      dict(sorted(Counter(c[12] for c in fav).items(), reverse=True)))
print()

# ---- the classification.  Two mechanisms beyond a = 0 also force D = 0:
#  (i)  HYPERSURFACE BLINDNESS (session 24, Prop. 4): two orbit closures that
#       are hypersurfaces of the same degree and GL-weight have IDENTICAL
#       multiplicity functions, because 0 -> C[W]_{delta-e}(x)det^w -> C[W]_delta
#       -> C[X]_delta -> 0 is exact and the outer terms do not see F.  In World A
#       that is exactly the pair {Ac, D}: both are degree-6, weight det^12.
#  (ii) SATURATION AT THE CEILING: mult_A = mult_B = a.  Both closures carry the
#       whole ambient isotypic piece, i.e. neither has any degree-delta equation
#       in it, so D = 0 is again forced from above rather than coincidental.
BLIND = {('Ac', 'D'), ('D', 'Ac')}
forced  = [c for c in zeros if c[13] == 0]
blind   = [c for c in zeros if c[13] >= 1 and (c[0], c[1]) in BLIND]
rest    = [c for c in zeros if c[13] >= 1 and (c[0], c[1]) not in BLIND]
satur   = [c for c in rest if c[5] == c[13] and c[8] == c[13]]
empty   = [c for c in rest if c[5] == 0 and c[8] == 0]
subst   = [c for c in rest if c not in satur and c not in empty]
n = len(zeros)
print("CLASSIFICATION OF THE %d ZEROS" % n)
def row(lbl, L): print("  %-58s : %4d  (%.1f%%)" % (lbl, len(L), 100.0*len(L)/n))
row("forced   a = 0; both counts 0 by ambient arithmetic", forced)
row("blind    the {Ac,D} pair; mult functions identical (Prop. 4)", blind)
row("ceiling  a >= 1 and mult_A = mult_B = a (both saturate the cap)", satur)
row("empty    a >= 1 but mult_A = mult_B = 0 anyway", empty)
row("interior a >= 1 and 0 < mult_A = mult_B < a  -- GENUINE", subst)
print("  " + "-"*58)
row("FORCED by some structural mechanism (first four buckets)",
    forced + blind + satur + empty)
print()
print("  genuine (interior) cells, by (A,B) pair and common multiplicity:")
c2 = Counter((c[0], c[1], c[5]) for c in subst)
for k, v in sorted(c2.items(), key=lambda kv: -kv[1])[:14]:
    print("     A=%-4s B=%-4s  mult_A = mult_B = %d   x%d" % (k[0], k[1], k[2], v))
print()
print("  a-distribution over the genuine cells:",
      dict(sorted(Counter(c[13] for c in subst).items())))
print("  (mult, a) over the genuine cells:",
      dict(sorted(Counter((c[5], c[13]) for c in subst).items())[:12]))
print()

# ---- the whole favourable set, not just the zeros
f_forced = sum(1 for c in fav if c[13] == 0)
print("for context, over all %d favourable cells: a = 0 in %d (%.1f%%)"
      % (len(fav), f_forced, 100.0*f_forced/len(fav)))
print("and over all %d ordered-pair cells:        a = 0 in %d (%.1f%%)"
      % (len(cells), sum(1 for c in cells if c[13] == 0),
         100.0*sum(1 for c in cells if c[13] == 0)/len(cells)))

# ---- the strongest form: how much of the 742 involves only HYPERSURFACE
# closures?  For those, mult(lam) = a(lam,delta) - a(lam - w.1, delta - e)
# is determined by the AMBIENT plethysm and the (degree, weight) of the
# defining equation alone -- no boundary geometry enters at all.  So D = 0
# between two of them is a statement about plethysm coefficients, full stop.
HYP = {'Iz', 'Jz', 'Ac', 'D'}
hh   = [c for c in zeros if c[0] in HYP and c[1] in HYP]
mix  = [c for c in zeros if (c[0] in HYP) != (c[1] in HYP)]
nn   = [c for c in zeros if c[0] not in HYP and c[1] not in HYP]
print()
print("HYPERSURFACE DECOMPOSITION OF THE %d ZEROS" % n)
print("  both closures hypersurfaces (D = 0 is plethysm arithmetic) : %4d  (%.1f%%)"
      % (len(hh), 100.0*len(hh)/n))
print("  one hypersurface, one not                                  : %4d  (%.1f%%)"
      % (len(mix), 100.0*len(mix)/n))
print("  neither a hypersurface                                     : %4d  (%.1f%%)"
      % (len(nn), 100.0*len(nn)/n))
print("  genuine (interior) cells that involve a NON-hypersurface   : %4d"
      % sum(1 for c in subst if (c[0] not in HYP) or (c[1] not in HYP)))
print()
print("  the 22 genuine cells in full:")
for c in sorted(subst, key=lambda c: (c[0], c[1], c[2], c[3])):
    print("     A=%-4s B=%-4s delta=%2d lam=(%2d,%2d)  a=%d  mult_A=mult_B=%d  = a-1"
          % (c[0], c[1], c[2], 4*c[2]-c[3], c[3], c[13], c[5]))
