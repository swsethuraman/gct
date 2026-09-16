# B18-10 — Independent adversarial review of the Slot 01 v1 report

**Worktree start state** (recorded before anything was written, per preamble):

```
git rev-parse HEAD          421493a0c0b09e0aa71724a44e83d324cbb8d1e5
git rev-parse HEAD^{tree}   67f2639ef230ebbde3cbe406c2165cc998887ddc
```

**Object under review:** `Claude_Handover_B15_B18/batch18_launch/b18_01_report_v1.md`
(713 lines), read in full **before** the board's intake section and before any
later revision of that report. The comparison with the board's intake is in §6,
written only after §§1–5 were on disk.

## 0. Plain terms

The v1 report claims three things: (1) a proved finite degree bound `d <= 4^49` for a
five-row determinant equation that separates padding; (2) that making the ruledness
argument effective is the wrong target; (3) a "structural warning" that five-row
cells are the wrong place to look for a positive gap `D > 0`, backed by an aggregate
Hilbert-function inequality (Claim 5.1) and the exact dimensions `dim D45 = 50`,
`dim R135 = 39`.

My method: every claim gets a decision — **ACCEPTED**, **REJECTED**, or
**CONDITIONAL** (accepted only with a stated correction or hypothesis). I replay the
decisive small certificates myself (the Jacobian rank behind `dim D45 = 50`, the
stabiliser dimension behind Lemma C, `dim R135 = 39`, the arithmetic of `4^49`), I
check the direction of every rank-to-dimension inference, I check conventions
(ordinary coefficients; ordinary vs symmetric rectangular Kronecker; clipped vs
unclipped ceilings), and I try cheap witnesses against every stated criterion.

What I am going to do, in order: §1 replay the certificates; §2 decide the geometric
and degree-bound claims (Sections 1–4 of the report); §3 decide the aggregate claim
5.1 and, separately, every sentence that draws a cell-level or regime-level
implication from it; §4 decide the ceilings and the "missing theorems" section;
§5 the ledger of decisions; §6 comparison with the board's intake; §7 the release-gate
position for slots 03, 04, 09.

## 1. Independent replay of the decisive certificates (MEASURED here)

All runs: one `python3` process each, `python-flint 0.9.0` + `sympy 1.14`, pure
integer / rational arithmetic, each well under one second. Scripts kept in the session
scratchpad (`replay_d45.py`, `replay_r135.py`); the inputs are fully specified below
so they can be re-run from this text alone.

### 1.1 The Jacobian rank behind `dim D45 = 50`

Map `phi : (Mat_4)^5 -> Sym^4(C^5)^*`, `phi(B) = det(sum_k x_k B_k)`. Row `(k,i,j)` of
the `80 x 70` Jacobian is `[x^alpha](x_k * cofactor_ij(M))`, `M = sum_k x_k B_k`. I
built this matrix myself from `d det = tr(adj(M) dM)` (not from the report's
description) at the report's fixed point `B0..B4` (report §4) and at one independent
random integer point (seed 20260915, entries in `[-9,9]`).

| point | rank mod 2147483647 | rank mod 1000003 | **exact rank over Q** |
|---|---|---|---|
| report's `B0..B4` | 50 | 50 | **50** |
| independent random point | 50 | (not run) | **50** |

Controls replayed: `M * adj(M) = det(M) * I` as a polynomial identity; the Euler
identity `sum_{k,i,j} (B_k)_ij x_k cof_ij(M) = 4 det M` (checks every Jacobian entry
against `det M`); `det M` has all 70 monomials; a deliberately sign-flipped cofactor
breaks the Euler identity. All pass.

**Direction of inference, checked.** `rank_p <= rank_Q <= max_B rank(d phi_B) =
dim closure(im phi)` (characteristic zero). So rank 50 at a point is a **lower**
bound `dim D45 >= 50`. The report uses it only as a lower bound (its §4 says so in
so many words) and gets the upper bound from Lemma C. That is the right direction.
I additionally computed the exact rational rank, so the modular step is not even
needed: `dim D45 >= 50` is now PROVED over `Q` by an exhibited integer point.

### 1.2 The generic stabiliser behind Lemma C (`dim D45 <= 50`)

At the report's point I solved the linear system `p B_k + B_k q = 0` (`k = 0..4`) for
`(p, q) in gl_4 x gl_4`: 80 equations, 32 unknowns. **Nullity = 1** (the line
`p = cI, q = -cI`), so the Lie algebra of the stabiliser of this point in
`{(P,Q) : det P det Q = 1}` (dimension 31) is one-dimensional and the orbit through it
has dimension 30. Independently, the Jacobian kernel at the same point has dimension
`80 - 50 = 30`. The two numbers agree, which is exactly the statement that at this
point the fibre of `phi` is (locally) the group orbit. Lemma C's argument is a
generic-stabiliser argument; the point check confirms it at an explicit point, and
since stabiliser dimension is upper-semicontinuous the generic value is `<= 1`,
hence `= 1`. **Lemma C ACCEPTED**, and with 1.1, **Claim 4.1 (`dim D45 = 50`,
`dim P(D45) = 49`) ACCEPTED.**

### 1.3 `dim R135 = 39`

Jacobian of `(l, C) -> l*C` at a random integer point: `40 x 70`, exact rank over `Q`
**= 39**. Lower bound 39. Upper bound 39 from the report's UFD fibre argument
(fibre of a reduced `lC` with `C` irreducible is the `C^*`-line `(tl, t^{-1}C)`),
which I checked and which is elementary. **Claim 4.2 ACCEPTED.**

### 1.4 Arithmetic

`4^49 = 2^98 = 316912650057057350374175801344`, about `3.17e29`. Matches the report.

### 1.5 The Weyl ratio used in Claim 5.1

`dim S_lambda(C^5) / dim S_lambda(C^4) = prod_{i=1..4} (lambda_i + 5 - i)/(5 - i)`
for `lambda_5 = 0`: verified against the Weyl dimension formula on six shapes; the
bound `<= (4d+4)^4 / 24` holds on each. Elementary; ACCEPTED.

## 2. The geometry and the degree bound (report §§1-4): decisions

**Claim 1.1 (Zariski = Euclidean closure on constructible sets). ACCEPTED.**
Standard (Mumford, Red Book I.10 Cor. 1 is the right pointer). Proof as written is
correct.

