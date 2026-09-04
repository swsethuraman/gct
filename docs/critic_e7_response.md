# Response to the E7/SL_8 session

Integrator, 2026-09-04.  Every numbered claim below was checked independently
before responding.

## 1. What I verified and agree with

**The Pfaffian identity.**  For `Ω = [[0,B],[−B^T,C]]` on `W = H ⊕ K` with `H`
isotropic and `dim H = dim K = 4`, `Pf Ω = ± det B`.  The combinatorial reason
given is right: with four `H`-indices, no `H`–`H` pair can appear in a
contributing perfect matching, so all four pair into `K`, exhausting `K`, and no
`K`–`K` pair appears either.

**Determinant type implies a common isotropic 4-plane.**  For `L ⊂ A ∧ B`, both
`A` and `B` are isotropic for every `α ∈ L`.  Immediate and correct.

**Closedness of `I_r`.**  The incidence variety projects properly because
`Gr(4,W)` is projective, so the image is Zariski closed.  Correct, and it is the
right reason to prefer this invariant over the grading involution.

**Every dimension count.**  `dim ker(Λ²W → Λ²H) = 28 − 6 = 22`;
`dim I_9 ≤ 16 + 9·13 = 133` against `dim Gr(9,28) = 171`, codimension `≥ 38`;
`dim I_10 ≤ 16 + 10·12 = 136` against `180`, codimension `≥ 44`;
`dim B_9 ≤ 32 + 9·7 = 95`, codimension `≥ 76`; `dim B_10 ≤ 32 + 10·6 = 92`,
codimension `≥ 88`.  All correct.

**Both kills.**  `μ_2`: determinant type lands in `Λ²A ⊗ Λ²B`, rank `≤ 36`,
nontrivial from `r = 9` since `dim Sym² C⁹ = 45`.  Padded type gives
`≤ 9 + 15 = 24 < 36`.  The invariant fails in the wrong direction and should be
killed.  `K(L)`: I checked `J^T Ω + Ω J = 0` for `Ω = [[0,M],[−M^T,0]]` and
`J = diag(I,−I)` — it holds; and the padded block construction has a larger
obvious kernel, so the condition fails to separate.  Killing both is right.

The general lesson is one we already carry as a failure class: the padded
permanent is *more* degenerate than the determinant under most natural
degeneracy statistics.  This is the same shape as the Milnor-corank problem.
Any invariant of the form "determinant type is special in way X" needs a check
that the padded permanent is not special in way X first, and that check is
cheap.  It should be run before the invariant is developed, not after.

## 2. Where the argument is stronger than stated

The `r = 10` rigidity is presented through Atkinson–Lloyd: dimension above
`nr − r + 1 = 10` forces compression structure, so `dim = 10` sits "exactly at
the exceptional classification threshold".  Two things.

First, `dim = 10` is *not* above `10`, so Atkinson–Lloyd as quoted does not
apply at the dimension of interest.  As stated the argument has a gap.

Second, the gap does not matter, because the full classification is available
and is stronger.  Atkinson (1983) classified primitive spaces of bounded rank
`3`, and Huang–Landsberg confirm it: *there are no non-classical examples of
spaces of bounded rank when `r ≤ 3`*, and the only primitive examples are
`E = C^a ⊂ Hom(E, Λ²E)`, `e ↦ (v ↦ e ∧ v)`, of bounded rank `a − 1`, together
with their projections.  For `r = 3` that means `a = 4`: a **four-dimensional**
space, nowhere near ten.

So every ten-dimensional space of singular `4×4` matrices is a subspace of a
compression space.  The compression types for rank `≤ 3` in `M_4` are indexed by
`(k,i)` with `(4 − k) + i = 3`:

| `(k,i)` | `dim` |
|---|---|
| `(1,0)` | 12 |
| `(2,1)` | 10 |
| `(3,2)` | 10 |
| `(4,3)` | 12 |

The case list at `dim = 10` is therefore: the two ten-dimensional compression
spaces, plus ten-dimensional subspaces of the two twelve-dimensional ones.  That
is a genuinely small finite list, resting on a complete classification rather
than on a threshold.  Use this rather than Atkinson–Lloyd.

## 3. Where I would not let the claim stand as written

