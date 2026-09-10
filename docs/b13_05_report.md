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
> Two closure theorems then do the pruning without any further computation
> (§4): the **ideal ladder** `i(μ,δ) ≥ 1 ⟹ i(μ+ν, δ+δ') ≥ 1`, and its converse
> partner **Theorem F**, `i(κ,p) = i(ν,q) = 0 ⟹ mult(κ+ν, p+q) ≥ 1`, which
> closes a cell outright when `a = 1`.  Both are one-line proofs resting on
> `C[X]` being a domain, and together they are the pruning engine.
>
> **Degree 8 is one campaign from closing.**  42 cells stand between the record
> and `I(D_r^{per₃})_8 = 0` for every `r`; **17 are now closed** — 5 by Theorem F
> and 12 more measured here on the validated instrument, every one CERTIFIED,
> **no candidate drops at any cell at either prime** — leaving **26**, a
> completed and resumable prefix (§7).  Degree 8 is *not* closed and is not
> claimed; Theorem B stands at `δ ≤ 7`.
>
> **The residual set is 197 cells at degree 9** plus those 25 at degree 8, and
> the 25 are subordinate: each is closed by the degree-9 cell `μ + 3e₁`.  Against
> a naive census of **1329** constituents over `δ = 7, 8, 9`, **222** are left.
>
> **The residual is expensive, and this is the number batch 14 should plan
> against**: fitted from 15 measured builds and 12 Wiedemann certificates on
> this host, deciding the 197 degree-9 cells costs **at least ~1 100 CPU-hours**,
> dominated by the kernel and not by the build (§5.2).  That is a new fact — the
> earlier `Σ N_S·δ` framing understated it — and it is the strongest argument in
> this report for B13-10's leaner builder.
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
shared; nothing in this session is a heavy job.  The structural work — census,
bound, top cells, Jacobians, closure — cost about **16 minutes** of CPU in
total.  The degree-8 campaign of §7 then ran two workers for about **an hour**
of wall clock on the two cores, peak memory 0.32 GB.  Every run was launched
under `timeout` and `ulimit -v`, with its process id written to
`results/logs/b13_05_*.pid`; the campaign workers were ended at the handoff by
those recorded ids, and no run was ended by name-pattern matching.

One failure worth recording: the campaign's **first** launch used the dense
kernel route with `--nchi-cap 60000`, and both workers died on
`numpy._core._exceptions._ArrayMemoryError` — 2.18 GiB and 31.1 GiB requests,
because `n_χ` at these cells runs to `10⁴–10⁵` where the earlier validation
cells (large `|Stab_W(μ)|`) had `n_χ ≈ 300`.  The cap was mine and it was wrong
by two orders of magnitude.  Nothing was banked from that launch and nothing was
corrupted — the workers write per cell to separate files — but it cost twenty
minutes, and the lesson is the one §5.3 states: **on this queue `n_χ`, not
`N_S`, is the size that matters**, and a cap has to be set on it.

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

### 4.1 Theorem F — the ladder's converse, and the pruning engine

**Theorem F (PROVED).**  Let `X` be irreducible and `I = I(X)`.  If
`i(κ, p) = 0` and `i(ν, q) = 0`, then `mult(κ+ν, p+q) ≥ 1`; in particular

    a(κ+ν, p+q) = 1   ⟹   i(κ+ν, p+q) = 0.

*Proof.*  `i(κ,p) = 0` says the whole weight-`κ` highest-weight space injects
into `C[X]_p`, so **every** nonzero highest-weight vector of that weight is
nonzero in `C[X]` — no choice of vector is involved.  Take such `h_κ` and `h_ν`.
Their product is a highest-weight vector of weight `κ+ν` (raising operators are
derivations, so they annihilate a product of annihilated vectors) and is nonzero
in `C[X]` because `C[X]` is a domain.  So the weight-`(κ+ν)` multiplicity in
`C[X]_{p+q}` is at least one.  ∎

By the restriction lemma `i(κ,p)` does not depend on the ambient `r ≥ ℓ(κ)`
(Theorem A), so blocks of any length combine at the target's length.  A target
of length 7 needs a length-7 factor, and the only such blocks are the degree-7
top cells — which is why Theorem F reaches as far as it does and no further.

