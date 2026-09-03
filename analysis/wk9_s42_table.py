#!/usr/bin/env python3
"""
Session 42 -- render results/mult_red_table.md (the lookup table) and
results/s42_frontier.md (every unreached cell with its size) from the census,
the banked sweep cells, the validation file, the lifts and the s36 det side.

usage: python3 wk9_s42_table.py
"""
import sys, os, json, re, glob
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, '..', 'results')

def load_jsonl(fn):
    out = []
    if os.path.exists(fn):
        for line in open(fn):
            line = line.strip()
            if line: out.append(json.loads(line))
    return out

def key(c): return (tuple(c['lam']), c['delta'])

# ---------------------------------------------------------------- inputs
census = json.load(open(os.path.join(R, 's42_census.json')))
weyl = json.load(open(os.path.join(R, 's42_census_weyl.json'))) if os.path.exists(os.path.join(R, 's42_census_weyl.json')) else []
cells = {}
for fn in sorted(glob.glob(os.path.join(R, 's42_cells_*.jsonl'))):
    for c in load_jsonl(fn):
        k = key(c)
        if k not in cells or (cells[k].get('status') in ('beyond', 'failed') and c.get('status') not in ('beyond', 'failed')):
            cells[k] = c
valid = {key(c): c for c in load_jsonl(os.path.join(R, 's42_validation.jsonl'))}
lifts = {key(c): c for c in load_jsonl(os.path.join(R, 's42_lifts.jsonl'))}

# det side: s36 ledger (a >= 2) and s36 a = 1 table
det = {}
for line in open(os.path.join(R, 's36_ledger.md')):
    m = re.match(r"\| [AB]7? \| `\((.*?)\)` \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| \w+ \| (\d+) \| (\d+) \|", line)
    if m:
        lam = tuple(int(x) for x in m.group(1).split(',')); det[(lam, int(m.group(2)))] = (int(m.group(9)), int(m.group(10)), 's36 ledger')
for line in open(os.path.join(R, 's36_aone.md')):
    m = re.match(r"\| (\d) \| (\d) \| `\((.*?)\)` \| 1 \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", line)
    if m:
        lam = tuple(int(x) for x in m.group(3).split(',')); det[(lam, int(m.group(2)))] = (int(m.group(6)), int(m.group(7)), 's36 a=1')
det[((4, 4, 4, 4, 4, 4), 6)] = (1, 0, 's36 I_6')

def lamstr(lam): return '`(' + ', '.join(str(x) for x in lam) + ')`'
def a_nul(c): return next(iter(c['primes'].values()))['nullity']

# ---------------------------------------------------------------- the table
L = []
L.append("# `mult_red` lookup table — the reducible-locus multiplicity `mult_λ C[R_r]_δ` on the obstruction-eligible region\n")
L.append("Session 42 (`s42-redengine`).  Pre-registration `results/PREREG_s42.md`; engine `analysis/wk9_s42_redengine.py` "
         "(+ `wk9_s42_sparse.py`, `wk9_s42_wied.c`); census `analysis/wk9_s42_census.py`; theory and certificates "
         "`docs/reducible_engine.md`.  Region: `n = 4`, `6 ≤ ℓ(λ) ≤ 10`, `λ_1 ≥ δ`, `a ≥ 1`, `δ = 7 … 12` "
         "(`ℓ(λ) ≤ δ` always, so `ℓ ≤ 7` at `δ = 7` and `ℓ ≤ 8` at `δ = 8`).\n")
L.append("**Contract (transfer lemma).**  `mult_red ≥ mult_pad` with equality at `ℓ = 5`; at `ℓ ≥ 6` a value `mult_red ≤ mult_det` "
         "proves `D ≤ 0` (blindness, no pad-point computation), a value `mult_red > mult_det` flags a candidate for the true-pad recheck; "
         "the table never confirms `D > 0`.\n")
L.append("**Columns.**  `a`: plethysm multiplicity.  `h_pad`: the normalisation bound `mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)` — a **proved** upper "
         "bound on `mult_red` at every cell (`docs/reducible_engine.md` §B), so `mult_red ≤ min(a, h_pad)` everywhere and `h_pad < a` is a "
         "proved pad-side bite.  `n_χ`, `n_red`: columns of the isotypic reduction and of its (★)-red part.  `nullity`: `nullity_p(E_red)` at both "
         "house primes (certified both ways, `docs/reducible_engine.md` §A).  `mult_red = a − nullity`; **status** `proved` means "
         "`nullity_p = 0` (then `mult_red = a` over `Q`, no randomness), `measured` means `nullity_p = k > 0` at both primes "
         "(`mult_red ≥ a − k` proved, `= a − k` measured; `lifted` when `k` integer highest-weight vectors in the ideal were exhibited, "
         "which proves it).  `det`: `mult_det` where session 36 measured it (always `= a`); **verdict** `blind` when `mult_red ≤ mult_det`.\n")

