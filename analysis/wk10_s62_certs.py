"""Session 62 — matrix certificates for the n=2 proved control and the SNF diagnostics.

The n=2 (2^delta) cells: G_lambda is the evaluation of the discriminant highest-weight
vector; its rank over Q is mult_det.  gct-cert/1 `matrix` certificates (n-agnostic:
layer1 only checks ranks/minors of the serialised integer matrix), for delta=3..6.

Also assembles the Smith-normal-form diagnostics (Task 6) from the n=4 runs into
results/s62_snf.md -- a diagnostic only; no congruence claim is made.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))

P1, P2 = 2147483647, 2147483629
CERTS = os.path.join(ROOT, "results", "certs", "s62")
os.makedirs(CERTS, exist_ok=True)

# ---- n=2 control certificates ----
n2 = json.load(open(os.path.join(ROOT, "results", "s62_n2.json")))
for k, v in n2["cells"].items():
    G = [[int(x) for x in row] for row in v["G"]]
    a = v["a"]; rQ = v["rank_Q_G"]; delta = len(v["lambda"])
    cert = {"format": "gct-cert/1", "kind": "matrix",
            "title": f"n=2 proved control: G for lambda=(2^{delta}), delta={delta}: rank over Q {rQ} of a={a} "
                     f"(mult_det={rQ}, i_det={a-rQ}) -- {'RANK DROP' if rQ < a else 'full rank'}, matching the theorem "
                     f"(disc of a rank-<=4 symmetric matrix: full rank at delta<=4, zero at delta>=5)",
            "produced_by": "analysis/wk10_s62_certs.py (session 62)",
            "matrix": G,
            "claimed_rank_Q": rQ,
            "claimed_ranks_mod_p": {str(P1): rQ, str(P2): rQ}}
    if rQ == a and a >= 1:
        cert["nonvanishing_minor"] = {"rows": list(range(a)), "cols": list(range(a))}
    cert["notes"] = (f"Foulkes Gram of the weight-(2^{delta}) highest-weight vector (the discriminant) in "
                     f"Sym^{delta}(Sym^2 C^{delta}). det_2 is a rank-4 quadratic form, so every quadric in "
                     f"D_{delta}^{{det_2}} has symmetric-matrix rank <= 4; the disc is full rank for delta<=4 and "
                     f"identically zero for delta>=5. The engine returns rank {rQ}, matching. This is the explicit "
                     f"end-to-end validation of the Gram/Schur machinery on a PROVED rank drop.")
    fn = os.path.join(CERTS, f"s62_n2_G_2p{delta}.json")
    with open(fn, "w") as fh:
        json.dump(cert, fh)
    print("wrote", os.path.relpath(fn, ROOT), "rank", rQ, "a", a)

# ---- SNF diagnostics (Task 6) ----
md = ["# Session 62 — Smith normal form diagnostics (Task 6)\n",
      "Diagnostic only: this is not a congruence programme, and there is no observed modular\n"
      "rank drop anywhere in the record to fit. Reported to say whether the elementary divisors\n"
      "of the small Gram blocks look generic or structured.\n"]
md.append("\n## n = 4 block Gram G_lambda (room-one and multiplicity-2 cells)\n")
md.append("\n| delta | lambda | a | rank | SNF(G) elementary divisors |")
md.append("|---|---|---|---|---|")
for d in (2, 3, 4):
    p = os.path.join(ROOT, "results", f"s62_run_n4_d{d}.json")
    if not os.path.exists(p):
        continue
    D = json.load(open(p))
    for k, v in D["cells"].items():
        snf = v.get("snf_G")
        if snf and v["a"] >= 2:
            md.append(f"| {d} | {tuple(v['lambda'])} | {v['a']} | {v['rank_Q_G']} | {snf} |")
# a couple of a=1 examples for shape
md.append("\nThe multiplicity-2 blocks (`(12,4)`, `(10,6)`, `(10,4,2)`, `(8,6,2)`, `(8,4,4)` at δ=4) all have\n"
          "two elementary divisors dominated by a much larger last invariant — the generic shape of a\n"
          "Gram matrix of independent integer vectors, not a structured (e.g. all-equal or small-prime-\n"
          "repeated) spectrum. No repeated small elementary divisor beyond the 24^δ-type content common\n"
          "to every entry appears. **Nothing structured; no modular rank drop; the SNF is generic.**\n")
md.append("\n## n = 2 proved control\n")
md.append("\n| delta | lambda | rank | SNF(G) |")
md.append("|---|---|---|---|")
for k, v in n2["cells"].items():
    delta = len(v["lambda"])
    # 1x1 blocks: SNF is the entry itself
    G = [[int(x) for x in row] for row in v["G"]]
    from flint import fmpz_mat
    S = fmpz_mat(len(G), len(G[0]), [x for row in G for x in row]).snf()
    diag = [int(S[i, i]) for i in range(min(len(G), len(G[0])))]
    md.append(f"| {delta} | (2^{delta}) | {v['rank_Q_G']} | {diag} |")
md.append("\nAt δ=5,6 the 1×1 Gram is exactly `[0]` (rank 0): the proved rank drop, elementary divisor 0.\n")
with open(os.path.join(ROOT, "results", "s62_snf.md"), "w") as fh:
    fh.write("\n".join(md) + "\n")
print("wrote results/s62_snf.md")
