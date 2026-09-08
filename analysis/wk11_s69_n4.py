#!/usr/bin/env python3
"""Session 69, regimes R3/R4: the n = 4 LMR ladder bottom  ((17,17,2^7), 12), a = 2, det_4, r = 9,
by the compact circuit -- no coordinates anywhere.

  * fillings of lambda' = (9, 9, 2^15): two 9-columns, fifteen 2-columns, no 1-columns;
    every filling has k >= 6 letters shared by the two tall columns (12 letters, 18 tall slots);
  * sample fillings, evaluate at generic points (the Grassmann DP evaluator, wk11_s69_dp.c), greedy independent
    set until the generic rank reaches a = 2;
  * evaluate the basis at det_4 pencils at both primes: rank = mult_det, kernel = U_D (if any);
  * record every evaluation value at the committed points (seeds in the record) so that a
    coordinate-side vector can be compared with the circuit without any conversion;
  * R4: one LMR-shape filling (delta = 24, n1 = 48) at one point, timing only.

    python3 analysis/wk11_s69_n4.py [--kgen 12] [--kdet 12] [--extra 20] [--lmr]
"""
import argparse, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                              # noqa: E402
from wk9_s42_census import a_weyl                                            # noqa: E402
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs, generic_point,
                              det_point, fast_eval_c, dp_eval_c, letter_order, rank_mod, left_kernel_mod, PRIMES)   # noqa: E402

EVAL = dp_eval_c          # the Grassmann DP evaluator (validated against fast_eval_c, results/s69_dp_check.json)