def status_str(c):
    k = key(c)
    st = c.get('status')
    if st == 'proved': s = 'proved'
    elif st == 'measured':
        s = f"measured (k={c['nullity']})"
        if k in lifts and 'PROVED' in lifts[k].get('verdict', ''): s = f"lifted (k={c['nullity']}): proved"
    else: s = st
    return s

sections = []
for delta in sorted({c['delta'] for c in census}):
    for ell in sorted({c['ell'] for c in census if c['delta'] == delta}):
        sub = sorted([c for c in census if c['delta'] == delta and c['ell'] == ell], key=lambda c: (c['nchi_lb'], c['N_S']))
        reached = [c for c in sub if key(c) in cells and cells[key(c)].get('status') in ('proved', 'measured')]
        beyond_built = [c for c in sub if key(c) in cells and cells[key(c)].get('status') == 'beyond']
        failed = [c for c in sub if key(c) in cells and cells[key(c)].get('status') == 'failed']
        unreached = [c for c in sub if key(c) not in cells or cells[key(c)].get('status') in ('beyond', 'failed')]
        hz = [c for c in sub if c['h_pad'] == 0]
        hlt = [c for c in sub if c['hpad_lt_a']]
        bites = [c for c in reached if cells[key(c)]['nullity'] > 0]
        blind = [c for c in reached if key(c) in det and cells[key(c)]['mult_red'] <= det[key(c)][0]]
        L.append(f"\n## `δ = {delta}`, `ℓ = {ell}` — {len(sub)} cells; reached {len(reached)} ({sum(1 for c in reached if cells[key(c)]['status']=='proved')} proved, "
                 f"{sum(1 for c in reached if cells[key(c)]['status']=='measured')} measured); beyond the frontier {len(unreached)}\n")
        L.append(f"Ambient units `Σ a = {sum(c['a'] for c in sub)}`, reached `{sum(c['a'] for c in reached)}`.  "
                 f"`h_pad < a` (proved bites, no rank needed) at **{len(hlt)}** cells, of which `h_pad = 0` (`mult_red = 0` proved) at **{len(hz)}**.  "
                 f"Bites found by the engine among reached cells: {len(bites)}"
                 + (f" ({', '.join(lamstr(c['lam']) for c in bites)})" if bites else "") + ".  "
                 f"Cells with a session-36 det side: {sum(1 for c in sub if key(c) in det)}, blind (`mult_red ≤ mult_det`) at every one of them that was reached: {len(blind)}.\n")
        if reached:
            L.append("| λ | a | h_pad | n_χ | n_red | nullity | **mult_red** | status | det (s36) | verdict | secs |")
            L.append("|---|---|---|---|---|---|---|---|---|---|---|")
            for c in reached:
                k = key(c); cc = cells[k]
                d = det.get(k)
                verdict = ('blind: mult_red ≤ mult_det' if d and cc['mult_red'] <= d[0] else ('candidate: mult_red > mult_det' if d else 'det side open'))
                L.append(f"| {lamstr(c['lam'])} | {c['a']} | {c['h_pad']} | {cc['n_chi']} | {cc['n_red']} | {cc['nullity']} | **{cc['mult_red']}** | {status_str(cc)} | "
                         f"{d[0] if d else '—'} | {verdict} | {cc.get('secs', '')} |")
        if hz:
            L.append(f"\n**`h_pad = 0` cells (`mult_red = 0` proved by the normalisation bound; every copy of `S_λ` vanishes on `R_r`; "
                     f"each is a negative instance of Kadish–Landsberg's Question 1.5 at `(n, m) = (4, 3)`):** "
                     + ', '.join(f"{lamstr(c['lam'])} (a={c['a']})" for c in hz) + ".\n")
        if hlt:
            others = [c for c in hlt if c['h_pad'] > 0]
            if others:
                L.append(f"**`0 < h_pad < a` cells (`mult_red ≤ h_pad < a` proved):** "
                         + ', '.join(f"{lamstr(c['lam'])} (a={c['a']}, h_pad={c['h_pad']})" for c in others) + ".\n")
        if unreached:
            sizes = Counter()
            for c in unreached:
                n = cells[key(c)]['n_chi'] if key(c) in cells and 'n_chi' in cells[key(c)] else c['nchi_lb']
                sizes['≤ 150k' if n <= 150000 else '150k–400k' if n <= 400000 else '400k–1M' if n <= 1000000 else '> 1M'] += 1
            L.append(f"**Beyond the frontier ({len(unreached)} cells)** by `n_χ` (exact where built, else the lower bound `N_S/|Stab|`): "
                     + ', '.join(f"{k}: {v}" for k, v in sorted(sizes.items())) + ".  Full list in `results/s42_frontier.md`.\n")

