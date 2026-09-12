#!/usr/bin/env python3
"""B14-01 -- confirm the members at both house primes, check each one
independently, and extract a nonzero h x h minor.

Per-member independent checks (the board asks for "every input definition saved
and independently checked"):
  M1  letter-order variation: the DP is re-run with a DIFFERENT processing order
      of the letters.  The slot allocation, the open/close sign bookkeeping and
      the rho_sign correction all change; the value must not.
  M2  torus weight: F(f(t.x)) == prod t_i^{lam_i} * F(f).
  M3  raising: invariant under the strictly-triangular substitution in the
      highest-weight direction and NOT in the other.
  M4  forced zero: every member vanishes at a point of span < l(lambda) = 9.
  M5  a pure-Python DP with a completely different state encoding (dicts keyed by
      the actual row sets, no ranked masks, no C) agrees at the real shape, on a
      sample -- an independent check of the C core's indexing, not only of small
      shapes.
"""
import argparse, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from b14_01_mixed import (MixedFilling, mixed_eval_c, rank_mod, letter_tensors_mixed,
                          letter_order_mixed, cached_order_mixed, msym_linear, msym_cubic)
from b14_01_controls import (subst_linear, subst_cubic, scale_linear, scale_cubic,
                             rand_point, ms_of)
from b14_01_run import load_points, msyms, CFG
from wk8_s30_core import P1, P2
from flint import nmod_mat


# ------------------------------------------------------------------ M5: independent pure-Python DP
def py_dp_eval(F, msym_by_val, p, r=None, order=None):
    """A second implementation of the same Leibniz sum with a DIFFERENT state
    encoding: states are (frozenset of used C1 rows, frozenset of used C2 rows,
    tuple of open-2-column assignments).  No ranked masks, no popcount ranking,
    no C.  Signs are computed from the actual row sets."""
    h = F.h
    r = r or h
    LT = letter_tensors_mixed(F, msym_by_val, p, r)
    if order is None:
        # a low-width order found independently of cached_order_mixed (different rng
        # seed, different restarts), so the processing order, the slot allocation and
        # the sign bookkeeping all differ from the C path.  The naive order
        # list(range(d)) is mathematically fine but its open-2-column width is large
        # enough to exhaust memory at h = 9 -- measured, not assumed.
        order, _W = letter_order_mixed(F, random.Random(987654), restarts=120)
    # which letter closes each 2-column edge, in this order
    pos = {l: t for t, l in enumerate(order)}
    first_letter = {}
    for e, (a, b) in enumerate(F.two):
        first_letter[e] = a if pos[a] < pos[b] else b
    states = {(frozenset(), frozenset(), ()): 1}
    for l in order:
        inC1, inC2, edges, T = LT[l]
        new = {}
        for (m1, m2, opens), val in states.items():
            od = dict(opens)
            # legs of this letter on 2-columns: opening ones branch, closing ones are determined
            opening = [(e, sd) for e, sd in edges if first_letter[e] == l]
            closing = [(e, sd) for e, sd in edges if first_letter[e] != l]
            for br in range(1 << len(opening)):
                bits = 0; od2 = dict(od); sgn2 = 0; ok = True
                for q, (e, sd) in enumerate(edges):
                    if first_letter[e] == l:
                        x = (br >> [ee for ee, _ in opening].index(e)) & 1
                        bits |= x << q
                        od2[e] = (x, sd)
                        if sd == 0: sgn2 ^= x            # this letter sits in row 0
                    else:
                        if e not in od2: ok = False; break
                        xo, sdo = od2.pop(e)
                        mine = 1 - xo
                        bits |= mine << q
                        if sd == 0: sgn2 ^= mine
                if not ok: continue
                ris = [i for i in range(h) if i not in m1] if inC1 else [None]
                rjs = [j for j in range(h) if j not in m2] if inC2 else [None]
                for i in ris:
                    s1 = sum(1 for x in m1 if x > i) % 2 if i is not None else 0
                    for j in rjs:
                        s2 = sum(1 for x in m2 if x > j) % 2 if j is not None else 0
                        tv = T[(i, j, bits)]
                        if not tv: continue
                        term = val * tv % p
                        if (sgn2 ^ s1 ^ s2) & 1: term = (-term) % p
                        k = (m1 | {i} if i is not None else m1,
                             m2 | {j} if j is not None else m2,
                             tuple(sorted(od2.items())))
                        k = (frozenset(k[0]), frozenset(k[1]), k[2])
                        new[k] = (new.get(k, 0) + term) % p
        states = new
    full = (frozenset(range(h)), frozenset(range(h)), ())
    tot = states.get(full, 0)
    # the DP built the rows in letter order; convert to the columns' own row order
    def rho(col):
        rows = [col.index(l) for l in order if l in col]
        s = 1
        for x in range(len(rows)):
            for y in range(x + 1, len(rows)):
                if rows[x] > rows[y]: s = -s
        return s
    return rho(F.C1) * rho(F.C2) * tot % p


