# Integrator review — session 67 (C6), and the S4/S5/S6 reports

## Part I — session 67: accepted and merged

Bundle md5 `a3c8ce5629ffc0e7680f41cbea78043b` matches, ancestry against
`226b4ef1` passes, 8 commits, 285 files.

**Self-test: 10/10**, including case 7 (the 4515-digit `nonvanishing_minor`
regression for the session-56 defect) and cases 9 and 10 (the new field
discipline).

**Adversarial testing done here, independently of the session's own audit.**
Four certificates put through `tools/verify/verify.py` — one genuine, three
forged by me from it:

| input | verdict | message |
|---|---|---|
| genuine `sparse_nullity` | **PASS** | `mult_det = a = 5` over `Q` from `nullity_p = 0`, `rank_p ≤ rank_Q ≤ a` |
| `recipe.N_S` inflated to 999999 | **FAIL** | "recorded 999999, true 4942 — certificate misrepresents its size" |
| `nullity` forged to 1 (claiming `i_det = 1` where the truth is 0) | **UNPARSEABLE** | "nullity > 0 must record the checked kernel vectors in `basis`" |
| `field` relabelled `F_p → Q` | **UNPARSEABLE** | "field must be a finite field … a char-0 nullity is not this kind" |

The third is the one I most wanted to test and it is the right behaviour:
**an obstruction cannot be claimed without exhibiting it.**  The second confirms
the audit's own fix (the forged-size exploit) is real, not just reported.  The
fourth enforces the distinction that this whole batch has been turning on.

**The `PASS` / `RECORDED` split is exactly right** and should be kept as a
standing convention: 21 re-derived (`PASS`), 243 reproducible but not re-derived
(`RECORDED`), and the difference is stated rather than blurred.  Re-deriving one
cell costs a build plus a Wiedemann sequence — I confirmed that the hard way,
timing out on a `N_S = 56 427` cell before dropping to the smallest.

**Part B is honestly reported.**  Sound (0 false certifications over 51 cells),
cheap on a real class (27 of 32 nontrivial-reducible cells, point-free), and
intrinsically limited elsewhere — 99.4–99.9% of columns and no further, precisely
near the rectangular corner where a determinant equation would live.  The
conclusion that only a *hybrid* is worth a successor's time is the right call,
and the one-directional discipline (a shortfall is uninformative, never an
obstruction) is stated correctly throughout.

**Part C's correction to session 60 is accepted and matters:** the int64 wall was
at `δ_close = 20`, not `δ ≥ 19`; `CODE_SAFE_DELTA = 18` was conservative by one,
1 048 cells were already int64-buildable, and only the 27 `δ_close = 20` cells
genuinely overflowed.  **Buildable closing cells 892 → all 1 075.**  Bit-identity
on seven cells up to `n_χ = 70 027`, no banked value changed.

## Part II — S5: confirmed independently, and the polar branch is closed

S5 reports `det_5`'s polar profile as `(5,20,80,220,430,580,520,280,70)`.
Computed here from the dual Segre by the classical polar-class formula
(`analysis/wk10_int_polar_dual.py`), sharing nothing with S5:

    mu_k(Segre P^3 x P^3) = 20, 60, 84, 68, 36, 12, 4
      reversed (biduality) = 4, 12, 36, 68, 84, 60, 20   = the BANKED det_4 profile ✓

    mu_k(Segre P^4 x P^4) = 70, 280, 520, 580, 430, 220, 80, 20, 5
      reversed             = 5, 20, 80, 220, 430, 580, 520, 280, 70   = S5's det_5 ✓

**The method reproduces `det_4`'s measured profile exactly**, which is the
calibration that makes the `det_5` value trustworthy.  And the last entry, 70, is
`C(8,4)` — the integrator's own prediction in `docs/batch10_plan.md` §4 (S5),
derived from the dual being the Segre of dimension `2n−2` and degree
`C(2n−2,n−1)`.

**Verdict: `δ_6(det_5) = 520 ≫ 30`.**  The question that opened S5 — *is
`δ_6(det_5) < 30`?* — is answered decisively negative, and **the conormal route
caps at `dc̄(per_3) ≥ 5`.**  Bank it as a closed branch; it cost minutes and it
retires a line the plan was right to bound rather than fund.

**One note on the replication no-go, so the two directions are not confused.**
S5's block-diagonal row says the direction is wrong — restriction carries
large-`n` equations *down* to small `n`, not up.  Correct, and it does **not**
conflict with the `ℓ·det_3` route of `docs/one_plus_three_assessment.md`: there
the same downward direction is exactly what is wanted, since
`X_{1+3} ⊆ D_9` gives `mult_X ≤ mult_det`, a *lower* bound on the determinant
multiplicity from a smaller family.  The unsafe direction is transporting a
kernel *upward* in `n`, which is what S5 rules out.  Same functoriality, opposite
uses; both are right.

## Part III — S6: the family formula is a genuine addition, and it checks

    delta_n = 2n(n-1),   lambda_n = (2n^3 - 4n^2 + 1,  2n^2 - 4n + 1,  2^{2n-1})

reproduces both cells exactly — `n=3 → (19,7,2⁵)` at `δ=12`, `n=4 → (65,17,2⁷)`
at `δ=24` — and `|λ_n| = 2n²(n−1) = n·δ_n` identically, so it is degree-correct
at every `n`.  (I first checked it against `4δ` and flagged a false error; the
ambient is `Sym^δ(Sym^n)`, so the condition is `n·δ`.  My mistake, recorded.)

**The observation worth banking is the stability boundary.**  With
`ρ_n = (2n²−4n+1, 2^{2n−1})`, `|ρ_n| = 2n²−1` and `(ρ_n)_1 = 2n²−4n+1`, so

    |rho_n| + (rho_n)_1 = 4n^2 - 4n = 2 * delta_n        EXACTLY, for every n

checked at `n = 3,4,5,6`.  **The whole LMR family sits on the rectangular-
stability boundary at exact equality** — which is why Manivel's reduction is
available at these cells at all, and it explains a fact the record had only for
`n = 4`.

**And a consequence S6 does not draw.**  `t_n = |ρ_n| = 2n²−1` against
`δ_n = 2n²−2n`, so `δ_n < t_n` for every `n ≥ 1`: **every LMR cell lies below the
proved stable threshold.**  Therefore the monotonicity argument of
`docs/stable_coordinates.md` §2 — `i_det(δ_n) ≤ i_det^∞(ρ_n)`, so a stable value
of 1 settles the cell with no rank at `δ_n` — is available at **every** `n`, not
only at `n = 4`.  If the stable computation is ever made to work, it settles the
family, not one member.

**The kernel-vector caution is correct and should be enforced.**  There is no
`n = 4` line in common source coordinates; the `n = 3` artefact is a calibration
and not a substitute, and C4 must not compare `U_P` against it.  The "safe
statement for C2/C4" is exactly the right thing to hand forward.

## Part IV — S4

Assessed in full at `docs/s1_s4_assessment.md` Part II.  The new document adds
the flag-incidence formulation (`π(v ∧ E) = 0` as a condition on a `4×6` matrix
plus `[v] ∈ P³`), which is a real improvement over searching for the incidences.
Nothing further to check; the exhaustion statement remains the named gap and
should be reported separately from whatever components C5 certifies.