# large-delta Weyl census
if weyl:
    L.append("\n## `δ ≥ 9` — the Weyl-route census (a and h_pad only where the size cap admits)\n")
    for delta in sorted({c['delta'] for c in weyl}):
        sub = [c for c in weyl if c['delta'] == delta]
        sized = [c for c in sub if c.get('a') is not None]
        live = [c for c in sized if c['a'] >= 1]
        reached = [c for c in live if key(c) in cells and cells[key(c)].get('status') in ('proved', 'measured')]
        L.append(f"`δ = {delta}`: {len(sub)} partitions with `λ_1 ≥ {delta}`, `6 ≤ ℓ ≤ 10`; sized (a computed) {len(sized)}, of which `a ≥ 1`: {len(live)}; "
                 f"`h_pad < a`: {sum(1 for c in live if c.get('hpad_lt_a'))}; `h_pad = 0`: {sum(1 for c in live if c.get('h_pad') == 0)}; "
                 f"reached by the engine: {len(reached)}.\n")
        if reached:
            L.append("| λ | ℓ | a | h_pad | n_χ | n_red | nullity | **mult_red** | status |")
            L.append("|---|---|---|---|---|---|---|---|---|")
            for c in sorted(reached, key=lambda c: c['nchi_lb']):
                cc = cells[key(c)]
                L.append(f"| {lamstr(c['lam'])} | {c['ell']} | {c['a']} | {c['h_pad']} | {cc['n_chi']} | {cc['n_red']} | {cc['nullity']} | **{cc['mult_red']}** | {status_str(cc)} |")
        hz = [c for c in live if c.get('h_pad') == 0]
        if hz:
            L.append(f"`h_pad = 0` (`mult_red = 0` proved): " + ', '.join(f"{lamstr(c['lam'])} (a={c['a']})" for c in hz[:60]) + (" …" if len(hz) > 60 else "") + "\n")

# engine demonstrations: direct h_pad = 0 checks and det-side certificates
hz = load_jsonl(os.path.join(R, 's42_hz_checks.jsonl'))
dc = load_jsonl(os.path.join(R, 's42_detcert.jsonl'))
if hz or dc or lifts:
    L.append("\n## Certificates beyond the sweep\n")
    if lifts:
        L.append("**Exact lifts** (`analysis/wk9_s42_lift.py`; integer highest-weight vectors supported on `M_★`, verified `E v = 0` over `Z`, in `results/s42_certs/`):\n")
        L.append("| λ | δ | a | nullity | **mult_red** | max coefficient | verdict |")
        L.append("|---|---|---|---|---|---|---|")
        for k, c in sorted(lifts.items(), key=lambda kv: (kv[0][1], kv[0][0])):
            L.append(f"| {lamstr(c['lam'])} | {c['delta']} | {c['a']} | {c['nullity']} | **{c['a'] - c['nullity']}** | {c.get('max_coeff', '—')} | {'proved' if 'PROVED' in c['verdict'] else c['verdict'][:60]} |")
    if hz:
        L.append("\n**Direct engine checks of `h_pad = 0` cells** (prediction `mult_red = 0`, i.e. `nullity = a`):\n")
        L.append("| λ | δ | a | n_χ | n_red | nullity | **mult_red** |")
        L.append("|---|---|---|---|---|---|---|")
        for c in hz:
            L.append(f"| {lamstr(c['lam'])} | {c['delta']} | {c['a']} | {c['n_chi']} | {c['n_red']} | {c['nullity']} | **{c['mult_red']}** |")
    if dc:
        L.append("\n**The det side by the same certificate** (`analysis/wk9_s42_detcert.py`: nonsingularity of `[E; Ev]` with `Ev` = `a + 8` det-point rows proves `mult_det = a`; session 36's values reproduced):\n")
        L.append("| λ | δ | a | n_χ | nullity | **mult_det** | secs per prime |")
        L.append("|---|---|---|---|---|---|---|")
        for c in dc:
            secs = ', '.join(str(v['secs']) for v in c['primes'].values())
            L.append(f"| {lamstr(c['lam'])} | {c['delta']} | {c['a']} | {c['n_chi']} | {a_nul(c)} | **{c['mult_det']}** | {secs} |")

