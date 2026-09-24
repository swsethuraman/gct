# Integrator review — session 58, symmetric rectangular Kronecker at scale

**Accepted.  `sk((65,17,2⁷), 24⁴) = 48 825` and the boundary concern is
closed.**  The session answered the mid-session question in the terms it was
asked, and the answer is the good one: the value is computed *at* `δ = 24` by an
identity of symmetric functions, with no stability hypothesis anywhere.  This
review adds twelve independent boundary values, the full ambient ladder at the
LMR tail, and one observation the report did not draw (§4) that should go into
the s56 brief before it runs.

## 1. Reproduced independently

By the direct `p(4δ)` character sum — Murnaghan–Nakayama over every partition of
`N`, no reduction, no stability, sharing no code with the session:

| `λ` | `δ` | `N` | `g` | `A` | `sk` | session |
|---|---|---|---|---|---|---|
| `(8,2,2)` | 3 | 12 | 2 | 2 | 2 | ✓ |
| `(11,3,2)` | 4 | 16 | 2 | 2 | 2 | ✓ |
| `(10,2,2,2)` | 4 | 16 | 5 | 5 | 5 | ✓ |
| `(13,3,2,2)` | 5 | 20 | 6 | 6 | 6 | ✓ |
| `(16,4,2,2)` | 6 | 24 | 20 | 16 | 18 | ✓ |
| `(18,4,2⁴)` | 7 | 28 | 61 | 33 | 47 | ✓ |
| `(21,5,2³)` | 8 | 32 | 110 | 44 | 77 | ✓ |
| `(23,5,2⁴)` | 9 | 36 | 311 | 83 | 197 | ✓ |
| `(26,6,2⁴)` | 10 | 40 | 657 | 163 | 410 | ✓ |
| `(29,7,2⁴)` | 11 | 44 | 1073 | 207 | 640 | ✓ |
| `(32,8,2⁴)` | 12 | 48 | 1759 | 333 | 1046 | ✓ |
| `(31,7,2⁵)` | 12 | 48 | 2436 | 348 | 1392 | ✓ |
| **`(19,7,2⁵)`, `n = 3`** | 12 | 36 | 11 | 9 | **10** | ✓ |

**Twelve boundary-family cells and the `n = 3` LMR cell, zero disagreements**,
including the Adams part `A` at every one — the half of `sk` that no other route
available here confirms.  The first nine are the family the mid-session note
asked for, on which `2δ = |ρ| + ρ₁` holds with equality exactly as at the goal
cell; the three at `N = 44, 48` extend it past where that note reached.

On the goal family itself I reproduce the pre-stable values
`sk = 2714, 15383, 26654` (`g = 5241, 29326, 50660`) at `δ = 12, 13, 14`,
matching the report's table.  These are the values that make the claim checkable:
below the threshold the reduction returns numbers that are *not* the limit, and a
direct partition sum returns the same ones.

**`g = 92 000` at the goal cell** was confirmed separately by a third route —
Manivel's reduction to `dim S_ρ(sl₄)^{GL₄}` at `ρ = (17,2⁷)`, computed as a
plethysm on the adjoint, itself calibrated 5/5 against the boundary family
(`docs/lmr_cell.md` §3).  `A = 5 650` I cannot reach independently; it now rests
on this session's reduction and the external Manivel route, with the reduction's
`A` column validated on all thirteen cells above.

**The ambient ladder.**  `a((4δ−31, 17, 2⁷), δ)` for `δ = 12 … 32`, one DP pass:

    2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274, then 274 throughout

matching session 57's sequence exactly, and carried to `δ = 31` — the degree at
which the ladder theorem *guarantees* constancy — so `a_∞ = 274` is settled
rather than read off a flattening.  `a = 274` at `δ = 24` and `a = 273` at
`δ = 23`.  Also `a((19,7,2⁵), 12) = 6` at `n = 3` (inner degree 3), LMR's own
value.

## 2. The question, and why the answer is the good one

The mid-session note asked whether `48 825` is a direct computation at `δ = 24`
or an extrapolation from the stable range, and said the distinction was the whole
question.  The answer is direct, and the report's §0 is right about why: the
reduction is Jacobi–Trudi along **`λ`'s** first row followed by Frobenius
reciprocity on the rectangle, so the rectangle enters only through the box
condition `β₁ ≤ δ`, which is enforced at `δ = 24` and nowhere else.  Two things
make that checkable rather than asserted, and both check out here: the pre-stable
values differ from the limit and are reproduced by direct sums, and the boundary
family — the one place where the external route's hypothesis holds only with
equality — is reproduced at nineteen cells, twelve of them again here.

