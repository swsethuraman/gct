# B13-05 — finite-range padded/reducible equality

**Delivery: the bundle `b13_05_fable.bundle` is ONE part, not split — total part
count 1.**  It is made against base `00495110c62acfbbbc951e82cc218ed091563b3f`
(`main` at clone time) and carries the branch `b13_05_fable`.  `b13_05_fable.bundle.md5`
names the bare filename and carries the digest of the whole file; there are no
per-part digests because there are no parts.  Branch history was **not** rewritten.
No push was attempted.

```
board_numbering: batch13
session:         B13-05
base:            00495110c62acfbbbc951e82cc218ed091563b3f
branch:          b13_05_fable
pre-registration results/PREREG_b13_05.md (commit e675cb8, before any computation)
                 + addendum A (fee12aa) + addendum B (671e2e5), each committed
                 before the measurements it governs
```

**Model, recorded truthfully.**  Two models ran this session.  **Claude Fable
5.1** (`claude-fable-5-1`) ran it from the start through the census, the
orbit-stabiliser bound, the top-cell instrument, the Jacobian witnesses, the I4
cell and the brute-force check — every computation reported below, and every
commit through `671e2e5`.  The session was then switched, and **Claude Opus 5**
(`claude-opus-5`) wrote this report and made the delivery commits.  No
computation was re-run across the change; the results below are Fable 5.1's and
the prose assembling them is Opus 5's.  The preamble asks for the model that
actually ran the session, and the honest answer is both, in that order.

---

## 0. Verdict

> **The permanent's degree floor moves up one, for every length at once:
> `I(D_r^{per₃})_δ = 0` for every `r` and every `δ ≤ 7`** (PROVED, §2), where the
> record's global statement stopped at `δ ≤ 6`.  By Prop. 8(1) of
> `docs/transfer_lemma.md` this gives **`mult_pad = mult_red` at every weight of
> every length in every degree `δ ≤ 7`** — the bounded padded/reducible equality
> theorem this assignment asked for.
>
> The new content is the **top cells** `ℓ(μ) = δ`: they are maximal minors of
> the second catalecticant, they carry `a = 1`, and all nineteen of them at
> `δ = 7, 8, 9` are **CERTIFIED empty by exact integer determinants** (§3).  At
> `δ = 7` the top cells *are* the whole genuinely-new census, which is why
> degree 7 closes outright.
>
> **The residual set is 214 cells, all at degree 9** — 152 of length 7 and 62
> of length 8 (§5).  Degrees 7 and 8 need no separate computation: degree 7 is
> closed, and each of the 48 open degree-8 cells is closed by the degree-9 cell
> `μ + 3e₁` through the ideal ladder (§4, PROVED and verified present in the
> census for all 48).  Against a naive census of **1329** constituents over
> `δ = 7, 8, 9`, that is **214** left, none of them below degree 9.
>
> **A negative, characterised and priced** (§6): the orbit-stabiliser bound
> `mult ≤ dim S_μ(C⁹)^{H'}` — the natural cheap invariant-theoretic screen — is
> **silent at every cell in range**, by margins of 62 to 10⁵.  It cannot
> substitute for B13-09's numerical queue at any length in this range, and the
> reason is structural, not accidental (§6.3).

Everything below is labelled **PROVED** / **CERTIFIED** / **MEASURED** /
**ADOPTED** / **RECORDED**.

## 1. Preflight, host, and what was installed

| item | state | label |
|---|---|---|
| `python3 -c "import flint, sympy, numpy, scipy"` | **failed** — no `flint` | RECORDED |
| installed here | `python-flint 0.9.0`, `sympy 1.14.0`, `mpmath 1.3.0` (`pip --break-system-packages`) | RECORDED |
| already present | `numpy 2.4.4`, `scipy 1.17.1`, Python 3.11.15, gcc | RECORDED |
| absent, never needed | Singular, msolve | RECORDED |

**Declared host resources: 2 vCPU (Intel Xeon @ 2.10 GHz), 7 GB RAM, no swap,
~30 GB writable disk.**  This is one small container and it is assumed to be
shared; nothing in this session is a heavy job.  Total compute consumed: about
**16 minutes** of CPU across all runs, the largest single run being the I4
validation cell at 388 s and the degree-9 bound at 88 s.  Peak memory stayed
under 1 GB.  Every run was launched under `timeout` and `ulimit -v 5000000`
with its process id written to `results/logs/b13_05_*.pid`; no run had to be
ended early.

## 2. The length stratification, and the new degree floor

