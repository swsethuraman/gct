# The DIP technique, tested against our pair

Session 37 (2026-09-02), branch `s37-dip`.  Direction 3 of
`docs/theory_directions.md`, run as the s35 review recommended ("first,
cheapest, calibrates whether the `ell = 5` hunt can ever be permanent-
sensitive").  Read with the two varieties `D_6^{det_4}` (dim 66) and `P_6`
(dim 55) — and `R_6` (dim 61) between them — in hand
(`docs/washout_lemma.md`, `docs/transfer_lemma.md`).

Literature read this session (all **adopted-from-literature**, verified to
the statements quoted; lemma numbers are those of the arXiv versions):
Dörfler–Ikenmeyer–Panova, *On geometric complexity theory: multiplicity
obstructions are stronger than occurrence obstructions*, ICALP 2019 / SIAM
J. Appl. Algebra Geom. 4 (2020), arXiv:1901.04576 [DIP];
Bürgisser–Ikenmeyer–Panova, *No occurrence obstructions in geometric
complexity theory*, J. AMS 32 (2019), arXiv:1604.06431 [BIP];
Bürgisser–Ikenmeyer, *Explicit lower bounds via geometric complexity
theory*, STOC 2013, arXiv:1210.8368, and *Fundamental invariants of orbit
closures*, J. Algebra 477 (2017) [BI]; Landsberg–Manivel–Ressayre,
*Hypersurfaces with degenerate duals and the GCT program*, Comment. Math.
Helv. 88 (2013), arXiv:1004.4802 [LMR].

## 0. Verdict

> **DIP's mechanism transfers verbatim — and it is already in the house.**
> Their multiplicity obstruction is not an evaluated highest-weight vector;
> it is an *ambient-versus-stabiliser* count: the large variety has no
> equations in the degree considered (its multiplicity is the ambient
> plethysm), the small variety's multiplicity is bounded by its stabiliser
> invariants (Peter–Weyl), and a plethysm inequality separates the two
> numbers.  In our notation that is exactly `pad_units = 0` and
> `a > m_det` — the arithmetic route of s28 and Direction 4's occurrence
> screen.
>
> **Their no-go does not transfer as a theorem, but the thing it protects
> does.**  Any obstruction the DIP mechanism can produce, at any length,
> sits at a cell where the pad ideal is empty; by Prop. 8 of
> `docs/transfer_lemma.md` the permanent is invisible at every such cell.
> So the DIP method can produce, at `ell = 6` or anywhere, only separators
> of the *reducible locus* from the determinant — never a permanent-
> sensitive one.  Combined with the transfer theorem (the permanent only
> erases), this promotes the blindness hypothesis to its precise form:
> **every multiplicity obstruction for `(pad, det_4)` is an obstruction for
> `(R_r, det_4)`, and the permanent's only possible role is to erase
> `R_r`-obstructions at `r >= 6`.**  That is a success of this deliverable.
>
> The pair's *set-theoretic* separation is not in doubt: `x_0·per_3 ∉
> closure(GL_16 · det_4)` follows in-house from s32's Theorem 5 (§1 below)
> and agrees with [LMR]'s bound on border determinantal complexity.  So the
> hunt is, exactly as DIP's, for a multiplicity witness of a known
> non-containment — a proof-of-concept for the method, which is how DIP
> themselves describe their result ("extremely modest").

## 1. The two pairs side by side

| | DIP | this programme (`n = 4`) |
|---|---|---|
| small variety | Chow `Ch^n_m = closure{l_1 ··· l_n}`, splitting type `(1^n)` | `D_r^{det_4}`, or (the object the hunt actually sees) `R_r = {l·c}`, splitting type `(1,3)` |
| large variety | `Pow^n_{m,k} = σ_k(Veronese)`, border Waring rank `<= k` | `P_r ⊆ R_r` (true pad), `D_r^{det_4}` |
| separation proved | `Pow ⊄ Ch` (`mult_Ch < mult_Pow`) — obvious as sets | `D > 0` would prove `P_r ⊄ D_r^det` — known as sets |
| status of the set-theoretic statement | trivial | Theorem 5 (s32) + Corollary 1 below; [LMR] |

**Corollary 1 (proved; in-house).**  `x_0 · per_3 ∉ closure(GL_16 · det_4)`.
*Proof.*  If `pad = lim g_t · det_4`, pull back along any linear
`phi : C^5 -> C^16`: `pad ∘ phi = lim det_4 ∘ (g_t ∘ phi) ∈ D_5^{det_4}`
(closed).  So `P_5 ⊆ D_5^{det_4}`.  But `P_5 = R_5` (washout) and
`R_5 ⊄ D_5^{det_4}` (s32, Theorem 5 / Corollary 6).  ∎
This is the statement "border determinantal complexity of `per_3` exceeds
4"; [LMR] prove the quadratic lower bound `\overline{dc}(per_m) >= m^2/2`
(abstract: "a quadratic lower bound for the determinantal border-complexity
of the permanent"; the constant is quoted from the paper's statement as
recorded in the literature, not re-derived), which at `m = 3` gives `>= 5`
— the same fact.  The programme's `n = 4` target is therefore a *known*
separation, and every `D` it computes is about how the multiplicity method
sees it.

## 2. (i) DIP's mechanism, exactly

DIP Theorem 2.3 (quoted): for `m >= 3`, `n >= 2`, `k = d = n + 1` and
`lam = (n^2 − 2, n, 2)`,
`mult_lam(C[Ch^n_m]_d) < mult_lam(C[Pow^n_{m,k}]_d)`; the smallest instance
`m = 3, n = 6, k = d = 7, lam = (34, 6, 2)` gives `7 < 8`.  The proof has
three steps and **no evaluation of any highest-weight vector**:

1. **Large side is ambient** (DIP Prop. 3.3, citing BIP Prop. 3.2): for
   `k >= d`, `mult_lam(C[Pow^n_{m,k}]_d) = a_lam(d[n])`, the plethysm
   coefficient of `Sym^d(Sym^n)`.  Reason: a degree-`d` form vanishing on
   all sums of `d` `n`-th powers vanishes identically (polarise
   `F(sum t_i l_i^n)`; the coefficient of `t_1 ··· t_d` is `d!` times the
   full polarisation evaluated on `n`-th powers, which span).  In house
   terms: `Pow_units(lam, d) = 0` for `d <= k`.
2. **Small side is bounded by its stabiliser** (DIP Lemma 3.4): with
   `H = {diag(alpha_1..alpha_n) : prod alpha_i = 1} ⋊ S_n` the stabiliser
   of `x_1 ··· x_n`, `mult_lam(C[Ch^n_m]_d) <= dim {lam}^H = a_lam(n[d])`
   (Peter–Weyl on `C[GL_n]`; the orbit closure's ring injects into the
   orbit's).  This is the *Peter–Weyl part* of `docs/s24_obstruction.md`,
   `m(lam) = dim (S_lam^*)^H`, and for the determinant it is the
   rectangular Kronecker bound `m_det(lam, delta) <= g(lam, (delta^4),
   (delta^4))` of Direction 4.
3. **A plethysm inequality** (DIP Thm. 3.5, via symmetric functions):
   `a_{(n^2−2, n, 2)}(n+1 [n]) = 1 + a_{(n^2−2, n, 2)}(n [n+1])`.  So
   ambient minus stabiliser bound is `>= 1`.

"Evaluated where": nowhere.  "What makes it tractable": both sides are
plethysm coefficients; the only geometry is in steps 1–2, and both are
general lemmas.  The house identity of s24,
`mult_A − mult_B = [m_A − m_B] − [def_A − def_B]`, reads DIP's obstruction as
a pure Peter–Weyl-part obstruction with `def_Pow = 0` (ambient) and
`def_Ch` unknown but irrelevant (only the bound is used).

**Transfer of the mechanism (proved as a template).**  For our pair the
DIP-mechanism cell is `(lam, delta)` with `ell(lam) = r` such that
(a) `pad_units(lam, delta) = 0`, i.e. `I(P_r)_{lam, delta} = 0`, and
(b) `a(lam, delta) > m_det(lam, delta)`.  Then `D >= a − m_det > 0`.
Step (a) has no general-lemma analogue of Prop. 3.3 for `P_r` — `P_r` is
not a secant variety — so it must be measured (pipeline, or Direction 7),
except that below the pad onset it is automatic.  Step (b) is Direction 4's
screen and is pure combinatorics.  This is precisely the "arithmetic route"
that fired at `n = 3`, `delta = 10`, lengths 8–9 (`docs/d5_ideal.md` §4),
by the degenerate mechanism `m_det = 0`.

## 3. (ii) The occurrence no-go: what is `(1^n)`-specific

DIP prove there are no occurrence obstructions in two finite cases
(`(m, n, d, k) = (3, 6, 7, 4)` and `(4, 7, 8, 4)`): every `mu` with
`a_mu(d[n]) > 0` has `mult_mu(C[Ch^n_m]_d) > 0`.  Structure of the
argument, and what survives splitting type `(1, 3)`:

| ingredient | DIP | survives for `(R_r, D_r^det)`? |
|---|---|---|
| semigroup closure: `mult_mu > 0`, `mult_nu > 0` ⇒ `mult_{mu+nu} > 0` | products of nonvanishing HWVs in the domain `C[Ch]` | **yes**, for any irreducible variety (`R_r`, `P_r`, `D_r^det` all irreducible) |
| length `<= 2`: `a_mu > 0` ⇒ `mult_mu(Ch) > 0` (DIP Prop. 3.12, fundamental theorem of algebra: binary forms split, `Ch_2 = Sym^n C^2`) | `(1^n)`-flavoured but the analogue is available: `R_2 = Sym^4 C^2` and even `D_3^{det_4} = Sym^4 C^3` (`docs/sweep62.md` §4), so at `ell <= 3` every occurring `mu` occurs on both sides; at `ell = 4` by containment `R_4 ⊆ D_4^det` | **yes**, one length better on the det side |
| generators of the semigroup `{mu : a_mu(d[n]) > 0}` (DIP Prop. 3.9–3.10, computer + pigeonhole) | specific to their `(n, m)` | the *method* survives; the list must be recomputed for `Sym^delta(Sym^4 C^5)`, `ell = 5` |
| positivity at length-3 generators by computer (DIP Prop. 5.1) | evaluation on products of linear forms is cheap | for us the check is `mult_det(mu, delta) > 0` at each `ell = 5` generator — the pipeline's `N_S` wall applies; **does not transfer for free** |
| identification `mult(Ch) <= a_lam(n[d])` and its use | needs `Stab(x_1···x_n)`, i.e. `(1^n)` | for `R_r` the analogue is the bidegree bound `h_pad(lam, delta) = mult of S_lam in Sym^delta V ⊗ Sym^delta(Sym^3 V)` (Pieri over `a_mu(delta[3])`) — an upper bound on `mult_R`, useful only for pad-side ideal (the `D < 0` direction); for `D_r^det` it is the Kronecker bound `m_det` | **partially**: the det-side bound is the transferable half |

So the no-go does *not* transfer as a theorem: its finite verification is
pair-specific, and at `ell = 5` it would cost exactly the det-side
multiplicities the pipeline cannot reach in bulk.  What does transfer is a
concrete recipe for a no-go *proof* at `ell = 5`, should one want it:
generators of the `a > 0` semigroup at `ell(lam) = 5` (cheap), then
`mult_det > 0` at each generator (expensive), then semigroup closure.
Note also that [BIP]'s theorem (Thm. 1.4, quoted: "`n >= m^25` and
`lam ⊢ nd`: if `lam` occurs in `C[Z_{n,m}]` then `lam` occurs in
`C[Omega_n]`") is asymptotic and **silent at `(m, n) = (3, 4)`**.  The
house convention that `a = 1` cells are "closed by BIP"
(`docs/n4_gate.md` §2) is therefore an extrapolation outside the theorem's
regime — the *regime transfer* failure class of the ledger — and should be
re-labelled "excluded by convention, not by theorem".  This session does
not change the convention; it flags it.

## 4. (iii) The honest transfer verdict at `ell = 6`

**Theorem 2 (DIP-type cells are permanent-insensitive; proved).**  Let
`(lam, delta)` be a cell at which an obstruction is exhibited by the DIP
mechanism, i.e. with `pad_units(lam, delta) = 0`.  Then
`mult_{P_r}(lam, delta) = mult_{R_r}(lam, delta) = a(lam, delta)` and the
cell is an obstruction for the pair `(R_r, D_r^det)`; replacing `per_3` by
any cubic changes nothing at that cell.

*Proof.*  `I(R_r) ⊆ I(P_r)` (transfer Lemma 1), so `I(P_r)_{lam,delta} = 0`
forces `I(R_r)_{lam,delta} = 0`; both multiplicities equal `a`.  ∎

Together with Theorem 3(4) of `docs/transfer_lemma.md` (the permanent only
erases) this answers the brief's question:

- **Is there a permanent-sensitive separator DIP's method could produce at
  `ell = 6`?**  No — not at `ell = 6` and not at any length.  A
  "permanent-sensitive separator" can only mean a cell where
  `mult_{P_r} < mult_{R_r}`, and at such a cell the DIP mechanism's
  hypothesis (`pad_units = 0`) fails.  The DIP method separates `R_r` from
  `D_r^det`; the permanent enters only to *lower* `D` at cells where
  `I(D_r^{per_3})_delta != 0` — at `r = 6`, only at `delta >= 6`
  (Prop. 8 there).
- **At what cost could DIP's method produce an `(R_6, det)` obstruction at
  `ell = 6`?**  Two ingredients per cell: `m_det(lam, delta)` — a
  rectangular Kronecker coefficient `g(lam, (delta^4), (delta^4))`, cheap
  for `delta <= 8` by character sums or the s31 quiver route, and IP's
  positivity results (arXiv:1512.03798) say in advance where it cannot be
  zero; and `pad_units(lam, delta) = 0` — automatic only below the pad
  onset at length 6, which is unknown (the length-6 pad ideal is
  constrained by `I(R_6) ⊆ I(P_6)`, and `I(R_6)` has 13x13 catalecticant
  minors at `delta = 13`, plus whatever lower-length weights already
  carry: `I(R_3)` starts at `delta = 6`, `docs/blindness_slab.md` §3).  The
  cheapest length-6 cells at `delta = 6` (`results/s37_ell6.log`) all have
  `a = 1`: `(14,2,2,2,2,2)` at `N_S = 7508`, `(10,8,3,1,1,1)` at `9346`,
  `(13,4,2,2,2,1)` at `10486`, … — the first two are inside the pipeline's
  reach, the rest at or beyond the ~10^4 wall.  An `a = 1` hit would be an
  occurrence obstruction for `(R_6, det)` with `m_det = 0`; the s28 mirror
  says such cells appear at `delta ≈ 10` for `n = 3` and at lengths above
  the balanced ones.  **Expectation:** at `n = 4` the first `a > m_det`
  cells at `ell = 6` sit at `delta >= 8`, beyond the pipeline, so the pad
  half of a DIP cell there needs Direction 7.
- **Does the no-go transfer?**  Not as a theorem (§3).  But the *blindness
  hypothesis* is promoted, in the precise form of the Verdict: the hunt is
  a hunt for `(R_r, det)` witnesses, and the permanent can only erase.

**Bürgisser–Ikenmeyer's explicit evaluation, mined for the same question
(adopted at the level of technique; expectation for the cost).**  BI
construct highest-weight vectors of `Sym^d(Sym^n V)` (and of tensor
spaces) from tableaux / obstruction designs: `f_T(p)` is the contraction of
`p^{⊗ d}` with a product of column determinants prescribed by `T`, so at a
point `p` with few terms in its own coordinates (a power sum, a product of
variables, `det_n` as a signed sum over permutations) the evaluation is a
signed count of fillings — combinatorial rather than linear-algebraic.
That is what made `Phi_18(det_3)` computable and is the model for
Direction 7.  For our cells the point is `F = l(s)·per_3(M(s))` in the
`r`-plane coordinates.  After the generic substitution `A : C^r -> C^10`
the restricted quartic is dense in `Sym^4 C^r`, so no sparsity is visible
in the weight coordinates — but structurally `pad ∘ A` is a **sum of six
products of four linear forms** (one product per term of `per_3`, the
linear forms being the rows of `A` pulled back), i.e. a point of the sixth
secant variety of the Chow variety `Ch^4_r`.  BI/DIP evaluate tableau
HWVs at products of linear forms by a signed count of fillings (column
determinants of the chosen forms), and at sums of products by expanding
the `delta`-th tensor power over the summands.  Naively that is
`(6 · 4!)^delta` fillings per HWV per point — `≈ 9·10^12` at `delta = 6`
— which is **not** cheaper than the `N_S^2 ≈ 10^8`–`10^9` pipeline at the
same cells; the BI symmetry reductions (Young symmetriser structure,
identical linear forms across summands) cut this by large but unquantified
factors.  So BI's technique is the right *shape* for the pad side — the
pad point has Chow-secant structure that the det point (24 products, at
balanced weights) does not — but the cost is an open engineering question,
not a free lunch.  Label: **expectation**, mechanism named; the first test
remains one banked `delta = 6` cell (Direction 7's own first test).

## 5. Candidates for session 36's successors (at most three)

1. **`(lam, delta) = ((14,2,2,2,2,2), 6)` and `((10,8,3,1,1,1), 6)`** — the
   two cheapest length-6 cells (`a = 1`, `N_S = 7508`, `9346`; measured
   list `results/s37_ell6.log`).  Reason: the DIP mechanism verbatim at
   length 6 — compute `g(lam, (6^4), (6^4))` (if `0`, `det_units = 1`
   automatically) and `mult_pad` by the pipeline (both reachable); a hit
   is the programme's first `D > 0`, an `(R_6, det)` occurrence
   obstruction, permanent-insensitive by Theorem 2 and outside [BIP]'s
   regime.
2. **The first weight of `I(D_6^{per_3}) ⊂ C[Sym^3 C^6]`** (degree `>= 6`
   by Pieri; the `delta = 6` scan `analysis/wk9_s37_onsets.py per6 6 6` is
   the cheapest exact computation in the programme — 56 coefficients).
   Reason: by Prop. 8 its Pieri transport `mu + (horizontal 6-strip)` is
   the *complete list* of `delta = 6` cells where `P_6 != R_6` can be felt;
   every other length-6 cell at `delta = 6` has `mult_pad = mult_{R_6}` and
   can be computed against `{l·c}` (collapsing) without loss.
3. **The `lam_5 = 1` sub-slab at `ell = 5`, `delta = 7, 8`, cheapest
   `N_S` first** (e.g. the `delta = 7` successors of `(14,5,2,2,1)`,
   `(13,5,4,1,1)`).  Reason: `docs/blindness_slab.md` §4 shows the
   pad-jet variety is *not* covered by jets of actual reducible det pencils
   (33 of 34 dimensions) and the generic block-degeneration limit does not
   cover it either, so these are the first cells where a border
   phenomenon — det-side ideal without pad-side ideal — is structurally
   possible; they are also the cheapest `ell = 5` cells there are.

## 6. Honest boundary

- **Proved:** Corollary 1; the template transfer of §2; Theorem 2; the
  survival table's "yes" entries in §3 (semigroup closure, low-length
  trivialities).
- **Adopted from literature (read this session, to the statements
  quoted):** DIP Thm. 2.3, Prop. 3.3, Lemma 3.4, Thm. 3.5, the structure of
  §§3–5 of DIP; BIP Thm. 1.4 and Prop. 3.2; the LMR quadratic bound; the
  BI tableau-evaluation technique (read at the level of the technique;
  lemma numbers not verified).
- **Measured:** the `delta = 6`, length-6 `(a, N_S)` list.
- **Expectation:** the cost estimates of §4 (both the Kronecker side and
  the BI-style pad evaluation); the guess `delta >= 8` for the first
  `a > m_det` cell at `ell = 6`.
- **Flagged, not changed:** the `a >= 2` gate's attribution to [BIP].
