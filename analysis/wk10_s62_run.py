"""Session 62 — the block Gram matrices G_lambda = V^T B_lambda V on every constituent
of Sym^delta(Sym^n), the room-one Schur complements, the supports and the cost curve.

    python3 analysis/wk10_s62_run.py <n> <delta> [--kostka] [--no-snf] [--certs DIR]

--kostka   also builds B_mu on EVERY dominant weight mu (ell(mu) <= delta) and
           recovers m_lambda, a_lambda by inverse Kostka from the weight-space ranks
           (session 56's route (b)), as an independent check of rank_Q G_lambda.
Writes results/s62_run_n<n>_d<delta>.json (+ counts under results/logs/, not committed
when large) and, with --certs, gct-cert/1 `matrix` certificates for every G_lambda.
"""
import json
import os
import sys
import time
from fractions import Fraction
from math import factorial

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
import wk10_s62_gram as G                 # noqa: E402
import wk9_s56_core as C56                # noqa: E402
from pleth import ambient_multiplicity    # noqa: E402
from wk8_s30_core import exps, monomials  # noqa: E402

args = sys.argv[1:]
n = int(args[0])
delta = int(args[1])
KOSTKA = "--kostka" in args
SNF = "--no-snf" not in args
CERTS = args[args.index("--certs") + 1] if "--certs" in args else None
CACHE = args[args.index("--cache") + 1] if "--cache" in args else None
N = n * delta
P1, P2 = C56.P1, C56.P2
CACHED = None
if CACHE and os.path.exists(CACHE):
    _z = np.load(CACHE)
    CACHED = {k: _z[k] for k in _z.files}


def frac(x):
    return str(x) if isinstance(x, Fraction) else str(Fraction(x))


t_all = time.time()
t = time.time()
lab = G.enum_H(n, delta)
nH = lab.shape[0]
enum_s = time.time() - t
G.log(f"n={n} delta={delta} N={N} |H|={nH} enumerated in {enum_s:.1f}s")
t = time.time()
orb = G.Orbitals(n, delta)
orb_s = time.time() - t

# constituents and the bookkeeping identities (P6)
all_weights = [mu for mu in C56.partitions(N, maxlen=delta)]
a_of = {mu: ambient_multiplicity(mu, delta, n=n) for mu in all_weights}
constituents = [mu for mu in all_weights if a_of[mu] > 0]
sum_a2 = sum(a_of[mu] ** 2 for mu in constituents)
G.log(f"constituents {len(constituents)}, max a {max(a_of.values())}, sum a^2 = {sum_a2}, orbitals {orb.n_orb}")

out = {"n": n, "delta": delta, "N": N, "H": nH, "enum_s": round(enum_s, 2), "orbitals": orb.n_orb,
       "labelled_margin_matrices": orb.n_labelled, "orbitals_s": round(orb_s, 2),
       "K_by_orbital": {str(orb.keys[d]): orb.K[d] for d in range(orb.n_orb)},
       "constituents": len(constituents), "max_a": max(a_of.values()), "sum_a2": sum_a2,
       "sum_a2_equals_orbitals": sum_a2 == orb.n_orb,
       "mult2_constituents": [list(mu) for mu in constituents if a_of[mu] == 2],
       "cells": {}, "weights": {}}