**Claim 1.2 (`D45` is a Zariski-closed cone equal to both closures; `R135` is
Zariski closed). ACCEPTED.** `R135` is the affine cone (with vertex) over the image of
the projective morphism `P^4 x P^34 -> P^69`; the multiplication map has no base
points because `l C` is nonzero whenever both factors are. Correct.

**Claim 1.3. ACCEPTED** (follows from 1.1-1.2 plus accepted B17-01-A dominance).

**Claim 1.4 (ADOPTED from B17-03 Lemmas 1-2). ACCEPTED as adopted.** I read B17-03's
Lemmas 1 and 2 in `B15-03/docs/b17_03_report.md` and B17-11's acceptance 03-A. The
v1 report describes them accurately, and the re-derivation sketch (positive weights
force support on the first `r` variables; raising operators with `j > r` vanish by
the `alpha_j = 0` case) is the same proof. Convention: ordinary coefficients, raising
`E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)`; the report states this once and
never uses any factorial-normalised symbol. No convention drift found anywhere in
the report; it never performs a raising computation, so there was little room for
one.

**Claim 2.1. ACCEPTED.** Trivial from `F*` outside `D45` (B17-11 accepts 01-C) and
closedness.

**Claim 2.2 (some `lambda` with `ell(lambda) = 5` exactly). ACCEPTED.** The
submodule-containment-on-highest-weight-spaces argument is correct (a submodule of a
completely reducible module is generated by its highest-weight vectors, and its
weight-`lambda` highest-weight vectors are its intersection with `H_lambda`). The
exclusion of `ell <= 4` is B17-11's accepted 03-C, used in the right direction.

**Claim 2.3 (no sign for `D` follows). ACCEPTED**, and this is the most important
correct sentence in the report. The two-lines-in-a-plane example is a genuine
counterexample to any promotion from "`K_det` not inside `K_pad`" to `D > 0`.

**Claim 2.4. ACCEPTED** (trivial).

**Lemma A (separate a point from `Y` in degree `<= deg Y`). ACCEPTED.** I checked the
proof step by step, including the edge case `k = m - 1` (then `Lambda'` is empty,
`Lambda = {p}`, `L` is empty, and the projection is the identity; the argument
degenerates correctly). The key identity `deg(pi_L(Y)) * deg(Y -> pi_L(Y)) = deg Y`
for a projection from a linear space disjoint from `Y` is standard. The
reducible-case product is fine but unused: `P(D45)` is irreducible.

**Lemma B (`deg Y <= D^{dim Y}` for the image closure of a map by degree-`D`
forms). ACCEPTED, with the refined-Bezout citation checked as far as I can.** The
proof is correct: general hyperplane sections of `Y` pick `deg Y` general image
points; each pulls back to an `(n-k)`-dimensional component of the intersection of
`k` degree-`D` hypersurfaces; distinct points give distinct components; refined
Bezout (sum of degrees of irreducible components `<=` product of the degrees) closes
it. The theorem cited is real and is correctly stated. Pointer check: the inequality
is Fulton, *Intersection Theory*, **Example 8.4.6** (the most commonly cited
location) and the refined version is **Theorem 12.3**; the report's "Example 12.3.1"
is in the right section but I would cite Ex. 8.4.6 / Thm 12.3. This is a pointer
correction, not a mathematical one. The report's own hypothesis flag (only the
component-sum form is used) is right.

**Lemma C. ACCEPTED** (§1.2 above).

**Theorem E (`d <= 4^49`): do the three ingredients compose? Yes. ACCEPTED.**
I checked the interfaces explicitly:

- Lemma B's `Y` is the closure of the image of `psi : P^79 --> P^69` given by the 70
  coefficient forms of degree 4 in the 80 matrix entries, that is `P(D45)` as a
  *reduced* projective variety, irreducible. Lemma A takes exactly a reduced closed
  `Y` and its degree as a reduced variety. Same object, same degree.
- Lemma C bounds the exponent `k = dim P(D45) <= 49`; the pilot is **not** needed
  for Theorem E, only for the sharpness remark.
- The separated point `[F*]` in `P^69` is well defined (`F*` nonzero) and lies
  outside `P(D45)` by B17-01-C.
- The pulled-back form `h = rho_5^* bar h` is a **global** polynomial on the ambient
  `Sym^4(C^16)^*` (a polynomial in the coefficients supported on five variables),
  vanishes on all of `X_det` because `rho_5(X_det)` lies in `D45`, and is nonzero at
  the ambient padding point `F*'` with `rho_5(F*') = F*` (B17-01's frame
  certificate). Global polynomiality and closure validity are both fine.
- Claim 2.2 then supplies `ell(lambda) = 5` in degree `d = deg bar h`.

So the statement "there is a five-row highest-weight determinant equation of degree
`d <= 4^49` that does not vanish on `X_pad`" is PROVED, modulo the standard citation.

**Two calibration remarks on Theorem E that the report does not make (my
additions, MEASURED/ADOPTED).**

1. The bound is not merely "astronomically weak"; the route is loose at *both*
   steps, and the four-variable control quantifies it. For `D44` (4x4 linear
   determinantal quartic surfaces), Lemma B gives `deg <= 4^34`, about `2.9e20`. The
   actual degrees of the components of the determinantal-quartic-surface divisor are
   computed in Leal, Lozano Huerta, Vite, arXiv:2303.09028 (v3, Nov 2024; I fetched
   the abstract): `320, 2508, 136512, 38475, 320112`. So refined Bezout overshoots
   the true degree by roughly **fifteen orders of magnitude** in the control. The
   v1 report says of this degree "even that degree I could not source"; the source
   is the paper the preamble already names.
2. Lemma A's `d <= deg Y` is itself only a set-theoretic cut-out bound; nothing says
   the *first* separating degree is anywhere near `deg P(D45)`. So the report's
   framing, "the only quantity standing between this and a usable bound is
   `deg P(D45)`" (§3.5) and "the effectivity obstruction is ... the degree of the
   determinant pencil variety" (plain terms (1)), is **REJECTED as an implication**
   while Theorem E itself is ACCEPTED. The obstruction is the absence of *any*
   handle on `I(D45)` (generators, regularity, or one explicit equation), which the
   report's own §7.1 (a)-(c) list correctly; the plain-terms summary collapses that
   list to one number, and the control shows that number would not rescue the bound
   anyway. Hypothesis flag: whether 320112 is the specific component consisting of
   4x4 *linear* determinantal quartics I did not verify; the calibration holds
   whichever of the five it is.

