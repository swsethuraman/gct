#!/usr/bin/env python3
"""
Session 24 -- the existence question, inside an IRREDUCIBLE ambient.

W = Sym^8 C^2.  Pencil  f_t = x^8 + t x^4 y^4 + y^8.  For every t != 0 the
stabiliser is LITERALLY THE SAME subgroup

   K = { diag(al,be) : al,be in mu_8, al^4 = be^4 } |x S_2 ,   |K| = 64,

(the diagonal condition al^8=be^8=1 and (al be)^4 = 1 is exactly what fixing
the three monomials x^8, x^4y^4, y^8 demands, and it does not involve t).
So m is the SAME function for every member of the pencil and the Peter-Weyl
part P vanishes identically between any two of them.  t = +-2 is the member
f_2 = (x^4+y^4)^2, a perfect square: a different orbit closure.

Any weight where the closure multiplicities differ is therefore a
100% deficit-driven obstruction.
"""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_orbit import orbit_mult

def m_K(a, b):
    s = a - b
    assert (s + 2 * b) % 8 == 0
    idx = [i for i in range(s + 1) if (s - i + b) % 4 == 0]
    n = 0
    for i in idx:
        j = s - i
        if i < j: n += 1
        elif i == j: n += 1 if b % 2 == 0 else 0
    return n

TS = [1, 3, 5, 2, -2]
DMAX = 4
tab = {}
for t in TS:
    cf = [1, 0, 0, 0, t, 0, 0, 0, 1]
    for dl in range(1, DMAX + 1):
        tab[(t, dl)] = orbit_mult(cf, dl)
        print("t=%3d delta=%d : mult by b = %s" % (t, dl,
              [tab[(t, dl)].get(b, 0) for b in range(0, 4 * dl + 1)]))

print()
print("Peter-Weyl m_K by b:")
for dl in range(1, DMAX + 1):
    print("  delta=%d : %s" % (dl, [m_K(8 * dl - b, b) for b in range(0, 4 * dl + 1)]))
print()
print("generic members agree with each other?",
      all(tab[(1, d)] == tab[(3, d)] == tab[(5, d)] for d in range(1, DMAX + 1)))
print("t=2 agrees with t=-2?",
      all(tab[(2, d)] == tab[(-2, d)] for d in range(1, DMAX + 1)))
print()
print("DEFICIT-DRIVEN OBSTRUCTIONS between A = closure(f_1) and B = closure(f_2)")
print("(and the reverse), all with P = 0 identically:")
found = 0
for dl in range(1, DMAX + 1):
    for b in range(0, 4 * dl + 1):
        a = 8 * dl - b
        uA, uB = tab[(1, dl)].get(b, 0), tab[(2, dl)].get(b, 0)
        mm = m_K(a, b)
        if uA != uB:
            found += 1
            hi, lo = ('f_2', 'f_1') if uB > uA else ('f_1', 'f_2')
            print("  delta=%d lam=(%d,%d): m=%d  mult(f_1)=%d mult(f_2)=%d "
                  "| def(f_1)=%d def(f_2)=%d  -> obstruction to %s subset %s, P=0"
                  % (dl, a, b, mm, uA, uB, mm - uA, mm - uB, hi, lo))
print("total weights with a multiplicity difference:", found)
