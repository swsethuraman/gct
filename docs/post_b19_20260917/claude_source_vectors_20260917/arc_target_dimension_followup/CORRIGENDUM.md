# Corrigendum to the parent report `routeA_signfilter_20260917/REPORT.md`

Claude session, 17 September 2026. The parent packet is preserved byte-for-byte (31 outputs and 46
inherited inputs re-hashed at the start of this session, 0 mismatches). Each item cites the parent
section and gives the replacement; the parent's certified results (four independent source
directions, transverse triple of rank 3, sampled relation of `n02`) are unchanged.

## C1. Parent §7, "Smallest next step": the transposition component in the `b_L` count

**Defect.** The parent proposed computing `b_L` "with the three scalar conditions and the transposition
component from `STABILIZER.md`". Two errors: (i) `STABILIZER.md` describes the stabilizer of the
pencil `K5`, a different group from the grading-preserving Levi of the arc; (ii) no element of the
transposition coset of `H` preserves the `gamma`-grading (it swaps the first row `r` with the first
column `c`), so the Levi `L` of B19-01 Prop. 6.1 contains no transposition component and the
B19-01 count is an `L`-invariant count, full stop.

**Replacement.** `b_L = dim F^L` is computed here with `L` connected, exactly as in B19-01 §6
(REPORT.md §2.3, §3.1): `b_L = 74`. Transposition enters only as a separate, proved refinement:
`tau : Y -> Y^T` normalises `L`, preserves the `L`-invariant forbidden components, and the forbidden
components of every `z ∈ M` are `tau`-invariant functions, so `C(M) ⊆ (F^L)^{tau}` (REPORT.md §6.2);
`dim (F^L)^{tau}` is **not** computed in this session.

## C2. Parent §7, the conditional paragraph "if `b_L = 2` … Outcome B follows"

**Defect.** The paragraph is conditional on a value of `b_L` that is now known to be false
(`b_L = 74`). The paragraph's logic was also stated for the global rank; the same conclusion in fact
needs only `rank C|_S = 2` on `S = span(q_3, q_7, n02)`.

**Replacement.** REPORT.md §7.2 (Proposition 7.1): if `rank C|_S = 2` then the exact kernel vector
`n* = n02 − α* q_3 − β* q_7` exists, reduces mod `P` to the displayed modular candidate, and satisfies
`C4_{S1,S2}(n*) ≠ 0`, `C4_{S1,S4}(n*) ≠ 0` over `Q`. `rank C|_S = 2` is **not** proved; the Levi bound
does not give it.

## C3. Parent §5.3 and §5.4, witness language

**Defect.** The parent writes `n := n02 − 265391·q_3 − 275398·q_7 (coefficients modulo P)` and calls it
a "sampled arc-kernel candidate". The coefficients are residues, and three different statements were
not kept apart.

**Replacement.** (1) *Existence* of a characteristic-zero element of `ker C` outside `ker T`: OPEN
(would follow from `rank C ≤ 2`, or from `rank C|_S = 2`, neither proved). (2) *Explicit construction*
of such an element with rational coefficients: OPEN; the residues `265391, 275398` are not a rational
witness and no small-height lift exists (parent, bound 2000). (3) *Lifting of the displayed modular
candidate*: PROVED **conditionally** on `rank C|_S = 2` (REPORT.md Prop. 7.1); unconditionally the
displayed `n̄` is a vector over `F_P` in the kernel of ten sampled functionals and nothing more.

## C4. Parent §7, price of the next step

**Defect.** "seconds of runtime, perhaps a few hours of careful implementation" referred to the
Levi count, which indeed took 14 s here — but that count is not decisive. The decisive next step is
the refined target `F''` of REPORT.md §6, whose price is different (§6.4).

## What is unchanged

`dim span(q_3, q_7, e, n02) = 4` (certified); `rank T = 3` on `M` (proved); the sign-obstruction
criterion; all recorded evaluations and receipts; the standing reminder that `a = m_det = 1` and no
positive multiplicity gap is possible in this cell.
