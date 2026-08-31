"""Session 23(a), corollary: which balanced {0,1} directions have g3 != 0?
At lambda' = (9,9,9,6^6) (delta = 21, the delta = 3 row of the conductor table)
the uniqueness step survives with dim E_3 = 1, so TOTAL = c*g3 there.  g3
vanishes at every banked point, so a certificate at that weight needs a
direction off the g3-locus.  This finds candidates and tests weight-feasibility
only on those (feasibility is the expensive step)."""
import sys
from itertools import product
from wk4_s23_gens import extract, fval, Psi
from wk4_s23_g3locus import mons_of_pencil, feasible, mat_of

DEMAND = (9,9,9,6,6,6,6,6,6); NC = 21

if __name__ == '__main__':
    r3, gens3, mons3 = extract(3)
    g3v = gens3[0]
    g3 = lambda A, B: fval(g3v, mons3, A, B)
    nz = []
    for ab in range(512):
        A = mat_of(ab)
        for bb in range(512):
            B = mat_of(bb)
            g = g3(A, B)
            if g: nz.append((abs(g), g, ab, bb))
    nz.sort(key=lambda t: (t[0], bin(t[2]).count('1') + bin(t[3]).count('1')))
    print(f"{{0,1}} pencils with g3 != 0: {len(nz)} of 262144", flush=True)
    print("smallest |g3|, fewest transvections first; testing feasibility at "
          "(9,9,9,6^6), delta = 21:")
    shown = 0
    for _, g, ab, bb in nz:
        A, B = mat_of(ab), mat_of(bb)
        nt = bin(ab).count('1') + bin(bb).count('1')
        if nt > 4: continue
        f = feasible(list(mons_of_pencil(A, B)), DEMAND, NC)
        print(f"   g3 = {g:>4}  Psi = {Psi(A,B):>3}  transvections = {nt}  "
              f"feasible = {f}   A = {A}  B = {B}", flush=True)
        shown += 1
        if shown >= 12: break
