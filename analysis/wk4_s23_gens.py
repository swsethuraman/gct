"""Session 23(a), step 3: the generators themselves, extracted correctly.

The constraint nullspace is a COEFFICIENT space and contains the relation space
(vectors representing the zero function).  A generator is any nullspace vector
whose function is nonzero; this file picks one, puts it in primitive integral
form, and tests it.
"""
import random
from fractions import Fraction
from math import gcd
from wk4_s23_words import monomials, mono_value, mm, mtr
from wk4_s23_equiv import analyse, rank_and_nullspace

def Psi(A, B):
    t = mtr
    AA, BB, AB = mm(A,A), mm(B,B), mm(A,B)
    u1 = t(AA)*t(BB) - t(AB)**2
    u2 = t(mm(AA,BB)) - t(mm(AB,AB))
    D  = (t(A)*t(B) - t(AB))**2 - (t(A)**2 - t(AA))*(t(B)**2 - t(BB))
    return 2*u1 - 4*u2 - D

rng = random.Random(5150)
def rmat(k=5): return tuple(tuple(rng.randint(-k,k) for _ in range(3)) for _ in range(3))
def fval(vec, mons, A, B):
    return sum(c*mono_value(mo, A, B) for c, mo in zip(vec, mons) if c)

def primitive(vec):
    L = 1
    for c in vec:
        if c: L = L*Fraction(c).denominator // gcd(L, Fraction(c).denominator)
    w = [int(Fraction(c)*L) for c in vec]
    g = 0
    for c in w: g = gcd(g, abs(c))
    return [c//g for c in w] if g else w

def show(mo):
    return "*".join("tr(" + "".join('AB'[c] for c in ww) + ")" for ww in mo)
def pretty(vec, mons):
    return " ".join(f"{'+' if c>0 else '-'}{abs(c)}*{show(mo)}"
                    for c, mo in zip(vec, mons) if c)

def extract(m):
    """returns (generators as primitive integral coefficient vectors, mons)."""
    r = analyse(m)
    mons, ns = r['mons'], r['ns']
    pts = [(rmat(), rmat()) for _ in range(60)]
    # value matrix of the nullspace vectors as FUNCTIONS
    F = [[fval(v, mons, A, B) for (A, B) in pts] for v in ns]
    # greedily pick vectors whose functions are independent
    chosen, basis = [], []
    for v, row in zip(ns, F):
        trial = basis + [row]
        rk, _ = rank_and_nullspace(trial, len(pts))
        if rk == len(trial):
            chosen.append(v); basis.append(row)
        if len(chosen) == r['dim_function']: break
    return r, [primitive(v) for v in chosen], mons

if __name__ == '__main__':
    print("=== m = 3: the generator, extracted as a nonzero function ===")
    r3, gens3, mons3 = extract(3)
    assert len(gens3) == 1 and r3['dim_function'] == 1
    g3v = gens3[0]
    nz = [(c, mo) for c, mo in zip(g3v, mons3) if c]
    print(f"  {len(nz)} trace monomials, coefficient set {sorted(set(abs(c) for c,_ in nz))}")
    print("  g3 =", pretty(g3v, mons3))
    print("  sample values:", [fval(g3v, mons3, rmat(), rmat()) for _ in range(4)])

    print()
    print("=== the banked pencils, and the compression family ===")
    E = lambda i,j: tuple(tuple(1 if (a,b)==(i,j) else 0 for b in range(3)) for a in range(3))
    def addm(*Ms):
        return tuple(tuple(sum(M[i][j] for M in Ms) for j in range(3)) for i in range(3))
    BANK = {'C': (E(2,1), E(1,2)), 'R': (E(0,0), E(1,1)),
            'T4': (addm(E(0,0),E(1,1)), addm(E(1,1),E(2,2))),
            'X4': (E(0,0), addm(E(1,2),E(2,1))),
            'Xm3': (addm(E(0,2),E(1,1)), addm(E(1,1),E(2,0))),
            'P': (E(0,0), E(0,0))}
    for k,(A,B) in BANK.items():
        print(f"   {k:4s} Psi = {Psi(A,B):>3}   g3 = {fval(g3v, mons3, A, B)}")
    def compression():
        A = [list(rmat()[i]) for i in range(3)]; B = [list(rmat()[i]) for i in range(3)]
        A[2] = [0,0,0]; B[2] = [0,0,0]
        return tuple(tuple(r) for r in A), tuple(tuple(r) for r in B)
    vals = [(Psi(*cb), fval(g3v, mons3, *cb)) for cb in (compression() for _ in range(6))]
    print(f"  (Psi, g3) at six compression nets: {vals}")

    print()
    print("=== m = 4: two independent generators, one of them Psi^2 ===")
    r4, gens4, mons4 = extract(4)
    print(f"  dim = {r4['dim_function']}; extracted {len(gens4)} independent functions")
    pts = [(rmat(), rmat()) for _ in range(30)]
    rows = [[fval(v, mons4, A, B) for (A,B) in pts] for v in gens4]
    tgt  = [Psi(A,B)**2 for (A,B) in pts]
    rk, _  = rank_and_nullspace([[Fraction(rows[j][i]) for j in range(len(rows))] for i in range(len(pts))], len(rows))
    rka, _ = rank_and_nullspace([[Fraction(rows[j][i]) for j in range(len(rows))] + [Fraction(tgt[i])] for i in range(len(pts))], len(rows)+1)
    print(f"  rank {rk}; with Psi^2 adjoined {rka}  =>  Psi^2 lies in the space: {rk==rka}")
    # a second element, independent of Psi^2: subtract the Psi^2 component
    for v in gens4:
        vals_v = [fval(v, mons4, A, B) for (A,B) in pts]
        M = [[Fraction(tgt[i]), Fraction(vals_v[i])] for i in range(len(pts))]
        rr, _ = rank_and_nullspace(M, 2)
        if rr == 2:
            print("  an element independent of Psi^2 exists (rank 2 against Psi^2): YES")
            comp = [(Psi(A,B), fval(v, mons4, A, B)) for (A,B) in
                    [compression() for _ in range(4)]]
            print(f"  that element at four compression nets (Psi, value): {comp}")
            break