def pivot_columns(mat, p):
    """columns of a nonsingular maximal minor, by elimination with column pivoting."""
    nr = len(mat); nc = len(mat[0])
    A = [[int(x) % p for x in row] for row in mat]
    piv = []
    rr = 0
    for c in range(nc):
        if rr >= nr: break
        r0 = next((i for i in range(rr, nr) if A[i][c]), None)
        if r0 is None: continue
        A[rr], A[r0] = A[r0], A[rr]
        inv = pow(A[rr][c], -1, p)
        A[rr] = [x * inv % p for x in A[rr]]
        for i in range(nr):
            if i != rr and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][k] - f * A[rr][k]) % p for k in range(nc)]
        piv.append(c); rr += 1
    return piv


def det_mod(mat, cols, p):
    k = len(cols)
    M = nmod_mat(k, k, [int(mat[i][c]) % p for i in range(k) for c in cols], p)
    return int(M.det())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=13)
    ap.add_argument("--members", default=None)
    ap.add_argument("--m5-sample", type=int, default=3)
    ap.add_argument("--seed", type=int, default=140199)
    a = ap.parse_args()
    C = CFG[a.degree]
    h, n2, n1, delta, r, DIM = C["h"], C["n2"], C["n1"], C["delta"], C["r"], C["dim"]
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    src = a.members or os.path.join(ROOT, "results", "b14_01", f"members_d{delta}.json")
    D = json.load(open(src))
    Fs = [MixedFilling.from_json(m["filling"]) for m in D["members"]]
    rng = random.Random(a.seed)
    t0 = time.time()

    meta, prim = load_points(C["pts"], "primary")
    _, hold = load_points(C["pts"], "holdout")
    out = dict(degree=delta, lam=list(lam), n_members=len(Fs),
               target_dim_adopted=DIM,
               source_file=os.path.relpath(src, ROOT),
               point_file=f"results/b14_prep/points/{C['pts']}",
               point_blob_contract=True)

    # ---- rows at both primes, primary points
    rows = {}
    for p in (P1, P2):
        MS = msyms(prim, r, p)
        rows[p] = [[mixed_eval_c(F, ms, p, r=r) for ms in MS] for F in Fs]
    rk = {p: rank_mod(rows[p], p) for p in (P1, P2)}
    out["rank_primary"] = {str(p): rk[p] for p in (P1, P2)}
    out["rank_agrees_between_primes"] = (rk[P1] == rk[P2])

    # ---- holdout (C6): unused in the search
    MSh = {p: msyms(hold, r, p) for p in (P1, P2)}
    rows_h = {p: [[mixed_eval_c(F, ms, p, r=r) for ms in MSh[p]] for F in Fs] for p in (P1, P2)}
    allrows = {p: [rows[p][i] + rows_h[p][i] for i in range(len(Fs))] for p in (P1, P2)}
    out["rank_all_points"] = {str(p): rank_mod(allrows[p], p) for p in (P1, P2)}
    out["C6_holdout_does_not_raise_rank"] = all(
        rank_mod(allrows[p], p) == rk[p] for p in (P1, P2))
    out["C7_rank_within_adopted_dim"] = all(rk[p] <= DIM for p in (P1, P2))

    # ---- the minor
    cert = None
    if rk[P1] == rk[P2] and rk[P1] >= 1:
        k = rk[P1]
        cols = pivot_columns(rows[P1], P1)
        d1 = det_mod(rows[P1], cols, P1)
        d2 = det_mod(rows[P2], cols, P2)
        if d2 == 0:                                  # re-pivot on the other prime
            cols2 = pivot_columns(rows[P2], P2)
            if det_mod(rows[P1], cols2, P1) != 0:
                cols = cols2; d1 = det_mod(rows[P1], cols, P1); d2 = det_mod(rows[P2], cols, P2)
        cert = dict(
            kind="target_minor",
            size=k,
            complete=(k == DIM),
            point_ids=[prim[c][0] for c in cols],
            point_index_in_primary=cols,
            u_symbols=[prim[c][3] for c in cols],
            u_all_nonzero=all(prim[c][3] != 0 for c in cols),
            det_P1=d1, det_P2=d2,
            nonzero_at_both_primes=(d1 != 0 and d2 != 0),
            primes=[P1, P2],
            values_are="F_T(l_k . c_k) mod p for the mixed-letter bracket monomial T; "
                       "NO transport factor and NO u-power is applied to a target member "
                       "(transport applies to SOURCE rows only). Raw evaluator output.",
        )
    out["minor_certificate"] = cert

    # ---- per-member independent checks
    p = P1
    MS = msyms(prim, r, p)
    lin, cmap = rand_point(r, p, rng)
    m1ok = m2ok = m3ok = m4ok = 0
    m3void = 0
    for idx, F in enumerate(Fs):
        # M1 letter-order variation.  The REVERSED processing order: every letter is
        # visited in the opposite sequence, so the slot allocation, which letter opens
        # and which closes each 2-column, the firstside of every edge and the rho_sign
        # correction all differ -- while the open-2-column width is unchanged (an edge
        # is open between its two endpoints either way), so the cost is unchanged.
        # A uniformly random order is NOT usable here: its width reaches 2^15 states
        # and the packer's allocation blows past the run's memory bound (measured).
        alt = list(reversed(cached_order_mixed(F)[0]))
        v_def = mixed_eval_c(F, MS[0], p, r=r)
        v_alt = mixed_eval_c(F, MS[0], p, r=r, order=alt, max_W=10)
        m1ok += (v_def == v_alt)
        # M2 torus
        t = [rng.randrange(1, p) for _ in range(r)]
        v0 = mixed_eval_c(F, ms_of(lin, cmap, r, p), p, r=r)
        v1 = mixed_eval_c(F, ms_of(scale_linear(lin, t, p), scale_cubic(cmap, t, p), r, p), p, r=r)
        chi = 1
        for i in range(r): chi = chi * pow(t[i], lam[i], p) % p
        m2ok += (v1 == chi * v0 % p)
        # M3 raising (both directions)
        def const(i, j):
            vs = []
            for _ in range(2):
                e = rng.randrange(1, p)
                vs.append(mixed_eval_c(F, ms_of(subst_linear(lin, i, j, e, p),
                                                subst_cubic(cmap, i, j, e, p, r), r, p), p, r=r))
            return all(v == v0 for v in vs)
        cu, cd = const(0, 1), const(1, 0)
        if v0 == 0: m3void += 1
        else: m3ok += (cu != cd)
        # M4 forced zero
        L8, C8 = rand_point(r, p, rng, support=list(range(r - 1)))
        m4ok += (mixed_eval_c(F, ms_of(L8, C8, r, p), p, r=r) == 0)
    out["per_member_checks"] = dict(
        n=len(Fs),
        M1_letter_order_invariant=m1ok,
        M2_torus_weight=m2ok,
        M3_raising_one_sided=m3ok, M3_void_because_zero_at_probe=m3void,
        M4_forced_zero_span8=m4ok,
        all_passed=(m1ok == len(Fs) and m2ok == len(Fs) and m4ok == len(Fs)
                    and m3ok == len(Fs) - m3void))

    dst = os.path.join(ROOT, "results", "b14_01", f"certificate_d{delta}.json")

    def bank():
        json.dump(dict(out, members=[m for m in D["members"]],
                       rows_P1=rows[P1], rows_P2=rows[P2],
                       values_are="rows[prime][i][j] = F_{T_i}(l_j . c_j) mod prime, "
                                  "primary points in P13/P14 file order, no transform applied"),
                  open(dst, "w"))
    bank()                       # the certificate is banked BEFORE the optional M5 step

    # ---- M5 independent pure-Python DP at the real shape
    m5 = []
    m5_error = None
    try:
        for F in Fs[:a.m5_sample]:
            for q in (P1, P2):
                MSq = msyms(prim, r, q)
                vc = mixed_eval_c(F, MSq[0], q, r=r)
                vp = py_dp_eval(F, MSq[0], q, r=r)
                m5.append(dict(prime=q, c_core=vc, py_dp=vp, equal=(vc == vp), nonzero=(vc != 0)))
    except MemoryError as e:
        m5_error = "MemoryError: the dict-state DP exceeded the run's ulimit at this shape"
    out["M5_independent_python_dp"] = dict(
        error=m5_error, n=len(m5), n_equal=sum(1 for x in m5 if x["equal"]),
        n_nonzero=sum(1 for x in m5 if x["nonzero"]),
        passed=(len(m5) > 0 and all(x["equal"] for x in m5)
                and any(x["nonzero"] for x in m5)),
        detail=m5)

    out["elapsed_s"] = round(time.time() - t0, 1)
    bank()
    out.pop("minor_certificate", None)
    print(json.dumps(out, indent=1)[:4000])
    print("\nMINOR:", json.dumps(cert, indent=1) if cert else "none")
    print("wrote", os.path.relpath(dst, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
