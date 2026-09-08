# Programme stock-take at the end of batch 11

Twelve sessions ran: **s68–s73** on the implementation side and **S1–S6** on the
reasoning side.  All twelve delivered.  Every bundle verified against its `.md5`
and applied cleanly onto `226b4ef1`.

This document consolidates the two reviews (`docs/s68_s73_batch11_review.md`,
`docs/s1_s6_batch11_review.md`) with the integrator's own measurements, and is
the record batch 12 should be specified from.  Everything below is either
verified independently here, or labelled as relayed.

---

## 0. The verdict in one sentence

**The wall is gone.**  Batch 10 ended with a single diagnosis — *`dim M_λ = 274`,
and every construction the programme owns realises it inside a carrier of size
`≥ 10⁷`* — and batch 11 produced **two independent realisations that are small**,
neither of which touches the carrier: a bracket-contraction circuit that
evaluates a highest-weight vector at the LMR cell in **0.13 s**, and a one-block
recursion whose precursor at that same cell is **2 168-dimensional**.  The
programme's central obstacle for three batches turned out to be a property of
the coordinates, not of the object.

---

## 1. The batch's central result: two small realisations

### 1.1 The bracket circuit (s69)

A highest-weight vector of weight `λ` in `Sym^δ(Sym^n C^r)` written as a
**contraction network** — one antisymmetriser per column of `λ`, one polarised
copy of the form per letter, the cells as edges — indexed by a filling of the
diagram.  For the LMR shapes `λ' = (h, h, 2^{n₂}, 1^{n₁})` this is two tall
brackets, `n₂` `2×2` brackets and `n₁` linear factors: `(65,17,2⁷)' =
(9,9,2^{15},1^{48})` is exactly the `(2⁹) + (63,15)` split the brief named.

| | coordinate route (s63) | circuit (s69) |
|---|---|---|
| build one vector at LMR | 14.4 TB, 415 days | not built |
| **evaluate** one vector at LMR | — | **0.13 s** (exterior-algebra DP) |
| exact `n = 3` control | banked | **reproduced entry for entry** |

The control is the load-bearing part and it passed exactly: at `((19,7,2⁵),12)`
the circuit's ideal vector expands into the banked `χ`-vector with **0 mismatches
across all 17 047 coordinates**, and is equal up to sign over `Z` after rational
reconstruction (support 3 900, max coefficient 544, `E·U_D = 0`).  Three
independent evaluators agree on 152 cases over 19 shapes at both primes; a
fourth agrees on every `n = 4` case.

**Its honest residue is basis enumeration, not evaluation.**  `mult_det` needs a
spanning set of the 274-dimensional `M_λ`, and random fillings concentrate on
the early-born directions, so the last dimensions are rare.  With the ladder
climb (implemented, validated exactly at `n = 3`) this becomes twelve small
coupon-collector problems instead of one large one, priced at **12–15 CPU-hours
in a 2-core / 7 GB container**.

### 1.2 The one-block recursion (S5), and the number that decides it

`H_δ = S₄ ≀ S_δ`, `K_δ = H_{δ−1} × S₄`.  Restricting `S^{λ_δ}` to
`S_{4δ−4} × S₄` and taking `S₄`-invariants keeps only the `ν = (4)` component,
and `c^λ_{μ,(4)} = 1` exactly when `λ_δ/μ` is a horizontal 4-strip.  Since `K_δ`
and one adjacent block transposition `τ` generate `H_δ`:

    (S^{λ_δ})^{K_δ}  ≅  ⊕_{λ_δ/μ horiz 4-strip} M_{δ−1,μ}  =:  W_δ ,
    M_{λ_δ}  =  ker(τ − I | W_δ) .

**Checked here structurally** — the group theory and the Pieri branching both
hold.  The channel counts reproduce: **3** at `δ = 12` (the first-row
coincidence `λ₁ = λ₂ = 17` collapses it) and **12** at `δ = 13, 14, 16, 18, 24`,
with the twelve predecessor shapes at `δ = 24` matching S5's list one for one.

**`B_δ = dim W_δ`, computed here** (`analysis/wk11_int_bdelta.py`,
`analysis/wk11_int_b24.py`; results in `results/wk11_int_bdelta.json`,
`results/wk11_int_b24.json`):

