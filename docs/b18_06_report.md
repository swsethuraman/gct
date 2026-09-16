# B18-06 — Choose cells by the size of the missing proof

15 September 2026. Slot 06, batch 18. Worktree `work/batch15_workers/B15-06`.
Author: Claude (Opus 5). Theory plus existing-data intake; any pilot is declared
in §6 before it runs.

**Provenance (read-only, recorded before any write):**

```
git rev-parse HEAD          8f7ab3bbc1f5352b2ec705894c56f69c93bc6c36
git rev-parse HEAD^{tree}   f0428d8181e067362b71afa663c4b574392777ff
```

No other git command was run.

## 0. Plain terms

We want a finite cell `(d, lambda)` where the padded permanent has *more*
highest-weight coordinate directions than the determinant. To prove that, two
separate proofs are needed in the same cell:

1. a **determinant upper bound** `B`, proved globally on the whole closure, and
2. an **actual padding lower bound** `r > B`.

"The size of the missing proof" is how far each side is from what we already
have. This report sizes both sides for each cell family that is still open,
using only numbers already in the tree where possible, and says which side
binds.

**Conclusion in plain terms.** No cell is nominated (§7). In every open row
count one side of the proof is missing entirely, not merely expensive:

- **Five to eight rows.** Padding is cheap to certify here; in five rows
  exactly. But a gap needs at least one determinant equation of that row type
  (Lemma 2.1). None is known, and the only equation mechanisms in the tree
  provably cannot produce one (Lemmas 3.1–3.2). The symmetric orbit bound
  never drops below the ambient multiplicity where it has been measured.
  So the boundary route must first certify at least 22 dimensions of
  "dead loss" in the best unclosed five-row cells.
- **Ten rows.** Determinant equations exist, but padding's ten-variable
  ceiling sits far below the ambient multiplicity.

Along the way: the five-row family with the smallest symmetric bound,
`(4d-8,2^4)`, is closed by a Hessian covariant (Prop. 4.1). A declared pilot
closed the next five cheapest five-row cells and one `a = 2` cell, each with
`D = 0`, in at most 5 s each (§6). The practical rule for the integrator:
**never build a carrier before one determinant full-rank evaluation in the
same cell.**

Plan:

1. reconcile what is already covered (§1);
2. derive the quantities that decide whether a cell is worth preferring,
   in particular two structural facts about five- to eight-row cells (§2–§4);
3. if a pilot is needed, declare its exact cells, range and cap *before*
   running it (§6; there is no §5, the numbering was fixed before the pilot);
4. size the open families and build the requested table (§7);
5. one next test (§8), labelled claims and negatives (§9), resources (§10).

Conventions are ADOPTED from the preamble: forms in `Sym^4(V*)`, coefficient
ring `Sym(Sym^4 V)`, ordinary coefficients `c_alpha = [x^alpha]F`, positive
weights, `E_ij c_alpha = (alpha_i+1) c_(alpha+e_i-e_j)`. `s` always means the
**symmetric** rectangular Kronecker coefficient (full stabilizer, transpose
included), `s = (g + t)/2`, where `g = g(lambda,(d^4),(d^4))` is the ordinary
(connected) rectangular Kronecker coefficient and `t` is the transpose trace.
`U = min(a, T)` is always clipped.

## 1. What is already covered (reconciliation, before adding anything)

Sources read: `SUMMARY_B15_B17.md`; `B15-06/docs/b17_06_report.md`;
`B15-08/docs/b17_08_report.md`; `B15-11/docs/b17_11_supplement04_08.md`;
`Batch17_Planning/SCREEN_REPORT.md` with `degree7_screen.json` and
`finite_screen.json`; `Batch17_Planning/symmetry_dream/astra/TOY_CALCULATIONS.md`
with `toy_character_screen_d5_d6.json`; `Batch16/STOCKTAKE.md`;
`Batch15_Launch/native_20260913/BATCH15_STOCKTAKE.md`; `B15-02/docs/b15_02_report.md`;
`B15-12/docs/b15_12_report.md` (head); the revised B18 board; and, as an
**unreviewed** input only, `batch18_launch/b18_01_report_v1.md` §§5–6.

### 1.1 The ten excluded cells (ADOPTED)

All ten have tail `2^8`, so all have length ten.

| source | d | lambda | a | i_det (q) | m_det | U | q+U-a |
|---|---:|---|---:|---:|---:|---:|---:|
| B16 | 23 | (61,15,2^8) | 189 | 1 | 188 | 158 | -30 |
| B16 | 25 | (67,17,2^8) | 294 | 4 | 290 | 218 | -72 |
| B16 | 26 | (71,17,2^8) | 294 | 4 | 290 | 218 | -72 |
| B16 | 27 | (73,19,2^8) | 429 | 11 | 418 | 288 | -130 |
| B17 screen | 23 | (4d-t-16,t,2^8), t=17 | 292 | 2 | 290 | 218 | -72 |
| B17 screen | 24 | t=17 | 293 | 3 | 290 | 218 | -72 |
| B17 screen | 23 | t=19 | 419 | 4 | 415 | 288 | -127 |
| B17 screen | 24 | t=19 | 424 | 7 | 417 | 288 | -129 |
| B17 screen | 25 | t=19 | 427 | 9 | 418 | 288 | -130 |
| B17 screen | 26 | t=19 | 428 | 10 | 418 | 288 | -130 |

