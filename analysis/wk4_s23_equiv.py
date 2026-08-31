"""Session 23(a), step 2: the dimension of the slab-equivariant subspace of the
bidegree-(m,m) simultaneous-conjugation invariants, with character det^m.

Conditions (derived in session 22 from the slot dictionary, not imported):
    D_A f + m tr(A) f = 0     with  dA = -A^2 , dB = -BA
    D_B f + m tr(B) f = 0     with  dA = -AB , dB = -B^2
Exact arithmetic: Fraction Gaussian elimination over Q throughout.
"""
import random
from fractions import Fraction
from wk4_s23_words import (monomials, mono_value, mono_value_dual, mm, mtr, neg, mscal)

def rank_and_nullspace(rows, ncols):
    """rows: list of lists of Fractions/ints. Returns (rank, nullspace basis)."""
    M = [[Fraction(x) for x in r] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        sel = None
        for i in range(r, len(M)):
            if M[i][c] != 0: sel = i; break
        if sel is None: continue
        M[r], M[sel] = M[sel], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    free = [c for c in range(ncols) if c not in piv]
    ns = []
    for fc in free:
        v = [Fraction(0)]*ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        ns.append(v)
    return r, ns

def analyse(m, npts=None, seed=11):
    mons = monomials(m)
    n = len(mons)
    if npts is None: npts = n + 12
    rng = random.Random(seed + 1000*m)
    def rmat(): return tuple(tuple(rng.randint(-5, 5) for _ in range(3)) for _ in range(3))
    E, CA, CB = [], [], []
    for _ in range(npts):
        A, B = rmat(), rmat()
        A2 = mm(A, A); AB = mm(A, B); BA = mm(B, A); B2 = mm(B, B)
        trA, trB = mtr(A), mtr(B)
        rowE, rowA, rowB = [], [], []
        for mo in mons:
            v, dv = mono_value_dual(mo, A, B, neg(A2), neg(BA))
            rowE.append(v); rowA.append(dv + m*trA*v)
            _, dv2 = mono_value_dual(mo, A, B, neg(AB), neg(B2))
            rowB.append(dv2 + m*trB*v)
        E.append(rowE); CA.append(rowA); CB.append(rowB)
    rE, nsE = rank_and_nullspace(E, n)
    rC, nsC = rank_and_nullspace(CA + CB, n)
    relations = n - rE
    dim_fn = len(nsC) - relations
    return dict(m=m, nmons=n, rankE=rE, relations=relations,
                coef_nullity=len(nsC), dim_function=dim_fn, ns=nsC, mons=mons)

if __name__ == '__main__':
    import sys
    ms = [int(x) for x in sys.argv[1:]] or [2, 3]
    print(" m  #mons  rank(E)=dim  relations  coef-nullity  DIM(equivariant, function space)")
    for m in ms:
        r = analyse(m)
        print(f" {r['m']}  {r['nmons']:>5}  {r['rankE']:>11}  {r['relations']:>9}"
              f"  {r['coef_nullity']:>12}   {r['dim_function']}")
