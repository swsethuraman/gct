#!/usr/bin/env python3
"""Session 74 -- the certified statements at the goal cell, banked as minors and
residues (integrator instruction, 03:05 UTC: bank the determinant 273-minor
against LMR's bound; keep the padded 269 as a floor; retain the five padded
candidate relations; test whether the determinant kernel line separates true
padding with a certified nonzero value).

(a) MINORS.  For each prime and family: a column set on which the source rows
    have a nonzero maximal minor, with its determinant mod p.  det: 273 columns
    on the 273 transported delta=23 rows (rank T_det >= 273, and = 273 with
    LMR); pad: 269 columns on all 274 rows (rank T_pad >= 269, a floor).
    Sound over Q: the rows are integer polynomials at integer points, so a
    nonzero minor mod p is the reduction of a nonzero integer minor.

(b) THE LMR LINE, EXACTLY.  With rank_Q T_det = 273 exactly, ker T_det over Q
    is one line <y>, y a primitive integer vector on the 274-vector source;
    y is the LMR equation of weight (65,17,2^7) in I(Det_4), restricted to the
    9-pencil variety.  The mod-p point-evaluation matrix has nullity exactly 1,
    and y mod p lies in its kernel, so  y = c_p * k_p (mod p)  with k_p the
    computed kernel vector and c_p != 0.  Hence for any integer point f,
        y(f) = c_p * (k_p . row(f))  (mod p),
    and k_p . row(f) != 0 (mod p) CERTIFIES y(f) != 0 over Q -- no rational
    reconstruction is needed for that.  This script computes the residues
    k_p . row(f) at every padded (and, when banked, reducible / per_4 / generic)
    point at both primes: a nonzero residue at a padded point is a certificate
    that the LMR equation does not vanish on the true padded permanent, i.e.
    y in I(Det) \ I(Pad).

(c) THE FIVE PADDED CANDIDATES.  The mod-p kernel of the padded evaluation
    (dimension 5 at both primes) is retained as candidate relations; their
    values at the determinant points (must be nonzero somewhere, since
    U_P cap U_D = 0) are recorded.  No characteristic-zero membership is
    claimed for them.

Writes results/s74/certified.json.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from flint import nmod_mat                                            # noqa: E402
from wk8_s30_core import P1, P2                                       # noqa: E402
from wk11_s69_circuit import rank_mod                                 # noqa: E402
from wk12_s74_decide import assemble, load_col, left_kernel           # noqa: E402

OUT = os.environ.get("S74_OUT", os.path.join(ROOT, "results", "s74"))


def maximal_minor(rows, p):
    """greedy column selection to a nonzero rank(rows) x rank(rows) minor; returns
    (rank, row set, column set, det mod p)."""
    r = rank_mod(rows, p)
    cols = []
    for j in range(len(rows[0])):
        trial = cols + [j]
        if rank_mod([[row[c] for c in trial] for row in rows], p) == len(trial):
            cols = trial
            if len(cols) == r:
                break
    # rows: greedy too (rows may exceed rank)
    rsel = []
    for i in range(len(rows)):
        trial = rsel + [i]
        if rank_mod([[rows[t][c] for c in cols] for t in trial], p) == len(trial):
            rsel = trial
            if len(rsel) == r:
                break
    sub = [[rows[i][c] % p for c in cols] for i in rsel]
    d = int(nmod_mat(r, r, [x for row in sub for x in row], p).det())
    return r, rsel, cols, d


def main():
    src = json.load(open(os.path.join(OUT, "source.json"), encoding="utf-8"))
    out = dict(cell=src["cell"], row_system=src["row_system"], primes={})
    for p in (P1, P2):
        rec = {}
        det = load_col("det", p)
        pad = load_col("pad", p)
        if det is None or pad is None:
            continue
        rows23, idx23, K23 = assemble(src, det, p, 23)           # the transported delta=23 source at det points
        r, rs, cs, d = maximal_minor(rows23, p)
        rec["det_minor_delta23"] = dict(rank=r, rows=len(rows23), cols=K23, row_set=rs, col_set=cs, det_mod_p=d,
                                        point_index=[det["point_index"][c] for c in cs],
                                        statement="rank_Q T_det >= %d on the transported delta=23 source; with LMR (<= 273) "
                                                  "rank T_det = 273 exactly, i_det(23) = 0, i_det(24) = 1" % r)
        rows24, idx24, K24 = assemble(src, det, p, 24)
        rp, rsp, csp, dp_ = maximal_minor(assemble(src, pad, p, 24)[0], p)
        rec["pad_minor"] = dict(rank=rp, rows=274, cols=K24, row_set=rsp, col_set=csp, det_mod_p=dp_,
                                point_index=[pad["point_index"][c] for c in csp],
                                statement="rank_Q T_pad >= %d (a floor); the measured value %d at this prime is not a theorem" % (rp, rp))
        # (b) the LMR line
        kd = left_kernel(rows24, p)
        assert len(kd) == 1, "det kernel is not one-dimensional at this prime"
        k = kd[0]
        rows_pad, _, _ = assemble(src, pad, p, 24)
        res_pad = [sum(k[i] * rows_pad[i][j] for i in range(274)) % p for j in range(K24)]
        rec["lmr_line"] = dict(kernel_mod_p=k, coefficient_on_T57=k[273],
                               residues_at_padded_points=res_pad,
                               nonzero_padded_points=sum(1 for v in res_pad if v), K=K24,
                               statement="y = c_p k (mod p) for the LMR equation y; a nonzero residue certifies y(f) != 0 over Q "
                                         "at that integer padded point: the LMR equation does not vanish on the true padded permanent")
        for fam in ("red", "per4", "gen"):
            col = load_col(fam, p)
            if col is None or len(col["rows_native"]) < 274:
                continue
            rows_f, _, Kf = assemble(src, col, p, 24)
            res = [sum(k[i] * rows_f[i][j] for i in range(274)) % p for j in range(Kf)]
            rec["lmr_line"][f"residues_at_{fam}_points"] = res
            rec["lmr_line"][f"nonzero_{fam}_points"] = sum(1 for v in res if v)
        # (c) the five padded candidates
        kp = left_kernel(rows_pad, p)
        vals_det = [[sum(v[i] * rows24[i][j] for i in range(274)) % p for j in range(K24)] for v in kp]
        rec["padded_candidates"] = dict(dimension=len(kp), vectors_mod_p=kp,
                                        nonzero_det_points_per_vector=[sum(1 for x in row if x) for row in vals_det],
                                        statement="mod-p kernel of the padded evaluation, retained as candidate relations; "
                                                  "no characteristic-zero membership claimed")
        out["primes"][str(p)] = rec
        print(f"p={p}: det minor {r}x{r} det {d} (cols {len(cs)}); pad minor {rp}x{rp} det {dp_}; "
              f"LMR line: {rec['lmr_line']['nonzero_padded_points']}/{K24} padded points nonzero; "
              f"padded candidates {len(kp)} (nonzero det points per vector {rec['padded_candidates']['nonzero_det_points_per_vector']})",
              flush=True)
    json.dump(out, open(os.path.join(OUT, "certified.json"), "w", encoding="utf-8"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
