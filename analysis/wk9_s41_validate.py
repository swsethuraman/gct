#!/usr/bin/env python3
"""
Session 41 -- the validation battery (results/PREREG_s41.md P1).  Nothing new
is measured until every part passes.

  part A  the l^3 m witness through the reduced pipeline (kernel (12,-3,1),
          mult 0; the wrong rule gives (1,-4,3), mult 1) and unreduced;
          analysis/wk8_s30_calib.py as-is (quote the discriminating ratio).
  part B  the in-place kernel route against the exact route on the six s36
          validation cells (delta 6, ell 5): same a, same mult_det, mult_pad,
          identical kernel span, both primes.
  part C  three banked ell = 6 cells of results/s36_ledger.md, chosen by the
          rule fixed in the prereg: (10,8,7,1,1,1) [D = -1, discriminating],
          (13,8,4,1,1,1) [exact route], (13,9,2,2,1,1) [compressed route] --
          reproduced by s36's route AND by the in-place route; ledger values
          and identical kernel spans required.
  part D  the m_det anchors (scripts/ambient_screen.py --selftest: 3, 11, 43).

usage: python3 wk9_s41_validate.py [A|B|C|D|all]  -> results/s41_validation.md
"""
import sys, os, time, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.join(HERE, '..')
from wk9_s36_stabred import (orbit_setup, reduced_rows, kernel_exact, point_rows, mult_from,
                             expand, P1, P2, log)
from wk8_s30_core import measure, per_padded
from wk9_s41_kernel import measure_cell, span_identical

OUT = os.path.join(ROOT, 'results', 's41_validation.md')
S36VAL = {  # results/sweep62_ledger.md rows used by s36's Part 2: lam -> (a, N_S, mult_det, mult_pad)
    (13, 5, 2, 2, 2): (2, 3672, 2, 2), (14, 4, 2, 2, 2): (2, 2337, 2, 2),
    (12, 6, 2, 2, 2): (4, 5194, 4, 4), (13, 5, 4, 1, 1): (2, 1824, 2, 2),
    (12, 5, 5, 1, 1): (2, 2795, 2, 2), (9, 8, 5, 1, 1): (2, 5159, 2, 2),
}
S36ELL6 = {  # results/s36_ledger.md Stratum B rows: lam -> (delta, a, N_S, Stab, n_chi, route, mult_det, mult_pad)
    (10, 8, 7, 1, 1, 1): (7, 3, 75689, 6, 5740, 'compressed', 3, 2),
    (13, 8, 4, 1, 1, 1): (7, 2, 27213, 6, 1844, 'exact', 2, 2),
    (13, 9, 2, 2, 1, 1): (7, 2, 23148, 4, 4747, 'compressed', 2, 2),
}

def emit(s):
    print(s); sys.stdout.flush()
    with open(OUT, 'a') as fh: fh.write(s + "\n")

def partA():
    emit("\n## Part A — the `l^3 m` witness (reduced and unreduced) and `wk8_s30_calib.py` as-is\n")
    f1, N1 = per_padded(1, 4)
    ok = True
    basis, vecs, group = orbit_setup(4, 2, 2, (4, 4), verbose=False)
    rows, _ = reduced_rows(4, 2, 2, (4, 4), vecs, verbose=False)
    for p in (P1, P2):
        a, rk, kern = kernel_exact(rows, len(vecs), p)
        full = expand(vecs, kern[0], p)
        v = [full.get(m, 0) for m in basis]
        inv = pow(v[2], p - 2, p); vn = tuple(x * inv % p for x in v)
        ev = point_rows(f1, N1, 4, 2, basis, vecs, 9, 11, 40, p)
        mult = mult_from(kern, ev, a, p)
        good = (a == 1 and vn == (12 % p, (-3) % p, 1) and mult == 0)
        ok &= good
        emit(f"- reduced witness, p = {p}: a = {a}, kernel ∝ `{(12, -3, 1) if good else vn}`, mult = {mult} — "
             f"{'ok' if good else '**FAIL**'} (wrong rule would give `(1,-4,3)`, mult 1)")
    res = measure(f1, N1, 4, 2, 2, (4, 4), a_expect=1)
    good = res['mult'] == 0; ok &= good
    emit(f"- unreduced witness (`wk8_s30_core.measure`): mult = {res['mult']} — {'ok' if good else '**FAIL**'}")
    pr = subprocess.run([sys.executable, os.path.join(HERE, 'wk8_s30_calib.py')], capture_output=True, text=True)
    txt = pr.stdout
    emit("- `analysis/wk8_s30_calib.py` as-is:\n")
    emit("```\n" + txt.strip() + "\n```")
    good = 'CALIBRATION PASSED' in txt; ok &= good
    emit(f"\n**Part A: {'PASS' if ok else 'FAIL'}** — the discriminating ratio is the battery line above "
         f"(World A cells with `mult < a` / cells).")
    return ok

