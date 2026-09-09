# Batch-12 S4 — integrator review

## 1. What it delivered, in one page

**The headline is a floor where there was none.** `rank T_pad ≥ 12` at the goal
cell, certified over `Q` by two 12-minors on **true padded** points (`ℓ · per₃`,
not `ℓ · c`), at both house primes, on two independently written evaluators.
Before this the padded side had no lower bound at all.  With S1's transported
determinant bound the programme now stands at

    2 ≤ rank T_det ≤ 273,      12 ≤ rank T_pad ≤ 274,      −261 ≤ D ≤ 272.

Broad, and for the first time bounded on both sides.

**Six other things, in order of what they change:**

1. **The padded factorization, proved, with its normalization pinned.**
   `M_λ →^S ⊕_μ M^{(3)}_μ →^Q ⊕_μ N_μ`, `rank(Q∘S) = rank T_pad`, and the exact
   obstruction identity `rank T_pad = rank S − dim(S(M_λ) ∩ K)`.  Full padded
   rank needs **both** `ker S = 0` **and** that intersection zero.  The coefficient
   formula `μ*(c_α) = Σ_i y_i d_{α−e_i}` has no `α_i` factor; the house-symbol
   version does; the tensor split carries `4^24`.
2. **The fixed-factor kernel lemma.**  On highest-weight sources,
   `ker R_1 = ker S`, where `R_1` sets `c_α = 0` for `α_1 = 0` and reads the rest
   as cubic coordinates.  Fixing the linear factor to `x_1` is an **exact** kernel
   test — no reducible pullback to expand.  The proof is the shear argument on a
   dense open set and it is correct.
3. **`dim P_6 = 55 < 61 = dim R_6`.**  Jacobian minors plus torus upper bounds.
   The first hard evidence in the programme that the padded and reducible
   families differ *at the parameter level*, rather than only in principle.
4. **A correction on s64.**  Its 48-row ledger has **zero** rows with
   `mult_pad ≠ mult_red` and twelve with `mult_pad ≠ mult_det`.  There is no
   banked padded-versus-reducible discriminating cell to lean on.
5. **Exact calibration identities.**  The `(8,8,8), δ=6, r=3` control with source
   2, determinant 2, reducible/padded 1 and explicit kernel `(1,0)`; an archived
   `r=5` kernel lifted to an exact 19,834-term integer highest-weight polynomial
   vanishing identically on reducibles — checked over `Z`, not inferred from two
   modular zeros.
6. **The 48-block ledger and the residual structure.**  `M_λ = V₀ ⊕ L`,
   `dim L = 262`, with `T_pad(V₀) ∩ T_pad(L) = 0` — a *justified* independent-image
   decomposition, so `rank T_pad = 12 + rank(T_pad|_L)` — plus an explicit
   finishing matrix `H`.  Every one of the 48 block ranks is OPEN.

**What it did not do**, and says so cleanly: no full source, no assembled split
matrix, no `Q_μ`/`K_μ`, no new determinant bound, and the requested small residual
is 262 rather than one.  It met its bounded-fallback branch, not its prize.

---

## 2. Verified here, independently

**The headline certificate reproduces.**  S4's Windows host could not load this
repository's Linux evaluators, so its minors came entirely from its own code.
I re-derived them from **S4's own 36 points and 34 fillings** through the s69
Grassmann DP evaluator (`analysis/wk12_int_s4_verify.py`):

    conventions: S4's exponent list is wk8_s30_core.exps(4,9) entry for entry,
                 and u = c_(4,0,...,0) sits at index 494 with S4's recorded value
    entries    : 144 per prime, checked by BOTH normalizations S4 specifies —
                 native x u(f_j)^(24-d_i)  and  literal x 24^-(24-d_i)
                 → 576 agreements, no exceptions
    determinants: 1086325324 and 2097075880, reproduced by modular elimination
                 and by exact integer Bareiss, both ours

The two-route entry check is the one that matters: S4 itself flags transport
normalization as where a silent error would live, and both routes agree
everywhere.  **`rank T_pad ≥ 12` is verified, not merely reported.**

**The structural census reproduces.**  `I = {μ : |μ| = 72, λ_i ≥ μ_i ≥ λ_{i+1}}`
enumerated independently gives exactly S4's 48 shapes, identical as a set to its
closed form (`(58−b, b, 2⁷)`, `(59−b, b, 2⁶, 1)`, `(60−b, b, 2⁶)` for `b = 2..17`);
the inherited `a₃` values sum to 521; and the 48 row intervals are consistent
with them and end exactly at 521.

---

## 3. The correction lands on me, and it is a real one