def cell(lam):
    r = len(lam)
    rec = {"lambda": list(lam), "r": r, "a": a_of[lam]}
    t0 = time.time()
    wo = G.weight_orbits(lab, lam, n, r)
    rec["n_lam"] = wo["n_lam"]
    rec["orbit_sizes_min_max"] = [int(wo["size"].min()), int(wo["size"].max())]
    t1 = time.time()
    if CACHED is not None and str(lam) in CACHED:
        Ncount = CACHED[str(lam)]
        cost = {"total_s": 0.0, "per_rep_s": 0.0, "n_pass": wo["n_lam"], "H": nH, "cached": True}
        assert np.array_equal(Ncount.sum(axis=2), np.repeat(wo["size"][:, None], wo["n_lam"], axis=1))
    else:
        Ncount, cost = G.pair_counts(lab, wo, orb, verbose=(wo["n_lam"] > 100), tag=str(lam))
    rec["pass"] = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in cost.items()}
    rec["touched_orbitals_per_pair"] = G.n_touched(Ncount)
    t2 = time.time()
    B = G.B_from_counts(Ncount, wo["size"], orb.beta)
    rec["B_build_s"] = round(time.time() - t2, 2)
    t3 = time.time()
    basis, vecs = G.hwv_basis_Q(n, r, delta, lam)
    rec["hwv_s"] = round(time.time() - t3, 3)
    assert list(basis) == list(wo["monos"]), "monomial orders differ"
    assert len(vecs) == a_of[lam], ("kernel dimension != a", lam, len(vecs), a_of[lam])
    V = G.to_orbit_coords(wo["monos"], vecs)
    t4 = time.time()
    Gm = G.gram_block(V, B)
    rec["G_s"] = round(time.time() - t4, 3)
    rQ = G.rank_Q(Gm)
    rec["rank_Q_G"] = rQ
    rec["i_det"] = a_of[lam] - rQ
    rec["rank_mod_p_G_info_only"] = {str(P1): G.rank_mod(Gm, P1), str(P2): G.rank_mod(Gm, P2)}
    rec["G"] = [[str(x) for x in row] for row in Gm]
    rec["rank_Q_B"] = G.rank_Q(B)
    rec["B_full_rank"] = rec["rank_Q_B"] == wo["n_lam"]
    # supports
    supp_each = [sum(1 for x in v if x) for v in vecs]
    union = set()
    for v in vecs:
        union |= {k for k, x in enumerate(v) if x}
    rec["hwv_support_each"] = supp_each
    # |S|, the REDUCED-ROUTE deciding number (integrator note 3): the support of the HWVs
    # in the weight-space / orbit-sum basis -- how many monomials O the source vectors touch.
    # The reduced block A = C_S^T beta_S C_S is a quadratic form over these, cost ~ a|S|^2.
    rec["reduced_route_S"] = len(union)            # = |S|, orbit-basis support (<= n_lam = weight-space dim)
    rec["hwv_support_union"] = len(union)          # (kept: same quantity, old name)
    rec["S_over_n_lam"] = str(Fraction(len(union), wo["n_lam"]))
    # the ENUMERATION-route cost object: the raw number of block decompositions the HWVs touch,
    # = sum of orbit sizes over the support = |H| when the HWV is dense in the weight space.
    rec["enumeration_raw_S"] = G.foulkes_support(wo["size"], union)   # = Sum_{O in supp} |O|
    rec["H_total"] = int(sum(int(x) for x in wo["size"]))            # = |H_{n,delta}| (orbit sizes partition all of H)
    NS, ufree, NSp = G.u_free_count(n, r, delta, lam)
    rec["u_free_monomials"] = ufree
    rec["N_S_pred"] = NSp
    # centrality (integrator note 4): beta scalar on M_lambda iff G_lambda proportional to
    # N_lambda = V^T diag(|O|) V (the standard H inner product).  a >= 2 makes it a real test.
    if a_of[lam] >= 2:
        Nmat = G.gram_H(V, wo["size"])
        prop, c = G.proportional(Gm, Nmat)
        rec["centrality"] = {"N_lambda": [[str(x) for x in row] for row in Nmat],
                             "G_proportional_to_N": bool(prop),
                             "ratio": (str(c) if c is not None else None),
                             "central_block": bool(prop),
                             "note": "beta is scalar (central) on this multiplicity space iff proportional"}
        G.log(f"  centrality lambda={lam}: G proportional to N = {prop} -> block {'central (scalar)' if prop else 'NONCENTRAL'}")
    # SNF diagnostics
    if SNF:
        rec["snf_G"] = [str(x) for x in G.snf_diagonal(Gm)]
        if wo["n_lam"] <= 120:
            rec["snf_B"] = [str(x) for x in G.snf_diagonal(B)]
    # ladder: predecessor and Schur complement
    lam_pred = (lam[0] - n,) + tuple(lam[1:])
    valid_pred = lam_pred[0] >= (lam_pred[1] if r > 1 else 0) and delta >= 2
    if r > 1 and lam_pred[0] == 0:
        valid_pred = False
    if valid_pred:
        a_pred = ambient_multiplicity(lam_pred, delta - 1, n=n) if sum(lam_pred) == n * (delta - 1) else 0
        rec["pred"] = {"lambda": list(lam_pred), "a": a_pred}
        room = a_of[lam] - a_pred
        rec["room"] = room
        if a_pred > 0:
            pb, pv = G.hwv_basis_Q(n, r, delta - 1, lam_pred)
            assert len(pv) == a_pred
            T, new = G.transported_and_new(n, r, delta, lam, pb, pv, basis, vecs)
            TV = G.to_orbit_coords(wo["monos"], T)
            GA = G.gram_block(TV, B)
            rec["rank_Q_A"] = G.rank_Q(GA)
            rec["A_nonsingular"] = rec["rank_Q_A"] == a_pred
            if room == 1:
                full = TV + [G.to_orbit_coords(wo["monos"], [new])[0]]
                Gfull = G.gram_block(full, B)
                forms = G.schur_all_forms(Gfull)
                detA, s, detG = G.schur_complement(Gfull)
                rec["schur"] = {"det_A": frac(detA), "s": frac(s), "det_G": frac(detG), "s_zero": s == 0,
                                "born": s == 0,
                                "s_schur": frac(forms["s_schur"]), "s_detB_over_detA": frac(forms["s_detB_over_detA"]),
                                "s_distance": frac(forms["s_distance"]), "three_forms_agree": bool(forms["agree"]),
                                "detA_mod_p": {str(P1): G.detA_mod_p(Gfull, P1), str(P2): G.detA_mod_p(Gfull, P2)},
                                "A_nonsingular_mod_p_lower_bound": (G.detA_mod_p(Gfull, P1) != 0 and G.detA_mod_p(Gfull, P2) != 0)}
                assert forms["agree"], ("three Schur forms disagree", lam)
                nvec_ufree = sum(1 for k, x in enumerate(new) if x and G.exps(n, r).index((n,) + (0,) * (r - 1)) not in basis[k])
                rec["new_vector_u_free_support"] = nvec_ufree
                rec["new_vector_support"] = sum(1 for x in new if x)
                G.log(f"  room-one: a={a_of[lam]} a_pred={a_pred} det A={detA} s={s} (3 forms agree={forms['agree']}) -> {'BORN' if s == 0 else 'not born'}")
            elif room >= 2:
                # block Schur complement rank = rank G - rank A
                rec["schur_block"] = {"rank_G_minus_rank_A": rQ - rec["rank_Q_A"], "room": room}
            else:
                rec["schur"] = None
        elif a_of[lam] == 1:
            # room one with an empty predecessor: A is 0 x 0 and s = c = G itself
            s = Fraction(int(Gm[0][0]))
            rec["schur"] = {"det_A": "1", "s": frac(s), "det_G": frac(s), "s_zero": s == 0, "born": s == 0,
                            "empty_predecessor": True}
            rec["new_vector_support"] = sum(1 for x in vecs[0] if x)
            rec["new_vector_u_free_support"] = sum(1 for k, x in enumerate(vecs[0]) if x and G.exps(n, r).index((n,) + (0,) * (r - 1)) not in basis[k])
    else:
        rec["pred"] = None
        rec["room"] = a_of[lam]
    rec["cell_s"] = round(time.time() - t0, 2)
    rec["H_times_nlam"] = nH * wo["n_lam"]
    G.log(f"lambda={lam} a={a_of[lam]} n_lam={wo['n_lam']} rank_Q G={rQ} i_det={rec['i_det']} "
          f"B full rank={rec['B_full_rank']} pass {cost['total_s']:.1f}s ({cost['per_rep_s']:.3f}s/rep) "
          f"room={rec.get('room')} ({rec['cell_s']:.1f}s)")
    return rec, Ncount, B, wo