| `δ` | `a_δ` | channels | **`B_δ`** | `n_χ` | `B_δ / a_δ` | compression `n_χ / B_δ` |
|---|---|---|---|---|---|---|
| 12 | 2 | 3 | **31** | 5 103 802 | 15.5 | **165 000 ×** |
| 24 | 274 | 12 | **2 168** | 31 039 465 | 7.9 | **14 300 ×** |

The twelve predecessor multiplicities at `δ = 24`:

| `μ` (`λ₂₄` less a horizontal 4-strip) | `a₂₃(μ)` |
|---|---|
| `(65,15,2⁶)` | 166 |
| `(65,14,2⁶,1)` | 102 |
| `(65,13,2⁷)` | 109 |
| `(64,16,2⁶)` | 215 |
| `(64,15,2⁶,1)` | 130 |
| `(64,14,2⁷)` | 150 |
| `(63,17,2⁶)` | 246 |
| `(63,16,2⁶,1)` | 163 |
| `(63,15,2⁷)` | 180 |
| `(62,17,2⁶,1)` | 199 |
| `(62,16,2⁷)` | 235 |
| `(61,17,2⁷)` | **273** |
| **`B₂₄`** | **2 168** |

**The computation checks itself.**  The twelfth predecessor `(61,17,2⁷)` *is*
`λ₂₃` on the LMR ladder, so its `a₂₃` must return the banked **273**.  It does,
computed by the same alternation as the other eleven with no special-casing.

**Against S5's own gate this is a clear GO**, by a factor of 4.6 (`B ≤ 10⁴` was
"GO immediately").  And the ratio `B/a` *improves* up the ladder — 15.5 at the
bottom rung, 7.9 at the goal cell — so the precursor tightens around the object
as the degree grows.

### 1.3 The number S5 did not name

`B_δ` measures **one level**; an implementation is recursive, and each
predecessor multiplicity space must be built before the level above it can be
formed.  What an implementation pays is the size of the memoised DAG of distinct
`(shape, δ)` pairs down to the base (`analysis/wk11_int_s5_dag.py`,
`results/wk11_int_s5_dag.txt` — pure combinatorics, seconds to run):

| from | peak distinct shapes at one level | total nodes to `δ = 1` |
|---|---|---|
| `λ₁₂ = (17,17,2⁷)` | 189 | **921** |
| `λ₂₄ = (65,17,2⁷)` | 585 | **7 656** |

Seven and a half thousand nodes, flat at 585 across `δ = 12…16` and falling away
on both sides.  **This should replace `B_δ` as the pre-registered economic
number**, because it is the one that scales with the work.  The `δ = 12`
sub-DAG at 921 nodes is a control small enough to run in an afternoon.

### 1.4 The one caution against both

**A compressed source is worth nothing until it evaluates.**  Both realisations
produce `M_λ` as an object in a representation that supports their own natural
operation — contraction for s69, the block swap for S5 — while the programme
needs `Θ`: those vectors evaluated at determinant and permanent points, in the
monomial coordinates `c_α`.  s69 has already cleared this (its evaluator *is*
the point of it, and the `n = 3` control proves the conventions agree).  S5 has
not: it names the risk in one clause and then prices the route without it.

So the `δ = 12` control for S5 must be **two** tests: recover `dim M₁₂ = 2` from
the three-channel precursor, **and evaluate the two vectors it recovers** against
determinant points, reproducing the value the native engine gives.  Only the
second proves the coordinates are usable, and it is the failure mode of every
realisation the programme has already discarded.

---

## 2. The seed: two sessions, one object, opposite verdicts

| | s68 (coordinates) | s69 (circuit) |
|---|---|---|
| the object | `M₁₂` at `(17,17,2⁷)`, `a = 2` | the same |
| build | monomial array **2.47 TB**, peak 8.18 TB | no coordinates built |
| matrix | `nnz ≈ 0.5–1.8×10¹¹`, 0.6–2.2 TB | — |
| solve | **90–310 years per prime** | sampled fillings, generic rank 2 |
| verdict | **walled twice, each by ≥ 100×** | `mult_det = 2`, **`i_det = 0`**, both primes |

