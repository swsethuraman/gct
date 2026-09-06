"""Session 56 — the Foulkes engine at delta = 2, 3: the full Hecke route (a) and
the weight-space route (b) on the whole of H_{4,delta}.

    python3 analysis/wk9_s56_hecke.py <delta>

Writes results/s56_hecke_d<delta>.json.  Exact arithmetic throughout.

The signed kernel.  pi -> eps_pi is NOT S_N-equivariant: g.eps_pi =
sigma(g,pi) eps_{g pi} with sigma the product of block-sorting signs.  With the
coset representative g_pi (increasing on each block) eps_pi = g_pi . eps_0, so

    K(pi, pi') = <eps_0, h . eps_0> = sigma(h, pi0) K(pi0, h pi0),   h = g_pi^{-1} g_pi',

and one directly computed row K(pi0, .) gives the whole signed Gram matrix.
Its square beta = K∘K is S_N-invariant and depends only on the double coset;
beta is the Gram matrix of Theta^+(pi) = eps_pi (x) eps_pi.
"""
import itertools
import json
import os
import sys
import time
from fractions import Fraction
from math import factorial

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
import wk9_s56_core as C            # noqa: E402
from pleth import ambient_multiplicity   # noqa: E402

delta = int(sys.argv[1])
N = 4 * delta
t0 = time.time()
log = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(f"[{time.time()-t0:7.1f}s] {s}", flush=True)
    log.append(s)


# ------------------------------------------------------------------ H_{4,delta}
H = C.set_partitions(N)
nH = len(H)
index = {pi: i for i, pi in enumerate(H)}
say(f"delta={delta} N={N} |H|={nH}")
pi0 = C.standard_partition(delta)
i0 = index[pi0]

labels = np.zeros((nH, N), dtype=np.int64)
for i, pi in enumerate(H):
    for j, m in enumerate(pi):
        for pos in range(N):
            if m >> pos & 1:
                labels[i, pos] = j
onehot = np.zeros((nH, N, delta), dtype=np.int64)
for j in range(delta):
    onehot[:, :, j] = (labels == j)

# ---------------------------------------------- double cosets W\S_N/W via rel
all_labelled = C.margin4_matrices(delta)
canon = {M: C.canonical_matrix(M) for M in all_labelled}
d_keys = sorted(set(canon.values()))
d_index = {k: i for i, k in enumerate(d_keys)}
rel_of_labelled = {M: d_index[canon[M]] for M in all_labelled}
nd = len(d_keys)
reps = {}
for i, pi in enumerate(H):
    key = C.rel(pi0, pi)
    assert key in d_index
    reps.setdefault(key, pi)
assert len(reps) == nd, "every double coset must be met from pi0"
say(f"labelled margin-4 matrices: {len(all_labelled)}; double cosets W\\S_N/W: {nd}")

powers = 5 ** np.arange(delta * delta, dtype=np.int64)
codes = np.array([sum(M[j][l] * 5 ** (delta * j + l) for j in range(delta) for l in range(delta))
                  for M in rel_of_labelled], dtype=np.int64)
ids = np.array([rel_of_labelled[M] for M in rel_of_labelled], dtype=np.int64)
order = np.argsort(codes)
codes_sorted, ids_sorted = codes[order], ids[order]


def rel_ids_row(i):
    M = np.einsum("pj,kpl->kjl", onehot[i], onehot)
    code = (M.reshape(nH, delta * delta) * powers).sum(axis=1)
    pos = np.searchsorted(codes_sorted, code)
    assert np.all(codes_sorted[pos] == code)
    return ids_sorted[pos]


D = np.zeros((nH, nH), dtype=np.int16)
for i in range(nH):
    D[i] = rel_ids_row(i)
say("relation matrix built")
dsize = np.bincount(D[i0].astype(np.int64), minlength=nd)
assert int(dsize.sum()) == nH

# ------------------------------------------------------- the signed kernel row
krow = C.krow_direct(H, delta)                    # K(pi0, pi) for all pi, signed
assert krow[i0] == 24 ** delta
Kd_abs = {}
for i, pi in enumerate(H):
    d = int(D[i0, i])
    Kd_abs.setdefault(d, abs(krow[i]))
    assert Kd_abs[d] == abs(krow[i]), "|K| is not constant on a double coset"
