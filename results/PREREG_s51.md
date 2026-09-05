# Pre-registration — session 51 (the Λ⁵ structure, derived from the resolution)

Branch `s51-lambda5`, off `eb8cecb` (ancestry gate: `eb8cecb` is HEAD of `main`
as staged; `git merge-base --is-ancestor eb8cecb HEAD` holds).  Committed
**before any rank, nullspace or character in §2–§4b is written down as a
result.**  Labels used in the report: **proved / measured / certified /
adopted-from-literature / expectation**.

Convention throughout: `F = det_n` restricted to a generic `r`-dimensional
pencil `M(s) = Σ sᵢ Aᵢ`, `d = 3n−5`.  `drop = ρ_d − rank M_d(F)` where
`ρ_d = dim Sym^d ℂ^r − h_d`, `h_d = [t^d]((1−t^{n−1})/(1−t))^r`.  A syzygy of the
`r` partials `∂ᵢF` (degree `n−1 = 3`) at internal degree `d` is a tuple
`(gᵢ)`, `gᵢ ∈ S_{d−3}`, with `Σ gᵢ ∂ᵢF = 0`; **non-Koszul** = modulo the
`C(r,2)·dim S_{d−2(n−1)}` Koszul syzygies.

## Note on infrastructure state (recorded, not a result)

