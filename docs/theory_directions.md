# Theory directions for the onset window `delta in [9, 405]`, `ell >= 5`

Session 35 (2026-09-01), branch `s35-theory`.  Pre-registration:
`results/PREREG_s35.md` (the rubric, committed before any direction was
generated).  Test ledger: `results/s35_tests.md`; code
`analysis/wk9_s35_daytests.py`.  Clone tip `c02cee8`; ancestry gate passed.
No session-35 collision found.

Convention, restated so it cannot drift: `D(lam, delta) = mult_pad -
mult_det = det_units - pad_units`; an obstruction is a single cell with
`D > 0`; `D < 0` is the expected direction and is not an obstruction.

**Two headline banked results fell out of the day-one tests** (details under
Directions 1 and 2, proofs-and-labels in §B):

1. **The window is no longer empty-handed at its bottom edge: `D < 0` is
   proved at an explicit cell, `(lam, delta) = ((10,10,10,6,0), 9)`** — the
   first cell in the programme where the two multiplicities provably differ.
   The witness is classical: a 9x9 minor of the middle catalecticant, zero on
   `D_5^pad` by a two-line structure lemma, nonzero at explicit integer
   points of `D_5^det` (exact over `Z`).  The det side of the cell is empty
   by s33's certified `e >= 10` plus principality of `I(D_4^det)` (soft link
   named in §B).  Pad's onset is pinned to `[5, 9]`: `I(D_5^pad)` is
   *exactly zero* through degree 4 (measured, all weight blocks, exact).
2. **`D_5^det` is the non-factorial locus in miniature: its generic member
   is a 20-nodal quartic threefold whose nodes fail cubics by exactly 1**
   (defect 1, non-Q-factorial), and the failure is detected by the Jacobian
   ring in degree 7: `(R/J_F)_7 = 31` against 30 for every control class.
   This identifies the geometric structure any det-side ideal element must
   see, and it caps the det onset at `<= 300` (from 405), modulo one
   literature statement and one transversality page.

---

## A. The ranked directions

Scores are `I x P / C` per the pre-registered rubric (impact-if-works x
probability-of-working / days-to-first-decision).  First tests marked RUN
were executed and banked this session.

| # | direction | I | P | C | score |
|---|---|---|---|---|---|
| 1 | Pad is catalecticant-degenerate; Kempf collapsing computes its ideal | 5 | 0.7 | 0.5 | 7.0 |
| 2 | The defect route: non-factoriality is the det-side structure | 4 | 0.8 | 0.5 | 6.4 |
| 3 | Mine the GCT-obstruction literature with these two varieties in hand | 3 | 0.85 | 0.5 | 5.1 |
| 4 | The occurrence screen in the window: `a` vs rectangular Kronecker | 5 | 0.6 | 2 | 1.5 |
| 5 | Multiplicity blindness as a half-theorem: `D <= 0` on `ell <= 4`, and where the proof stops | 3.5 | 0.3 | 1 | 1.05 |
| 6 | The flattening rank screen: hunt a det-dropper | 4 | 0.25 | 1 | 1.0 |
| 7 | Break the `N_S` wall: abstract-HWV evaluation at structured points | 4 | 0.45 | 2 | 0.9 |

Directions 1 and 2 are developed in depth in §B and §C; 3–7 are stated in
brief in §D.  §E records what was considered and discarded under the
pre-registered criteria.  §F is the honest boundary.

---

## B. Direction 1 — pad is catalecticant-degenerate, and its whole ideal is
## computable without elimination  *(seed B, delivered and extended)*

**(i) The claim.**  `I(D_5^pad)` is an essentially classical object: its
low-degree part is controlled by the middle catalecticant, its onset is
`[5, 9]` (bracket closed this session from both sides), and its full
weight-by-weight multiplicity is computable by a Kempf collapsing — Bott
cohomology on `P^4` plus Koszul homology in *isotypic-sized* blocks, with no
`N_S`-sized elimination anywhere.  This converts the obstruction hunt from
two unknowns per cell to one: at any candidate cell, `pad_units` becomes a
lookup, and only `det_units` needs compute.

