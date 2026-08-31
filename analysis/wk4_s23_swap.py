"""Session 23(b): the self-transpose (swap-symmetric) family, and what the
transpose-vanishing law does to the equivariant space at odd q.

A net in slab normal form is fixed by the slot-1<->3 swap iff (S_k)_{ji} =
(S_j)_{ki}; with S_0 = I this forces row 0 of A = e_1, row 0 of B = e_2 and
row 2 of A = row 1 of B, leaving nine free parameters.  For such a net the
transposed slab-zero is the identity, so det G = 1 and chi = det(t)^q = (-1)^q.
"""
import random
from fractions import Fraction
from wk4_s23_words import mm, mtr
from wk4_s23_gens import extract, fval, Psi, rank_and_nullspace

def swap_pair(vals):
    p, r, s, u, v, w, y, z, c = vals
    A = ((0,1,0), (p,r,s), (u,v,w))
    B = ((0,0,1), (u,v,w), (y,z,c))
    return A, B

def is_swap_symmetric(A, B):
    S = [((1,0,0),(0,1,0),(0,0,1)), A, B]
    return all(S[k][j][i] == S[j][k][i] for i in range(3) for j in range(3) for k in range(3))

if __name__ == '__main__':
    rng = random.Random(2718)
    pts = [swap_pair([rng.randint(-5,5) for _ in range(9)]) for _ in range(60)]
    print("=== the family is swap-symmetric, and Psi does not vanish on it ===")
    print("  all swap-symmetric:", all(is_swap_symmetric(A,B) for A,B in pts))
    print("  Psi at six members:", [Psi(A,B) for A,B in pts[:6]])

    for m in (2, 3, 4):
        r, gens, mons = extract(m)
        vals = [[fval(g, mons, A, B) for (A,B) in pts] for g in gens]
        rk, ns = rank_and_nullspace(
            [[Fraction(vals[j][i]) for j in range(len(gens))] for i in range(len(pts))],
            len(gens))
        print(f"\n=== m = {m}: dim E_m = {r['dim_function']}, "
              f"rank of E_m restricted to the swap family = {rk}")
        if rk == len(gens):
            print(f"  => NO nonzero element of E_m vanishes on the self-transpose family.")
            print(f"     At any weight (p,p,p,q^6) with p-q = {m} and q ODD, the transpose")
            print(f"     forces TOTAL = 0 there, hence TOTAL == 0 IDENTICALLY on the")
            print(f"     whole balanced cone.")
        else:
            print(f"  => a {len(gens)-rk}-dimensional subspace of E_m vanishes on the family;")
            print(f"     at odd q, TOTAL is confined to it (not forced to zero).")
