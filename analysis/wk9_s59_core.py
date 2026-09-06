#!/usr/bin/env python3
"""
Session 59 -- core arc/jet machinery for the higher-order (q >= 2) Rees
exceptional image of det_4 at r = 5.

Objects (all over F_p via python-flint nmod_mat for ranks; dual numbers eps^2=0
for exact Jacobians -- no hand-rolled elimination, no adjugate identity beyond
what Leibniz gives):

  X_5   = Hom(C^5, M_4),  M(s) = sum_k s_k B_k,  B_k in M_4.        dim 80
  Phi   : M |-> det M(s) in Sym^4 C^5.                              (70 coeffs)
  D_5   = closure Phi(X_5),  dim 50.
  B_5   = base locus {M : det M(s) == 0} = bounded-rank-<=3 pencils.
  W     = {s_5 . c} = quartics divisible by s_5.                    dim 35
  pi    : f |-> f|_{s_5=0}  (the 35 s_5-degree-0 monomials).
          pi(Phi(M)) = det(M'(s')), M' = s_1..s_4 slices  ==> D_5 cap W
          is the fibre of pi|_{D_5} over 0.

An arc M(t,s) = M_0 + t M_1 + ... + t^q M_q (each M_j a 5-var pencil) with
det M_0(s) == 0 has det M(t,s) = sum_k t^k g_k(s); the leading quartic g_q
(first g_q != 0) is a point of D_5 (exceptional image of Bl_J(P X_5)).

This module builds det M(t,s) exactly as a t-series of quartics-in-s, in dual
numbers, so a single call yields both a value and a directional derivative.
"""
import sys, itertools
from flint import nmod_mat

# ----------------------------------------------------------------------
# monomial bookkeeping
R, n = 5, 4

def _mk_qexp():
    out = []
    def rec(k, left, cur):
        if k == R - 1:
            out.append(tuple(cur + [left])); return
        for v in range(left + 1):
            rec(k + 1, left - v, cur + [v])
    rec(0, 4, [])
    return out

QEXP = _mk_qexp()                     # 70 quartic exponent tuples (deg 4 in 5 vars)
QIDX = {e: i for i, e in enumerate(QEXP)}
NQ = len(QEXP)                        # 70
S5DEG0 = [i for i, e in enumerate(QEXP) if e[4] == 0]   # 35 : monomials with no s_5
S5POS  = [i for i, e in enumerate(QEXP) if e[4] >= 1]   # 35 : W = span of these

assert NQ == 70 and len(S5DEG0) == 35 and len(S5POS) == 35

# cubic monomials in 5 vars (for tracking c = f / s_5)
def _mk_cexp():
    out = []
    def rec(k, left, cur):
        if k == R - 1:
            out.append(tuple(cur + [left])); return
        for v in range(left + 1):
            rec(k + 1, left - v, cur + [v])
    rec(0, 3, [])
    return out
CEXP = _mk_cexp()                     # 35 cubic exponent tuples
CIDX = {e: i for i, e in enumerate(CEXP)}
NC = len(CEXP)                        # 35
assert NC == 35

# map: index in QEXP of a quartic divisible by s_5 -> index in CEXP of quotient
Q2C = {}
for i, e in enumerate(QEXP):
    if e[4] >= 1:
        ce = (e[0], e[1], e[2], e[3], e[4] - 1)
        Q2C[i] = CIDX[ce]

# ----------------------------------------------------------------------
# dual-number arithmetic mod p : a value is a pair (a, b) meaning a + b*eps
def dadd(x, y, p): return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)
def dsub(x, y, p): return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)
def dmul(x, y, p): return ((x[0]*y[0]) % p, (x[0]*y[1] + x[1]*y[0]) % p)

# a "linear form" is a dict {var_index(0..4): (a,b)} ; a t-series entry is a
# dict {tpow(int): linear-form-dict}.

def lf_from_int(vec, p, dvec=None):
    """linear form from integer coeff list (len 5); optional dual part dvec."""
    d = {}
    for k in range(R):
        a = vec[k] % p
        b = (dvec[k] % p) if dvec is not None else 0
        if a or b:
            d[k] = (a, b)
    return d

def lf_mul(f, g, p):
    """product of two linear forms -> quadratic, as {exp2-tuple: (a,b)}; but we
    keep the running product as {exp-tuple: (a,b)} of the accumulated degree."""
    out = {}
    for k1, c1 in f.items():
        for k2, c2 in g.items():
            e = [0]*R; e[k1] += 1; e[k2] += 1; e = tuple(e)
            out[e] = dadd(out.get(e, (0, 0)), dmul(c1, c2, p), p)
    return out

def poly_mul_lf(poly, g, p):
    """multiply a degree-d s-polynomial {exp: (a,b)} by a linear form g."""
    out = {}
    for e1, c1 in poly.items():
        for k2, c2 in g.items():
            e = list(e1); e[k2] += 1; e = tuple(e)
            out[e] = dadd(out.get(e, (0, 0)), dmul(c1, c2, p), p)
    return out

def series_mul(A, B, p, tcap):
    """multiply two t-series; A,B are {tpow: s-poly}, s-poly = {exp:(a,b)}.
    keep tpow <= tcap."""
    out = {}
    for t1, p1 in A.items():
        for t2, p2 in B.items():
            t = t1 + t2
            if t > tcap: continue
            # multiply s-polys p1, p2
            acc = out.setdefault(t, {})
            for e1, c1 in p1.items():
                for e2, c2 in p2.items():
                    e = tuple(e1[i] + e2[i] for i in range(R))
                    acc[e] = dadd(acc.get(e, (0, 0)), dmul(c1, c2, p), p)
    return out