I read the "ten explicitly excluded cells" of the preamble as exactly these
four plus six. The tree does not print that list under that name, so this
identification is itself ADOPTED, not certified.

### 1.2 Other closed regions (ADOPTED, with the source's own scope)

| region | status | source |
|---|---|---|
| every lambda with length <= 4, every d | `D <= 0` | B17-01/03 |
| every lambda with length > 10 | `m_pad = 0` | ten essential variables (B15-12, B16) |
| nine-row tail `(21,2^7)`, d >= 16 | excluded under recorded transport premises; d = 14, 15 closed by B16-07 | Batch16 BOARD/STOCKTAKE |
| nine-row LMR ladder, `(65,17,2^7)` at d = 24 | `D` in `[-4,-3]` under accepted premises | B15-01 |
| seven/eight-row tail 21 and twenty lower odd-tail families | full determinant rank (378, 460) plus transport | B15-06 |
| nine degree-7, seven-row, `a = 1` cells | `m_det = 1 = a`, retired at the first determinant point | B15-02 |
| degree-8 cells `(13,11,3,2,1^3)` and two others | `D <= 0` | B15-03/04 |
| degree 1–6, **every** cell | symmetry census: `symmetry_deficit_cells = 0` (no cell has `s < a`), `headroom_cells = 0` | Astra toy census |
| degree 7, `lambda = (28-|nu|, nu)`, `|nu| <= 10`, `2 <= len(nu) <= 6`, `a >= 2` | 114 shapes / 31 eligible; no `1 <= B = min(a,s) < U` | B17 degree-7 screen |
| seven cells of B15-12 | every symmetric Kronecker bound exceeds `a` | B15-12 |

### 1.3 What the degree-7 screen actually covered in the admissible range

**MEASURED here** from `degree7_screen.json`: of the 31 eligible rows, 29 have
length 3 or 4. Those were already closed for gaps in every degree by B17-01/03,
which post-dates the screen's design. Only **two** eligible rows lie in the
admissible range 5–10:

| d | lambda | a | U | g | t | s | B | b_required = s-U+1 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 7 | (18,5,2,2,1) | 2 | 2 | 93 | 13 | 53 | 2 | 52 |
| 7 | (18,4,2,2,2) | 3 | 3 | 61 | 33 | 47 | 3 | 45 |

So the degree-7 screen is, in effect, a two-cell five-row screen. It is **not**
evidence about five- to ten-row cells in degree 7 beyond those two.

### 1.4 Every admissible cell for which `s` is on disk has `s >= a`

**MEASURED here** from the Astra census, lengths 5 and 6 only:

| d | length | cells | cells with s < a | min (s - a) | argmin |
|---:|---:|---:|---:|---:|---|
| 5 | 5 | 23 (all a=1) | 0 | 4 (U=0 cell (4^5)); 7 among U >= 1 | (12,2^4) |
| 6 | 5 | 105 (38 with a=1) | 0 | 7 | (16,2^4) |
| 6 | 6 | 59 (55 with a=1) | 0 | 9 (U=0 cell (4^6)); 12 among U >= 1 | (14,2^5) |

Smallest `b_required = s-U+1` among `U >= 1` cells, same data (MEASURED):

| d, length | 1st | 2nd | 3rd | 4th |
|---|---|---|---|---|
| 5, five rows | (12,2^4): 8 | (9,7,2,1,1): 15 | (7,7,4,1,1): 19 | (8,5,5,1,1), (8,7,3,1,1): 23 |
| 6, five rows | (16,2^4): 8 | (15,3,2,2,2): 15 | (11,9,2,1,1): 22 | (12,8,2,1,1): 24 |
| 6, six rows | (14,2^5): 13 | (9,9,2,2,1,1): 53 | (13,4,2,2,2,1): 75 | (8,8,2,2,2,2): 86 |

The best `a >= 2` five-row entry at d = 6 is (8,7,7,1,1): `a = U = 2`, `s = 30`,
`b_required = 29`. For six rows `U` is only the generic-product ceiling
(§3.3), so its `b_required` is itself an under-estimate of the real requirement.

