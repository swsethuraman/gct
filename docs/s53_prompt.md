# Session 53 — Border degenerations of `det_4`: the finite first layer

A different category of argument from the rest of the batch.  This session does
not compute a multiplicity and does not use the `GCT` statistic.  It addresses
`ℓ·per_3 ∉ D_10` directly, through the base locus of a border degeneration.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No `claude.ai/...` URL in
  any file you write.
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.  Do not
  select processes by name pattern.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config is
  append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result before running it.  Bank the result per cell.
- `python-flint` only for exact linear algebra.
- Any cell reporting `D > 0` goes through the verification protocol before it is
  written down as a claim.
- Before developing any statistic meant to characterise determinant type, run
  the degeneracy-direction pre-check in `docs/brief_wording.md` §6.

## 1. Setup

A border degeneration of a `det_4` pencil in `r` variables is

    M(t,s) = M_0(s) + t M_1(s) + t^2 M_2(s) + ...

with `det M_0(s) ≡ 0`.  Then `E = M_0(V) ⊆ M_4(C)` is a linear space of `4×4`
matrices of rank at most three, of dimension at most `r`.

For `r = 10` — the length at which `ℓ·per_3` lives — the classification of such
spaces is **complete**, and it is much more restrictive than a dimension bound.

## 2. What is actually known, and what to use

Do **not** argue from Atkinson–Lloyd's threshold.  That result says dimension
*above* `nr − r + 1 = 12 − 3 + 1 = 10` forces compression structure, so at
`dim E = 10` it does not apply.  As an argument for the case at hand it has a
gap.

Use the classification instead.  Atkinson (1983) classified primitive spaces of
bounded rank `3`, and Huang–Landsberg (*On linear spaces of matrices of bounded
rank*, Selecta Math.) confirm it: **there are no non-classical examples of spaces
of bounded rank when `r ≤ 3`**, and the only primitive family is

    E = C^a ⊂ Hom(E, Λ^2 E),   e ↦ (v ↦ e ∧ v),

of bounded rank `a − 1`, together with its projections.  For bounded rank `3`
that is `a = 4`: a **four-dimensional** space, nowhere near ten.

Hence every ten-dimensional space of singular `4×4` matrices is a subspace of a
compression space.  The compression types for rank `≤ 3` in `M_4`, indexed by a
subspace `K` of dimension `k` mapped into a subspace `I` of dimension `i` with
`(4 − k) + i = 3`, are:

| `(k,i)` | `dim` |
|---|---|
| `(1,0)` — common kernel vector | 12 |
| `(2,1)` | 10 |
| `(3,2)` | 10 |
| `(4,3)` — common image hyperplane | 12 |

So the case list at `dim E = 10` is: the two ten-dimensional compression spaces,
plus ten-dimensional subspaces of the two twelve-dimensional ones.  Small and
finite.

**Task 1 is to verify all of the above against the sources** before using it.
This is an imported classification and it is load-bearing.  Confirm in
particular that the primitive family cannot reach dimension ten at bounded rank
three, and that no combination of primitive and compression pieces does either.

## 3. Task 0, before any case analysis: what happens at order `≥ 2`

The case list is finite **at leading order only**.  If
`det(M_0 + t M_1 + ...)` vanishes to order `k` in `t`, the leading quartic is not
the first polar, and the analysis of order-`k` terms is where border problems
characteristically die.

Before touching the cases, write down:

- the order-`k` leading term of `det(M_0 + t M_1 + ...)` in general;
- how many additional cases that generates for `k = 2, 3, ...`;
- whether there is any bound on `k`, and if not, what would give one.

If there is no plan for order `≥ 2`, **stop there and say so.**  Do not complete
layer one and present it as near-completion.  Reporting "layer one is finite and
here it is; layer two has no plan and here is why" is the honest and useful
outcome, and it is an acceptable result for this session.

## 4. Task 2 — the normal forms and their first polars

Write out each compression normal form explicitly.  For the common-left-kernel
case, coordinates can be chosen so the last row of `M_0` vanishes, and the first
determinant polar in a transverse direction is

    Σ_{j=1}^{4} m^{(1)}_{4j}(s) · C_{4j}(M_0(s)),

a linear form against cubic cofactors, summed over four terms.  Do the analogous
expansion for the `(2,1)` and `(3,2)` cases.

## 5. Task 3 — the cheap screen, run first

`ℓ·per_3` is **reducible**: a linear form times a cubic.  So before any
`GL_10`-equivalence test, screen each leading-quartic normal form by:

1. Does it factor at all?  Most will not; those cases close immediately.
2. If it factors, does it factor as (linear)·(cubic)?
3. Only for survivors: is the cubic factor `GL_9`-equivalent to `per_3`?

Reducibility is a closed, cheap, and very restrictive condition, and it should do
most of the pruning.  Use it before any Hessian or singular-locus invariant.

For step 3, cheap decisive invariants first: dimension and degree of the singular
locus, Hessian rank profile, and the number of singular points if finite.
`per_3` has a well-understood singular locus; use it as the discriminating
statistic rather than attempting a normal-form match.

## 6. What this session is and is not

**Is:** a direct approach to `ℓ·per_3 ∉ D_10`, which is the entire open problem
at `(3,4)`.

**Is not:** a contribution to the multiplicity statistic.  Nothing here produces
an equation in `Sym^δ Sym^4 C^r`, and this session does not feed s49–s52.

Note why the question is genuinely open despite `dc(per_3) = 7`: Alper–Bogart–
Velasco's bound is for **exact** determinantal representations, and their
Remark 1.9 shows `dc` is *not* upper semicontinuous — `xy^2 + yt^2 + z^3` has
`dc > 3` and degenerates to `z^3` with `dc = 3`.  So nothing about `dc(per_3)`
survives to the border by general principle.

Related and already recorded, as background rather than a task: any exact `8×8`
Pfaffian representation of `ℓ·per_3` with a common isotropic 4-plane would give
`ℓ·per_3 = det B` for `B` a `4×4` matrix of linear forms, hence on `ℓ = 1` an
affine `4×4` determinantal representation of `per_3`, contradicting
`dc(per_3) = 7`.  The separating content there is entirely Alper–Bogart–Velasco's;
the Pfaffian language localises which structure fails.  Do not restate it as a
new separation.

## 7. Success and failure

**Success:** Task 0 answered honestly, the classification verified, the normal
forms written out, and the reducibility screen run on each.

**Best outcome:** every ten-dimensional case closed, with a clear statement of
what remains at order `≥ 2` and at base-space dimensions `9, 8, ...`.

**Failure mode to avoid:** presenting a finite first layer as a near-proof.

## 8. Report

`docs/s53_report.md`.  Deliver as a bundle.