def det_arc(entry, p, tcap):
    """entry[a][b] = t-series {tpow: linear-form-dict}. Returns det as
    {tpow: quartic-s-poly {exp: (a,b)}}, tpow <= tcap."""
    out = {}
    for perm in itertools.permutations(range(n)):
        sgn = 1
        pl = list(perm)
        for i in range(n):
            for j in range(i+1, n):
                if pl[i] > pl[j]: sgn = -sgn
        # product of entry[a][perm[a]] as t-series of s-polys
        prod = {0: {(0,)*R: ((sgn) % p, 0)}}
        for a in range(n):
            # convert linear form {var:(a,b)} to s-poly {exp-tuple:(a,b)}
            fac = {}
            for tp, lf in entry[a][perm[a]].items():
                sp = {}
                for kvar, c in lf.items():
                    e = [0]*R; e[kvar] = 1
                    sp[tuple(e)] = c
                fac[tp] = sp
            prod = series_mul(prod, fac, p, tcap)
        for tp, sp in prod.items():
            acc = out.setdefault(tp, {})
            for e, c in sp.items():
                acc[e] = dadd(acc.get(e, (0, 0)), c, p)
    # drop zero coeffs
    cleaned = {}
    for tp, sp in out.items():
        s = {e: c for e, c in sp.items() if c[0] % p or c[1] % p}
        if s: cleaned[tp] = s
    return cleaned

def quartic_vec(sp, p, part=0):
    """quartic s-poly {exp:(a,b)} -> length-70 list of the 'part' (0=val,1=dual)."""
    v = [0]*NQ
    for e, c in sp.items():
        v[QIDX[e]] = c[part] % p
    return v

# ----------------------------------------------------------------------
# building pencils as t-series entries from integer coefficient arrays.
# A jet list Ms = [M0, M1, ...], each M_j a list of R matrices (B_{j,k})[a][b] int.
# optional duals: same shape.
def pencils_to_entry(Ms, p, duals=None):
    """entry[a][b] = { tpow=j : linear form sum_k s_k * M_j[k][a][b] }."""
    entry = [[None]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            ser = {}
            for j, Mj in enumerate(Ms):
                vec = [Mj[k][a][b] for k in range(R)]
                dvec = None
                if duals is not None and duals[j] is not None:
                    dvec = [duals[j][k][a][b] for k in range(R)]
                lf = lf_from_int(vec, p, dvec)
                if lf: ser[j] = lf
            entry[a][b] = ser
    return entry

def rank_mod(rows, ncols, p):
    """rank of a list of length-ncols int rows over F_p."""
    if not rows: return 0
    m = len(rows)
    flat = [int(rows[i][j]) for i in range(m) for j in range(ncols)]
    return nmod_mat(m, ncols, flat, p).rank()

# ----------------------------------------------------------------------
# stratum bases : a stratum is given by a basis of the space E of 4x4 matrices
# (bounded-rank-<=3) that the pencil M_0 maps C^5 into. M_0(s) = sum_k s_k B_k
# with each B_k in E.  We follow s54/s32 conventions.
def stratum_E_basis(name, rng, p):
    """return a list of 4x4 integer matrices spanning E (the image space)."""
    G = []
    if name == 'ker':          # common kernel e_0 : column 0 == 0
        for a in range(n):
            for b in range(1, n):
                E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    elif name == 'coker':      # common cokernel : row 0 == 0
        for a in range(1, n):
            for b in range(n):
                E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    elif name == 'c21':        # (2,1) compression : rows 1,2,3 of cols 0,1 == 0
        for a in range(n):
            for b in range(n):
                if b in (0, 1) and a in (1, 2, 3): continue
                E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    elif name == 'c32':        # (3,2) compression : rows 2,3 of cols 0,1,2 == 0
        for a in range(n):
            for b in range(n):
                if b in (0, 1, 2) and a in (2, 3): continue
                E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    elif name == 'prim':       # primitive C^4 -> Hom(C^4, Lambda^2 C^4)
        phi = [[[0]*n for _ in range(n)] for _ in range(n)]
        for a in range(n):
            for b in range(n):
                for c in range(b+1, n):
                    v = rng.randint(1, p-1)
                    phi[a][b][c] = v; phi[a][c][b] = (-v) % p
        for c in range(n):
            G.append([[phi[a][b][c] for b in range(n)] for a in range(n)])
    else:
        raise ValueError(name)
    return G

STRATA = ['ker', 'coker', 'c21', 'c32', 'prim']

def random_pencil_in_E(Ebasis, rng, p, lo=1, hi=None):
    """M_0 = sum_k s_k B_k, B_k a random combination of the E-basis (so image in E)."""
    if hi is None: hi = p-1
    m = len(Ebasis)
    B = []
    for k in range(R):
        coeffs = [rng.randint(lo, hi) for _ in range(m)]
        M = [[0]*n for _ in range(n)]
        for j, Eb in enumerate(Ebasis):
            for a in range(n):
                for b in range(n):
                    if Eb[a][b]:
                        M[a][b] = (M[a][b] + coeffs[j]*Eb[a][b]) % p
        B.append(M)
    return B

def random_pencil(rng, p, lo=1, hi=None):
    """generic 5-var pencil (image all of M_4)."""
    if hi is None: hi = p-1
    return [[[rng.randint(lo, hi) for _ in range(n)] for _ in range(n)] for _ in range(R)]

if __name__ == '__main__':
    print("core loaded: NQ=%d dim W=%d |S5DEG0|=%d NC=%d strata=%s"
          % (NQ, len(S5POS), len(S5DEG0), NC, STRATA))
