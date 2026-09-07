# Programme stock-take at the end of batch 10

Eleven of the twelve planned sessions ran: C1/s62, C2/s63, C3/s64, C5/s66,
C6/s67 on the implementation side; S1–S6 on the theory side.  **C4/s65 did not
run**, correctly — its gate never opened.  §6 says what to do with it.

Everything below is either verified independently here or labelled as relayed.

---

## 0. The verdict in one sentence

The batch did not resolve the LMR cell, and **it converted that failure from a
vague cost estimate into three quantified walls of different kinds, all of which
turn out to have one cause** — every route needs an explicit basis of the
274-dimensional source `M_λ`, and every construction the programme owns realises
that basis inside a carrier of size `≥ 10⁷`.

---

## 1. What was banked that the programme did not have

**The first rank drop in its history, and it is two-sided.**  At the `n = 3` LMR
cell `((19,7,2⁵), 12)`: full rank at `δ = 9, 10, 11` and `mult_det = 5 < 6 = a`
only at `δ = 12`, both house primes.  The instrument does not under-report rank;
the drop is genuine.  With it, an explicit highest-weight vector in
`I(D_7^{det_3})` — the programme's first exhibited candidate equation, with the
right caveat attached (finite-point vanishing is Schwartz–Zippel evidence of
ideal membership, not a proof; the rigorous `i_det ≥ 1` is still LMR's theorem).

**A proved two-sided calibration of the Gram machinery.**  `n = 2`: `det_2` is a
rank-4 quadratic form, so the `(2^δ)` discriminant is nonzero for `δ ≤ 4` and
identically zero for `δ ≥ 5`.  Reproduced here from scratch — full rank at
`δ = 3, 4`, identically zero at `δ = 5, 6`, two seeds × two primes.  **The only
place in the record where a theorem fixes the answer on both sides**, and the
machinery matches it.

**The `n = 3` predecessor argument, end to end.**  `mult_det(11) = 5` full rank
+ ladder monotonicity + LMR pins `i_det(12) = 1` — the 273/274 deduction
rehearsed at a size that is affordable, before it is trusted at `n = 4`.

**The padded side, from "conceptually missing" to calibrated.**  S3's
factorization `M^{(4)}_λ → ⊕_μ M^{(3)}_μ → ⊕_μ M^{(3)}_μ/K_μ`; s64's engine on
the *same* source coordinates as the determinant, 48/48 cells, 12 of them
discriminating, with two kernel witnesses verified here against independently
generated points, and an `r ≥ 6` separation at the sample-variety level
(`dim P_6 = 55 < 61 = dim R_6`) proving the engine is not silently the reducible
one.

**`h_pad` at LMR = 521**, computed here.  Since `mult_pad ≤ h_pad` is proved and
`521 > 274 = a`, **the pad-side ceiling is entirely vacuous at LMR** — the cheap
screen that settles cells elsewhere has nothing to say, and a rank is genuinely
required.  That is the strongest argument the batch produced that C2/C3 were
worth their cost.

**The LMR family in closed form** (S6): `δ_n = 2n(n−1)`,
`λ_n = (2n³−4n²+1, 2n²−4n+1, 2^{2n−1})`, `ℓ(λ_n) = 2n+1`, `|λ_n| = n·δ_n`
identically.  And `|ρ_n| + (ρ_n)_1 = 4n(n−1) = 2δ_n` **exactly at every `n`** —
the whole family sits on the rectangular-stability boundary, which is why
Manivel's reduction is available at these cells at all.  Consequence S6 does not
draw: `t_n = 2n²−1 > δ_n = 2n²−2n` always, so **every LMR cell lies below the
proved stable threshold**, and the monotonicity route (`i_det(δ_n) ≤ i_det^∞`)
is available for the whole family, not one member.

**A second ladder.**  `det(A_1)` is a highest-weight vector of weight
`(4,0,…,0)` in the tail variables and a nonzerodivisor on `C[M_ℓ]`, so `i_det`
is monotone in the tail's first part.  Wrong direction for the goal cell; right
direction for widening the stable dead region.

**Certification.**  264 algorithmic proofs now machine-checkable, field
discipline enforced by the format, both engineering defects fixed, and all
1 075 closing cells buildable (was 892).  Tested here with four forged
certificates: an inflated size `FAIL`s, a forged nullity is rejected because the
schema requires the kernel vectors to be exhibited, and a finite field relabelled
as `Q` is rejected.  **An obstruction cannot be claimed without exhibiting it.**

**The contact-order lemma** (s66, proved): at a smooth point of `V(J)` the
exceptional fibre is `P(im dΦ)` at every order.  This turns s59's measured
"invariance of contact order" into a theorem *and* localises any hidden component
of the exceptional divisor to `Sing V(J)` — which is exactly the locus s66 then
measured.  It is what makes s66's enumeration an argument rather than a survey.

---

## 2. What died — twelve more routes

| # | route | killed by |
|---|---|---|
| 1 | the conormal/polar method beyond `n = 4` | `δ_6(det_5) = 520 ≫ 30`; verified here by an independent route that reproduces `det_4`'s measured profile exactly |
| 2 | a global commutative spectral algebra | `Sym⁴(Sym⁴)` not multiplicity-free (28 constituents, five of multiplicity 2, `Σa² = 43`); and `β_4` **measured noncentral** (s62) |
| 3 | birth morphology as a selector | unimodal 2 107/2 107; `ε = 1/a_∞` puts LMR at rank 632 of 885, on the wrong side |
| 4 | the Foulkes enumeration Gram | dead at `δ = 5` (7.4 min/pass × ~192 weights) |
| 5 | the reduced Gram route at LMR | `|S|` plateaus at `0.20–0.26·n_χ` and reaches `n_λ` at 11 of 28 `δ=4` cells; it does not thin |
| 6 | generic contact order `q > 4` at `r = 5` | the contact-order lemma makes s59's invariance a theorem at smooth points |
| 7 | transverse directions at the compression incidences | quotient **0** at every point tested, in both the compression and primitive worlds |
| 8 | a climb over the primitive family at orders 1–3 | every reducible image `≤ 29 < 31 ≪ 35`, at every incidence, both primes |
| 9 | Adams, plethysm, wreath, block-diagonal, Kronecker as kernel transporters | wrong functorial direction — restriction carries large-`n` equations *down* |
| 10 | three weight-13 stable tails | `(7,2,2,1,1)`, `(5,5,1,1,1)`, `(5,3,3,1,1)` all have `i_det^∞ = 0`, run here |
| 11 | border `3×3` determinants at `r = 5` | `dim{det_3 cubics in 5 vars} = 29 < 35` |
| 12 | initial-term degeneration as an obstruction finder | one-directional only; it certifies full rank and can never evidence a drop |

Twenty-four dead routes across batches 9 and 10.

---

## 3. What is still open

- **`i_det` at the `n = 4` LMR cell.**  The batch's central goal.  Not certified.
- **`i_pad` at LMR**, hence `D_LMR`.  Not attempted (C4 did not run).
- **`R_5 ⊄ D_5`.**  Still needs the upper bound — the special-fibre algebra of
  `J`, or a length-5 equation of `I(D_5)` above degree 9.  s66 removed the last
  mechanism the roadmap had for a climb; it did not supply the bound.
- **`m_0(6) ≥ 14`.**  Three of 47 weight-13 shapes closed; the other 44 have
  `a_∞ ≥ 2` and need ranks, not scalars.
- **A row-efficient replication operator.**  The named target is a wreath/`Θ`
  intertwining square `S_q Θ_{n,δ}^+ = Θ_{nq,δ'}^+ R_q` with row growth `o(nq)`.
  No such square is established.

---

## 4. The single diagnosis

Every route to the LMR cell hits a wall, and the walls look different but are
not:

    native HWV build   n_χ = 3.10×10⁷ , N_S = 1.56×10¹¹ ; 14.4 TB, ~415 days
    Foulkes column     |H_{4,24}| = 1.2×10⁹³
    reduced Gram       |S| ≥ 6×10⁶ (of n_χ) ; entries cost ~273·|S|²

And every proposed workaround **relocates** the cost rather than removing it:

- the Gram route removes the 48 825-dimensional target and puts the cost in the
  entries;
- the stable picture (Proposition S) shrinks the carrier by a measured 21.7×
  (`3.10×10⁷ → 1.43×10⁶`) and is still 15× past anything built;
- the `ℓ·det_3` route takes the target from 48 825 to 521 and leaves the source
  untouched;
- S3's padded factorization does the same on the padded side.

> **The bottleneck is not the rank, not the target, not the field.  It is
> constructing 274 vectors.**  `M_λ ≅ [λ]^{S_4≀S_24}` has dimension 274 from
> birth; every construction the programme owns realises it as a kernel inside a
> carrier of size `≥ 10⁷`, and that is the only reason the cell is out of reach.

The one route nobody has tried is to build those 274 coordinates **directly**,
by seminormal/Jucys–Murphy branching up the wreath chain
`S_4≀S_1 ⊂ … ⊂ S_4≀S_24`, never forming the carrier.  The pre-registrable number
is the **maximum live branching-state count** through `δ = 12, 14, 16, 18`.  If
it stays in the hundreds or thousands, everything above unblocks at once — C2's
rank, C3's split matrix, C4's orientation, and the stable route as a bonus.  If
it reaches `10⁶` despite a multiplicity of 274, that is a real theorem about the
obstruction and the programme should say so and stop.

---

## 5. Corrections ledger — and the process finding

**Four items specified as missing turned out to be already banked.**

| described as missing | actually |
|---|---|
| the Gram / double-coset observation | session 56, in `wk9_s56_hecke.py`'s docstring |
| the `h_pad` Pieri identity | session 42, implemented and **proved** via Kempf collapsing |
| the padded evaluation family | sessions 36/41, `forms['pad'] = (PAD34, N_PAD)` |
| a separation test above `r = 5` at the multiplicity level | session 47 proved `mult_pad = mult_red` at every reachable `r = 6` cell — my proposed test was **vacuous as stated**, and s66/s64 replaced it with a sample-variety test |

Common cause: **batch 10 was specified from documents and summaries, and the
code was ahead of them every time.**  For batch 11: read the code before writing
the brief, cite the file rather than the memo, and push the plan before the
briefs go out (s62 and s66 both cloned a tree that did not contain it).

**Corrections to the integrator, recorded.**

- My `|S|` extrapolation was wrong.  Note 2 concluded "both walls measured,
  stop"; note 3 withdrew it because three points could not carry four orders of
  extrapolation.  The sessions measured it and **note 2 was right** — the support
  does not thin, it plateaus.  The withdrawal was premature.
- My Schur denominator was wrong — it is the *current-degree* Gram restricted to
  the transported predecessor, not the predecessor's own Gram.  S2 caught it; I
  verified the correction on an explicit instance.
- I checked S6's family formula against `4δ` when the condition is `n·δ`, and
  flagged a false error.

**Corrections to the workers, recorded.**

- The "four transverse directions" at `C_21 ∩ C_32` is zero.  It surfaced in
  three documents after being corrected once; it is now retired everywhere.
- S1's raising-operator formula is the divided-power normalisation and does not
  pair with the plain-coefficient substitution.  Both give a one-dimensional
  kernel, so the multiplicity check cannot see the mismatch, and a
  non-highest-weight vector evaluates nonzero generically — **the test as
  specified would have produced an unfalsifiable negative.**  Caught by a
  covariance check the memo did not include.
- s66 found a 49-dimensional semi-primitive component absent from every stratum
  list since s32, and showed `P ∩ ker` is a rank-`≤2` locus, not a rank-3
  incidence — the genuine `n = 4` analogue of Hüttenhain–Lairez.
- s67 corrected s60's int64 wall (`δ_close = 20`, not 19).

---

## 6. Session 65

**Its gate never opened and it should not run as briefed.**  C4 needs `i_det`
and `i_pad` at LMR; C2 reached neither and C3 correctly did not attempt them.

**It should not be re-pointed at `n = 3` either**, and the reason is structural
rather than practical.  `per_2(A) = a₁₁a₂₂ + a₁₂a₂₁` and
`det_2(A) = a₁₁a₂₂ − a₁₂a₂₁` are both rank-4 quadratic forms in four variables,
hence `GL`-equivalent over `C`.  So the padded `per_2` in degree 3 is `ℓ·det_2`
up to `GL`, which is the block split `diag(ℓ, A_2)` **inside** `det_3`:

    P_{n=3} = closure{ℓ·per_2} = closure{ℓ·det_2} ⊆ D_{n=3}
      ⟹ I(D) ⊆ I(P) ⟹ i_det ≤ i_pad ⟹ D ≤ 0 always at n = 3.

**The `n = 3` LMR cell can never carry a multiplicity obstruction.**
Permanent-versus-determinant separation genuinely begins at `m = 3`, and the
`n = 3` cell is a calibration for the machinery and nothing more.

There is also no `r = 5` cell where orientation can be exercised: s60 measured
`mult_det = a` at all 419, so `i_det = 0` and `U_D = 0` everywhere there.

**Recommendation: hold s65 unchanged.**  Its brief is correct and will be usable
without edit the moment a source basis exists.  Its *slot* in batch 11 goes to
the source construction, and s65 runs immediately after that lands.

---

## 7. What batch 11 should be

One session decides the batch, and it is not a measurement:

1. **The direct source construction.**  Build `M_λ` at dimension 274 by wreath
   branching, never forming the carrier.  Pre-register the maximum live
   branching-state count at `δ = 12, 14, 16, 18`.  Everything else waits on this
   number, and it is worth funding two independent attempts rather than one.

Then, gated on it and in this order:

2. **`rank S_{λ,24}`, the `274 × 521` split** — one rank that yields `mult_red`
   at LMR (a number the record does not hold) *and* gates the `ℓ·det_3` route,
   since `X_{1+3} ⊆ R_9` forces `i_red ≤ i_X` and the route needs `i_X ≤ 1`.
3. **`det A_24`, the `273 × 273` restricted Gram** — characteristic-free, both
   house primes; nonsingular gives `i_det = 1` outright.
4. **s65 unchanged** — `i_pad`, `U_P`, `dim(U_D ∩ U_P)`, and the three-outcome
   decision table.

Ungated alongside: the `a_∞ = 2, 3` weight-13 stable shapes (the machinery is
built and each is minutes); the `r = 5` upper bound, which is the only thing
that would settle `R_5 ⊄ D_5` and which s66 explicitly did not supply; and the
wreath/`Θ` intertwining square, which is the only named path to asymptotic reach.

**And if the source construction fails**, the batch's honest output is a
theorem-shaped statement about why: a multiplicity space of dimension 274 that
cannot be realised below `10⁷` coordinates is itself a result, and the write-up
— twenty-four dead routes, the ladder theorem, Theorem P, Proposition S, the
contact-order lemma, the specialisation inequality, the conormal certificates —
does not depend on it.
