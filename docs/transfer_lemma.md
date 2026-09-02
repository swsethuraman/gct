# The transfer lemma: what a `D` computed against `{l·c}` proves

Session 37 (2026-09-02), branch `s37-dip`.  Formalises the caveat of
`docs/s35_review.md` §1.  Notation as in `docs/washout_lemma.md` §1:
`R_r = {l·c} ⊆ Sym^4 C^r` (reducible locus with a linear factor),
`P_r = D_r^{x_0·per_3} = closure{ l(s) · per_3(M(s)) }` (the true padded-
permanent variety), `D_r^det = D_r^{det_4}`.  Labels as pre-registered.

## 0. Verdict

> `P_r ⊆ R_r` for every `r`, with equality iff `r <= 5`.  Writing
> `D_R = mult_{R_r} − mult_det` and `D_P = mult_{P_r} − mult_det`
> (the latter is the programme's `D`), one has `D_P <= D_R` cell by cell.
> Hence: a `D_R < 0` cell **transfers** to the true pair (and any bound
> `D_R <= −k` transfers); a `D_R > 0` cell **does not** transfer and must be
> re-derived against `P_r`; conversely every true obstruction `D_P > 0` shows
> up as `D_R > 0`, so `R_r`-computations are a *complete screen* for
> obstructions, never a certificate.  The house pipeline evaluates at true
> padded-permanent points and therefore computes `mult_{P_r}` at every `r`;
> the caveat bites only on literature-style arguments about `{l·c}`
> (catalecticant minors, Kempf collapsing of `{l·c}`), and for those the
> permanent can make a difference only at degrees where
> `I(D_r^{per_3}) ⊂ C[Sym^3 C^r]` is nonzero (Prop. 8).

## 1. Containment and monotonicity

**Lemma 1 (proved).**  `P_r ⊆ R_r` for all `r`, and `P_r = R_r` iff
`r <= 5`.

*Proof.*  Every point `l(s) · per_3(M(s))` of the parametrisation is a
linear form times a cubic, so lies in `R_r`; `R_r` is closed (the image of
the proper map `P(V^*) x P(Sym^3 V^*) -> P(Sym^4 V^*)`, plus `0`), so it
contains the closure `P_r`.  Equality for `r <= 5` is Theorem 2 of
`docs/washout_lemma.md`; for `r >= 6`, `dim P_r = r + dim D_r^{per_3} − 1
<= r + 9r − 4 − 1 < r + C(r+2,3) − 1 = dim R_r` (both by §4 there; at
`r = 6`: `55 < 61`).  ∎

**Lemma 2 (monotonicity; proved).**  If `X ⊆ Y ⊆ Sym^n C^r` are closed and
`GL_r`-stable then `I(Y) ⊆ I(X)` and, in every `(lam, delta)`,
`mult_lam C[X]_delta <= mult_lam C[Y]_delta`, i.e. `X_units >= Y_units`.

*Proof.*  Restriction `C[Y] -> C[X]` is a surjection of graded
`GL_r`-modules; multiplicities of a quotient are at most those of the
source.  ∎

## 2. The transfer theorem

**Theorem 3 (transfer; proved).**  For every `r`, `lam` with
`ell(lam) = r`, and `delta`:

    D_P(lam, delta)  <=  D_R(lam, delta),          with equality for r <= 5.

Consequently:

1. (**`D < 0` transfers.**)  `D_R(lam, delta) <= −k` implies
   `D_P(lam, delta) <= −k`.  In particular every pad-side equation found
   against `{l·c}` — the catalecticant minors of degrees 9, 11, 15
   (`docs/theory_directions.md` §B), the s35 cell `((10,10,10,6,0), 9)` —
   is a genuine equation of the true padded-permanent variety, at every
   `r`.
2. (**`D > 0` does not transfer.**)  `D_R > 0` says only that
   `mult_{R_r} > mult_det`; since `mult_{P_r}` can be smaller than
   `mult_{R_r}` (for `r >= 6`), `D_P` may be `<= 0` at the same cell.  A
   `D_R > 0` cell is a *candidate* and must be re-derived against `P_r`.
3. (**Complete screen.**)  `D_P > 0` implies `D_R > 0`.  So the set of
   `R_r`-obstruction cells contains the set of true obstruction cells; a
   sweep that certifies `D_R <= 0` on a region certifies `D_P <= 0` there.
4. (**The permanent only erases.**)  Passing from `R_r` to `P_r` can only
   *lower* `D`.  The permanent never creates an obstruction that reducibility
   alone would not give; it can only remove one.  The hunt for `D > 0` is
   therefore, at every length, first a hunt for a multiplicity witness of
   `R_r ⊄ D_r^det` (a set-theoretic fact known for all `r >= 5`: Theorem 5
   of `docs/singular_spaces.md` at `r = 5`, and restriction to 5-planes for
   `r >= 6`), and only then a check that the permanent has not erased it.

*Proof.*  Lemmas 1 and 2 give `mult_{P_r} <= mult_{R_r}`; subtract
`mult_det`.  Items 1–4 are restatements.  ∎

## 3. What the house pipeline actually computes

`analysis/wk8_s30_core.py::measure` evaluates the weight-`lam` highest-
weight vectors at points `f(sum s_i A_i)` with `f = x_0 · per_3` and random
integer `A_i in C^10` (`per_padded(3, 4)`), i.e. at points
`l(s) · per_3(M(s))` of the parametrisation whose closure is `P_r`.  So
`mult_pad` as measured is `mult_lam C[P_r]_delta` — **the pipeline is
correct at every `r`**, including `r >= 6`, with the standing random-point
caveat unchanged: the rank of an evaluation matrix at finitely many random
points is at most its generic rank, so a measured `mult_pad` is a lower
bound on `mult_{P_r}` (a measured `pad_units` an upper bound), attaining
`a` is a certificate, and a reading below `a` is believed only after the
house's re-run discipline.  Nothing in the pipeline touches `R_r`.

Where the caveat bites is on **arguments that never evaluate at a permanent
point**:

- *Catalecticant minors* (s35).  These vanish on all of `R_r` by the
  structure lemma, hence on `P_r`: they are `D < 0` evidence and transfer
  by Theorem 3(1).  Their nonvanishing at a det pencil is a `det_units`
  statement and is independent of the pad side.  No issue.
- *Kempf collapsing of `{l·c}`* (Direction 1).  This computes
  `mult_lam C[R_r]_delta` exactly.  See Corollary 9.
- *Any "pad ideal is empty at `(lam, delta)`" claim derived from `R_r`*
  (for instance by a bidegree bound `h_pad`): it shows `R_r`-units `= 0`,
  which for `r >= 6` does **not** show `P_r`-units `= 0`.  A DIP-style
  obstruction argument (large side has empty ideal, small side bounded by
  its stabiliser) applied to `(P_r, D_r^det)` needs the emptiness on the
  `P_r` side; on the `R_r` side it gives only the screen of Theorem 3(3).

## 4. Where exactly the permanent can enter

**Proposition 8 (proved).**  Let `mu : V^* x Sym^3 V^* -> Sym^4 V^*`,
`(l, c) |-> l·c`, `V = C^r`.  Then for every `delta`

    I(P_r)_delta / I(R_r)_delta   ↪   C[V^*]_delta ⊗ I(D_r^{per_3})_delta ,

`GL_r`-equivariantly.  In particular:

1. If `I(D_r^{per_3})_delta = 0` then `I(P_r)_delta = I(R_r)_delta` and
   `mult_{P_r}(lam, delta) = mult_{R_r}(lam, delta)` for **every** `lam`.
2. Weight by weight: `mult_{P_r}(lam, delta) < mult_{R_r}(lam, delta)`
   requires a weight `mu ⊆ lam` with `lam/mu` a horizontal strip of size
   `delta` (Pieri) and `S_mu ⊆ I(D_r^{per_3})_delta`.

*Proof.*  `mu^* : C[Sym^4 V^*]_delta -> C[V^* x Sym^3 V^*]` lands in
bidegree `(delta, delta)` because `mu` is bilinear.  Since `mu` is dominant
onto `R_r`, `h in I(R_r)` iff `mu^* h = 0`; since `mu(V^* x D_r^{per_3})` is
dense in `P_r`, `h in I(P_r)` iff `mu^* h` vanishes on `V^* x D_r^{per_3}`,
i.e. `mu^* h in I(V^* x D_r^{per_3}) = C[V^*] ⊗ I(D_r^{per_3})` (ideal of a
product, `V^*` being affine space), in bidegree `(delta, delta)`.  So `mu^*`
induces the injection.  (1) is immediate; (2) is the decomposition
`C[V^*]_delta ⊗ S_mu = Sym^delta V ⊗ S_mu = ⊕ S_lam` over horizontal
`delta`-strips.  ∎

**Where the ideal of `D_6^{per_3}` can start (proved + measured).**
`I(D_6^{per_3})` is concentrated at weights of length exactly 6 (restriction
lemma: `D_5^{per_3}` is everything), and every constituent of
`Sym^delta(Sym^3 C^6)` has at most `delta` rows (Pieri), so
`I(D_6^{per_3})_delta = 0` for `delta <= 5` **for free**: the first degree
at which `D_6^{per_3} ⊂ Sym^3 C^6` can have an equation at all is
`delta = 6`, and the first weight a rectangular-ish `lam ⊢ 18` of length 6.
(The scan `analysis/wk9_s37_onsets.py per6` confirms `sum a = 0` at
`delta = 2..5`; its `delta = 6` leg — the first informative one — is
recorded in `results/s37_onset_per6_d56.log` if it completed, see
`docs/session_37.md`.)  With Prop. 8(1): **at `r = 6`,
`mult_{P_6} = mult_{R_6}` in every weight through `delta = 5`**; the
permanent cannot be felt anywhere below degree 6, and at degree `delta`
only at weights `lam` admitting a length-6 `mu ⊆ lam` with `lam/mu` a
horizontal `delta`-strip and `S_mu ⊂ I(D_6^{per_3})_delta`.

## 5. Corollary for Direction 1

**Corollary 9 (proved).**  The Kempf collapsing of `docs/theory_directions.md`
§B(ii)(c), if implemented as described, computes `mult_lam C[R_r]_delta`.
Then:

- for `r <= 5` it computes `mult_pad = mult_{P_r}` exactly (Theorem 2 of
  `docs/washout_lemma.md`), so the s30/s34 anchors at `ell = 5` are the
  right validation targets;
- for `r >= 6` it computes an **upper bound** on `mult_pad`, equivalently a
  **lower bound** on `pad_units`; the gap is bounded above, weight by
  weight, by the Pieri transport of `I(D_r^{per_3})_delta` (Prop. 8(2)),
  and is zero at every degree where `I(D_r^{per_3})_delta = 0`.

So a collapsing-based table remains a valid `D < 0` source and a valid
obstruction *screen* at every `r`; a `D > 0` reading from it at `r >= 6`
is a candidate to be confirmed by the pipeline (which evaluates at
permanent points) or by exhibiting a permanent-specific equation via
Prop. 8.

## 6. Honest boundary

- **Proved:** Lemmas 1–2, Theorem 3, Proposition 8, Corollary 9.
- **Measured:** `sum a = 0` over length-6 weights of `Sym^delta(Sym^3 C^6)`
  for `delta <= 5` (consistent with the Pieri proof); the `delta = 6` leg
  is the first informative measurement and is reported in
  `docs/session_37.md`.
- **Expectation:** nothing here is expectation; the collapsing itself
  (whether it runs) is Direction 1's business, not this document's.
- **Not claimed:** that any `D_R > 0` cell exists; that the permanent ever
  actually erases one.  Both remain open in both directions.