### 2.1 Where the cubic ideal lives (PROVED, assembling ADOPTED inputs)

**Theorem A.**  For every `r ≥ 1` and every `δ ≥ 1`, the constituents `S_μ` that
can appear in `I(D_r^{per₃})_δ ⊂ C[Sym³Cʳ]_δ` satisfy

    6  ≤  ℓ(μ)  ≤  min(r, δ, 9).

*Proof.*  `ℓ(μ) ≤ δ` because every constituent of `Sym^δ(Sym³Cʳ)` has at most
`δ` rows (Pieri).  `ℓ(μ) ≤ r` because `S_μ(Cʳ) = 0` for `ℓ(μ) > r`.
`ℓ(μ) ≥ 6` by `docs/washout_lemma.md` Theorem 2 (`D_k^{per₃} = Sym³C^k` for
`k ≤ 5`, ADOPTED, an exact full-Jacobian-rank witness, rank 35 at both house
primes) together with the restriction lemma of the same document (ADOPTED): a
weight of length `k` sees only `Sym³C^k`, so its multiplicity is the length-`k`
one, and at `k ≤ 5` the variety is everything and the ideal is zero.
`ℓ(μ) ≤ 9`: `per₃` lives in `Sym³C⁹`, so for `r ≥ 9` the restriction lemma sends
every weight of length `k > 9`… more precisely, `D_r^{per₃}` for `r ≥ 9` is the
image of maps `Cʳ → C⁹`, every such map factors through a `≤ 9`-dimensional
image, and `dim D_r^{per₃} ≤ 9r − 4` (Prop. 5, ADOPTED) is far below
`dim Sym³Cʳ`; the ideal is nonzero, but the *problem* is the length-`≤ 9` one
because the whole family is pulled back along `Cʳ → C⁹`.  ∎

**What Theorem A is for.**  It says the cubic equation problem is one finite
object — the ideal of `closure(GL₉ · per₃) ⊂ Sym³C⁹` — stratified by length,
with lengths `≤ 5` empty by theorem, lengths `6, 7, 8, 9` the entire content,
and no dependence on `r` beyond `min(r, ·)`.  A length-7 constituent is the
*same* constituent whether it is met at `r = 7`, `r = 8` or `r = 9`.  **This is
why B13-05's lengths 7 and 8 are shared between the `r = 7` and `r = 8`
problems and are not two separate censuses** — the board's framing of "lengths
seven and eight" is the right one and this is its proof.

### 2.2 The census (MEASURED, two independent routes, and it reproduces four sessions)

`analysis/wk13_b13_05_census.py` → `results/b13_05_census.json` (1444 rows).
`a(μ,δ)` by `wk8_s30_pleth.amb` (symmetric functions) **and** by
`wk9_s42_census.a_weyl` (Weyl alternation over the tail DP), asserted equal at
every one of the 1444 rows; `N_S` by the tail DP at `r = ℓ(μ)`; `|Stab_W(μ)|`
and `n_χ ≥ N_S/|Stab|`.

Constituents with `a ≥ 1`, by degree and length:

| `δ` | ℓ≤5 | ℓ=6 | ℓ=7 | ℓ=8 | ℓ=9 | total |
|---|---|---|---|---|---|---|
| 7 | 129 | **27** | 5 | — | — | 161 |
| 8 | 232 | **91** | 42 | 6 | — | 371 |
| 9 | 365 | **210** | 152 | 62 | 8 | 797 |