## 3. The aggregate claim 5.1, and every implication the report draws from it

### 3.1 Claim 5.1 as stated: ACCEPTED

Statement: there is `d_0` such that for all `d >= d_0`,
`S_5(d) := sum_{lambda ⊢ 4d, ell(lambda) = 5} dim S_lambda(C^5) * D(d,lambda) < 0`.

I re-derived it. The identity
`sum_{ell <= 5} dim S_lambda(C^5) * D(d,lambda) = dim I(D45)_d - dim I(R135)_d = h_R135(d) - h_D45(d)`
is exact (both ideals are `GL5`-stable homogeneous ideals in `Sym(Sym^4 C^5)`;
`D(d,lambda) = i_det - i_pad` and `i_X^16 = i_X^5` for `ell <= 5` by Claim 1.4).
`h_D45` is the Hilbert function of the reduced 49-dimensional `P(D45)`, so it is
eventually a polynomial of degree 49 with leading coefficient `deg P(D45)/49! > 0`;
`h_R135` has degree 38. The length-`<= 4` correction is bounded by
`sum_{ell<=4} a(d,lambda) dim S_lambda(C^5) <= ((4d+4)^4/24) * binom(34+d, 34) = O(d^38)`;
each step (|D| <= a; `a` for `ell <= 4` equals the four-variable multiplicity; the
sum over `ell <= 4` of `a * dim S_lambda(C^4)` is `binom(34+d,34)`; the Weyl ratio,
§1.5) checks. So `S_5(d) ~ -(deg P(D45)/49!) d^49 < 0` eventually. **PROVED, and it
needs exactly `dim P(D45) > 38`, which §1 supplies. `d_0` is not effective.** The
report labels it "aggregate only" and says in §5 that individual cells are not
controlled. That labelling is correct.

### 3.2 What Claim 5.1 does not license: the implications, one by one

The board's stated reason for this slot is that correct results and false
implications coexist in the document. Claim 5.1 is where they coexist. The report
keeps the *statement* aggregate but does not keep the *use* aggregate. Decisions:

**(a) "The length-five cells ... are structurally the wrong place to look for
`D > 0`" (plain terms (3)). REJECTED.** A negative weighted sum over a family of
cells says nothing about the sign of any member. The report says this itself in §5
("individual cells with `D > 0` are not excluded") and then asserts the cell-level
recommendation anyway in the summary a reader will actually read.

**(b) "Five rows is where separation begins and, on the aggregate, where `D` is
most negative" (§7.2, triage (a)). REJECTED.** "Most negative" is a comparison
between regimes. No other regime's aggregate is computed or bounded anywhere in the
report, so the superlative has no support. Worse, the comparison goes the other way
in the only sense one can make precise: see (d).

**(c) "That pushes any serious `D > 0` hunt into `6 <= ell(lambda) <= 10`, where the
padding restriction ... restricted dimension can approach that of the determinant
side" (§5, Consequence for the board). REJECTED.** Two reasons.

  First, the aggregate-negativity argument is not specific to five rows. It runs
  verbatim at every length: for each `r`, the `ell <= r` aggregate equals
  `h_{P_r}(d) - h_{D4r}(d)`, and the determinant side is the larger variety at every
  `r`. I measured the two sides (MEASURED here: one `python3` process, exact
  Jacobian ranks over `Q` at a random integer point, all six lengths in one run of
  a few seconds; lower bounds, and for the determinant side they meet the
  stabiliser upper bound `16r - 30`):

  | `r` | `dim D4r` (det side) | `dim P_r` (padding side, `>=`) | gap |
  |---|---|---|---|
  | 5 | 50 | 39 | 11 |
  | 6 | 66 | 55 | 11 |
  | 7 | 82 | 65 | 17 |
  | 8 | 98 | 75 | 23 |
  | 9 | 114 | 85 | 29 |
  | 10 | 130 | 95 | 35 |
  | 16 (ambient) | 226 | 155 | 71 |

  (Ambient values: `256 - dim Stab(det4) = 256 - 30`; `256 - dim Stab(z per3) =
  256 - 101`, where the stabiliser of `z per3` in `GL16` is the 5-dimensional
  stabiliser of `z per3` inside `GL10` times the 96 free entries of the six unused
  rows. These two I derived by hand and did not machine-check; they are not needed
  for the ruling, the `r <= 10` rows suffice.) The padding side does not "approach"
  the determinant side as the length grows; the dimension gap widens monotonically
  from 11 to 35. So the one property Claim 5.1 rests on, "determinant side bigger",
  holds at every length, and if it were a reason to leave five rows it would be a
  reason to leave every length. It is not a reason to do either.

  Second, the positive-`D` question is a cell question, and the cellwise information
  the programme actually has at five rows (Theorem E: some five-row cell carries a
  determinant equation padding does not satisfy) is *more* than it has at any other
  length. The recommendation inverts the evidence.

**(d) "Claim 5.1 proves that ... five rows is ... on the aggregate where `D` is most
negative" read as "the five-row aggregate is more negative than the `ell <= 4`
aggregate". CONDITIONAL, and pointless.** It is true that `S_5(d)` dominates
`S_{<=4}(d)` in order of growth (`d^49` against `d^38`) — that is the content of the
proof. But `S_{<=4}(d) <= 0` cellwise by B17-03, so the four-row regime is
"negative" in the strongest possible sense and the five-row regime only in the
weakest. If "most negative" is meant in growth order, say so; it then says nothing
about cells. If it is meant about cells, it is false as a deduction.

**(e) "This slot supplies evidence against [a positive five-row gap] in this
regime" (§7.2). REJECTED as evidence.** A statement that is implied by
`dim D45 > dim R135` alone, and that holds equally at every length, carries no
information about the existence of a positive cell at five rows. Evidence would be a
cell-level bound, e.g. `m_pad <= m_det` in a named cell, or `U <= B` across a named
range of cells. None is given.

**(f) The forbidden heuristic.** The report says (§5, last bullet) that Claim 5.1 is
not the "dim source vs dim target" heuristic. As a *theorem* it is not. As the
*recommendation* in (a), (c), (e) it is exactly that heuristic, since the theorem's
only input beyond bookkeeping is `50 > 39`. The preamble's rule "a positive upper
bound proves nothing" has a mirror image the report trips over: a negative
aggregate proves nothing about a cell.

