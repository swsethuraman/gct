"""Session 23(a): the dimension computation in GF(p), for the larger m where
exact elimination over Q is too slow.  All arithmetic is exact integer
arithmetic in GF(p) (numpy int64, p = 2^31-1, so products stay below 2^63);
no floating point anywhere.  nullity_p >= nullity_Q, so a mod-p nullity of d
together with d independent witnesses over Q pins the dimension exactly."""
import random, sys
import numpy as np
from wk4_s23_words import monomials, necklaces, mm, mtr, neg, dmul, dtr, MZERO

P = (1 << 31) - 1
ID = ((1,0,0),(0,1,0),(0,0,1))

def rank_modp(M):
    """M: numpy int64 array, entries in [0,P).  Returns the rank over GF(P)."""
    M = M.copy() % P
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        pr = None
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0: continue
        pr = r + int(nz[0])
        if pr != r: M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), P-2, P)
        M[r] = (M[r] * inv) % P
        col = M[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            M[nzr] = (M[nzr] - np.outer(col[nzr], M[r])) % P
        r += 1
        if r == rows: break
    return r

def point_rows(m, A, B, mons, neck):
    """returns (value row, A-condition row, B-condition row) for one point."""
    A2, AB, BA, B2 = mm(A,A), mm(A,B), mm(B,A), mm(B,B)
    trA, trB = mtr(A), mtr(B)
    dA1, dB1 = neg(A2), neg(BA)      # derivation for the A-condition
    dA2, dB2 = neg(AB), neg(B2)      # derivation for the B-condition
    tv, t1, t2 = {}, {}, {}
    for w in neck:
        M0 = (ID, MZERO); M1 = (ID, MZERO)
        for c in w:
            M0 = dmul(M0, (A, dA1) if c == 0 else (B, dB1))
            M1 = dmul(M1, (A, dA2) if c == 0 else (B, dB2))
        a0, a1 = dtr(M0); b0, b1 = dtr(M1)
        tv[w] = a0 % P; t1[w] = a1 % P; t2[w] = b1 % P
    rE, rA, rB = [], [], []
    for mo in mons:
        v = 1; d1 = 0; d2 = 0
        for w in mo:                      # product rule via dual numbers
            d1 = (d1*tv[w] + v*t1[w]) % P
            d2 = (d2*tv[w] + v*t2[w]) % P
            v = (v*tv[w]) % P
        rE.append(v); rA.append((d1 + m*trA*v) % P); rB.append((d2 + m*trB*v) % P)
    return rE, rA, rB

def analyse_p(m, seed=17, extra=8):
    mons = monomials(m); neck = necklaces(m, m); n = len(mons)
    rng = random.Random(seed + 1000*m)
    def rmat(): return tuple(tuple(rng.randint(-5,5) for _ in range(3)) for _ in range(3))
    E, C = [], []
    while len(E) < n + extra:
        A, B = rmat(), rmat()
        rE, rA, rB = point_rows(m, A, B, mons, neck)
        E.append(rE); C.append(rA); C.append(rB)
    rankE = rank_modp(np.array(E, dtype=np.int64))
    rankC = rank_modp(np.array(C, dtype=np.int64))
    return n, rankE, n - rankE, n - rankC, (n - rankC) - (n - rankE)

if __name__ == '__main__':
    ms = [int(x) for x in sys.argv[1:]] or [2,3,4,5]
    print(" m  #mons  rank(E)=dim  relations  coef-nullity  DIM(equivariant)  predicted #{2a+3b+4c=m}")
    for m in ms:
        n, rE, rel, cn, df = analyse_p(m)
        pred = sum(1 for a in range(m//2+1) for b in range((m-2*a)//3+1)
                   if (m - 2*a - 3*b) % 4 == 0)
        print(f" {m}  {n:>5}  {rE:>11}  {rel:>9}  {cn:>12}   {df:>14}   {pred}",
              flush=True)
