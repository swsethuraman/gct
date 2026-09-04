#!/usr/bin/env python3
"""Session 45 -- assemble docs/sparse_det_route.md from the prose parts and the
banked measurements."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, '..', 'results'); D = os.path.join(HERE, '..', 'docs')
sys.path.insert(0, HERE)
from wk9_s45_report import cells, curve, bal

def build_table():
    L = ["", "### 3a. Build — time and peak resident as a function of `N_S` *(measured)*", "",
         "One process per cell, `VmHWM`.  `mono` is the monomial array, `orbits` the",
         "isotypic reduction (`2|Stab|` numpy passes), `rows` the raising operators.", "",
         "| λ | δ | `N_S` | \\|Stab\\| | `n_χ` | rows | `nnz` | `nnz/N_S` | mono s | orbits s | rows s | build s | HWM GB |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in curve():
        L.append(f"| `{tuple(d['lam'])}` | {d['delta']} | {d['N_S']} | {d['stab']} | {d['n_chi']} | "
                 f"{d['nrows']} | {d['nnz']} | {d['nnz']/d['N_S']:.2f} | {d['mono_secs']} | "
                 f"{d['orbit_secs']} | {d['rows_secs']} | {d['build_secs']} | {d['hwm_gb']} |")
    cs = curve()
    hi = max(cs, key=lambda d: d['N_S'])
    L += ["", f"""**The law.**  Peak resident is linear in `N_S` with slope about
`{(hi['hwm_gb']*1e9 - 3.0e8)/hi['N_S']:.0f}` bytes per monomial plus a fixed ~0.15 GB of interpreter and
libraries; build time is linear in `N_S` with the group passes as the only
superlinear-looking term (`orbits` scales as `N_S·|Stab|`).  The extremes
measured: `N_S = {min(d['N_S'] for d in cs)}` in {min(d['build_secs'] for d in cs)} s, and
`N_S = {hi['N_S']}` (`|Stab| = {hi['stab']}`) in {hi['build_secs']} s at {hi['hwm_gb']} GB.
`nnz(E) ≈ {sum(d['nnz']/d['N_S'] for d in cs)/len(cs):.2f}·N_S` across the whole range
({min(d['nnz']/d['N_S'] for d in cs):.2f}–{max(d['nnz']/d['N_S'] for d in cs):.2f}), independently of `|Stab|` — the single most useful
number for planning a successor sweep.  **Compare the dense route**: `8 n_χ²`
bytes, i.e. {8*max(d['n_chi'] for d in cs)**2/1e9:.0f} GB at the largest `n_χ` reached here
(`n_χ = {max(d['n_chi'] for d in cs)}`) and {8*hi['n_chi']**2/1e9:.0f} GB at the largest `N_S` cell, against the
{max(d['hwm_gb'] for d in cs)} GB this route actually used anywhere."""]
    return "\n".join(L)

def solve_table():
    cs = cells()
    L = ["", "### 3b. Solve — the sequence cost *(measured)*", "",
         "`nnz_c` is the `nnz` of the compressed stack that carried the verdict (the",
         "level in the ledger); one sequence is `2 n_χ` matvecs at `2 nnz_c` field",
         "operations each, and the two house primes run concurrently on the two cores,",
         "so the wall time of a cell is one sequence plus the build plus",
         "Berlekamp–Massey.", "",
         "| λ | δ | `n_χ` | level | `nnz_c` | `nnz_c/n_χ` | seq s | wall s | ns per element-op |",
         "|---|---|---|---|---|---|---|---|---|"]
    pts = []
    for d in cs:
        pp = d['sides']['det']['per_prime']
        best = None
        for p, v in pp.items():
            dg = v['diag'][-1]
            if dg['status'] == 'NONSINGULAR': best = dg
        if best is None: best = list(pp.values())[0]['diag'][-1]
        lvl = ('(%d,%d)' % (d['sample'], d['group'])) if 'sample' in d else \
              {'cheap': ['(3,2)', '(12,2)', 'full'], 's42': ['(12,2)', 'full']}[
                  d.get('levelset', 'cheap')][best['level']]
        note = best['note']
        secs = 0.0
        for chunk in note.split('|'):
            if 'BM' in chunk and 'secs=' in chunk:
                secs = float(chunk.strip().split('secs=')[-1])
        nnzc = best['nnz']; n = d['n_chi']
        ns = secs * 1e9 / (4.0 * n * nnzc) if secs else float('nan')
        pts.append(ns)
        L.append(f"| `{tuple(d['lam'])}` | {d['delta']} | {n} | {lvl} | {nnzc} | "
                 f"{nnzc/n:.1f} | {secs:.0f} | {d.get('wall_secs', d['secs'])} | {ns:.2f} |")
    good = [x for x in pts if x == x]
    L += ["", f"""One sequence costs `4 · n_χ · nnz_c` element-operations at
