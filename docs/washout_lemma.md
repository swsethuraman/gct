# The washout lemma: when does the permanent enter?

Session 37 (2026-09-02), branch `s37-dip`.  Pre-registration:
`results/PREREG_s37.md` (committed before any computation).  Exact checks:
`analysis/wk9_s37_jacobian.py` → `results/s37_jacobian.log`;
`analysis/wk9_s37_onsets.py` → `results/s37_onset_*.log`.
Clone tip `5367c75`; ancestry gate (`c02cee8`) passed; no session 36/37
collision on `main`.

Labels: **proved** / **measured** / **adopted-from-literature** /
**expectation**, per the pre-registration.

## 0. Verdict

> **The permanent is invisible below length 6.**  For every weight `lam`
> with `ell(lam) <= 5` and every degree `delta`,
> `mult_pad(lam, delta) = mult_{R_ell}(lam, delta)` where `R_r = {l·c}` is
> the reducible locus with a linear factor, and therefore
> `D(lam, delta) = mult_{R_ell(lam)} − mult_{D_ell(lam)^det}` — a quantity in
> which `per_3` does not appear.  Every `D != 0` cell at `ell <= 5`, in
> either sign, is a statement about *reducibility versus the determinant*.
> The first length at which any cell can be permanent-sensitive is
> `ell = 6`, where `dim D_6^{per_3} = 50 < 56` exactly (Theorem 6), and
> even there the permanent can enter only at degrees where the ideal of
> `D_6^{per_3} ⊂ Sym^3 C^6` is nonzero — which it is not through
> `delta = 6` (Pieri through 5, measured at 6; Prop. 8 of
> `docs/transfer_lemma.md`): **nothing below length 6 and degree 7 can see
> the permanent.**

The finite-generic-stabiliser page flagged in `docs/s30_review.md` §3 is
written here (§4), once for `per_3` and once for `det_4`; with it the
dimension tables of sessions 26, 30 and 33 and the `n = 4` codimension
table are **unconditional** (§5).

## 1. Setting and notation

`f` is a form of degree `n` in `N` variables; `X_f = closure(GL_N · f) ⊂
Sym^n C^N`.  For `r >= 1`,

    D_r^f  =  closure{ f(s_1 A_1 + ... + s_r A_r) : A_i in C^N }  ⊆  Sym^n C^r,

the closure of the pullbacks of `f` along linear maps `C^r -> C^N` (the
`A_i` are the columns; for `f = det_4`, `per_3` the `A_i` are matrices).  The
house objects at `n = 4`: `det_4` (`N = 16`), the padded permanent
`pad = x_0 · per_3` (`N = 10`), and

    R_r  =  { l · c : l in (C^r)^*, c in Sym^3 (C^r)^* }  ⊆  Sym^4 C^r     (closed: image of a proper map),
    P_r  =  D_r^{pad}  =  closure{ l(s) · per_3(M(s)) }                     (the *true* padded-permanent variety).

`mult_f(lam, delta)` is the multiplicity of `S_lam` in `C[X_f]_delta`;
`a(lam, delta)` the ambient multiplicity in `C[Sym^n C^N]_delta`;
`f_units = a − mult_f` the ideal's share; `D = mult_pad − mult_det`.

**Restriction lemma (standing; s28 §3, n4_gate §1; proved).**  Let
`ell(lam) = k`.  A highest-weight vector `h` of weight `lam` in
`C[Sym^n C^N]_delta` is a polynomial in the coefficient functionals `c_alpha`
with `supp(alpha) ⊆ {1..k}` (each monomial `prod c_{alpha_j}` has weight
`sum alpha_j = lam`, and `alpha_j >= 0` componentwise forces
`(alpha_j)_i = 0` for `i > k`), so `h(F) = h(F|_{C^k})` with
`F|_{C^k} = F(x_1..x_k, 0..0)`.  As `g` ranges over `GL_N`, `(g·f)|_{C^k}`
ranges over the pullbacks of `f` along injective linear maps `C^k -> C^N`,
dense in `D_k^f`.  Hence `h in I(X_f)` iff `h in I(D_k^f)`, and the weight-
`lam` highest-weight spaces of `C[Sym^n C^N]_delta` and `C[Sym^n C^k]_delta`
coincide (the extra raising operators `E_{ij}`, `j > k`, kill every
`c_alpha` with `alpha_j = 0`).  Therefore

    mult_f(lam, delta)  =  mult_lam C[D_k^f]_delta,        k = ell(lam),

which is the house definition of `mult` (`analysis/wk8_s30_core.py`).  ∎

## 2. One exact point proves dominance

