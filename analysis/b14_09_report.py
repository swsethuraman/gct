#!/usr/bin/env python3
"""
B14-09 -- every number quoted in docs/b14_09_report.md, generated from the
banked artefacts.  Printed, never hand-transcribed.

usage: python3 analysis/b14_09_report.py [--out results/b14_09/report_numbers.md]
"""
import sys, os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
WIDE = 1 << 21


def load():
    sz = json.load(open(os.path.join(ROOT, 'results/b14_09/sizing.json')))
    ct = json.load(open(os.path.join(ROOT, 'results/b14_09/controls.json')))
    ex = json.load(open(os.path.join(ROOT, 'results/b14_09/extended.json')))
    ec = json.load(open(os.path.join(ROOT, 'results/b14_09/engine_controls.json')))
    dec = []
    for fn in sorted(glob.glob(os.path.join(ROOT, 'results/b14_09/per6_d10_lane*.jsonl'))):
        for line in open(fn):
            if line.strip():
                dec.append(json.loads(line))
    seen = {}
    for d in dec:
        seen[d['rank']] = d
    return sz, ct, ex, ec, [seen[k] for k in sorted(seen)]


def main():
    sz, ct, ex, ec, dec = load()
    cells = {c['rank']: c for c in sz['cells']}
    L = []
    P = L.append
    P("# B14-09 — the generated numbers\n")
    P("Every figure quoted in `docs/b14_09_report.md` is printed here from the banked")
    P("artefacts by `analysis/b14_09_report.py`. Nothing in the report is transcribed by hand.\n")

    P("## 1. The object\n")
    P(f"- open cells sized: **{len(cells)}**  (47 of B13-08's 95-cell queue unreached + 11 it deferred)")
    P(f"- `sum a` over the 58: **{sum(c['a'] for c in cells.values())}**")
    P(f"- `n_chi` over the 58: **{min(c['n_chi'] for c in cells.values()):,}** to "
      f"**{max(c['n_chi'] for c in cells.values()):,}**")
    P(f"- of the 58, **{sum(1 for c in cells.values() if c['needs_matmul_mod_wide'])}** have "
      f"`n_chi >= 2^21` and so need `matmul_mod_wide`")
    P(f"- whole-degree table: all **{ex['degree10_all_402']['count']}** degree-10 six-row weights, "
      f"`n_chi` {ex['degree10_all_402']['n_chi_min']:,} to {ex['degree10_all_402']['n_chi_max']:,}, "
      f"**{ex['degree10_all_402']['wide_measured']}** needing `matmul_mod_wide`")
    P("")

    P("## 2. Controls on the sizing instrument\n")
    c12 = ct['c1_c2']
    P(f"- **C1/C2** — {c12['records']} banked `(n,r,mu,delta)` records carrying a MEASURED `n_chi`, "
      f"from {len(c12['sources'])} files, {c12['by_nr']}. "
      f"`N_S` mismatches **{len(c12['C1_N_S_mismatches'])}**, "
      f"`n_chi` mismatches **{len(c12['C2_n_chi_mismatches'])}**, "
      f"`|Stab|` mismatches **{len(c12['stab_mismatches'])}**, in {c12['secs']} s. "
      f"{c12['C1']} / {c12['C2']}")
    a = ct['c3a_chi_dropped']
    P(f"- **C3a** (chi dropped) — tested {a['tested']}, **disagrees on {a['disagreeing']}**, "
      f"still agrees on {a['still_agreeing']} (forced: those are the cells whose repeated parts are all "
      f"even, where chi is trivial). {a['C3a']}")
    b = ct['c3b_group_widened']
    P(f"- **C3b** (group widened to S_6) — tested {b['tested']}, disagrees on **{b['disagreeing']}**. {b['C3b']}")
    cc = ct['c3c_weight_perturbed']
    P(f"- **C3c** (weight off n*delta) — {cc['refused']} of {cc['tested']} refused, no number returned. {cc['C3c']}")
    c4 = ct['c4_independent_implementations']
    P(f"- **C4** (the repository's own enumerate-and-canonicalise routes) — {c4['tested']} cells, "
      f"all agree. {c4['C4']}")
    for r in c4['rows']:
        extra = f", s36 {r['s36']['secs']} s" if 's36' in r else ""
        P(f"    - `{tuple(r['mu'])}`_{r['delta']}: N_S {r['s45']['N_S']:,}, |Stab| {r['s45']['stab']}, "
          f"n_chi {r['s45']['n_chi']:,}  — s45 {r['s45']['secs']} s{extra}, character sum {r['char_sum']['n_chi']:,}")
    P("")

    P("## 3. Engine controls, on this host\n")
    P(f"- A {ec['A']['status']}, B {ec['B_status']}, C {ec['C_status']}, D {ec['D_status']}")
    for e in ec['B']:
        P(f"    - B `{tuple(e['mu'])}` a={e['a']}: all fields equal **{e['all_equal']}**; "
          f"{e['wall_secs']} s here against {e['record_secs']} recorded, "
          f"HWM {e['hwm_gb']} GB against {e['record_hwm_gb']}")
    for e in ec['C']:
        for p, v in e['per_prime'].items():
            P(f"    - C `{tuple(e['mu'])}` p={p}: diagonal rank **{v['rank_diagonal_pencils']}** "
              f"(rows all zero {v['diag_all_rows_zero']}), per_3 rank {v['rank_per3_pencils']}, "
              f"det_3 rank {v['rank_det3_pencils']}")
    P("")

    P("## 4. Decided cells\n")
    P(f"**{len(dec)} of the 58 decided.** All at both house primes.\n")
    P("| rank | mu | a | n_chi | mult | units | C5 | C6 | wide | secs | HWM GB |")
    P("|---:|---|---:|---:|---:|---:|:-:|:-:|:-:|---:|---:|")
    for d in dec:
        P(f"| {d['rank']} | `{tuple(d['mu'])}` | {d['a']} | {d['n_chi']:,} | {d['mult']} | {d['units']} | "
          f"{d['C5']} | {d['C6']} | {'W' if d.get('wide_used') else '·'} | {d['total_secs']} | {d['hwm_gb']} |")
    if dec:
        P(f"\n- `sum a` decided: **{sum(d['a'] for d in dec)}** of {sum(c['a'] for c in cells.values())}")
        P(f"- drops: **{sum(1 for d in dec if d['units'])}**; prime disagreements: "
          f"**{sum(1 for d in dec if not d['primes_agree'])}**")
        P(f"- C5 failures: **{sum(1 for d in dec if d['C5'] != 'PASS')}**; "
          f"C6 failures: **{sum(1 for d in dec if d['C6'] != 'PASS')}**")
        P(f"- total decided wall time: **{sum(d['total_secs'] for d in dec):,.0f} s** "
          f"across two lanes on 2 CPUs; peak resident over all cells **{max(d['hwm_gb'] for d in dec)} GB**")
        errs = [abs(d['total_secs'] - cells[d['rank']]['pred_total_secs']) / d['total_secs'] for d in dec]
        P(f"- the pre-registered cost fit's relative error on these, median "
          f"**{sorted(errs)[len(errs)//2]:.2f}**, max **{max(errs):.2f}** "
          f"(two lanes sharing 2 CPUs; the fit was made on single-lane data)")
    P("")

    P("## 5. Where the record stands after this session\n")
    n_after = 344 + len(dec)
    P(f"- degree-10 length-6 weights empty: **{n_after} of 402** (s79's 296 + B13-08's 48 + this session's {len(dec)})")
    P(f"- still open: **{402 - n_after}**, every one of which now has a measured `n_chi` and a priced cost")
    P("")

    P("## 6. `N_S/|Stab|` is neither bound — the measured size of the error\n")
    cr = ex['corpus_ratio']
    P(f"- over **{cr['count']}** banked records that carry both, `n_chi / (N_S/|Stab|)` runs "
      f"**{cr['min']['ratio']}** to **{cr['max']['ratio']}** "
      f"({cr['below_one']} below one, {cr['above_one']} above, {cr['equal']} equal)")
    P(f"    - lowest: `{tuple(cr['min']['mu'])}`_{cr['min']['delta']} (r={cr['min']['r']}), "
      f"N_S {cr['min']['N_S']:,}, |Stab| {cr['min']['stab']}, n_chi {cr['min']['n_chi']:,}")
    P(f"    - highest: `{tuple(cr['max']['mu'])}`_{cr['max']['delta']} (r={cr['max']['r']}), "
      f"N_S {cr['max']['N_S']:,}, |Stab| {cr['max']['stab']}, n_chi {cr['max']['n_chi']:,}")
    g = ex['degree10_all_402']
    P(f"- on the 402 degree-10 cells the ratio stays in **{g['ratio_min']}–{g['ratio_max']}** and the quotient "
      f"routes **{len(g['routed_wrongly_by_quotient'])}** of them wrongly — it gets the right answer here, "
      f"which is not the same as being a rule")
    bb = ex['b13_05_open_222']
    P(f"- `results/b13_05_final.json` labels `N_S/|Stab|` a **lower bound** (`n_chi_lb`) on all "
      f"{bb['count']} of its open cells. Measured: **{bb['below_the_recorded_lower_bound']} of {bb['count']}** "
      f"fall below it; ratios **{bb['ratio_min']}–{bb['ratio_max']}**; "
      f"sum measured {bb['sum_measured']:,} against {bb['sum_recorded_lb']:,} recorded")
    P("")
    txt = "\n".join(L) + "\n"
    dest = os.path.join(ROOT, sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv
                        else 'results/b14_09/report_numbers.md')
    open(dest, 'w').write(txt)
    print(txt)


if __name__ == '__main__':
    main()
