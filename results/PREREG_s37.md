# Pre-registration — session 37 (theory: washout, transfer, DIP, blindness slab)

Committed before any computation and before the DIP / Bürgisser–Ikenmeyer /
Dimca–Cynk–Rams reading passes.  Branch `s37-dip`; clone tip `5367c75`
(integrator's s35 review); ancestry gate `git merge-base --is-ancestor
c02cee8 HEAD` passed; `docs/s35_review.md` present.  No `s36`/`s37` files or
commits found on `main` — no collision.

Convention (unchanged): `D(lam, delta) = mult_pad − mult_det = det_units −
pad_units`; an obstruction is `D > 0`; `D < 0` is the expected direction.

Labels used throughout the session's documents: **proved** (a proof is
written in the document), **measured** (exact arithmetic in this container,
script named), **adopted-from-literature** (statement quoted, reference given,
verified only to the statement quoted), **expectation** (neither).

## Deliverable 1 — `docs/washout_lemma.md`

**Expected to prove.**
- (W1) For `r <= 5` the restriction map `M_3^r -> Sym^3 C^r`,
  `A |-> per_3(sum s_i A_i)`, is dominant.  Certificate: full Jacobian rank
  `C(r+2,3)` = `4, 10, 20, 35` at one fresh exact point for `r = 2..5`, two
  primes.  Full rank at one point proves dominance (lower semicontinuity of
  rank + generic-rank = dimension of image in characteristic 0).
- (W2) Hence `D_r^pad = R_r := {l·c : l in V_r^*, c in Sym^3 V_r}` for
  `r <= 5`, and `mult_pad(lam, delta)` for `ell(lam) <= 5` is a function of
  `R_{ell(lam)}` alone: replacing `per_3` by any cubic with dense `r <= 5`
  restrictions leaves every `D(lam, delta)`, `ell(lam) <= 5`, unchanged.
- (W3) At `r = 6`, `dim D_6^{per_3} = 50 < 56`: lower bound Jacobian rank 50
  at a fresh point; upper bound `9·6 − 4 = 50` from the finite-stabiliser
  page.  The page: for a generic `r`-tuple, the stabiliser in the effective
  symmetry group of the form is finite — for `per_3` at every `r >= 1`
  (torus part killed by one entrywise-nonzero matrix), for `det_4` at
  `r >= 3` (commutant of two generic matrices is scalar); at `r = 2` the
  `det_4` commutant is the 4-dimensional diagonal algebra and the bound
  degrades to `32 − 27 = 5 = dim Sym^4 C^2`, consistent.
- (W4) With (W3) the s26/s30/s33 dimension tables and the `n = 4` codimension
  table are unconditional.

**What would show it false.**  A Jacobian rank below `35` at `r = 5` at a
fresh point over both primes (would mean the s26 rank-35 point was
exceptional — impossible by semicontinuity, so it would indicate a bug in one
of the two implementations, to be resolved before anything else); a
`det_4`/`per_3` stabiliser argument that needs a hypothesis not satisfied by
a generic tuple; a rank at `r = 6` above 50 (would refute the effective-group
dimension count and the identification `dim Stab(per_3) = 4`).

## Deliverable 2 — `docs/transfer_lemma.md`

**Expected to prove.**  `P_r ⊆ R_r` for all `r`, hence `I(R_r) ⊆ I(P_r)`
and `mult_{P_r} <= mult_{R_r}` in every `(lam, delta)`; so
`D_R := mult_{R_r} − mult_det >= D_P := mult_{P_r} − mult_det`.
Consequences: `D_R < 0 ⇒ D_P < 0` (transfers); `D_R > 0` does not imply
`D_P > 0`; but `D_P > 0 ⇒ D_R > 0`, so `R_r`-computations are a *complete
screen* for obstructions (every true obstruction cell shows `D_R > 0`) and
never a certificate.  The house pipeline evaluates at points
`l(s)·per_3(M(s))`, i.e. computes `mult_{P_r}` at every `r`.  Direction 1's
collapsing computes `mult_{R_r}`; equal to `mult_{P_r}` for `r <= 5` by
washout, an upper bound for `r >= 6`.

**What would show it false.**  A cell where the pipeline's `mult_pad`
exceeds an independently computed `mult_{R_r}` (would contradict the
containment — i.e. a bug), or a proof that the pipeline's sampled points do
not lie in `P_r` (they do by construction).

## Deliverable 3 — `docs/dip_transfer.md`

**Expectation, stated before reading in detail.**
- DIP's multiplicity obstruction is exhibited by an explicit highest-weight
  vector of small degree in a 3-row weight, evaluated at a single structured
  point of the *larger* variety (where it is nonzero) and shown to vanish on
  the smaller variety by a structural argument (a Lie-algebra / GIT
  reduction or an explicit vanishing), with tractability coming from the
  point being a product of linear forms or a power sum, on which tableau
  evaluations factor.
- Their occurrence no-go uses that the Chow variety's coordinate ring
  contains every irreducible that the comparison variety's ring contains
  (a "plethysm containment" of the `Sym^d(Sym^n)`-type), via the fully split
  structure `(1^n)` — in particular a `S_n`-symmetrisation / Kronecker or
  Foulkes-type inclusion that has no analogue at splitting type `(1,3)`.
- **Transfer verdict expected:** their *mechanism* (explicit HWV evaluated at
  structured points) transfers; their *no-go* argument does not transfer
  wholesale to type `(1,3)` because it uses the full `(1^n)` symmetrisation,
  but the part that says "a cubic factor with dense restrictions is
  invisible at `ell <= 5`" (our washout) plays the same role and is in fact
  stronger at `ell <= 5`.  Expected honest answer at `ell = 6`: a
  permanent-sensitive separator is *not excluded* by DIP, and their method
  would need `delta` large enough that a 6-row weight has a HWV nonzero at
  `l·per_3(M(s))` and zero on `D_6^det` — cost unknown, to be estimated.
- Candidate cells: at most three, at `ell = 6`, small `delta`, chosen by
  `a > 0`, small `N_S`, and by the `x_0`-multiplicity filtration.

**What would show it false.**  Reading DIP and finding the mechanism is not
HWV evaluation at structured points, or that the no-go rests on something
that transfers verbatim to `(1,3)` — in which case the verdict flips to
"no-go transfers", which is a *success* of the deliverable and will be
reported as such.

## Deliverable 4 — `docs/blindness_slab.md`

**Expected to prove.**  For every `lam` with `ell(lam) <= 4` and every
`delta <= 9` (and `delta <= e − 1` given the principality of `I(D_4^det)`,
which the s35 review closed via Beauville + Jacobian rank 34):
`det_units(lam, delta) = 0`, hence `D(lam, delta) = −pad_units <= 0`.  Strict
cells: `((10,10,10,6,0), 9)` (s35) and the length-`<= 4` weights of the
`delta = 11` and `delta = 15` catalecticant elements — those are at
`delta > 9` and rely on the `e − 1` extension.  For `ell(lam) <= 3`,
`D_3^det = Sym^4 C^3` so `det_units = 0` for *every* `delta` with no
principality needed.  Expected for the `lam_5 = 1` sub-slab: a restriction
argument would need `x_5`-differentiation to carry `D_5^pad` into
`D_5^det`-related loci; Theorem 5 (s32) — the generic `l·c` is not a `4x4`
determinant — is expected to block a containment-based argument, and the
precise stopping point will be recorded.

**Literature pin expected.**  The graded statement
`dim (R/J_F)_{3d−5} = (smooth value) + defect` for nodal hypersurfaces should
be in Dimca's work on Milnor algebras of nodal hypersurfaces (Dimca 1990,
Duke / Compositio; Dimca–Sticlaru) or Cynk–Rams "Defect and Hodge numbers of
hypersurfaces" (Cynk's "Defect of a nodal hypersurface" 2001; Cynk–Rams
2011).  Expectation: the statement exists for nodal hypersurfaces in `P^4`
with defect defined by `h^4 − h^{2,2}`-type invariants, possibly needing the
degree to be exactly `3d − 5` … to be quoted exactly or reported as must-prove.

**What would show it false.**  A weight with `ell <= 4`, `delta <= 9` where
`mult_det < a` (impossible given s33's certified rungs + principality —
would indicate the restriction lemma is misapplied); a literature statement
that gives the defect in a *different* graded degree than `3d − 5`, in which
case the s35 cap is re-labelled accordingly.

## Discipline

Exact arithmetic only (`python-flint` `nmod_mat.rank` over `2147483647` and
`2147483629`); Jacobian ranks at random points are lower bounds on generic
ranks unless an upper bound is argued from structure; no hand-rolled
elimination.  Single-writer files untouched.  Delivery by bundle only.
