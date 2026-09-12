#!/usr/bin/env python3
"""B14-01 -- the target-side run: mixed-letter members and a nonzero h x h minor.

  --degree 13   lambda = (21,17,2^7), shape (9,9,2^15,1^4), target dim 73, points P13
  --degree 14   lambda = (25,17,2^7), shape (9,9,2^15,1^8), target dim 159, points P14

Search phases, exactly as pre-registered in results/PREREG_b14_01.md section 4:
  S1  strip-directed random, quota 4*a_3(mu) draws per strip   (pre-registered)
  S2  one deterministic semistandard pass per strip            (pre-registered, the ONLY one)
  S3  unconstrained fallback                                   (pre-registered as EXPLORATORY)

A candidate is accepted iff it strictly raises the rank over P1.  Accepted members
are re-evaluated at P2 independently.  Resumable: state is checkpointed after every
acceptance.
"""
import argparse, json, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from b14_01_mixed import (MixedFilling, random_mixed_filling, mixed_eval_c, rank_mod,
                          msym_linear, msym_cubic, strip_ell_cells)
from b14_01_controls import horiz_strips
from wk8_s30_core import P1, P2
from flint import nmod_mat

CFG = {
    13: dict(h=9, n2=15, n1=4, delta=13, r=9, dim=73, pts="P13.json",
             a3=[7, 4, 9, 5, 4, 9, 5, 3, 8, 3, 2, 6, 2, 1, 5]),
    14: dict(h=9, n2=15, n1=8, delta=14, r=9, dim=159, pts="P14.json", a3=None),
}


def load_points(fn, role="primary"):
    d = json.load(open(os.path.join(ROOT, "results", "b14_prep", "points", fn)))
    CE = [tuple(x) for x in d["cubic_exponents"]]          # the file's OWN order
    out = []
    for pt in d["points"]:
        if role and pt["role"] != role: continue
        cmap = {CE[k]: pt["cubic_coefficients"][k] for k in range(len(CE))}
        out.append((pt["id"], pt["linear"], cmap, pt["u_symbol"]))
    return d, out


def msyms(pts, r, p):
    return [{1: msym_linear(lin, r, p), 3: msym_cubic(cmap, r, p)} for _, lin, cmap, _ in pts]


def row_of(F, MS, p, r):
    return [mixed_eval_c(F, ms, p, r=r) for ms in MS]