**Lemma 1 (proved).**  Let `Phi : C^m -> C^M` be a polynomial map and let
`Y = closure(Phi(C^m))`.  Then `dim Y = max_x rank dPhi_x` (characteristic
0), and `rank dPhi_x` is lower semicontinuous in `x`.  Consequently a single
point `x_0` with `rank dPhi_{x_0} = M` proves `Y = C^M`, i.e. `Phi` is
dominant.

*Proof.*  `C^m` is irreducible and smooth; by generic smoothness the
differential of the dominant map `C^m -> Y` is surjective onto `T_y Y` at a
general point, so the generic rank of `dPhi` is `dim Y`; the rank at any
point is at most the generic rank because the vanishing of all
`(k+1)`-minors is a closed condition.  If some point has rank `M` then
`dim Y >= M`, and `Y ⊆ C^M` is irreducible, so `Y = C^M`.  ∎

Rank modulo a prime `p` at an integer point is at most the rank over `Q` at
that point, so a full rank read modulo `p` is a proof, not a probability.

## 3. Washout at `r <= 5`

**Theorem 2 (washout; proved).**  For `r <= 5` the map
`Phi_r : M_3^r -> Sym^3 C^r`, `(A_i) |-> per_3(sum s_i A_i)`, is dominant:
`D_r^{per_3} = Sym^3 C^r`.  Consequently `P_r = R_r` for `r <= 5`.

*Proof.*  By Lemma 1 it suffices to exhibit one point of full Jacobian rank
`C(r+2, 3)`.  Session 26 banked rank 35 at `r = 5`; re-verified this session
at a fresh random integer point (box `±10^6`, seed `20260902`), exact modulo
both house primes, with a dual-number implementation sharing no code with
`analysis/wk8_s30_dims.py` (**measured**, `results/s37_jacobian.log`):

| `r` | rank `dPhi_r` (both primes) | `dim Sym^3 C^r` | dominant |
|---|---|---|---|
| 2 | 4 | 4 | yes |
| 3 | 10 | 10 | yes |
| 4 | 20 | 20 | yes |
| 5 | **35** | 35 | **yes** |
| 6 | 50 | 56 | no |

For the second sentence: a linear map `C^r -> C^10 = C x M_3` is a pair
`(l, M(s))` with `l in (C^r)^*` and `M(s) = sum s_i A_i` independent, so
`P_r = closure{ l · per_3(M(s)) } = closure{ l · c : l in (C^r)^*, c in Phi_r(M_3^r) }`.
Multiplication `(l, c) |-> l·c` is continuous, `Phi_r(M_3^r)` is dense in
`Sym^3 C^r`, and `R_r` is closed, so the closure is exactly `R_r`.  ∎

**Theorem 3 (what the hunt can see below length 6; proved).**  For every
weight `lam` with `ell(lam) <= 5` and every `delta`:

1. `mult_pad(lam, delta) = mult_lam C[R_{ell(lam)}]_delta`, and hence
   `D(lam, delta) = mult_lam C[R_k]_delta − mult_lam C[D_k^{det_4}]_delta`,
   `k = ell(lam)`, an expression in which `per_3` does not occur.
2. Let `g` be *any* cubic form in any number of variables whose 5-plane
   restrictions are dense (`D_5^g = Sym^3 C^5`; by Lemma 1 a single
   Jacobian rank 35 certifies this).  Then
   `I(X_{x_0·g})_{lam, delta} = I(X_{x_0·per_3})_{lam, delta}` for all
   `ell(lam) <= 5`: no covariant of length `<= 5` distinguishes the padded
   permanent from the padded `g`, nor from `l · (any cubic)`.
