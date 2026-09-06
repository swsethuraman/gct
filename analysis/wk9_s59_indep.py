#!/usr/bin/env python3
"""
Session 59 -- independent cross-check of the two anchor dimensions. Builds the
Jacobians from sympy's symbolic ADJUGATE (d det M / d M_{ab} in the s_k direction
= s_k * adj(M)[b][a]) -- shares no code with the det_arc dual-number machinery --
and takes the rank mod a prime (unrelated to the house primes) with flint.
Confirms dim D_5 = 50 and the exact reducible locus (c21) = 31.
"""
import sys, random
import sympy as sp
from flint import nmod_mat

n, R = 4, 5
P = 2000000011                     # a prime unrelated to the house primes
s = sp.symbols('s0 s1 s2 s3 s4')

def coeffs_mod(poly, p):
    poly = sp.expand(poly)
    if poly == 0: return {}
    P_ = sp.Poly(poly, *s)
    return {tuple(m): int(c) % p for m, c in P_.terms()}

def rank_cols(cols, p):
    idx = {}
    for c in cols:
        for e in c: idx.setdefault(e, len(idx))
    nr, nc = len(idx), len(cols)
    if nr == 0: return 0
    flat = [0]*(nr*nc)
    for j, c in enumerate(cols):
        for e, v in c.items():
            flat[idx[e]*nc + j] = v % p
    return nmod_mat(nr, nc, flat, p).rank()

def sym_matrix(B):
    M = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            M[a, b] = sum(s[k]*B[k][a][b] for k in range(R))
    return M

def dim_D5(seed=1):
    rng = random.Random(seed)
    B = [[[rng.randint(-6, 6) for _ in range(n)] for _ in range(n)] for _ in range(R)]
    M = sym_matrix(B)
    adj = M.adjugate()                     # sympy adjugate (independent expansion)
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                der = s[k]*adj[b, a]        # d det / d M_{ab} in the s_k direction
                cols.append(coeffs_mod(der, P))
    return rank_cols(cols, P)

def c21_basis():
    G = []
    for a in range(n):
        for b in range(n):
            if b in (0, 1) and a in (1, 2, 3): continue
            E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    return G

def exact_dim_c21(seed=3):
    rng = random.Random(seed)
    Eb = c21_basis(); m = len(Eb)
    def A_of(coords):
        A = sp.zeros(n, n)
        for j, Ej in enumerate(Eb):
            for a in range(n):
                for b in range(n):
                    if Ej[a][b]: A[a, b] += coords[j]*Ej[a][b]
        return A
    u = [[rng.randint(-6, 6) for _ in range(m)] for _ in range(4)]
    A5 = sp.Matrix(n, n, lambda a, b: rng.randint(-6, 6))
    Ai = [A_of(u[i]) for i in range(4)]
    M = sp.zeros(n, n)
    for i in range(4): M += s[i]*Ai[i]
    M += s[4]*A5
    adj = M.adjugate()
    cols = []
    # A_i coords : direction s_i * E_j  ->  der = sum_{a,b} E_j[a][b] * s_i * adj[b][a]
    for i in range(4):
        for j in range(m):
            der = 0
            for a in range(n):
                for b in range(n):
                    if Eb[j][a][b]:
                        der += Eb[j][a][b]*s[i]*adj[b, a]
            q, r = sp.div(sp.Poly(sp.expand(der), *s), sp.Poly(s[4], *s))
            assert r == 0
            cols.append(coeffs_mod(q.as_expr(), P))
    # A_5 entries : direction s_4 * E_{ab}  ->  der = s_4 * adj[b][a]
    for a in range(n):
        for b in range(n):
            der = s[4]*adj[b, a]
            q, r = sp.div(sp.Poly(sp.expand(der), *s), sp.Poly(s[4], *s))
            assert r == 0
            cols.append(coeffs_mod(q.as_expr(), P))
    return rank_cols(cols, P)

if __name__ == '__main__':
    d5 = dim_D5()
    print(f"[sympy adjugate, mod {P}] dim D_5 = {d5}   (det_arc: 50)")
    ex = exact_dim_c21()
    print(f"[sympy adjugate, mod {P}] exact reducible locus (c21) = {ex}   (det_arc: 31; Q-certified)")