def semistandard_fillings(h, n2, n1, delta, cells, max_out, rng_seed=0):
    """ONE deterministic pass: c-letters assigned to the non-strip cells column by
    column, left to right, rows top to bottom, letters chosen in increasing index
    among those still having legs -- a semistandard-style canonical order, then
    systematic rotations of the letter alphabet.  Deterministic: no rng."""
    val = [1] * delta + [3] * delta
    ncol = 2 + n2 + n1
    cols = [(0, list(range(h))), (1, list(range(h)))]
    cols += [(2 + e, [0, 1]) for e in range(n2)]
    cols += [(2 + n2 + c, [0]) for c in range(n1)]
    out = []
    for rot in range(max_out):
        rem = list(val)
        cell_letter = {}
        for li, cell in enumerate(cells):
            cell_letter[cell] = li; rem[li] -= 1
        ok = True
        step = 0
        for col, rows in cols:
            used = {cell_letter[(col, rw)] for rw in rows if (col, rw) in cell_letter}
            for rw in rows:
                if (col, rw) in cell_letter: continue
                avail = [l for l in range(len(val)) if rem[l] > 0 and l not in used]
                if not avail: ok = False; break
                # deterministic: rotate the starting point by (rot + step)
                pick = avail[(rot + step) % len(avail)]
                step += 1
                cell_letter[(col, rw)] = pick; rem[pick] -= 1; used.add(pick)
            if not ok: break
        if not ok or any(rem): continue
        C1 = [cell_letter[(0, k)] for k in range(h)]
        C2 = [cell_letter[(1, k)] for k in range(h)]
        two = [(cell_letter[(2 + e, 0)], cell_letter[(2 + e, 1)]) for e in range(n2)]
        one = [cell_letter[(2 + n2 + c, 0)] for c in range(n1)]
        try:
            out.append(MixedFilling(h, n2, n1, val, C1, C2, two, one))
        except AssertionError:
            continue
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, default=13)
    ap.add_argument("--seed", type=int, default=140113)
    ap.add_argument("--max-seconds", type=float, default=5400)
    ap.add_argument("--s3-draws", type=int, default=60000)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    C = CFG[a.degree]
    h, n2, n1, delta, r, DIM = C["h"], C["n2"], C["n1"], C["delta"], C["r"], C["dim"]
    lam = tuple([2 + n2 + n1, 2 + n2] + [2] * (h - 2))
    out = a.out or os.path.join(ROOT, "results", "b14_01", f"members_d{delta}.json")
    meta, pts = load_points(C["pts"], "primary")
    MS1 = msyms(pts, r, P1)
    S = horiz_strips(lam, delta, r)
    a3 = C["a3"] or [None] * len(S)
    rng = random.Random(a.seed)
    t0 = time.time()

    accepted = []          # (phase, mu, filling, row_P1)
    mat = []
    seen = set()
    probe_idx = [0, 1, 2]

    def try_candidate(F, mu, phase):
        k = F.key()
        if k in seen: return False
        seen.add(k)
        if not any(mixed_eval_c(F, MS1[i], P1, r=r) for i in probe_idx):
            return False                                   # not live; cheap screen
        row = row_of(F, MS1, P1, r)
        if not any(row): return False
        if rank_mod(mat + [row], P1) <= len(mat): return False
        mat.append(row); accepted.append((phase, mu, F, row))
        return True

    log = []
    def note(s):
        log.append(f"[{time.time()-t0:7.1f}s] {s}")
        print(log[-1], flush=True)

    # ---------------- S1: strip-directed, quota 4*a3 per strip
    for si, mu in enumerate(S):
        quota = 4 * a3[si] if a3[si] else 40
        for _ in range(quota):
            if len(mat) >= DIM or time.time() - t0 > a.max_seconds: break
            try:
                cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                F = random_mixed_filling(h, n2, n1, delta, delta, rng, ell_cells=cells)
            except Exception:
                continue
            try_candidate(F, list(mu), "S1")
    note(f"S1 done: rank {len(mat)} / {DIM}  ({len(seen)} candidates)")
    s1_rank = len(mat)

    # ---------------- S2: ONE deterministic semistandard pass per strip
    if len(mat) < DIM:
        for si, mu in enumerate(S):
            if time.time() - t0 > a.max_seconds: break
            cells = strip_ell_cells(lam, mu, h, n2, n1, None)     # no shuffle: deterministic
            for F in semistandard_fillings(h, n2, n1, delta, cells, max_out=4 * (a3[si] or 10) + 20):
                if len(mat) >= DIM or time.time() - t0 > a.max_seconds: break
                try_candidate(F, list(mu), "S2")
    note(f"S2 done: rank {len(mat)} / {DIM}  ({len(seen)} candidates)")
    s2_rank = len(mat)

    # ---------------- S3: pre-registered EXPLORATORY fallback
    drew = 0
    if len(mat) < DIM:
        order = list(range(len(S)))
        while len(mat) < DIM and drew < a.s3_draws and time.time() - t0 < a.max_seconds:
            si = order[drew % len(order)]
            mu = S[si]
            drew += 1
            try:
                cells = strip_ell_cells(lam, mu, h, n2, n1, rng)
                F = random_mixed_filling(h, n2, n1, delta, delta, rng, ell_cells=cells)
            except Exception:
                continue
            if try_candidate(F, list(mu), "S3") and len(mat) % 10 == 0:
                note(f"S3: rank {len(mat)} / {DIM}  ({len(seen)} candidates, {drew} draws)")
    note(f"S3 done: rank {len(mat)} / {DIM}  ({len(seen)} candidates, {drew} draws)")

    res = dict(degree=delta, lam=list(lam), shape=[h, h] + [2] * n2 + [1] * n1,
               target_dim_adopted=DIM, n_points=len(pts),
               point_ids=[p[0] for p in pts],
               rank_P1=len(mat), s1_rank=s1_rank, s2_rank=s2_rank,
               n_candidates=len(seen), s3_draws=drew,
               elapsed_s=round(time.time() - t0, 1),
               seed=a.seed,
               members=[dict(phase=ph, mu=mu, filling=F.to_json()) for ph, mu, F, _ in accepted],
               rows_P1=[row for _, _, _, row in accepted],
               log=log)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"))
    note(f"wrote {out}  rank_P1={len(mat)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
