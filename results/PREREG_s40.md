# Pre-registration — session 40 (theory: the onset conjecture, the `n = 3` twin, three write-ups)

2026-09-02.  Branch `s40-onset` off `e9cb8dd` (main = the s36 merge).  Ancestry
gate `git merge-base --is-ancestor 48bbdc3 HEAD` passes; `docs/s36_review.md`
present.  No prior session 40 in the tree (`docs/s40_prompt.md` is the brief,
committed by the integrator; no `PREREG_s40`, no `session_40`, no
`wk9_s40_*`).  Committed before any computation.

Labels used throughout: **proved** / **measured** / **adopted-from-literature**
/ **expectation**.  Every claim in the four deliverables carries one.

## 0. Standing conventions

- `D_5^{det_n} = closure{ det(s_1 A_1 + ... + s_5 A_5) : A_i ∈ M_n } ⊆ Sym^n C^5`.
  `I(·)` its ideal, `onset` the least degree in which the ideal is nonzero.
- `M_k(F)`: the degree-`k` Macaulay matrix of the five partials of `F`
  (rows `(i, m)`, `m` a monomial of degree `k − (n−1)`; columns the monomials
  of degree `k`; entry the coefficient of the column monomial in `m · ∂_i F`).
  Entries are linear in the coefficients of `F`.
- `μ_k(n) = [t^k] ((1 − t^{n−1})/(1 − t))^5` (Milnor algebra of a smooth
  quinary `n`-ic in degree `k`),
  `cap(n) = dim Sym^{3n−5} C^5 − μ_{3n−5}(n)`,
  `ν(n) = deg{rank ≤ n−2} ⊂ P(M_n)`.
- Exact arithmetic only: python-flint `nmod_mat` at the two house primes
  `2147483647`, `2147483629`; integer inputs in a stated box; seeds recorded.

## 1. Deliverable 1 — `docs/onset_conjecture.md`

**P1.1 (the cap theorem; expect: proved modulo one adopted step).**  For every
`n ≥ 2`, the size-`cap(n)` minors of `M_{3n−5}(F)` lie in `I(D_5^{det_n})`.
Expected proof route: (i) Jacobi — every parametrised member is singular
along `Z = pencil ∩ {rank ≤ n−2}`; (ii) Kleiman transversality (char 0,
applied to the rank strata) — for generic `(A_i)`, `Z` is `ν(n)` reduced
points of rank exactly `n−2`, the pencil misses rank `≤ n−3`, and the section
is smooth elsewhere; the Schur-complement expansion makes each point an
ordinary double point (this part proved, not adopted); (iii) the nodes fail
to impose independent conditions on forms of degree `2n−5` by at least one;
(iv) Dimca 2013 Thm 3.1 + the s37 Koszul bookkeeping (`docs/blindness_slab.md`
§5, adopted as pinned there) give `dim (S/J_F)_{3n−5} = μ + def_{2n−5} ≥ μ + 1`
on a dense subset, so the minors vanish there and on the closure.  The one
step *adopted* is Kleiman (and Dimca, already pinned by s37); everything
else is to be proved on the page.
*Falsifier:* a determinantal pencil at which `corank M_{3n−5} = μ_{3n−5}(n)`
(no drop) at `n = 3` or `n = 4` in exact arithmetic — that would contradict
the chain and stop the session.

**P1.2 (the defect at every `n ≥ 3`; expect: proved).**  I expect to prove
step (iii) for *all* `n ≥ 3`, not only `n = 3, 4`, by the Hilbert function of
the ideal `J` of `(n−1)`-minors of the pencil: with the Gulliksen–Negård
resolution (adopted; a resolution for the generic pencil because `J` has the
generic grade 4), `H_{S/J}(2n−5) = ν(n) − 1`, and `J ⊆ I_Z` forces the nodes
to impose at most `ν − 1` conditions in degree `2n − 5`.  At `n = 3` this is
the trivial `6 > 5 = h^0(O(1))`; at `n = 4` it is s35's `16 > 15`.
*Falsifier:* the polynomial identity `H_{S/J}(2n−5) = ν(n) − 1` failing
symbolically, or a measured `dim J_{2n−5}` at a random pencil *below* the GN
value at `n = 5` or `6` (measured ranks are lower bounds on the generic
rank, so a shortfall cannot be blamed on the pencil once two pencils agree).

**P1.3 (the `n = 3` corank re-verification; expect: measured 6 vs 5).**  At
three fresh integer pencils (box `±10^6`, seeds recorded), both primes,
`corank M_4(det M(s)) = 6` against `5` for random cubics and `5` for
`l·(random quadric)` controls.  *Falsifier:* any pencil giving 5, or the
two primes disagreeing.