**Item 5 is a corollary of Alper–Bogart–Velasco, and its content is theirs.**
The chain is: common isotropic 4-plane ⟹ `ℓ·per_3 = det B` for `B` a `4×4`
matrix of linear forms ⟹ setting `ℓ = 1`, an affine `4×4` determinantal
representation of `per_3` ⟹ contradiction with `dc(per_3) = 7`.  Every step is
correct.  But the separating power is entirely ABV's bound `7 > 4`; the Pfaffian
language adds no new lower-bound content.

What it *does* add is localisation: it names the specific geometric feature of
determinant-type pencils that the padded permanent cannot have.  That is worth
recording, with the attribution stated that way.  It should not be written up as
a new separation.

**"That is finite-looking" understates the target.**  The goal in §7 —
`ℓ·per_3` is not a leading quartic of any ten-dimensional singular base pencil —
is a step toward `ℓ·per_3 ∉ D_10`, which is the entire open problem at `(3,4)`.
It is worth being explicit about why it is open: ABV's bound is for exact
representations only, and they note in their Remark 1.9 that `dc` is *not* upper
semicontinuous, giving `xy² + yt² + z³` (with `dc > 3`) degenerating to `z³`
(with `dc = 3`).  So nothing about `dc(per_3) = 7` survives to the border by
general principle.

The consequence for §7: the classification makes the **first layer** finite, and
that is a real reduction.  It does not make the problem finite.  A border
degeneration need not have its first nonzero normalised coefficient at order
one; the polar expansion handles `ord = 1`, and order-`k` terms are where border
problems characteristically die.  The session's own phrasing — "a surprisingly
rigid finite first layer" — is the accurate one, and the later "finite-looking"
should be pulled back to it.

**The E7 content is gone by §7.**  The normal-cone programme is stated in the
determinantal picture, `M(t,s)` a `4×4` matrix, with no Pfaffian and no
exceptional group in it.  The session says as much.  The practical consequence
is that this should not be staffed as an exceptional-groups session; it is a
bounded-rank-matrix-spaces session.  Also worth noting: item 5's argument does
not need the Bläser–Eisenbud–Schreyer `6×6` presentation at all, which is a
strength — the one place the programme depends on an imported construction is a
place where it turns out not to need it.

## 4. Where this sits relative to our statistic

Everything above is an invariant of the **pencil** `L ⊂ Λ²W`, not of the quartic
`F ∈ Sym⁴C^r`.  It does not produce a multiplicity obstruction and it does not
feed s49–s52.  The `I_1(B_9) = I_1(B_10) = 0` computation makes that concrete
from the other side: even inside the Plücker representation the first equations
start at degree two, and degree-two Plücker equations of the section locus still
do not reach coefficient space.

So this is a **change of category**, not a contribution to the current line: it
proposes to prove border non-membership directly, abandoning the GCT statistic
rather than sharpening it.  That is a legitimate and possibly better use of
effort, but it should be named as a second track and not folded into the
existing one.

## 5. What I would do

- **Record** the isotropic-4-plane statement in the research record, attributed
  as a corollary of ABV, with the corrected classification argument from §2
  above replacing the Atkinson–Lloyd framing.
- **Do not reorder s49–s52.**  Those are foundations, the LMR evaluation, the
  `Λ^5` derivation, and the `a = 1` census; none of them is displaced by this.
- **Open a separate track** for the normal-cone classification, staffed as a
  bounded-rank-matrix-spaces session, with the first task being to write out the
  four compression normal forms and their first determinant polars explicitly,
  and the second being to state precisely what happens at order `≥ 2` before any
  case analysis is attempted.  If the order-`≥ 2` question has no plan, the
  session should stop there and say so rather than completing layer one and
  presenting it as near-completion.
- **Reproduce `I_1(B_9) = I_1(B_10) = 0`** independently before promoting it, as
  the session itself proposes.  Low priority — it is a negative result about a
  representation we are not going to use — but it is cheap.
- **Deprioritise `I_2`.**  Degree-two Plücker equations are still equations of
  the section locus, one category away from what we need.

## References checked

- Alper, Bogart, Velasco, *A lower bound for the determinantal complexity of a
  hypersurface*, Found. Comput. Math. 17 (2017).  `dc(per_3) = 7`; Remark 1.9 on
  the failure of upper semicontinuity.
- Atkinson, *Primitive spaces of matrices of bounded rank II* (1983);
  Atkinson–Lloyd, *Large spaces of matrices of bounded rank* (1980).
- Huang, Landsberg, *On linear spaces of matrices of bounded rank*, Selecta Math.
  — "there are no non-classical examples of spaces of bounded rank when `r ≤ 3`".
