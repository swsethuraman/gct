"""Session 23: the ring structure, checked directly.
If restriction is an isomorphism onto the equivariant functions, then E_m is
spanned by the products of the generators g2 = Psi, g3, g4' (the element of E_4
independent of Psi^2).  This file verifies that for m = 5, 6 -- where the direct
nullspace computation over Q is expensive -- and computes the rank of each E_m
on the self-transpose (swap-symmetric) family, which is what the odd-q
transpose law turns on."""
import random
from fractions import Fraction
from wk4_s23_gens import extract, fval, Psi, rank_and_nullspace
from wk4_s23_swap import swap_pair

rng = random.Random(31415)
def rmat(k=5): return tuple(tuple(rng.randint(-k,k) for _ in range(3)) for _ in range(3))

def rk(funcs, pts):
    rows = [[Fraction(f(A,B)) for f in funcs] for (A,B) in pts]
    r, _ = rank_and_nullspace(rows, len(funcs))
    return r

if __name__ == '__main__':
    r3, g3s, mons3 = extract(3)
    r4, g4s, mons4 = extract(4)
    g3 = lambda A,B: fval(g3s[0], mons3, A, B)
    # pick the element of E_4 independent of Psi^2
    pts0 = [(rmat(), rmat()) for _ in range(20)]
    cand = [ (lambda A,B,v=v: fval(v, mons4, A, B)) for v in g4s ]
    f4 = None
    for c in cand:
        if rk([lambda A,B: Psi(A,B)**2, c], pts0) == 2: f4 = c; break
    assert f4 is not None
    print("generators in hand: g2 = Psi (dim E_2 = 1), g3 (dim E_3 = 1), "
          "and f4 independent of Psi^2 (dim E_4 = 2)")

    gen = [(rmat(), rmat()) for _ in range(60)]
    swp = [swap_pair([rng.randint(-5,5) for _ in range(9)]) for _ in range(60)]

    print()
    print("=== products span E_m, and their rank on the self-transpose family ===")
    tests = {
      2: [lambda A,B: Psi(A,B)],
      3: [g3],
      4: [lambda A,B: Psi(A,B)**2, f4],
      5: [lambda A,B: Psi(A,B)*g3(A,B)],
      6: [lambda A,B: Psi(A,B)**3, lambda A,B: Psi(A,B)*f4(A,B), lambda A,B: g3(A,B)**2],
      7: [lambda A,B: Psi(A,B)**2*g3(A,B), lambda A,B: f4(A,B)*g3(A,B)],
    }
    predicted_dim = {m: sum(1 for a in range(m//2+1) for b in range((m-2*a)//3+1)
                            if (m-2*a-3*b) % 4 == 0) for m in tests}
    print(" m  #products  rank(generic)  predicted dim E_m  rank on swap family  "
          "kernel there")
    for m, fs in tests.items():
        rg = rk(fs, gen); rs = rk(fs, swp)
        print(f" {m}  {len(fs):>9}  {rg:>13}  {predicted_dim[m]:>17}  {rs:>19}  {rg-rs}")
    print()
    print("g3 on the swap family:", [g3(A,B) for A,B in swp[:5]])
    print("Psi on the swap family:", [Psi(A,B) for A,B in swp[:5]])