**(ii) The mechanism.**  Three parts, in increasing strength.

*(a) The catalecticant lemma (proved).*  For `F = l.c` the middle
catalecticant `Cat_{2,2}(F): Sym^2 V^* -> Sym^2 V` has rank `<= 10`
(at `r = 4`: `<= 8`): second partials of `l.c` are
`l.(d_i d_j c) + (d_i l)(d_j c)` with `d_i d_j c` *linear* (c is a cubic)
and `d_i l` *scalar*, so the image lies in `l.V + span{d_j c}`.  This is
special to `n = 4` — quartics have a square middle catalecticant, cubics do
not — and is why the pad side got classical precisely at this `n`; nothing
like it exists in the `n = 3` mirror, which is consistent with it never
appearing in the record.  Measured (T1, T1r4): pad points sit at exactly
10 (r=5) and 8 (r=4); det pencils, generic quartics, and `q.q'` products
all have full rank.  Consequences, all explicit:

- `(11 x 11 minors of Cat) subset I(D_5^pad)_11`, and the degree-15
  invariant `det Cat_{2,2}` of weight `(12^5)` is in `I(D_5^pad)_15`;
  neither is in `I(D_5^det)` (rank 15 at an explicit integer det point is
  an exact certificate).  These are the first explicit equations of
  `D_5^pad` on the record, and they also separate the `l.c` component from
  the `q.q'` component of the reducible locus (T1: `q.q'` has full rank).
- At `r = 4` the 9x9 minors give **degree-9** elements.  The extremal
  minor (omit the lowest-weight row and column) has every Leibniz term of
  torus weight `(10,10,10,6)`, is the unique 9-minor of that weight — the
  dominance-maximal weight of the minor span, so a nonzero value exhibits a
  highest-weight vector — and evaluates to a nonzero *integer* at a generic
  quartic and at a det-surface pencil, and to 0 at pad points (T1w, exact
  over `Z`).  Hence `S_(10,10,10,6) subset I(D_4^pad)_9`, a covariant in
  `I(D_4^pad) \ I(D_4^det)` of degree 9 — five orders of magnitude below
  `e = 320112`, which is the sharpest possible illustration of how
  differently the two `r = 4` ideals begin.

*(b) The banked cell (proved / certified, one named soft link).*  Read at
`r = 5`, the extremal minor's coefficient functions involve only `alpha`
supported on `x_1..x_4`, and `c_alpha(F) = c_alpha(F|_{x_5=0})`, so the
minor vanishes on `D_5^pad` (restriction of `l.c` to a 4-plane is again a
padded form) and is nonzero at a generic point of `D_5^det` (its restriction
is a generic 4-variable pencil; nonzero value banked exactly).  Therefore

    pad_units((10,10,10,6,0), 9)  >=  1        (proved, exact arithmetic)
    det_units((10,10,10,6,0), 9)  =   0        (certified + one soft link)
    =>  D((10,10,10,6,0), 9)  <=  -1.

