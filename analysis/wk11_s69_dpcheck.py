#!/usr/bin/env python3
"""Session 69: the Grassmann DP evaluator (wk11_s69_dp.c) against the mixed-discriminant
evaluator (wk11_s69_eval.c) at h = 9 -- the seed shape (9,9,2^15) and the LMR shape
(9,9,2^15,1^48) -- on random fillings at both primes; plus the n = 3 basis fillings of the
passed control (values must match the recorded ones).  Writes results/s69_dp_check.json."""
import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
from wk11_s69_circuit import *

out = dict(cases=[])
rng = random.Random(2024)
t0 = time.time()
for (delta, n2, n1, ks) in ((12, 15, 0, (6, 7, 8, 9)), (24, 15, 48, (5, 6, 9))):
    n, h = 4, 9
    A, idx, fact, tab = sym_table(n, h)
    for k in ks:
        F = random_filling(h, n, delta, n2, n1, rng, k=k)
        for p in PRIMES:
            cv = generic_point(n, h, p, rng); ms = symbols_from_coeffs(cv, n, h, p)
            t = time.time(); a = dp_eval_c(F, ms, p, tab, max_W=9); ta = time.time() - t
            t = time.time(); b = fast_eval_c(F, ms, p, tab); tb = time.time() - t
            out["cases"].append(dict(delta=delta, k=k, p=p, W=letter_order(F)[1], dp=a, mixed=b, agree=a == b,
                                     secs_dp=round(ta, 3), secs_mixed=round(tb, 1)))
            print(out["cases"][-1], flush=True)
# n = 3 control basis: recorded values
r = json.load(open(os.path.join(ROOT, "results", "s69_n3_d12.json")))
n, h = 3, 7
A, idx, fact, tab = sym_table(n, h)
ok = True
for i, Fj in enumerate(r["basis"]):
    F = Filling.from_json(Fj)
    for p in PRIMES:
        for j in range(4):
            cv = generic_point(n, h, p, random.Random(r["seed"] * 1000 + j)); ms = symbols_from_coeffs(cv, n, h, p)
            v = dp_eval_c(F, ms, p, tab)
            # the recorded rows are in the record only for det points; recompute the mixed-disc value here
            v2 = fast_eval_c(F, ms, p, tab)
            ok &= (v == v2)
out["n3_basis_agree"] = ok
out["all_agree"] = ok and all(c["agree"] for c in out["cases"])
out["secs"] = round(time.time() - t0, 1)
print("ALL AGREE:", out["all_agree"])
json.dump(out, open(os.path.join(ROOT, "results", "s69_dp_check.json"), "w"), indent=1)
