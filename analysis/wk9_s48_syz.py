#!/usr/bin/env python3
"""
Session 48, target A -- the six non-Koszul syzygies of det_4 on a six-row pencil.

THE ANSATZ.  For M(s) = sum s_k A_k, 4x4, F = det M, differentiating
adj(M) = F M^{-1} gives the polynomial identity (degree 6, valid everywhere)

    (*)   tr( adj(M) A_a adj(M) A_b )  =  (d_a F)(d_b F)  -  F * d_a d_b F .

Now put, for x antisymmetric in (a,b),

    W(s)  =  sum_{a<b, c}  x_{abc} * s_c * ( A_a adj(M) A_b  -  A_b adj(M) A_a ) .

Then tr(adj(M) W) = sum x_{abc} s_c [ T_ab - T_ba ] = 0 by the SYMMETRY of (*)
in (a,b) -- the (d_aF)(d_bF) term is symmetric and the Hessian term is
symmetric, so every antisymmetric combination annihilates it identically.
So EVERY member of this 90-dimensional family is a syzygy of the partials the
moment it lies in L: writing W = sum_k G_k A_k gives sum_k G_k d_k F =
tr(adj(M) W) = 0.

The whole problem therefore collapses to ONE linear condition:

    W(s)  in  L (x) S_4 ,

i.e. 10 x 126 = 1260 linear equations on the 90 unknowns x_{abc}.  This script
solves that system, compares the solution space with the true non-Koszul
syzygies computed from the Macaulay nullspace, and reports both.

usage: wk9_s48_syz.py [seed] [--pencils N]
"""
import sys, os, random, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (P1, P2, PRIMES, monos, mono_index, dim_sym,
                          pderiv, pmul, padd, rand_pencil, pencil_entries,
                          det_form, submax_minors, ideal_rows, rank_rows)
from flint import nmod_mat

N, R, D = 4, 6, 7
E = D - N + 1          # 4, the degree of the coefficient forms G_k
BOX = 10 ** 6


def pscale(f, c, p):
    return {e: (v * c) % p for e, v in f.items() if (v * c) % p}


def padd_p(f, g, p):
    out = dict(f)
    for e, v in g.items():
        w = (out.get(e, 0) + v) % p
        if w: out[e] = w
        elif e in out: del out[e]
    return out


def pmul_p(f, g, p):
    out = {}
    for e1, v1 in f.items():
        for e2, v2 in g.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = (out.get(e, 0) + v1 * v2) % p
    return {e: v for e, v in out.items() if v}


def mat_of_forms(A, p):
    """M(s) as a 4x4 array of linear forms (dicts)."""
    M = [[dict() for _ in range(N)] for _ in range(N)]
    for k in range(R):
        for i in range(N):
            for j in range(N):
                c = A[k][i][j] % p
                if c:
                    e = tuple(1 if t == k else 0 for t in range(R))
                    M[i][j][e] = (M[i][j].get(e, 0) + c) % p
    return M


def adjugate(M, p):
    """adj(M)_{ij} = (-1)^{i+j} * minor(M, j, i)  (cofactor transpose)."""
    def minor3(rows, cols):
        # 3x3 determinant of forms
        tot = {}
        for perm, sg in (((0,1,2),1), ((1,2,0),1), ((2,0,1),1),
                         ((0,2,1),-1), ((2,1,0),-1), ((1,0,2),-1)):
            t = {(0,)*R: 1}
            for a in range(3):
                t = pmul_p(t, M[rows[a]][cols[perm[a]]], p)
            tot = padd_p(tot, pscale(t, sg % p, p), p)
        return tot
    Adj = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rows = [x for x in range(N) if x != j]
            cols = [x for x in range(N) if x != i]
            m = minor3(rows, cols)
            Adj[i][j] = pscale(m, (-1) ** (i + j) % p, p)
    return Adj