S4 writes: *"A further correction to the original integrator note is necessary…
The entire deficit from 521 is not the sum of cubic permanent kernels."*

That is `docs/s64_integrator_note1.md`, which said

> "the deficit `h_pad − mult_pad` is exactly the cubic-permanent kernels"

and it is **false**.  The identity is

    h_pad − rank T_pad  =  (h_pad − rank S)  +  dim(S(M_λ) ∩ K)

and `rank S ≤ dim M_λ = 274`, so at LMR the deficit from 521 is **at least 247 for
dimensional reasons alone**, before a single kernel is considered.  Only the
second term is kernel.  My sentence would have licensed reading `mult_pad` off
the 48 block kernels, which is exactly the mistake S4 also warns against in its
"do not sum individual block ranks" note.

Corrected in place.  What survives untouched is the architecture — the
factorization I recommended is now *proved*, with normalization pinned, which is
the better half of the outcome.  What does not survive is the accounting.

This is the third error of mine a session has caught this batch (the `FAMILIES`
seed-offset insertion, the `k < 5` misreading, now this).  All three were
statements I made *about* other people's results rather than results I computed.
That is a pattern worth naming rather than a run of bad luck.

---

## 4. Where S4 pushes back on my framing, and how much of it lands

> "the 273-dimensional old source span at degree 23 has not been certified
> padded-full.  The last-born direction cannot be the sole padded question here.
> Even after an old padded rank-273 certificate exists, a new vector must escape
> the **old padded image span**, not merely evaluate nonzero."

**Against integrator note 1, this lands.**  I wrote there that the residual
difficulty "sits on one identifiable vector."  It does not, and did not.

**Against note 3, we agree and S4's phrasing is the better one.**  Note 3 has
`i_pad(24) = i_pad(23) + ε_pad` with *two* unknowns, and says explicitly that a
nonzero padded evaluation of `F_{T₅₇}` does not give `ε_pad = 0` — what is needed
is that `T_pad(F_{T₅₇})` lies outside `T_pad(uM₂₃)`.  "Escape the old padded
image span" is the same statement said better, and I adopt the wording.

S4's `dim L = 262` is the concrete form of it: the certified complementary source
space is 262-dimensional, not one.  Note that this `L` and the birth line are
different objects — `L = ker e₀` is defined by twelve *evaluation* conditions,
the birth quotient by the *ladder*.  Neither supersedes the other and the report
is right not to conflate them.

---

## 5. What this changes for the running sessions

S4's handoff is addressed to "s74, s75, s76" in the reconciled proposal's
numbering.  In ours that is **s74, s75 + s76, and s77**.

- **s74** gains a free head start it does not know about: twelve certified padded
  rows, the exact source order and `u`-normalization in
  `source_coordinate_transforms.json`, and 36 true-padded integer points — with
  both transport routes now verified here.  It should use the first twelve
  certified columns as an evaluation pivot block and evaluate residuals against
  it, rather than starting the padded column from nothing.  It must **not** add
  the 113-vector checkpoint's rank to this one, and must not reclassify the other
  22 saved rows as certified.
- **s75 / s76** get a warning worth having: S4 reports that **S3 has run** and
  supplies a compact operator plus a certified 31→2 *dimension* control, but
  explicitly leaves control-basis **evaluation** unresolved.  That is precisely
  my s75's two-part control, and its second part is the part still open.  s75
  should not treat the 31→2 kernel as evaluated.
- **s77, s78, s79**: nothing.

I have not seen S3's report.  It is referenced throughout S4 and it bears
directly on two running sessions, so it is the next thing I want.

---

## 6. Ledger

| claim | status |
|---|---|
| `rank T_pad ≥ 12` at the goal cell, true padded points | **CERTIFIED**, and independently re-derived here |
| padded factorization, normalization, `rank T_pad = rank S − dim(S(M_λ) ∩ K)` | PROVED (S4) |
| fixed-factor kernel lemma `ker R_1 = ker S` | PROVED (S4) |
| `dim P_6 = 55 < 61 = dim R_6` | CERTIFIED (S4) |
| 48-block census, `a₃` sum 521, row intervals | **re-enumerated here, agree exactly** |
| s64 has zero `mult_pad ≠ mult_red` rows | CORRECTION, accepted |
| "the deficit from 521 is the cubic-permanent kernels" | **FALSE — mine, withdrawn** |
| the residual is one vector / the last-born line | **FALSE — mine, withdrawn**; the certified residual is 262 |
| every `S_μ`, `Q_μ`, `K_μ` block rank | OPEN |
| `rank T_det = 273`, `rank T_pad = 274`, the sign of `D` | OPEN |