os.makedirs(os.path.join(ROOT, "results", "logs"), exist_ok=True)
counts_store = {}
weight_rank = {}
for lam in constituents:
    rec, Ncount, B, wo = cell(lam)
    out["cells"][str(lam)] = rec
    counts_store[str(lam)] = Ncount
    weight_rank[lam] = (rec["rank_Q_B"], wo["n_lam"])
    with open(os.path.join(ROOT, "results", f"s62_run_n{n}_d{delta}.json"), "w") as fh:
        json.dump(out, fh, indent=1)

if KOSTKA:
    # route (b): every dominant weight, ranks of B_mu, inverse Kostka
    for mu in all_weights:
        if mu in weight_rank:
            continue
        r = len(mu)
        wo = G.weight_orbits(lab, mu, n, r)
        Ncount, cost = G.pair_counts(lab, wo, orb, verbose=False)
        B = G.B_from_counts(Ncount, wo["size"], orb.beta)
        rk = G.rank_Q(B)
        weight_rank[mu] = (rk, wo["n_lam"])
        G.log(f"weight {mu}: nb={wo['n_lam']} rank_Q B={rk} ({cost['total_s']:.1f}s)")
    weights = sorted(all_weights, key=lambda mu: tuple(-x for x in mu))
    Kmat, Kinv = C56.inverse_kostka_matrix(weights)
    routeb = {}
    agree = True
    for i, lam in enumerate(weights):
        m = sum(Kinv[j][i] * weight_rank[weights[j]][0] for j in range(len(weights)))
        a = sum(Kinv[j][i] * weight_rank[weights[j]][1] for j in range(len(weights)))
        assert m.denominator == 1 and a.denominator == 1
        m, a = int(m), int(a)
        assert a == a_of[lam], (lam, a, a_of[lam])
        entry = {"m_routeb": m, "a_routeb": a}
        if lam in [tuple(c) for c in constituents]:
            rG = out["cells"][str(lam)]["rank_Q_G"]
            entry["rank_Q_G"] = rG
            entry["agree"] = (rG == m)
            agree &= (rG == m)
        else:
            assert m == 0
        routeb[str(lam)] = entry
    out["route_b"] = routeb
    out["route_b_agrees_everywhere"] = agree
    out["weights"] = {str(mu): {"nb": weight_rank[mu][1], "rank_Q_B": weight_rank[mu][0]} for mu in weights}
    G.log(f"route (b) inverse Kostka: agrees with rank_Q G at every constituent: {agree}")