say("|K_d| by double coset:", {d: Kd_abs[d] for d in sorted(Kd_abs)})

# the full signed matrix: K(pi,pi') = sigma(h,pi0) K(pi0, h pi0), h = g_pi^{-1} g_pi'.
# h pi0 = g_pi^{-1}(pi'), and sigma(h, pi0) is the product over blocks of pi' of
# the sorting sign of g_pi^{-1} on that block.  Vectorised over pi'.
greps = [C.coset_rep(pi, delta) for pi in H]
ginv = np.zeros((nH, N), dtype=np.int64)
for a, g in enumerate(greps):
    for i, gi in enumerate(g):
        ginv[a, gi] = i
blockpos = np.zeros((nH, delta, 4), dtype=np.int64)
for b, pi in enumerate(H):
    for j, m in enumerate(pi):
        blockpos[b, j] = C.block_positions(m, N)
keyidx = -np.ones(delta ** N, dtype=np.int64)
dpow = delta ** np.arange(N, dtype=np.int64)
for i in range(nH):
    keyidx[int((labels[i] * dpow).sum())] = i
krow_arr = np.array(krow, dtype=np.int64)
Kfull = np.zeros((nH, nH), dtype=np.int64)
ar = np.arange(nH)
for a in range(nH):
    Q = ginv[a][blockpos]                              # (nH, delta, 4): g_a^{-1} of each block of pi_b
    inv = np.zeros(nH, dtype=np.int64)
    for i in range(4):
        for j in range(i + 1, 4):
            inv += (Q[:, :, i] > Q[:, :, j]).sum(axis=1)
    sign = 1 - 2 * (inv % 2)
    mins = Q.min(axis=2)                               # (nH, delta)
    ranks = np.argsort(np.argsort(mins, axis=1), axis=1)
    lab = np.zeros((nH, N), dtype=np.int64)
    for j in range(delta):
        for t in range(4):
            lab[ar, Q[:, j, t]] = ranks[:, j]
    idx = keyidx[(lab * dpow).sum(axis=1)]
    assert np.all(idx >= 0)
    Kfull[a] = sign * krow_arr[idx]
say("signed Gram matrix built")
# validation of the sign formula against the direct tensor sum on a sample
rng = np.random.default_rng(20260905)
sample = [(int(a), int(b)) for a, b in rng.integers(0, nH, size=(40 if delta == 3 else 200, 2))]
for a, b in sample:
    assert Kfull[a, b] == C.kernel_K(H[a], H[b], N), (a, b)
assert np.array_equal(Kfull, Kfull.T)
say(f"sign formula validated on {len(sample)} random pairs by direct evaluation")
# |K|^2 equals the double-coset lookup everywhere
beta = np.vectorize(lambda d: Kd_abs[int(d)] ** 2)(D).astype(np.int64)
assert np.array_equal(beta, Kfull.astype(np.int64) ** 2)
say("beta = K∘K agrees with the double-coset lookup at every pair")

# P2: rank K = f_{delta^4}
f_rect = C.hook_length_f((delta,) * 4)
rK = C.rank_both_primes(Kfull.tolist())
rK_Q = C.rank_Q(Kfull.tolist())
say(f"P2 rank K = {rK} over Q {rK_Q} (f_rect = {f_rect})")
assert rK == (f_rect, f_rect) and rK_Q == f_rect

# rank beta = rank Theta^+
rb = C.rank_both_primes(beta.tolist())
rb_Q = C.rank_Q(beta.tolist())
say(f"rank beta (= rank Theta^+) = {rb}, over Q {rb_Q}; |H| = {nH}")
assert rb[0] == rb[1] == rb_Q

# -------------------------------------------------- route (a): P_lambda in Hecke
blocks0 = [C.block_positions(m, N) for m in pi0]
perms4 = list(itertools.permutations(range(4)))
W = []
for sigma in itertools.permutations(range(delta)):
    for choice in itertools.product(perms4, repeat=delta):
        w = [0] * N
        for j in range(delta):
            src, dst = blocks0[j], blocks0[sigma[j]]
            for t in range(4):
                w[src[t]] = dst[choice[j][t]]
        W.append(tuple(w))
