# Session 74, complete — reviewed

**Delivery.**  `s74_births.bundle`, md5 `0693bba7…718c` matching, base `afb8c33`,
39 commits (history rewritten since the checkpoint to drop two 6.8 MB generic
columns, which is the right handling of the five-megabyte rule).  There is
no session-link trailer and no external URL anywhere; commits carry `Co-Authored-By: Claude Fable 5.1` —
the model that ran the session — with the deviation from the preamble declared
in PREREG §8.  Truthful attribution is the right call; accepted.

**Verification.**  `analysis/wk12_int_s74_final.py`, **54 of 54**, on top of the
checkpoint's 47 of 47.  Every rank recomputed here from the delivered *native*
values, with the transport applied by my code, `msym_u` recomputed exactly over
`Z` from each point's own integer data — `4!·det A₁`, `4!·per A₁`,
`4!·ℓ₁·per B₁`, `4!·ℓ₁·c_{s₁³}`, `4!·c_{(4,0,…,0)}` for the five families — and
my own elimination.  My `msym_u` agrees with s74's stored `u_symbol` at all 282
points of all five families at both primes, and no delivered point is a
`u`-zero.  `u` resolved by `exps(4,9).index(...)`, index 494, never a literal.

| column | rank / nullity, both primes | reading |
|---|---|---|
| generic | **274 / 0** | the 274 transported births **are** a basis of `M₂₄` — falsifier F3 cleared |
| `det₄` | **273 / 1** | with LMR, `rank T_det = 273` **exactly**, `i_det(24) = 1` |
| `ℓ·per₃` | **269 / 5** | certified floor 269 |
| `ℓ·c` | **269 / 5** | `U_R = U_P`: the *same* five-space at both primes |
| `per₄` | **274 / 0** | `i_per4 = 0` |

The five padded kernel vectors are supported on rungs 13 (three) and 14 (two),
none touches the δ=24 birth row, and the LMR line `y` is nonzero at 282/282
padded, reducible, `per₄` and generic points at both primes.  The five-column
ladder agrees rung by rung.

## 1. The finding, which is not the number

`U_R = U_P` — at the goal cell and, measured here independently at rung 13
(`docs/rung13_reducible.md`), on a different point stream with a different
evaluator.  Together with `i_per4 = 0`:

- the **unpadded** permanent has **no** equation in this weight;
- every equation the **padded** permanent has is an equation of the reducible
  locus `ℓ·c`;
- the determinant has exactly one, LMR's.

So in the weight `(65, 17, 2⁷)` the statistic **cannot distinguish `ℓ·per₃` from
`ℓ·c`.**  It is measuring reducibility, not permanence.  `mult_pad = mult_red`
at every rung of the ladder, at both primes.

This is `docs/brief_wording.md` §5's committed three-point test run at the goal
cell, and it answers the question §5 poses: (2) and (3) do not disagree.  §5
says that where they disagree, the disagreement is the result; here they agree
exactly, and *that* is the result.

`D = mult_pad − mult_det = mult_red − mult_det` at this cell, so whatever `D`
turns out to be, it is a statement about the reducible locus against the
determinant, with `per₃` playing no part.  s64 found `mult_pad = mult_red` at
`r ≤ 5`; it recurs here at `r = 9`, `δ = 24`.

**The screen this hands the programme.**  `mult_pad ≤ mult_red` always, so a
cell can carry permanent-specific information only where `mult_pad < mult_red`.
`mult_red` is a multiplicity of the *reducible* variety — the image of
`(C⁹)* × S³ → S⁴`, classical, with no permanent in it and no orbit closure to
sample.  **Compute `i_red` first, and spend evaluation only on cells with
`i_pad > i_red`.**  That is cheap, reusable, and it is the most transferable
thing this cell has produced.

## 2. The arithmetic that is settled, and the one thing that is not

    rank T_det(24) = 273   exactly        PROVED (transported 273-minor + the
                                          birth-quotient proposition + LMR)
    i_det(23) = 0          exactly        PROVED
    i_pad(24) = i_pad(23)  (eps_pad = 0)  PROVED (no kernel vector touches the birth row)
    rank T_pad(24) >= 269                 CERTIFIED
    D = 1 - i_pad(23)  =  1 - i_red(23)   PROVED
    -4 <= D <= +1                         PROVED;  D = -4 MEASURED, not certified