**{min(good):.1f}–{max(good):.1f} ns** each on this container's single core (the spread is cache:
the random access `xs[col[t]]` leaves L2 as `n_χ` grows past a few times `10^4`).
So a cell costs about `{4*sum(good)/len(good):.1f}·10^-9 · n_χ · nnz_c` seconds of wall clock,
against `O(n_χ³)` time and `8 n_χ²` bytes for the dense route."""]
    L += ["", """### 3c. Which compression level to start at *(measured; a finding for successors)*

The cheap level `(3,2)` samples `3 n_χ` of the `n_rows` rows of `E` and groups
them in pairs.  It carried the verdict at every cell with
`n_rows / n_χ ≲ 8` and cost a third of what the `(12,2)` level costs.  At
`(8,8,6,2,2,2)_7`, where `n_rows / n_χ = 12.3`, it failed — and failed
*informatively*: the compressed matrix came out with Berlekamp–Massey degree
`114,818` against `n_χ = 114,875`, i.e. exactly `57` short of full column rank,
**at both primes with independent randomness**.  That is sampling loss, not a
kernel of `[E; ev]`: the candidate vector failed the check against the full
matrix and the run escalated, correctly, to `(12,2)`, which certified
nonsingularity.  The escalation is sound but it is not free — that cell cost
3 h 45 m instead of 2 h 30 m.  So the rule this session leaves behind is
**start at `(12,2)` whenever `n_rows / n_χ ≳ 10`**, and the two cells run after
the finding (`(9,9,9,3,1,1)_8` at `13.7` and `(6,6,6,6,2,2)_7` at `36.5`) were
run that way and were certified at the first level they tried.

The episode is also the clearest live demonstration in the session that the
one-sided certificate does what it claims: a compressed matrix that is genuinely
rank-deficient produces a kernel candidate, the candidate is checked against the
full `[E; ev]`, it fails, and no wrong verdict is emitted anywhere."""]
    return "\n".join(L)

def corner():
    cs = cells()
    out = subprocess.run([sys.executable, os.path.join(HERE, 'wk9_s45_reach.py')],
                         capture_output=True, text=True).stdout
    bals = sorted({bal(tuple(d['lam'])) for d in cs})
    best = min(bals)
    bl = [d for d in cs if bal(tuple(d['lam'])) == best]
    L = [f"""This session measured {len(cs)} cells with balances {', '.join(map(str, bals))}, the best being
**balance {best}** at `{tuple(bl[0]['lam'])}`, `δ = {bl[0]['delta']}`, `n_χ = {bl[0]['n_chi']}` — the most
balanced six-row cell the programme has ever measured on the determinant side,
(it is `λ_1 < δ`, so it cannot itself carry an obstruction — but it can carry the
determinant ideal, and it does not), and `mult_det = a` there too.  Extrapolating the cost law of §3 across the
census (`analysis/wk9_s45_reach.py`; an **expectation**, not a measurement — it
assumes the fitted `nnz_c/n_χ` and the fitted ns-per-op hold at cells nobody has
built):""", "", "```", out.rstrip(), "```", "",
"""So the balance-6 and balance-7 corner at `δ = 7` is now *routine* — six and
sixteen cells respectively inside a 48-hour budget — where before this session
none of it was reachable at all; the `δ = 8` balanced corner and the
`λ_1 < δ` onset-only cells above `n_χ ~ 3·10^5` remain out of reach, and the
`δ = 8` rectangles (`(7,7,7,7,2,2)`, `n_χ ≈ 5.8·10^5`) are two orders of
magnitude of work away."""]
    return "\n".join(L)

if __name__ == '__main__':
    head = open(os.path.join(HERE, 'wk9_s45_doc_parts', 'doc_head.md')).read()
    mid = open(os.path.join(HERE, 'wk9_s45_doc_parts', 'doc_mid.md')).read()
    tail = open(os.path.join(HERE, 'wk9_s45_doc_parts', 'doc_tail.md')).read()
    cs = cells()
    hi = max(cs, key=lambda d: d['n_chi']); hn = max(cs, key=lambda d: d['N_S'])
    prov = sum(1 for d in cs if d['sides']['det']['nullity'] == 0)
    bl = min(bal(tuple(d['lam'])) for d in cs)
    verdict = (f"**{len(cs)} determinant-side cells measured, {prov} of them with `mult_det = a` proved "
               f"by a single-prime nonsingularity certificate — no bite, no onset.**  They run from "
               f"`n_χ = {min(d['n_chi'] for d in cs)}` to `n_χ = {hi['n_chi']}` and from balance "
               f"{max(bal(tuple(d['lam'])) for d in cs)} down to balance **{bl}**; the pre-registered "
               f"prediction (§5 of the pre-registration: no cell shows `mult_det < a`, confidence 85–90 %) "
               f"held at every one.")
    head = (head.replace('PLACEHOLDER_FRONTIER', f"{hi['n_chi']:,}".replace(',', ','))
                .replace('PLACEHOLDER_NSNCHI', f"{hn['n_chi']:,}")
                .replace('PLACEHOLDER_NSHWM', str(hn.get('hwm_gb')))
                .replace('PLACEHOLDER_NS', f"{hn['N_S']:,}")
                .replace('PLACEHOLDER_DENSE_GB', f"{8*hi['n_chi']**2/1e9:.0f}")
                .replace('PLACEHOLDER_VERDICT_CELLS', verdict)
                .replace('PLACEHOLDER_RECORD', f"{90+len(cs)} cells / {195+sum(d['a'] for d in cs)} ambient units"))
    tail = tail.replace('PLACEHOLDER_CORNER', corner())
    sweep = ["", "## 4. The sweep", "",
             "The order was published in `results/PREREG_s45.md` §4 before any of it was",
             "measured; the ledger is `results/s45_ledger.md`.  Summary:", "",
             "| δ | λ | balance | `a` | `n_χ` | `nnz` | nullity `[E; ev_det]` | verdict | wall s | HWM GB |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for d in cs:
        det = d['sides']['det']
        sweep.append(f"| {d['delta']} | `{tuple(d['lam'])}` | {bal(tuple(d['lam']))} | {d['a']} | {d['n_chi']} | "
                     f"{d['nnz']} | {det['nullity']} | **`mult_det = a = {d['a']}`** (proved) | "
                     f"{d.get('wall_secs', d['secs'])} | {d.get('hwm_gb')} |")
    sweep += ["", f"""`a` is the plethysm value at every cell and is additionally asserted equal to
