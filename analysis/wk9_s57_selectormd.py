#!/usr/bin/env python3
"""
Session 57 -- write results/s57_selector.md from the published data and the analyses.
Run after wk9_s57_publish.py, wk9_s57_ladder.py, wk9_s57_shortladders.py, wk9_s57_falsify.py.
"""
import sys, os, json, glob
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s57_lib import negative_record, tail_of, ladder_cell, lmr_weight, count_region, load_json_any, ROOT, log

CELLS = os.path.join(ROOT, 'results/s57_cells')
def J(name, default=None):
    return load_json_any(os.path.join(CELLS, name), default)
def L(l): return '`(' + ','.join(str(x) for x in l) + ')`'
def fmt(x):
    if x is None: return 'pending'
    if isinstance(x, bool): return 'yes' if x else 'no'
    if isinstance(x, int): return f"{x:,}"
    return str(x)

if __name__ == '__main__':
    pub = J('publish_summary.json'); ladder = J('ladder_status.json'); short = J('short_ladders.json'); fals = J('falsify.json')
    census = J('census_counts.json'); verify = J('verify.json', {})
    stable = {}
    for ln in open(os.path.join(CELLS, 'stable_a.jsonl')):
        r = json.loads(ln); stable[tuple(r['tail'])] = r['a_inf']
    rec = negative_record()
    fam = {(tuple(int(x) for x in r['lam'].strip('()').split(',')), r['delta']): r for r in pub['families']}
    out = []
    W = out.append
    W("# `results/s57_selector.md` — the rank-loss selector table, session 57\n")
    W("Region: `6 ≤ ℓ(λ) ≤ 10`, `10 ≤ δ ≤ 24`, `|λ| = 4δ`, `λ_1 ≥ δ`.  Pre-registration `results/PREREG_s57.md`; report `docs/s57_report.md`; code `analysis/wk9_s57_*.py`.  Every number below is banked in `results/s57_cells/` with its route; `pending` means not computed this session, keyed by `(δ, λ)` so it can be filled without redoing the rest.  `n_χ~ = ⌈N_S/|Stab|⌉` is an **estimate** (s46), for cost only.\n")
    # ---- 1 census
    W("## 1. The region: census counts (exact, all 75 chunks)\n")
    W("| δ | ℓ=6 | ℓ=7 | ℓ=8 | ℓ=9 | ℓ=10 | total |\n|---|---|---|---|---|---|---|")
    grand = 0
    for d in range(10, 25):
        row = census['per'][str(d)]; grand += sum(row)
        W(f"| {d} | " + " | ".join(f"{x:,}" for x in row) + f" | {sum(row):,} |")
    W(f"| **all** | | | | | | **{grand:,}** |\n")
    W("Coverage: **all columns at every cell of δ = 10, 11, 12** (71,501 cells, `sk` and `a` from the s39 engine table re-verified here); the families F1–F4 of the pre-registration at δ = 13–16 (all columns) and δ = 17–24 (`a`, `N_S`; `sk` pending — session 58); the ℓ = 6 slices below the region (δ = 6–9) for the scoring; every ladder with `|λ̄| ≤ 16` at ℓ = 6–10 through its stable value `a_∞`.  Everything else is pending.\n")
    # ---- 2 per-chunk summary
    W("## 2. δ = 10–12, every cell: chunk summary\n")
    W("`a≥1` = cells with a highest-weight vector; `units` = Σa; `LemmaA` = `h_pad = 0` (mult_pad = 0, D ≤ 0, excluded from ranking); `pad-forced` = `0 < h_pad < a` (i_pad ≥ a − h_pad forced); transport statuses from Lemma L against the 326-cell negative record; reach by `n_χ~` (dense ≤ 20,000, sparse ≤ 120,000, else beyond; `N_S` exact or a lower bound).\n")
    W("| δ | ℓ | cells | a≥1 | units | LemmaA dead | pad-forced | dead by transport | bounded | unconstrained | dense | sparse | beyond | N_S exact |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for key in sorted(pub['summary'], key=lambda k: (int(k.split('|')[0]), int(k.split('|')[1]))):
        d, e = key.split('|'); s = pub['summary'][key]
        W(f"| {d} | {e} | {s['cells']:,} | {s['a1']:,} | {s['units']:,} | {s['lemmaA']:,} | {s['padf']:,} | {s['dbt']} | {s['bounded']} | {s['unc']:,} | {s['dense']:,} | {s['sparse']:,} | {s['beyond']:,} | {s['exact']:,} |")
    W("\nPer-cell files: `results/s57_cells/table_d{δ}_l{ℓ}.csv.gz` (columns: delta, ell, lam, tail, a, sk, h_pad, bal, stab, N_S, N_S_status, nchi_est, reach, pad_forced, lemmaA_dead, transport, room, a_inf, stable_bound, perm_dead_ladder).\n")
    # ---- 3 families
    W("## 3. The families above δ = 12\n")
    W("### 3.1 F1 — the LMR ladder, tail `(17, 2^7)`, ℓ = 9\n")
    W("`a_∞((17,2^7)) = 274` (Proposition S).  `forced` = the kernel forced at that degree by the LMR equation at δ = 24 through Lemma L (`≥ 1 − [a(24) − a(δ)]`).\n")
    W("| δ | λ | a (engine / Weyl) | sk | h_pad | pad-forced | N_S | n_χ~ | forced kernel |\n|---|---|---|---|---|---|---|---|---|")
    lmr_rows = []
    for d in range(12, 25):
        lam = ladder_cell((17,) + (2,) * 7, d)
        r = fam.get((lam, d))
        if not r:
            W(f"| {d} | {L(lam)} | pending | pending | pending | | pending | | |"); continue
        a24 = fam.get((ladder_cell((17,) + (2,) * 7, 24), 24), {}).get('a')
        forced = (max(0, 1 - (a24 - r['a'])) if (a24 is not None and r['a'] is not None) else None)
        lmr_rows.append((d, r['a']))
        W(f"| {d} | {L(lam)} | {fmt(r['a'])} ({fmt(r['a_engine'])} / {fmt(r['a_weyl'])}) | {fmt(r['sk'])} | {fmt(r['h_pad'])} | {fmt(r['pad_forced'])} | {fmt(r['N_S'])}{'' if r['N_S_status']=='exact' else ' (lb)'} | {fmt(r['nchi_est'])} | {fmt(forced) if forced is not None else ''} |")
    W("")
    W("### 3.2 F2 — the peaked ladders `(4δ − 2(ℓ−1), 2^{ℓ−1})`\n")
    W("Dead at every δ ≥ ℓ by Theorem P (report §1): `a = a_∞ = 1`, the unique highest-weight vector is the bordered discriminant, nonzero at a generic pencil.  Tabulated values (a, sk constant in δ as s38/s39 found):\n")
    W("| ℓ | a_∞ | sk (δ ≤ 16) | h_pad | n_χ~ at δ = 12 / 16 | K_∞/\\|Stab'\\| |\n|---|---|---|---|---|---|")
    for ell in range(6, 11):
        t = (2,) * (ell - 1)
        vals = {d: fam.get((ladder_cell(t, d), d)) for d in range(12, 25)}
        sks = sorted({v['sk'] for v in vals.values() if v and v['sk'] is not None})
        hps = sorted({v['h_pad'] for v in vals.values() if v and v['h_pad'] is not None})
        n12 = vals.get(12) and vals[12]['nchi_est']; n16 = vals.get(16) and vals[16]['nchi_est']
        sl = next((r for r in short if tuple(r['tail']) == t), None)
        W(f"| {ell} | {stable.get(t)} | {sks} | {hps} | {fmt(n12)} / {fmt(n16)} | {sl['K_inf_over_stab'] if sl else ''} |")
    W("")
    W("### 3.3 F3 — the LMR shapes at the other lengths, `λ(k,4) = (8k+17, 2k+5, 2^{k+1})` and their ladders\n")
    W("| k | ℓ | tail | a_∞ | threshold | LMR cell (δ) | a profile (δ: a) | sk profile | h_pad profile | n_χ~ at the lowest tabulated δ |\n|---|---|---|---|---|---|---|---|---|---|")
    for k in (3, 4, 5, 6, 7):
        lam_k, d_k = lmr_weight(k); t = tail_of(lam_k)
        prof = [(d, fam[(ladder_cell(t, d), d)]) for d in range(10, 25) if (ladder_cell(t, d), d) in fam]
        ap = ", ".join(f"{d}:{r['a']}" for d, r in prof if r['a'] is not None)
        sp = ", ".join(f"{d}:{r['sk']}" for d, r in prof if r['sk'] is not None)
        hp = ", ".join(f"{d}:{r['h_pad']}" for d, r in prof if r['h_pad'] is not None)
        n0 = next((f"{d}: {r['nchi_est']:,}" for d, r in prof if r['nchi_est'] is not None), '')
        W(f"| {k} | {len(lam_k)} | {L(t)} | {stable.get(t)} | δ ≥ {sum(t)} | {L(lam_k)} ({d_k}) | {ap} | {sp} | {hp} | {n0} |")
    W("")
    W("### 3.4 F4 — the most balanced eligible cells (δ = 13–16, as far as the run reached)\n")
    W("| δ | ℓ | λ | bal | a | sk | h_pad | pad-forced | N_S (lb) | n_χ~ |\n|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted([r for r in pub['families'] if (r['family'] or '').startswith('F4')], key=lambda r: (r['delta'], r['ell'], r['lam'])):
        W(f"| {r['delta']} | {r['ell']} | `{r['lam']}` | {r['bal']} | {fmt(r['a'])} | {fmt(r['sk'])} | {fmt(r['h_pad'])} | {fmt(r['pad_forced'])} | {fmt(r['N_S'])} | {fmt(r['nchi_est'])} |")
    W("")
    # ---- 4 ladders
    W("## 4. Ladders: what the record already decides (Lemma L + Proposition S)\n")
    imp = ladder['implied']
    W(f"**Record cells implied by a lower cell of their ladder with equal `a`:** {len(imp)} of 326 ({sum(1 for x in imp if len(x['lam'])==6)} of the 210 six-row cells, {sum(1 for x in imp if len(x['lam'])==5)} of the 116 length-5 cells).\n")
    RL = ladder['record_ladders']
    perm = [r for r in RL if r['permanently_dead']]; roomy = [r for r in RL if not r['permanently_dead']]
    W(f"**Six-row ladders touched by the record:** {len(RL)}; **permanently dead** (a measured cell has `a = a_∞`, so `i_det = 0` on the whole ladder and `I(M_6)` has no component of that tail): {len(perm)}; with room above: {len(roomy)}.\n")
    W("Permanently dead tails: " + ", ".join(L(r['tail']) + f"(a_∞={r['a_inf']}, at δ={r['top_dead'][0]})" for r in sorted(perm, key=lambda r: (r['a_inf'], r['tail']))) + "\n")
    W("### 4.1 The next-room cells of the 66 ladders with room\n")
    W("The first cell above the highest dead cell where `a` grows; `new room` = the number of highest-weight vectors not obtained from below by transport — the only ones that can vanish on `D_6`.  A dead verdict at a cell with `a = a_∞` closes the ladder permanently.\n")
    W("| tail | a_∞ | top dead (δ, a) | next-room cell | δ | a | new room | stable there? | h_pad | pad-forced | n_χ~ | reach |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
    below = {(tuple(int(x) for x in r['lam'].strip('()').split(',')), r['delta']): r for r in pub.get('below', [])}
    tab = {}
    for p in glob.glob(os.path.join(CELLS, 'bank_d*_l*.jsonl')):
        for ln in open(p):
            r = json.loads(ln); tab[(tuple(r['lam']), r['delta'])] = r
    def cellinfo(lam, d):
        r = tab.get((lam, d)) or below.get((lam, d))
        return r or {}
    rows = []
    for r in roomy:
        n = r.get('next_room_cell')
        if not n: continue
        ci = cellinfo(tuple(n['lam']), n['delta'])
        rows.append((n['new_room'], ci.get('nchi_est') or 10**12, r, n, ci))
    rows.sort(key=lambda x: (x[0], x[1]))
    for nr, _, r, n, ci in rows:
        W(f"| {L(r['tail'])} | {r['a_inf']} | ({r['top_dead'][0]}, {r['top_dead'][1]}) | {L(n['lam'])} | {n['delta']} | {n['a']} | {nr} | {'yes' if n['a']==r['a_inf'] else 'no'} | {fmt(ci.get('h_pad'))} | {fmt(ci.get('pad_forced'))} | {fmt(ci.get('nchi_est'))}{'' if ci.get('N_S_status')=='exact' else ' (lb)'} | {ci.get('reach','')} |")
    W("")
    # ---- 5 short ladders
    W("## 5. The short ladders: every tail with `|λ̄| ≤ 16` and `a_∞ ≥ 1`, ℓ = 6–10\n")
    W("A ladder is tested completely by any cell where `a = a_∞`; the *first stable region cell* is the cheapest such cell at δ ≥ 10 (the first observed `a = a_∞`, or the bound `|λ̄|`).  `K_∞/|Stab'|` is the size of the same computation done on the slice `Z` (report §1).  Tails with `a_∞ = 0` carry no highest-weight vector at any degree and are omitted (counts given).\n")
    for ell in range(6, 11):
        rows = [r for r in short if r['ell'] == ell]
        live = [r for r in rows if r['a_inf'] >= 1]
        pd = [r for r in live if r['permanently_dead']]
        W(f"### ℓ = {ell}: {len(rows)} tails with |λ̄| ≤ 16, {len(live)} with a_∞ ≥ 1, {len(pd)} permanently dead, {len(live) - len(pd)} open\n")
        if not live: continue
        W("| tail | \\|λ̄\\| | a_∞ | record cells (δ:a, * dead) | permanently dead | first stable region cell | δ | a | sk | h_pad | n_χ~ | reach | K_∞/\\|Stab'\\| |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in sorted(live, key=lambda r: (r['permanently_dead'], r['first_region_stable']['nchi_est'] or 10**12)):
            f = r['first_region_stable']
            rc = ", ".join(f"{c['delta']}:{c['a'] if c['a'] is not None else '?'}{'*' if c['dead'] else ''}" for c in r['cells'] if c['delta'] <= 12 and (c['dead'] or c['a']))
            ci = cellinfo(tuple(f['lam']), f['delta']) if f['lam'] else {}
            W(f"| {L(r['tail'])} | {r['size']} | {r['a_inf']} | {rc} | {'yes (δ=' + str(r['perm_dead_at']) + ')' if r['permanently_dead'] else 'no'} | {L(f['lam']) if f['lam'] else '-'} | {f['delta']} | {fmt(f['a'])} | {fmt(f['sk'])} | {fmt(ci.get('h_pad'))} | {fmt(f['nchi_est'])}{'' if f['N_S_status']=='exact' else ' (lb)'} | {(f['reach'] or '').rstrip('?')} | {r['K_inf_over_stab']:,} |")
        W("")
    # ---- 6 criteria scores
    W("## 6. The criteria against the negative record (Task 3)\n")
    dp = fals['dead_percentiles']
    W("Percentile of each dead cell in its `(δ, ℓ)` slice under the criterion's ordering (0 = the criterion's first nominee).  324 eligible dead cells scored (the two onset-only ones, `(4^6)_6` and `(6,6,6,6,2,2)_7`, are outside every eligible slice).\n")
    W("| criterion | ordering | dead cells: min | q1 | median | q3 | max | in first quartile | in first decile | ranked first in slice |\n|---|---|---|---|---|---|---|---|---|---|")
    names = {'K1': 'balance, ascending λ_1 − λ_ℓ', 'K2': 'closeness, ascending sk/a', 'K3': 'LMR shape, ascending tail distance'}
    for k in ('K1', 'K2', 'K3'):
        v = dp[k]
        W(f"| {k} | {names[k]} | {v['min']:.3f} | {v['q1']:.3f} | {v['median']:.3f} | {v['q3']:.3f} | {v['max']:.3f} | {100*v['frac_first_quartile']:.0f}% | {100*v['frac_first_decile']:.0f}% | {100*v['frac_top_cell']:.1f}% |")
    lm = fals['lmr']
    W(f"\nThe one known live cell, {L(lm['lam'])} at δ = 24 (ℓ = 9): balance {lm['bal']} in a slice whose balances run {lm['min_balance']}–{lm['max_balance']}; K1 percentile {lm['K1_percentile']:.4f} (rank {lm['K1_rank']:,} of {lm['slice_size']:,}; only {lm['n_more_skewed']:,} cells are more skewed); K3 percentile 0 by construction; K2: `sk` pending, but `sk ≥ sk(δ=16)` by transport and `sk/a` is in the hundreds on the ladder.\n")
    W("### 6.1 Per slice: the first nominee of each criterion, and its status\n")
    W("| (δ, ℓ) | slice | dead | K1 first (balance) | dead? | K2 first (sk/a) | dead? | K3 first | dead? | dead among 5 most balanced |\n|---|---|---|---|---|---|---|---|---|---|")
    for key in sorted(fals['slices'], key=lambda k: (int(k.split('|')[1]), int(k.split('|')[0]))):
        s = fals['slices'][key]; d, e = key.split('|')
        if int(d) > 12: continue
        W(f"| ({d}, {e}) | {s['size']:,} | {s['dead']} | {L(s['K1']['first'][0])} ({s['K1']['first_value'][0]}) | {fmt(s['K1']['first_dead'][0])} | {L(s['K2']['first'][0])} ({s['K2']['first_value'][0]:.0f}) | {fmt(s['K2']['first_dead'][0])} | {L(s['K3']['first'][0])} | {fmt(s['K3']['first_dead'][0])} | {s['balanced5_dead']} |")
    W("")
    # ---- 7 verification
    if verify:
        W("## 7. Verification runs (`analysis/wk9_s57_verify.py`, `results/s57_cells/verify.json`)\n")
        v = verify
        if 'V1a' in v: W(f"- V1a: `a` at all {v['V1a']['cells']:,} cells of (δ, ℓ) = (10, 6) recomputed by the modular Weyl route: {len(v['V1a']['disagreements'])} disagreements with the s39 table.")
        if 'V1b' in v:
            cov = ", ".join("(" + k.replace("|", ", ") + "): " + str(n) for k, n in sorted(v['V1b'].get('coverage', {}).items()))
            W(f"- V1b: a sample of {v['V1b']['cells']} cells across the other chunks (by (δ, ℓ): {cov}; tail box ≤ {v['V1b'].get('box_cap', 0):.0e}): {len(v['V1b']['disagreements'])} disagreements.")
        if 'V2' in v and 'rows' in v['V2']: W(f"- V2: `sk` by the house Python route at {len(v['V2']['rows'])} cells of δ = 10: {'all agree' if v['V2']['all_agree'] else 'DISAGREEMENT'} with the s39 table.")
        if 'V3a' in v: W(f"- V3: `a` non-decreasing up ladders at {v['V3a']['pairs']:,} consecutive pairs on {v['V3a']['ladders']:,} ladders: {len(v['V3a']['violations'])} violations; `h_pad` at {v['V3b']['pairs']:,} pairs: {len(v['V3b']['violations'])} violations.")
        if 'V4' in v: W(f"- V4: `a ≤ a_∞` at {v['V4']['cells']:,} cells with a stable value: {len(v['V4']['violations_le'])} violations; `a = a_∞` at the {v['V4']['stable_cells']:,} of them with δ ≥ |λ̄|: {len(v['V4']['violations_eq'])} violations.")
        if 'V5' in v: W(f"- V5: family cells with both `a` routes: {v['V5']['both']}, disagreements {len(v['V5']['disagreements'])}.")
        if 'V6' in v: W(f"- V6: census counts vs the s39 candidate counts at δ = 10–12: {len(v['V6']['mismatches'])} mismatches.")
        W("")
    open(os.path.join(ROOT, 'results/s57_selector.md'), 'w').write("\n".join(out) + "\n")
    log("written results/s57_selector.md (%d lines)" % len(out))