The batch briefs `docs/s49_prompt.md … s55_prompt.md` are committed, but sessions
49 and 50 **have not been run**: there is no `tools/verify/`, no
`docs/s49_report.md`/`s50_report.md`, no `results/certs/`.  Two consequences,
both honoured below:
- the cap corrections of s49 §2.1 (**1148 proved / 661 certified**, replacing the
  repository's 1197/666) are *adopted as stated in the s49 brief*, not
  re-derived here except where §2 recomputes the relevant Hilbert functions;
- "hand the check to the session-49 verifier" is met by an **independent
  ℤ-checker written this session** (`tools/verify_s51.py`, sharing no code with
  the worker toolkit) implementing the s49-brief verifier spec (layer 1
  syntactic over ℚ + two primes and exact ℤ; layer 2 semantic: weight, degree,
  variable count, and that the recorded pencil really is `det_n` of the recorded
  matrices).  Its existence and clean run are themselves logged as a result.

## What will be measured, and the positive-result bar

### P1 — the drop is `C(r,5)` and the regime is stated (§2 count)
Recompute `drop` at `n = 4`, `d = 7`, `r = 4,5,6` and confirm `0,1,6 = C(r,5)`;
confirm at `n = 5`, `d = 10`, `r = 7` the drop `21 = C(7,5)` is reproduced (s48
value).  **Positive:** all four reproduce `C(r,5)` at both house primes, AND the
GN-ceiling regime is stated precisely (`C(r,5)` is the drop only where the
Gulliksen–Négård ceiling `dim S_d − H_{GN}(d)` does not bind; where it binds the
drop is larger, which will be exhibited at `n = 3`, `r = 6,7` as the negative
control).  Prior 0.90.

### P2 — the count derived from the resolution, not read off a rank (§2)
Give `dim(S/J_F)_d` as a combination of Hilbert functions of the **restricted
Gulliksen–Négård complex** of `I_3(M)` (the ideal of `3×3` minors, codim 4,
`0→S(−8)→S(−5)¹⁶→S(−4)³⁰→S(−3)¹⁶→S`) plus the generic-position term relating the
`r`-generated Jacobian ideal `J_F` to the 16-generated `I_3·S`.  **Positive:**
the resolution-derived number equals the measured `dim(S/J_F)_d` at
`n=4, r=4,5,6`, and the "`5`" is identified as `codim(Σ_{n−2}) + 1 = 4 + 1`
(independent of `n`), consistent with the `n=3` reproduction of `C(r,5)` at the
one non-ceiling case `r=5`.  A number of the **wrong** dimension is the negative
worth reporting (brief §6).  Prior 0.80.

### P3 — the `r = 5` syzygy exhibited exactly and verified over ℤ (§3)
Extract the unique (up to scale) non-Koszul syzygy at `(n,r,d) = (4,5,7)` as an
**exact rational** tuple `(g₀,…,g₄)`, `gᵢ ∈ S₄`.  **Positive:** `Σ gᵢ ∂ᵢF = 0`
verified as an exact identity over **ℤ** (every coefficient, integer pencil), not
mod p, and re-checked by the independent ℤ-checker.  Prior 0.90.

### P4 — a closed FORM for the `r = 5` syzygy (§3, the hard part)
A short formula for `(gᵢ)` in the pencil (`M`, `adj M`, the `Aᵢ`), verified over
ℤ.  Pre-registered honest state: single-adjugate words (`T_{ab}=tr(adj(M)AₐMA_b)`)
and two-adjugate words of shape `gₐ = (adj entry)·(linear)` have **already been
ruled out** in exploratory runs (they capture 0 of the 1 non-Koszul dimension),
consistent with s48 ruling out the one-adjugate ansatz.  So a clean word formula
is unlikely.  **Positive:** any explicit construction reproducing the exact
`r=5` syzygy and verified over ℤ.  Prior **0.25** (s48 gave the analogous A1
prior 0.30 and it failed).

### P5 — the module is `Λ⁵ℂ^r` (the equivariant type) (§4)
Identify the `GL_r`-representation carried by the non-Koszul syzygy space.
Route: the transport law `Σ_b g_{ab} g'_b(s) = χ(g)·gₐ(gᵀs)` defines a character
`χ` on the `r=5` (one-dimensional) syzygy line; measure `χ(g)` for explicit
`g ∈ GL₅` (a scaling and a coordinate permutation).  **Positive:** `χ(g) =
det(g)` exactly (so the line is `Λ⁵ℂ⁵`, the determinant representation), i.e.
`χ(diag(t,1,1,1,1)) = t` and `χ(σ) = sgn(σ)` for a transposition `σ`; and the
dimension `C(r,5)` matches `dim Λ⁵ℂ^r` at `r=4,5,6,7`.  This is the
"partial success worth having" of brief §6 and settles what s48 left open
(A2/A3).  Prior 0.70.

### P6 — the `(5,7)` consistency test (§4)
The `Λ⁵` identification must predict the measured drop `21` at `(n,r) = (5,7)`.
`dim Λ⁵ℂ⁷ = C(7,5) = 21`.  **Positive:** `21`, matching s48's measured value; a
prediction of anything else falsifies the module (brief §4).  Prior 0.90.

### P7 — §4b: the Fitting degree, and the degeneracy-direction pre-check
Build a universal presentation map `Ψ_f` **from the coefficients of `f` alone**
whose Fitting minors cut out (a variety containing) `D_r`, and report its degree
in the coefficients of `f`.  **Degeneracy-direction pre-check (brief §4b.3 /
wording §5), RUN FIRST and committed here as the gate:** evaluate the rank
condition (the degree-`d` Macaulay rank-drop that `Ψ_f` refines) at (1) a `det_4`
pencil, (2) a reducible `ℓ·c`, `c` generic, (3) the full ten-variable
`ℓ·per_3`.  **Stop rule:** if the padded permanent (3) is at least as degenerate
(drop at least as large, at equal `r`) as the determinant (1), the statistic
separates in the wrong direction and §4b stops there with that reported.
**Positive for the deliverable:** the pre-check passes (det strictly more
degenerate than `ℓ·per_3`) AND a Fitting degree is reported, even if only as the
current honest bound (the full Macaulay-minor size `ρ_d − C(r,5) + 1`) together
with a precise statement of what a small `Ψ_f` needs (the closed-form map of
P4).  Closedness of `rank ≤ R` (so the condition passes to the border) is to be
stated and checked.  Prior: pre-check runs and is reported 0.95; separates the
right way 0.6; a genuinely *small* (below-degree-24) `Ψ_f` obtained 0.15.

## Falsifiers / negative outcomes worth reporting
- P1/P2 wrong dimension ⇒ the drop is **not** a syzygy phenomenon (brief §6).
- P5 `χ ≠ det` ⇒ the module is not `Λ⁵` and the whole `Λ⁵` reading is wrong.
- P6 ≠ 21 ⇒ wrong module.
- P7 pre-check failing (padded permanent at least as degenerate) ⇒ the rank
  condition separates the wrong way; report and stop, do not develop it.

## Fixed test data (committed before use, brief §4b.3 / wording §5)
Seeds for the degeneracy pre-check: `det_4` pencil seed 5107; reducible `ℓ·c`
seed 5108; `ℓ·per_3` (ten-variable) seed 5109; house primes `P1,P2`.  Random
control quartic seed 5100.  These strings are fixed now; the runs use exactly
them.