def partB():
    emit("\n## Part B — in-place kernel route vs exact route, the six s36 validation cells (`δ = 6`, `ℓ = 5`)\n")
    emit("| lam | a | N_S | n_chi | route | a (kernel) | rank(R) | mult_det | mult_pad | ledger (det, pad) | span identical (p1, p2) | VmHWM GB | verdict |")
    emit("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    fails = []
    for lam, (a_exp, ns, md, mp) in S36VAL.items():
        oe = measure_cell(4, 5, 6, lam, a_exp, route='exact', verbose=False)
        oi = measure_cell(4, 5, 6, lam, a_exp, route='inplace', verbose=False)
        same = [span_identical(oe['per_prime'][p]['kern'], oi['per_prime'][p]['kern'], a_exp, p) for p in (P1, P2)]
        for o, name in ((oe, 'exact'), (oi, 'inplace')):
            ok = (o['N_S'] == ns and o['mult_det'] == md and o['mult_pad'] == mp
                  and all(v['a'] == a_exp and v['rank'] == o['n_chi'] - a_exp for v in o['per_prime'].values()))
            ok_all = ok and all(same)
            if not ok_all: fails.append((lam, name))
            emit(f"| `{lam}` | {a_exp} | {o['N_S']} | {o['n_chi']} | {name} | {o['per_prime'][P1]['a']} | {o['per_prime'][P1]['rank']} | "
                 f"{o['mult_det']} | {o['mult_pad']} | ({md}, {mp}) | {'yes' if same[0] else 'NO'}, {'yes' if same[1] else 'NO'} | "
                 f"{o['hwm']:.2f} | {'ok' if ok_all else '**FAIL**'} |")
    emit(f"\n**Part B: {'PASS' if not fails else 'FAIL'}** — failures: {fails if fails else 'none'}.")
    return not fails

def partC():
    emit("\n## Part C — three banked `ℓ = 6` cells of `results/s36_ledger.md`, by s36's route and by the in-place route\n")
    emit("Chosen by the prereg rule: the only `D ≠ 0` six-row row `(10,8,7,1,1,1)`, plus `(13,8,4,1,1,1)` and `(13,9,2,2,1,1)` "
         "drawn by `sha256(\"s41 2026-09-02\")` from the 17 `D = 0` rows with `n_χ ≤ 8000`.\n")
    emit("| lam | delta | route | a | N_S | Stab | n_chi | rank(R) | mult_det | mult_pad | D | ledger (a, N_S, Stab, n_chi, det, pad) | span identical (p1, p2) | secs | VmHWM GB | verdict |")
    emit("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    fails = []
    for lam, (delta, a_exp, ns, so, nchi, route36, md, mp) in S36ELL6.items():
        o36 = measure_cell(4, 6, delta, lam, a_exp, route=route36, verbose=False)
        oi = measure_cell(4, 6, delta, lam, a_exp, route='inplace', verbose=False)
        same = [span_identical(o36['per_prime'][p]['kern'], oi['per_prime'][p]['kern'], a_exp, p) for p in (P1, P2)]
        for o, name in ((o36, route36 + ' (s36)'), (oi, 'inplace')):
            ok = (o['N_S'] == ns and o['stab'] == so and o['n_chi'] == nchi and o['mult_det'] == md and o['mult_pad'] == mp
                  and all(v['a'] == a_exp and v['rank'] == nchi - a_exp for v in o['per_prime'].values()))
            ok_all = ok and all(same)
            if not ok_all: fails.append((lam, name))
            emit(f"| `{lam}` | {delta} | {name} | {o['per_prime'][P1]['a']} | {o['N_S']} | {o['stab']} | {o['n_chi']} | {o['per_prime'][P1]['rank']} | "
                 f"{o['mult_det']} | {o['mult_pad']} | {o['mult_pad']-o['mult_det']:+d} | ({a_exp}, {ns}, {so}, {nchi}, {md}, {mp}) | "
                 f"{'yes' if same[0] else 'NO'}, {'yes' if same[1] else 'NO'} | {o['secs']:.0f} | {o['hwm']:.2f} | {'ok' if ok_all else '**FAIL**'} |")
    emit(f"\n**Part C: {'PASS' if not fails else 'FAIL'}** — failures: {fails if fails else 'none'}.  "
         "The `(10,8,7,1,1,1)` row is the discriminating one: `mult_pad = 2 < a = 3` must reproduce, not merely `mult = a`.")
    return not fails

def partD():
    emit("\n## Part D — the `m_det` anchors\n")
    pr = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'ambient_screen.py'), '--selftest'],
                        capture_output=True, text=True)
    lines = [l for l in pr.stdout.splitlines() if 'm_det' in l or 'PASSED' in l or 'FAIL' in l]
    emit("```\n" + "\n".join(lines) + "\n```")
    ok = 'ALL CHECKS PASSED' in pr.stdout
    emit(f"\n**Part D: {'PASS' if ok else 'FAIL'}** — `Σ m_det = 3, 11, 43` at `n = 3`, `δ = 2, 3, 4`.")
    return ok

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which == 'all' or not os.path.exists(OUT):
        with open(OUT, 'w') as fh:
            fh.write("# Validation battery — session 41\n\n"
                     "Run before any new cell (`results/PREREG_s41.md` P1).  Both house primes at every rank.  "
                     "Pad points everywhere are true padded-permanent restrictions `x_0 · per_3(x_1..x_9)` with random "
                     "linear-form substitutions.  The in-place kernel route is `analysis/wk9_s41_kernel.py`.\n")
    parts = {'A': partA, 'B': partB, 'C': partC, 'D': partD}
    results = {}
    for k in (['A', 'B', 'C', 'D'] if which == 'all' else [which]):
        t0 = time.time()
        results[k] = parts[k]()
        emit(f"\n_(part {k}: {time.time()-t0:.0f}s)_")
    emit("\n---\n**BATTERY " + ("PASSED" if all(results.values()) else "FAILED — STOP") +
         f"** (parts run: {sorted(results)})")
