# Integrator review — session 37 (theory: washout, transfer, DIP, blindness slab)

2026-09-02.  Branch `s37-dip`, head `8e9bda2` (3 commits on `5367c75`; prereg
first at `ce2e657`, before reading or computing).  Four documents delivered.
The arguments were each walked independently; the few numbers were recomputed.

## 1. Verification — the logic holds, the numbers agree

- **Transfer lemma.**  `P_r ⊆ R_r` gives `I(R_r) ⊆ I(P_r)`, hence
  `pad_units_P ≥ pad_units_R` and `D_P ≤ D_R` cell by cell.  So `D < 0`
  transfers to the true permanent, `D > 0` does not, and — the useful
  corollary — **the reducible-locus computation is a complete screen**: no
  obstruction against the permanent can hide from a computation against
  `{l·c}`.  And the pipeline, which evaluates at `l·per_3(M(s))`, computes
  `P_r` at every `r`.  All correct.
- **Pieri argument (Prop. 8).**  An equation of degree `δ` of `D_6^{per_3}`
  has at most `δ` rows, so for `δ ≤ 5` it has length ≤ 5 and corresponds to
  an equation of `D_5^{per_3} = Sym^3 C^5` — none exist.  So
  `I(D_6^{per_3})_δ = 0` for `δ ≤ 5` for free, and the session measured it
  empty at `δ = 6` too.  Combined with the pullback argument (an equation of
  `P_r` of degree `δ` is one of `R_r` unless `I(D_r^{per_3})_δ ≠ 0`), this
  gives the refinement that matters below.
- **Dimensions.**  `dim D_6^{per_3} = 50` (rank 50 ≤ dim ≤ 54 − 4),
  `P_6 = 55 = 6 + 50 − 1`, `R_6 = 61 = 6 + 56 − 1`, `D_6^{det_4} = 66 = 96 − 30`
  in `126`.  All reproduce.  With the finite-stabiliser page now written for
  both forms, every dimension table in the record is unconditional.
- **Ambient counts at the new strict cells.**  `a((8,8,8),6) = 2` (the two
  degree-6 invariants of ternary quartics, `I_3^2` and `I_6` — matches
  Dixmier–Ohno), `a((12,8,8),7) = 5`, `a((4,4,4),3) = 1`.  The claim
  `D((8,8,8),6) = −1` needs exactly one degree-6 invariant combination to
  vanish on `l·c`; consistent with the counts, not independently verified
  here (the det side is ambient at length 3 by the codimension-0 row, so only
  the pad vanishing carries the claim).
- **BIP's threshold.**  Bürgisser–Ikenmeyer–Panova's no-occurrence-obstruction
  theorem needs `n ≥ m^25`; at `(m, n) = (3, 4)` it is silent.  Correct, and
  consequential (§2b).

## 2. Four consequences that change what we do next

**(a) The permanent enters at length 6 *and* degree ≥ 7 — not at length 6
alone.**  Prop. 8 says `P_6` and `R_6` have identical ideals through
`δ = 6`.  So the six-row cells at `δ = 6` in session 36's Stratum B —
including `(7,7,4,4,1,1)` — are *not* permanent-sensitive after all; the
first cells that can be are the six-row cells at `δ = 7`, which s36 is
sweeping.  Read s36's report with this refinement, and correct my s36 brief's
"first permanent-sensitive cells" to "first *possibly* permanent-sensitive
cells, at δ ≥ 7."

**(b) The `a ≥ 2` gate is a convention we inherited from a theorem that does
not apply here.**  We excluded `a = 1` cells because occurrence obstructions
"are closed by BIP" — but BIP needs `n ≥ m^25`.  At `(3, 4)` an occurrence
obstruction (`a = 1`, `mult_det = 0 < mult_pad = 1`) is not ruled out by
anything.  Two actions: future sweeps use the gate `a ≥ 1`; and the
"det-side empty through 7" record, which rests on `a ≥ 2` sweeps at δ = 6, 7,
should be closed on the `a = 1` cells too — they are the peaked, cheap ones
(s38 measured several at δ = 8: all empty).  A small pass.

**(c) The reducible locus can *prove* blindness.**  Since `D_P ≤ D_R`, showing
`D_R ≤ 0` across a range proves `D_P ≤ 0` there.  That gives Direction 1's
Kempf-collapsing route a second life at every `r`: not as a source of
obstructions (it can only over-estimate `mult_pad`) but as the cheapest
possible blindness prover.  Worth carrying into the next theory brief.

**(d) The honest frame for paper 2.**  DIP's obstruction is an
ambient-versus-stabiliser count — the house's own `a > m_det` screen — not an
HWV evaluation; any such cell has empty pad ideal, so the permanent is
irrelevant to it; and s38's screen says that route is silent at length 5
through δ = 10.  The set-theoretic separation `x_0·per_3 ∉ closure(GL_16·det_4)`
follows in-house from s32's Theorem 5 and agrees with Landsberg–Manivel–
Ressayre.  So paper 2 is, like DIP, exhibiting (or bounding) the multiplicity
method on a *known* non-containment.  That is a respectable frame and it
should be stated plainly rather than discovered by a referee.

## 3. Smaller items

- The s35 cap is now literature-backed: Dimca (2013) Thm 3.1 plus Koszul
  bookkeeping gives `dim M(f)_{3d−5} = smooth + defect`, so
  `onset ≤ 300` is a theorem modulo Kleiman transversality.  The det-side
  window is **`[8, 300]`** from here on.
- Pad onset at `r = 5` is `5` or `6`, decided by `(4,4,4,4,4)` and
  `(6,4,4,4,2)` at δ = 5 — both have large weight-stabilisers (`S_5` and `S_3`),
  so under s36's reduction they are cheap.  Recommend for s36's successor.
- The `λ_5 = 1` sub-slab: reduced to a first-order jet question with an honest
  open end (pad jets 34-dimensional, actual reducible det jets ≤ 33 on every
  s32 stratum, the block-degeneration limit not recovering the direction).
  Labelled open; it is the first place a genuine border phenomenon is
  structurally possible at length 5, which is why the session's suggested
  cells there are worth measuring.
- Process: the prereg's expectation about DIP's mechanism was wrong and is
  recorded as such — that is the discipline working.  `pkill -f` self-match
  cost a restart for the **third** session running; the rule is in every
  brief and is not sticking.  Next briefs will name a house helper
  (`scripts/killpid.sh`, kill by PID read back) and ban the command outright.

## 4. Standing after session 37

The week's correction is now a theorem with a precise boundary: below length
6 the hunt is `{l·c}` against the determinant; at length 6 the permanent can
first be felt only from degree 7; and at every length the permanent can only
*erase* an obstruction, never create one.  The reducible-locus computation is
a complete screen and a blindness prover.  The det-side window is `[8, 300]`.
Next measurements, in order: s36's six-row δ = 7 cells (already in flight);
the `a = 1` gap at δ = 6, 7; the two pad-onset deciders under the reduction;
s37's `λ_5 = 1` cells at δ = 7, 8.