### 3.3 What survives from Section 5

- Claim 5.1: PROVED (aggregate, non-effective `d_0`).
- The observation that within `ell <= 5` the programme has "`<= 4` proved
  non-positive; `= 5` proved separating": ACCEPTED (it is B17-03 plus Theorem E).
- Every sentence that turns Claim 5.1 into advice about where to look: REJECTED.
  The integrator should strike plain-terms (3) and the "Consequence for the board"
  paragraph, and the "(a) genuinely open, and this slot supplies evidence against
  it" sentence in §7.2, before anything downstream cites this report.

## 4. The ceilings, the screen, the rejected criterion, and the missing theorems (report §§6-7, 9)

### 4.1 Claim 6.1, `m_det(d,lambda) <= g((d^4),(d^4),lambda)`: CONDITIONAL

The argument is sound: `phi^*` is `GL5`-equivariant with kernel `I(D45)_d`, its
image lies in the `SL4 x SL4`-invariants of `Sym^{4d}(C^4 ⊗ C^4 ⊗ C^5)`, and the
Cauchy-Kronecker decomposition puts the `S_lambda(C^5)`-multiplicity of those
invariants at `g((d^4),(d^4),lambda)` because the only `SL4`-invariant `S_mu(C^4)`
with `mu ⊢ 4d` is the rectangle. Direction: an upper bound on `m_det`, i.e. on the
coordinate multiplicity, obtained from a source ceiling; that is the correct
direction (image of a map has multiplicity at most the target's). Dual-vs-nondual
bookkeeping does not affect the number because Kronecker coefficients are invariant
under dualising all three factors together.

The condition: the ledger row says "= B17-02's `s`". It is not. B17-02 (line 13 and
42 of `B15-02/docs/b17_02_report.md`) defines `s` as the **symmetric** rectangular
Kronecker coefficient, transposition included; the preamble requires that this be
said every time. Claim 6.1 as displayed is the **ordinary** rectangular Kronecker
coefficient, which is `>= s`. The parenthetical after the proof does say the
transposition refines it to `s`. So: the inequality is PROVED; the identification
with `s` holds only for the refined form; the ledger row must read
"`m_det <= s <= g`, with `g` ordinary". A downstream session that transcribes `B = g`
from the ledger will use a weaker `B` than the programme's `s` and may miss a
`U > B` cell; one that transcribes `B = s` from the ledger without the transposition
step has an unproved bound. Both are avoidable by the one-line correction.

### 4.2 Claim 6.2, `m_pad <= U := sum_{lambda/nu horizontal d-strip} mult(S_nu, Sym^d(Sym^3 C^5))`: CONDITIONAL

The Pieri argument is correct and the direction is correct (again image `<=`
target). But the quantity displayed is the **unclipped** target multiplicity, which
the preamble calls `T` and B17-08 (equation (3) of `B15-08/docs/b17_08_report.md`)
calls `T`, with `U = min(a, T)`. The report names it `U` and the ledger says
"= B17-08's product ceiling". The preamble says: "Do not quote an unclipped `T`."
The mathematics is right; the label is the programme's reserved symbol for a
different number. Correction: rename to `T`, and set `U = min(a, T)`.

This is not cosmetic for §9 (below): the screen `U > B` with `U` unclipped and
`B = g` unclipped can fire in a cell where `min(a,T) <= min(a, s)`, i.e. produce a
false candidate.

### 4.3 Claim 6.3, the screen: ACCEPTED, with the same relabelling

"An actual padding rank `r` satisfies `r <= m_pad <= U`, so `r > B` needs `U > B`" is
correct, and the report's own caution (a failed screen retires the cell for this
certificate route only and does **not** prove `D <= 0`) is exactly right. This is
the one place in §§5-7 where the report correctly refuses to promote an upper bound
to a sign. ACCEPTED as a necessary condition, once `U` means `min(a,T)` and `B`
means `min(a, s - b)`.

### 4.4 The `MN = F·I4` criterion (§6.1, second bullet): REJECTED

The report writes: "`F` in `D45` (for reduced `F`) iff there are a linear `M` and a
cubic `N`, both `4x4`, with `MN = F·I4`." Witness: `F = lC` with `l` linear and `C` an
irreducible cubic is reduced; `M = l·I4`, `N = C·I4` gives `MN = lC·I4`; but by
B17-01-C (accepted) `lC` is **not** in `D45` when `C` is a smooth cubic threefold.
So the criterion has false positives and cannot characterise membership. The
report calls it "a correct reformulation"; it is not.

Disclosure: the preamble I was given lists this criterion as already rejected with
this witness, so I did not find it cold. What I add is the diagnosis of *why* it
fails, which matters for any repair: `MN = F·I4` forces only `det M · det N = F^4`,
and unique factorisation then allows `det M` to be any quartic whose fourth power
divides `F^4` with the right cofactor, e.g. `l^4`. The intended condition is
`det M = F` (then `N = adj M` is forced and the identity is automatic). An incidence
construction must impose `det M = F` itself, and a closure-correct one must handle
the limits in which no finite `M` exists (B17-01 shows such limits are in `D45`).
Nothing else in the report depends on this bullet; it is inside a NOT REACHED
section.

I looked for further witnesses of this shape against every stated criterion in the
report (Lemma A's disjointness, Lemma B's fibre-dimension step, Claim 2.2's
isotypic reduction, Claim 4.2's fibre, Claim 6.3's necessity) and found none: each
of those is a genuine equivalence or a correctly one-directional inequality.

### 4.5 The Hessian remark (§6.1, first bullet): ACCEPTED as a mechanism statement

"`det4` has Hessian rank at most 8 on its own hypersurface" is correct: at a corank-1
matrix, WLOG `diag(1,1,1,0)`, the second-order term of `det(A + tE)` is
`E_44 (E_11 + E_22 + E_33) - sum_{i<4} E_i4 E_4i`, a quadratic form of rank
`2 + 2·3 = 8`. (General `n`: rank `2n`.) The five-variable pullback has Hessian
`L^T H L` with `L : C^5 -> C^16`, rank `<= min(5, 8) = 5`, so no forced drop; the
report's conclusion that the B15 mechanism does not transfer is right. This is a
NOT REACHED item and I have no objection to how it is recorded.

### 4.6 Section 7, the "missing theorems": decisions

