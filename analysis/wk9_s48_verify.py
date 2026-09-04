#!/usr/bin/env python3
"""
Session 48 -- independent verification of the two identities claimed PROVED in
docs/sixrow_cap_closed.md section 2, checked as polynomial identities (every
coefficient, not a sample point) at fresh pencils and both house primes.

  (I)   tr( adj(M) A_a adj(M) A_b )  =  (d_aF)(d_bF) - F d_a d_b F     [36 pairs]
  (II)  tr( adj(M) . ( M P_B(M) M - 3 F B ) )  =  0                    [B over a
        basis of M_4; P_B(M) = d/dt adj(M+tB)|_0]                       16 cases

usage: wk9_s48_verify.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import PRIMES, rand_pencil, pencil_entries, det_form, pderiv
from wk9_s48_syz import (mat_of_forms, adjugate, matmul_forms, const_mat,
                         pmul_p, padd_p, pscale)
from wk9_s48_syzfam import polar_adj

N, R = 4, 6
for p in PRIMES:
    for sd in (11111, 22222):
        rnd = random.Random(sd)
        A = rand_pencil(N, R, rnd, 10 ** 6)
        F = {e: v % p for e, v in det_form(pencil_entries(A, N, R), N).items() if v % p}
        M = mat_of_forms(A, p); Adj = adjugate(M, p)
        Ac = [const_mat(A[k], p) for k in range(R)]
        d = [{e: v % p for e, v in pderiv(F, k).items() if v % p} for k in range(R)]
        dd = [[{e: v % p for e, v in pderiv(d[a], b).items() if v % p}
               for b in range(R)] for a in range(R)]

        def tr(X):
            t = {}
            for i in range(N):
                for j in range(N):
                    if X[i][j] and Adj[j][i]:
                        t = padd_p(t, pmul_p(Adj[j][i], X[i][j], p), p)
            return t

        bad1 = 0
        for a in range(R):
            for b in range(R):
                lhs = tr(matmul_forms(matmul_forms(Ac[a], Adj, p), Ac[b], p))
                rhs = padd_p(pmul_p(d[a], d[b], p),
                             pscale(pmul_p(F, dd[a][b], p), p - 1, p), p)
                if padd_p(lhs, pscale(rhs, p - 1, p), p):
                    bad1 += 1
        bad2 = 0
        for i0 in range(N):
            for j0 in range(N):
                B = [[dict() for _ in range(N)] for _ in range(N)]
                B[i0][j0] = {(0,) * R: 1}
                V = matmul_forms(matmul_forms(M, polar_adj(M, B, p), p), M, p)
                FB = [[pmul_p(F, B[i][j], p) for j in range(N)] for i in range(N)]
                W = [[padd_p(V[i][j], pscale(FB[i][j], (p - 3) % p, p), p)
                      for j in range(N)] for i in range(N)]
                if tr(W):
                    bad2 += 1
        print(f"p={p} seed={sd}:  identity (I) failures {bad1}/36,  "
              f"identity (II) failures {bad2}/16", flush=True)
