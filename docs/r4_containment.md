# `R_r ⊆ D_r^{det_4}` for `r ≤ 4`, written out; and `r = 5` isolated as open

Session 49 (brief §2.2 and §2.3), 2026-09-05.  Labels: **proved** /
**measured** / **adopted-from-literature**.  The one computation is the
dominance check `analysis/wk9_s49_checks.py A` (`results/logs/s49_checks_A.log`),
a Jacobian rank at a fixed integer point (seed 20260905) modulo both house
primes — a rank at a point is a *lower* bound on the generic rank, the direction
that proves dominance (Lemma 1 of `docs/washout_lemma.md`).

## 0. Statement

> **Theorem 1 (proved).**  For `r ≤ 4`, `R_r ⊆ D_r`, where
> `R_r = {ℓ·c : ℓ ∈ (C^r)^*, c ∈ Sym^3(C^r)^*}` (closed) and
> `D_r = D_r^{det_4} = closure{det_4(Σ_{i=1}^r s_i A_i)} ⊆ Sym^4 C^r`.  Hence
> `P_r ⊆ R_r ⊆ D_r`, and `D(λ, δ) = mult_pad − mult_det ≤ 0` at every weight of
> length `≤ 4` and every degree — the length-`≤ 4` slab is closed by
> containment, in every degree, with no cell measured.  (This is the geometry
> behind paper 2's Theorem `thm:slab`; the multiplicity statement there is
> Lemma 2 of `docs/transfer_lemma.md`.)

> **Open (recorded, not attempted — the subject of session 54).**  Whether
> `R_5 ⊆ D_5`.  The construction below fails at `r = 5` for a proved reason
> (§3), but that rules out the construction, not the inclusion: `D_5` is a
> *closure*, and `R_5 ⊆ D_5` asks whether every `ℓ·c` is a **limit** of `det_4`
> pencils.  Nothing on record decides it, in either direction.

## 1. The block construction and the one thing it needs

**Lemma 2 (block construction; proved, no hypothesis on `ℓ` or `c`).**  If a
cubic `c` in `r` variables is a `3×3` linear determinant, `c = det_3 N(s)` with
`N(s) = Σ_i s_i N_i`, `N_i ∈ M_3`, then for every linear form `ℓ`,

    ℓ·c = det_4( diag(ℓ(s), N(s)) ) = det_4( Σ_i s_i · diag(ℓ_i, N_i) ),

a `det_4` pencil in the same `r` variables.  So `ℓ·c ∈ im Φ_r ⊆ D_r`, where
`Φ_r : (M_4)^r → Sym^4 C^r`, `(A_i) ↦ det_4(Σ s_i A_i)`.  ∎

Lemma 2 assumes nothing about `ℓ` — it may be zero, may divide `c`, may be a
component of a reducible `c`.  So the whole question is **which cubics `c` are
`3×3` linear determinants**, and — because `D_r` is closed — **which are limits
of such.**

**Lemma 3 (det-`3` cubics are dense for `r ≤ 4`; measured, hence proved).**  The
map `Ψ_r : (M_3)^r → Sym^3 C^r`, `(N_i) ↦ det_3(Σ s_i N_i)`, is dominant for
`r ≤ 4`: at the fixed integer point of `analysis/wk9_s49_checks.py A` the
Jacobian has rank `dim Sym^3 C^r` modulo both primes,

| `r` | rank `dΨ_r` | `dim Sym^3 C^r` | dominant |
|---|---|---|---|
| 2 | 4 | 4 | yes |
| 3 | 10 | 10 | yes |
| 4 | **20** | **20** | **yes** |
| 5 | **29** | 35 | **no** |

so a *general* cubic in `≤ 4` variables is a `3×3` linear determinant.  The
count is exactly tight at `r = 4`: `9·4 − 16 = 20 = dim Sym^3 C^4`, the `36`
matrix entries minus the `16`-dimensional effective symmetry
`(P,Q)·N = PNQ`, `det P det Q = 1`, modulo the scalar `(μI, μ^{-1}I)` that fixes
`N` — the image has the full dimension `20` and not one more.  Equivalently
`dim D_4^{det_3} = 20 = dim Sym^3 C^4` (`docs/singular_spaces.md` §6, the
stacking table: works for `r ≤ 4`, fails by `6` at `r = 5`).

## 2. The proof of Theorem 1

**(a) The general member, directly.**  For `r ≤ 4` let `U ⊆ Sym^3 C^r` be the
dense open set of cubics that are `3×3` linear determinants (nonempty by Lemma
3, being the image of a dominant morphism, which contains a dense open).  For
`c ∈ U` and every `ℓ`, Lemma 2 gives `ℓ·c ∈ im Φ_r ⊆ D_r` outright — no limit.

**(b) Every member, by one limit.**  `R_r` is by definition the closure of
`{ℓ·c : ℓ ∈ (C^r)^*, c ∈ Sym^3(C^r)^*}`.  Since `U` is dense in `Sym^3 C^r`,
the set `{ℓ·c : c ∈ U}` is dense in `{ℓ·c : all c}`, whose closure is `R_r`.
Every point of `{ℓ·c : c ∈ U}` lies in `D_r` by (a), and `D_r` is closed, so

    R_r = closure{ℓ·c : c ∈ U} ⊆ D_r .   ∎

This is the whole of the degeneration argument the brief asks for, and it covers
each of the three special cases at once, since each is a point of `R_r`:

