#!/usr/bin/env python3
"""Session 69, regime R0: the three evaluators of the bracket monomial agree.

brute_force_eval (the Leibniz sum, the definition) vs fast_eval_py (Identity 3 with
flint determinants) vs fast_eval_c (the same in C), on random column-strict fillings
of small two-tall-column shapes, at random generic points, both house primes.  Also
checks that a filling with a letter in both rows of a 2-column is rejected and that
F_T changes sign when two rows of a tall column are swapped (column antisymmetry).

    python3 analysis/wk11_s69_r0.py      -> results/s69_r0.json
"""
import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk11_s69_circuit import (Filling, random_filling, sym_table, symbols_from_coeffs,
                              generic_point, brute_force_eval, fast_eval_py, fast_eval_c, PRIMES)

SHAPES = [  # (n, h, delta, n2, n1)
    (2, 3, 3, 0, 0), (2, 3, 4, 0, 2), (2, 3, 4, 1, 0),
    (3, 3, 3, 0, 3), (3, 3, 3, 1, 1), (3, 4, 4, 0, 4), (3, 4, 4, 1, 2), (3, 4, 4, 2, 0),
    (4, 3, 3, 0, 6), (4, 3, 3, 1, 4), (4, 3, 3, 2, 2), (4, 3, 3, 3, 0),
    (4, 4, 4, 0, 8), (4, 4, 4, 1, 6), (4, 4, 4, 2, 4), (4, 4, 4, 3, 2), (4, 4, 4, 4, 0),
    (3, 5, 5, 2, 1), (4, 5, 5, 3, 4),
]

def main():
    rng = random.Random(69)
    out = []; t0 = time.time()
    n_cases = 0; n_nonzero = 0
    for (n, h, d, n2, n1) in SHAPES:
        A, idx, fact, tab = sym_table(n, h)
        for rep in range(4):
            F = random_filling(h, n, d, n2, n1, rng)
            for p in PRIMES:
                cv = generic_point(n, h, p, rng)
                ms = symbols_from_coeffs(cv, n, h, p)
                b = brute_force_eval(F, ms, p, tab)
                f1 = fast_eval_py(F, ms, p, tab)
                f2 = fast_eval_c(F, ms, p, tab)
                ok = (b == f1 == f2)
                n_cases += 1; n_nonzero += (b != 0)
                out.append(dict(n=n, h=h, delta=d, n2=n2, n1=n1, p=p, filling=F.to_json(),
                                brute=b, fast_py=f1, fast_c=f2, agree=ok, shared=len(F.shared)))
                if not ok:
                    print("DISAGREE", n, h, d, n2, n1, p, F.to_json(), b, f1, f2, flush=True)
        # column antisymmetry: swap two rows of C1 -> sign flips (checked with the C evaluator)
        F = random_filling(h, n, d, n2, n1, rng)
        C1 = list(F.C1); C1[0], C1[1] = C1[1], C1[0]
        G = Filling(h, n, d, C1, F.C2, F.two, F.one)
        p = PRIMES[0]; cv = generic_point(n, h, p, rng); ms = symbols_from_coeffs(cv, n, h, p)
        a1, a2 = fast_eval_c(F, ms, p, tab), fast_eval_c(G, ms, p, tab)
        out.append(dict(check="antisymmetry", n=n, h=h, delta=d, n2=n2, n1=n1, p=p,
                        val=a1, swapped=a2, ok=(a1 + a2) % p == 0))
        assert (a1 + a2) % p == 0, "column antisymmetry failed"
        print(f"shape n={n} h={h} d={d} n2={n2} n1={n1}: 8 cases ok, antisymmetry ok  [{time.time()-t0:.1f}s]", flush=True)
    # rejection of a letter twice in a 2-column
    try:
        Filling(3, 2, 3, [0, 1, 2], [0, 1, 2], [], []); rej1 = True
    except AssertionError:
        rej1 = False
    try:
        Filling(3, 3, 3, [0, 1, 2], [0, 1, 2], [(0, 0)], [1, 2]); rej2 = False   # letter 0 twice in a 2-col
    except AssertionError:
        rej2 = True
    agree = all(r.get("agree", True) for r in out)
    summary = dict(cases=n_cases, nonzero=n_nonzero, all_agree=agree, rejects_repeated_letter=rej2,
                   valid_no_twocol=rej1, secs=round(time.time() - t0, 1))
    print(summary)
    with open(os.path.join(ROOT, "results", "s69_r0.json"), "w") as fh:
        json.dump(dict(summary=summary, cases=out), fh, indent=1)
    assert agree

if __name__ == "__main__":
    main()