**Proposition M1 (effectiveness) framing: ACCEPTED; its bullet "(a) genuinely open:
a usable bound … `deg P(D45)` is … uncomputed": CONDITIONAL.** The list (i)-(iii) of
what would replace `4^49` is correct and complete enough (a regularity bound, a
degree bound, or explicit low-degree equations missing `F*`). But per §2 the
four-variable control shows that route (i) is not the binding one: even the exact
degree, fed through Lemma A, gives a set-theoretic cut-out bound, not a first
separating degree. The report should not present `deg P(D45)` as "the" obstruction.

**7.1 (c), "the ruledness argument cannot yield a degree bound": ACCEPTED as an
assessment, labelled ASSESSED by the report, which is the right label.** The
argument (birational invariants of the special fibre carry no coefficient-degree
information) is persuasive for the *specific* chain Matsusaka-then-Clemens-Griffiths.
It does not exclude that some *other* geometric property of every member of `D45`
(every member is singular, for instance, though the discriminant does not separate
`lC`) has a polynomial certificate of known degree. The report's sentence "the
degree must come from the determinant side" is an opinion; the weaker "the degree
does not come from the ruledness chain" is what is argued. CONDITIONAL on that
weakening.

**Proposition M2 (positive five-row gap): the statement and "what is proved":
ACCEPTED.** Correctly says Theorem E orders nothing.

**"These are the same statement; (2) is the operational form" (M2, forms 1 and 2):
REJECTED.** Form (1), `K_pad ⊆ K_det` and `K_det ⊄ K_pad`, gives `D >= 1`. Form (2),
a certified `B >= m_det` and an actual padding rank `r >= B + 1`, gives `D >= 1`.
Each is sufficient. Neither implies the other: `i_det > i_pad` does not give
`K_pad ⊆ K_det` (two subspaces of different dimension need not nest), and form (1)
supplies no certified `B`. Two sufficient conditions for the same conclusion are not
the same statement. The correction is one word: "equivalent" to "both sufficient".

**M2 triage (a) "evidence against": REJECTED (§3.2(e)).** **(b), (c): ACCEPTED.**

**§7.3 "both missing theorems reduce to facts about the single variety `D45`":
CONDITIONAL.** M1 does. M2 does not: a positive gap needs a **lower** bound on
`m_pad`, which is a fact about `R135` (an actual padding minor), not about `D45`.
The sentence as written points the next worker at the wrong variety for half the
problem.

### 4.7 Section 9, the next test: CONDITIONAL

The proposed screen (compute `a`, `B`, `U` on every five-row cell for `d <= 5` and
report `U > B`) is the right kind of test and is cheap. Conditions for it to be
usable, all from §§4.1-4.2:

1. `B` must be `min(a, s)` with `s` the **symmetric** rectangular Kronecker
   coefficient (or `min(a, s - b)` if a certified `b` exists). The report's §9 text
   does say `g_sym`; its ledger says `g`. Use `s`.
2. `U` must be `min(a, T)`, not `T`.
3. A cell passing the screen is headroom, not a candidate (the report says this;
   keep it).
4. The claimed price ("well under 60 s / 512 MiB for `d <= 5`") is unverified. The
   binding cost is symmetric rectangular Kronecker coefficients at `|lambda| = 20`,
   which by character methods needs `S_20` character values on a few hundred
   shapes; plausible within the cap but not obviously so. Price it by running
   `d <= 3` first under the cap and extrapolating, rather than asserting.

Also: the report's expectation ("the screen never fires ... which, given Claim 5.1,
is the outcome I expect") is again Claim 5.1 used cellwise. Strike the "given
Claim 5.1". The screen's outcome is an open empirical question at every length.

## 5. Ledger: decision on every claim of the v1 report

Transcribable form. "ACCEPTED" = the displayed claim survives with its label.
"CONDITIONAL" = survives only with the stated correction. "REJECTED" = does not
follow from the evidence given. Column "Indep." records whether I reached the
decision before reading any other opinion of the report (yes for every row; the
one exception is disclosed in 4.4).