**P1.4 (the conjecture; expectation, labelled).**  `onset I(D_5^{det_n}) =
cap(n)`: proved at `n = 2` (discriminant of quadrics generates the
rank-`≤ 4` ideal); at `n = 3` the record is `I(D_5)_δ = 0` for `δ ≤ 7`
(paper 1, measured totals) so the bracket becomes `[8, 65]`; at `n = 4`
`[8, 300]`.  I do **not** expect to prove the conjecture.  What kills it:
any length-5 bite below 65 at `n = 3` (Deliverable 4 is the test), or below
300 at `n = 4`.  My prior that the conjecture is true at `n = 3`: low-to-
moderate (it is extrapolated from a hypersurface case and from silence
through degree 7; the six-nodal locus at `n = 3` has other cheap invariants
— degree-10 `SL_5`-invariants of cubic threefolds exist — and nothing rules
out one of them vanishing on `D_5`).  This prior is recorded so the
Deliverable-4 cells are an honest test, not a confirmation exercise.

**P1.5 (the `n = 5` anomaly; expect: proved statements + one measured).**
`ν(5) = 50`, `codim D_5^{det_5} = 49`.  Expected reading: the tangent space
to the `ν`-nodal locus at a nodal `F` is `H^0(I_N(n))`; at a determinantal
`F` the tangent space of `D_5^{det_n}` is `J_n` (adjugate identity), of
dimension `3n² + 2` (GN); so `codim D_5^{det_n} = ν(n) − def_n(N)` when `J`
is saturated in degree `n`, and `ν(n) − H_{S/J}(n) = C(n−1, 4)` (to be proved
as a polynomial identity): `0, 0, 1, 5, 15` at `n = 3..7`.  The coincidence
`ν = codim` at `n = 3, 4` is `def_n = 0`; at `n = 5` the defect degree
`2n − 5 = n` and `def_5 ≥ 1` by P1.2.  Whether `D_5^{det_5}` is a component
of the 50-nodal locus reduces to `h^0(I_N(5)) = 77` exactly (measured, one
direction: upper semicontinuity makes a measured 77 a proof of `≤ 77`, and
GN gives `≥ 77`).  The cap theorem is unaffected: Dimca's equality only
needs `def_{2n−5} ≥ 1`, and a larger defect raises the corank further.
*Falsifier:* measured `h^0(I_N(5)) > 77` at two pencils (then
`D_5^{det_5}` may sit inside a larger nodal component; recorded as such).
*Bonus measurement:* the corank of `M_{10}` at a `5×5` pencil (expect
`102 = 101 + 1`) and of `M_{13}` at a `6×6` pencil (expect `256 = 255 + 1`);
these test Dimca + GN at fresh `n`.  A corank *below* prediction kills P1.2
at that `n`; above it means `def > 1` (saturation adds forms) and is
recorded, not a failure.

## 2. Deliverable 2 — `docs/paper1_delta0_patch.md`

**P2.1.**  Replacement text for the two places the bracket appears (the
closing paragraph of "Short weights: the length theorem", and Question
`q:delta0`), plus the intro sentence "in degree 80" if the integrator wants
it touched: new bracket `8 ≤ δ_0 ≤ 65`, one paragraph of argument in the
paper's notation (`D_5`, `\cO`, `\mult`, `a(λ,δ)`), Kleiman labelled as the
one adopted step, Dimca cited, one sentence placing the conjecture.  No
claim beyond Deliverable 1; the tex is not touched.
*Falsifier:* none (a write-up); the integrator's placement decides.

**P2.2 (optional paragraph, clearly separated).**  Question 8.5 asks
whether the generic six-nodal cubic threefold is determinantal.  I expect
to prove: `D_5` is the closure of the cubics singular at six points in
linearly general position (a frame).  Route: 6 frame points are
`PGL_5`-unique; cubics singular at the standard frame form a `P^4` (30
independent conditions — exact rank check); so that locus is irreducible of
dimension `≤ 24 + 4 = 28 = dim P(D_5)`; if the six nodes of a generic
determinantal cubic form a frame (open condition; one exact integer pencil
built to have all six nodes rational), `D_5` sits inside it and equality
follows.  *Falsifier:* rank `< 30` at the frame, or the six nodes of the
explicit pencil failing the frame test.  If either fails the paragraph is
withdrawn, not weakened.

## 3. Deliverable 3 — `docs/reducible_ideal.md`

