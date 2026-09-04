#!/usr/bin/env python3
"""
Session 44, Phase 3 -- the syzygies behind the drop at (n, r, d) = (4, 6, 7).

rank M_d = r*dim S_{d-n+1} - dim Syz_d, and the generic (smooth) value is
attained exactly when Syz_d is the Koszul span.  The drop is therefore the
dimension of the non-Koszul syzygies.  This script

  (a) computes the left kernel of M_d at a determinantal point (both primes),
  (b) computes the Koszul span (C(r,2) * dim S_{d-2n+2} vectors),
  (c) reports dim (Syz / Koszul) -- the drop -- and
  (d) probes the structure of the extra syzygies: whether the coefficient
      forms G_k lie in J(M)_{d-n+1} (the ideal of the (n-1)-minors), and
      whether the matrix W(s) = sum_k G_k A_k lies in the space
      { X M + M Y : tr(X + Y) = 0 } spanned by the Gulliksen-Negard linear
      syzygies of the minors -- which it must, if GN generates.

usage: wk9_s44_syzygy.py [seed] [n] [r] [d]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *
from flint import nmod_mat

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
N = int(sys.argv[2]) if len(sys.argv) > 2 else 4
R = int(sys.argv[3]) if len(sys.argv) > 3 else 6
D = int(sys.argv[4]) if len(sys.argv) > 4 else 7
BOX = 10 ** 6
E = D - N + 1                       # multiplier degree


def dense(rows, nc, p):
    ent = [0] * (len(rows) * nc)
    for i, row in enumerate(rows):
        b = i * nc
        for c, v in row.items():
            ent[b + c] = v % p
    return nmod_mat(len(rows), nc, ent, p)


def left_kernel(rows, nc, p):
    M = dense(rows, nc, p)
    Mt = M.transpose()
    X, nul = Mt.nullspace()
    return [[int(X[i, j]) for i in range(len(rows))] for j in range(nul)], nul


def koszul_vectors(grads, p):
    """Koszul syzygies in degree D: for k<l and each monomial mu of degree
    D-2(n-1), the vector with block k = mu*grad_l and block l = -mu*grad_k."""
    idxE = mono_index(E, R)
    nb = len(monos(E, R))
    out = []
    deg_mu = D - 2 * (N - 1)
    if deg_mu < 0:
        return out
    for k in range(R):
        for l in range(k + 1, R):
            for mu in monos(deg_mu, R):
                v = [0] * (R * nb)
                for e, c in grads[l].items():
                    ee = tuple(x + y for x, y in zip(e, mu))
                    v[k * nb + idxE[ee]] = (v[k * nb + idxE[ee]] + c) % p
                for e, c in grads[k].items():
                    ee = tuple(x + y for x, y in zip(e, mu))
                    v[l * nb + idxE[ee]] = (v[l * nb + idxE[ee]] - c) % p
                out.append(v)
    return out


def rank_of(vecs, nc, p):
    if not vecs: return 0
    return nmod_mat(len(vecs), nc, [x % p for v in vecs for x in v], p).rank()


def run(p, seed):
    rnd = random.Random(seed)
    A = rand_pencil(N, R, rnd, BOX)
    ent = pencil_entries(A, N, R)
    F = det_form(ent, N)
    grads = [pderiv(F, i) for i in range(R)]
    rows, nc = ideal_rows(grads, N - 1, D, R)
    nb = len(monos(E, R))
    rho = rho_generic(D, N, R)
    rk = dense(rows, nc, p).rank()
    ker, nul = left_kernel(rows, nc, p)
    kos = koszul_vectors(grads, p)
    dk = rank_of(kos, R * nb, p)
    both = rank_of(kos + ker, R * nb, p)
    print(f"  p={p} seed={seed}: rows {len(rows)} cols {nc} rank {rk} (rho {rho}, "
          f"drop {rho-rk}) | nullity {nul} = Koszul {dk} + extra {both-dk} "
          f"[span check {'OK' if both==nul else 'BROKEN'}]")

    # --- extract the extra syzygies modulo Koszul
    stacked = kos + ker
    M = nmod_mat(len(stacked), R * nb, [x % p for v in stacked for x in v], p)
    Rr = M.rref()[0]
    # greedily pick kernel vectors independent modulo Koszul
    extra, cur = [], list(kos)
    base = dk
    for v in ker:
        t = rank_of(cur + [v], R * nb, p)
        if t > base:
            extra.append(v); cur.append(v); base = t
    print(f"  extracted {len(extra)} extra syzygies (expect {nul-dk})")

    # --- probe 1: do the coefficient forms G_k lie in the minor ideal J(M)_E?
    minors = submax_minors(ent, N)
    jrows, jnc = ideal_rows(minors, N - 1, E, R)
    jdim = rank_rows(jrows, jnc, p)
    print(f"  J(M)_{E}: dim {jdim} of {jnc} (GN predicts {dim_sym(E,R)-H_GN(E,N,R)})")
    for a, v in enumerate(extra):
        inside = []
        for k in range(R):
            g = {e: v[k * nb + i] for i, e in enumerate(monos(E, R)) if v[k * nb + i]}
            if not g:
                inside.append('0'); continue
            grow = [{mono_index(E, R)[e]: c for e, c in g.items()}]
            inside.append('in' if rank_rows(jrows + grow, jnc, p) == jdim else 'OUT')
        print(f"    extra {a}: G_k in J(M)_{E}? {inside}")

    # --- probe 2: is W(s) = sum_k G_k A_k of the form X M + M Y, tr(X+Y)=0 ?
    # basis of {X M(s) + M(s) Y : tr X + tr Y = 0} tensored with S_{E-1},
    # inside M_N tensor S_E ; compare ranks with and without each extra W.
    idxE = mono_index(E, R)
    def wvec(v):
        """W = sum_k G_k A_k as a vector in (N*N) x dim S_E."""
        w = [0] * (N * N * nb)
        for k in range(R):
            for i, e in enumerate(monos(E, R)):
                c = v[k * nb + i]
                if not c: continue
                for a in range(N):
                    for b in range(N):
                        w[(a * N + b) * nb + i] = (w[(a * N + b) * nb + i]
                                                   + c * A[k][a][b]) % p
        return w
    gn = []
    for (X, Y) in gn_basis(N):
        # (X M(s) + M(s) Y) has linear entries; multiply by each monomial of degree E-1
        lin = [[[0] * R for _ in range(N)] for _ in range(N)]
        for k in range(R):
            XA = [[sum(X[a][c] * A[k][c][b] for c in range(N)) for b in range(N)] for a in range(N)]
            AY = [[sum(A[k][a][c] * Y[c][b] for c in range(N)) for b in range(N)] for a in range(N)]
            for a in range(N):
                for b in range(N):
                    lin[a][b][k] = XA[a][b] + AY[a][b]
        for mu in monos(E - 1, R):
            w = [0] * (N * N * nb)
            for k in range(R):
                e = list(mu); e[k] += 1; e = tuple(e)
                j = idxE[e]
                for a in range(N):
                    for b in range(N):
                        if lin[a][b][k]:
                            w[(a * N + b) * nb + j] = (w[(a * N + b) * nb + j]
                                                       + lin[a][b][k]) % p
            gn.append(w)
    gdim = rank_of(gn, N * N * nb, p)
    print(f"  span{{ (XM+MY)*S_{E-1} : tr(X+Y)=0 }} has dim {gdim}")
    for a, v in enumerate(extra):
        w = wvec(v)
        print(f"    extra {a}: W in that span? "
              f"{'YES' if rank_of(gn + [w], N*N*nb, p) == gdim else 'NO'}")
    return rho - rk, nul - dk


def gn_basis(n):
    """a basis of {(X, Y) in gl_n + gl_n : tr X + tr Y = 0} modulo (I, -I):
    2n^2 - 2 pairs."""
    out = []
    for a in range(n):
        for b in range(n):
            if a == b: continue
            X = [[0] * n for _ in range(n)]; X[a][b] = 1
            out.append((X, [[0] * n for _ in range(n)]))
            Y = [[0] * n for _ in range(n)]; Y[a][b] = 1
            out.append(([[0] * n for _ in range(n)], Y))
    # traceless diagonal parts: E_aa - E_{a+1,a+1} on each side, plus the
    # mixed (E_00, -E_00)
    for a in range(n - 1):
        X = [[0] * n for _ in range(n)]; X[a][a] = 1; X[a + 1][a + 1] = -1
        out.append((X, [[0] * n for _ in range(n)]))
        Y = [[0] * n for _ in range(n)]; Y[a][a] = 1; Y[a + 1][a + 1] = -1
        out.append(([[0] * n for _ in range(n)], Y))
    X = [[0] * n for _ in range(n)]; X[0][0] = 1
    Y = [[0] * n for _ in range(n)]; Y[0][0] = -1
    out.append((X, Y))
    return out


if __name__ == '__main__':
    t0 = time.time()
    print(f"[s44 syzygy] n={N} r={R} d={D}, multiplier degree {E}")
    print(f"  gn_basis size {len(gn_basis(N))} (expect {2*N*N-2})")
    for p in PRIMES:
        for s in (SEED, SEED + 11):
            run(p, s)
    print(f"[s44 syzygy] done in {time.time()-t0:.1f}s")