So the two routes are now genuinely independent in the way that matters: one
does not use stability at all, the other uses it exactly at equality, and the
first validates the second's use of it.  That is a better outcome than agreement
alone.

## 3. What the numbers say about the block

`Θ⁺_LMR : C²⁷⁴ → C⁴⁸ ⁸²⁵`, and `mult_det` is the rank.  Two facts worth putting
side by side, neither of which either report states:

- `sk` is **already constant from `δ = 23`** (report §5), and `a₂₃ = 273`,
  `a₂₄ = 274`.  So the predecessor cell `(61,17,2⁷)` at `δ = 23` is
  `C²⁷³ → C⁴⁸ ⁸²⁵` — *one column narrower, identical target*.  It is strictly
  cheaper than the goal cell and it is the sharper experiment: if its rank is
  273, then `mult_det,24 ≥ 273` by the ladder, so `i_det,24 ≤ 274 − 273 = 1`,
  and since the LMR module gives `i_det,24 ≥ 1`, **`i_det,24 = 1` exactly**.
  That deduction needs only the two `a` values and monotonicity — no stability,
  no `sk` — and both `a` values are now confirmed here.
- The Manivel reduction is **unavailable at `δ = 23`**: `2δ = 46 < 48 = |ρ| + ρ₁`,
  so the cell is strictly below the threshold.  Its target dimension comes from
  this session's reduction alone, which is exactly why the reduction's
  independence from stability matters.  (The reduction gives `48 825` there too.)

## 4. The free positive control the report did not name

Report §7 computes the LMR weight at `n = 3`: `λ = (19,7,2⁵)`, `δ = 12`,
`ℓ = 7`, `a = 6`, `sk = 10`.  Both numbers are confirmed above.  That is not
just a by-product — **it is a `6 × 10` positive control for the Foulkes engine**,
and it is essentially free.

The LMR module is non-vacuous at that cell (it is LMR's own weight at `n = 3`),
so `i_det ≥ 1` there and therefore

    rank Θ⁺_{n=3} at ((19,7,2⁵), 12)  must be  ≤ 5,  not 6.

Every other cell the programme has measured has `mult_det = a`, i.e. full rank;
an engine calibrated only on full-rank data has never been shown a rank drop.
This one is a six-column rank computation.  **It should be a mandatory
calibration in the s56 brief, ahead of the `δ = 3` blocks** — those are `C → C²`
maps of rank one, which test the plumbing; this one tests whether the engine can
see the phenomenon the whole programme is looking for.  If it returns rank 6,
the engine or the identification is wrong and we learn it for the price of a
`6 × 10` matrix rather than a `274 × 48 825` one.

## 5. Hygiene, scope, and two small things

Pre-registration `0dde185` precedes every computation.  No single-writer file
touched, no blob over the limit (the long-weight values are gzipped), no session
link in any of the four commits, `Co-Authored-By` on each.  The one run ended
early is recorded with its pid and its cause (an exponential vertical-strip
enumeration, rewritten polynomially and re-run with the value unchanged).  No
certificate was produced, correctly: no `gct-cert/1` kind can carry a
character-sum value, and the session says so rather than inventing one.  Its
suggestion of a `kronecker` kind recording `(j, τ)`, the box, and the inner sums
is a good one and should be taken up when a second session needs to check these
numbers.

Two observations of the session's own (§9) are right and should be actioned:
`results/occurrence_screen.md`'s statement that `δ = 11, 12` exceed budget is now
false, and `results/longweight_screen.md` does not record the s39 engine's
`N ≤ 64` and bead-width limits.  Both are single-writer files; I will fold them
into the next housekeeping pass rather than here.

The `n = 5` LMR value (`sk = 1 435 445 282` at `N = 200`, `p(N) ≈ 4 × 10¹²`) is
beyond any check available to me and is recorded as the session states it: a
computation no previous route could attempt, unverified by a second route.

## 6. Verdict

Accepted and merged.  The scorecard is honest, the dropped deliverable 3 is
correctly attributed to the integrator's mid-session instruction, and the
replacement rule of §6 — cost driven by `|λ̄|`, with `N` and `δ` out of it — is
more useful than the table it replaced.  Carried forward:

1. `docs/lmr_cell.md` is updated with `sk = 48 825` confirmed by a
   stability-free route and with the `δ = 23` predecessor as the sharper test.
2. The `n = 3` LMR cell `((19,7,2⁵), 12)`, `6 → 10`, goes into the s56 brief as
   a mandatory calibration with the pre-registered expectation `rank ≤ 5`.
3. The two single-writer corrections of §9 go into the next housekeeping pass.