3. In particular every cell with `D(lam, delta) != 0` at `ell(lam) <= 5` —
   the s35 cell `((10,10,10,6,0), 9)` included — is a statement about the
   reducible locus `R_k` versus `D_k^{det_4}`, never about the permanent.  A
   `D > 0` cell at `ell <= 5`, should one exist, would be a multiplicity
   witness of the *set-theoretic* non-containment `R_5 ⊄ D_5^{det_4}`
   already proved as s32's Theorem 5 — a proof-of-concept for the
   multiplicity method (exactly DIP's situation, `docs/dip_transfer.md`),
   not new information about `per_3`.

*Proof.*  (1) is the restriction lemma plus Theorem 2.  (2): both sides
equal `I(R_k)_{lam, delta}` by (1) applied to `g` (restrictions of `g` to
`r <= 5` planes are dense once the 5-plane ones are, since a general
`r`-plane sits in a general 5-plane).  (3) restates (1).  ∎

**Remark (a control that is not dense).**  `det_3` fails the hypothesis of
Theorem 3(2): its 5-plane restrictions have rank `29 < 35` (session 26,
`docs/singular_spaces.md` C1).  So `x_0 · det_3` and `x_0 · per_3` are
indistinguishable by covariants of length `<= 4` (both are `R_4` there) but
*can* differ at length 5 — the padded determinant enters one length earlier
than the padded permanent.  This is the sharpest available illustration that
the washout length is a property of the cubic factor, not of padding.

## 4. The finite-generic-stabiliser page

This is the page `docs/s30_review.md` §3 asked for.  It makes the
stabiliser-count upper bounds rigorous.

**Lemma 4 (fibre bound; proved).**  Let `G` be an algebraic group acting on
`C^m`, `Phi : C^m -> C^M` a polynomial map constant on `G`-orbits, and
`Y = closure(Phi(C^m))`.  If the stabiliser `G_x` of a generic point is
finite, then `dim Y <= m − dim G`.

*Proof.*  For a dominant map of irreducible varieties `C^m -> Y` the
generic fibre has dimension `m − dim Y`.  The fibre through `x` contains the
orbit `G·x`, of dimension `dim G − dim G_x = dim G` for generic `x`.  ∎

**Proposition 5 (`per_3`; proved).**  Let `T = {(D_1, D_2) : D_i` diagonal
`3x3`, `det D_1 det D_2 = 1}` act on `M_3^r` by `A_i |-> D_1 A_i D_2`.  Then
`per_3(D_1 A D_2) = per_3(A)` (the permanent is multiplicative under
diagonal scaling of rows and columns: `per(D_1 A D_2) = det D_1 det D_2 per A`),
so `Phi_r` is `T`-invariant.  `dim T = 5`; the subgroup
`{(mu I, mu^{-1} I)}` acts trivially, so the effective group `T_eff = T /
{(mu I, mu^{-1} I)}` has dimension `4 = dim Stab_{GL_9}(per_3)` (the
permanent's stabiliser is `(T_eff ⋊ (S_3 x S_3)) ⋊ Z_2`, adopted from
Marcus–May / Botta, but only the torus part is used and it is proved here).
**For every `r >= 1` the stabiliser in `T_eff` of a generic `r`-tuple is
trivial**: if `D_1 A_1 D_2 = A_1` with every entry of `A_1` nonzero, then
`d_j e_k = 1` for all `j, k`, so `D_1 = d I`, `D_2 = d^{-1} I`.  Hence, by
Lemma 4,

    dim D_r^{per_3}  <=  min( C(r+2, 3),  9r − 4 )          for every r >= 1.

At `r = 6` this reads `dim D_6^{per_3} <= 54 − 4 = 50`.  (Using the full
stabiliser instead of its torus part cannot improve the bound: the extra
factors are finite.)  ∎

**Proposition 6 (`det_4`; proved).**  Let `G = {(P, Q) in GL_4 x GL_4 :
det P det Q = 1}` act by `A_i |-> P A_i Q`; `det(P A Q) = det A`, so the
determinantal `Phi_r` is `G`-invariant.  `dim G = 31`, the scalar
subgroup `{(mu I, mu^{-1} I)}` acts trivially, `G_eff` has dimension
`30 = dim Stab_{GL_16}(det_4) = 2(16 − 1)`.  **For `r >= 3` the stabiliser
in `G_eff` of a generic `r`-tuple is trivial.**  Take `A_1` invertible and
normalise `A_1 = I` (replace `A_i` by `A_1^{-1} A_i`, an element of `G`).
Then `P A_1 Q = A_1` forces `Q = P^{-1}`, and `P A_i P^{-1} = A_i` for
`i >= 2`: `P` lies in the commutant of `{A_2, ..., A_r}`.  For `r >= 3` two
generic `4x4` matrices generate `M_4` as an algebra (take `A_2` with distinct
eigenvalues: its polynomials give the four diagonal idempotents `E_ii` in the
eigenbasis; `A_3` with all entries nonzero in that basis gives
`E_ii A_3 E_jj = a_ij E_ij`, hence every `E_ij`), so the commutant is the
scalars and `P` is trivial in `G_eff`.  Hence

    dim D_r^{det_4}  <=  min( C(r+3, 4),  16r − 30 )        for r >= 3.

**The `r = 2` exception, explained.**  At `r = 2` the commutant of the single
generic matrix `A_2` is its 4-dimensional algebra of polynomials (the
diagonal algebra in its eigenbasis), 3-dimensional modulo scalars, so the
generic stabiliser has dimension 3, the orbit has dimension `27`, and Lemma
4 (with `dim G_x = 3`) gives `dim D_2^{det_4} <= 32 − 27 = 5 = dim Sym^4 C^2`
— consistent with the elementary fact that every binary quartic is a
product of four linear forms, i.e. `det diag(l_1, .., l_4)`.  Stating the
`r >= 3` bound at `r = 2` would read `dim D_2 <= 2` and be false; this is
the same exception as Lemma 5b's at `n = 3` (`docs/isotypic_rank.md`).  ∎

**The reducible locus and the true pad (proved).**  `R_r` is the image of
`(l, c) |-> l·c`; for generic `c` (irreducible cubic) unique factorisation
gives `l·c = l'·c'` only for `(l', c') = (t l, t^{-1} c)`, so the generic
fibre is `C^*` and `dim R_r = r + C(r+2, 3) − 1`.  Likewise, since a general
6-plane restriction of the irreducible cubic `per_3` is irreducible
(Bertini), `dim P_6 = 6 + dim D_6^{per_3} − 1`.

## 5. Consequences: the tables are unconditional, and `ell = 6` is the entry

**Theorem 6 (entry at `r = 6`; proved).**  `dim D_6^{per_3} = 50 < 56`.
Lower bound: Jacobian rank 50 at a fresh exact point (§3 table, both
primes).  Upper bound: Proposition 5.  Hence `dim P_6 = 55 < 61 = dim R_6`,
so `P_6 ⊊ R_6` and `I(R_6) ⊊ I(P_6)`: **length 6 is the first length at
which the padded-permanent variety is smaller than the reducible locus,
and therefore the first at which any cell can be permanent-sensitive.**  ∎

**Corollary 7 (the dimension tables; proved).**  Every entry of the
following is now a theorem, each by the sandwich "Jacobian rank at an exact
point `<= dim <=` stabiliser bound" with the two sides equal:

| variety | `r=2` | `r=3` | `r=4` | `r=5` | `r=6` | upper bound used |
|---|---|---|---|---|---|---|
| `D_r^{per_3}` | 4 | 10 | 20 | 35 | 50 | `min(C(r+2,3), 9r−4)`, Prop. 5 |
| `D_r^{det_4}` | 5 | 15 | 34 | 50 | 66 | `min(C(r+3,4), 16r−30)`, Prop. 6 (`r=2` direct) |
| `R_r = P_r` (`r<=5`) | 5 | 12 | 23 | 39 | — | `r + C(r+2,3) − 1`, §4 |
| `P_6` | | | | | 55 | `6 + 50 − 1` |
| `R_6` | | | | | 61 | `6 + 56 − 1` |

(`R_2 = Sym^4 C^2`; all ranks in `results/s37_jacobian.log`.)  In
particular the `n = 4` codimension table of `docs/sweep62.md` §4 (`codim
det = 0, 1, 20`; `codim pad = 3, 12, 31` at `r = 3, 4, 5`), the `n = 4` gate
table of `docs/n4_gate.md` §2, the dimension rows of `docs/s30_review.md`
§3 and `docs/s33_review.md` (the `r = 4` codimension-1 statement, hence the
principality of `I(D_4^{det_4})`, which the s35 review had already closed
by Beauville) are **unconditional**.  The one soft link named in
`docs/theory_directions.md` §F ("principality of `I(D_4^det)`") is closed
twice over.  For `n = 3` the same page is `docs/isotypic_rank.md` Lemma 5b
(det) and the diagonal argument of Prop. 5 (per), so the session-26 tables
are unconditional too.

**What Theorem 6 does not say.**  `P_6 ⊊ R_6` makes permanent-sensitive
cells *possible* at `ell = 6`; it does not produce one.  Which degrees can
carry them is Prop. 8 of `docs/transfer_lemma.md`: `mult_{P_6} <
mult_{R_6}` at `(lam, delta)` requires `I(D_6^{per_3})_delta != 0` inside
`C[Sym^3 C^6]`, and that ideal is zero through `delta = 5` for free (every constituent of
`Sym^delta(Sym^3)` has at most `delta` rows, and `I(D_6^{per_3})` lives at
length exactly 6) and zero at `delta = 6` by measurement (all four `a > 0`
cells, both primes), so **the permanent cannot be felt below degree 7 even
at length 6**.

## 6. Honest boundary

- **Proved:** Lemma 1, Theorem 2 (given the measured rank 35), Theorem 3,
  Lemma 4, Propositions 5–6, Theorem 6, Corollary 7.
- **Measured (exact, two primes, fresh seed):** the Jacobian table of §3
  and the `det_4`/`pad` rows of §5.
- **Adopted from literature, not load-bearing:** the full stabiliser groups
  of `per_3` and `det_4` (only their torus / `(P,Q)` parts are used, and
  those are proved above); Bertini for the irreducibility of a general
  6-plane restriction of `per_3` (used only for the `55 = 6 + 50 − 1`
  bookkeeping, which is also measured directly as rank 55).
- **Expectation:** none in this document.
