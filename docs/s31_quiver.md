# Session brief — s31: `delta_0` by the quiver route

**Branch `s31-quiver`.**  Theory lineage (26 → 28).  Mathematics first; small
exact computations second.  Goal: turn `delta_0` — the first degree at which
`I(D_5)` appears at a length-5 weight — from a search into a computation, using
semi-invariant theory of quivers.

## 0. Standing orders

- Rule 9; new files only; no `paper/`, no `PROJECT_NOTES.md`, no
  `boundary_deficit.html`.  Ancestry: `1203fe4` an ancestor of tip; commits
  above expected.  Pre-register first.  Bundle on push refusal.

## 1. Context, self-contained

`D_5 ⊆ Sym^3 C^5` is the closure of `{det(s_1A_1 + ... + s_5A_5)}`:
dimension 29, codimension 6.  Known (session 28): every member is singular
(a 5-variable pencil must meet the rank-1 Segre: `4 + 4 >= 8`), so the
discriminant of quinary cubics — degree 80, weight `(48^5)` — lies in
`I(D_5)`; and `I(D_5)` is concentrated at weights of length exactly 5.
Bracket: `8 <= delta_0 <= 80` (given the paper's published deficit sequence;
`6 <=` unconditionally).  Session 28's arithmetic sweep found no bite through
`delta = 10` at length 5, and its pre-registered `delta_0 = 8` was refuted.

The unused structure: each coefficient functional `c_alpha`
(`alpha` a degree-3 exponent on 5 slots) is an `SL_3 x SL_3` **semi-invariant**
of the 5-arrow Kronecker quiver at dimension vector `(3,3)`, of weight
`(det_P, det_Q)`:  `det(P M Q) = det P . det Q . det M`.  So

    C[D_5]_delta  =  image of  Sym^delta( span{c_alpha} )  ⊆  SI_{(delta,delta)},

and `I(D_5)_delta` is the kernel.  Derksen–Weyman theory describes
`SI_sigma(Q, beta)` for quivers combinatorially: semi-invariants are spanned by
Schofield determinantal ones `c^V`, the weight semigroup is saturated and cut
out by Horn-type inequalities, and dimensions are computable.

## 2. The work

**A. Set the dictionary up carefully and verify it.**  The `GL_5`-equivariant
grading: `SI_{(delta,delta)}` is a `GL_5`-representation (the five arrows carry
`C^5`); its `lam`-isotypic multiplicity vs the ambient plethysm `a(lam,delta)`
and vs `C[D_5]`.  First checks, non-negotiable before anything new:

    dim span{c_alpha} = 35 -- is that ALL of SI_{(1,1)}?  (compute it)
    the framework must be CONSISTENT with: mult = a at every length-5 weight
      with delta <= 7 (measured, certified), and with disc in I at delta = 80.

**B. Two independent routes to `dim SI_{(delta,delta)}` and its `GL_5` graded
pieces**, e.g. (i) Schur–Weyl / character integral (Molien–Weyl over
`SL_3 x SL_3`, exact, small `delta`), (ii) the Derksen–Weyman / King count via
subrepresentation combinatorics.  Cross-check at `delta <= 6`.

**C. The kernel.**  `I(D_5)_delta != 0` at a length-5 weight iff the map
`Sym^delta(SI_1) -> SI_{(delta,delta)}` fails injectivity there OR the image
misses part of `C[Sym^3 C^5]_delta`'s isotypic piece — sort out which
formulation is the right one (this is exactly the kind of bookkeeping that has
bitten twice; write it down before computing).  Then push `delta = 8, 9, 10,
...` at length-5 weights until the first kernel appears or a structural reason
emerges why it cannot below some bound.  Even a purely combinatorial LOWER
bound on `delta_0` beating 10 would be progress; an upper bound below 80 more
so.

**D. If the machinery is kind**: the six-nodal question.  `dim D_5 = 29 =`
dim of the six-nodal locus.  Is `D_5` a component of it / equal to its closure?
If yes, `I(D_5)` is the ideal of six-nodal cubics and `delta_0` is a question
about multi-discriminants with classical literature.

Literature: Schofield; King; Derksen–Weyman (*Semi-invariants of quivers and
saturation*); Domokos–Zubkov; for D: Gelfand–Kapranov–Zelevinsky on
discriminants and their degrees.

## 3. Pre-registration

1. Predicted `delta_0`, or predicted shape of the answer (attained vs bounded),
   with a falsifier.
2. Whether `SI_{(1,1)}` is exactly 35-dimensional.
3. Whether `D_5` equals the six-nodal closure.

Integrator's priors, stated to be beaten: `SI_{(1,1)} = 35`;  `delta_0` well
below 80 but above 12;  six-nodal equality **true** (dimensions and the
Giambelli count both match) — and if true it is a lovely statement for the
record on its own.

## 4. Kill criteria

- Any inconsistency with `mult = a` at a certified length-5 cell: your
  dictionary is wrong; stop and fix orientation before proceeding.
- If Derksen–Weyman dimensions disagree with Molien–Weyl at any `delta <= 6`:
  stop; one route is misapplied.
- If the six-nodal identification FAILS (a six-nodal cubic that is provably not
  in `D_5`, or dimensions diverge), report it prominently — that would mean
  `D_5` is cut out by more than nodality, which changes the `delta_0` hunt.

## 5. Deliverables

    results/PREREG_s31.md     first
    docs/quiver_route.md      the dictionary, both dimension routes, the kernel
    docs/session_31.md        record, ledger, honest boundary
    analysis/wk8_s31_*.py     Molien-Weyl + combinatorial counts