Both are correct.  s68 measured the cost of the *coordinate realisation*; s69
never formed one.  The brief anticipated exactly this pair — "if one side
produces it and the other does not, say so plainly; that is the batch's best
possible outcome for this pair" — and s69 said so.  **This is the redundancy
design paying for itself**, and it is why the batch reached the answer in one
night rather than three.

**So the record must not carry "the seed is unreachable".**  What s68 proved is
that the seed is unreachable *in coordinates*, and — new, and valuable — that
session 63's named opening (streaming orbit representatives) does not change
that, because the *reduced* matrix already has `nnz ≈ N_S` (the fit
`nnz/n_χ ≈ |Stab|`).  Streaming removes the monomial array and leaves the matrix
and the solve untouched.

s69's `i_det(12) = 0` is also the first measurement ever made on the `n = 4` LMR
ladder, and it is consistent: Lemma L makes `i_det` non-decreasing and LMR gives
`i_det(24) ≥ 1`, so zero at the bottom is what a correct instrument returns.

> **Corrected 2026-09-08.**  This paragraph first read `i_det(24) = 1`.  That
> equality is *not* banked — LMR gives only `i_det(24) ≥ 1`, equivalently
> `mult_det ≤ 273`, and the equality needs a certified lower bound
> `rank T_det ≥ 273`.  The consistency argument here needs only the inequality,
> so nothing in this section changes.  What does change is elsewhere: the
> batch-11 C3 line that read "`rank S < 274` ⟹ `i_pad ≥ 1`, which with
> `i_det = 1` gives `D ≤ 0`" leaned on the equality and is withdrawn.  See
> `docs/batch12_integrator_note1.md` §1 for the economy that follows —
> the determinant side never needs the 274th vector, and the one it may skip is
> the last-born direction at `δ = 24`.

---

## 3. What composes — the shortest path to every LMR number

Three sessions each hold one piece and none could see the others.

- `mult_red = rank S`, and `rank S` is the rank of the `a` source vectors in the
  normalisation `D_δ` (s70, proved by Schur).  Equivalently and more cheaply,
  `mult_red` is the rank of the source **evaluated at random reducible points**
  `ℓ·c` — ordinary points of `Sym⁴C⁹`.
- s69's circuit evaluates a highest-weight vector at *any* point in ~0.13 s.
- So `mult_red`, `mult_det`, `mult_pad` and `i_{per₄}` at LMR are all ranks of
  the **same** `274 × K` evaluation matrix, and every one is cheap **once 274
  spanning fillings exist** — which is s69's own stated residue at 12–15
  CPU-hours.
- s71's hybrid, where the build fits, hands back the kernel basis `K` as a
  by-product, which is session 65's `U_D` in source coordinates.

> **Every LMR number the programme wants is one basis enumeration away, on
> hardware already in use.**

This is a proposal, not a result.  The thing to check first is whether `μ*`
pushes through a bracket monomial: with `f = ℓ·c` the polarisation gives
`f̃ = (1/n)Σᵢ ℓ(vᵢ)·c̃(…v̂ᵢ…)`, so `μ*` turns each `f̃` node into a sum of `n`
nodes with one leg split off and the result is again a contraction network.  If
that holds, the evaluation route does not even need `μ*`.

**And s73 makes it decisive rather than incremental.**  By its flat-ladder
argument plus s57's measurement that the LMR cell is the first stable cell of its
ladder at `n = 4`: **once `D(24)` is known it is known at every `δ ≥ 24`.**  The
`n = 4` question is one cell, not a ladder.

---

## 4. What was banked that the programme did not have

**`D = +1` is a theorem, not a measurement (s73).**  On the `n = 3` ladder
`λ_δ = (3δ−17, 7, 2⁵)` the ambient multiplicity is flat from `δ = 12` — verified
here independently at `δ = 12…18, 20` — so Lemma L forces `i_det(δ) = 1` and
`i_per(δ) = 0` at every rung:

    δ     :  8  9  10  11  12  13  14  15  16  17  18 …
    a     :  0  2   4   5   6   6   6   6   6   6   6 …
    i_det :  —  0   0   0   1   1   1   1   1   1   1 …
    i_per :  —  0   0   0   0   0   0   0   0   0   0 …
    D     :  —  0   0   0  +1  +1  +1  +1  +1  +1  +1 …

