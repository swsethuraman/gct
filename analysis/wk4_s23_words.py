"""Session 23(a): trace-monomial machinery for bidegree-(m,m) invariants of a
pencil (A,B) of 3x3 matrices, with exact integer / dual-number evaluation.

A WORD is a tuple over {0,1} (0 = A, 1 = B), taken up to cyclic rotation
(canonical form = lexicographically least rotation).  A MONOMIAL is a multiset
of words; its value is the product of the traces.  By the first fundamental
theorem for matrix invariants, these span the invariants of each bidegree, so
no degree bound is assumed anywhere.
"""
from itertools import product as iproduct
from functools import lru_cache

# ---------- 3x3 matrix arithmetic over any commutative ring of Python objects
def mm(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3))
                 for i in range(3))
def madd(X, Y): return tuple(tuple(X[i][j]+Y[i][j] for j in range(3)) for i in range(3))
def mscal(c, X): return tuple(tuple(c*X[i][j] for j in range(3)) for i in range(3))
def mtr(X): return X[0][0]+X[1][1]+X[2][2]
MZERO = ((0,0,0),(0,0,0),(0,0,0))

# ---------- dual numbers M0 + eps M1 (eps^2 = 0), 3x3 matrices ------------
def dmul(P, Q):
    return (mm(P[0], Q[0]), madd(mm(P[0], Q[1]), mm(P[1], Q[0])))
def dtr(P): return (mtr(P[0]), mtr(P[1]))

# ---------- necklaces ------------------------------------------------------
def canon(w):
    n = len(w)
    return min(tuple(w[i:]+w[:i]) for i in range(n))

def necklaces(maxa, maxb):
    out = set()
    for n in range(1, maxa+maxb+1):
        for w in iproduct((0,1), repeat=n):
            a = w.count(0); b = w.count(1)
            if a <= maxa and b <= maxb and (a or b):
                out.add(canon(w))
    return sorted(out, key=lambda w: (len(w), w))

def monomials(m):
    """all multisets of necklaces with total content (m,m), as sorted tuples."""
    neck = [w for w in necklaces(m, m)]
    cont = [(w.count(0), w.count(1)) for w in neck]
    res = []
    def rec(i, a, b, acc):
        if a == 0 and b == 0:
            res.append(tuple(acc)); return
        if i == len(neck): return
        ca, cb = cont[i]
        kmax = min(a // ca if ca else 10**9, b // cb if cb else 10**9)
        for k in range(kmax, -1, -1):
            rec(i+1, a - k*ca, b - k*cb, acc + [neck[i]]*k)
    rec(0, m, m, [])
    return res

# ---------- evaluation -----------------------------------------------------
def word_value(w, A, B, mulf, one):
    M = one
    for c in w:
        M = mulf(M, A if c == 0 else B)
    return M

def mono_value(mono, A, B):
    """plain integer value of a trace monomial at (A,B)."""
    v = 1
    for w in mono:
        M = ((1,0,0),(0,1,0),(0,0,1))
        for c in w:
            M = mm(M, A if c == 0 else B)
        v *= mtr(M)
    return v

def mono_value_dual(mono, A, B, dA, dB):
    """returns (value, D value) where D is the derivation A -> dA, B -> dB."""
    DA = (A, dA); DB = (B, dB)
    ID = (((1,0,0),(0,1,0),(0,0,1)), MZERO)
    tot = (1, 0)
    for w in mono:
        M = ID
        for c in w:
            M = dmul(M, DA if c == 0 else DB)
        t = dtr(M)
        tot = (tot[0]*t[0], tot[0]*t[1] + tot[1]*t[0])
    return tot

def neg(X): return mscal(-1, X)

if __name__ == '__main__':
    for m in (1,2,3,4,5):
        mons = monomials(m)
        print(f"m = {m}: {len(necklaces(m,m))} necklaces, {len(mons)} trace monomials")
