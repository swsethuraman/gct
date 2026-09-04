#!/usr/bin/env python3
"""
Session 48, target A -- the six non-Koszul syzygies against the natural
GL_4 x GL_4-equivariant families.

Equivariance.  Under M |-> P M Q the pencil space transports as L |-> P L Q,
adj(M) |-> det(PQ) Q^{-1} adj(M) P^{-1}, and F |-> det(PQ) F.  So a matrix word
is equivariant (W |-> det(PQ)^a P W Q, which is what tr(adj(M) W) = 0 needs)
exactly when it ALTERNATES L-elements and adjugates, beginning and ending with
an L-element.  At s-degree 4 the complete list of such words is small, and this
script builds every one of them:

  fam1  l(s) * A_a adj(M) A_b                              216
  fam2  M P_B(M) M            [P_B(M) = d/dt adj(M+tB)]     16
  fam3  F * B                                                16
  fam4  phi_X(s) * M          [phi_X = tr(adj(M) X)]         16
  fam5  l(s) * A_a P_{A_b}(M) M   and  l(s) * M P_{A_a}(M) A_b   216 + 216
  fam6  l(s) * M ADJ(A_a, A_b, M) M                         216

Two of them are automatically in the Gulliksen-Negard kernel, by identities
proved here rather than assumed:

  (I)   tr(adj M . A_a adj M . A_b)  =  (d_aF)(d_bF) - F d_a d_b F   [symmetric
        in (a,b)], so every ANTIsymmetric combination of fam1 annihilates.
  (II)  tr(P_B(M) M) = 3 d_B F, and adj(M) M = F I, so
            V_B  :=  M P_B(M) M  -  3 F B
        has tr(adj(M) V_B) = 3F d_BF - 3F d_BF = 0 for EVERY B and every pencil.

For each family the script solves the two linear conditions
   (i) W in L (x) S_4     (ii) tr(adj(M) W) = 0
and reports how much of the answer is new modulo the 90 Koszul syzygies.

usage: wk9_s48_syzfam.py [seed] [npencils]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (PRIMES, monos, mono_index, dim_sym, pderiv,
                          rand_pencil, pencil_entries, det_form, ideal_rows,
                          rank_rows, submax_minors)
from wk9_s48_syz import (mat_of_forms, adjugate, matmul_forms, const_mat,
                         pmul_p, padd_p, pscale, complement_functionals,
                         koszul_matrix)
from flint import nmod_mat

N, R, D, E = 4, 6, 7, 4
BOX = 10 ** 6


def det3(X, rows, cols, p):
    tot = {}
    for perm, sg in (((0,1,2),1), ((1,2,0),1), ((2,0,1),1),
                     ((0,2,1),-1), ((2,1,0),-1), ((1,0,2),-1)):
        t = {(0,) * R: 1}
        for a in range(3):
            t = pmul_p(t, X[rows[a]][cols[perm[a]]], p)
        tot = padd_p(tot, pscale(t, sg % p, p), p)
    return tot


def d_det3(X, Y, rows, cols, p):
    """d/dt det3(X + tY) at t = 0: sum over replacing one row of X by that of Y."""
    tot = {}
    for k in range(3):
        Z = [list(r) for r in X]
        for c in range(N):
            Z[rows[k]][c] = Y[rows[k]][c]
        tot = padd_p(tot, det3(Z, rows, cols, p), p)
    return tot


def polar_adj(M, B, p):
    """P_B(M) = d/dt adj(M + tB) at t = 0."""
    P = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rows = [x for x in range(N) if x != j]
            cols = [x for x in range(N) if x != i]
            P[i][j] = pscale(d_det3(M, B, rows, cols, p), (-1) ** (i + j) % p, p)
    return P


def second_polar_adj(M, B, C, p):
    """ADJ(B, C, M)-ish: d^2/dtdu adj(M + tB + uC) at 0."""
    Mt = [[padd_p(M[i][j], pscale(C[i][j], 1, p), p) for j in range(N)] for i in range(N)]
    P1 = polar_adj(Mt, B, p)
    P0 = polar_adj(M, B, p)
    return [[padd_p(P1[i][j], pscale(P0[i][j], p - 1, p), p) for j in range(N)]
            for i in range(N)]


def flat(W, idx, p):
    """4x4 matrix of degree-4 forms -> vector of length 16*126."""
    v = [0] * (N * N * len(idx))
    for i in range(N):
        for j in range(N):
            base = (i * N + j) * len(idx)
            for e, c in W[i][j].items():
                if e in idx:
                    v[base + idx[e]] = c % p
    return v


def build_families(A, p):
    M = mat_of_forms(A, p)
    Adj = adjugate(M, p)
    Ac = [const_mat(A[k], p) for k in range(R)]
    idx4 = mono_index(E, R)
    lin = [{tuple(1 if t == c else 0 for t in range(R)): 1} for c in range(R)]
    Eb = [[None] * N for _ in range(N)]        # basis of M_4 as constant matrices
    basis16 = []
    for i in range(N):
        for j in range(N):
            Z = [[dict() for _ in range(N)] for _ in range(N)]
            Z[i][j] = {(0,) * R: 1}
            basis16.append(Z)
    F = det_form(pencil_entries(A, N, R), N)
    F = {e: v % p for e, v in F.items() if v % p}

    def times(Wf, sc):
        return [[pmul_p(Wf[i][j], sc, p) for j in range(N)] for i in range(N)]

    fams = {}
    # fam1
    v = []
    for a in range(R):
        for b in range(R):
            X = matmul_forms(matmul_forms(Ac[a], Adj, p), Ac[b], p)
            for c in range(R):
                v.append(flat(times(X, lin[c]), idx4, p))
    fams["fam1 l*A_a adj(M) A_b"] = v
    # fam2 / fam3 / fam4 (B over a full basis of M_4)
    v2, v3, v4 = [], [], []
    for B in basis16:
        P = polar_adj(M, B, p)
        v2.append(flat(matmul_forms(matmul_forms(M, P, p), M, p), idx4, p))
        v3.append(flat(times(B, F), idx4, p))
        phi = {}
        for i in range(N):
            for j in range(N):
                if B[i][j]:
                    phi = padd_p(phi, pmul_p(Adj[j][i], B[i][j], p), p)
        v4.append(flat(times(M, phi), idx4, p))
    fams["fam2 M P_B(M) M"] = v2
    fams["fam3 F*B"] = v3
    fams["fam4 phi_X * M"] = v4
    # fam5
    v5 = []
    for a in range(R):
        for b in range(R):
            P = polar_adj(M, Ac[b], p)
            X = matmul_forms(matmul_forms(Ac[a], P, p), M, p)
            Y = matmul_forms(matmul_forms(M, P, p), Ac[a], p)
            for c in range(R):
                v5.append(flat(times(X, lin[c]), idx4, p))
                v5.append(flat(times(Y, lin[c]), idx4, p))
    fams["fam5 l*A P_A(M) M / l*M P_A(M) A"] = v5
    # fam6
    v6 = []
    for a in range(R):
        for b in range(a, R):
            S = second_polar_adj(M, Ac[a], Ac[b], p)
            X = matmul_forms(matmul_forms(M, S, p), M, p)
            for c in range(R):
                v6.append(flat(times(X, lin[c]), idx4, p))
    fams["fam6 l*M ADJ(A,A,M) M"] = v6
    return fams, M, Adj, Ac, F, idx4


def syzygies_in_span(vecs, A, M, Adj, F, idx4, p):
    """W in span(vecs), W in L (x) S_4, tr(adj(M) W) = 0.  Returns the G-vectors."""
    nv = len(vecs)
    funcs, nf = complement_functionals(A, p)
    idx7 = mono_index(D, R)
    nrow = nf * len(idx4) + len(idx7)
    Mat = nmod_mat(nrow, nv, p)
    mons4 = monos(E, R)
    for jc, w in enumerate(vecs):
        # (i) projection to the complement of L, monomial by monomial
        for t, phi in enumerate(funcs):
            base = t * len(idx4)
            acc = [0] * len(idx4)
            for pos in range(N * N):
                cf = phi[pos] % p
                if not cf:
                    continue
                b2 = pos * len(idx4)
                for u in range(len(idx4)):
                    if w[b2 + u]:
                        acc[u] = (acc[u] + cf * w[b2 + u]) % p
            for u, val in enumerate(acc):
                if val:
                    Mat[base + u, jc] = val
        # (ii) tr(adj(M) W) = sum_{ij} adj_{ji} W_{ij}
        tr = {}
        for i in range(N):
            for j in range(N):
                b2 = (i * N + j) * len(idx4)
                Wij = {e: w[b2 + u] for u, e in enumerate(mons4) if w[b2 + u]}
                if Wij and Adj[j][i]:
                    tr = padd_p(tr, pmul_p(Adj[j][i], Wij, p), p)
        for e, val in tr.items():
            Mat[nf * len(idx4) + idx7[e], jc] = val
    X, nul = Mat.nullspace()
    out = []
    # pick 6 of the 16 coordinates on which L is already invertible, so that
    # W(s) = sum_k G_k A_k can be solved by a square system; W in L is already
    # enforced by condition (i), so any invertible 6-subset gives the same G.
    full = [[A[k][i][j] % p for k in range(R)] for i in range(N) for j in range(N)]
    pick = []
    cur = nmod_mat(0, R, p)
    for pos in range(N * N):
        cand = pick + [pos]
        T = nmod_mat(len(cand), R, [full[q][k] for q in cand for k in range(R)], p)
        if T.rank() == len(cand):
            pick = cand
        if len(pick) == R:
            break
    Lmat = nmod_mat(R, R, [full[q][k] for q in pick for k in range(R)], p)
    for c in range(nul):
        w = [0] * (N * N * len(idx4))
        for jv in range(nv):
            co = int(X[jv, c]) % p
            if co:
                for u in range(len(w)):
                    if vecs[jv][u]:
                        w[u] = (w[u] + co * vecs[jv][u]) % p
        g = [0] * (R * len(idx4))
        for u, e in enumerate(mons4):
            rhs = nmod_mat(R, 1, p); nz = False
            for t2, pos in enumerate(pick):
                val = w[pos * len(idx4) + u]
                if val:
                    rhs[t2, 0] = val; nz = True
            if not nz:
                continue
            sk = Lmat.solve(rhs)
            for k in range(R):
                g[k * len(idx4) + u] = int(sk[k, 0]) % p
        out.append(g)
    return out, nul


def main():
    seed0 = int(sys.argv[1]) if len(sys.argv) > 1 else 20260904
    npen = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    for t in range(npen):
        for p in PRIMES:
            rnd = random.Random(seed0 + 977 * t)
            A = rand_pencil(N, R, rnd, BOX)
            print(f"\n=== pencil {t}, p = {p} ===", flush=True)
            fams, M, Adj, Ac, F, idx4 = build_families(A, p)
            krows, nc = koszul_matrix(F, p)
            ksp = [{i: v for i, v in enumerate(r) if v} for r in krows]
            rk_k = rank_rows(ksp, nc, p)
            allv = []
            for name, vecs in fams.items():
                t0 = time.time()
                gs, nul = syzygies_in_span(vecs, A, M, Adj, F, idx4, p)
                sp = ksp + [{i: v for i, v in enumerate(g) if v} for g in gs]
                rk = rank_rows(sp, nc, p)
                print(f"  {name:<32} {len(vecs):>4} words -> {nul:>3} syzygies, "
                      f"NEW mod Koszul = {rk - rk_k}   [{time.time()-t0:.1f}s]", flush=True)
                allv.extend(vecs)
            t0 = time.time()
            gs, nul = syzygies_in_span(allv, A, M, Adj, F, idx4, p)
            sp = ksp + [{i: v for i, v in enumerate(g) if v} for g in gs]
            rk = rank_rows(sp, nc, p)
            print(f"  {'ALL FAMILIES TOGETHER':<32} {len(allv):>4} words -> {nul:>3} syzygies, "
                  f"NEW mod Koszul = {rk - rk_k}   [{time.time()-t0:.1f}s]", flush=True)
            print(f"  (dim Koszul = {rk_k}; the true answer is 6 new)", flush=True)


if __name__ == "__main__":
    main()