Five rungs were measured anyway and agree with the theorem everywhere — a run
whose answer is predicted is the sharpest instrument test available.  **46
certificates, 46 PASS.**  The transport work is the best part: the same integer
vector arrives by direct Wiedemann measurement at each new rung and by transport
from the previous one, and session 62's independently exhibited vector transports
into session 73's — two sessions, two drivers, two evaluation families, one line.

**`R₅ ⊄ D₅` on the enumerated normal cone (s72).**  `dim(D₅ ∩ W) = 31 < 35`,
with all four of session 66's named residues closed to numbers: `P ∩ c21` at
order 2 = **19** (the one number s66 left open); the `ker ∩ coker` rank strata
are **0 and 9 only**, both image 29; contact order `≥ 4` obstructed on the linear
route (evidence, labelled as such); the deeper rank-`≤2` strata **drop**
(`28 → 19 → 9`).  New: the interior/boundary split, with `W_int = Φ(X_5) ∩ W`
reparametrised through the `r = 4` base locus and its dimension an **exact
Jacobian upper bound of 31** — not an arc lower bound, so no closure gap.  This
closes the image-versus-closure objection that s54/s59 raised and that Sol's S6
independently re-raised this batch.  It is honest that the *completeness* of the
enumeration is not its to prove; that is S3's object.

**A better house instrument (s71).**  Session 67's initial-term cover finished by
an **exact Schur complement on the uncovered ~0.1 % of columns** produces the
full mod-`p` kernel of the raising operator.  It reproduces all 72 banked
calibration cells exactly — the eleven `mult_red < a` ones included — and runs at
**10 s against 3 094 s** for the Wiedemann route on identical matrices, two to
three orders of magnitude cheaper at every cell with `n_χ ≥ 2·10⁴`.  It is
bounded by the build, not by `n_χ²`, and it hands back the kernel basis.
**It should replace the Wiedemann route as the house instrument below the build
wall.**

**The ladder algorithm, validated to the last vector (s68).**  Transport +
deflate + a three-part rung certificate holds at both primes on two reachable
`n = 4` ladders, with a genuine chained climb that carries the *assembled*
predecessor forward rather than a recomputed oracle.  Recovered births equal
`a_δ − a_{δ−1}` exactly.

**`S` written down for the first time (s70).**  `S = μ*_δ` restricted to the
`λ`-highest-weight space, `rank S = mult_red` proved by Schur, target
`⊕_μ M³_μ` of dimension `h_pad` source-free by the session-42 Pieri identity.
Calibrated two-sided against banked truth — `rank S = 6, 1, 5` where the record
has `mult_red = 6, 1, 5`, both bites strictly below `a` — four-way cross-checked,
and reproduced by an adversarial from-scratch reimplementation.

**The `r = 5` sweep, extended (s71).**  151 cells in frozen pre-registered cost
order, `i_det = 0` at every one and **proved**; **250 of 1 075 tails** now closed
for `D > 0` in every degree, 513 census rungs settled, first length-5 cells ever
measured at `δ = 18, 19, 20`, `a` to 640, `n_χ` to 193 330, 3.4 h total.  Stopped
on its own information-rate rule, not a wall.

**The weight-13 stable dead region, completed (S4 + integrator).**  `|ρ| = 13`
and `a_∞(ρ) ≤ 3` ⟹ `i_det^∞(ρ) = 0`, on **eleven** blocks (see §6).

**A cheaper determinant equation does not exist among the audited families
(S1).**  The one genuine lower-`r` explicit equation is the quinary quartic
discriminant, at coefficient degree `5·3⁴ = 405` — arrived at independently by
S1 and by s71 the same night.  It corrects a statement the record had been
making: "there are no equations at `r < 9`" is false; the right statement is
*no known cheap equations*.  S1 also derives the LMR degree from the
Landsberg–Manivel–Ressayre construction — `(k+2)(d−1)` with `k = 2n−2`, `d = n`,
giving `2n(n−1) = 24` at `n = 4` — which *derives* the family degree formula S6
found empirically in batch 10.

---

## 5. What died