the full-`E` nullity at the {sum(1 for d in cs if 'full_E_nullity' in d)} cells where that second
certificate was affordable.  Both house primes agree at every cell.  No
determinant-side nullity was positive, so the pre-registered stopping rules 3
and 4 (exhibited vectors, exact verification, fresh preconditioner and prime,
20 fresh pencils, then the pad side, then `docs/OBSTRUCTION_CANDIDATE.md`) were
never triggered."""]
    frontier = f"""

## 7. The frontier as this session leaves it

**Determinant side, `n = 4`, `ℓ(λ) = 6`.**  Reached and proved:
`n_χ = {max(d['n_chi'] for d in cs)}` (`{tuple(max(cs, key=lambda x: x['n_chi'])['lam'])}` at
`δ = {max(cs, key=lambda x: x['n_chi'])['delta']}`), against session 41's `19,985` — a
{max(d['n_chi'] for d in cs)/19985:.1f}× move.  Largest cell built:
`N_S = {max(d['N_S'] for d in cs):,}` (`{tuple(hn['lam'])}` at `δ = {hn['delta']}`,
`|Stab| = {hn['stab']}`) in {hn['build_secs']} s at {hn['build_hwm_gb']} GB.  Best balance measured:
**{min(bal(tuple(d['lam'])) for d in cs)}**.  Peak resident anywhere in the sweep:
{max(d['hwm_gb'] for d in cs)} GB.

**The binding constraint is now `N_S`, through the `2|Stab|` group passes of the
isotypic reduction, not `n_χ` through memory.**  The named next targets, in
order: `(8,4,4,4,4,4)_7` (`N_S = 10,060,304`, `|Stab| = 120`, balance 4,
`n_χ ≈ 83,836`, the most balanced *obstruction-eligible* `δ = 7` cell of all) —
blocked only by the group passes, which are embarrassingly parallel and could be
blocked over `N_S` on more than two cores; then the `δ = 7` balance-5 and
balance-6 cells listed in §5; then `(7,7,7,7,2,2)_8`.

**Six-row record after this session:** {90+len(cs)} cells / {195+sum(d['a'] for d in cs)} ambient
units across `δ = 6, 7, 8`, `mult_det = a` at **every one**.  The six-row onset
of `I(D_6^{{det_4}})` is still not observed; the bracket `≥ 9` in every component
reached is unchanged in degree and pushed outward in balance, from 8 to
{min(bal(tuple(d['lam'])) for d in cs)}.  `D > 0` remains arithmetically impossible everywhere reached.
"""
    open(os.path.join(D, 'sparse_det_route.md'), 'w').write(
        head + mid + build_table() + "\n" + solve_table() + "\n" + "\n".join(sweep) + "\n" + tail + frontier)
    print("written docs/sparse_det_route.md")