N_DEG, R, H = 4, 9, 9
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kgen", type=int, default=12)
    ap.add_argument("--kdet", type=int, default=12)
    ap.add_argument("--extra", type=int, default=20, help="nonzero fillings beyond a to keep sampling for")
    ap.add_argument("--maxsamples", type=int, default=400)
    ap.add_argument("--kset", default="6,7,8,9")
    ap.add_argument("--seed", type=int, default=69)
    ap.add_argument("--lmr", action="store_true", help="R4 timing only")
    ap.add_argument("--out", default="s69_n4_seed.json")
    args = ap.parse_args()
    A, idx, fact, tab = sym_table(N_DEG, R)

    if args.lmr:
        # R4: the LMR shape (65,17,2^7): h = 9, delta = 24, n2 = 15, n1 = 48 -- one filling, one point
        rng = random.Random(args.seed)
        F = random_filling(H, N_DEG, 24, 15, 48, rng, k=6)
        cv = generic_point(N_DEG, R, P1, random.Random(1))
        ms = symbols_from_coeffs(cv, N_DEG, R, P1)
        t = time.time(); val = EVAL(F, ms, P1, tab); secs = time.time() - t
        t = time.time(); val2 = fast_eval_c(F, ms, P1, tab); secs2 = time.time() - t
        assert val == val2, "the two evaluators disagree at the LMR shape"
        rec = dict(shape="LMR (65,17,2^7) delta=24", filling=F.to_json(), shared=len(F.shared), value_nonzero=val != 0,
                   secs_dp=round(secs, 2), secs_mixed_disc=round(secs2, 2), W=letter_order(F)[1], dets_mixed_disc=2 ** 15 * 2 ** 9)
        log(f"LMR-shape evaluation: {secs:.1f}s, value {'nonzero' if val else 'ZERO'}, k={len(F.shared)}")
        json.dump(rec, open(os.path.join(ROOT, "results", "s69_n4_lmr_timing.json"), "w"), indent=1)
        return

    delta, n2, n1 = 12, 15, 0
    lam = (17, 17, 2, 2, 2, 2, 2, 2, 2)
    a = a_weyl(lam, delta, N_DEG, {})
    kset = [int(x) for x in args.kset.split(",")]
    log(f"cell {lam} delta={delta}: a={a}; fillings of lambda'=(9,9,2^15); kset={kset}")
    rec = dict(lam=list(lam), delta=delta, n=N_DEG, r=R, a=a, n2=n2, n1=n1, kset=kset, seed=args.seed,
               kgen=args.kgen, kdet=args.kdet, generic_seed_rule="random.Random(seed*1000+i) per point, uniform mod p",
               det_seed_rule="random.Random(11), det_point(4, 9, rng, bound=30) sequentially", det_bound=30)
    gen_pts = {p: [generic_point(N_DEG, R, p, random.Random(args.seed * 1000 + i)) for i in range(args.kgen)] for p in PRIMES}
    det_rng = random.Random(11)
    det_pts, det_As = [], []
    for _ in range(args.kdet):
        cv, As = det_point(N_DEG, R, det_rng, bound=30); det_pts.append(cv); det_As.append(As)
    msym_gen = {p: [symbols_from_coeffs(cv, N_DEG, R, p) for cv in gen_pts[p]] for p in PRIMES}
    msym_det = {p: [symbols_from_coeffs(cv, N_DEG, R, p) for cv in det_pts] for p in PRIMES}
    rec["det_pencils_A"] = det_As          # the integer matrices, so the points are reproducible exactly

    rng = random.Random(args.seed)
    basis, basis_rows, nonzero = [], [], []
    samples = 0; t_eval = 0.0; n_eval = 0; hist = []
    while samples < args.maxsamples and (len(basis) < a or len(nonzero) < a + args.extra):
        kk = rng.choice(kset)
        F = random_filling(H, N_DEG, delta, n2, n1, rng, k=kk)
        samples += 1
        t = time.time()
        # first point alone decides zero-ness cheaply
        v0 = EVAL(F, msym_gen[P1][0], P1, tab)
        t_eval += time.time() - t; n_eval += 1
        if v0 == 0:
            hist.append((samples, "zero", len(F.shared)))
            continue
        t = time.time()
        row = [v0] + [EVAL(F, ms, P1, tab) for ms in msym_gen[P1][1:]]
        t_eval += time.time() - t; n_eval += len(row) - 1
        nonzero.append((F, row))
        r_new = rank_mod(basis_rows + [row], P1)
        if r_new > len(basis):
            basis.append(F); basis_rows.append(row); hist.append((samples, "new", len(F.shared)))
            log(f"  sample {samples}: k={len(F.shared)} rank -> {r_new}  ({t_eval/n_eval:.1f}s per evaluation)")
        else:
            hist.append((samples, "dep", len(F.shared)))
        rec.update(samples=samples, basis=[F.to_json() for F in basis], basis_rows_P1=basis_rows,
                   nonzero_fillings=[F.to_json() for F, _ in nonzero], nonzero_rows_P1=[r for _, r in nonzero],
                   sample_history=hist, eval_secs=round(t_eval / max(n_eval, 1), 3))
        if samples % 20 == 0: json.dump(rec, open(os.path.join(ROOT, "results", args.out), "w"), indent=1)   # bank as we go
    rec["generic_rank_P1"] = len(basis)
    if len(basis) < a:
        rec["status"] = "SPANNING_FAILED"; json.dump(rec, open(os.path.join(ROOT, "results", args.out), "w"), indent=1); return
    # the extra nonzero fillings: all must be in the span (rank of all nonzero rows = a)
    rec["all_nonzero_rank_P1"] = rank_mod([r for _, r in nonzero], P1)
    # both primes, generic and det, on the basis
    rows_gen = {str(P1): basis_rows}
    rows_gen[str(P2)] = [[EVAL(F, ms, P2, tab) for ms in msym_gen[P2]] for F in basis]
    rec["generic_rank"] = {p: rank_mod(rows_gen[p], int(p)) for p in rows_gen}
    log(f"  generic ranks {rec['generic_rank']}")
    rows_det = {}
    for p in PRIMES:
        rows_det[str(p)] = [[EVAL(F, ms, p, tab) for ms in msym_det[p]] for F in basis]
        log(f"  det rows done at p={p}")
    rec["rows_generic"] = rows_gen; rec["rows_det"] = rows_det
    rec["det_rank"] = {p: rank_mod(rows_det[p], int(p)) for p in rows_det}
    rec["mult_det"] = rec["det_rank"]
    rec["i_det"] = {p: a - rec["det_rank"][p] for p in rows_det}
    rec["kernel"] = {p: left_kernel_mod(rows_det[p], int(p)) for p in rows_det}
    rec["status"] = "OK"
    log(f"  det ranks {rec['det_rank']} -> i_det {rec['i_det']}; kernels {rec['kernel']}")
    json.dump(rec, open(os.path.join(ROOT, "results", args.out), "w"), indent=1)
    log("done")


if __name__ == "__main__":
    main()