| # | route | closed by |
|---|---|---|
| 1 | standard `q = 2` Adams / wreath replication | `ψ²(s_{(1)}) = p₂ = s_{(2)} − s_{(1,1)}` — Adams doubling is not a positive map `[λ] → [2λ]` (S2) |
| 2 | block-diagonal determinant replication | `det_{2n}(diag(A,B)) = det_n(A)det_n(B)` — lands on a power variety (S2) |
| 3 | wreath deflation as the replication map | canonical direction is large → small; no canonical inverse (S2) |
| 4 | partition-algebra diagram bases | `≈ 3.6×10³³` states; the top-depth quotient still `≈ 1.1×10²³` (S5) |
| 5 | wreath Jucys–Murphy as a multiplicity basis | every vector of `M_λ` is `H`-trivial, so `C[H]` acts by the same character on all 274 copies (S5) |
| 6 | low stable multiplicity as a selector | eleven consecutive weight-13 blocks with `a_∞ ≤ 3` are determinant-full (S4 + integrator) |
| 7 | the `F₄` coincidence `274 = 273 + 1` | audited against the actual source construction: no 26-dimensional object, no Albert algebra, no `𝔣₄` action.  273 is simply the penultimate ladder rung (S6) |
| 8 | classical cheap-equation retrieval as a shortcut | no audited family beats LMR on cost (S1) |
| 9 | middle catalecticant minors | `rank Cat₂(det₄) = C(4,2)² = 36` against `dim Sym²C⁹ = 45`, so the first minor is `37 × 37` — thirteen degrees worse than LMR (S1) |
| 10 | column-support restriction as a per-rung saving | the highest-weight space is **dense** (0.91–1.00) and `ker(E|_{u-free}) = 0` at every rung (s68) |
| 11 | streaming orbit reps as the seed's opening | the *reduced* matrix already has `nnz ≈ N_S`; streaming removes the array, not the matrix or the solve (s68) |
| 12 | sieving the determinant side | the `a + 8` evaluation rows are dense and share at most one leading column, so the certifier stops short by `a − 1` at every cell with `a ≥ 2` — structural (s71) |
| 13 | generic higher-order `r = 5` arcs | smooth support is inert by the contact-order lemma; the singular residue needs the normal cone (S3, s72) |

Thirty-seven dead routes across batches 9, 10 and 11.

**Not dead, reclassified.**  The native LMR carrier, the Foulkes enumeration and
the Gram/support carrier are *implementation*-dead, not mathematically dead —
valid mathematics in a computationally wrong representation (S6).  §1 is what
happens when the representation changes.

---

## 6. What is still open

- **`i_det`, `i_pad` and `D` at the `n = 4` LMR cell.**  Still the programme's
  central goal, and now one basis enumeration away (§3) rather than behind a
  14 TB wall.
- **Completeness of s72's enumeration** — that `Proj gr_J R` has no component
  outside the list.  This is the global special-fibre-algebra statement and it is
  S3's object; s72 says so plainly.
- **`a_∞ = 4` at weight 13.**  The first possible weight-13 stable determinant
  equation now needs `a_∞ ≥ 4`.
- **A determinant-specific intertwiner.**  S2 closed every standard functorial
  operation; a genuinely new construction remains the only asymptotic route.
- **Whether `μ*` pushes through a bracket monomial** (§3) — the one check that
  turns the composition from a proposal into a plan.
- **The `r = 5` coverage residue.**  825 of 976 open closing cells remain,
  `n_χ` from 159 884 up; the frozen queue continues from rank 152.  Coverage, not
  progress on containment.

---

## 7. Corrections ledger

### 7.1 To the record

**The birth profile in `docs/lmr_cell.md` §6 has been wrong since it was
written.**  It read `11, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1`.  The first
entry is `a₁₂ = 2` — banked in `results/s63_aladder.json` and recomputed
independently here.  The old sequence sums to **283**; `a₂₄ = 274`.  The
corrected one sums to 274 exactly.  **Session 69 quoted it back this batch.**
Fixed in place with a note.  Only the first entry changes, so nothing that used
the thin tail is affected — s69's concentration diagnosis and the plan's §2.3
both stand.

**The weight-13 `a_∞ = 1` row was incomplete.**  S4's dead-region theorem stood
on ten blocks; enumerating all 57 partitions of 13 into at most five parts and
computing `a_∞` for each gives **four** tails with `a_∞ = 1`, not three:

    a_∞ = 1 :  (7,2,2,1,1)   (5,5,1,1,1)   (5,3,3,2)   (5,3,3,1,1)