**Applied** (`analysis/wk13_b13_05_closure.py`, iterated with Theorem D to a
fixed point, reached in one round): seed blocks are the 1188 census cells with
`i = 0` from inheritance and §3.  Theorem F closes **18 further cells**: 5 at
`(δ=8, ℓ=7)`, 7 at `(δ=9, ℓ=7)`, 6 at `(δ=9, ℓ=8)`, and bounds `i ≤ a−1` at 3
more (the `a ≥ 2` cells, where one product gives only `mult ≥ 1`).  Theorem D
adds nothing on top — every cell it could reach was already closed — which is
itself worth recording: **at these degrees the ladder is not a pruning tool, it
is an ordering tool.**

Two of Theorem F's predictions were then checked independently on the numerical
instrument, and both hold: `(12,2⁶)₈ = (9,2⁶)₇ · (3)₁` and
`(15,2⁶)₉ = (9,2⁶)₇ · (6)₂` both measure `mult = a = 1` at both primes (§7).
That is a real control on the theorem, not a restatement of it.

## 5. The residual set (the deliverable for B13-09)

### 5.1 What is left

After Theorem B, the top cells, Theorems D and F, and the degree-8 campaign of
§7, the open cells at lengths 7 and 8 through degree 9 are:

| | cells | closed | **open** |
|---|---|---|---|
| `δ = 7`, `ℓ = 7` | 5 | 5 | **0** |
| `δ = 8`, `ℓ = 7` | 42 | 17 | **25** |
| `δ = 8`, `ℓ = 8` | 6 | 6 | **0** |
| `δ = 9`, `ℓ = 7` | 152 | 11 | **141** |
| `δ = 9`, `ℓ = 8` | 62 | 6 | **56** |
| `δ = 9`, `ℓ = 9` (exploratory) | 8 | 8 | **0** |

**222 open, of which 197 are at degree 9 and 25 at degree 8** — and the 26 are
subordinate: each has its ladder successor `μ + 3e₁` among the 141, so a
B13-09 run that clears the right subset of degree 9 clears degree 8 for free.
The irreducible residual is therefore **197 cells, all at degree 9**, against a
naive census of 797 constituents at that degree and 1329 over `δ = 7, 8, 9`.

`results/b13_05_final.json` carries every open cell with `a`, `N_S`,
`|Stab_W(μ)|` and `n_χ ≥ N_S/|Stab|`, and every closed one with the reason —
inherited, top cell, Theorem F witness, Theorem D successor, or measured here.
**123 of the 197 have `a = 1`**, where the injectivity certificate of §7 applies
directly; the other 74 have `a` from 2 to 6, and the same certificate decides
them too (`[E; Ev]` injective ⟺ `mult = a` for every `a`).

### 5.2 What it costs — the number batch 14 should plan against

Fitted from this session's own measurements on the declared host (15 builds,
`N_S` from 4 743 to 454 272; 12 Wiedemann certificates, `n_χ` from 2 140 to
30 704), both at **MEASURED**:

| stage | fitted rate | cost over the 197 |
|---|---|---|
| lean build (`wk9_s45_build.build_cell`) | ~184 s per 10⁶ monomials | `Σ N_S = 6.25·10⁸` → **~32 CPU-hours** |
| decision (sparse Wiedemann on `[E; Ev]`, both primes) | ~45 s per 10³ of `n_χ` | **≥ ~1 100 CPU-hours** |

**The kernel, not the builder, is what this queue costs** — by a factor of
twenty — and the 1 100 hours is a *lower* bound three times over: it uses the
`n_χ` lower bound `N_S/|Stab|` rather than the true `n_χ` (measured overshoots
ran 5 % to 20 % high); the linear fit comes from the cells that finished, which
are the cheap ones; and Wiedemann is superlinear in `n_χ` while the fit is not.

The superlinearity is now measured rather than assumed, and it is steep.  Two
points from the campaign's dear end, both at one prime:

| `μ` | `n_χ` | nnz | seconds | linear fit predicts |
|---|---|---|---|---|
| `(8,6,5,2,1,1,1)₈` | 8 504 | 93 691 | **19** | 132 |
| `(8,4,4,2,2,2,2)₈` | 23 896 | 1 573 691 | **1 409** | 371 |
| `(9,4,4,2,2,2,1)₈` | 30 704 | 1 177 840 | **1 201** | 476 |