def matmul_forms(X, Y, p):
    Z = [[dict() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            acc = {}
            for k in range(N):
                if X[i][k] and Y[k][j]:
                    acc = padd_p(acc, pmul_p(X[i][k], Y[k][j], p), p)
            Z[i][j] = acc
    return Z


def const_mat(Ak, p):
    return [[({(0,)*R: Ak[i][j] % p} if Ak[i][j] % p else {}) for j in range(N)]
            for i in range(N)]


def complement_functionals(A, p):
    """10 linear functionals on M_4 (as 16-vectors) vanishing on L = span(A_k)."""
    rows = [[A[k][i][j] % p for i in range(N) for j in range(N)] for k in range(R)]
    Mt = nmod_mat(R, N * N, [v for r in rows for v in r], p)
    X, nul = Mt.nullspace()          # columns span ker of the R x 16 matrix
    return [[int(X[i, j]) for i in range(N * N)] for j in range(nul)], nul


def ansatz_space(A, p, verbose=True):
    """Solve  W(s) in L (x) S_4  over the 90-dim antisymmetric family."""
    M = mat_of_forms(A, p)
    Adj = adjugate(M, p)
    Aconst = [const_mat(A[k], p) for k in range(R)]
    # E_ab = A_a adj(M) A_b - A_b adj(M) A_a, a 4x4 matrix of cubics
    Eab = {}
    for a in range(R):
        for b in range(a + 1, R):
            X = matmul_forms(matmul_forms(Aconst[a], Adj, p), Aconst[b], p)
            Y = matmul_forms(matmul_forms(Aconst[b], Adj, p), Aconst[a], p)
            Eab[(a, b)] = [[padd_p(X[i][j], pscale(Y[i][j], p - 1, p), p)
                            for j in range(N)] for i in range(N)]
    funcs, nf = complement_functionals(A, p)
    idx4 = mono_index(E, R)
    cols = []                                     # one column per unknown x_abc
    keys = []
    for (a, b) in sorted(Eab):
        for c in range(R):
            sc = {tuple(1 if t == c else 0 for t in range(R)): 1}
            col = [0] * (nf * len(idx4))
            for i in range(N):
                for j in range(N):
                    f = Eab[(a, b)][i][j]
                    if not f:
                        continue
                    g = pmul_p(f, sc, p)
                    pos = i * N + j
                    for t, phi in enumerate(funcs):
                        cf = phi[pos] % p
                        if not cf:
                            continue
                        base = t * len(idx4)
                        for e, v in g.items():
                            col[base + idx4[e]] = (col[base + idx4[e]] + cf * v) % p
            cols.append(col); keys.append((a, b, c))
    nrows = nf * len(idx4)
    Mat = nmod_mat(nrows, len(cols), p)
    for jc, col in enumerate(cols):
        for ir, v in enumerate(col):
            if v:
                Mat[ir, jc] = v
    X, nul = Mat.nullspace()
    sols = [[int(X[i, j]) for i in range(len(cols))] for j in range(nul)]
    if verbose:
        print(f"  ansatz: {nrows} conditions on {len(cols)} unknowns "
              f"-> solution space dim = {nul}", flush=True)
    return sols, keys, Eab, M, Adj, funcs


def syzygy_vector(sol, keys, Eab, A, p):
    """Turn a solution x into G = (G_1..G_6) with sum_k G_k A_k = W."""
    W = [[dict() for _ in range(N)] for _ in range(N)]
    for x, (a, b, c) in zip(sol, keys):
        if x % p == 0:
            continue
        sc = {tuple(1 if t == c else 0 for t in range(R)): 1}
        for i in range(N):
            for j in range(N):
                f = Eab[(a, b)][i][j]
                if f:
                    W[i][j] = padd_p(W[i][j], pscale(pmul_p(f, sc, p), x % p, p), p)
    # solve W(s) = sum_k G_k A_k monomial by monomial
    idx4 = mono_index(E, R)
    Lmat = nmod_mat(N * N, R, p)
    for k in range(R):
        for i in range(N):
            for j in range(N):
                if A[k][i][j] % p:
                    Lmat[i * N + j, k] = A[k][i][j] % p
    G = [dict() for _ in range(R)]
    for e in monos(E, R):
        rhs = nmod_mat(N * N, 1, p)
        nz = False
        for i in range(N):
            for j in range(N):
                v = W[i][j].get(e, 0) % p
                if v:
                    rhs[i * N + j, 0] = v; nz = True
        if not nz:
            continue
        sol_k = Lmat.solve(rhs)      # exact; L has full column rank 6
        for k in range(R):
            v = int(sol_k[k, 0]) % p
            if v:
                G[k][e] = v
    return G, W


def check_syzygy(G, F, p):
    """sum_k G_k * dF/ds_k  ==  0 ?"""
    tot = {}
    for k in range(R):
        if not G[k]:
            continue
        dk = {e: v % p for e, v in pderiv(F, k).items() if v % p}
        tot = padd_p(tot, pmul_p(G[k], dk, p), p)
    return len(tot) == 0


def koszul_matrix(F, p):
    """the 90 Koszul syzygies as coefficient vectors in (S_4)^6."""
    idx4 = mono_index(E, R)
    grads = [{e: v % p for e, v in pderiv(F, k).items() if v % p} for k in range(R)]
    rows = []
    for k in range(R):
        for l in range(k + 1, R):
            for mu in monos(E - (N - 1), R):
                vec = [0] * (R * len(idx4))
                mm = {mu: 1}
                for e, v in pmul_p(grads[l], mm, p).items():
                    vec[k * len(idx4) + idx4[e]] = v
                for e, v in pmul_p(grads[k], mm, p).items():
                    vec[l * len(idx4) + idx4[e]] = (vec[l * len(idx4) + idx4[e]] - v) % p
                rows.append(vec)
    return rows, R * len(idx4)


def gvec(G, p):
    idx4 = mono_index(E, R)
    vec = [0] * (R * len(idx4))
    for k in range(R):
        for e, v in G[k].items():
            vec[k * len(idx4) + idx4[e]] = v % p
    return vec


def main():
    seed0 = int(sys.argv[1]) if len(sys.argv) > 1 else 20260904
    npen = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    print("# s48 target A -- the antisymmetric adj-word ansatz")
    print("#   W = sum_{a<b,c} x_abc s_c ( A_a adj(M) A_b - A_b adj(M) A_a )")
    print("#   tr(adj(M) W) = 0 identically for EVERY x, by (*); the only")
    print("#   condition is W in L (x) S_4.")
    for t in range(npen):
        for p in PRIMES:
            rnd = random.Random(seed0 + 977 * t)
            A = rand_pencil(N, R, rnd, BOX)
            F = det_form(pencil_entries(A, N, R), N)
            F = {e: v % p for e, v in F.items() if v % p}
            print(f"pencil {t}  p={p}", flush=True)
            t0 = time.time()
            sols, keys, Eab, M, Adj, funcs = ansatz_space(A, p)
            # each solution really is a syzygy?
            ok = True
            vecs = []
            for sol in sols:
                G, W = syzygy_vector(sol, keys, Eab, A, p)
                ok &= check_syzygy(G, F, p)
                vecs.append(gvec(G, p))
            print(f"  all {len(sols)} are genuine syzygies of the partials: {ok}", flush=True)
            # how many are NEW, i.e. non-Koszul?
            krows, nc = koszul_matrix(F, p)
            rk_k = rank_rows([{i: v for i, v in enumerate(r) if v} for r in krows], nc, p)
            allr = krows + [v for v in vecs]
            rk_a = rank_rows([{i: v for i, v in enumerate(r) if v} for r in allr], nc, p)
            print(f"  dim Koszul = {rk_k};  dim (Koszul + ansatz) = {rk_a};"
                  f"  NEW = {rk_a - rk_k}   [{time.time()-t0:.1f}s]", flush=True)


if __name__ == "__main__":
    main()