Together with 1.2 (degree-7 rows, B15-12's seven cells), no admissible cell in
the tree has a symmetry deficit. So `B0 = min(a,s) = a` everywhere measured,
and by the clipping lemma of B17-08 (ACCEPTED)

```
b_required = s - U + 1 = (s - a) + (a - U + 1).
```

The first summand, `s - a`, is **dead loss**: boundary rank that must be
certified before the determinant bound improves at all. The second, `a - U + 1`,
is the part that actually buys headroom. This split is the basis of the
ranking below.

## 2. What a positive cell needs, stated as necessary conditions

All statements in the fixed cell `(d, lambda)`.

**Lemma 2.1 (PROVED, elementary).** `D > 0` implies `i_det >= a - m_pad + 1 >= a - U + 1 >= 1`.

*Proof.* `D = m_pad - m_det = m_pad - a + i_det > 0` gives `i_det >= a - m_pad + 1`;
`m_pad <= U <= a` gives the rest. QED.

Therefore **a positive cell must carry at least `a - U + 1` independent
determinant equations of its own type.** A cell certified to have `i_det = 0`
(one full-rank determinant evaluation, `rank = a`) is closed. This is why
B15-02's nine cells closed at the first point.

**Lemma 2.2 (PROVED).** For any boundary-rank floor `b` with `0 <= b <= s - m_det`
(the only achievable range, since forbidden projections vanish on the
`m_det`-dimensional extension space), `B(b) < U` forces `m_det <= U - 1`; if
`U = a` it forces `i_det >= 1`.

*Proof.* `m_det <= B(b) = min(a, s-b) <= U - 1`. QED.

So the boundary route of B17-02 is, logically, a **non-constructive proof that
determinant equations exist** in the cell. It cannot succeed in a cell that
Lemma 2.1's single evaluation already closes. **Consequence for slots 02/03:**
before building any full-stabilizer carrier, which scales with `s`, run the
determinant full-rank evaluation in that cell. It costs one HWV construction
and `a` evaluations, and closes the cell if the rank is `a`.

## 3. Row count decides which proof is missing

### 3.1 Every known determinant-equation mechanism is blind to at most eight rows

**Lemma 3.1 (PROVED, extends B17-08 (8) to every generator in the tree).** Let
`J` be the ideal of `Sym(Sym^4 V)` generated by the determinant equations that
the tree certifies:

- the LMR/flag module `E24` of type `(65,17,2^7)`;
- the stable tail-21 four-space and its lifts, types `(4d-35,21,2^7)`;
- B15-01's degree-14 reduced equations, type `(25,17,2^7)`;
- the tail-19 eleven-space and its lifts, types `(4d-35,19,2^8)`;
- the degree-23 equation, type `(61,15,2^8)`, and the tail-17 classes, types `(4d-33,17,2^8)`.

Then `Hom(S_lambda V, J_d) = 0` for every `d` and every `lambda` with
`length(lambda) <= 8`.

*Proof.* Every generator type `mu` has length 9 or 10. `J_d` is an equivariant
quotient of a sum of `S_mu V (x) Sym^(d-deg)(Sym^4 V)`. Every constituent of the
second factor is polynomial, and `c^lambda_(mu,nu) > 0` needs `mu ⊆ lambda`,
hence `length(lambda) >= 9`. A quotient acquires no new type. QED.

Scope (as in B17-08/11): this is about the ideal these generators **generate**.
It says nothing about saturation, where division by a factor of many rows can
shorten the type, nor about the full determinant ideal. It also does not cover
the saturated Cayley candidate `J_C` of the supplementary discussion, which has
no explicit equation or type in the tree.

**Lemma 3.2 (PROVED).** Let `P` be any polynomial in the coefficients of forms
that is built from `k x k` minors of the Hessian with `k >= 9`, in any chart
and after any remainder or contraction. That covers the ordinary-divisibility
9-minors, the squared-divisibility 10-determinants and their adjugate
contractions. Then every highest-weight component of `P` of length `<= 8` is zero.

*Proof.* Let `Sub_8` be the closed, GL16-stable, irreducible cone of quartics
with at most eight essential variables. Such a form has Hessian rank at most
eight at every point in every coordinate system, so every `k x k` minor with
`k >= 9` vanishes identically. Remainders modulo a zero polynomial and
contractions of zero are zero. A chart expression lifted by `c^N` vanishes on
`Sub_8 ∩ {c != 0}`, which is dense in `Sub_8`. Hence `P ∈ I(Sub_8)`.
`I(Sub_8)` is GL16-stable, so it contains every isotypic component `P_lambda`.
It contains no nonzero highest-weight vector of length `<= 8`: such a vector
involves only coefficients `c_alpha` supported on the first eight coordinates,
because its weight is zero on the others. It is therefore determined by its
values on `Sym^4` of that coordinate subspace, which lies in `Sub_8`.
A GL-stable space with no highest-weight vector of type lambda has zero
lambda-isotypic part. So `P_lambda = 0` for every `length(lambda) <= 8`. QED.

(Caution recorded for the reviewer: vanishing on one **coordinate** subspace
alone would not suffice for a chart-dependent `P`. The linear function
`c_(4 e_9)` vanishes there and has one-row type `(4)`. The argument needs
vanishing on the whole GL-stable `Sub_8`, which the Hessian rank bound supplies.)

**Reading.** The Hessian-rank-8 geometry is the only source of certified
det4 equations in the tree, and it cannot see lengths 5–8 at all. The rows
where padding is least restricted (5–8: ten essential variables are not yet
binding) are exactly the rows where **no determinant-equation mechanism
exists**. By Lemma 2.1, a gap there needs a new determinant equation of that
row type. In the rows where the known mechanism works (9–10), padding's own
equations and its ten-variable ceiling have closed every assigned family (§1.2).

### 3.2 The empirical record in lengths 5–8

**ADOPTED.** Every length 5–8 cell ever tested for determinant rank was
full rank: B15-02's nine seven-row `a = 1` cells, B15-06's seven/eight-row
tail-21 cells (378, 460), B15-03/04's degree-8 cells. No determinant equation
of length `<= 8` has been observed anywhere in the tree, sampled or certified.
B17-01/03 (ACCEPTED) prove that **some** exactly-five-row determinant equation
separates in **some** degree. B18-01 v1 (unreviewed) proposes the bound
`d <= 4^49` for it.

### 3.3 The padding side by row count

- **Five rows.** `m_pad = rank Phi_(d,lambda)` exactly (B17-08, ACCEPTED). An
  actual padding floor is a modular minor of an explicit product-map
  coefficient matrix, a lower bound in the correct direction. This is the
  cheapest padding certificate in the programme.
- **Six to nine rows.** Five-variable density fails. Restrictions of
  `z*per3` to `l` variables form a family of dimension at most
  `l + 9l - 4 - 1 = 10l - 5` (ten linear forms modulo the 4-dimensional
  row/column torus of `per3` and the scalar moved between `z` and `per3`).
  Generic `l*C` in `l` variables has dimension `l + binom(l+2,3) - 1`, which
  is 39 at `l = 5`. For `l = 5` the family bound 45 exceeds 39, consistent
  with density; for `l = 6` it gives 55 against 61. So for `l >= 6`,
  `U = min(a, T)` built from generic `l*C` is **only a ceiling**, and
  `m_pad = rank Phi` is not available. The actual padding certificate needs
  genuine `per3` restrictions: B17-06's matching normal form, capacity
  `K_d`. (PROVED as a parameter count; the torus dimension is the
  row-by-column scaling with product one.)
- **Ten rows.** The ten-variable support ceiling binds hard: `U/a` is about
  0.67–0.84 in the ten excluded cells.

## 4. The smallest-`s` five-row family is closed by a classical covariant

The five-row cell with the least `b_required` in every census degree is
`lambda = (4d-8, 2,2,2,2)` (§1.4: `s = 8`, `a = U = 1` at d = 5, 6). It is closed
by theory, so no carrier should be built for it.

**Proposition 4.1 (PROVED).** Let `V = C^16`, `f ∈ Sym^4(V*)`, and put
`H(f) = det( d^2 f / dx_i dx_j (e_1) )_(1 <= i,j <= 5)`, the leading 5×5 Hessian
determinant at `e_1`. Then for every `d >= 5` the polynomial
`c^(d-5) H` is a nonzero highest-weight vector of weight `(4d-8, 2^4)`, where
`c = c_(4 e_1)`. It is nonzero on `X_det` and nonzero on `X_pad`. Hence
`m_det >= 1` and `m_pad >= 1`, and in every such degree with `a = 1`:
`m_det = m_pad = 1`, so `D = 0`.

*Proof.*
(i) *Weight.* Under `t = diag(t_i)`, `c_alpha(t^-1 f) = t^alpha c_alpha(f)`. The
restricted Hessian `Hess_5(t^-1 f)(e_1) = T5 Hess_5(f)(t_1 e_1) T5`, with `T5`
the first five `t_i`, and the Hessian is homogeneous of degree 2 in the point.
So `H(t^-1 f) = (t_1...t_5)^2 t_1^10 H(f)`: weight `(12,2,2,2,2)`, coefficient
degree 5. The monomial `c_(4e1) * prod_(j=2..5) c_(2e1+2e_j)` occurs with
nonzero coefficient, so `H != 0`.
(ii) *Highest weight.* Let `u` be upper unitriangular. Then `u e_1 = e_1` and
the first five coordinates span a `u`-stable flag space, so
`Hess_5(u^-1 f)(e_1) = u5^T Hess_5(f)(e_1) u5` with `det u5 = 1`, where `u5` is the
leading 5×5 block. So `H(u^-1 f) = H(f)`. A U-invariant weight vector of
dominant weight is a highest-weight vector in the positive-weight convention.
`c` is one as well, and so is the product.
(iii) *Determinant side.* Let `g = x1 x2 x3 x4 - x5^4 = det(diag(x1,..,x4) + x5 P)`,
with `P` the permutation matrix of a 4-cycle. A permutation mixing diagonal and
`P` entries would need a nonempty proper `P`-stable subset, and there is none. At
`p = (1,1,1,1,1)`, `Hess g(p) = (J_4 - I_4) ⊕ (-12)`, with determinant
`(-3)(-12) = 36`. Choose any invertible `G` whose first column is `p` and put
`g' = g ∘ G`. Then `Hess_5 g'(e_1) = G^T Hess g(p) G`, so `H(g') = 36 det(G)^2 != 0`.
`g'` is a five-variable linear determinantal quartic, hence the restriction of
a point of `GL16 · det4`. Because `H` involves only coefficients supported on
the first five coordinates, `H(g') = H(point of the orbit)`.
(iv) *Padding side.* `C = x1 x2 x3 + x4^3 = per[[x1,x4,0],[0,x2,x4],[x4,0,x3]]`
(the two nonzero matchings are the diagonal and one 3-cycle). `z C` with
`z = x5` lies in `X_pad`, as a limit of all-entries-nonzero substitutions. For a
cubic `C` in `n` variables with Hessian `K`, Euler gives
`det Hess(zC) = -(3/2) z^(n-1) C det K` (identity accepted in B17-11 for n = 9;
the proof is n-independent). At `(1,1,1,1,1)`: `C = 2`, `det K = 6 x4 · 2 x1x2x3 = 12`,
so `det Hess = -36 != 0`. Transport to `e_1` exactly as in (iii).
(v) `c(g') = g'(e_1) = g(p) = 1 - 1 = 0` would kill `c^(d-5) H`. So choose
instead `G` whose first column is a point `p'` near `p` with `g(p') != 0` and
`det Hess g(p') != 0`. Both are nonempty Zariski-open conditions on `p'`, and
the second holds at `p`. Similarly on the padding side, with `zC(p') != 0`.
Then `c^(d-5) H` is nonzero at both points. QED.

`a = 1` for `(12,2^4)` at d = 5, `(16,2^4)` at d = 6 and `(20,2^4)` at d = 7 is
ADOPTED: the Astra census for the first two; for d = 7 the degree-7 screen
considered the shape and found `a < 2`, and Proposition 4.1 gives `a >= 1`.
Multiplication by `c` is injective on highest-weight vectors, so `a` is
nondecreasing in `d`. For `d >= 8` I have not certified `a = 1`; there the
proposition proves only `D <= a - 1`.

**What this closes.** It removes the only five-row cell with single-digit
`b_required` in the measured degrees. It is also a template: an `a = 1` cell is
closed whenever its unique highest-weight vector is a coefficient of a
covariant that is nonzero on some determinantal quartic.

Arithmetic of (iii) and (iv) was rechecked symbolically in a scratch sympy
session (a few seconds; not a mathematical screen). It confirmed
`det(diag(x1..x4) + x5 P) = x1x2x3x4 - x5^4`, `det Hess g(1^5) = 36`,
`per N = x1x2x3 + x4^3`, `det Hess(x5 C)(1^5) = -36`, and the identity
`det Hess(zC) = -(3/2) z^3 C det K` for a random integer cubic in four variables.

## 6. Pilot P1 — declared before execution

**Why a pilot is necessary.** §2 shows that for any cell handed to slots 02/03,
a single determinant full-rank evaluation either closes the cell or exhibits
a sampled determinant kernel. The evaluation costs one highest-weight
construction. A carrier costs the same highest-weight data plus `s` invariant
columns. The next-ranked five-row cells after Proposition 4.1 have `a <= 2`,
weight spaces of 600–2400 monomials (counted, §6.3), and no determinant rank
on disk. Without this check any shortlist of them would rest on an unknown
that one evaluation settles. B15-02 closed nine analogous seven-row cells this
way at the first point.

### 6.1 Exact cells (and nothing else)

All in `GL5` coordinates. `a`, `s`, `U` are from the Astra census (ADOPTED).

| id | d | lambda | a | s | U | b_required | role |
|---|---:|---|---:|---:|---:|---:|---|
| C0 | 5 | (12,2,2,2,2) | 1 | 8 | 1 | 8 | control: must be nonzero and proportional to `H` of Prop. 4.1 |
| C1 | 5 | (9,7,2,1,1) | 1 | 15 | 1 | 15 | second-smallest `b_required`, d = 5 |
| C2 | 6 | (15,3,2,2,2) | 1 | 15 | 1 | 15 | second-smallest, d = 6 |
| C3 | 5 | (7,7,4,1,1) | 1 | 19 | 1 | 19 | third, d = 5 |
| C4 | 6 | (11,9,2,1,1) | 1 | 22 | 1 | 22 | third, d = 6 |
| C5 | 6 | (14,4,2,2,2) | 2 | 45 | 2 | 44 | smallest-weight-space `a = 2` five-row cell (d = 6) |

Excluded, with reasons: (8,7,7,1,1) at d = 6 (weight space 6718, dense kernel
above the memory cap) and (14,2^5) at d = 6 (six rows, weight space 7508).
Both are priced in §6.3 and are NOT REACHED.

### 6.2 Method, range, cap, decision rule

- Weight space: all multisets of `d` exponent vectors in `N^5` of size 4 summing
  to lambda. The highest-weight space is the common kernel of the four simple
  raising derivations `E_(i,i+1)`, ordinary convention above, computed modulo
  `p = 2^31 - 1`. Rows are compressed by a random signed bucket sketch. Since
  `ker_p A ⊆ ker_p(SA)` and `dim ker_p A >= a`, observing
  `dim ker_p(SA) = a` certifies `ker_p A = ker_p(SA)`, equal to the reduction of
  the saturated rational kernel lattice. If the observed dimension differs
  from `a`, the cell is recorded as FAILED/inconsistent and not interpreted.
- Determinant points: `det(sum_k x_k A_k)` with seeded integer 4×4 matrices,
  entries in [-5,5]. A point is used only if the 16×5 column block has rank 5,
  so it is the restriction of an invertible GL16 substitution of `det4`.
- Padding points: `l(x) * per(sum_k x_k N_k)` with seeded integer data, entries
  in [-5,5], all ten linear forms nonzero. Any such 10×5 block completes to an
  invertible 16×16 substitution of independent `z*per3`.
- Three determinant points and three padding points per cell; for C5 an
  `a × a` minor over pairs.
- **Rule.** A nonzero value (or nonzero `a × a` minor) modulo `p` at determinant
  points proves `m_det = a` over Q, and the cell is **CLOSED**
  (`D <= 0`, Lemma 2.1). If every determinant value is zero, record a
  **sampled zero only**. That would make the cell a candidate whose missing
  proof is one global identity; it is not evidence of an equation. Padding
  values are recorded as lower bounds on `m_pad` only.
- Cap: one process at a time, one BLAS thread, `analysis/b15_bound.py
  --seconds 60 --memory-mb 512`, one run per cell, at most six runs. A cap hit
  is recorded as NOT REACHED, not as an exclusion.
- Outputs: `analysis/b18_06_pilot.py`, `results/b18_06/P1_<id>.json`,
  resource receipts `results/logs/b18_06_P1_<id>_resources.json`.

### 6.3 Size counts (pricing only; computed before the pilot)

Weight-space dimensions, counted by exact dynamic programming:
(12,2^4)_5: 553; (9,7,2,1,1)_5: 621; (15,3,2,2,2)_6: 1280; (11,9,2,1,1)_6: 1251;
(14,4,2,2,2)_6: 2337; (16,2^4)_6: 608; (18,4,2,2,2)_7: 2565;
(8,7,7,1,1)_6: 6718; (14,2^5)_6 in six variables: 7508.

### 6.4 P1 results (MEASURED; conclusions PROVED under the stated inputs)

Script `analysis/b18_06_pilot.py`, SHA-256
`4a67b5366baf35e13926167155bbfbdabcc991806eed92592c7947ea3c9e0466`, unchanged
after the runs. Six runs, one per cell, each under the declared wrapper cap.

| id | d | lambda | weight dim | ker_p dim (= a) | det rank floor | pad rank floor | verdict | wall s | peak job MiB |
|---|---:|---|---:|---:|---:|---:|---|---:|---:|
| C0 | 5 | (12,2^4) | 553 | 1 | 1 | 1 | CLOSED, D = 0 | 0.23 | 32 |
| C1 | 5 | (9,7,2,1,1) | 621 | 1 | 1 | 1 | CLOSED, D = 0 | 0.26 | 37 |
| C2 | 6 | (15,3,2,2,2) | 1280 | 1 | 1 | 1 | CLOSED, D = 0 | 1.20 | 99 |
| C3 | 5 | (7,7,4,1,1) | 1564 | 1 | 1 | 1 | CLOSED, D = 0 | 1.79 | 139 |
| C4 | 6 | (11,9,2,1,1) | 1251 | 1 | 1 | 1 | CLOSED, D = 0 | 1.12 | 97 |
| C5 | 6 | (14,4,2,2,2) | 2337 | 2 | 2 (all six 2×2 minors nonzero) | 2 (all six nonzero) | CLOSED, D = 0 | 5.12 | 289 |

No cap was hit; every exit code was 0. Every cell closed at its **first**
determinant point, for `a = 1`, or first pair, for `a = 2`.

**Recorded failure of the first sketch.** In every cell the `n+10`-row random
bucket sketch lost rank: observed nullities 31, 47, 77, 112, 112 and 157
against `a`. The declared retry with `2n` rows gave nullity exactly `a` in all
six. Only the retry is interpreted, per §6.2. The failed nullities are kept in
each JSON as `retry_factor2_previous_nullity`.

**Control C0.** The mod-p kernel vector `F` satisfies `F(pt) / H(pt) = 2028179000`
(mod p) at the five points where `H(pt) != 0`. At the sixth, a padding point
whose linear factor vanishes at `e_1`, both are 0. This checks Proposition 4.1's
highest-weight vector against an independent computation of the same space.

**Why each verdict is a proof.**
(1) `ker_p A ⊆ ker_p SA`, and `dim ker_p A >= dim ker_Q A = a`. So
`dim ker_p SA = a` gives `ker_p A = ker_p SA` of dimension `a`, which is the
reduction of the saturated integral kernel lattice.
(2) A nonzero value (or `a × a` minor) of that reduced basis at integer points
is a nonzero integer multiple of the corresponding rational minor, modulo p.
(3) The determinant points restrict invertible substitutions of `det4`: each
16×5 block was checked to have rank 5 before use. The padding points restrict
invertible substitutions of independent `z*per3`: all ten forms nonzero, and
completion to GL16 is always possible. Hence `m_det >= a`, `m_pad >= a`, and
with `m <= a`, `D = 0`.
Input ADOPTED: `a` from the Astra character census. If that `a` were wrong,
step (1) would fail, and the observed `dim ker_p = a` is consistent with it.

**Reading.** Together with Proposition 4.1, the five five-row cells of least
`b_required` at d = 5, 6 (with `a = U = 1`), and the smallest `a = 2` cell tried,
are all closed with `D = 0`. Each was closed by a computation of at most five
seconds. Building a carrier for any of them would have been wasted work.

## 7. The shortlist

### 7.1 Verdict

**No cell is nominated.** Current evidence names no affordable cell in which a
determinant bound and a padding floor can plausibly meet. This is the honest
empty shortlist the assignment allows. Below are the three best-positioned
**families**, each sized field by field, so that slots 02, 03 and 04 can see
exactly what is missing and do not start on any of them. `unknown` means no
certified or measured value exists in the tree; no entry is estimated.

### 7.2 Table

| field | A: five rows, `U = a` | B: six to eight rows | C: ten rows beyond the ten excluded (e.g. r10, t21) |
|---|---|---|---|
| representative | next unclosed by `b_required`: (8,5,5,1,1)_5, (8,7,3,1,1)_5 [23]; (12,8,2,1,1)_6 [24]; `a = 2`: (8,7,7,1,1)_6 [29] | (14,2^5)_6 [13], then (9,9,2,2,1,1)_6 [53] | stable r10, t21 |
| `a` | census for d <= 6 (e.g. 1, 1, 1, 2 above); two d = 7 cells (2, 3); **unknown** for all other d >= 7 | census for d <= 6 six-row (1, 1); **unknown** for seven/eight rows outside B15's closed ladders | 594 (stable, ADOPTED from B16 HESSIAN_REPORT); finite `a` **unknown** |
| `s` (symmetric, transpose included) | census d <= 6 (23, 23, 24, 30 above); d = 7: 53, 47; **unknown** otherwise | census d <= 6 (13, 53); **unknown** otherwise | **unknown** (B15-12: exceeds `a` in its seven cells) |
| `U = min(a,T)` clipped | equals `a` in the representatives; for five rows `m_pad = rank Phi` exactly (B17-08) | generic-`l*C` ceiling only, not attained (§3.3); actual ceiling **unknown** | **unknown**; in the ten excluded ten-row cells `U/a` = 0.67–0.84 |
| `b` known | **none**, nowhere in the tree | **none** | **none**; known ideal floor `q` for r10, t21 **unknown** |
| `b_required = max(0,s-U+1)` | 23, 23, 24, 29 (of which dead loss `s-a` is 22, 22, 23, 28) | 13, 53 (under-estimates; `U` loose) | **unknown**; the `q`-route equivalent is `a - U + 1`, about 95–200 if `U/a` resembled the excluded cells (arithmetic on a hypothetical, not a claim) |
| available padding evidence | exact product-map formula; P1 shows `m_pad = a` in all six tested cells | none; needs B17-06 matching normal form with capacity `K_d` | none for this cell; tail-19 history: floor 243 against ceiling 288 after large runs |
| necessary determinant input (Lemma 2.1) | at least 1 five-row determinant equation; **none known in any degree**, and Lemmas 3.1/3.2 prove the known mechanisms cannot give one | at least 1 six-to-eight-row equation; none known; same blindness | at least `a - U + 1` equations of that type; the Hessian mechanism gives up to 11 in comparable cells |
| est. cost, Lemma 2.1 evaluation | MEASURED: <= 5.2 s and <= 289 MiB for weight dimension <= 2337 (P1); the dense sketch stores `2n x n` residues (`16 n^2` bytes), so above about n = 5000 a sparse kernel method is needed (unpriced) | as A in six variables, weight dimension 7508 for (14,2^5)_6: **unpriced** (sparse kernel needed) | B15-05-scale: 533-column minors with 560 points; hours-class historically |
| est. cost, carrier (slot 02) | **unknown**; scales with `s` invariant columns times the weight support of `S_lambda W` in adapted coordinates (B17-08 price table); no instance priced | **unknown** | **unknown**, and `s` itself is not computed |
| binding side | **determinant**: no equation exists to certify; boundary route must first certify 22+ dimensions of dead loss | **determinant**, plus a more expensive padding floor | **padding ceiling**: ten essential variables force `U` well below `a` |
| rank by cost | 1 | 2 | 3 |
| rank by proof prospect | 1 of 3, but low: 15/15 tested analogues closed at the first point (six five-row cells in P1, nine seven-row cells in B15-02) | 2 | 3: every assigned ten-row cell has `q + U - a <= -30` |

### 7.3 What would change the verdict

Any one of the following would produce a nomination, each with a small
missing proof:

1. **A certified determinant equation of length 5–8 in any degree.** This is
   slots 01/07's target. Its cell then has `q >= 1`. If also `U = a` there,
   the whole remaining proof is one `a × a` padding minor, which in five rows
   is a product-map minor (§8).
2. **A sampled determinant deficiency** (Lemma 2.1 evaluation of rank `< a`)
   in a five-row cell with `U = a`. The missing proof is then one global
   identity plus the same padding minor. P1 found none; B15-02 found none.
3. **A five-row cell with `s < U`.** Then `b = 0` and `B = s` are free (orbit
   bound, BLMW), and the missing proof is only a padding minor of size `s + 1`.
   No cell with `s < a` exists at d <= 6. B18-01 v1's aggregate argument
   (unreviewed) says that in large degree the orbit ring, of dimension 50,
   outgrows the padding product ring, of dimension 39. This is aggregate
   hostility, not a cell-level exclusion.
4. **A ten-row equation mechanism** yielding on the order of `0.3a` equations
   in one cell. Nothing in the tree approaches this.

**Heuristic control, not a shortcut (conditional, unreviewed here).** If the
closure `D44` of four-variable restrictions of det4 is the linear
determinantal component of Leal–Lozano Huerta–Vite (arXiv:2303.09028), an
irreducible hypersurface of degree 320112, then by B17-03's kernel transfer
**no** determinant equation of length `<= 4` exists below degree 320112. This
proves nothing about five rows. It is recorded only as a caution: the
determinant ideal can be empty in few-row types far beyond any degree a sieve
can reach. That is one more reason not to fund an unrestricted low-degree
five-row sieve (item 2) on hope.

## 8. One next sufficient test, and its price

**Test (conditional on slots 01/07; the smallest proof of a gap the programme
can currently describe).** Given the first certified determinant equation `F`
of highest weight `lambda`, `length(lambda) = 5`, in degree `d`:

1. certify `a` and `T` in that cell by the existing character routines;
2. if `U = min(a,T) = a`, construct the `a`-dimensional highest-weight basis
   (P1 code, unchanged method) and evaluate it at `a` product points `l*C`,
   where `C` is a five-variable restriction of `per3`, as in P1;
3. a nonzero `a × a` minor modulo p proves `m_pad = a`, while `F` gives
   `m_det <= a - 1`. Hence **D >= 1**.

It is sufficient, not necessary. A zero minor is only a failed test, and if
`U < a` one needs `a - U + 1` equations instead.
**Price.** Steps 2–3: MEASURED at <= 5.2 s and <= 289 MiB for weight dimension
<= 2337 and `a <= 2`. Beyond about 5000 a sparse kernel method is required,
unpriced. Step 1: seconds at d <= 7 (B17 degree-7 screen: 12 s for 114
shapes), growing with `p(4d)`. The expensive part is not this test but
producing `F`, which no current mechanism can do (Lemmas 3.1–3.2).

**Unconditional work for slot 06 now: none recommended.** A complete five-row
Lemma-2.1 sieve at d = 7 is possible. Its price is **unknown**: the cell count
and weight dimensions have not been counted, and weight spaces of balanced
shapes exceed the dense-sketch limit. On the evidence of 15/15 closures and
§7.3's heuristic control, its expected yield is low. I do not request it.

**Release gates this implies.** Slots 02/03/04 have no cell to take. If the
integrator nonetheless assigns a cell, run the Lemma 2.1 evaluation in that
cell **first**. It costs seconds and closed all six P1 cells.

## 9. Claim ledger

| # | claim | label |
|---|---|---|
| 1 | Provenance: HEAD `8f7ab3bb…`, tree `f0428d81…` | MEASURED |
| 2 | The ten excluded cells are the four B16 and six B17 tail-`2^8` cells of §1.1 | ADOPTED (identification not printed in the tree) |
| 3 | The degree-7 screen has only two eligible rows of length 5–10 | MEASURED (from its JSON) |
| 4 | No admissible cell with `s` on disk has `s < a`; minimum `b_required` among five-row `U >= 1` cells is 8, then 15 (d = 5, 6) | MEASURED (from census JSON) |
| 5 | `D > 0` implies `i_det >= a - U + 1 >= 1` (Lemma 2.1) | PROVED |
| 6 | The boundary route can pass only if `m_det <= U - 1` (Lemma 2.2) | PROVED |
| 7 | The ideal generated by every certified det4 equation in the tree has no type of length `<= 8` in any degree (Lemma 3.1) | PROVED; generator list ADOPTED; not about saturation or the full ideal |
| 8 | Hessian `k`-minor constructions with `k >= 9` have no length `<= 8` components (Lemma 3.2) | PROVED |
| 9 | For `l >= 6`, `z*per3` restrictions to `l` variables have dimension `<= 10l - 5 < l + binom(l+2,3) - 1`, so generic-product `U` is only a ceiling | PROVED (parameter count) |
| 10 | `c^(d-5) H` is a highest-weight vector of weight `(4d-8,2^4)`, nonzero on both closures; `D = 0` when `a = 1` (Prop. 4.1) | PROVED; `a = 1` at d = 5, 6, 7 ADOPTED |
| 11 | P1: `m_det = m_pad = a` hence `D = 0` in (12,2^4)_5, (9,7,2,1,1)_5, (15,3,2,2,2)_6, (7,7,4,1,1)_5, (11,9,2,1,1)_6, (14,4,2,2,2)_6 | PROVED (modular nonzero minors on actual substitutions); `a` ADOPTED from census |
| 12 | P1's first `n+10`-row sketches lost rank in all six cells | MEASURED failure, recorded |
| 13 | No affordable cell is nominated; three families sized in §7.2 | selection judgement, based on 4–11 |
| 14 | Five-row aggregate hostility (B18-01 v1 Claim 5.1) | NOT REVIEWED here; used only as context |
| 15 | No length `<= 4` determinant equation below degree 320112 | CONDITIONAL on the literature identification; heuristic control only |
| 16 | Existence, degree, or cost of a five-to-eight-row determinant equation | NOT REACHED |
| 17 | Any positive gap | NOT REACHED |

**Honest negatives.**
- Nothing here excludes five- to eight-row gaps in any degree. P1 closes six
  cells; Proposition 4.1 closes one family in degrees where `a = 1`.
- The failure of symmetry-only bounds (`s >= a`) at d <= 7 does not exclude
  boundary losses. It prices them: the dead loss is at least 22 dimensions in
  the best unclosed five-row cells.
- Lemmas 3.1–3.2 are about mechanisms. They do not say the full determinant
  ideal lacks five-row equations; B17-01/03 prove it has some.
- The `b_required` entry for family C in §7.2 is arithmetic on a hypothetical
  ratio, not an estimate of that cell.

## 10. Resources and files

- Pilot P1: six runs of `.venv/python.exe -B analysis/b15_bound.py --slot 06
  --name b18_06_P1_<id> --seconds 60 --memory-mb 512 analysis/b18_06_pilot.py <id>
  results/b18_06/P1_<id>.json`, sequential, one process, one BLAS thread.
  Total wall about 9.7 s; peak job memory 289 MiB (C5). No cap hit.
- Pre-pilot scratch (not research artifacts, outside the worktree): a
  weight-space count (DP, under `timeout 60`) and a sympy recheck of
  Proposition 4.1's arithmetic (under `timeout 60`).
- Written: `docs/b18_06_report.md`, `analysis/b18_06_pilot.py`,
  `results/b18_06/P1_C0.json` … `P1_C5.json`, and receipts
  `results/logs/b18_06_P1_C0_resources.json` … `C5` plus the wrapper's `.pid`
  files. No historical artifact was modified. No git command other than the
  two `rev-parse` calls.
