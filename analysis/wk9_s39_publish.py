#!/usr/bin/env python3
"""
Session 39 -- aggregate results/s39_screen/*.csv into the published screen:
results/longweight_screen.csv (all rows) and results/longweight_screen.md
(the table: per (delta, ell) cell counts, the one-bit and forced lists, the
tightest margins, and the coverage/boundary statement).

A (delta, ell) chunk counts as COMPLETE iff results/s39_screen/d<d>_l<l>.csv.done
exists; otherwise it is reported as PARTIAL with the number of rows banked so
far against the candidate count.  Nothing is inferred: only banked rows are
summarised.

usage: python3 wk9_s39_publish.py
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s39_chars import partitions

ROOT = os.path.join(HERE, '..')
SDIR = os.path.join(ROOT, 'results', 's39_screen')
CSV = os.path.join(ROOT, 'results', 'longweight_screen.csv')
MD = os.path.join(ROOT, 'results', 'longweight_screen.md')
DMIN, DMAX = 8, 12


def cand_count(delta, ell):
    N = 4 * delta
    return sum(1 for lam in partitions(N) if len(lam) == ell and lam[0] >= delta)


def load():
    rows = {}          # (delta, ell) -> list of (lam, a, m_det, cls, margin)
    for delta in range(DMIN, DMAX + 1):
        for ell in range(6, min(delta, 10) + 1):
            p = os.path.join(SDIR, 'd%d_l%d.csv' % (delta, ell))
            seen = {}
            if os.path.exists(p):
                for ln in open(p):
                    if ln.startswith('delta') or not ln.strip(): continue
                    f = ln.strip().split(',')
                    lam = tuple(int(x) for x in f[1].split('|'))
                    row = (lam, int(f[3]), int(f[4]), f[5], f[6])
                    if lam in seen:
                        assert seen[lam] == row, ('duplicate row disagrees', p, lam, seen[lam], row)
                    seen[lam] = row
            rows[(delta, ell)] = list(seen.values())
    return rows


def complete(delta, ell):
    return os.path.exists(os.path.join(SDIR, 'd%d_l%d.csv.done' % (delta, ell)))


def main():
    rows = load()
    # write the flat csv
    with open(CSV, 'w') as fh:
        fh.write('delta,lam,ell,a,m_det,class,margin\n')
        for (delta, ell), rr in sorted(rows.items()):
            for lam, a, md, cls, margin in rr:
                fh.write('%d,%s,%d,%d,%d,%s,%s\n' % (delta, '|'.join(map(str, lam)), ell, a, md, cls, margin))

    onebit = [(d, e, lam, a, md) for (d, e), rr in rows.items() for lam, a, md, cls, margin in rr if cls == 'onebit']
    forced = [(d, e, lam, a, md) for (d, e), rr in rows.items() for lam, a, md, cls, margin in rr if cls == 'forced']

    L = []
    W = L.append
    W('# Long-weight occurrence screen — `a` vs `m_det`, `6 ≤ ℓ(λ) ≤ 10`, `n = 4`\n')
    W('Session 39, 2026-09-02.  Code `analysis/wk9_s39_screen.py` on the exact')
    W('C Murnaghan–Nakayama engine `analysis/wk9_s39_chars.{c,py}` (validated:')
    W('`results/logs/s39_chars_selftest.log` — house `chi`/`a`/`m_det`, the `n=3`')
    W('anchors, the s28 `δ=10` precedent, and s38\'s length-5 table δ 5–9).  Data:')
    W('`results/longweight_screen.csv`.  This screen EXTENDS s38\'s length-5')
    W('`results/occurrence_screen.md` to lengths 6–10 (rows 11–16 excluded by')
    W('theorem — see the region statement).\n')
    W('## What is computed, and the eligible region\n')
    W('For every `λ ⊢ 4δ` with `6 ≤ ℓ(λ) ≤ min(δ,10)` and `λ_1 ≥ δ`:\n')
    W('- `a(λ,δ)` = plethysm `⟨h_δ[h_4], s_λ⟩` (ambient room; `mult_det, mult_pad ≤ a`).')
    W('- `m_det(λ)` = symmetric rectangular Kronecker coeff, rectangle `(δ^4)`,')
    W('  `= (1/2)[g(λ,(δ^4),(δ^4)) + T(λ)]` (`mult_det ≤ m_det`), computed only when `a ≥ 1`.\n')
    W('The eligible region for an occurrence obstruction (`mult_det = 0 < mult_pad`)')
    W('or a forced multiplicity drop is bounded, all proved: `a ≥ 1`')
    W('(BIP silent at `(3,4)`); `λ_1 ≥ δ` (Kadish–Landsberg via (★),')
    W('`docs/stabiliser_reduction.md`); `ℓ ≥ 6` (`ℓ ≤ 5` cannot see the permanent,')
    W('`docs/washout_lemma.md`); `ℓ ≤ min(δ,10)` — `ℓ ≤ δ` since every constituent')
    W('of `Sym^δ(Sym^4)` has `≤ δ` rows, and **`ℓ ≤ 10`** because the padded')
    W('permanent is concise in 10 variables, so `P_r ⊆ Sub_10` and `mult_pad = 0`')
    W('for `ℓ ≥ 11` (`results/PREREG_s39.md` §0, proved).  Rows 11–16 are excluded')
    W('by that theorem, not by budget.\n')
    W('## Classification\n')
    W('- **one-bit**: `a = 1, m_det = 0` — det side zero for free; pad side a single evaluation.')
    W('- **forced**: `a > m_det ≥ 1` — det loses `a − m_det` for free; pad-side rank `≥ m_det+1` certifies an obstruction.')
    W('- **silent**: `a ≤ m_det` (no arithmetic bite).\n')
    if onebit or forced:
        W('## RESULT: the screen is NOT silent — candidate cells found\n')
        if onebit:
            W('### one-bit cells (`a = 1, m_det = 0`)\n')
            W('| δ | ℓ | λ |')
            W('|---|---|---|')
            for d, e, lam, a, md in sorted(onebit):
                W('| %d | %d | `%s` |' % (d, e, lam))
            W('')
        if forced:
            W('### forced cells (`a > m_det ≥ 1`)\n')
            W('| δ | ℓ | λ | a | m_det | det_units ≥ |')
            W('|---|---|---|---|---|---|')
            for d, e, lam, a, md in sorted(forced):
                W('| %d | %d | `%s` | %d | %d | %d |' % (d, e, lam, a, md, a - md))
            W('')
        W('These are tested in Phase 1 (`results/onebit_ledger.md`).\n')
    else:
        W('## RESULT: the occurrence route is SILENT at every length 6–10 across the completed region\n')
        W('**No cell has `a = 1, m_det = 0` and no cell has `a > m_det`.** Every cell')
        W('with `a ≥ 1` has `a ≤ m_det` — the determinant\'s symmetric rectangular')
        W('Kronecker room dominates the ambient plethysm room at lengths 6–10 just as')
        W('s38 found at length 5.  So no occurrence obstruction and no forced')
        W('multiplicity drop lives at `6 ≤ ℓ ≤ 10` in the region screened; any')
        W('separation here would have to be a genuine multiplicity phenomenon')
        W('(`mult_det < a ≤ m_det`), invisible to arithmetic.\n')

    W('## Coverage by `(δ, ℓ)`\n')
    W('“cells” = candidates with `a ≥ 1`; `a = 0` candidates are not cells.')
    W('A chunk is COMPLETE iff its `.done` marker exists; else PARTIAL (banked/candidates).\n')
    W('| δ | ℓ | candidates | banked | cells (a≥1) | one-bit | forced | tightest `m_det−a` (λ) | status |')
    W('|---|---|---|---|---|---|---|---|---|')
    tot_cells = tot_one = tot_forced = 0
    for delta in range(DMIN, DMAX + 1):
        for ell in range(6, min(delta, 10) + 1):
            rr = rows[(delta, ell)]
            cand = cand_count(delta, ell)
            cells = [x for x in rr if x[1] >= 1]
            nb = len(rr)
            no = sum(1 for x in rr if x[3] == 'onebit')
            nf = sum(1 for x in rr if x[3] == 'forced')
            tot_cells += len(cells); tot_one += no; tot_forced += nf
            tight = min(((md - a, lam) for lam, a, md, cls, mg in cells), default=None)
            tstr = ('%d (`%s`)' % (tight[0], tight[1])) if tight else '—'
            st = 'complete' if complete(delta, ell) else 'PARTIAL %d/%d' % (nb, cand)
            W('| %d | %d | %d | %d | %d | %d | %d | %s | %s |'
              % (delta, ell, cand, nb, len(cells), no, nf, tstr, st))
    W('')
    W('Totals across banked rows: **%d cells (a≥1), %d one-bit, %d forced.**\n' % (tot_cells, tot_one, tot_forced))
    W('_(generated %s by `analysis/wk9_s39_publish.py`)_' % time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()))

    open(MD, 'w').write('\n'.join(L) + '\n')
    print('wrote', MD, 'and', CSV)
    print('one-bit:', len(onebit), 'forced:', len(forced), 'cells:', tot_cells)
    return 0


if __name__ == '__main__':
    sys.exit(main())