| Report item | Claim (as the report states it) | Decision | Correction / reason |
|---|---|---|---|
| 1.1 | Zariski = Euclidean closure on constructible sets | **ACCEPTED** | standard; proof correct |
| 1.2 | `D45` closed cone, both closures agree; `R135` Zariski closed | **ACCEPTED** | — |
| 1.3 | "dense among five-variable cubics" unambiguous; `D_pad,5 = R135` | **ACCEPTED** | uses accepted 01-A |
| 1.4 | B17-03 Lemmas 1-2 (restriction / kernel identification) | **ACCEPTED (ADOPTED)** | checked against `b17_03_report.md`; ordinary-coefficient convention consistent throughout |
| 2.1 | some `d` with `I(D45)_d ⊄ I(R135)_d` | **ACCEPTED** | — |
| 2.2 | such `d` has `lambda ⊢ 4d`, `ell = 5`, `K_det ⊄ K_pad` | **ACCEPTED** | isotypic reduction correct; `ell <= 4` excluded by accepted 03-C |
| 2.3 | no order between `i_det`, `i_pad` follows; `D` unsigned | **ACCEPTED** | correct and load-bearing |
| 2.4 | if also `K_pad ⊆ K_det` then `D >= 1` | **ACCEPTED** | trivial |
| Lemma A | point separated from `Y` in degree `<= deg Y` | **ACCEPTED** | proof checked incl. hypersurface edge case |
| Lemma B | `deg(image closure) <= D^{dim}` | **ACCEPTED** | refined Bezout: cite Fulton Ex. 8.4.6 / Thm 12.3 (pointer fix only) |
| Lemma C | `dim D45 <= 50` | **ACCEPTED** | stabiliser nullity 1 replayed at explicit point (§1.2) |
| Thm E | five-row separating equation exists in degree `d <= 4^49` | **ACCEPTED (PROVED mod citation)** | ingredients compose (§2); arithmetic checked |
| §3.5 / plain (1) | "the only quantity standing between this and a usable bound is `deg P(D45)`" | **REJECTED as implication** | Lemma A is a set-theoretic cut-out bound; 4-variable control (LLV 2303.09028) shows refined Bezout overshoots true degree by ~15 orders; obstruction is any handle on `I(D45)` |
| 4.1 | `dim D45 = 50`, `dim P(D45) = 49` | **ACCEPTED (PROVED)** | replayed: exact rank 50 over `Q` at report's point and at an independent point; direction (rank at a point is a lower bound) used correctly by the report |
| 4.2 | `dim R135 = 39` | **ACCEPTED (PROVED)** | replayed: exact Jacobian rank 39; UFD upper bound checked |
| pilot receipt | scripts at `out/b18_01_pilot.py`, `out/b18_01_control.py` | **CONDITIONAL** | no such files exist in the B15-01 worktree (`out/` absent); the numbers are nevertheless independently reproduced here, so nothing depends on the missing scripts |
| 5.1 | `sum_{ell=5} dim S_lambda(C^5) D(d,lambda) < 0` for `d >= d_0` | **ACCEPTED (PROVED, aggregate, `d_0` non-effective)** | re-derived; needs `dim P(D45) > 38`, supplied |
| plain (3) | five-row cells "structurally the wrong place to look for `D > 0`" | **REJECTED** | aggregate-to-cell inference; §3.2(a) |
| §5 consequence | "pushes any serious `D > 0` hunt into `6 <= ell <= 10`"; padding dimension "can approach" determinant side there | **REJECTED** | same argument at every length; measured gap widens 11 -> 35 from `r = 5` to `10` (§3.2(c)) |
| §7.2 (a) | "evidence against" a positive five-row gap; "where `D` is most negative" | **REJECTED** | no cross-regime comparison exists; implied by `50 > 39` alone (§3.2(b),(e)) |
| 6.1 | `m_det <= g((d^4),(d^4),lambda)` | **CONDITIONAL** | inequality PROVED with `g` **ordinary**; ledger's "= B17-02's `s`" holds only after the transposition refinement: `m_det <= s <= g` |
| 6.2 | `m_pad <= U := (Pieri sum)` | **CONDITIONAL** | quantity is the unclipped `T` of B17-08; rename `T`, set `U = min(a,T)` (preamble: never quote unclipped `T`) |
| 6.3 | standard certificate needs `U > B` | **ACCEPTED** | necessary-only; report's caution correct; with `U = min(a,T)`, `B = min(a, s-b)` |
| §6.1 bullet 2 | "`F ∈ D45` (reduced `F`) iff `∃` linear `M`, cubic `N`: `MN = F·I4`", "a correct reformulation" | **REJECTED** | witness `M = l·I4`, `N = C·I4` with `lC ∉ D45` (accepted 01-C); mechanism in §4.4 |
| §6.1 bullet 1 | Hessian-divisibility mechanism does not transfer (`det4` Hessian rank `<= 8` on hypersurface) | **ACCEPTED** | rank-8 claim verified by hand |
| 7.1 M1 list (i)-(iii) | what would replace `4^49` | **ACCEPTED** | — |
| 7.1 (a) | usable bound genuinely open; `deg P(D45)` uncomputed | **CONDITIONAL** | true, but not "the" obstruction (see §3.5 row) |
| 7.1 (c) | ruledness argument cannot yield a degree bound | **CONDITIONAL (ASSESSED)** | argued for the specific chain; "must come from determinant side" is opinion |
| 7.2 M2 statement, "what is proved", forms (1),(2) each sufficient | | **ACCEPTED** | — |
| 7.2 "these are the same statement" | forms (1) and (2) equivalent | **REJECTED** | two sufficient conditions, neither implies the other (§4.6) |
| 7.3 | both missing theorems reduce to facts about `D45` | **CONDITIONAL** | M1 yes; M2 needs a lower bound on `m_pad`, a fact about `R135` |
| §9 test | screen `U > B`, `d <= 5`, five-row cells | **CONDITIONAL** | use `min(a,T)` and symmetric `s`; price unverified; strike "given Claim 5.1" |
| honest negatives 1-6 | | **ACCEPTED** | all six are correct as written; negative 3 contradicts plain (3) and should win |
| Conventions section | ordinary coefficients, stated raising rule, no factorial symbols | **ACCEPTED** | verified: no raising computation is performed, no drift possible |
| Global polynomiality / closure validity of `h = rho_5^* bar h` | | **ACCEPTED** | §2, Theorem E interface check |
| Actual lower minors | none claimed | **n/a** | the report correctly claims no `r` anywhere |

**Summary of what survives.** Sections 1-4 of the report survive essentially
intact: the closure audit, the "separation but no sign" analysis (2.3), Lemma
A/B/C, Theorem E with `4^49`, and both exact dimensions. Claim 5.1 survives as
stated. Claims 6.1-6.3 survive after two symbol corrections. What does not survive
is every sentence that converts the aggregate 5.1 into cellwise or regime-wise
advice, the "same statement" equivalence in 7.2, the `MN = F·I4` criterion, and
the framing of `deg P(D45)` as the sole obstruction.

**The one ruling the integrator most needs.** Do not let the report's plain-terms
item (3) or the §5 "Consequence for the board" steer the batch. Claim 5.1 is a
theorem about a weighted sum whose only geometric input is `dim D45 > dim R135`;
that inequality holds at every length 5 through 16 with a widening gap, so it
cannot single out five rows, and it says nothing about any cell. The programme's
sole cellwise separation evidence is *at* five rows (Theorem E). Where to hunt
for `D > 0` remains an open empirical question, to be settled by the `U > B`
screen with clipped `U` and symmetric `s`, at every length, not by Section 5.

## 7. Release gate for slots 03, 04 and 09 (written before reading the board's intake)

State at the time of writing: no B18 artefact exists under `B15-03`, `B15-04` or
`B15-09` (`docs/`, `results/`, `analysis/` checked for `b18_*`). Nothing from those
slots has been released, so there is nothing to pass or fail yet. The criteria I
will apply, so that a worker can pre-check their own release against them:

**G1 - Provenance.** The report opens with `git rev-parse HEAD` and `HEAD^{tree}`.
Every numerical artefact has a path under `results/b18_NN/` in the slot's own
worktree, and the script that produced it exists at the cited path. (The v1 Slot 01
report cited `out/` scripts that do not exist; I reproduced its numbers
independently, but a release I cannot reproduce from the tree does not pass.)

**G2 - Conventions declared per number.** For every `s`: ordinary or symmetric
rectangular Kronecker, said at the point of use. For every `U`: `min(a, T)`, with
`T` shown separately if at all. For every coefficient computation: ordinary
`c_alpha` with raising `(alpha_i + 1) c_(alpha + e_i - e_j)`, or factorial-normalised
with `alpha_j`, stated; a rank computed in one convention is not transported to
the other by "equal kernel dimensions".

