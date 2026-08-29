# What group does the evaluation actually respect? (session 17, math only)

Prompted by the session-16 retraction: both dead theories assumed too large a
symmetry. This session derives the symmetry that h₁ **does** have, verifies
the conventions from scratch, tests the result against all 11 banked engine
points, and banks one decisive prediction. No engine runs were made.

## 1. Conventions, verified (they were right, with one refinement)

λ′ = (8,8,8,6⁶) has two distinct parts (3 and 6 of them), so the stabilizer
of the highest-weight LINE is the standard parabolic **Q with Levi
GL₃ × GL₆** — confirmed. The 3-space is span{x₀,x₁,x₂}, the first row, and
this agrees with the counting lemma, which forces 24 = 3·8 first-row legs.
Weight structure and combinatorics single out the same 3-space.

REFINEMENT (needed, and it matters): Q is the parabolic in which the
**weight-8 block RECEIVES from the weight-6 block**, not the reverse. Verified
two independent ways:
 - Binary-form check: for f = a x₀² + b x₀x₁ + c x₁², the HWV h = a is fixed
   by x₀ ↦ x₀ + t x₁ and NOT by x₁ ↦ x₁ + t x₀ (it becomes a + bt + ct²).
 - Consistency: balanced directions u_N (the 6-block receiving from the
   3-block) are therefore TRANSVERSE to Q, which is exactly why V ≠ 0 there —
   the same fact the counting lemma expresses. Under the opposite orientation
   u_N ∈ Q for every N, forcing V ≡ 0: refuted instantly by the data.

χ on the Levi is det(·|3-block)^8 · det(·|6-block)^6.

## 2. The theorem

For q ∈ Q, s ∈ H: h(q f) = χ(q)^{±1} h(f) and s·det₃ = det₃, so if
u_{N′} = q u_N s then V(N′) = χ(q)^{±1} V(N). Hence **the evaluation is
constant on the double cosets Q·u·H up to χ**. Since Q = Stab(W) with
W = span{x₃..x₈}, Q\GL₉ ≅ Gr(6,9) via g ↦ g⁻¹W, so:

> **The double coset of u_N is exactly the H-orbit of the 6-dimensional
> subspace Γ_N := u_N⁻¹(W) ⊂ M₃ — the graph of −φ, where φ is the direction
> viewed as a map from the first-row 3-space. Dually: the H-orbit of the
> 3-dimensional annihilator NET Γ_N^⊥ ⊂ M₃ under X ↦ aXb (plus transpose).**

So the true invariant of a direction is a **net of 3×3 matrices**, whose
classical invariant is its determinantal plane cubic det(sM₁+uM₂+wM₃) —
the object this whole programme already lives on.

**Sign/exponent convention pinned by homogeneity** (a self-calibrating test):
V is degree 4 in N, so V(2N) = 16 V(N). Computing χ for the pair (N, 2N)
gives exactly 16 in the det(quotient)^8·det(W)^6 convention. Therefore

    V(N′) = χ(q) · V(N),     χ(q) = det(q|_{C⁹/W})^8 · det(q|_W)^6 .

## 3. THE OBJECT IS THE TOTAL, NOT THE SUBPROBLEM (correction made in-session)

h(f) is the FULL scheme evaluation. The banked per-σ values (+108,712,800
etc.) are pieces of the σ-decomposition, which is internal bookkeeping and is
NOT preserved by Q or H. An early version of this analysis tested the theorem
against per-σ values and produced an apparent contradiction; the theorem
constrains **totals** only. All results below are stated for totals.

## 4. Scorecard against the bank

Net data (vertex ranks are H-orbit invariants):

| point | det-cubic | vertex ranks | generic rank | value |
|-------|-----------|--------------|--------------|-------|
| C     | −suw (triangle)      | [1,2,2] | 3 | TOTAL 1,152,144,000 |
| Q_pt  | −suw                 | [1,2,2] | 3 | = C (H-conjugate) |
| R     | suw                  | [1,1,1] | 3 | TOTAL 1,152,144,000 |
| T4    | suw                  | [1,1,1] | 3 | table = C's |
| X4    | s(u−w)(u+w)          | [1,1,1] | 3 | σ-values ≠ |
| Xm3   | u(s²−sw+w²)          | —       | 3 | σ-values ≠ |
| P, Y2, Y3, Y4 | ≡ 0          | —       | **2**, common left kernel | **0** |
| D     | −uw²                 | —       | 3 | 0 (weight-infeasible) |

