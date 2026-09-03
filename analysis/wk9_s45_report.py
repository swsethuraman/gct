#!/usr/bin/env python3
"""Session 45 -- assemble results/s45_ledger.md and the cost curve from the
banked records (results/s45_cells.jsonl, results/s45_buildcurve.jsonl)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, '..', 'results')

def load(p):
    p = os.path.join(R, p)
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

def cells():
    seen = {}
    for d in load('s45_cells.jsonl'):
        seen[(tuple(d['lam']), d['delta'])] = d
    return sorted(seen.values(), key=lambda d: d['n_chi'])

def bal(lam): return lam[0] - lam[-1]

def ledger():
    cs = cells()
    L = []; A = L.append
    A("""# Session 45 ledger — the six-row determinant side by sparse certificate

`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, ascending in `n_χ`, most balanced cell available
at each size — the order published in `results/PREREG_s45.md` §4 before any of
it was measured.  Column `elig` = obstruction-eligible (`λ_1 ≥ δ`, Corollary B
of `docs/reducible_ideal.md`); the one `onset-only` row is the balanced corner
cell `(6,6,6,6,2,2)_7`, which cannot itself carry an obstruction but *can* carry
the determinant ideal, and is the cell the session was built to reach.

**Pipeline.**  The memory-lean build of `analysis/wk9_s45_build.py` (validated
against `wk9_s36_stabred` / `wk9_s42_orbits` at 16 cells, `results/s45_validation.md`
§2): weight-`λ` monomials enumerated as an `int32` array under an exact
feasibility DP, the `χ_λ`-isotypic reduction in two `|Stab|`-passes, the simple
raising operators assembled chunkwise into CSR against a directly enumerated
target basis, the `K = a + 8` evaluation rows contracted to `χ`-coordinates by
numpy.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`, seed 11,
bound 40 — the house points of `wk8_s30_core`.  **Nullity.**  the session-42
Wiedemann certificates (`analysis/wk9_s42_wied.c` through
`analysis/wk9_s42_sparse.py`, unchanged) with the evaluation rows **pinned**
through every compression level (`analysis/wk9_s45_cell.py`), both house primes
`2147483647`, `2147483629` run concurrently.  `a` is always the plethysm value
(`wk8_s30_pleth`), asserted equal to the full-`E` nullity where marked.

**The certificate.**  `mult_det = a − dim ker[E; ev]` and `rank_p ≤ rank_Q`, so

    a − nullity_p([E; ev])  ≤  mult_det  ≤  a,

and `nullity_p = 0` at a **single** prime *proves* `mult_det = a` over `Q` — no
randomness enters that implication.  Every row below has `nullity_p = 0` at both
primes unless stated otherwise.  `level` is the compression `(sample, group)` that
carried the verdict — `(s, g)` means `s·n_χ` rows of `E` sampled and grouped in
`g`s, with the `K` evaluation rows pinned on afterwards; a nonsingularity
certificate at any level proves the full matrix injective.

`balance := λ_1 − λ_6`.  `HWM` is the cell's own peak resident set, one process
group per cell.

| δ | λ | elig | bal | a | full-`E` | `N_S` | \\|Stab\\| | `n_χ` | rows | `nnz` | `nnz/n_χ` | nullity | `mult_det` | level | build s | wall s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|""")
    for d in cs:
        det = d['sides']['det']; pp = det['per_prime']
        LS = {'cheap': ['(3,2)', '(12,2)', 'full'], 's42': ['(12,2)', 'full']}
        if 'sample' in d:                      # a wk9_s45_bigcell run: one prepared level
            lv = ['(%d,%d)' % (d['sample'], d['group'])]
        else:
            names = LS[d.get('levelset', 'cheap')]
            lv = sorted({names[v['level']] for v in pp.values()})
        fc = d.get('full_E_nullity', '—')
        A(f"| {d['delta']} | `{tuple(d['lam'])}` | {'yes' if d['lam'][0] >= d['delta'] else 'onset-only'} | {bal(tuple(d['lam']))} | {d['a']} | {fc} | {d['N_S']} | {d['stab']} | "
          f"{d['n_chi']} | {d['nrows']} | {d['nnz']} | {d['nnz']/d['n_chi']:.1f} | {det['nullity']} | "
          f"**{d['mult_det']}**{' = a' if det['nullity']==0 else ''} | {lv[0] if len(lv)==1 else '/'.join(lv)} | "
          f"{d['build_secs']} | {d.get('wall_secs', d['secs'])} | {d.get('hwm_gb')} |")
    prov = sum(1 for d in cs if d['sides']['det']['nullity'] == 0)
    A(f"""
**{len(cs)} cells, {prov} of them with `mult_det = a` proved by a single-prime
nonsingularity certificate.**  Ambient units (`Σ a`): {sum(d['a'] for d in cs)}.
Frontier reached: `n_χ = {max(d['n_chi'] for d in cs)}` at
`N_S = {max(d['N_S'] for d in cs)}`; best balance measured: {min(bal(tuple(d['lam'])) for d in cs)}.
""")
    return "\n".join(L) + "\n"

def curve():
    bcs = load('s45_buildcurve.jsonl') + [dict(lam=d['lam'], delta=d['delta'], N_S=d['N_S'],
        stab=d['stab'], n_chi=d['n_chi'], nrows=d['nrows'], nnz=d['nnz'],
        build_secs=d['build_secs'], mono_secs=d['mono_secs'], orbit_secs=d['orbit_secs'],
        rows_secs=d['rows_secs'], hwm_gb=d['build_hwm_gb']) for d in cells()]
    seen = {}
    for d in bcs: seen[(tuple(d['lam']), d['delta'])] = d
    return sorted(seen.values(), key=lambda d: d['N_S'])

if __name__ == '__main__':
    open(os.path.join(R, 's45_ledger.md'), 'w').write(ledger())
    print(ledger())
