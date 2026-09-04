#!/usr/bin/env python3
"""
Session 48, target A -- the true six, their invariants, and the last natural
family (two constant slots inside a polarised adjugate).

  (a) extract the six non-Koszul syzygies from the Macaulay left kernel,
  (b) re-measure whether their coefficient forms G_k lie in J(M)_4,
  (c) rank of W(s) = sum G_k A_k at a generic s, and whether det W == 0,
  (d) fam7 = { q(s) * A_a ADJ(A_b, M, M) A_c },  q in S_2 -- the only s-degree-4
      equivariant one-adjugate word shape not already covered by
      wk9_s48_syzfam.py.  Its span is reported first: if it is all of
      M_4 (x) S_4 the test is vacuous and is labelled so.

usage: wk9_s48_syzprobe.py [seed]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (PRIMES, monos, mono_index, pderiv, rand_pencil,
                          pencil_entries, det_form, submax_minors, ideal_rows,
                          rank_rows)
from wk9_s48_syz import (mat_of_forms, adjugate, matmul_forms, const_mat,
                         pmul_p, padd_p, pscale, koszul_matrix)
from wk9_s48_syzfam import polar_adj, flat, syzygies_in_span
from flint import nmod_mat

N, R, D, E = 4, 6, 7, 4
BOX = 10 ** 6


def macaulay_left_kernel(F, p):
    idx7 = mono_index(D, R); idx4 = mono_index(E, R)
    mons4 = monos(E, R)
    grads = [{e: v % p for e, v in pderiv(F, k).items() if v % p} for k in range(R)]
    nr = R * len(mons4)
    Mt = nmod_mat(len(idx7), nr, p)          # transpose: columns are the rows of M_7
    i = 0
    for k in range(R):
        for m in mons4:
            for e, c in grads[k].items():
                ee = tuple(x + y for x, y in zip(e, m))
                Mt[idx7[ee], i] = c
            i += 1
    X, nul = Mt.nullspace()
    return [[int(X[i, j]) for i in range(nr)] for j in range(nul)], nul


def main():
    seed0 = int(sys.argv[1]) if len(sys.argv) > 1 else 20260904
    for p in PRIMES:
        rnd = random.Random(seed0)
        A = rand_pencil(N, R, rnd, BOX)
        F = det_form(pencil_entries(A, N, R), N)
        F = {e: v % p for e, v in F.items() if v % p}
        idx4 = mono_index(E, R); mons4 = monos(E, R)
        print(f"\n=== pencil seed {seed0}, p = {p} ===", flush=True)

        syz, nul = macaulay_left_kernel(F, p)
        krows, nc = koszul_matrix(F, p)
        ksp = [{i: v for i, v in enumerate(r) if v} for r in krows]
        rk_k = rank_rows(ksp, nc, p)
        allsp = ksp + [{i: v for i, v in enumerate(g) if v} for g in syz]
        rk_a = rank_rows(allsp, nc, p)
        print(f"(a) dim Syz_7 = {nul}   dim Koszul = {rk_k}   "
              f"non-Koszul = {rk_a - rk_k}", flush=True)

        # extract 6 representatives spanning the quotient
        extra, cur = [], list(ksp)
        base = rk_k
        for g in syz:
            gd = {i: v for i, v in enumerate(g) if v}
            r2 = rank_rows(cur + [gd], nc, p)
            if r2 > base:
                extra.append(g); cur.append(gd); base = r2
            if base == rk_a:
                break
        print(f"    extracted {len(extra)} representatives of Syz/Koszul", flush=True)

        # (b) do the G_k lie in J(M)_4 (the ideal of the sixteen 3x3 minors)?
        mins = submax_minors(pencil_entries(A, N, R), N)
        mins = [{e: v % p for e, v in g.items() if v % p} for g in mins]
        jrows, jn = ideal_rows(mins, N - 1, E, R)
        rkJ = rank_rows(jrows, jn, p)
        inJ = 0
        for g in extra:
            for k in range(R):
                gk = {e: g[k * len(mons4) + u] for u, e in enumerate(mons4)
                      if g[k * len(mons4) + u]}
                if not gk:
                    continue
                if rank_rows(jrows + [{idx4[e]: v for e, v in gk.items()}], jn, p) == rkJ:
                    inJ += 1
        print(f"(b) dim J(M)_4 = {rkJ} (of {jn});  coefficient forms G_k lying in "
              f"J(M)_4: {inJ} of {6*R}", flush=True)

        # (c) rank of W(s) at a random s, and det W
        Mf = mat_of_forms(A, p); Adj = adjugate(Mf, p)
        pt = [rnd.randrange(1, p) for _ in range(R)]
        def ev(f):
            t = 0
            for e, c in f.items():
                m = c
                for v, x in zip(e, pt):
                    for _ in range(x):
                        m = (m * pt[0]) % p     # placeholder, replaced below
            return t
        def evalf(f):
            tot = 0
            for e, c in f.items():
                m = c % p
                for v in range(R):
                    for _ in range(e[v]):
                        m = (m * pt[v]) % p
                tot = (tot + m) % p
            return tot
        ranks = []
        for g in extra:
            Wn = nmod_mat(N, N, p)
            for i in range(N):
                for j in range(N):
                    acc = 0
                    for k in range(R):
                        gk = {e: g[k * len(mons4) + u] for u, e in enumerate(mons4)
                              if g[k * len(mons4) + u]}
                        if gk:
                            acc = (acc + evalf(gk) * (A[k][i][j] % p)) % p
                    Wn[i, j] = acc
            ranks.append(Wn.rank())
        print(f"(c) rank W(s) at a random s, over the six: {ranks}", flush=True)

        # (d) fam7
        Ac = [const_mat(A[k], p) for k in range(R)]
        mons2 = monos(2, R)
        vecs = []
        t0 = time.time()
        for a in range(R):
            for b in range(R):
                P = polar_adj(Mf, Ac[b], p)
                for c in range(R):
                    X = matmul_forms(matmul_forms(Ac[a], P, p), Ac[c], p)
                    for q in mons2:
                        qq = {q: 1}
                        Y = [[pmul_p(X[i][j], qq, p) for j in range(N)] for i in range(N)]
                        vecs.append(flat(Y, idx4, p))
        dimspan = rank_rows([{i: v for i, v in enumerate(w) if v} for w in vecs],
                            N * N * len(mons4), p)
        print(f"(d) fam7 q(s)*A_a ADJ(A_b,M,M) A_c : {len(vecs)} words, "
              f"span dim {dimspan} of {N*N*len(mons4)}"
              f"{'  -- VACUOUS (spans everything)' if dimspan == N*N*len(mons4) else ''}",
              flush=True)
        if dimspan < N * N * len(mons4):
            gs, nul7 = syzygies_in_span(vecs, A, Mf, Adj, F, idx4, p)
            sp = ksp + [{i: v for i, v in enumerate(g) if v} for g in gs]
            print(f"    -> {nul7} syzygies, NEW mod Koszul = "
                  f"{rank_rows(sp, nc, p) - rk_k}   [{time.time()-t0:.1f}s]", flush=True)


if __name__ == "__main__":
    main()