- **`c` singular** (nodal, cuspidal, a cone): `c` may lie in the complement of
  `U` (a singular cubic can still be determinantal, but need not be a *general*
  one), so `ℓ·c` is reached as a limit `ℓ·c_t`, `c_t ∈ U`, `c_t → c` — never
  assumed to be a determinant itself.
- **`c` non-reduced** (`c = q·ℓ'`, `c = ℓ'^3`): likewise a boundary point of
  `U`; the same limit applies.
- **`ℓ` a component of `c`** (`ℓ | c`, or `c = ℓ·q`, giving `ℓ^2 q`), and `ℓ = 0`
  (giving `0 ∈ D_r`): Lemma 2 already needs no hypothesis on `ℓ`, so these are
  in `im Φ_r` for `c ∈ U` and in `D_r` by the same limit for `c ∉ U`.

**(c) Tightness is respected.**  The count `9·4 − 16 = 20 = dim Sym^3 C^4` has
**no slack**, and the proof is written so as not to spend any it does not have.
The only existence claim made about an individual cubic is for `c ∈ U`
(a *general* one), where Lemma 3 earns it; for every *special* `c` — exactly the
members where "general" would be an over-claim — the proof uses a limit and
Lemma 2, never a determinantal representation of that special `c`.  Because
`dim D_4^{det_3} = dim Sym^3 C^4`, `U` is dense and the limit always exists; this
is the sole place the equality `20 = 20` is used, and it is used only through
density, not through surjectivity.  Were the image a proper subvariety (as at
`r = 5`, §3), `U` would not be dense and step (b) would collapse.

**The classical picture, for the smooth case (adopted-from-literature; not
load-bearing here).**  A *smooth* cubic surface in `P^3` is a `3×3` linear
determinant, in `72` inequivalent ways — the `72` sixers of its `27` lines, i.e.
the `72` blow-downs to `P^2` (Dolgachev, *Classical Algebraic Geometry* §9.3;
Beauville, *Determinantal hypersurfaces*, Michigan Math. J. **48** (2000) §6).
A smooth plane cubic (`r = 3`) is determinantal via its non-trivial degree-`0`
line bundles, and a binary cubic (`r = 2`) is `det diag(ℓ_1, ℓ_2, ℓ_3)`.  This
exhibits `U` concretely at the smooth cubics, but the proof above rests on
Lemma 3's dimension count, not on the representation count, and so needs no
smoothness.

## 3. Why `r = 5` is different, and is left open

At `r = 5`, `9·5 − 16 = 29 < 35 = dim Sym^3 C^5`: Lemma 3 fails (measured rank
`29`, §1), a general quinary cubic is **not** a `3×3` linear determinant, and
`diag(ℓ, N)` cannot reach a general `ℓ·c`.  This is proved — it is Theorem 5 of
`docs/singular_spaces.md` (the four-dimensional singular subspaces of `M_4(C)`
are classified; the best branch reaches `31 < 35`), and it is the set-theoretic
non-containment `R_5 ⊄ im Φ_5` on the *open orbit*.

It does **not** decide `R_5 ⊆ D_5`, because `D_5` is a closure.  The block
construction is one way to land `ℓ·c` in `im Φ_5`; its failure removes that way
and says nothing about whether `ℓ·c` is a **limit** of `det_4` pencils by some
other family.  So the length-5 slab is **not** closed by containment on the
present evidence, and `R_5 ⊆ D_5` is recorded as open and handed to session 54.

## 4. Correcting what was recorded as decided

Two things elsewhere in the repository over-read the `r = 5` situation, and are
corrected here (the wording fixes themselves are in `docs/s49_report.md` §2.3
and applied in place):

1. **`docs/l5_containment.md` and `docs/singular_spaces.md`** prove
   `R_5 ⊄ im Φ_5` — the generic `ℓ·c` is not a `4×4` determinant of linear forms
   — and state it as "`D_5^{pad}` is **not** contained in `D_5^{det_4}`."  That
   conclusion is about the **image**, not the **closure** `D_5`.  Both documents
   already carry the correct caution ("non-containment does not by itself produce
   an obstruction … the two ideals can have equal multiplicities with different
   subspaces"), but the closure gap is the sharper point: **`R_5 ⊄ im Φ_5` is
   proved; `R_5 ⊆ D_5` (the closure) is open.**  Session 32's Theorem 5 is a
   statement about linear determinantal *representations*, i.e. about `im Φ_5`,
   and should be cited as such — which is exactly how `docs/dip_transfer.md`
   Corollary 1 uses it (`P_5 ⊆ D_5` there is the easy inclusion, and the
   *non*-membership it needs is `x_0·per_3 ∉ closure(GL_16·det_4)`, established
   by [LMR]'s border-complexity bound, not by s32).
2. **Excluding `ℓ ≤ 5` "because of washout."**  Several documents justify
   confining the obstruction search to `ℓ ≥ 6` by `P_r = R_r` for `r ≤ 5`.  That
   is the wrong justification and is corrected in §2.3 of the report: washout
   (`P_r = R_r`) makes a length-`≤ 5` cell a statement about *reducibility versus
   the determinant*, not about the permanent — it does **not** show `D ≤ 0`
   there.  What actually excludes an obstruction at `ℓ ≤ 4` is Theorem 1 above
   (containment, so `D ≤ 0`); what excludes it at `ℓ = 5` is only that **we
   measured those cells and found `D ≤ 0`** (the nine s27/s30 length-5 cells,
   and s38's exhaustive occurrence screen), since containment is open there.
