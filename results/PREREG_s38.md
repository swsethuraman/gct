# Pre-registration — session 38: the onset of `I(D_5^det)`

2026-09-02. Branch `s38-onset`, clone tip `5367c75` (s35 review).
Ancestry gate: `git merge-base --is-ancestor c02cee8 HEAD` **passes**;
`docs/s35_review.md` **present**. No session-38 collision in the record.

Written and committed **before any computation** (only reads of the record and
one `scripts/ambient_screen.py --selftest`, which passed, precede it).

---

## 0. A flagged discrepancy in the brief's required reading — recorded up front

The s38 brief names `docs/s36_prompt.md` as the source of "the stabiliser
reduction lemma, which you will also implement — independently … from the lemma
statement, not from session 36's code (two independent implementations are the
house's check on a shared spec)."

**Neither `docs/s36_prompt.md` nor any session-36 or session-37 material exists
in this repository.** The record's latest prompt is `docs/s35_prompt.md`; the
tip is the s35 review; `git log` shows no s36/s37 commit and no
`analysis/wk*_s36*` code. There is therefore **no shared spec and no sibling
implementation** to be independent from. Per the brief's own house rule for
anomalies ("if the repository already shows a session 38, do not renumber; flag
it and carry on"), I flag it and carry on, as follows:

- The **rectangular** stabiliser–isotypic reduction *is* on the record, stated
  and proved: `docs/s33_review.md` §2 and the docstring of
  `analysis/wk9_s33_rungs.py` (sign^δ-isotypic projection under the S_4 of
  variable permutations; `A_4` 2-transitivity collapses the four simple raising
  operators to `E_12`; odd-δ swap-fixed rows cancel exactly). This is a genuine
  lemma with a validation battery, and I reimplement it independently (§P1)
  and reproduce the r=4 ladder as the first check.
- For **general length-5 weights** the rectangular argument does **not** port:
  `S_lam(C^5)` is not one-dimensional, so highest-weight vectors are not Weyl
  eigenvectors and the isotypic collapse of `ker R` to one operator is
  unavailable (derivation in the session record). I will therefore **not**
  fabricate a "session-36 reduction" I cannot certify. Phase-1 measurements
  proceed on the **unreduced** `measure()` of `wk8_s30_core.py` (corrected
  raising rule, two primes, rank-attains-`a` certificate), which is exact and
  needs no reduction, wherever the weight space `N_S` is within the container's
  memory model (`7.5e-8·N_S^2` GB, `run62c` fit; usable ~6.5 GB ⇒ `N_S ≲ 9000`
  per cell). Cells above that wall without a certified reduction are reported as
  **not reached**, named exactly, not guessed.

This keeps the house invariant intact: **nothing is banked that is not either
proved or certified by an exact rank that attains `a`.**

---

## 1. The object and the identification (from the record, restated so it cannot drift)

`D_5^det = closure{ (s_1..s_5) ↦ det_4(s_1 A_1 + … + s_5 A_5) : A_i ∈ M_4 } ⊆
Sym^4 C^5`, the quinary quartics with a 4×4 linear determinantal representation.
Ambient `Sym^4 C^5` has dimension `C(8,4) = 70`; `dim D_5^det = 50`
(`docs/n4_gate.md` §4, Jacobian rank `16·5 − 30 = 50`), so **codimension 20**.

By the length-reduction (`docs/isotypic_rank.md` Prop. 5 / Thm 6′), for a weight
`lam` with `ell(lam) = 5`,

    mult_lam C[closure(GL_16 · det_4)]_delta  =  mult of S_lam(C^5) in C[D_5^det]_delta ,

and `I(D_5^det)` is concentrated at **length exactly 5** in the whole onset
window: length ≤ 3 sees only ternary quartics (`det_4|_{3-plane}` dense, rank
15/15), and length 4 sees `D_4^det`, whose ideal is principal of degree
`e = 320112` (`docs/e4_hunt.md`) — far above 405. So the onset lives at `ell = 5`.

**Onset (definition).** `onset := min{ delta : I(D_5^det) has a nonzero isotypic
component at some ell=5 weight of degree delta }`. Equivalently the least `delta`
with a length-5 `lam` at which `det_units(lam,delta) := a(lam,delta) −
mult_det(lam,delta) > 0`.

Window on entry: **`[8, 405]`** — empty through 7 on every measured cell
(`docs/sweep62.md`, `docs/n4_gate.md`, s34 record); capped by the discriminant
of quartic threefolds, degree `5·3^4 = 405` (`docs/s33_review.md` §4).

**Two counts, both pure representation theory (no geometry):**
- `a(lam,delta)` = mult of `S_lam` in `Sym^delta(Sym^4 C^5)` = plethysm
  coefficient `⟨h_delta[h_4], s_lam⟩` (independent of variable count for
  `nv ≥ ell(lam)`); `scripts/ambient_screen.py::a(·,·,d=4,nv≥5)`.
- `m_det(lam)` = `dim (S_lam^*)^{Stab(det_4)}` = the **symmetric rectangular
  Kronecker coefficient**, rectangle `(delta^4)`, `N = 4δ`
  (`docs/screen_results.md`; `ambient_screen.py::m_det(·,4,delta)`), the
  Peter–Weyl multiplicity in the coordinate ring of the *orbit*.

Since `mult_det ≤ min(a, m_det)`, **any cell with `a > m_det` has
`det_units ≥ a − m_det > 0` with no rank computation** — an equation of
`D_5^det`, located by arithmetic alone. This is the s28 occurrence mechanism.

---

## 2. Predictions

### P1 — the validation battery passes (including odd-block sign tests)

I reimplement the pipeline independently and require, **before any new cell**:

1. **Witness gate K1** (`docs/sweep62.md` §(b)): binary quartics, closure`{l^3 m}`,
   `lam=(4,4)`, `delta=2` ⇒ `a=1`, `mult=0`, kernel proportional to
   `(12,−3,1)` at both primes (the corrected-rule signature; the wrong rule
   gives `(1,−4,3)`).
2. **Rectangular r=4 ladder** rungs 4–8: `a((delta^4),delta) = 1,0,1,1,3`
   (`docs/n4_gate.md` §5, `results/e4_ledger.md`), reproduced from my own
   plethysm and my own reduction; `rank(R) = n_chi − a`; **odd-δ swap-fixed
   rows cancel exactly** (rungs 5,7 — the odd-block sign test), asserted, not
   observed. `mult_det((4^4),4)=1`, `((6^4),6)=1`, `((7^4),7)=1`, `((8^4),8)=3`
   at both primes.
3. **Length-5 banked cells** (`docs/n4_gate.md` §6): the nine `delta=6`,
   `ell=5` cells (and, cost permitting, the `delta=5` cells) return
   `mult_det = a`, reduced == unreduced where both are affordable.

**Prediction: passes.** The core primitives are the s30/s33 code the record
already certified 48/48 on the World-A battery and on every rung; my
independent re-run must reproduce them or the kill fires.

### P2 — does the occurrence screen (`a > m_det`, `ell=5`) fire by `delta = 12`?

**Prediction: SILENT through 12** — I expect no `ell=5` cell with `a > m_det` at
`delta ≤ 12`, i.e. the onset, when found, will be a genuine *multiplicity* drop
(`mult_det < a ≤ m_det`) needing a rank, not an occurrence phenomenon.
Confidence: **moderate (≈65%)**, deliberately lower than the programme's usual,
for the reasons below.

Reasoning, with the regime warning the brief demands (the house has been burned
by regime transfer three times — quotient-blindness, lowest-invariant bias,
shared-spec correlation):

- The n=3 mirror "fired at δ=10" (`docs/d5_ideal.md` §4) — **but at lengths 8
  and 9, by the degenerate `m_det = 0` route**, not at length 5. At length 5
  (the true `D_r` analogue) the n=3 arithmetic route *never* fired in reach:
  `mult = a` was measured through δ=7 and `a ≤ m_det` held (Cor. 7). So "n=3
  fired at 10" is a **different length regime** from ours; transferring it to
  "n=4, ell=5 fires by 12" is precisely the move that has misfired before. I
  therefore do **not** lean on it.
- Across every measured regime of the programme, the symmetric rectangular
  Kronecker `m_det` has *dominated* the plethysm `a` (Cor. 7: `a ≤ m_det` at all
  length-≤4 weights through δ=7; the n=3 length-5 cells likewise). The rectangle
  `(delta^4)` grows its Kronecker room fast. For `a` to overtake it at moderate
  δ would be against the grain of all prior data.

Counter-weight (why only moderate confidence): `D_5^det` has **codimension 20**,
much larger than the n=3 `D_5`'s codimension 6, and the brief's own framing is
that codim-20 loci "usually have low-degree equations." A large ideal has more
chances to outrun `m_det`. If the screen *does* fire, δ=8 is the natural first
suspect. The screen decides this cleanly either way and is cheap; the prediction
is registered so the outcome is scored honestly.

### P3 — does `delta = 8` bite on any reachable cell?

**Prediction: more likely empty than not on reachable cells — low confidence
(~55% empty).** If the occurrence screen fires at δ=8, the answer is trivially
yes and the kernel is exhibited. If not, a δ=8 bite requires a true rank drop
`mult_det < a`. The n=3 length-5 mirror stayed empty well past the degree its
codimension-6 might suggest (bracket `[8,80]`, never seen to bite in reach), so
"empty at the window's floor" has precedent. But codim 20 ≫ codim 6 pulls the
other way. Genuinely open; registered as such. If δ=8 is empty on every
*reachable* cell, the floor moves to 9 **for the measured corner**, and I will
state exactly which cells were not reached.

---

## 3. Kill criteria (standing)

- **Validation failure** (any item of P1) → **stop**. The pipeline is wrong;
  fix and re-validate before any cell.
- **A Phase-0 `a > m_det` cell whose rank measurement fails to bite**
  (`mult_det = a` measured where `a > m_det` was computed) → **stop everything**.
  This is a contradiction: one of `a`, `m_det`, or the pipeline is wrong, and
  *that* is the finding. No further cells until it is resolved.
- Memory: a cell whose predicted footprint exceeds the budget is **not run**
  and reported as not-reached — never estimated, never half-run and banked.

## 4. Protocol for a bite (the full sceptical treatment)

The **first** det-side bite (the onset) receives: 3× evaluation points; a second
seed and a second prime; the kernel vector exhibited in coefficient coordinates
and shown to **vanish at 10 fresh determinantal pencils and not at a generic
quartic**; then its weight, degree and length recorded as the programme's first
equation of `D_5^det`. Every banked cell carries `a` by two routes (my plethysm
and `ambient_screen`), `rank(R) = N_S − a` (or `n_chi − a`) asserted, and two
primes, with a commit per cell.

## 5. Deliverables

`results/PREREG_s38.md` (this file); `results/occurrence_screen.md` (the full
`a` vs `m_det` table by degree, δ=8..12 as budget allows, plus δ≤7 as a
consistency check against "empty through 7"); `results/onset_ledger.md`
(per-cell bank); `docs/det_onset.md` (findings in house style — the certificate
if a bite is found, the honest bracket if not); code `analysis/wk9_s38_*.py`.
Delivery by `git bundle` (`onset.bundle`, single ref `s38-onset`), insurance
bundle every few hours, no pushes. Ends with the window as left — `[floor, 405]`
or the pinned onset — and the bundle head hash.