out["total_s"] = round(time.time() - t_all, 1)
out["sum_nlam_constituents"] = sum(out["cells"][str(l)]["n_lam"] for l in constituents)
with open(os.path.join(ROOT, "results", f"s62_run_n{n}_d{delta}.json"), "w") as fh:
    json.dump(out, fh, indent=1)
np.savez_compressed(os.path.join(ROOT, "results", "logs", f"s62_counts_n{n}_d{delta}.npz"), **counts_store)

if CERTS:
    os.makedirs(CERTS, exist_ok=True)
    for lam in constituents:
        rec = out["cells"][str(lam)]
        Gm = [[int(x) for x in row] for row in rec["G"]]
        a = rec["a"]
        rQ = rec["rank_Q_G"]
        cert = {"format": "gct-cert/1", "kind": "matrix",
                "title": f"G_lambda = V^T B_lambda V for lambda={tuple(lam)}, n={n}, delta={delta}: rank over Q {rQ} of a={a} (mult_det = {rQ}, i_det = {a - rQ})",
                "produced_by": "analysis/wk10_s62_run.py (session 62)",
                "matrix": Gm, "claimed_rank_Q": rQ,
                "claimed_ranks_mod_p": {str(P1): rec["rank_mod_p_G_info_only"][str(P1)],
                                        str(P2): rec["rank_mod_p_G_info_only"][str(P2)]}}
        if rQ == a:
            cert["nonvanishing_minor"] = {"rows": list(range(a)), "cols": list(range(a))}
        notes = (f"Foulkes Gram (beta = K∘K) on the highest-weight space of weight {tuple(lam)} in Sym^{delta}(Sym^{n} C^{len(lam)}); "
                 f"rows/cols = the exact integer highest-weight basis of wk8_s30_core.build_R carried to H^(S_lambda) by v_O = h_O * prod mult_k(O)!. "
                 f"rank over Q is the multiplicity; the mod-p ranks are recorded for the verifier's protocol only and are NOT used as multiplicities (rank(Theta*Theta) = rank Theta holds in characteristic zero only).")
        if rec.get("schur"):
            notes += (f" Room-one cell: predecessor {tuple(rec['pred']['lambda'])} at delta-1 with a={rec['pred']['a']}; in the ladder basis "
                      f"(transported, then the new vector) det A = {rec['schur']['det_A']}, s = {rec['schur']['s']}, det G = {rec['schur']['det_G']}.")
        cert["notes"] = notes
        fn = os.path.join(CERTS, f"s62_G_n{n}_d{delta}_" + "_".join(map(str, lam)) + ".json")
        with open(fn, "w") as fh:
            json.dump(cert, fh)
    G.log(f"certificates written to {CERTS}")
G.log("done")