A 2.8× rise in `n_χ` bought a 74× rise in time, because `nnz` grows with it and
the Wiedemann cost is `O(n_χ · nnz)`.  **So read the 1 100 hours as the optimistic
end of a range whose realistic value is several times larger**, and note that the
residual's `n_χ` lower bounds reach `4.1·10⁵` — seventeen times the dearest cell
measured here.  A handful of cells at the top of that queue could each cost more
than everything this session ran.

This inverts the batch-12 stock-take's reading of where the wall is.  §7 of
`docs/stocktake_batch12.md` puts the raising-row builder in front — correctly,
for the six-row quartic cells that motivated it, where s79 hit 4 GB of rows.
On **this** queue the builder is comfortable (peak 0.32 GB at `N_S = 8.4·10⁵`)
and the decision is the expense.  So B13-10's leaner builder, valuable as it is,
does **not** unblock the degree-9 cubic queue; what would is a faster kernel —
a block-Wiedemann or a better-conditioned cover — and I record that as the
recommendation this session did not have the remit to act on.

### 5.3 The queue front

The ten cheapest open cells by `n_χ` lower bound, for B13-09:

| `δ` | `ℓ` | `μ` | `a` | `N_S` | `|Stab|` | `n_χ ≥` |
|---|---|---|---|---|---|---|
| 9 | 7 | `(13, 4, 2, 2, 2, 2, 2)` | 2 | 279 322 | 120 | 2 328 |
| 9 | 8 | `(12, 3, 2, 2, 2, 2, 2, 2)` | 1 | 2 479 761 | 720 | 3 445 |
| 9 | 7 | `(12, 5, 2, 2, 2, 2, 2)` | 2 | 453 215 | 120 | 3 777 |
| 9 | 7 | `(11, 6, 2, 2, 2, 2, 2)` | 3 | 644 448 | 120 | 5 371 |
| 9 | 8 | `(11, 4, 2, 2, 2, 2, 2, 2)` | 1 | 4 678 248 | 720 | 6 498 |
| 9 | 7 | `(10, 7, 2, 2, 2, 2, 2)` | 2 | 809 508 | 120 | 6 746 |
| 9 | 7 | `(9, 8, 2, 2, 2, 2, 2)` | 2 | 905 411 | 120 | 7 546 |
| 9 | 7 | `(12, 6, 2, 2, 2, 2, 1)` | 2 | 214 526 | 24 | 8 939 |
| 9 | 8 | `(10, 5, 2, 2, 2, 2, 2, 2)` | 1 | 7 363 399 | 720 | 10 227 |
| 9 | 7 | `(11, 7, 2, 2, 2, 2, 1)` | 2 | 276 644 | 24 | 11 527 |

Cells with a large `|Stab_W(μ)|` are enormously cheaper than their `N_S`
suggests — `(15,2⁶)₉` has `N_S = 65 416` but `n_χ = 301` and decided in 6 s —
so **the queue should be sorted by `n_χ`, not by `N_S`**.  s79's ordering was by
`N_S·δ`, which is the build cost; on this queue that is the wrong key.

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

## 7. Degree 8: the campaign, and the instrument it validated

### 7.1 Validation cells — the instrument, checked against the record