**G3 - Direction of every rank.** A modular rank equal to the ambient `a` (or to the
row count of the evaluated family) proves the rational statement; any deficient
modular rank is a lower bound on the rational rank and hence an upper bound on the
ideal multiplicity, never a floor on `i`. A rank of evaluations at sampled points is
a lower bound on `m` for the variety the points lie on, and on nothing else. A
sampled zero establishes nothing. I will re-derive at least one decisive small
rank per release myself, at the released point, exactly over `Q` where the size
allows, before passing it.

**G4 - Which variety the points lie on.** An "actual padding" rank `r` must be
computed at points exhibited as `(z per3) ∘ T` with `T` written down (or, for
`ell <= 5`, as `l · per3(L(x))` with `l` and `L` written down). A rank at points
merely asserted to lie in `R135` or in `X_pad` is accepted for `m_pad` only if
membership is shown (for `R135`: the point is an explicit product `l · C`). A rank
at points of `X_det` or its restrictions is a bound for `m_det`, never for
`m_pad`. Orbit multiplicity is not closure multiplicity: a function evaluated on
orbit points bounds `m` for the closure from below only because the polynomials
are global; a "regular function on the orbit" is not admissible.

**G5 - A gap claim.** Passes only with `B = min(a, s - b)` (`b` certified or `0`) and
an exhibited `(B+1)`-minor of highest-weight polynomials evaluated at actual
padding points, both in the same `(d, lambda)`, both in the same convention, with
the minor's nonvanishing rechecked here. `U > B` alone is headroom and is reported
as such. "Geometric separation" (one determinant equation nonzero on padding) is
reported as such and never as `D > 0`.

**G6 - Aggregate versus cell.** Any statement derived from Hilbert functions,
dimensions, or a weighted sum over `lambda` is labelled aggregate and is not used
to nominate, exclude, or rank cells (§3 of this review).

**G7 - Scope.** The ten excluded cells and the original-entry diagonal method are
not reopened; the `MN = F·I4` criterion and the four-variable LLV control are not
used as membership tests or shortcuts.

A release meeting G1-G7 passes with the numbers quoted as labelled. A release
failing G2 or G3 is returned with the specific number named. A release failing G5
but otherwise sound is passed with its claim relabelled (headroom or separation),
not rejected.

## 6. Comparison with the board's intake (read only after §§1-5 and §7 were on disk)

The board's "Intake of the first Slot 01 report" is six bullets. Point by point:

| Board bullet | My finding | Reached independently? |
|---|---|---|
| `d <= 4^49` "looks defensible"; not a search budget | ACCEPTED, and I checked that the three lemmas compose (§2) | yes |
| exact dimension 50 "requires the producer's modular rank certificate to be delivered and reviewed" | **Discharged here.** The producer's scripts are not in the tree, but I rebuilt the Jacobian from scratch and obtained exact rank 50 over `Q` at the producer's point and at an independent point, plus the stabiliser nullity 1 (§1). `dim D45 = 50` is PROVED, not provisional. | yes; and I go further than the board |
| aggregate sum "provisionally credible conditional on that certificate"; does not exclude a positive cell, predict screens fail, or justify abandoning five rows | Same ruling, now unconditional (PROVED). I add the reason it *cannot* single out five rows: the identical argument holds at every length, and the measured dimension gap widens from 11 at `r = 5` to 35 at `r = 10` (§3.2(c)). | yes |
| reject `MN = F·I4` with the `l·I4`, `C·I4` witness | REJECTED. **Not independent**: the preamble handed me the witness. My addition is the mechanism (`det M · det N = F^4` is all the identity forces) (§4.4). | no, disclosed |
| do not accept the degree as the only route; do not equate sufficient kernel inclusion with a necessary multiplicity condition | Both REJECTED by me (§2 calibration remark 2; §4.6 "same statement"). I add the quantitative point that in the four-variable control the refined-Bezout route overshoots the true degree by ~15 orders of magnitude, so even the exact degree would not rescue the bound. | yes |
| distinguish ordinary vs symmetric Kronecker; use `U = min(a,T)`, `B = min(a, s-b)` | Same two corrections (§4.1, §4.2), traced to B17-02 line 42 and B17-08 eq. (3). | yes |
| LLV 2303.09028 Table 2 / Theorem 2: 320112 is the 4x4 linear component `F1` | I fetched only the abstract and flagged which component as unverified (§2). The board's pointer resolves my flag; I ADOPT it from the board without having opened Table 2. | partially |

**Where I disagree with the intake.** Nowhere on substance. On strength: the board
leaves `dim D45 = 50` and Claim 5.1 conditional pending a certificate; both are now
proved by replay and should be recorded as such. On completeness: the intake does
not note that the producer's pilot scripts are absent from the tree (G1 of §7), nor
that §7.3 of the report points the gap hunt at `D45` when the missing half of M2 is
a lower bound on `m_pad`, a fact about `R135`.

**The board's characterisation, "correct results and false implications coexist in
a polished document", is confirmed**, and this review locates the seam precisely:
everything through Claim 5.1's *statement* is correct; every *use* of Claim 5.1,
and the `deg P(D45)` framing, is an implication the evidence does not support.

## 8. Next sufficient test, resources, and status

**One next sufficient test.** Run the report's §9 screen in its corrected form, at
`d <= 3` first: for every `lambda ⊢ 4d` with `ell(lambda) = 5`, compute `a`,
`s` (symmetric rectangular Kronecker, transposition included), `T` (Pieri sum),
`U = min(a, T)`, `B = min(a, s)`, and list cells with `U > B`. Price: one process,
`timeout 60`, `ulimit -v 524288`; at `d = 3` the partitions of 12 with five rows
number 13 and `S_12` character values are trivial, so this is seconds. Extend to
`d = 5` only after the `d <= 3` run is timed. Whatever it returns is headroom, not
a candidate, and it says nothing about `D` in cells it retires.

**Resources used by this review (MEASURED).** Three `python3` processes
(`replay_d45.py`, `replay_r135.py`, `lengths.py` in the session scratchpad), one
process each, `python-flint` exact rational ranks, no BLAS, each finishing in
seconds; the largest matrix was `160 x 715`. They were run on the Windows bash
shell without an explicit `timeout`/`ulimit` wrapper; each is far inside the
preamble's cap by inspection, and I record the omission rather than claim the
wrapper. One network fetch: the arXiv abstract page of 2303.09028. No git command
beyond the two `rev-parse` calls and one `git status --porcelain`; the only file
written in the worktree is `docs/b18_10_review.md`.

