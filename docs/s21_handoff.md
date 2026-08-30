**PRIORITY CHANGE — read before continuing with degree 24.**

The theory session (S22) has closed step (iii) of the totals-law proof and is
claiming Theorem 5.5. Before that goes into the paper it needs one engine value,
and that value is now ahead of degree 24 in your queue. Degree 24 gates a
corollary; this gates a theorem.

## Job 1 — TOTAL at X₋₃ (do this first)

**Pre-registered, by S22, before you run anything:**

```
TOTAL(X_-3) = -3,456,432,000 = -3 x 1,152,144,000 = 151,200 x (-22,860)
```

because Ψ(X₋₃) = −3 and the totals law asserts TOTAL(N) = Ψ(N) × 1,152,144,000.

The inputs are already in the repository: `inputs/evalin/f1Xm3_00.txt` through
`f1Xm3_35.txt`. One value is already banked from session 16:

```
f1Xm3_00 = +893,138,400 = 151,200 x 5907
```

Assemble the orbit exactly as the X₄ total was assembled in
`results/results_T4.md` — orbit representatives with weights summing to 36 —
and report the total.

**Why this value and not another.** Every total ever measured sits at
Ψ ∈ {0, 1, 4}, all non-negative. The S22 proof is a parity argument: it turns on
det(transpose) = (−1)³ = −1 on M₃, on 6 being even so that det(q)⁶ drops, and on
the transpose coset therefore not contributing. **Ψ = −3 is the first value that
can detect a sign error in that argument.** It is also demanding in the same way
X₄ was: the one measured value is positive (+5907 in cofactor units) while the
predicted total is negative (−22,860), so the unmeasured values must overturn
it, exactly as at X₄ six unmeasured values had to contribute +8,485,344,000.

**Why the caution is not generic.** Read the session 15 and session 16 records
in `PROJECT_NOTES.md` side by side. Session 15 proved the rank-1 theorem by
interpolation, closed every measured class, and pre-registered four completing
runs; all four hit. Session 16 then ran one off-locus point, got
f1X4_00 = −308,145,600 against a pre-registered +434,851,200, and the theorem was
retracted. S22's situation is structurally identical: proved on the cases in
hand, with a pre-registered off-locus value not yet run.

**If the value does not match.** Do not adjust anything to fit. Report the
mismatch, log it as a refutation in the session-16 style, and say which of the
proof's inputs it falsifies. A refutation logged honestly is a result here, and
two of them are already in the paper. If it does match, say so plainly — it is
then the first confirmation of the law at a negative gauge value and the first
independent test of the χ ↔ det² identification.

## Job 2 — degree 24, as previously briefed

Unchanged. See `docs/next_session_degree24.md`.

## Job 3 — is our Φ₁₈ primitive? (fold into job 2)

While you are in this part of the invariant ring, settle a normalisation
question the paper currently flags as open.

`Φ₁₈` is defined only up to scale. The canonical integral choice is the
**primitive generator** of the rank-one lattice of integral invariants in degree
18 — unique up to sign, the same convention under which `Ψ = −I₆^prim` with
coefficient 1. Our reported value

```
Φ₁₈(det₃) = −877,879,296,000 = −2^16 · 3^7 · 5^3 · 7^2
```

is in the engine's normalisation `N` (unit weight on the standard slab basis).
**Nobody has checked whether `N` is primitive.**

What is known: the content divides the gcd of the two computed values,

```
gcd(877,879,296,000, 50,536,120,320) = 2^16 · 3^4 · 5 · 7 = 185,794,560
```

which is a weak bound and does not rule out `N` being a substantial multiple of
the primitive generator.

Two routes: compute the content of the explicit degree-18 invariant directly
(gcd of its coefficients), or tighten the bound by evaluating at further integer
points until the gcd stabilises. The second is cheap and uses machinery you
already have.

**If `N` is not primitive**, the headline factorisation in Theorem 4.6 must be
divided by the multiple and restated, and Remark 4.7 (which currently records
this as unresolved) becomes a statement instead of a caveat. This is the part of
the paper a reader is most likely to quote, so it should be right.

## Standing

Branch discipline unchanged: work on `s21-degree24`, push only that branch,
never `main`. Pre-register before every value. Exact arithmetic, regression suite
before any reported number, two independent routes.