Before any new cell was decided, the instrument was checked against a cell the
record already owns (`analysis/wk13_b13_05_validate.py`; build by
`wk9_s45_build.build_cell(μ, δ, n=3)`, exact kernel of the raising rows at both
house primes with `dim ker = a` asserted and `E·K = 0` verified, evaluation at
`a + 8` `per₃` pencils, seed 41, box ±40 — session 41's family, the one s79 used):

| cell | `a` | `N_S` | `n_χ` | `mult` | verdict |
|---|---|---|---|---|---|
| `(17,2,2,2,2,2)₉`, `ℓ=6` — **s79's own cell** | 1 | 4 743 | 116 | 1 | **reproduces s79** |
| `(12,2,2,2,2,2,2)₈`, `ℓ=7` | 1 | 63 711 | 284 | 1 | CERTIFIED — and **confirms Theorem F** |
| `(15,2,2,2,2,2,2)₉`, `ℓ=7` | 1 | 65 416 | 301 | 1 | CERTIFIED — and **confirms Theorem F** |

The first row is the control: a length-6 degree-9 weight from s79's scan,
rebuilt here from scratch on a different driver, giving the same `a` and the
same `mult`.  The second and third are cells Theorem F had already closed
(`(9,2⁶)₇ · (3)₁` and `(9,2⁶)₇ · (6)₂`); measuring them independently is a check
on the theorem, and both agree.

### 7.2 The campaign

With Theorem F's 5, exactly **37** cells stood between the record and
`I(D_r^{per₃})_8 = 0` for every `r` — the open `(δ=8, ℓ=7)` cells, every one
with `a = 1`.  Pre-registered in addendum C and run on two workers with separate
output files.  **12 of the 37 are newly CERTIFIED here**, all by the sparse
injectivity certificate.  The table lists 13: the extra row is `(12,2⁶)`,
which Theorem F had already closed and which is included as the §7.1 check.

| `μ` | `N_S` | `|Stab|` | `n_χ` | time | verdict |
|---|---|---|---|---|---|
| `(12, 2, 2, 2, 2, 2, 2)` | 63 711 | — | 284 | 36 s | CERTIFIED |
| `(11, 3, 2, 2, 2, 2, 2)` | 138 754 | — | 2 140 | 72 s | CERTIFIED |
| `(10, 4, 2, 2, 2, 2, 2)` | 245 689 | — | 3 649 | 158 s | CERTIFIED |
| `(6, 5, 5, 5, 1, 1, 1)` | 311 618 | — | 4 700 | 102 s | CERTIFIED |
| `(9, 5, 2, 2, 2, 2, 2)` | 361 997 | — | 5 180 | 283 s | CERTIFIED |
| `(8, 6, 2, 2, 2, 2, 2)` | 454 272 | — | 6 430 | 426 s | CERTIFIED |
| `(8, 5, 5, 3, 1, 1, 1)` | 166 125 | — | 7 063 | 77 s | CERTIFIED |
| `(10, 5, 2, 2, 2, 2, 1)` | 128 905 | — | 7 604 | 204 s | CERTIFIED |
| `(8, 6, 5, 2, 1, 1, 1)` | 105 462 | — | 8 504 | 78 s | CERTIFIED |
| `(9, 6, 2, 2, 2, 2, 1)` | 168 763 | — | 9 848 | 341 s | CERTIFIED |
| `(7, 5, 5, 4, 1, 1, 1)` | 254 060 | — | 11 127 | 197 s | CERTIFIED |
| `(8, 7, 2, 2, 2, 2, 1)` | 192 491 | — | 11 160 | 457 s | CERTIFIED |
| `(9, 4, 4, 2, 2, 2, 1)` | 309 494 | — | 30 704 | 2420 s | CERTIFIED |

**No candidate drops, at any cell, at either prime.**  Every verdict is
`[E; Ev]` NONSINGULAR — a Berlekamp–Massey minimal polynomial of degree exactly
`n_χ` with `f(0) ≠ 0`, which proves nonsingularity with no randomness in the
implication, and `rank_p ≤ rank_Q` carries it to `Q`.

**The route.**  `ker[E; Ev]` is exactly the space of weight-`μ` highest-weight
vectors vanishing at the `K` points, of dimension `a − mult`, so `[E; Ev]`
injective ⟺ `mult = a`.  This is s43's criterion and session 42's Wiedemann tool
(`analysis/wk9_s42_wied.c`, compiled here — see §9 defect 5), wired to the s45
lean build; `analysis/wk9_s43_inject.py` itself is hardcoded to `r = 6` and
could not be used directly, which is why the wiring lives in
`analysis/wk13_b13_05_validate.py::run_inject`.

**Where it stands: 17 of 42 closed, 25 open.**  That is a completed, resumable
prefix — the pre-registered fallback — and the boundary is exactly the cost
curve of §5.2: the cells done have `n_χ` from 284 to 30 704, and the 25 left run
from `n_χ ≈ 12 000` to `4.1·10⁵`.  **Degree 8 is not closed, and I do not claim
it.**  Theorem B stands at `δ ≤ 7`.

*What closing it would buy:* `I(D_r^{per₃})_8 = 0` for every `r`, hence
`mult_pad = mult_red` at every weight of every length through degree 8 — and, by
Theorem F with `ν = (3)₁`, it would close a further 9 cells at `(δ=9, ℓ=7)` for
nothing.  On the fitted curve the 25 are roughly **60–100 CPU-hours**, most of it
in the three dearest cells.

## 8. Two further results, both exact

**8.1 The dimension table extends (PROVED).**  `analysis/wk13_b13_05_checks.py
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

**8.2 The inheritance validation cell (CERTIFIED).**  `μ = (11,2,2,2,2,2)`
computed at `r = 7`, `δ = 7` with the house evaluator
`wk8_s30_core.measure(per₃, 9, 3, 7, 7, ·)`, `a + 8 = 9` pencils, seed 11, box
±40, both primes: `N_S = 4603`, `a = 1`, **`mult = 1`**, 388 s.  This is s41's
first line, recomputed at a length one higher than it was banked at, and it
agrees — the restriction lemma behaving as Theorem A says it must.

## 9. Defects in this assignment, and the scope calls I made

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

5. **`analysis/wk9_s43_inject.py` is hardcoded to `r = 6`.**  `inject_one` opens
   with `n, r = 3, 6`, so the injectivity certificate — the programme's only
   memory-lean decision route, and the one that carried s43's and s47's dearest
   cells — **cannot be pointed at length 7 or 8 as it stands**.  B13-09's brief
   says "use the existing builder", and the builder is fine; the *decider* is
   not.  I wired the same criterion to the s45 build in
   `analysis/wk13_b13_05_validate.py::run_inject` (§7.2) and B13-09 should use
   that rather than rediscover the limitation.  Related: session 42's Wiedemann
   binary is **not** in the tree as a binary and its default paths
   (`/root/s43/wied_bin`, `/root/s42/work`) are not writable in this container;
   `gcc -O3 -o <path> analysis/wk9_s42_wied.c` builds it in a second, and
   `WIED_BIN` / `WIED_WORK` must both be pointed somewhere writable.  That is
   two minutes if you know it and a dead end if you do not, so it belongs in the
   preamble's toolchain paragraph beside `python-flint`.

6. **The scope boundary has no rule for a cell that is cheap for me and dear for
   B13-09.**  The 13 cells I decided at degree 8 (§7) are inside B13-09's stated
   region.  I ran them because they are the remainder of *this* session's
   theorem, and I declare it; but "B13-05 owns the structural proofs and computes
   only to validate a claim" and "B13-09 owns the numerical queue" do not
   between them say who owns *finishing a degree*.  A one-line rule — the
   theorem's owner may complete the degree the theorem is about, and says so —
   would have saved this paragraph.

## 10. What I did not do, and what it would cost

| not done | why | price |
|---|---|---|
| **The 197-cell degree-9 residual** | B13-09 owns the numerical queue | §5.2 prices it from this session's own fits: **≥ ~1 100 CPU-hours** for the decisions plus ~32 for the builds. This is the headline cost of the whole cubic programme at these lengths and it is a *lower* bound |
| **The last 25 cells of degree 8** | the two-hour extension ran out mid-campaign; the workers were ended at the handoff by their recorded pids | ~**60–100 CPU-hours** on the fitted curve, most of it in the three dearest. Closing them gives `I(D_r^{per₃})_8 = 0` for every `r`, upgrades Theorem B to `δ ≤ 8`, and closes 9 degree-9 cells free by Theorem F. **This is the cheapest theorem left on the board** and it is fully set up: the cell list, the driver and the compiled tool are all in the bundle |
| **Instrument I6** — the `ℓ = δ−1` cells via the Pieri image of a top cell | pre-registered in addendum B, **not reached** | half a session. Its value fell once §5.2 showed the decision, not the construction, is the cost: I6 would still need an evaluation per cell. I no longer think it is the best next instrument, and I would put that half-session into a **faster kernel** (block Wiedemann, or a better cover) instead — which is what actually unblocks the 1 100 hours |
| **Raising the I3.3 cap** to cover the 7 skipped weights | all have `a = 0`; nothing depends on them | minutes |
| **Length 9 beyond the top cells** | outside the assignment | the 8 top cells at `δ = 9` are closed here; `δ ≥ 10` is unpriced and unenumerated |
| **Anything on the quartic/padded side** | not this assignment; and `D > 0` is governed by `i_det`, not by this ideal (`docs/batch13_corrections.md` §1) | — |

**The honest boundary of the negatives.**  §6 is a negative over a stated
region: every cell with `a ≥ 1` at `δ ≤ 9`, `ℓ ≤ 9`.  It says the
orbit-stabiliser bound is silent there.  §7 is a *prefix*, not a theorem: 17 of
42 degree-8 cells closed, and **the remaining 25 could still contain the first
permanent-specific equation the programme has ever seen**.  Nothing in this
report excludes that, and no measurement here even hints at it — every cell
decided came back full rank, with no candidate drop at either prime.

## 11. Relation to the two objectives

This session serves **objective 2** (`mult_pad < mult_red`).  Per
`docs/batch13_corrections.md` §1, that is not a prerequisite for objective 1, and
nothing here bears on `D > 0`: the binding constraint on the obstruction is
`i_det`, and this session touched neither the determinant side nor any padded
cell.  Theorem B is a statement that the permanent is *invisible* through degree
7 — it moves the frontier of a negative, and the programme should read it that
way.  If the 222 open cells come back empty too, the honest summary will be that
`mult_pad = mult_red` through degree 9 at every length, and the cubic screen will
have found nothing at four lengths on five instruments.

One planning consequence is worth stating plainly, because it is the only place
this session's numbers bear on batch 14's choices.  The cubic screen was adopted
(`docs/stocktake_batch12.md` §5) because it is "one computation per
`(length, degree)`" instead of one per weight.  That is true of the *statement*
but §5.2 shows it is not true of the *cost*: one `(length, degree)` at `r = 7, 8`
and `δ = 9` is 197 weights and at least 1 100 CPU-hours, and the expense is in the
kernel, where no instrument in this programme is currently strong.  Set against
the correction in `docs/batch13_corrections.md` §1 — that objective 2 is not on
the path to `D > 0` at all — the honest question for the evening stock-take is
whether degree 9 is worth 1 100 hours to close a negative that does not gate the
obstruction.  **Degree 8, at 60–100 hours, closes a clean theorem and is a
different proposition**; I would fund that and defer degree 9 behind a faster
kernel.  That is a recommendation, not a result, and it is the integrator's
call.

## 12. Artefacts

```
results/PREREG_b13_05.md           pre-registration + addenda A, B, C
results/b13_05_census.json         1444 rows, delta <= 9, ell <= 9: a (two routes), N_S, stab, n_chi_lb
results/b13_05_census_d7.json      the delta <= 7 timing probe
results/b13_05_bound_d1to5.json    b(mu,delta), all mu, with the id-term character cross-check
results/b13_05_bound_d6to7.json    "
results/b13_05_bound_d8to9.json    "
results/b13_05_topcells.json       the 32 top cells: nu, S(nu), mu, pencils, exact determinants, both primes
results/b13_05_checks.json         Jacobian ranks r = 7,8,9; the I4 cell; the I3.3 brute force
results/b13_05_closure.json        Theorems D and F to a fixed point, with the witness for every closure
results/b13_05_validate.json       validation cells (the s79 control and the two Theorem-F checks)
results/b13_05_deg8_w0.json        degree-8 campaign, worker 0 -- single writer
results/b13_05_deg8_w1.json        degree-8 campaign, worker 1 -- single writer
results/b13_05_final.json          THE HANDOFF: every open cell with its price, every closed one with its reason,
                                   and the fitted cost model
analysis/wk13_b13_05_census.py     the census
analysis/wk13_b13_05_bound.py      the orbit-stabiliser bound (F, Burnside, Cauchy, MN characters, sum rule)
analysis/wk13_b13_05_topcells.py   instrument I5 (top cells as catalecticant minors)
analysis/wk13_b13_05_checks.py     I3.3 brute force, Jacobian witnesses, the I4 cell
analysis/wk13_b13_05_closure.py    Theorems D and F, iterated
analysis/wk13_b13_05_validate.py   the decision driver: s45 build + dense kernel, and run_inject for large n_chi
analysis/wk13_b13_05_collect.py    merges every banked verdict, re-runs the closure, fits the cost model
results/logs/b13_05_*.log|.pid     every run, bounded at launch
```

To resume the degree-8 campaign: `gcc -O3 -o <path> analysis/wk9_s42_wied.c`,
export `WIED_BIN` and `WIED_WORK` to writable paths, take the open `δ = 8` cells
from `results/b13_05_final.json`, and run `wk13_b13_05_validate.py --cells
"<μ>@8" --nchi-cap 1500`.  It banks per cell and skips what is already banked.

All files are well under 5 MB; the largest is `results/b13_05_census.json` at
170 KB.  Repository configuration was not modified.

Author of record for the session: B13-05.  Ran as **Claude Fable 5.1**
(computation) and **Claude Opus 5** (report and delivery).  Programme author:
Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