`(5,3,3,2)` appears in no session of either batch.  Run here with the batch-10
instrument: `a_∞ = 1`, raw weight space 3 246, highest-weight support 680,
substituted polynomial nonzero at three random `M₆` pencils (one nonzero point
certifies it exactly), and the convention-independent covariance check
**PASSES**.  So `i_det^∞((5,3,3,2)) = 0` and **S4's theorem holds as stated**, on
eleven blocks rather than ten.  The `a_∞ = 2` (five) and `a_∞ = 3` (two) rows are
confirmed complete.

**A smaller count.**  The record has said "47 weight-13 shapes" since batch 10.
I get 46 (57 partitions, 11 with `a_∞ = 0`).  Whoever next quotes it should
recount rather than inherit.

**A near-miss worth naming.**  s73's third route to its `a`-ladder is the `n = 3`
stable value `a_∞((7,2⁵)) = 6`, over `Sym² ⊕ Sym³`.  The banked `a_inf` routine
computes the `n = 4` quantity, over `Sym² ⊕ Sym³ ⊕ Sym⁴`, and returns **12** for
the same tail.  Both are right; they are different objects.  Anyone comparing
them will think a session is wrong.

**The stock-take's `r = 5` falsifier phrasing is superseded.**
`docs/stocktake_batch10.md` asks for "a length-5 equation of `I(D₅)` above degree
9".  S1's discriminant satisfies that at degree 405 and settles nothing, because
every reducible quartic is singular too, so `Disc ∈ I(R₅)` as well.  The correct
target — which the s71 brief already stated — is an equation of `I(D₅)` **not in
`I(R₅)`**.

### 7.2 To the integrator — three errors in my own briefs

**(i) The `per₄` column at `r = 5` is vacuous** (s71, confirmed here).  The plan
told C4 to add the unpadded `per₄` evaluation wherever a cell was already being
evaluated.  At `r = 5` the `per₄` pencil map is **dominant**:
`dim{per₄ forms} = 16r − 6 = 74 ≥ 70 = dim Sym⁴C⁵`, so `I(Per₅) = 0` and
`i_{per₄} = 0` identically.  It becomes a genuine comparison only at `r ≥ 6`
(`90 < 126`); the LMR statement (`138 < 495` at `r = 9`) is unaffected.  s71
turned it into a two-sided control the engine passed 223 times where the answer
is provably zero — but **this is the second time I have specified a comparison
without checking both varieties are proper**, the first being batch 10's `r ≥ 6`
test that s47 had already made vacuous.

**(ii) "Sieve first" cannot work on the determinant side** (s71 §2.1).  I made
the cost ordering "degeneration first, hybrid for the residue" on the ground that
the certifier removes cells at almost no cost.  It does — on the *reducible*
side.  On the determinant side the dense evaluation rows defeat it structurally.
I had conflated `E_red` with `[E; ev_det]`.

**(iii) The support-restriction premise in C1 was wrong** (s68 Part C).  The
highest-weight space is dense (0.91–1.00, not the projected 0.20–0.26), and the
u-free part carries births only as a *quotient* — `ker(E|_{u-free}) = 0` at every
rung — so column restriction returns nothing.  s68's exact sequence
`0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0` is the correct statement and is new.

**The common shape: three premises taken from a measurement made somewhere else
and not re-checked in the regime the brief applies them to.**  Same failure as
batch 10's corrections ledger, in a different costume.  In each case the check
was one line of arithmetic, and it now belongs in the pre-registration of any
new evaluation column or cost ordering.

---

## 8. The process failure, and what it cost

**Every session cloned `226b4ef1`.**  The batch-11 plan, the worker preamble,
`docs/stocktake_batch10.md`, the P0-A code and certificates and the `n ∈ {3,4}`
verifier existed — in s73's words — "neither at `226b4ef1`, nor in any branch of
the public repository, nor in the integrator tree on the laptop".  The push
never landed.  This is batch 11's own **process rule 2** failing on the very
batch that added it.

What it cost, precisely:

- **s73 rebuilt the verifier extension** that was already banked, and named one
  point family `permanent_pencil` where the banked one is `permanent`.  That is a
  one-word rename across its 46 certificates and nothing else.