CONFIRMED RETRODICTIONS:
 - **R and T4 are in the same double coset with χ = 1** (explicit connecting
   element computed), so the theorem predicts equal totals — and the banked
   data has exactly that. This is the first structural explanation of any part
   of the universality.
 - Q_pt = C: H-conjugate, χ = 1, equal totals ✓.
 - Homogeneity V(tN) = t⁴V(N) ✓ (used as the calibration).

HONEST NEGATIVE — universality is still NOT explained:
 - **C and R are in DIFFERENT double cosets**, proven by an orbit invariant
   (vertex ranks [1,2,2] vs [1,1,1]; transpose preserves ranks, so the
   transpose coset of H does not rescue it). Their totals are nevertheless
   equal. So the symmetry does not force TOTAL_C = TOTAL_R: the equality of
   the two certificate points remains an unexplained coincidence, exactly as
   after session 16. The group is smaller than the phenomenon.

## 5. Independent empirical criterion (not derived from the symmetry)

**Compression ⟹ 0.** Every banked zero that is not weight-infeasible has a
net of generic rank ≤ 2 with a common left kernel, and every nonzero point
has generic rank 3 — 4/4 (P, Y2, Y3, Y4), plus the base point N = 0 (whose
net is the rank-≤1 row-0 net, value 0 by the counting lemma). This UNIFIES
three previously separate vanishing mechanisms recorded as open leads after
session 16: rank-1 pencils (P), A or B ∝ I (Y2, Y3), and complementary
projections with AB = 0, A+B = I (Y4). It is not implied by the double-coset
theorem (the compression points are not in the zero coset — different generic
rank), so it stands as its own conjecture with 5/5 support.

## 6. PRE-REGISTERED PREDICTION (banked, not run)

R and X4 ARE in the same double coset; the explicit connecting element has
det(a)det(b) = −4 and gives **χ = 4**. Therefore

    **TOTAL_X4 = 4 × 1,152,144,000 = 4,608,576,000**

Consistency check (not circular — uses the two X4 values already banked):
with X4's orbit design (point symmetry π = (1 2)(4 5)(7 8), sign −1,
ρ = (0 2); 8 orbits of sizes 4,4,8,4,8,4,2,2; reps 00,01,02,03,04,05,14,16),
    TOTAL_X4 = 4V₀₀+4V₀₁+8V₀₂+4V₀₃+8V₀₄+4V₀₅+2V₁₄+2V₁₆.
The known V₀₀ = −308,145,600 and V₀₅ = −661,046,400 contribute −3,876,768,000,
so the prediction requires the six unmeasured values to sum (weighted) to
+8,485,344,000. Both known σ-values are NEGATIVE while the predicted total is
POSITIVE — a strong and risky prediction, not already implied by what we have.

NOTABLE CONVERGENCE: the retracted Ψ = 2v−D theory predicted the same total
(Ψ(X4) = 4). The two theories disagree per-σ — which is what killed Ψ — but
agree on the total. So this test discriminates "both wrong" from "both right
about totals", and a hit would partially rehabilitate the Ψ arithmetic at the
level where it was never tested.

COST: 6 further subproblem runs (01, 02, 03, 04, 14, 16) at ~1.5–2.5 h each —
about one overnight on two workers. Per this session's instruction (run only
if a single subproblem settles it in < 2 h), it is **banked, not run**.

## 7. What died, and against what

- "V is a det²-covariant of the pencil" — died at X4 (session 16).
- "V is a simultaneous-conjugation invariant" — died at Y4 (session 16).
- "The double coset explains universality" — dies here, at the pair (C, R):
  same value, provably different cosets.
- "The determinantal cubic's projective type is the invariant" — too coarse:
  C, R, T4 and X4 all give triangles, but X4's σ-values differ. The finer
  net-orbit (vertex ranks) is the correct invariant.