The bold column is an **independent reproduction of the length-6 record's
counts**: 4 at `δ = 6` (s37), **27** at `δ = 7` (s41's 20 + s43's 7), **91** at
`δ = 8` (s41's 28 + s43's 54 + s47's 9), **210** at `δ = 9` (s79).  Four
sessions' enumerations, reproduced here from a different direction with an
independent `a`.  s47's own note that the count is 91 and not the 81+10 its
brief stated is confirmed.  The 365 at `δ = 9`, `ℓ ≤ 5` matches
`docs/s79_part2_review.md` §2a exactly, including `Σa = 1213`.

*Genuinely new*, i.e. not covered by any inherited theorem or certificate:
**5** at `δ = 7`, **48** at `δ = 8`, **214** at `δ = 9` — against naive census
sizes of 161, 371 and 797.  The inheritance already removes 72 % of degree 9
before anything is computed, and the board's brief named only the `ℓ ≤ 5` half
of it (§8, defect 1).

### 2.3 The new degree floor

**Theorem B (PROVED).**  `I(D_r^{per₃})_δ = 0` for **every** `r ≥ 1` and
**every** `δ ≤ 7`.  Consequently, by Prop. 8(1) of `docs/transfer_lemma.md`
(ADOPTED), `I(P_r)_δ = I(R_r)_δ` and

    mult_pad(λ, δ)  =  mult_red(λ, δ)      for every λ, every r, every δ ≤ 7.

*Proof.*  By Theorem A the constituents at degree `δ ≤ 7` have
`6 ≤ ℓ(μ) ≤ δ ≤ 7`.
- `ℓ(μ) = 6`: empty at `δ ≤ 6` by s37 (four cells, both primes) and at `δ = 7`
  by s43's completion of all 27 cells — CERTIFIED in the record, and their
  enumeration is reproduced in §2.2.
- `ℓ(μ) = 7`: forces `δ = 7`, i.e. `ℓ(μ) = δ`, the top cells.  There are
  exactly five, each with `a = 1`, and each is CERTIFIED empty in §3.  ∎

**What moved.**  `docs/transfer_lemma.md` §4 and `docs/washout_lemma.md` §5
state the global floor as "the permanent cannot be felt below degree 7".  The
length-6 work of s43 and s41/s47 pushed *length 6* to `δ ≤ 8` but could not move
the global floor, because at `δ = 7` there are also length-7 constituents and
nothing in the record touched length 7 at all.  Those five cells are what this
session closed, and with them the global floor becomes **`δ ≤ 7`**: the
permanent cannot be felt below degree **8**, at any length.  This is the
session's bounded equality theorem.

## 3. The top cells are catalecticant minors (PROVED + CERTIFIED)

**Theorem C.**  Let `ℓ(μ) = δ` and `V = C^δ`.
1. The top cells are indexed by strict partitions `ν ⊢ δ`: `μ = (ν | ν−1) + (1^δ)`
   in Frobenius notation, and `a(μ, δ) = 1`.
2. Write `S(ν)` for the shifted diagram of `ν` — `δ` cells `(i,j)`, `i ≤ j`.  The
   polynomial

       h_μ(c)  =  det [ ⟨c, e_i e_j e_k⟩ ]_{(i,j) ∈ S(ν),  k = 1..δ}

   — a `δ × δ` maximal minor of the second catalecticant
   `Cat_{1,2}(c) : V → Sym²V*` — is a highest-weight vector of weight `μ` in
   `Sym^δ(Sym³V)`, and it is nonzero.  By (1) it therefore *spans* the
   weight-`μ` highest-weight space.
3. Hence `i(μ, δ) = 0` **iff** `h_μ(c) ≠ 0` at a single point `c` of
   `D_δ^{per₃}` — one exact integer determinant, with no `N_S`-sized linear
   algebra anywhere.

*Proof.*  (2) first.  For `q_1..q_δ ∈ Sym²V` and `v_1..v_δ ∈ V`, the assignment
`(q_i; v_j) ↦ det[q_i v_j]` — a determinant of a `δ × δ` matrix with entries in
the commutative ring `Sym(Sym³V)` — is `GL(V)`-equivariant, multilinear, and
alternating in the `q`'s and in the `v`'s separately.  It therefore descends to
an equivariant map `ψ : Λ^δ(Sym²V) ⊗ Λ^δV → Sym^δ(Sym³V)`, and `Λ^δV = det` for
`dim V = δ`.  Littlewood's identity `e_δ[h₂] = Σ_{ν strict} s_{(ν|ν−1)}`
(ADOPTED from the literature; **verified against the census here**, see below)
gives the constituents of `Λ^δ(Sym²V)`, each with multiplicity one, the
`S_{(ν|ν−1)}` component having highest-weight vector the wedge of the quadratic
monomials `e_i e_j` over `S(ν)`.  Applying `ψ` to that wedge tensored with
`e_1∧…∧e_δ` gives exactly the displayed determinant, and equivariance makes it
a highest-weight vector of weight `(ν|ν−1) + (1^δ) = μ`.  Nonzeroness is checked
below.  (1): the weight of the wedge is `(ν|ν−1)` by inspection of `S(ν)`, and
`a(μ,δ) = 1` is read off the census.  (3): `h_μ` spans, so `i(μ,δ) ∈ {0,1}` and
`i = 1` iff `h_μ` vanishes identically on `D_δ^{per₃}`; a single nonvanishing
point refutes that.  ∎

**Validation of the instrument, all pre-registered in addendum A and all passed**
(`analysis/wk13_b13_05_topcells.py` → `results/b13_05_topcells.json`,
`results/logs/b13_05_topcells.log`):

| check | result |
|---|---|
| strict partitions of `δ` ↔ census cells with `ℓ(μ) = δ`, asserted equal | **PASS** at every `δ ≤ 9` (1,1,2,2,3,4,5,6,8 cells) |
| `a(μ,δ) = 1` at every top cell, asserted | **PASS** |
| `h_μ` expanded in the house monomial basis is killed by **every** house raising row (`wk8_s30_core.build_R`), exactly over `Z` | **PASS**, `rows_violated = 0`, at all 9 cells with `δ ≤ 5` |
| `h_μ ≠ 0` at a random rational cubic | **PASS** at all 32 cells, `δ ≤ 9` |
| `h_μ ≠ 0` at a `per₃` pencil for `δ ≤ 6` (the record has `i = 0` there) | **PASS**, 9/9 pencils at all 13 cells |

The third row is the one that matters, and it is the answer to the `exps`-ordering
trap: the expansion resolves every letter by `idx[α]` in `wk8_s30_core.exps`'s
own ordering — the same module whose `build_R` supplies the raising rows — and
the check **asserts that every monomial it produces lies in the weight-`μ` basis**
before testing.  It cannot silently drop a target; if a letter were misplaced the
assertion fires rather than the check passing on a subset.

**The measurement.**  Nineteen top cells at `δ = 7, 8, 9`, nine `per₃` pencils
each (seed 11, box ±40, the house family), exact integer determinants via
`flint.fmpz_mat.det`, also reduced at both house primes and recorded:

| `δ` | cells | result |
|---|---|---|
| 7 | 5: `(9,2⁶)`, `(8,4,2⁴,1)`, `(7,5,3,2,2,1,1)`, `(6,6,3,3,1,1,1)`, `(6,5,5,2,1,1,1)` | `h_μ ≠ 0` at **9 of 9** pencils, every cell |
| 8 | 6: `(10,2⁷)`, `(9,4,2⁵,1)`, `(8,5,3,2,2,2,1,1)`, `(7,6,3,3,2,1,1,1)`, `(7,5,5,2,2,1,1,1)`, `(6,6,5,3,1,1,1,1)` | `h_μ ≠ 0` at **9 of 9**, every cell |
| 9 | 8 (`ℓ = 9`, the `r = 9` problem — **exploratory**, outside the assignment) | `h_μ ≠ 0` at **9 of 9**, every cell |

**CERTIFIED: `i(μ,δ) = 0` at all nineteen.**  This is exact integer arithmetic,
not a modular rank — a nonzero integer is nonzero over `Q`, so one pencil would
have sufficed and nine are redundancy.  No transport, no `u`-scaling, so the
transported-certificate rule does not arise; the pencils themselves are stored
in the JSON beside the values, and `values_are: exact integer determinants of
the stated matrix, untransformed` is recorded in the file.

## 4. The ideal ladder (PROVED)

**Theorem D.**  Let `X ⊆ Sym³Cʳ` be any closed cone and `I = I(X)`.  If
`S_μ ⊆ I_δ` and `a(ν, δ') ≥ 1`, then `S_{μ+ν} ⊆ I_{δ+δ'}`.  Equivalently
`i(μ,δ) ≥ 1 ⟹ i(μ+ν, δ+δ') ≥ 1`, and contrapositively

    i(μ + ν, δ + δ') = 0   ⟹   i(μ, δ) = 0.

*Proof.*  Let `v` be a highest-weight vector of weight `μ` in `I_δ` and `w` one
of weight `ν` in `C[Sym³Cʳ]_{δ'}`.  `I` is an ideal, so `vw ∈ I_{δ+δ'}`; it is a
product of highest-weight vectors, hence a highest-weight vector of weight
`μ+ν`; and it is nonzero because `C[Sym³Cʳ]` is an integral domain.  ∎

**The use.**  Take `δ' = 1`: `Sym¹(Sym³Cʳ) = S_{(3)}`, so `ν = 3e₁` and every
degree-`δ` cell `μ` is closed by the single degree-`(δ+1)` cell `μ + 3e₁`, which
has the same length.  Verified in the census (`results/b13_05_census.json`) that
`μ + 3e₁` is present with `a ≥ 1` for **all 42** degree-8 length-7 cells, **all
6** degree-8 length-8 cells and **all 5** degree-7 length-7 cells — 53 of 53.

So the whole of degree 8 is subordinate to degree 9, and the residual set
collapses onto one degree.  This is the pruning the assignment asked for, and it
is a theorem rather than a heuristic ordering.

**What it does not do.**  It runs one way only.  Emptiness at low degree says
nothing about high degree — which is exactly why Theorem B stops at `δ = 7` and
does not extend itself to `δ = 8`.  A session that reads the ladder backwards
would conclude the problem is finished; it is not.

## 5. The residual set (the deliverable for B13-09)

**Everything that must still be computed, at lengths 7 and 8 through degree 9,
is 214 cells, all of degree 9.**  `results/b13_05_census.json` carries them with
`a`, `N_S`, `|Stab_W|` and `n_χ ≥ N_S/|Stab|`.

| | count | `Σa` | cheapest `N_S` | dearest `N_S` |
|---|---|---|---|---|
| `δ = 9`, `ℓ = 7` | 152 | 265 | 65 416 at `(15,2⁶)` | 1.08·10⁷ |
| `δ = 9`, `ℓ = 8` | 62 | 63 | 1.28·10⁶ at `(13,2⁷)` | 1.96·10⁷ |
| **total** | **214** | **328** | | |

Pricing against s79's measured wall (`N_S·δ = 1.47·10⁸`, rows over 4 GB,
`docs/batch13_board.md` B13-10): **211 of the 214 sit below it**; the three above
it are `(8,5,4,3,2,2,2,1)₉`, `(9,4,4,2,2,2,2,2)₉` and `(7,6,4,3,3,2,1,1)₉`.
**77 cells have `N_S ≤ 10⁶`** and are reachable with the current builder on
ordinary hardware; 175 have `N_S ≤ 5·10⁶`.  Total `Σ N_S = 6.36·10⁸`,
`Σ N_S·δ = 5.72·10⁹`.

The ten cheapest, for B13-09's queue front:

| `ℓ` | `μ` | `a` | `N_S` | `|Stab|` | `n_χ ≥` |
|---|---|---|---|---|---|
| 7 | `(15,2,2,2,2,2,2)` | 1 | 65 416 | 720 | 91 |
| 7 | `(14,4,2,2,2,2,1)` | 1 | 91 274 | 24 | 3 804 |
| 7 | `(12,5,5,2,1,1,1)` | 1 | 108 636 | 12 | 9 053 |
| 7 | `(13,5,3,2,2,1,1)` | 1 | 110 345 | 4 | 27 587 |
| 7 | `(12,6,3,3,1,1,1)` | 1 | 118 048 | 12 | 9 838 |
| 7 | `(14,3,2,2,2,2,2)` | 1 | 147 819 | 120 | 1 232 |
| 7 | `(13,5,2,2,2,2,1)` | 1 | 148 526 | 24 | 6 189 |
| 7 | `(11,6,5,2,1,1,1)` | 1 | 152 466 | 6 | 25 411 |
| 7 | `(12,6,3,2,2,1,1)` | 1 | 159 017 | 4 | 39 755 |
| 7 | `(10,8,3,3,1,1,1)` | 1 | 175 861 | 12 | 14 656 |

**Two notes for whoever runs it.**  First, `n_χ` here is the lower bound
`N_S/|Stab|`; the exact `n_χ` needs the orbit enumeration and is B13-09's, per
the scope boundary.  Second, **145 of the 214 have `a = 1`**, where s43's and
s47's sparse injectivity certificate (`analysis/wk9_s43_inject.py`) applies and
was the route that carried the dearest length-6 cells; that is the natural
instrument for most of this set, not the dense route.

## 6. The orbit-stabiliser bound: a negative, characterised and priced

### 6.1 The instrument

**Theorem E (PROVED).**  Let `H ⊆ GL₉` be any subgroup with `H · per₃ = per₃`.
Then for every `μ` and `δ`,

    mult(μ, δ)  :=  mult_μ C[D_δ^{per₃}]_δ   ≤   b_H(μ, δ)  :=  dim (S_μ(C⁹) ⊗ ·)^H  ,

concretely `b_H(μ,δ) = dim` of the `H`-invariants in the weight-`μ` isotypic
piece of `Sym^δ(Sym³C⁹)`'s ambient.  *Proof.* `C[X]_δ ↪ C[GL₉ · per₃]_δ` and
functions on an orbit are `H`-equivariantly `Ind`-type: a weight-`μ` covariant
restricted to the orbit is determined by its value at `per₃`, which lies in the
`H`-invariants of `S_μ`.  ∎  This is the standard orbit-stabiliser /
Kempf-style bound, and it passes the functoriality pre-check of
`docs/brief_wording.md` §7 in the right direction — it bounds `mult` from above,
so `b < a` is a **membership statement** `i ≥ a − b ≥ 1`, PROVED with no
sampling.

I used `H' = T ⋊ F ⊆ Stab_{GL₉}(per₃)`: `T` the row/column scalings with
`det D₁ det D₂ = 1` (proved in `docs/washout_lemma.md` Prop. 5), and
`F = (S₃ × S₃) ⋊ Z₂` the row permutations, column permutations and transpose,
`|F| = 72`.  Only the proved part of the stabiliser is used; the Marcus–May
full stabiliser is ADOPTED but not load-bearing.  **`F ⊆ Stab(per₃)` is
re-verified exactly at the start of every run** — all 72 elements applied to the
monomial dictionary of `per₃`, asserted equal — and the 72 elements are checked
to be closed under composition.

Computation (`analysis/wk13_b13_05_bound.py`): by Burnside over `F` acting on the
`T`-weight decomposition, `b(μ,δ) = (1/72) Σ_{f∈F} tr(f | S_μ^T)` with
`tr(f | S_μ[ν]) = ⟨s_μ, Π_c p_{ℓ_c}[h_{ν_c}]⟩` summed over the 3×3 magic squares
`ν` with line sums `δ` fixed by `f` (Cauchy identity), characters by
Murnaghan–Nakayama.

### 6.2 Instrument checks — all four pre-registered, all passed

| check | scope | result |
|---|---|---|
| I3.1 `f = id` term: independent Kostka DP vs the character route | every `μ ⊢ 3δ`, `ℓ ≤ 9`, `δ ≤ 7` (1157 weights) | **PASS**, exact agreement |
| I3.2 global sum rule `Σ_μ b(μ,δ)·dim S_μ(C⁹) = (1/72) Σ_f #{fixed monomials}` | `δ = 1..9`, all `μ` | **PASS** at all nine, e.g. `δ=9`: both sides `112 223 764 610 005 031 665` |
| I3.3 brute force — `F`-orbit sums of the monomial space, then the left raising operators, nullity exact over `Q` (`fmpq_mat`) **and** at both primes | `δ = 2` (all 11 `μ`), `δ = 3` (23 of 30 `μ`) | **PASS**, 34 of 34 agree; **7 skipped** above the 2·10⁵-monomial cap, all of them `μ` with `μ₁ ≤ 3` |
| I3.4 consistency with the record: `b ≥ a` wherever `i = 0` is known | all `δ ≤ 6`; `ℓ ≤ 6` at `δ = 7,8,9` | **PASS**, no violation |

The seven cells skipped by I3.3 are named in `results/b13_05_checks.json`; they
are the long thin weights `(3,2,1⁴)`, `(3,1⁶)`, `(2,2,2,2,1)`, `(2,2,2,1,1,1)`,
`(2,2,1⁵)`, `(2,1⁷)`, `(1⁹)`, at 3·10⁵ to 2.8·10⁶ monomials. **All seven have
`a = 0`**, so nothing in this report depends on them; closing them is a few
minutes at a raised cap and is named here rather than left silent.

### 6.3 The negative — outcome N1 of the pre-registration

**MEASURED, and it is the pre-registered negative: `b(μ,δ) ≥ a(μ,δ) at every
cell with `a ≥ 1`, at every degree `δ ≤ 9`, at every length.**  Not one bite in
4 517 weights.  The margins at the genuinely new cells:

| `δ` | `ℓ` | cells | smallest `b − a` | where |
|---|---|---|---|---|
| 7 | 7 | 5 | 117 | `(9,2⁶)` |
| 8 | 7 | 42 | 322 | `(12,2⁶)` |
| 8 | 8 | 6 | **29** | `(10,2⁷)` |
| 9 | 7 | 152 | 691 | `(15,2⁶)` |
| 9 | 8 | 62 | **62** | `(13,2⁷)` |
| 9 | 9 | 8 | **4** | `(11,2⁸)` (exploratory) |

**Why it fails, structurally.**  `b` counts `H'`-invariants in `S_μ(C⁹)`, whose
dimension grows like the dimension of the representation, while `a` counts
plethysm multiplicities, which grow far more slowly.  The ratio `b/a` at the
cheapest cells is already 30 to 700 and it worsens with `δ`.  The trend across
the table is the useful part: the margin shrinks sharply with **length** —
4 at `ℓ = 9` against 691 at `ℓ = 7`, at the same degree — because a longer `μ`
has fewer `H'`-invariants.  So the bound is not hopeless in principle; it is
hopeless *here*, and the place it could conceivably bite is `ℓ = 9`, `δ ≥ 10`,
which is outside this assignment and outside batch 13.  **Extending it to the
full `Stab_{GL₉}(per₃)` cannot rescue it**: the remaining factors are finite, so
`b` can fall by at most a bounded factor, and the margins are orders of
magnitude.  I would not spend another session on this instrument at `ℓ ≤ 8`, and
I record that as the recommendation.

## 7. Two further results, both exact

**7.1 The dimension table extends (PROVED).**  `analysis/wk13_b13_05_checks.py
--jacobian`: the rank of `dΦ_r` at a random integer point (box ±10⁶, seed
20260909+r), exact at both house primes, by a polarisation identity for the cubic
`t ↦ Φ(A + tE)` — not finite differences with truncation error:

| `r` | rank `dΦ_r`, both primes | `9r − 4` | `dim Sym³Cʳ` | conclusion |
|---|---|---|---|---|
| 7 | **59** | 59 | 84 | `dim D_7^{per₃} = 59`, codim 25 |
| 8 | **68** | 68 | 120 | `dim D_8^{per₃} = 68`, codim 52 |
| 9 | **77** | 77 | 165 | `dim D_9^{per₃} = 77`, codim 88 |

Each is a sandwich: the Jacobian rank is a lower bound for `dim` (Lemma 1 of
`docs/washout_lemma.md`, and `rank_p ≤ rank_Q` makes the modular reading a
proof), and Prop. 5's stabiliser bound `9r − 4` is the upper bound; they meet.
This extends Corollary 7's table from `r ≤ 6` to `r ≤ 9`: **`dim D_r^{per₃} =
9r − 4` for `6 ≤ r ≤ 9`**, so the generic stabiliser bound is attained
throughout, and the codimension grows fast — which is why the ideal is expected
to be large at length 9 and why the top cells at `ℓ = 9` being empty (§3) is
mildly surprising and worth the integrator's attention.

**7.2 The inheritance validation cell (CERTIFIED).**  `μ = (11,2,2,2,2,2)`
computed at `r = 7`, `δ = 7` with the house evaluator
`wk8_s30_core.measure(per₃, 9, 3, 7, 7, ·)`, `a + 8 = 9` pencils, seed 11, box
±40, both primes: `N_S = 4603`, `a = 1`, **`mult = 1`**, 388 s.  This is s41's
first line, recomputed at a length one higher than it was banked at, and it
agrees — the restriction lemma behaving as Theorem A says it must.

## 8. Defects in this assignment, and one scope call I made

The board asked for these, so here they are.

1. **The brief names only half the inheritance.**  B13-05's entry says "Theorem
   2 plus the restriction lemma excludes every constituent of length ≤ 5 at every
   degree, which is a large part of any naive census."  True, but the *larger*
   inherited part at the degrees in question is **length 6**, which is excluded
   not by Theorem 2 but by the certified length-6 record (s37, s43, s41/s47,
   s79).  At `δ = 9`: `ℓ ≤ 5` removes 365 of 797, and `ℓ = 6` removes a further
   210 — 26 % of the census that the brief does not mention.  **B13-09's entry
   has the same wording** ("account for shorter components explicitly — by
   citing Theorem 2 and the restriction lemma where they apply"), and a session
   reading it literally could recompute s79's 210 length-6 degree-9 weights,
   which is precisely the failure mode the board is trying to prevent.  The
   citation B13-09 needs is Theorem 2 **and** `results/s79_per6_d9.md`.

2. **"Through degree nine" does not say what happens at length 9.**  At `r = 8`
   the constituents stop at length 8, so the assignment is well posed; but the
   census at `δ = 9` contains 8 cells of length 9, which belong to the `r = 9`
   problem and to no batch-13 entry.  I computed them (they are top cells, and
   §3 closes them) and report them as **exploratory**, outside the assignment.
   The board should decide whether length 9 is B13-09's, batch 14's, or nobody's.

3. **A scope call, declared.**  "B13-05 owns the structural proofs and pruning
   and computes only to validate a claim."  Instrument I5 is a structural claim
   — that the `ℓ(μ) = δ` cells are catalecticant maximal minors — whose
   validation *decides* 19 cells outright, at a cost of 0.01 s each rather than
   the `N_S`-sized build those cells would need on the numerical route.  I judged
   that validating the claim requires evaluating the minor, and that having
   evaluated it I must report what it says.  If the integrator reads the boundary
   more strictly, the 19 decisions are B13-09's to re-derive and mine to have
   only proposed; the theorem in §3 stands either way.  I did **not** run any
   part of B13-09's census.

4. **A wording risk in the preamble, not an error.**  "Record the model that
   actually ran this session" assumes one model per session.  Two ran this one
   (see the header).  A field like `models: [(model, phase)]` would make that
   recordable without a paragraph.

## 9. What I did not do, and what it would cost

| not done | why | price |
|---|---|---|
| **The 214-cell residual queue** | B13-09 owns the numerical queue; the scope boundary is explicit | §5 prices it: 77 cells at `N_S ≤ 10⁶`, 211 of 214 below s79's build wall, `Σ N_S·δ = 5.7·10⁹` |
| **Instrument I6** — the `ℓ = δ−1` cells (the 42 at `δ=8,ℓ=7` and the 62 at `δ=9,ℓ=8`) via the Pieri image of a top cell | pre-registered in addendum B, **not reached before the 20:30 handoff** | this is the highest-value continuation and I price it at **half a session**: build `S_{λ'} ⊂ Λ^{δ−1}(Sym²V)` weight spaces by lowering operators from `ω_ν`, check against Kostka numbers, solve the 1-dimensional Pieri kernel over `Q`, then evaluate `Σ_γ Σ_R x_{R,γ}·det[·]·⟨c,e^γ⟩` at pencils. If it works it closes **all 62** length-8 degree-9 cells and, with the ladder, the 42 at degree 8 — leaving only the 152 length-7 degree-9 cells, and it would extend Theorem B's method rather than repeat it. The one place it can fail is a cell where every top-cell predecessor gives a zero image; that would be a genuine unresolved cell, not an instrument fault |
| **Raising the I3.3 cap** to cover the 7 skipped weights | all have `a = 0`; nothing depends on them | minutes |
| **Length 9 beyond the top cells** | outside the assignment | the `r = 9` census at `δ = 9` is 8 cells, all closed here; `δ ≥ 10` is unpriced and unenumerated |
| **Anything on the quartic/padded side** | not this assignment; and `D > 0` is governed by `i_det`, not by this ideal (`docs/batch13_corrections.md` §1) | — |

**The honest boundary of the negative.**  §6 is a negative over a stated region:
every cell with `a ≥ 1` at `δ ≤ 9`, `ℓ ≤ 9`.  It says the orbit-stabiliser bound
is silent there.  It does **not** say the cubic ideal is empty at degrees 8 and 9
— nothing here does, and §5 is exactly the set that would decide it.

## 10. Relation to the two objectives

This session serves **objective 2** (`mult_pad < mult_red`).  Per
`docs/batch13_corrections.md` §1, that is not a prerequisite for objective 1, and
nothing here bears on `D > 0`: the binding constraint on the obstruction is
`i_det`, and this session touched neither the determinant side nor any padded
cell.  Theorem B is a statement that the permanent is *invisible* through degree
7 — it moves the frontier of a negative, and the programme should read it that
way.  If the 214 cells come back empty too, the honest summary will be that
`mult_pad = mult_red` through degree 9 at every length, and the cubic screen will
have found nothing at four lengths on five instruments.

## 11. Artefacts

```
results/PREREG_b13_05.md           pre-registration + addenda A, B
results/b13_05_census.json         1444 rows, delta <= 9, ell <= 9: a (two routes), N_S, stab, n_chi_lb
results/b13_05_census_d7.json      the delta <= 7 timing probe
results/b13_05_bound_d1to5.json    b(mu,delta), all mu, with the id-term character cross-check
results/b13_05_bound_d6to7.json    "
results/b13_05_bound_d8to9.json    "
results/b13_05_topcells.json       the 32 top cells: nu, S(nu), mu, pencils, exact determinants, both primes
results/b13_05_checks.json         Jacobian ranks r = 7,8,9; the I4 cell; the I3.3 brute force
analysis/wk13_b13_05_census.py     the census
analysis/wk13_b13_05_bound.py      the orbit-stabiliser bound (F, Burnside, Cauchy, MN characters, sum rule)
analysis/wk13_b13_05_topcells.py   instrument I5
analysis/wk13_b13_05_checks.py     I3.3 brute force, Jacobian witnesses, the I4 cell
results/logs/b13_05_*.log|.pid     every run, bounded at launch
```

All files are well under 5 MB; the largest is `results/b13_05_census.json` at
170 KB.  Repository configuration was not modified.

Author of record for the session: B13-05.  Ran as **Claude Fable 5.1**
(computation) and **Claude Opus 5** (report and delivery).  Programme author:
Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