**P3.1 (the theorem; expect: proved).**  For any `n, r, δ` and any padding
exponent `k ≥ 1`: a highest-weight vector `v` of weight `λ` in
`C[Sym^n C^r]_δ` vanishes on `X_r^{(k)} = {l^k · c}` iff every monomial of
`v` has, for every `i ∈ [r]`, a factor `c_α` with `α_i ≤ k − 1`.  (`k = 1`
is s36's (★).)  Proof: Bruhat `G = ⊔ B w P`, `X = G·L_r^{(k)} = ∪_i B·L_i^{(k)}`,
`B`-stability of the zero set of a `B`-eigenvector, and `I(L_i^{(k)})` a
monomial ideal.  Corollaries: `mult_{X}(λ, δ) = a − dim(HWV_λ ∩ span M_★)`;
`λ_1 < kδ ⇒ mult_X(λ,δ) = 0` (Kadish–Landsberg's padding bound, in full
generality of `k`, since every padded orbit closure lies in `X^{(k)}`);
onsets of `I(R_5)`, `I(R_6)` for quartics.
*Falsifier:* a counterexample vector (an HWV satisfying (★) that does not
vanish at a point `l·c`, or vice versa) — s36's 91 cells already exclude
this at `n = 4`; I will re-check (★) against the s36 exact certificate
`(8,4,4,4,4)` monomial list only if cheap.

**P3.2 (literature; expect: the *technique* is standard, the *statement*
not on record).**  One search pass: Chipalkatti (coincident root loci /
reducible forms), CGGHMNS (secants of reducible hypersurfaces), Kadish–
Landsberg 2014, Landsberg's GCT book (HWV-on-orbit criteria).  Verdict
written as found, with the exact KL statement quoted from its abstract.
*Falsifier:* finding (★) stated — then it is cited, not claimed.

**P3.3 (onset corrections; expect: one correction to s36's phrasing).**
By the restriction lemma `I(R_6)_5 ⊇` the length-5 image of `I_5`, so the
onset of `I(R_6)` as a whole is 5; what begins at 6 is its *length-6* part
(`I_6`).  I expect to state this and to verify `a((4,4,4,4,4,0), 5) = 1`
in six variables by plethysm.

## 4. Deliverable 4 — `results/n3_length5_plan.md`

**P4.1 (census; expect: measured table).**  `analysis/wk9_s36_census.py`
adapted to `n = 3`: every `λ ⊢ 3δ`, `ℓ(λ) = 5`, `a ≥ 1`, `δ = 8..12`;
columns `a, N_S, |Stab|, n_χ, GB = 2.5e-8 n_χ², fits (≤ 6.5 GB usable of 7)`.
`n_χ` by orbit enumeration where `N_S ≤ 4·10^5`, else the bound `N_S/|Stab|`
marked `~`.  Expectation: at `n = 3` the weight spaces are far smaller than
at `n = 4` (35 coefficient functionals, not 70), so most of `δ = 8, 9` and
much of `δ = 10` should fit; `δ = 11, 12` partially.

**P4.2 (validation before any new cell).**  (a) reduced pipeline at `n = 3`
reproduces the unreduced `wk8_s30_core.measure` (`a`, `N_S`, `mult_det`) at
three small cells with nontrivial stabilisers, both primes; (b) the `n = 4`
gate: `(8,4,4,4,4)`, `δ = 6` reproduces s36's `a = 2, mult_det = 2,
mult_pad = 1` through the same reduced code (a bite-detecting anchor).
*Kill:* any mismatch stops the runs; the plan is still delivered.

**P4.3 (runs; expect: `mult_det = a` at every cell run).**  The cheapest
three-to-eight cells (by `n_χ`, ascending, interleaved with the rectangular
`(6^5)` at `δ = 10` — the unique candidate `SL_5`-invariant cell in range,
run because an invariant vanishing on `D_5` would be the cheapest possible
kill), det side only, both primes, `a + 8` points, box `±40`.  Prior for
`mult_det = a` at each: ~0.9 per cell (from P1.4's prior on the
conjecture spread over the cheapest cells, which are the peaked ones least
likely to bite).  A bite fires the sceptical branch (3× points, seed 907,
both primes) and, if it survives, the exact-certificate branch of s36 and a
STOP: the conjecture is dead at `n = 3` and `δ_0` is pinned — that would
supersede Deliverable 2's bracket and is reported as the session's headline.
*Falsifier of the plan itself:* none; the plan is a table plus an ordered
list a compute session executes.

## 5. Kill criteria and honesty rules

- P1.3 failing (no corank drop at a fresh pencil) stops everything until
  explained; the integrator's three-pencil measurement would then be in
  question and the theorem withheld.
- A det-side bite in P4.3 is STOP-EVERYTHING for the remaining runs; the
  documents are then revised to record it as fact, with the certificate.
- No measured number is promoted to generic in the wrong direction: ranks
  at a point bound the generic rank *below*; dimensions of linear systems
  through a point-set bound the generic value *above*.  Every promotion in
  the deliverables names its direction.
- Nothing over 5 MB is committed; logs under `results/logs/`; single-writer
  files untouched; no pushes; delivery by `onsetconj.bundle` (single ref).