assert len(W) == 24 ** delta * factorial(delta)
say(f"|W| = {len(W)}")

classes = list(C.partitions(N))
class_id = {rho: i for i, rho in enumerate(classes)}
hist = np.zeros((nd, len(classes)), dtype=object)
for key in d_keys:
    d = d_index[key]
    g = C.coset_rep(reps[key], delta)
    assert C.apply_perm(g, pi0) == reps[key]
    for w in W:
        gw = tuple(g[w[i]] for i in range(N))
        hist[d, class_id[C.cycle_type(gw)]] += 1
say("coset cycle-type histograms done")

lams = list(C.partitions(N, maxlen=delta))
chi_table = {lam: [C.mn_char(lam, rho) for rho in classes] for lam in lams}
d_id = d_index[C.rel(pi0, pi0)]
results, sum_mf, sum_af = {}, 0, 0
Bm = {p: flint.nmod_mat(nH, nH, [int(v) % p for v in beta.ravel()], p) for p in (C.P1, C.P2)}
for lam in lams:
    f = C.hook_length_f(lam)
    a_house = ambient_multiplicity(lam, delta)
    coef = {}
    for d in range(nd):
        s = sum(int(hist[d, c]) * chi_table[lam][c] for c in range(len(classes)))
        coef[d] = Fraction(f * s, factorial(N))
    tr = nH * coef[d_id]
    assert tr.denominator == 1 and int(tr) % f == 0
    a_trace = int(tr) // f
    rec = {"lambda": list(lam), "f": f, "a_house": a_house, "a_trace": a_trace,
           "sk": C.sk_coefficient(lam, delta), "g": C.g_coefficient(lam, delta)}
    assert a_trace == a_house, (lam, a_trace, a_house)
    if a_house == 0:
        assert all(c == 0 for c in coef.values())
        rec["m"] = 0
        results[str(lam)] = rec
        continue
    mvals = []
    demo = len([k for k in results if results[k].get("m") is not None and results[k]["a_house"]]) < 2
    for p in (C.P1, C.P2):
        cm = [int(coef[d].numerator) % p * pow(int(coef[d].denominator), -1, p) % p for d in range(nd)]
        lut = np.array(cm, dtype=object)
        Pm = lut[D.astype(np.int64)]
        Pmat = flint.nmod_mat(nH, nH, [int(v) for v in Pm.ravel()], p)
        rP = Pmat.rank()
        assert rP == a_house * f, (lam, rP, a_house, f)
        if demo and p == C.P1:
            assert Pmat * Pmat == Pmat                 # idempotent (checked on the first cells)
        if rb[0] < nH or demo:
            rBP = (Bm[p] * Pmat).rank()
            assert rBP % f == 0
            mvals.append(rBP // f)
        else:
            # beta is invertible on H (rank |H| at both primes and over Q above), so
            # ker beta = 0 and rank(beta P_lambda) = rank(P_lambda) = a f exactly.
            mvals.append(rP // f)
    rec["m_by_product"] = bool(rb[0] < nH or demo)
    assert mvals[0] == mvals[1]
    rec["m"] = mvals[0]
    results[str(lam)] = rec
    sum_mf += mvals[0] * f
    sum_af += a_house * f
    say(f"lambda={lam} f={f} a={a_house} sk={rec['sk']} g={rec['g']} m={mvals[0]}")
say(f"sum a f = {sum_af} (|H| {nH}); sum m f = {sum_mf} (rank beta {rb[0]})")
assert sum_af == nH and sum_mf == rb[0]

# ----------------------------------------------- route (b): weight spaces on H
weights = list(C.partitions(N, maxlen=delta))
weights.sort(key=lambda mu: tuple(-x for x in mu))      # lex-decreasing: dominance-compatible
extra = [mu for mu in C.partitions(N) if len(mu) >= 4 and len(mu) <= 8 and mu not in weights]
extra = extra[:: max(1, len(extra) // 12)]               # a spread of Specht-check weights
wb = {}
for mu in weights + extra:
    colour = np.zeros(N, dtype=np.int64)
    pos = 0
    for c, m in enumerate(mu):
        colour[pos:pos + m] = c
        pos += m
    # orbit id: sorted tuple of block colour-content vectors (= the monomial)
    orbits = {}
    for i in range(nH):
        cv = []
        for j in range(delta):
            v = [0] * len(mu)
            for p in range(N):
                if labels[i, p] == j:
                    v[colour[p]] += 1
            cv.append(tuple(v))
        orbits.setdefault(tuple(sorted(cv)), []).append(i)
    olist = sorted(orbits)
    nb = len(olist)
    rep = [orbits[o][0] for o in olist]
    b = [[0] * nb for _ in range(nb)]
    kk = [[0] * nb for _ in range(nb)]
    for r, O in enumerate(olist):
        members = orbits[O]
        for c2 in range(nb):
            col = beta[members, rep[c2]]
            b[r][c2] = int(col.sum())
            kk[r][c2] = int(Kfull[members, rep[c2]].sum())
    for r in range(nb):
        for c2 in range(nb):
            assert b[r][c2] * len(orbits[olist[c2]]) == b[c2][r] * len(orbits[olist[r]])
    rb_mu = C.rank_both_primes(b)
    assert rb_mu[0] == rb_mu[1]
    rb_mu_Q = C.rank_Q(b)
    assert rb_mu_Q == rb_mu[0]
    # Kostka check on the colour-multilinear orbits (signed symmetrisation is the
    # plain orbit sum there; the others symmetrise to zero)
    multi = [r for r, O in enumerate(olist) if all(max(v) <= 1 for v in O)]
    kk_m = [[kk[r][c2] for c2 in multi] for r in multi]
    rk = C.rank_both_primes(kk_m) if multi else (0, 0)
    kost = C.kostka((delta,) * 4, mu)
    assert rk[0] == rk[1] == kost, (mu, rk, kost)
    wb[mu] = {"nb": nb, "r": rb_mu[0], "r_Q": rb_mu_Q, "multilinear_orbits": len(multi),
              "rank_k_multilinear": rk[0], "kostka_rect": kost}
    say(f"weight {mu}{' (Specht check only)' if mu in extra else ''}: nb={nb} r={rb_mu[0]} | multilinear {len(multi)} rank k={rk[0]} = Kostka {kost}")

Kmat_w, Kinv = C.inverse_kostka_matrix(weights)
route_b = {}
for i, lam in enumerate(weights):
    # nb_mu = sum_nu K_{nu mu} a_nu  =>  a_lam = sum_mu (K^{-1})_{mu lam} nb_mu  (transpose)
    m = sum(Kinv[j][i] * wb[weights[j]]["r"] for j in range(len(weights)))
    a = sum(Kinv[j][i] * wb[weights[j]]["nb"] for j in range(len(weights)))
    assert m.denominator == 1 and a.denominator == 1
    route_b[str(lam)] = {"m": int(m), "a": int(a)}
    ra = results[str(lam)]
    assert int(a) == ra["a_house"], (lam, a, ra)
    assert int(m) == ra["m"], (lam, m, ra)
say("P4: route (b) agrees with route (a) at every weight (m and a)")

out = {"delta": delta, "N": N, "H": nH, "double_cosets": nd,
       "K_abs_d": {str(d_keys[d]): Kd_abs[d] for d in range(nd)},
       "krow_values": sorted(set(krow)),
       "dsize": [int(x) for x in dsize],
       "rank_K": rK[0], "rank_K_Q": rK_Q, "f_rect": f_rect,
       "rank_beta": rb[0], "rank_beta_Q": rb_Q,
       "cells": results, "weights": {str(mu): wb[mu] for mu in weights}, "specht_check_weights": {str(mu): wb[mu] for mu in extra},
       "route_b": route_b, "log": log, "seconds": time.time() - t0}
with open(os.path.join(ROOT, "results", f"s56_hecke_d{delta}.json"), "w") as fh:
    json.dump(out, fh, indent=1, default=str)
np.save(os.path.join(ROOT, "results", "logs", f"s56_Kfull_d{delta}.npy"), Kfull)
say("written")
