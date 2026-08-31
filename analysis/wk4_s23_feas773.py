"""Session 23(b): is the odd-q test weight non-vacuous?  Weight-feasibility of
balanced {0,1} directions at lambda' = (7,7,7,3^6), delta = 13, t = (4,4)."""
import sys
from wk4_s23_g3locus import mons_of_pencil, feasible, mat_of
from wk4_s23_gens import Psi

DEMAND = (7,7,7,3,3,3,3,3,3); NC = 13
BANKBITS = {  # A, B as 9-bit row-major masks, from the banked transvection points
 'C':   (0b000000010, 0b000001000),   # placeholder, recomputed below
}
def bits_of(M):
    return sum((1 << (3*i+j)) for i in range(3) for j in range(3) if M[i][j])

if __name__ == '__main__':
    E = lambda i,j: tuple(tuple(1 if (a,b)==(i,j) else 0 for b in range(3)) for a in range(3))
    def addm(*Ms): return tuple(tuple(sum(M[i][j] for M in Ms) for j in range(3)) for i in range(3))
    BANK = {'C': (E(2,1), E(1,2)), 'R': (E(0,0), E(1,1)),
            'T4': (addm(E(0,0),E(1,1)), addm(E(1,1),E(2,2))),
            'X4': (E(0,0), addm(E(1,2),E(2,1))),
            'Xm3': (addm(E(0,2),E(1,1)), addm(E(1,1),E(2,0)))}
    print("banked points at the new weight:")
    for k,(A,B) in BANK.items():
        f = feasible(list(mons_of_pencil(A,B)), DEMAND, NC)
        print(f"   {k:4s} feasible: {f}")
    print()
    print("sweep of the {0,1} balanced cone (512 x 512):")
    nfeas = 0; first = []
    swap_feas = []
    for ab in range(512):
        A = mat_of(ab)
        for bb in range(512):
            B = mat_of(bb)
            if not feasible(list(mons_of_pencil(A,B)), DEMAND, NC): continue
            nfeas += 1
            if len(first) < 6: first.append((ab, bb, Psi(A,B)))
            # is it swap-symmetric?
            S = [((1,0,0),(0,1,0),(0,0,1)), A, B]
            if all(S[k][j][i] == S[j][k][i] for i in range(3) for j in range(3) for k in range(3)):
                swap_feas.append((ab, bb, Psi(A,B)))
        if ab % 128 == 0: print(f"   ... A-block {ab}/512, feasible {nfeas}", flush=True)
    print(f"feasible balanced {{0,1}} directions at (7,7,7,3^6): {nfeas}")
    for ab, bb, p in first:
        print(f"   A = {mat_of(ab)}  B = {mat_of(bb)}   Psi = {p}")
    print(f"feasible AND swap-symmetric: {len(swap_feas)}")
    for ab, bb, p in swap_feas[:6]:
        print(f"   A = {mat_of(ab)}  B = {mat_of(bb)}   Psi = {p}")