The measured `−4` now rests on two primes, two point families (boxes 30 and
1000), two evaluation paths and — from my side — a third evaluator and a third
point stream at rung 13.  It is as well-supported as a sampled value gets.  It
is still not a theorem, and s74 correctly declines to enter the negative
decision-table branch.

**What would make it one.**  `i_red(13) ≥ 1` over `Q`: a single certified
element of `I(V_red) ∩ M₁₃`.  Then `i_pad(13) ≥ 1`, `i_pad(23) ≥ 1` by
monotonicity, and `D ≤ 0`.  It is a 39-dimensional question about a classical
variety, and `F ∈ I(V_red)` iff `F` is in the kernel of the pullback along the
multiplication map — finite exact linear algebra, no points, no permanent.

## 3. Session S3's continuation, and why it is now the right instrument

S3 delivered a complete 39-dimensional rung-13 basis with certified conversions
and generic and determinant rank 39 at both primes.  Checked against what is
banked here:

- **`a₁₃ = 39` a third time.**  S3's root residual is `2383 × 315` of rank 276
  with a 39-dimensional kernel.  That agrees with my cold-cache Weyl-alternation
  recount (`results/logs/wk12_int_fresh_a13.log`) and with s74's ladder, from
  three unrelated constructions.
- **`i_det(13) = 0` twice, from unrelated sources.**  S3 gets it from a
  recursive rational source; s74 from bracket-filling births.  The determinant
  column at rung 13 is now doubly independent.
- **`6,084 = 4 × 39²`** — two matrices at two primes on a 39×39 grid, as the
  report's own arithmetic requires.
- The report is honest where it costs it: a coordinator ran 2,065.766 s against
  a 420-second bound, recorded openly, with no further queries launched after
  detection; and its closing line — "determinant rank 273, true-padded rank 274
  and `D = 1` remain open" — was written before s74 landed and is superseded on
  the determinant half.

**The connection nobody has made.**  S3's source is *rational*, by a specified
convention rather than by reconstruction from residues: "this defines actual
rational vectors".  The one thing the LMR cell still needs is a
characteristic-zero membership statement at rung 13 — and S3 is the only
instrument in the programme that has rung 13 over `Q`.  The three reducible
candidates, written in S3's rational basis, become exact rational vectors, and
their membership in `I(V_red)` becomes the finite exact question of §2.  **That
is the next session.**

## 4. Smaller things

- `skipped_points` now reads correctly: eight reducible and two padded points
  were skipped for `msym_u = 0` and are recorded.  The checkpoint's confusing
  `[243, 263]` on fully-populated columns is resolved.
- The certificates are `sparse_nullity` in the session-67 spelling but are
  **RECORDED-class by construction**, as s74 says: the verifier re-derives by
  enumerating the weight space, and `N_S = 1.56 × 10¹¹` is not reachable.  s74's
  warning that the enumeration runs *before* the `VERIFY_MAX_NS` guard is a real
  defect in my verifier and I will fix the guard's position rather than avoid
  the files.
- `N_S(λ₂₃) = 156,419,279,221` and `N_S(λ₂₄) = 156,438,903,314` recounted by an
  exact multiset DP, both matching `docs/lmr_cell.md` §6.
- The compact-state DP is a real engineering result: 2.5–8× per evaluation and a
  clean 2× from a second core, validated entry for entry against `dp_eval_c` on
  50 pairs across rungs 12–24 at both primes.  A `274 × 282` column is 20–45
  minutes instead of hours.

## 5. Status

| claim | status |
|---|---|
| a complete, certified 274-vector source at the goal cell | **DELIVERED**, generic nullity 0 verified here |
| `rank T_det(24) = 273`, `i_det(24) = 1` | **PROVED** |
| `y` is the LMR equation and `y ∉ I(pad) ∪ I(red) ∪ I(per₄)` | **CERTIFIED** on residues at 282/282 points, four families, both primes |
| `rank T_pad(24) ≥ 269`, `D ∈ [−4, +1]` | **CERTIFIED** |
| `i_per4 = 0` — the unpadded permanent has no equation here | **CERTIFIED** |
| `U_R = U_P`, `mult_pad = mult_red` at every rung | **MEASURED** at both primes, at rung 24 and independently at rung 13 |
| `D = −4` | **MEASURED**, not certified; the negative branch is not entered |
| the LMR cell as a **permanent** obstruction | **settled against**: this weight does not see `per₃` at all |

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