- **s71 could not find session 67's bundle either** and re-implemented the
  widened monomial code *and* the initial-term certifier from session 67's
  report.  It says plainly the two implementations have not been compared line
  for line.  **This one is not free**: two independent implementations of the
  same certifier now exist and only one has been validated against the other's
  cells.
- **s73 could not read the P0-A result** and so re-derived `i_per(12) = 0`
  independently, on seeds chosen disjoint from the banked ones — which turned an
  accident into a third independent confirmation of `mult_per = 6`.

The preamble's "stop if the plan is not in your clone" check did not fire,
because the sessions had the brief text pasted and could reconstruct what they
needed.  **That is the check working badly: it should key on the tree, not on
whether the worker feels blocked.**

---

## 9. Session by session

### Implementation side

**s68 (C1) — the seed wall, and the algorithm validated.**  Reported Part A as a
*seed* failure and not a failure of the ladder algorithm, exactly as the brief
separated them, then validated the algorithm where every `M_δ` is independently
computable.  Its Part C is a clean negative that closes one of my own plan
assumptions.  Folded in an adversarial audit that caught its own over-claims.

**s69 (C2) — the batch's result.**  Exact control passed; LMR evaluation at
0.13 s; the `k`-vanishing regularity recorded so a successor does not rediscover
it; the ladder climb implemented and validated at `n = 3`.  Its limitation is
stated precisely and it is the right one.  One correction propagated (§7.1).

**s70 (C3) — the fallback, done properly.**  The Part A labelling is careful in
exactly the way the record needs: proved core, hardness judgment separated, and
the gating conclusion resting only on the proved half.  **One of its two premises
has since been overtaken** — its "the source is walled" was true of the
coordinate source, which is what s69 changed.

**s71 (C4) — the sweep, and a better instrument.**  See §4.  It recorded a
workflow defect of its own (a module edited while the sweep was running) along
with the fact that it ended the sweep **by its recorded pid** and removed the
spurious records.  That is the process rule working.

**s72 (C5) — the upper bound, on the enumerated cone.**  See §4.  Honest about
the one thing it does not prove and correct about whose object that is.

**s73 (C6) — the theorem.**  See §4.  Ran in Mode B as pre-registered when the
Mode A gate did not open, and did not wait.

### Reasoning side

**S1 — no cheaper equation**, with the discriminant correction and the LMR
degree derived rather than observed.  **S2 — every standard `q = 2` operation
closed**, structurally and correctly.  **S3 — the `r = 5` question reduced to a
finite normal-cone problem** with four named residues, which s72 then closed to
numbers; the two shared a target statement fixed before either started, and it
worked.  **S4 — the stable frontier**, complete at `a_∞ ≤ 3` after the eleventh
block.  **S5 — the session that matters** (§1.2).  **S6 — the audit**, with the
exact-image-versus-closure correction that independently reaches what the
batch-10 housekeeping reached from the geometry side.

---

## 10. What batch 12 should be

The batch's shape is different from batch 11's, because the bottleneck has
moved.  There is no longer one hard object; there are two cheap realisations of
it and a specific amount of work between them and every number the programme
wants.

1. **The composition of §3.**  s69's circuit as the source, reducible-point
   evaluation as the consumer, and 12–15 CPU-hours of basis enumeration between
   them.  Check `μ*` on a bracket monomial first — one afternoon — then run it.
   This is the first time every LMR number has had a single named, priced
   obstacle.
2. **S5's `δ = 12` control, in the two-part form of §1.4.**  Recover
   `dim M₁₂ = 2` from the 31-dimensional precursor **and evaluate what it
   recovers**.  The sub-DAG is 921 nodes.
3. **S3's completeness statement** — the only thing between s72's `31 < 35` and
   `R₅ ⊄ D₅` as a theorem.
4. **`a_∞ = 4` at weight 13**, in cost order, stopping at the first nonzero
   stable ideal.
5. **Reconcile the duplicated engineering** — two verifier extensions, two
   certifier implementations — and **push the tree before the briefs go out**.
6. **Adopt s71's hybrid as the house instrument** below the build wall.

And the standing note: if the composition of §3 lands, `D` at the LMR cell is
decided, and by s73's flat-ladder argument it is decided at every `δ ≥ 24` at
once.  **The `n = 4` question is one cell, not a ladder.**
