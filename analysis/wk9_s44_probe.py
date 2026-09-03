#!/usr/bin/env python3
"""
Session 44 -- structure probes on the six extra (non-Koszul) syzygies at
(n, r, d) = (4, 6, 7).

A syzygy sum_k G_k dF/ds_k = 0 is a degree-4 vector field annihilating F, i.e.
an element of Der(-log F)_0 in degree 4; the Koszul ones are the trivial
derivations (dF/ds_l) d/ds_k - (dF/ds_k) d/ds_l.  Probes:

  (a) rank of the matrix W(s) = sum_k G_k(s) A_k at random points s -- a low
      generic rank would mean the syzygies factor through a small piece of the
      pencil;
  (b) dimension of the span of the 36 forms G_k, and of that span plus J(M)_4,
      plus F, plus the "Koszul-shaped" space span{s_j dF/ds_i};
  (c) whether the six W's lie in { X M(s) + M(s) Y : tr X + tr Y = 0 } with X, Y
      of degree 3 restricted to the small natural families adj(M)A, A adj(M),
      cI -- the families that turn out to give only Koszul syzygies.

usage: wk9_s44_probe.py [seed]
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *
from wk9_s44_syzygy import left_kernel, koszul_vectors, rank_of, dense
from flint import nmod_mat

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
N, R, D, BOX = 4, 6, 7, 10 ** 6
E = D - N + 1
p = PRIMES[0]

rnd = random.Random(SEED)
A = rand_pencil(N, R, rnd, BOX)
ent = pencil_entries(A, N, R)
F = det_form(ent, N)
grads = [pderiv(F, i) for i in range(R)]
rows, nc = ideal_rows(grads, N - 1, D, R)
nb = len(monos(E, R))
ker, nul = left_kernel(rows, nc, p)
kos = koszul_vectors(grads, p)
dk = rank_of(kos, R * nb, p)
extra, cur, base = [], list(kos), dk
for v in ker:
    if rank_of(cur + [v], R * nb, p) > base:
        extra.append(v); cur.append(v); base += 1
print(f"[s44 probe] nullity {nul} = Koszul {dk} + extra {len(extra)}")

mE = monos(E, R)


def evalform(g, pt):
    return sum(c * pow_prod(e, pt) for e, c in g.items()) % p


def pow_prod(e, pt):
    v = 1
    for i, k in enumerate(e):
        if k: v = v * pow(pt[i], k, p) % p
    return v


# (a) generic rank of W(s)
print("\n(a) rank of W(s) = sum_k G_k(s) A_k at five random points of P^5:")
for a, v in enumerate(extra):
    ranks = []
    for _ in range(5):
        pt = [rnd.randrange(1, p) for _ in range(R)]
        Gv = [evalform({e: v[k * nb + i] for i, e in enumerate(mE) if v[k * nb + i]}, pt)
              for k in range(R)]
        M4 = [[sum(Gv[k] * A[k][i][j] for k in range(R)) % p for j in range(N)]
              for i in range(N)]
        ranks.append(nmod_mat(N, N, [x % p for row in M4 for x in row], p).rank())
    print(f"    extra {a}: ranks of W at random points {ranks}")

# (b) spans
allG = []
for v in extra:
    for k in range(R):
        g = {mono_index(E, R)[e]: v[k * nb + i] for i, e in enumerate(mE) if v[k * nb + i]}
        if g: allG.append(g)
dG = rank_rows(allG, dim_sym(E, R), p)
minors = submax_minors(ent, N)
jrows, jnc = ideal_rows(minors, N - 1, E, R)
dJ = rank_rows(jrows, jnc, p)
dJG = rank_rows(jrows + allG, jnc, p)
kosshape = []
idxE = mono_index(E, R)
for i in range(R):
    for j in range(R):
        row = {}
        for e, c in grads[i].items():
            ee = list(e); ee[j] += 1
            row[idxE[tuple(ee)]] = row.get(idxE[tuple(ee)], 0) + c
        kosshape.append(row)
dK = rank_rows(kosshape, jnc, p)
dKG = rank_rows(kosshape + allG, jnc, p)
print(f"\n(b) span of the {len(allG)} coefficient forms G_k in S_4 (dim {dim_sym(E,R)}):"
      f" {dG}")
print(f"    J(M)_4 has dim {dJ}; J(M)_4 + span(G) has dim {dJG} "
      f"(so span(G) meets J(M)_4 in {dG + dJ - dJG})")
print(f"    span{{s_j * dF/ds_i}} has dim {dK}; with span(G): {dKG} "
      f"(so span(G) meets it in {dG + dK - dKG})")

# (c) the natural families
nat = []
for i in range(R):
    # X = adj(M) A_i - (1/4) tr(adj(M)A_i) I  ->  W = F A_i - (1/4) (d_i F) M
    w = [0] * (N * N * nb)
    for a_ in range(N):
        for b_ in range(N):
            for e, c in F.items():
                w[(a_ * N + b_) * nb + idxE[e]] = (w[(a_ * N + b_) * nb + idxE[e]]
                                                  + c * A[i][a_][b_]) % p
    inv4 = pow(4, p - 2, p)
    for k in range(R):
        for e, c in grads[i].items():
            ee = list(e); ee[k] += 1; ee = tuple(ee)
            for a_ in range(N):
                for b_ in range(N):
                    if A[k][a_][b_]:
                        j = (a_ * N + b_) * nb + idxE[ee]
                        w[j] = (w[j] - inv4 * c * A[k][a_][b_]) % p
    nat.append(w)
dn = rank_of(nat, N * N * nb, p)
wex = []
for v in extra:
    w = [0] * (N * N * nb)
    for k in range(R):
        for i, e in enumerate(mE):
            c = v[k * nb + i]
            if not c: continue
            for a_ in range(N):
                for b_ in range(N):
                    w[(a_ * N + b_) * nb + i] = (w[(a_ * N + b_) * nb + i]
                                                 + c * A[k][a_][b_]) % p
    wex.append(w)
print(f"\n(c) the natural family W_i = F A_i - (1/4)(d_i F) M(s) spans dim {dn};"
      f" with the six extra W's: {rank_of(nat + wex, N*N*nb, p)} "
      f"(extra dim {rank_of(nat + wex, N*N*nb, p) - dn}) -- the natural family is"
      f" Koszul, so the extra six are outside it as expected")