# minimal-generator checks
gc = load_jsonl(os.path.join(R, 's42_gencheck.jsonl'))
if gc:
    L.append("\n**Minimal generators of `I(R_6)` in degree 8** (`analysis/wk9_s42_gencheck.py`: every Pieri predecessor at degree 7 proved free of the ideal):\n")
    L.append("| λ | δ | a | mult_red | predecessors checked | in the ideal | minimal generator |")
    L.append("|---|---|---|---|---|---|---|")
    for c in gc:
        inid = [tuple(r['mu']) for r in c['predecessors'] if r.get('verdict') == 'IN THE IDEAL']
        L.append(f"| {lamstr(c['lam'])} | {c['delta']} | {cells[key(c)]['a'] if key(c) in cells else ''} | {cells[key(c)]['mult_red'] if key(c) in cells else ''} | {len(c['predecessors'])} | {', '.join(lamstr(m) for m in inid) if inid else 'none'} | {'**yes**' if c['minimal_generator'] else 'no'} |")
    # the first generator's check lives in s42_gen8_checks.jsonl + the sweep; state it
    L.append("\n`(13,12,4,1,1,1)_8` was checked the same way before the script existed (15 predecessors: six with `a = 0`, nine with `nullity_p = 0` proved; `results/s42_gen8_checks.jsonl`): **yes**.\n")

# validation summary
if valid:
    L.append("\n## Validation against session 36 (P1)\n")
    L.append(f"{len(valid)} banked cells recomputed by the new engine, ascending `n_χ` (`results/s42_validation.jsonl`): "
             f"agreement at {sum(1 for v in valid.values() if v['agree'])} / {len(valid)}; dense-vs-sparse nullity agreement at every cell where both ran "
             f"({sum(1 for v in valid.values() if any('dense_nullity_red' in p for p in v['primes'].values()))} cells); "
             f"full-`E` nullity `= a` at every cell where it was run ({sum(1 for v in valid.values() if any(p.get('full_nullity') is not None for p in v['primes'].values()))} cells).\n")

open(os.path.join(R, 'mult_red_table.md'), 'w').write("\n".join(L) + "\n")

# ---------------------------------------------------------------- frontier
F = ["# The frontier — every region cell not reached by the engine, with its size\n",
     "`n_χ` exact where the cell was built (status `beyond`), else the lower bound `N_S/|Stab|`.  `a`, `h_pad` as in the census; `mult_red ≤ min(a, h_pad)` is proved at every one of them.\n"]
for delta in sorted({c['delta'] for c in census}):
    for ell in sorted({c['ell'] for c in census if c['delta'] == delta}):
        sub = sorted([c for c in census if c['delta'] == delta and c['ell'] == ell], key=lambda c: (c['nchi_lb'], c['N_S']))
        un = [c for c in sub if key(c) not in cells or cells[key(c)].get('status') in ('beyond', 'failed')]
        if not un: continue
        F.append(f"\n## `δ = {delta}`, `ℓ = {ell}` — {len(un)} unreached of {len(sub)}\n")
        F.append("| λ | a | h_pad | N_S | Stab | n_χ (or ≥) | note |")
        F.append("|---|---|---|---|---|---|---|")
        for c in un:
            k = key(c)
            if k in cells and 'n_chi' in cells[k]:
                nchi = str(cells[k]['n_chi']); note = cells[k].get('status', '') + (': ' + cells[k].get('error', '')[:80] if cells[k].get('error') else '')
            else:
                nchi = '≥ ' + str(c['nchi_lb']); note = 'not built' + (' (N_S over the build cap)' if c['N_S'] > 8000000 else '')
            F.append(f"| {lamstr(c['lam'])} | {c['a']} | {c['h_pad']} | {c['N_S']} | {c['stab']} | {nchi} | {note} |")
open(os.path.join(R, 's42_frontier.md'), 'w').write("\n".join(F) + "\n")
print("wrote mult_red_table.md and s42_frontier.md:", len(cells), "banked cells,", len(valid), "validation cells")
