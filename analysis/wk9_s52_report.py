#!/usr/bin/env python3
"""
Session 52 -- assemble results/s52_census.md and results/s52_ledger.md from the
banked jsonl.

usage: python3 wk9_s52_report.py
"""
import sys, os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s52_todo import banked

FILES = ['results/s52_cells.jsonl', 'results/s52_cells_d9.jsonl', 'results/s52_cells_d10.jsonl']


def load():
    B = banked()
    seen, rows = set(), []
    for f in FILES:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p): continue
        for ln in open(p):
            r = json.loads(ln)
            k = (tuple(r['lam']), r['delta'])
            if k in seen: continue
            seen.add(k)
            r['banked'] = k in B
            rows.append(r)
    return rows


def ledger_rows():
    p = os.path.join(ROOT, 'results/s52_ledger.jsonl')
    if not os.path.exists(p): return []
    return [json.loads(ln) for ln in open(p)]


def main():
    rows = load()
    deltas = sorted(set(r['delta'] for r in rows))
    L = []
    A = L.append
    A("# Session 52 — the `a = 1` census (`n = 4`, `r = 6`, `ℓ(λ) = 6`)\n")
    A("Region fixed in `results/PREREG_s52.md` §1 before any run: `λ ⊢ 4δ`, `ℓ(λ) = 6`\n"
      "exactly, **obstruction-eligible** iff `λ_1 ≥ δ` (Corollary B of\n"
      "`docs/reducible_ideal.md`; and, independently, Kadish–Landsberg's padding bound\n"
      "at `(n,m) = (4,3)` — see `docs/bip_transfer.md` §3(a)).\n")
    A("**Routes.**  `a` by Frobenius plethysm (`wk8_s30_pleth.amb`) **and** by Weyl\n"
      "alternation over a tail DP (`wk9_s42_census.a_weyl`), asserted equal at every\n"
      "`a = 1` cell and at a random sample of the rest.  `h_pad` by Pieri strips over\n"
      "the cubic plethysm (`wk9_s42_hpad.h_pad`) **and**, on a sample, by the Weyl\n"
      "route (`wk9_s42_census.h_pad_weyl`).  `N_S` by the generating-function DP.\n"
      "`n_χ ~` is the estimate `⌈N_S/|Stab|⌉`, which session 46 showed is **neither an\n"
      "upper nor a lower bound** on the true `n_χ` (off by 21% in both directions on\n"
      "different cells); the measured `n_χ` appears in `results/s52_ledger.md`.\n")
    A("**Lemma A** (`results/PREREG_s52.md` §2, proved before the census ran): at\n"
      "`a = 1` the `h_pad` bound fires exactly when `h_pad = 0`, and `h_pad = 0` forces\n"
      "`mult_red = 0`, hence `mult_pad = 0`, hence `i_pad = 1` and `D ≤ 0` — with no\n"
      "measurement.  So the **informative** `a = 1` cells are exactly those with\n"
      "`h_pad ≥ 1`, and the `h_pad = 0` cells are marked below and excluded from every\n"
      "count of evidence.  (Session 47 was refuted partly for counting them.)\n")

    A("\n## Summary\n")
    A("| `δ` | eligible cells | units | `a = 1` eligible | `h_pad = 0` (dead by Lemma A) | **informative** | already measured | unmeasured |")
    A("|---|---|---|---|---|---|---|---|")
    for d in deltas:
        sub = [r for r in rows if r['delta'] == d]
        el = [r for r in sub if r['eligible']]
        a1 = [r for r in el if r['a'] == 1]
        dead = [r for r in a1 if not r['informative']]
        inf = [r for r in a1 if r['informative']]
        bk = [r for r in inf if r['banked']]
        A(f"| {d} | {len(el)} | {sum(r['a'] for r in el)} | {len(a1)} | {len(dead)} | "
          f"**{len(inf)}** | {len(bk)} | {len(inf)-len(bk)} |")
    tot_el = [r for r in rows if r['eligible']]
    tot_a1 = [r for r in tot_el if r['a'] == 1]
    tot_inf = [r for r in tot_a1 if r['informative']]
    tot_bk = [r for r in tot_inf if r['banked']]
    A(f"| **all** | **{len(tot_el)}** | **{sum(r['a'] for r in tot_el)}** | **{len(tot_a1)}** | "
      f"**{len(tot_a1)-len(tot_inf)}** | **{len(tot_inf)}** | **{len(tot_bk)}** | "
      f"**{len(tot_inf)-len(tot_bk)}** |")

    A("\n## The `a = 1` cells, by degree\n")
    A("`meas` = a `mult_det` for this cell already exists in a banked ledger\n"
      "(`results/s36_aone.md`, `s36_ledger.md`, `s41_ledger.md`, `s43_ledger.md`,\n"
      "`s45_ledger.md`, `s46_ledger.md`), found by re-parsing those files; the same\n"
      "parser reproduces the reconciled six-row record exactly (193 cells,\n"
      "16/70/67/40 over `δ = 6,7,8,9`).\n")
    for d in deltas:
        a1 = sorted([r for r in rows if r['delta'] == d and r['eligible'] and r['a'] == 1],
                    key=lambda r: r.get('nchi_lb', 0))
        A(f"\n### `δ = {d}` — {len(a1)} `a = 1` eligible cells\n")
        A("| λ | `h_pad` | informative | `N_S` | \\|Stab\\| | `n_χ ~` | balance | meas |")
        A("|---|---|---|---|---|---|---|---|")
        for r in a1:
            A(f"| `{tuple(r['lam'])}` | {r['h_pad']} | {'yes' if r['informative'] else '**no**'} | "
              f"{r.get('N_S','—')} | {r.get('stab','—')} | {r.get('nchi_lb','—')} | {r['bal']} | "
              f"{'yes' if r['banked'] else '—'} |")

    LR = ledger_rows()
    if LR:
        A("\n## Measured this session\n")
        A("See `results/s52_ledger.md` for the full rows.\n")

    open(os.path.join(ROOT, 'results/s52_census.md'), 'w').write("\n".join(L) + "\n")
    print("wrote results/s52_census.md", len(L), "lines")

    # ---- ledger ----
    if not LR: return
    M = []
    B = M.append
    B("# Session 52 ledger — the `a = 1` cells measured this session\n")
    B("`n = 4`, `ℓ(λ) = 6`, `a = 1`, ascending in the pre-registered `n_χ` order.\n")
    B("**Route.**  Session 45's sparse certificate (`analysis/wk9_s45_cell.py`,\n"
      "`analysis/wk9_s42_wied.c`): `mult = a − dim ker[E; ev]` with the `K = a + 8`\n"
      "evaluation rows pinned through every compression level, both house primes\n"
      "`2147483647` and `2147483629` run concurrently.  Since `rank_p ≤ rank_Q`,\n"
      "`nullity_p = 0` at a **single** prime *proves* `mult = a` over `ℚ`; at `a = 1`\n"
      "that is exactly the brief's cheap direction, `i = 0` certified by one\n"
      "non-singularity certificate.  A non-zero nullity is a measurement, not a\n"
      "verdict, until its kernel vector is exhibited and verified.\n")
    B("**Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the\n"
      "**true** padded permanent `x_0·per_3(x_1..x_9)` restricted, never\n"
      "`ℓ·(random cubic)`.\n")
    B("\n| `δ` | λ | `h_pad` | `N_S` | \\|Stab\\| | `n_χ` | rows | `mult_det` | `i_det` | `mult_pad` | `i_pad` | `mult_red` | `D` | route | certificate | secs | HWM GB |")
    B("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in LR:
        if r.get('status') == 'DEFER':
            B(f"| {r['delta']} | `{tuple(r['lam'])}` | {r['h_pad']} | — | — | — | — | — | — | — | — | — | — | "
              f"— | **DEFER** | {r.get('secs')} | — |")
            continue
        B(f"| {r['delta']} | `{tuple(r['lam'])}` | {r['h_pad']} | {r['N_S']} | {r['stab']} | {r['n_chi']} | "
          f"{r['nrows']} | **{r['mult_det']}** | {r['i_det']} | {r['mult_pad']} | {r['i_pad']} | "
          f"{r.get('mult_red','—')} | {r['D']:+d} | {r.get('route')} | {r.get('cert')} | {r.get('secs')} | "
          f"{r.get('hwm_gb')} |")
    ok = [r for r in LR if r.get('status') == 'measured']
    B(f"\n**{len(ok)} cells measured, `i_det = 0` at "
      f"{len([r for r in ok if r['i_det']==0])} of them, `D > 0` at "
      f"{len([r for r in ok if r['D']>0])}.**\n")
    open(os.path.join(ROOT, 'results/s52_ledger.md'), 'w').write("\n".join(M) + "\n")
    print("wrote results/s52_ledger.md", len(M), "lines")


if __name__ == '__main__':
    main()
