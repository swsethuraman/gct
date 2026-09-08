# Session 75 — the `δ = 12` compact control

*(the reconciled proposal's s75, first half.  Read the preamble first.)*

## First 30 minutes

    git rev-parse main
    ls docs/batch12_s1_s2_consolidated.md    # if absent, STOP: you have an old tree
    python3 tools/verify/selftest.py         # expect 12 cases, PASSED

    python3 analysis/wk11_int_bdelta.py      # the predecessors and B_delta
    python3 -c "import json;d=json.load(open('results/wk11_int_c12.json'));\
print('C_12 =',d['C'],'over',d['two_strip_paths'],'paths,',d['distinct_shapes'],'shapes')"

Expect `B₁₂ = 31` and `C₁₂ = 239` over 36 paths and 23 shapes.  `C₁₂` is your
control; read `analysis/wk11_int_cdelta.py` (it is short) to see how it is
computed, because you will need the same object at `δ = 12` from the operator
side.

## The question

Does S5's one-block recursion produce an invariant source that can be
**evaluated**, at the smallest cell where the answer is known?

`λ₁₂ = (17, 17, 2^7)`, `B₁₂ = 31`, `a₁₂ = 2`.  Two parts, and the second is the
one that decides the route:

1. recover `dim M₁₂ = 2` from the 31-dimensional precursor;
2. **evaluate the two recovered vectors against determinant points**, reproducing
   s69's banked `i_det(12) = 0`.

Dimension alone is not success.  A recursion that returns the right count and
vectors that cannot be paired with determinant points is a dimension count, not a
source, and that is a full result — say so plainly if it happens.

## The operator, stated correctly

The invariant source is `W_δ ∩ Fix(τ)` with `W_δ = (S^{λ_δ})^{K_δ}`,
`K_δ = H_{δ−1} × S₄`.  **The raw adjacent block transposition `τ` does not
preserve `W_δ`** — `τv` is invariant under `τK_δτ^{-1}`.  Do not write
`ker(τ − I | W_δ)` as though the endomorphism existed.  Construct the projected
or spherical operator (`P_K τ P_K`, or the double-coset/Hecke form, or explicit
LR/Pieri recoupling) and say which.

## Pre-registered: the operator passes through a 239-dimensional space

The residual `τv − v` lives in the invariants of
`K' = K_δ ∩ τK_δτ^{-1} = H_{δ−2} × S₄ × S₄`, of dimension

    C_δ = Σ over two-step horizontal-4-strip paths λ → μ → ν of a_{δ−2}(ν)
        = Σ_{μ a one-strip predecessor of λ_δ} B_{δ−1}(μ)

— one more level of the same recursion.  Computed exactly:

    C₁₂ = 239        (against B₁₂ = 31, a₁₂ = 2)
    36 two-strip paths over 23 shapes, 21 nonzero, largest channel 18

`results/wk11_int_c12.json`, engine `analysis/wk11_int_cdelta.py`.

**This is your control, and it is sharper than `dim M₁₂ = 2`.**  Two is a small
number and several wrong operators return it.  A correct `P_K τ P_K` at `δ = 12`
maps a 31-dimensional space through a 239-dimensional one.  An implementation
that never forms a 239-dimensional object is either doing something cleverer than
we know or is wrong, and must say which.

## Constraints

- **No prime below 97**, at any `δ`, however tempting for speed here where
  `|λ₁₂| = 48`.  The preamble says why.
- `B₂₄ = 2168` and `B₁₂ = 31` are *dimensions*.  S1 is explicit that they are not
  supplied intertwiners or evaluable basis vectors.  Producing the embeddings and
  the evaluation map is your job, not an inherited input.
- The interface you must supply for s76: ordered predecessor vectors, normalized
  Pieri embeddings, their compact coordinates, and an evaluator for each embedded
  vector.

## Tasks

1. Pre-register.  Build the three horizontal-4-strip predecessor multiplicity
   spaces of `λ₁₂` and confirm `B₁₂ = 31` independently.
2. Construct the projected block-swap operator; record its exact matrix elements
   in predecessor coordinates and the dimension of the space it passes through.
3. Recover `dim M₁₂ = 2`.
4. Convert or evaluate the two vectors at generic quartics and at `det₄` pencils;
   reproduce `mult_det = 2`, `i_det(12) = 0`.
5. Record the complexity of each step as a function of `B_δ` and `C_δ`, so s76
   can price the same steps at `δ = 24`.

## Success

Both halves pass — source dimension **and** evaluation semantics — without
expansion into the native carrier.

## Stopping rules

- Exact recoupling or evaluation intrinsically requires ambient Specht/HWV
  carrier expansion: identify the exact obstruction, name the step, stop.
- The operator returns `dim = 2` but the vectors do not evaluate: that is the
  route's real risk and a complete deliverable.  Do not work around it.

## Deliverables

`results/PREREG_s75.md`; the operator's matrix elements and the measured
dimension of its intermediate space against the pre-registered 239; the two
vectors and their determinant evaluations; the s76 interface; `docs/s75_report.md`.
