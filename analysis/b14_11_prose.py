"""Apply explicit B14-11 errata and retain a machine-readable before/after audit."""
import hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b14_11'
changes=json.loads((OUT/'prose_changes.json').read_text(encoding='utf-8')) if (OUT/'prose_changes.json').exists() else []

def edit(path,old,new):
    p=ROOT/path; text=p.read_text(encoding='utf-8')
    if new in text:return
    if old not in text:
        if new in text:return
        raise ValueError('required prose missing: '+path+' '+old[:80])
    count=text.count(old)
    changes.append(dict(path=path,line=text[:text.index(old)].count('\n')+1,
                        occurrences=count,before=old,after=new))
    p.write_text(text.replace(old,new),encoding='utf-8')

def main():
    edit('docs/n4_gate.md',
         'Two conditions must both hold: ambient room `a >= 2` (below that any\nobstruction is an occurrence obstruction, closed by BIP) and length',
         'Historical selection used ambient room `a >= 2` and length')
    edit('docs/n4_gate.md','## 2. The gate, reproduced\n',
         '## 2. The gate, reproduced\n\n**B14-11 correction.** The table below records the historical `a >= 2`\nselection. It is not an exclusion of `a = 1`: BIP is silent at `(n,m)=(4,3)`.\nThe current ambient gate is `a > 0`, including A1; after the containment\nexclusion of section 1 the length gate is `ell >= 5`. See `bip_blind_at_n4`\nand `docs/b14_11_report.md`. Historical counts and measurements are unchanged.\n')
    edit('docs/n4_gate.md','Every 4-ary cubic is `3x3` linear-determinantal (classical for smooth',
         'A generic 4-ary cubic is `3x3` linear-determinantal (classical for smooth')
    edit('docs/easy_counts.md',
         '   where Buergisser-Ikenmeyer-Panova forces `def_per = m_per`, a full deficit.\n   So on the `m_det = 0` locus — 85% of live weights at `(5,2)` — the\n   cancellation `D = 0` is not a coincidence at all, it is BIP\'s theorem.\n   The unexplained saturation is confined to the `m_det > 0` locus.',
         '   where the ambient coefficient is zero (s25, `docs/ambient_audit.md`\n   section 8), hence `def_per = m_per`. This is ambient arithmetic, not a\n   BIP application. BIP supplies no exclusion at the small parameters here.')
    edit('docs/easy_counts.md',
         'and on most of the weight space (`m_det = 0`) that side is already settled\nagainst us by BIP.  Any future search should be confined to `m_det > 0` — 6 of\n42 weights at `(5,2)` — which is also exactly where the deficit is hardest to\ncompute.',
         'and the ambient-zero portion is settled by the ambient coefficient.\nAt `(5,2)` all 36 determinant-unsupported weights have `a = 0` (s25).\nAt other parameters, `m_det = 0` alone supplies no BIP exclusion; retain\nany `a > 0` label until an applicable theorem or certificate closes it.')
    edit('docs/s24_obstruction.md',
         'one multiplicity is zero — cannot separate the padded permanent from the\ndeterminant.',
         'the determinant multiplicity is zero and the padded multiplicity is\npositive — cannot separate their padded model from the determinant when\n`n >= m^25`. This does not exclude A1 at `(n,m)=(4,3)`.')
    edit('docs/batch11_plan.md',
         'over the range of `n` the programme cares about, while multiplicity obstructions\nremain open',
         'in their asymptotic range `n >= m^25`; that theorem is silent at\n`(n,m)=(4,3)`. Multiplicity obstructions remain open')
    edit('docs/batch11_plan.md',
         'stronger claim, since occurrence obstructions are ruled out in the padded regime\nand multiplicity obstructions are not.',
         'claim of a strict multiplicity gap despite occurrence on both sides.\nBIP rules out occurrence obstructions only in its `n >= m^25` regime; it\ndoes not exclude them for the programme\'s small padded pair.')
    edit('docs/obstruction_power.md',
         '**The occurrence sub-case is already closed.**',
         '**The occurrence sub-case needs a regime check.**')
    edit('docs/obstruction_power.md',
         '   the padded permanent against the determinant.  So the deficit cannot help\n   in the sub-case where it would be easiest to detect.',
         '   their padded permanent against the determinant when `n >= m^25`.\n   This leaves `(n,m)=(4,3)` open; A1 is excluded only by an applicable\n   theorem or certificate, never by that asymptotic citation alone.')
    edit('docs/screen_results.md',
         'Bürgisser–Ikenmeyer–Panova close.  So even where the Peter–Weyl side goes\nneutral, the only obstruction the arithmetic leaves room for is the one already\nknown to be unavailable.',
         'Bürgisser–Ikenmeyer–Panova close in their range `n >= m^25`. That\nhypothesis fails here. The two screened labels close by the ambient and\ndegree-one arguments above; the occurrence observation gives no extra closure.')
    edit('docs/screen_results.md',
         'Bürgisser–Ikenmeyer–Panova rule out.  So BIP\'s theorem, translated into this\nprogramme\'s language, says exactly:',
         'Bürgisser–Ikenmeyer–Panova do not rule out at these parameters.\n**B14-11: the following historical inference is withdrawn as a BIP claim:**')
    edit('docs/screen_results.md',
         'That is a nontrivial statement about the permanent\'s deficit obtained for free\nfrom a known theorem, and it is the first thing this programme\'s vocabulary has\nsaid about the permanent side.',
         'This needs an applicable ambient-zero result or a separate certificate\nat each label. The cited BIP theorem does not supply it at `(4,3)`.')
    edit('docs/screen_results.md','room for is an occurrence obstruction — the sub-case already closed.',
         'room for is an occurrence obstruction. BIP does not close that sub-case\nat `(4,3)`; the two labels above close by their separate ambient arguments.')
    edit('docs/session_24b.md',
         '* **A free statement about the permanent, from BIP**: at every weight where\n  `m_det(lam) = 0` — 14 of the 19 live weights at `(n,m,delta) = (4,3,2)` —\n  Bürgisser–Ikenmeyer–Panova\'s theorem forces\n  `def_{per^pad}(lam) = m_{per^pad}(lam)`, a *full* deficit.',
         '* **B14-11 erratum to the BIP inference:** the historical claim that\n  `m_det(lam)=0` forces a full padded deficit at `(n,m,delta)=(4,3,2)`\n  does not follow from BIP. Its hypothesis `n >= m^25` fails here.\n  Use a label-specific ambient-zero proof or exact certificate instead.')
    edit('docs/washout_threshold.md',
         '(no occurrence obstructions for `det` vs padded `per`), which is a different',
         '(no occurrence obstructions in their range `n >= m^25`, silent at\n`(4,3)`), which is a different')
    # Repair the actual theorem hypothesis rather than merely renaming it.
    edit('docs/bip_transfer.md',
         'and a weight vector of weight `λ` vanishes identically at every',
         'and a highest-weight vector of highest weight `λ` vanishes at every')
    old='''**Lemma B (proved).**  Let `f` be a weight vector of weight `λ` in
`C[Sym^n V]_δ` and let `p ∈ Sym^n V` have linear span of dimension `u < ℓ(λ)`.
Then `f(p) = 0`.

*Proof.*  Choose coordinates so the span is `⟨e_1,…,e_u⟩` and take the torus
element `t = diag(1,…,1,c,…,c)` with `c` in positions `u+1,…`.  Then `t·p = p`,
while `f(t·q) = t^λ f(q)` with `t^λ = c^{λ_{u+1}+···+λ_N}`.  Since `ℓ(λ) > u`,
`λ_{u+1} ≥ 1`, so the exponent is positive; choosing `c ≠ 1` forces
`f(p) = 0`. ∎'''
    new='''**Lemma B (PROVED; hypothesis corrected by B14-11).** Every vector in
the irreducible isotypic component labelled by `λ`, in particular every HWV
of highest weight `λ`, vanishes on forms of essential-variable dimension
`u < ℓ(λ)`. Use the consistent polynomial-label convention
`C[Sym^n V*]_δ = Sym^δ(Sym^n V)`.

*Proof.* For a form `p` supported on a subspace `U` of dimension `u`,
`p^δ` lies in `Sym^δ(Sym^n U*)`. The Schur functor `S_λ U*` is zero
when `ℓ(λ)>u`. The natural Schur isotypic projection of `p^δ` is therefore
zero, and pairing with the `λ`-component gives zero. This argument is
functorial under `U -> V`, so it covers every position of the support. ∎

The original torus proof changed coordinates while retaining the old weight
character, which is invalid for an arbitrary torus weight vector. Explicit
counterexample: the coefficient functional of `x^3 y` has weight `(3,1)`
but takes value `4` on `(x+y)^4`, a form of essential span one. The corrected
HWV statement retains the BIP blindness conclusion.'''
    edit('docs/bip_transfer.md',old,new)
    edit('docs/PROVED.md',
         'and a weight vector of weight `λ` vanishes at every point of span `< ℓ(λ)`.',
         'and the irreducible component with highest weight `λ` vanishes on forms of essential span `< ℓ(λ)` (B14-11 repairs the overbroad arbitrary-weight assertion).')
    edit('docs/PROVED.md',
         '**Therefore `a = 1` cells are "excluded by convention, not by theorem"**',
         '**Historically `a = 1` cells were "excluded by convention, not by theorem"; the batch14 shortlist retains eligible A1 cells**')
    edit('docs/s52_report.md',
         '**Lemma B (proved, one line).**  A weight vector of weight `λ` vanishes at every\npoint whose linear span has dimension `< ℓ(λ)`.  *(Torus element trivial on the\nspan; the weight character is a positive power of the scaling.)*',
         '**Lemma B (PROVED, corrected B14-11).** The irreducible isotypic\ncomponent with highest weight `λ` vanishes on forms of essential span\n`< ℓ(λ)`, by functorial Schur restriction. The original arbitrary-weight\nwording is false; see the explicit counterexample in `docs/bip_transfer.md`.')
    edit('docs/s52_report.md','> of weight `λ` vanishes identically at every point of span `< ℓ(λ)`;',
         '> of highest weight `λ` vanishes at every point of span `< ℓ(λ)`;')
    edit('docs/session_52.md',
         '* **Lemma B (proved, one line):** a weight vector of weight `λ` vanishes at every',
         '* **Lemma B (PROVED, corrected B14-11):** a highest-weight vector of\n  highest weight `λ` vanishes at every')
    # Source-specific model and partition convention corrections.
    edit('docs/bip_transfer.md',
         '(The weight is a body of `k` rows of\nlength `ℓ` under one long first row, so `ℓ(λ) = k+1`.)',
         '(B14-11 correction: v3 defines `sharp` by extending the existing first\nrow, so this weight has `k` rows. It does not append a `(k+1)`st row.)')
    edit('docs/bip_transfer.md',
         'so `ℓ(λ) = k+1 ≤ 3`, and the two surviving generators are `(2,2)` at degree 1\nand `(4,2,2)` at degree 2.  Sums of partitions of length `≤ 3` have length\n`≤ 3`, so the semigroup route (c) never leaves `ℓ(λ) ≤ 3` either.',
         'so `ℓ(λ) = k ≤ 2`. The distinct generators are `(4)` at degree 1\nand `(6,2)` at degree 2. Sums of partitions of length at most two retain\nthat length bound. The former degree-one `(2,2)` claim was impossible:\n`Sym^1(Sym^4 V)` contains only `(4)`. This strengthens blindness here.')
    edit('docs/bip_transfer.md',
         '**Maximum linear span 3.**  And over `C` every one of the eight is a *product of\nfour linear forms* — `φ_1²+φ_2² = (φ_1+iφ_2)(φ_1−iφ_2)` — so the whole supply\nlies inside the Chow variety `Ch^4`, which sits in a 3-dimensional subspace:\ndimension at most `4·3 − 3 = 9`, against `dim D_6^{det_4} = 66`.',
         '**Maximum essential span 3 for each point.** Over `C` all eight\nare products of four linear forms, using the factorisation of a binary\nquadratic. Their supply lies in `Ch^4` intersected with `Sub_3`.\nB14-11 withdraws the former dimension-nine comparison: the support subspace\nvaries, and the full Chow variety need not have essential span at most three.')
    start='''*A note for the `ℓ ≥ 7` sessions, flagged not claimed.*  [KL]'s companion bound
is `ℓ(λ) ≤ m² = 9`, whereas `docs/sixrow_frontier.md` §1 records the
permanent-visible window as `6 ≤ ℓ(λ) ≤ 10`.  The `10` is the support count
`1 + m²` of `x_0·per_3(x_1..x_9)`; [KL]'s `9` is sharper.  If [KL]'s bound
transfers to the length-reduced model, `ℓ = 10` is empty and the window closes
one row earlier.  This session does not settle it — it does not arise at
`ℓ = 6` — but it is worth one paragraph of a later session.'''
    edit('docs/bip_transfer.md',start,
         '**B14-11 model audit.** The v3 paper defines padding with `X11` already\ninside the `m x m` permanent (page 2), so its support bound is `m^2`.\nThis project uses an independent `x0`, giving ten essential variables.\nThus the cited nine-row bound supplies no ten-row exclusion for this model.\nThe first-row eligibility condition is justified independently by the reducible\npullback and Pieri; see `quartic_length_and_eligibility` in `PROVED.md`.')
    edit('docs/bip_transfer.md',
         'Two readings, both worth recording.  The eight zeros are Lemma B, as predicted.\nThe `chow6` zero is *not* Lemma B — that point has full support 6 — and says\nthat at these three cells the highest weight vector vanishes on the whole Chow\nvariety of products of four linear forms, so BIP\'s supply at `n = 4` fails for a\nsecond, independent reason.',
         'The eight zeros agree with Lemma B. B14-11 correction: a product of\nfour linear forms has essential span at most four, even when all six ambient\ncoordinates appear. Thus its six-row HWV vanishing also follows from the\ncorrected support lemma. The sampled `chow6` zero is not an independent\nproof of vanishing on an entire variety.')
    # Retain historical pricing table but forbid use of its incorrect rectangle column.
    edit('docs/bip_transfer.md','### The reach, as a function of `n`\n',
         '### The reach, as a function of `n`\n\n**B14-11 erratum.** The historical table\'s Prop. 2.3 column and the `best`\ncolumn based on it used the incorrect extra-row convention and are\nWITHDRAWN for inference. A direct rectangle of length `L` requires at least\n`n=2L`; the corrected `n=4` generators above have length at most two.\nThe Prop. 5.2 and Prop. 5.5 hypothesis checks are unaffected.\n')
    edit('docs/batch14_reconciliation.md','and a weight vector of weight `λ` vanishes at every point of',
         'and an HWV of highest weight `λ` vanishes at every point of')
    edit('docs/s52_report.md','| Prop. 2.3 + semigroup | `n ≥ kℓ`, `ℓ` even | `ℓ(λ) ≤ 3` |',
         '| Prop. 2.3 + semigroup | `n ≥ kℓ`, `ℓ` even | `ℓ(λ) ≤ 2` (B14-11 corrected row extension) |')
    edit('docs/session_52.md','* Prop. 2.3 + semigroup reaches `ℓ(λ) ≤ 3`;',
         '* Prop. 2.3 + semigroup reaches `ℓ(λ) ≤ 2` (B14-11 corrected row extension);')
    edit('docs/s52_report.md','> one a product of four linear forms with linear span at most 3; a weight vector\n> of highest weight `λ`',
         '> one a product of four linear forms with essential span at most 3; an HWV\n> of highest weight `λ`')
    edit('docs/bip_transfer.md','(Lemma B, one line)', '(Lemma B, corrected below)')
    edit('docs/bip_transfer.md','* **flagged, not claimed:** the `ℓ(λ) ≤ m² = 9` versus `ℓ ≤ 10` question in §3(a).',
         '* **B14-11 resolved convention:** the cited nine-variable padding model differs\n  from the independent ten-variable padding here; no nine-row exclusion is imported.')
    edit('docs/s25_race.md',
         '  obstruction — closed by Bürgisser–Ikenmeyer–Panova. **Multiplicity\n  obstructions require `a >= 2`.**',
         '  obstruction. B14-11 correction: BIP is silent at these small\n  parameters. A multiplicity gap with both multiplicities positive requires\n  `a >= 2`; the definition of multiplicity obstruction also includes A1\n  occurrence obstructions, which need an applicable exclusion of their own.')
    edit('docs/s63_report.md',
         '(session 64); `i_det = 1` alone is an occurrence statement (Ikenmeyer–Panova).',
         '(session 64). B14-11 correction: `i_det=1` is an ideal multiplicity\nstatement; with `a=274` it gives `mult_det=273`, so it is not an occurrence\nobstruction. The positive padded gap still requires a certified comparison.')
    (OUT/'prose_changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('explicit prose corrections',len(changes),'in',len({x['path'] for x in changes}),'files')

if __name__=='__main__':main()