The det line: a length-4 weight sees `D_5^det` through `D_4^det` (the s28
restriction argument, re-used at `n = 4`), whose ideal is principal of
degree `e`, and `e >= 10` is s33-certified — so degree 9 is empty at every
length-`<= 4` weight.  The one soft link is principality itself, i.e. codim
exactly 1 at `r = 4`, which rests on the finite-stabiliser page flagged in
`docs/s30_review.md` §3 and still unwritten.  A one-cell direct measurement
of `mult_det((10,10,10,6), 9)` at `r = 4` (house pipeline, small `N_S`)
would remove even that; it is the cheapest possible follow-up and should be
s36's first act.  **This is the first cell in the programme where
`mult_pad != mult_det` is proved rather than argued** — in the expected
`D < 0` direction, exactly as the s34 interpretation rule anticipates
(pad's variety is smaller; its ideal switches on first).

*(c) The collapsing (the direction proper — expectation, standard
machinery).*  `D_5^pad` is the image of the total space of the rank-35
subbundle `S = O(-1) (x) Sym^3 C^5 subset O (x) Sym^4 C^5` over
`P^4 = P(V^*)`, via multiplication; the collapsing is generically finite of
degree 1 (a generic `l.c` has a unique linear factor), i.e. birational.
This is exactly the situation of Weyman's geometric technique, with two
gifts: the base is `P^4` (Bott is trivial there), and the Koszul terms
`Lambda^k T^*` (`T = O(x)Sym^4 / S`) resolve by
`Sym^b(Sym^3 C^5)^* (x) Lambda^{k-b}(Sym^4 C^5)^* (x) O(b)` with `b >= 0`
— every twist nonnegative, so **all higher sheaf cohomology vanishes** and
the hypercohomology reduces to Koszul homology of explicit `GL_5`-maps.
Every object in sight is a plethysm-graded module, and the homology
computation splits into blocks of *multiplicity* size (tens to hundreds),
not weight-space size.  The `N_S` wall does not appear.  Outputs if it
works: `mult_pad(lam, delta)` exactly, for every weight, at every
`delta <= ~15` and plausibly far beyond; as corollaries the normalisation
defect of `D_5^pad` (the gap between `mult_pad` and the bidegree-`(d,d)`
bound `h_pad(lam, delta) = sum over Pieri strips of Sym^delta(Sym^3)`
multiplicities — `h_pad` alone is already a cheap new per-cell upper...
lower context: `h_pad` bounds `mult_pad` above, so `a - h_pad` bounds
`pad_units` below: cells with `h_pad < a` have pad-forced ideal, the
pad-side analogue of the `m_det` screen).

**(iii) The falsifiable first test (<= 1 day; the day-one half was RUN).**
Run: the catalecticant battery, the exact `I(pad)_{<=4} = 0` computation,
and the `(10,10,10,6)` witness — all banked (`results/s35_tests.md`).  The
remaining first test for (c): implement the Koszul-homology route and
reproduce, per weight, three banked s30 `mult_pad` values at `delta = 6`,
then one s34 `delta = 7` value once their ledger lands.  Validate-then-use,
the s33 ordering.

**(iv) What kills it.**  For (c): a mismatch against banked `mult_pad`
values that survives debugging kills the implementation; a conceptual
failure (e.g. the ideal-vs-normalisation bookkeeping needs `D_5^pad` normal
and it is not) would downgrade the route from "ideal exactly" to "ideal of
the normalisation + correction terms" — still decisive if the correction is
computable, dead if not.  For the banked cell: only an error in the
restriction argument or the s33 certificates could kill it; both are in the
record.

**(v) What changes if it works.**  Every candidate obstruction cell in the
window gets its pad side for free; the `delta = 9..12`, `ell = 5` strip
becomes "compute `det_units` only"; s34-style sweeps stop paying the pad
half of their budget; and the blindness hypothesis becomes *testable in
bulk* on the pad side (any cell with `pad_units = 0` and `a > m_det`-style
det-side evidence is an obstruction candidate locatable by table lookup).

---

## C. Direction 2 — the defect route: `D_5^det` lives in the non-factorial
## locus, and degree 7 of the Jacobian ring sees it
## *(seed A executed, then pushed past the nodal count)*

**(i) The claim.**  The generic member of `D_5^det` is a 20-nodal quartic
threefold whose 20 nodes lie on a length-20 subscheme of the rank-`<= 2`
locus cut by 16 independent cubics — one more than the 15 that 20 general
points allow.  So the generic det quartic is **non-Q-factorial with defect
exactly 1**, and the defect is visible as `(R/J_F)_7 = 31` against the
smooth value 30.  `D_5^det` is an irreducible component of the 20-nodal
locus (the `nu = codim = 20` pattern of the `n = 3` mirror replicates
exactly), but the *sharper* statement is the new one: it lies inside the
nodal-with-defect locus, which general k-nodal quartics avoid for every
constructible k.  Consequences: an explicit det-side ideal element family in
degree 300 (cap `405 -> <= 300`), and a precise structural target — any
`D > 0` witness in the window must vanish on defective quartics or see the
defect indirectly.

**(ii) The mechanism, with the evidence.**

*(a) The 20 nodes (proved modulo one standard transversality page).*
`sigma_2(P^3 x P^3) subset P^15` has projective dimension 11 (codim 4) and
Giambelli degree **20**; a generic `P^4` misses `sigma_1` (dim 6:
`4 + 6 < 15`) and meets `sigma_2` transversally (Kleiman, char 0) in 20
reduced points of rank exactly 2.  At such a point the adjugate vanishes
(rank 2 in size 4 kills all 3x3 minors), so by Jacobi every partial of
`det M(s)` vanishes; conversely at rank-3 points the gradient
`s -> v^T A_k u` is generically nonzero, so `Sing F` = the 20 points.  The
Hessian at a rank-2 point is, in adapted bases, the 2x2 determinant of the
complementary block of `M(t)` — a rank-4 quadric for generic data, i.e. an
ODP.  Measured (T2, T2node): the minor-ideal Hilbert function stabilises at
exactly 20 (both primes), and constructed rank-2 points have Hessian rank
4/4 at three independent pencils.  Dimension count as in s31 §5: every
component of the 20-nodal locus has projective dimension `>= 69 - 20 = 49`;
projectivised `D_5^det` is irreducible of dimension 49 inside it — a
component.  `nu = 20 = codim`, the `n = 3` pattern (`6 = 6`) on the nose.

*(b) The defect (measured at 4 pencils; formula verified against the
literature).*  `h^0(I_Z(3)) = 16` at the saturated node scheme (T2sat: the
16 minors of `M(s)`, independent at both primes, and *nothing else* — the
saturation adds no cubic).  Twenty general points would impose independent
conditions: `35 - 20 = 15`.  So the nodes fail cubics by exactly 1.  By the
nodal-threefold factoriality criterion (Cheltsov, after Clemens–Cynk–
Werner: a nodal quartic threefold is Q-factorial iff its nodes impose
independent conditions on forms of degree `2.4 - 5 = 3`), the generic det
quartic threefold is **non-factorial with defect 1** — which is the
classical determinantal story seen from our side: the cokernel sheaf of
`M(s)` supports a Weil divisor class that is not Cartier at the nodes.
The Jacobian-ring shadow (T2J/T2Jdet3/T2K, the session's sharpest single
measurement): `(R/J_F)_7 = 31` at four independent det pencils, `30`
(the smooth CI value, proved by Koszul exactness) for generic quartics
**and for quartics with k nodes at general points for k = 1, 5, 11, 13** —
the excess detects the *configuration*, not the count, exactly as the
defect reading predicts (general nodes never fail cubics for `k <= 35`).

*(c) The cap (`405 -> <= 300`; two labelled steps from theorem).*  Let
`M_7(F)` be the degree-7 Macaulay matrix of the five partials
(`330 x 350`, entries linear in `F`).  Generic corank is exactly 30
(proved), so its size-300 minors are nonzero polynomials of degree 300 in
the coefficients of `F`; on `D_5^det` the corank is `>= 31` — measured at
four pencils, and forced generically by (b) if the standard nodal-threefold
statement "(R/J)_{3d-5} = smooth value + defect" holds, then on all of
`D_5^det` by semicontinuity.  Hence `I(D_5^det)_300 != 0`:

    onset of I(D_5^det)  in  [9, 300]   (from [9, 405])

pending (1) the Milnor-algebra-degree-7 defect statement, to be pinned in
Dimca/Cynk/Rams (the factoriality criterion itself is verified; the
degree-`3d-5` graded refinement is the piece to quote precisely), and
(2) the Kleiman transversality page of (a).  Label until then: measured +
mechanism-identified, expectation for the full locus.  A parallel fact with
the same logic and no literature dependence: the corank-1 excess means the
five partials of a det quartic admit **one extra syzygy in degree 7**
(coefficients of degree 4) beyond Koszul — a candidate closed form via
adjugate identities (`d_k F . adj M = adj M . A_k . adj M + F . d_k(adj M)`)
is the natural follow-up and would make the whole chain elementary.

*(d) Where the ceiling-collapse hope honestly stands.*  Fitting-style
covariants of an F-linear matrix cost their minor size: the `t = 7` family
costs 300, `t = 8, 9` cost more, and nothing in this family goes below 300.
A genuinely lower-degree det-side element would need a different mechanism
— the eliminant of "some cubic beyond the expected 15 passes through
`Sing F`", or Direction 6's flattening search.  The 300-family also lies in
`I(D_5^pad)` (pad's Jacobian corank at `t = 7` is far larger — T2J), so the
cap improves but the *separating* covariant is not this one.  Stated so the
seed-A hope is neither oversold nor lost: the ceiling moved by 25%, not by
an order of magnitude, and the structural identification (defect) is the
real product.

**(iii) The falsifiable first test — RUN** (T2, T2sat, T2node, T2J,
T2Jdet3, T2K; all banked).  The remaining <= 1-day tests: (1) pin the
degree-7 defect statement in the literature (one focused reading pass);
(2) hunt the explicit degree-7 syzygy at one pencil by linear algebra on
adjugate-built candidates.

**(iv) What kills it.**  The component statement dies only with the
transversality argument (nothing measured contradicts it, and the `n = 3`
twin is proved).  The cap dies if the degree-7 defect statement fails as
quoted *and* the four-pencil measurement turns out non-generic — jointly
unlikely, but the honest kill is stated.  The hope of a sub-300 element
dies if the eliminant analysis lands at minor-sized degrees too; that would
itself be worth banking (it would say degree-7-visible structure cannot be
seen cheaply, pushing the hunt to Directions 4/6).

**(v) What changes if it works.**  The window top drops to 300; the det
ideal acquires its first structural description (inside the defect locus's
ideal); the `D > 0` hunt gets a target predicate — det-specific structure
beyond defect (the *class* of the non-Cartier divisor, i.e. the ACM/Ulrich
sheaf data, is exactly what pad points lack — a cohomological separator
candidate for future sessions); and the paper's `n = 4` section gains a
clean classical anchor (non-factoriality) matching the `n = 3` six-nodal
story.

---

## D. Directions 3–7, in brief

**3. Mine the GCT-obstruction literature with the two varieties in hand**
*(seed D, reading half; partially run).*  (i) Claim: the existing
multiplicity-obstruction exhibit — Dörfler–Ikenmeyer–Panova (ICALP 2019 /
SIAM J. Appl. Alg. Geom.), Chow variety vs powers-of-linear-forms — is
structurally the closest thing to our pair: their `Ch^n_m` is the fully
split cousin of our `D_5^pad` (splitting type `(1,3)` instead of
`(1,1,1,1)`), and they prove multiplicity obstructions exist where
occurrence obstructions provably do not.  (ii) Mechanism: their Lemma-3.4-
style GIT reduction of `mult(C[Ch])` and their plethysm bookkeeping port to
splitting type `(1,3)` — which is exactly the `h_pad`/collapsing object of
Direction 1; their λ = (n²-2, n, 2) is a 3-row partition, encouraging for
our forced-`ell = 5` regime.  Also to mine: Ikenmeyer–Panova rectangular-
Kronecker positivity (arXiv:1512.03798) for Direction 4's feasibility map,
and Bürgisser–Ikenmeyer HWV-evaluation for Direction 7.  (iii) First test
(<= 1 day, half done): the DIP setting/technique match was verified today
against the paper; remaining: extract their occurrence-no-go argument and
check which side of it survives padding type `(1,3)`.  (iv) Kill: if their
no-go transfers wholesale to our pair it *kills Direction 4's hunt* and
promotes blindness — that is a success of this direction, not a failure;
it dies only if the techniques turn out genuinely `(1^n)`-specific.
(v) If it works: either a template for exhibiting our obstruction or a
template for the no-go — both decisive.

**4. The occurrence screen in the window** *(seed C, structural half).*
(i) Claim: cells with `a(lam, delta) > m_det(lam, delta)` have
`det_units >= a - m_det > 0` with no geometry; the `n = 3` mirror fired at
`delta = 10` (s28).  At `n = 4` nobody has looked above `delta = 7`.
(ii) Mechanism: `m_det <= g(lam, (delta^4), (delta^4))` (5-arrow Kronecker
quiver on `M_4`, transpose-refined as in s31-D3); compute `a` by the ladder
DP and `g` by nested Kostant sums for `delta = 8..12`, `ell(lam) = 5`; the
IP rectangular-Kronecker positivity results say where `g = 0` *cannot*
happen, mapping the screen's reachable prey in advance.  An
obstruction-eligible cell is `m_det`-bound `< a <= h_pad`-attainment;
`mult_pad = a` at such a cell is then the single remaining unknown
(Direction 1 supplies it).  (iii) First test (~2 days): the `delta = 8`
row end-to-end, validated against the `delta <= 7` overlap with s30/s34.
(iv) Kill: IP-positivity covering all `ell <= 5` weights with `a > 0`
through the affordable range — then the occurrence route is *provably
closed* there, a blindness-side theorem worth banking (rubric: decisive
either way).  (v) If a live cell appears at reachable `N_S`: it is the
programme's first concrete obstruction candidate with one unknown left.

**5. Multiplicity blindness as a half-theorem.**  (i) Claim, provable part:
for every weight with `ell(lam) <= 4` and `delta <= 9` (certified; through
`e - 1` given principality), `det_units = 0`, so `D = -pad_units <= 0`:
**blindness in the obstruction direction is now a theorem on the whole
`ell <= 4` slab** — and this session exhibited cells there where the
inequality is strict.  The open half is `ell = 5`.  (ii) Mechanism
candidates for `ell = 5` sub-regimes: restriction filtrations by the
multiplicity of `x_5` (interpolating between the closed `ell <= 4` slab and
the open balanced cells), and DIP's no-go geometry (Direction 3).
(iii) First test: formalise the slab statement (a half page, essentially
done above) and probe the `lam_5 = 1` sub-slab for a restriction argument.
(iv) Kill: the `lam_5 = 1` argument needs pad ⊆ det after one
differentiation, which Theorem 5 (s32) likely poisons — if so, record why
and stop.  (v) If it works: the window narrows to balanced `ell = 5`
weights, a large cut in search space.

**6. The flattening rank screen: hunt a det-dropper.**  (i) Claim: some
`F`-linear equivariant map (Young flattening, Koszul flattening of the
Jacobian, adjugate-composite) drops rank on `D_5^det` below its pad and
generic values — the mirror image of the catalecticant, and a direct
`D > 0` mechanism at that flattening's minor weights.  (ii) Mechanism:
det points carry structure pad points lack (the rank-2 scheme, the ACM
divisor class); the `t = 7` Macaulay corank shows det-droppers *exist*
(size 300); the question is whether any exist at small size.  (iii) First
test (1 day): systematic rank triples (generic / det / pad, both primes)
over a list of small flattenings — `Cat_{1,3}`-augmented Koszul maps
`Lambda^p V (x) Sym^a V^* -> ...` built from `dF`, Hessian-of-`F`
composites, `adj M`-free constructions in the coefficients of `F`.
(iv) Kill: every tried flattening has `rank_det >= rank_pad` and no drop
below generic — banked as a calibrated negative (and evidence that
det-droppers need size ~O(100)+, consistent with `e`'s hugeness at
`r = 4`).  (v) If a small det-dropper exists: explicit candidate weights
for `D > 0` and a covariant to hand s36 for per-cell certification.

**7. Break the `N_S` wall by abstract-HWV evaluation** *(seed D, compute
half).*  (i) Claim: `mult` lower bounds need only (number of HWVs) x
(evaluations at variety points), never a weight-space elimination — the
Bürgisser–Ikenmeyer method; pad points `x_0.c` are sparse and structured,
so evaluations may factor combinatorially.  (ii) Mechanism: tableau-indexed
HWVs of `Sym^delta(Sym^4 C^5)` evaluated at `l.c` and at pencils;
`mult_pad = a` certificates at cells beyond the 7.2 GB frontier are
exactly what obstruction confirmation needs.  (iii) First test (~2 days):
implement for one banked `delta = 6` cell (must reproduce s30), then one
unreachable `delta = 7` cell with small `a`.  (iv) Kill: evaluation cost
explodes combinatorially before any unreachable cell is reached (the honest
risk; the structured-point factorisation is the mitigation to test first).
(v) If it works: the window's cheap-`a` cells at `delta = 8..10` open up
on both sides, and Direction 4's candidates become certifiable in-house.

---

## E. Considered and discarded (pre-registered criteria)

- **Global dimension-crossover counting** at `n = 4` (the s31 route):
  discarded under criterion 1 (killed route; the integrator's brief states
  the same Hilbert comparison kills it here).  Per-weight arithmetic
  screens (Direction 4) are not this route.
- **Rung-climbing at `r = 4`** in any disguise: criterion 1 (s33 closed it).
- **Vainsencher multinodal-class formulas as equation sources**: his
  formulas give classes (degrees) of k-nodal loci for `k <= 6`, not
  equations, and our k = 20 is outside their range; the Fitting-degree
  analysis in C(ii)(d) explains why naive nodal-count covariants cost
  hundreds of degrees anyway.  Folded into Direction 2's honest boundary
  rather than kept as a direction.
- **The `U_det` vs `U_pad` subspace comparison** (s32's flagged probe):
  still blocked — it needs a cell where *both* ideals are nonzero, and the
  banked cells have `det_units = 0`.  Unblocks at the first det-side bite.
- **`q.q'`-component bookkeeping**: `Cat` separates it from `l.c` (T1), and
  it is not in the padded chain; no direction needed.

## F. Honest boundary

- **Proved outright:** the catalecticant rank lemma on pad (both `r`); the
  weight and HWV status of the extremal 9-minor; `S_(10,10,10,6) subset
  I(D_4^pad)_9` and its `r = 5` lift into `I(D_5^pad)_9` with nonvanishing
  on `D_5^det` (exact integer evaluations); the smooth Jacobian-ring row;
  every component of the 20-nodal locus having dimension `>= 49` and
  `D_5^det` being irreducible of dimension 49 (hence a component, given
  (a)'s genericity); the `ell <= 4` slab statement of Direction 5 at
  `delta <= 9` (using only s33 certificates).
- **Measured, both primes, seeds independent:** `I(D_5^pad)_delta = 0` for
  `delta <= 4` (exact, all weight blocks); length-20 stabilisation of the
  node scheme; `h^0(I_Z(3)) = 16`; Hessian rank 4 at constructed rank-2
  points (3 pencils); `(R/J)_7 = 31` at four det pencils vs `30` at
  `k <= 13` general nodes; catalecticant ranks 10/15/8/10 as tabulated.
- **Adopted from literature, verified to the statement quoted:** the nodal
  quartic-threefold factoriality criterion (nodes vs cubics — Cheltsov,
  after Clemens/Cynk/Werner); DIP's setting and technique.  **To pin:**
  the graded degree-7 Milnor-algebra defect statement (Direction 2's cap
  rests on it; until then the cap is expectation with 4-pencil evidence);
  the precise Chipalkatti/CGGHMNS state of the art on reducible-form
  ideals (Direction 1 does not depend on it, but priority must be checked
  before the paper claims novelty for the degree-9/11/15 equations).
- **Expectation, labelled:** the Kempf-collapsing computation (mechanism
  standard, bookkeeping unrun); the transversality page; the sub-300
  eliminant hope; everything in Directions 4–7 not yet run.
- **Soft link inherited and named:** principality of `I(D_4^det)` (the
  s30 §3 finite-stabiliser page) enters only the `det_units = 0` line of
  the banked cell; a one-cell direct measurement removes it.
- **Sign discipline:** the banked cell is `D < 0` — the *expected*
  direction, not an obstruction; nothing in this session moves the
  obstruction question itself, which remains open in both directions, and
  the two headline results cut the window at both ends without deciding it.
- The day-one Giambelli print initially showed 18 from a per-factor
  integer-division bug; fixed before any use, and the measured Hilbert
  function (20, both primes) is the independent check.  Recorded per house
  transparency rules.