**Status: COMPLETE.** Sections 1-8 on disk. Gate for slots 03, 04, 09: criteria
G1-G7 stated in §7; no release from those slots existed when this was written, so
no numerical release has been passed or failed. Any such release is to be
checked against §7 before its numbers are quoted anywhere.

## 9. Reconciliation of the length sweep (§3.2(c)) with the integrator's table

**Outcome 1: the two tables measure different padding varieties, and mine is the
one the argument needs. The integrator's numbers are correct for the variety they
measure; that variety is not the `L`-variable restriction of `X_pad` for `L >= 6`.**

Provenance for this section: worktree still at `HEAD 421493a0…`, tree
`67f2639e…`. I read the integrator's script
`analysis/integrate/b18_10_verify_length_sweep.py` (read-only). Its `dim_R13(L)`
takes derivatives with respect to the coefficients of a **free** cubic `C` in `L`
variables, so it measures
`R13L = closure{ l * C : l linear, C any cubic in L variables }`,
of dimension `L + C(L+2,3) - 1`. I did not re-run it; the formula reproduces its
column exactly (61, 90, 127, 173, 229).

What my `lengths.py` measures (§3.2(c), the column I labelled `dim P_r`) is the
derivative with respect to the entries of `T`, for
`P_L = closure{ (z * per3) ∘ T : T ∈ Hom(C^L, C^10) }
     = closure{ l(x) * per3(N(x)) : l ∈ (C^L)^*, N ∈ Mat_3((C^L)^*) }`,
i.e. the honest `L`-variable restriction of `X_pad`, with the nine permanent entries
restricted to *linear forms in `L` variables*, not replaced by a free cubic. I did
not name `P_L` in the review text, only in the script comment; that omission is
what made the two tables look like the same measurement. Corrected and fully
labelled:

| `L` | ambient `Sym^4(C^L)` | `dim D4L` (= `16L - 30`) | `dim P_L` = restriction of `X_pad` | `dim R13L` = all linear × cubic | `D4L - P_L` | `D4L - R13L` |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 70 | 50 | 39 | 39 | +11 | +11 |
| 6 | 126 | 66 | 55 | 61 | +11 | +5 |
| 7 | 210 | 82 | 65 | 90 | +17 | -8 |
| 8 | 330 | 98 | 75 | 127 | +23 | -29 |
| 9 | 495 | 114 | 85 | 173 | +29 | -59 |
| 10 | 715 | 130 | 95 | 229 | +35 | -99 |

`dim P_L` values are exact Jacobian ranks over `Q` at a random integer point (lower
bounds) and, for `L >= 6`, they meet the upper bound `10L - 5` derived next, so
they are exact. `dim R13L` is the integrator's column; I agree with it as a
measurement of `R13L`.

**Why `P_L`, not `R13L`, is the object.** Claim 1.4 (B17-03 Lemma 2, accepted 03-A)
identifies the `ell(lambda) <= L` cells of the sixteen-variable problem with the
`GL_L` problem for `closure(rho_L(X_pad))`, and Lemma 2 computes that closure as
`closure{ f ∘ T : T ∈ Hom(C^L, C^16) }` with `f = z * per3`, which is `P_L` above.
`R13L` enters only through B17-01-A: at `L = 5` the map `N ↦ per3(N)` from
`Mat_3((C^5)^*)` to five-variable cubics is dominant, so `P_5 = R135`. That
dominance is a five-variable fact. For `L >= 6` it fails on dimension alone:
`Mat_3((C^L)^*)` has dimension `9L`, the stabiliser of `per3` in `GL_9` has
dimension 4 and acts freely at a generic `N`, and the product with a linear form
adds `L` and removes the scalar `(tl, t^{-1}C)` line, so

    dim P_L <= L + (9L - 4) - 1 = 10L - 5,

which is `55 < 61` at `L = 6` and falls further behind `L + C(L+2,3) - 1` after
that. So `P_L` is a *proper* closed subvariety of `R13L` for every `L >= 6`, the
padding ideal `I(P_L)` is strictly larger than `I(R13L)`, and any statement about
`i_pad`, `m_pad` or the aggregate at length `L >= 6` that uses `R13L` uses the wrong
ideal. The v1 report's own §5 says this in words ("the padding restriction
`R_{1,3,r}` is no longer the object; it is the honest `r`-variable image of
`z · per_3`"); I rejected only its guess that the honest image "can approach" the
determinant side.

**Where the linear-versus-cubic argument fails.** Its premise "`dim R13L` is cubic
in `L`" is true, but `R13L` is not the padding side. The padding side is
parametrised by `Hom(C^L, C^10)`, of dimension `10L`, so `dim P_L <= 10L - 5` is
*linear* in `L`, with slope 10 against the determinant side's slope 16. A linear
function of slope 16 does outpace one of slope 10; the gap `D4L - P_L = 6L - 25`
for `L >= 6` widens exactly as measured. Both sides are images of spaces of linear
maps, `Hom(C^L, C^16)` and `Hom(C^L, C^10)`, which is why both are linear in `L`.

**What survives, and what would have gone wrong.** §3.2(c) stands as written, with
`P_L` now named: the inequality `dim(det side) > dim(padding side)` holds at every
length 5 through 16 with a widening gap, so Claim 5.1's mechanism singles out no
length. Had the `R13L` column been carried forward instead, the next board would
have read a sign reversal at `L = 7` — "padding side bigger, aggregate turns
positive from length seven" — which is false for the actual restriction of `X_pad`
and would have been the same aggregate-to-cell mistake in the opposite direction.
That is the one thing this section is for.

**The verdict does not depend on any of this.** The strike of plain-terms (3) and
the §5 "Consequence" rests on Claim 2.3, that separation carries no sign for `D`,
and on the general point that a weighted sum controls no cell (§3.2(a),(e)); those
hold whichever table one uses. §3.2(c) was, and remains, the additional observation
that the aggregate mechanism is length-blind.

**Resources.** No new computation; one read of the integrator's script. Files
written: this section, appended to `docs/b18_10_review.md`; nothing else.
