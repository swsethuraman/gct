# B21-01 — The isotropic-type test of the pairing `B` (one pilot)

Worktree `B15-01`, branch `b15-01-ci159`, HEAD `878258f295dd5a6b306137fadaab816ce0deb3df`
(tree `eb32dbebf0c4f45fb196809cbae0ef52fc658d7b`). Read-only git; no commit, no push.
Phase 2 slot (a), released by B21-10 R24. `b21_10_review.md` §2 and R2–R7, R11 were read first; the
control's normalisation is used in B21-10's corrected form `det(g)^{-4}`, and Corollary A.1's
"both give, in addition, the degree-12 value" is not used.

## 0. Plain terms, and the verdict

`q_3`, `q_7`, `n02` each factor as a pairing `B` of two-column covariants. The degree-12 part of each
is `B(top, top)`, the degree-11 part is `B(top, mixed) + B(mixed, top)`. The pairing `B` lives on
`Λ²A ⊗ Λ²B` and, because `dim A' = dim B' = 3`, it is isotropic in a precise sense: it pairs the four
type components `X_{11}, X_{12}, X_{21}, X_{22}` only crosswise, `X_{11}` against `X'_{22}` and
`X_{12}` against `X'_{21}`. B20-01 §4.5(c) asked the cheap question this makes possible: **do the tops
and mixed parts of the four covariants have so few nonzero type components that the degree-11 relation
becomes automatic?** One wrapped pilot answers it by computing those components.

**VERDICT — the mechanism is CLOSED.** No type component of any top `t_i` or mixed part `s_i` vanishes: 32 blocks at 5 flag-locus points, all nonzero. The degree-11 relation is nonzero in each of the four type components separately and vanishes only in their sum. The isotropic structure of `B` therefore does not force the relation, and the mixed-pairing identity stays OPEN with O4's premises and price unchanged (§4, §5). Every control passed, including the G21 sealed replay (6 of 6) and a runner cross-check of the identity itself (6 of 6).

Nothing here is a gap, a cell, an equation nonzero on padding, or a separation. Everything this
session computes is producer-only (G18): one lineage, one session, no independent replay.

## 1. Pre-registration (written and saved before any run)

### 1.1 The type decomposition, the projectors, and the 256-vector layout

`W = A ⊗ B = Mat_4`; `A = C e_0 ⊕ A'` with `A' = <e_1, e_2, e_3>`, and `B = C f_0 ⊕ B'` likewise, in the
adapted coordinates of B18-02 §1 (`a = Y[0][0]`, `r = Y[0][1:]`, `c = Y[1:][0]`, `3×3` block
`Σ + A(v)`, `A(v)_{ij} = −ε_{ijk} v_k`, `ν_k := A(e_k)`).

A half-tensor `X_H` is the **256-vector** `X[a_1, a_2, b_1, b_2]`, `a_i ∈ A`, `b_i ∈ B`, produced by
`direct_arc` §B.1: sum (2.1) over every index of the two columns of one half of the pairing except the
`a`-legs of the two leftover `π`-slots and the `b`-legs of the two leftover `ρ`-slots. The pairing is

    B(X, X') = Σ ε_A[a_1 a_2 a_3 a_4] ε_B[b_1 b_2 b_3 b_4] X[a_1,a_2,b_1,b_2] X'[a_3,a_4,b_3,b_4].

Only the `Λ²A ⊗ Λ²B` part survives, so the **projector** is the double antisymmetrisation
`L(X)[p, q] = X[p_0,p_1,q_0,q_1] − X[p_1,p_0,q_0,q_1] − X[p_0,p_1,q_1,q_0] + X[p_1,p_0,q_1,q_0]`
over an `A`-pair `p = (p_0 < p_1)` and a `B`-pair `q = (q_0 < q_1)`. `Λ²A = (e_0 ∧ A') ⊕ Λ²A'`:
**type 1** is `e_0 ∧ A'`, with pairs `(0,1), (0,2), (0,3)`; **type 2** is `Λ²A'`, with pairs
`(2,3), (1,3), (1,2)` listed so that `TYPE2[i]` is the complement of `TYPE1[i]`. So `L(X)` is a
`2 × 3 × 2 × 3` array whose four `3 × 3` blocks are `X_{11}, X_{12}, X_{21}, X_{22}` (first index the
`A`-type, second the `B`-type).

Because every partition of `{0,1,2,3}` into two pairs has exactly one pair of each type, regrouping the
`ε`-sums gives, with `s_i := ε[TYPE1[i] ⌢ TYPE2[i]]` and
`<U, V> := Σ_{i,j} s_i s_j U[i,j] V[i,j]`, the **four-term type formula** of §4.5(c) (C7):

    B(X, X') = <X_11, X'_22> + <X_12, X'_21> + <X_21, X'_12> + <X_22, X'_11>.

The pilot computes `B` **both** ways — by the einsum definition and by this formula — on every pair it
uses at the general point and at flag point 0, and records whether they agree. That is the C7 replay.

### 1.2 Extraction of `t_i` and `s_i` at a flag-locus point

A flag-locus point is an `F_1`-tuple of Theorem A: `(Z_1, Z_2, Z + u ν_1, u ν_2, u ν_3)` with
`Z_1, Z_2, Z ∈ W'`. There `D = u²·(Z_1∧Z_2∧Z∧ν_2∧ν_3) + u³·(Z_1∧Z_2∧ν_1∧ν_2∧ν_3)` — **two** terms
only — and a half-tensor is quadratic in `D`, so `X_H(u) = u⁴ X^{(4)} + u⁵ X^{(5)} + u⁶ X^{(6)}`.
Hence `t := X^{(6)}` and `s := X^{(5)}` are recovered from **three** nodes `u = 1, 2, 3` by a
Vandermonde solve in degrees `(4, 5, 6)`, applied to the 256-vector. (Theorem A's five nodes and
degrees `8..12` are the quartic statement; a half is quadratic, so three nodes suffice for it. The
runner cross-check below does use the five nodes.) `det(g)^{-4}` is the normalisation that carries a
slice value back to the full row (B21-10 R3/R4); it enters this report only in the G21 sealed replay,
because the relation being tested is homogeneous and a common factor cannot change whether it holds.

**The four covariants** are the four distinct half-patterns: `Φ_1 := X_{q3_h1}`, `Φ_2 := X_{q3_h2}`,
`Φ_3 := X_{q7_h1}`, `Φ_4 := X_{n02_h1}`; `direct_arc` C.1 records `Φ_4 = −Φ_1` exactly at the general
point, so `Φ_4` is carried as a control, not as a fourth direction. `t_i, s_i` are the degree-6 and
degree-5 parts of `Φ_i`.

### 1.3 The relation, and the coefficients

`(α, β) = (265391, 275398)` mod `P = 524287`, from `routeA` §5.3 as replayed in `arc_target` C3 and
`direct_arc` C.2. The pilot records that the degree-12 rows alone **under-determine** `(α, β)` — they
are rank 1 with ratios `101007`, `295818`, one equation in two unknowns — and checks that the recorded
pair satisfies that one equation. The identity tested is

    4 B(t_1, s_1) = α·2[B(t_1,s_2) + B(s_1,t_2)] + β·2[B(t_3,s_2) + B(s_3,t_2)]    (`Φ`-form),

and, independently of `direct_arc`'s one-point coordinate identification, the same relation written
with all twelve halves, `z^{[n]}(q) = B(X_{h1}, X_{h2}) + B(X_{h1t}, X_{h2t})` graded (**direct form**).
Both are computed at every point and compared; the `Φ`-form's validity away from the general point is
itself an open question, and the run answers it.

### 1.4 Points

Flag point 0 is the slice form of the **pinned P6 point 0** (Theorem A(ii) applied to
`p6_basis.json`'s `points_entries[0]`), so that the sealed values control it. Then at most four further
**seeded** flag-locus points: `(Z_1, Z_2, Z)` drawn from `numpy.random.default_rng(20260918)` mod `P`
and projected into `W'`. Two-column tests decide nothing about `ker C`, and no minor computed here is
evidence about `rank(C|_U)` beyond what the relation residuals say.

### 1.5 Predicted outcome — honestly, with no derivation claimed

I predict **no type component of any `t_i` vanishes**, and I expect the same for the `s_i`. The reason
is not a derivation: `direct_arc` §B.4 already showed, exactly, that *no* isotypic component of
`ν_1∧ν_2∧ν_3∧Z_1∧Z_2` vanishes identically on `S*`, and the tops are restrictions of covariants to that
locus; a vanishing type block would be a strictly stronger coincidence than the one already refuted.
I therefore predict the mechanism is **closed**, i.e. transcription sentence 2. I attach no confidence
to the `s_i` half of that prediction — the degree-5 part lives on the larger loci `S**_{kl}` and I have
not looked at it before.

I pre-register one further branch the three sentences do not cover: **the relation may simply fail**
at a seeded flag point. By Theorem A(v) that would close the identity negatively — `rank(C|_U) = 3` —
which is B20-01 §8's reopening condition (b), not (c). If that lands I will say so in §4 as its own
finding, and still transcribe the sentence that fits what the type components did.

### 1.6 The three transcription sentences (one is copied verbatim into §4)

1. **Mechanism found.** *A named type component vanishes identically on the relevant pairs and forces
   the degree-11 relation. What would be needed to make this PROVED is not a sample but a proof that
   the component vanishes as a function on the locus — a `G'`-equivariance or weight argument on
   `S*` and `S**_{kl}` of the kind `direct_arc` §B.5 supplies for the tops — after which the relation
   follows from the four-term formula by algebra, O4 becomes unnecessary for the degree-11 identity,
   and the price of `1050` (or `840`) evaluations is not incurred.*
2. **Mechanism closed.** *The type components do not vanish, or vanish without implying the relation.
   The mixed-pairing identity stays OPEN exactly as B20-01 §8.3 left it; O4's premises (Theorem A,
   Proposition C) are unchanged and its price is unchanged; the scope of this finding is the four
   covariants' type blocks at the points evaluated here and nothing else.*
3. **Inconclusive within one pilot.** *What is missing is stated: which quantity was not reached,
   why the budget or a failed control stopped it, and what the next pilot would have to evaluate.*

## 2. Method

One wrapped pilot, `b21_01_p1_type_test`, 60 s / 512 MiB, `PYTHONDONTWRITEBYTECODE=1`, launched only
with `Get-Process python*` empty. Stages, each written to `results/b21_01/p1_type_test.json` as it
completes, with a 52 s internal deadline and a guard before each point:

0. **Pins (G9/G10) and the G21 sealed replay.** `paired_runner.py` and `b18_02_carrier.py` fetched by
   commit and path with read-only `git show`, hash-checked, and materialised under
   `results/b21_01/pinned/` — **not** under `results/b20_01/`, which this session does not write; the
   patched runner's hash is compared with the one B20-01's `MANIFEST.json` binds. `p6_basis.json` at
   `82633a60`; the three G8 certificates and `p2_reduction.json` read locally against the hashes in
   B20-01's manifest. Then the six sealed rows `(86170, 71919, 226580; 376209, 469277, 41046)` are
   recomputed from pilot 2's recorded slice values with `det(g)^{-4}`, and the count is emitted (G16).
1. **C7 replay.** `B` by einsum versus the four-term type formula on every pair used at the general
   point and at flag point 0; count emitted.
2. **Factorization control** (`direct_arc` §B.1): the twelve halves at the general P6 point 0 recombine
   through `B` to the sealed `260975, 301718, 386346`. This is the control on my own half-tensor
   implementation, which is written fresh here (`analysis/b21_01_types.py`) rather than imported.
3. **Flag point 0**: `t` and `s` of the twelve halves by the three-node extraction of §1.2; the four
   type blocks of each, their ranks, which are zero; the relation in both forms; the residual split
   into its four type contributions; the eight pairings `B(t_i, s_j)`, `B(t_i, t_j)` by type.
4. **Runner cross-check at flag point 0**: `[u^11]` and `[u^12]` of `q_3, q_7, n02` by the pinned runner
   at the five nodes (15 evaluations) against the covariant route of stage 3. This is the G21 control
   in its strongest form — the control is the identity it tests, computed twice by different routes.
5. **Up to four further seeded flag points**, same treatment.

## 3. Results (copied from `results/b21_01/p1_type_test.json`; nothing here is typed from memory)

**Controls, all passed.** Counts are the script's own (G16).

| control | count | outcome |
|---|---|---|
| G21 sealed replay, `det(g)^{-4}` on pilot 2's recorded slice values | 6 of 6 matched | `86170, 71919, 226580`; `376209, 469277, 41046` — exact. `det(g)^{-4} = 252079`; `det g = 199728` recomputed, equals pilot 2's |
| factorization control at the general P6 point 0 (`direct_arc` B.1) | 3 of 3 matched | `260975, 301718, 386346` — my fresh half-tensor reproduces the sealed values |
| C7 four-term type formula vs. the `einsum` definition | 24 pairings | equal in all 24 |
| runner cross-check at flag point 0 (15 runner evaluations, five nodes) | 6 of 6 matched | `[u^11] = 167233, 394903, 212528`, `[u^12] = 462650, 139666, 319220`, equal to the covariant route |
| patched runner's sha256 vs. the one B20-01's `MANIFEST.json` binds | 1 | equal (`e7ba4ff7…`) |

**The type components — the pre-registered question.** Five flag-locus points: the slice form of the
pinned P6 point 0, then four seeded points. For each of the four covariants and for both `t` and `s`,
all four type blocks were tested for vanishing at every point: **20 of 20 nonzero in every one of the
eight cases** (`t(Φ_i)`, `s(Φ_i)`, `i = 1..4`). `type_blocks_zero_at_every_point` is empty for all
eight; `any_type_block_identically_zero` is `false`.

The `3 × 3` block ranks are the same at all five points:

| part | `X_11` | `X_12` | `X_21` | `X_22` |
|---|---|---|---|---|
| `t(Φ_1)`, `t(Φ_2)`, `t(Φ_3)`, `t(Φ_4)` | **2** | 3 | 3 | 3 |
| `s(Φ_1)`, `s(Φ_2)`, `s(Φ_3)`, `s(Φ_4)` | 3 | 3 | 3 | 3 |

**The relation.** The degree-11 residual `z^{[11]}(n02) − α z^{[11]}(q_3) − β z^{[11]}(q_7)` at
`(α, β) = (265391, 275398)` is **`0` at all five points**, in the direct twelve-half form and in the
`Φ`-form; the degree-12 residual is `0` at all five too. The two forms agree on all six values at all
five points, and `Φ_4 = −Φ_1` in both the top and the mixed part at all five — so `direct_arc` C.1's
one-point coordinate identification survives every point tested here. The relation also holds, `0`,
on the runner-route values at flag point 0, which is the same statement computed by a second route.

**But the relation does not hold type by type.** The residual split into its four type contributions
is nonzero in every component at every point, summing to `0` only in the total. Degree 11, direct form:

| point | `11×22` | `12×21` | `21×12` | `22×11` | total |
|---|---:|---:|---:|---:|---:|
| `P6_point_0_slice` | 431076 | 522461 | 435486 | 183838 | **0** |
| `seeded_1` | 460697 | 371310 | 472481 | 268373 | **0** |
| `seeded_2` | 138866 | 407359 | 119275 | 383074 | **0** |
| `seeded_3` | 102457 | 290369 | 399091 | 256657 | **0** |
| `seeded_4` | 472053 | 31341 | 208841 | 336339 | **0** |

The same is true in degree 12, where the rank-1 phenomenon is already recorded: every type component
of that residual is nonzero at every point (with `12×21 = 21×12` throughout, as the symmetry of
`B(t, t')` requires), and only the sum vanishes.

## 4. Transcription sentence, and exact scope

Sentence **2** of §1.6 is transcribed verbatim:

> **Mechanism closed.** *The type components do not vanish, or vanish without implying the relation.
> The mixed-pairing identity stays OPEN exactly as B20-01 §8.3 left it; O4's premises (Theorem A,
> Proposition C) are unchanged and its price is unchanged; the scope of this finding is the four
> covariants' type blocks at the points evaluated here and nothing else.*

The run lands on the **first** disjunct and adds a sharper second one: not one of the thirty-two
tested blocks vanishes, and the four type contributions to the relation are individually nonzero and
cancel only in the sum. So the isotropic structure of `B` does not localise the identity — it neither
forces it nor is available to prove it — and the mechanism B20-01 §4.5(c) hoped for is not there. The
pre-registered prediction of §1.5 was correct for the `t_i`, and correct for the `s_i` as well, where
I had claimed no confidence.

**Scope.** This is five points, one prime `P = 524287`, one session, one lineage — **producer-only**
(G18). "No type block vanishes" is MEASURED at those five points, not proved as a statement about
functions; a block that vanished identically would have had to vanish at all five, so the negative
direction is the strong one and the positive direction was never available from sampling. The rank-2
pattern of `X_11` on the tops is MEASURED at five points and is not claimed as a theorem (G22/G23 do
not arise: no interpolation claim and no dimension inequality is made here). Two-column tests decide
nothing about `ker C`, and this report claims nothing about it. Nothing here is a gap, a cell, an
equation nonzero on padding, or a separation.

**What the run does add, stated at its evidence level.** The degree-11 relation held at four flag-locus
points that no previous packet evaluated, one of them cross-checked against the pinned runner. That
raises the sampled evidence for the identity; it does not certify it. `F_1` functionals span the
70-dimensional `V_70` of Proposition C, so five points are far from an injective evaluation set, and
the missing theorem of B20-01 §5.1 is untouched. The pre-registered fourth branch of §1.5 — the
relation failing, closing the identity negatively — did **not** occur.

## 5. Ledger

| id | statement | label | method |
|---|---|---|---|
| B21-01.1 | Session state as §0; HEAD `878258f2`, tree `eb32dbeb`, read-only git, no commit | VERIFIED | REPLAY |
| B21-01.2 | The six sealed rows are reproduced from pilot 2's recorded slice values with `det(g)^{-4}`, 6 of 6 | REPLAYED (G21); confirms B21-10 R4 | REPLAY |
| B21-01.3 | A freshly written half-tensor reproduces the sealed general-point values `260975, 301718, 386346` | PASSES | REPLAY |
| B21-01.4 | The four-term type formula of §4.5(c) equals the definition of `B` on all 24 pairings tested | C7 REPLAYED | INDEPENDENT (two evaluations of `B`) |
| B21-01.5 | Covariant route and pinned-runner route agree on `[u^11]`, `[u^12]` at flag point 0, 6 of 6 | PASSES | REPLAY (two routes) |
| B21-01.6 | **No type block of `t_i` or `s_i` vanishes**, at any of the five points, for any of the four covariants (32 blocks × 5 points) | **MEASURED negative** | producer-only |
| B21-01.7 | **The degree-11 relation is nonzero in each of the four type components and vanishes only in their sum**, at all five points; likewise in degree 12 | **MEASURED** | producer-only |
| B21-01.8 | **The §4.5(c) mechanism is CLOSED**: the type structure of `B` does not force the relation. The mixed-pairing identity stays OPEN; O4's premises and price unchanged | ruling, from .6 and .7 | — |
| B21-01.9 | The degree-11 and degree-12 relations hold at five flag-locus points, four of them new | MEASURED, evidence only | producer-only |
| B21-01.10 | `Φ_4 = −Φ_1` in top and mixed part, and the `Φ`-form agrees with the twelve-half direct form, at all five points | MEASURED; extends `direct_arc` C.1 beyond its one point | producer-only |
| B21-01.11 | `X_11` of every top has rank 2 and every other block rank 3, at all five points | MEASURED regularity; **open lead**, not a claim | producer-only |
| B21-01.12 | The degree-12 rows alone under-determine `(α, β)` — one equation, two unknowns; the recorded pair satisfies it | VERIFIED | REPLAY |
| B21-01.13 | Two wrapped launches, 25.98 s of 180 s; exits 1 then 0; the exit-1 was my own bug (a dropped reshape), relaunched under a new name, receipt kept; no cap hit; no unwrapped numerical run | MEASURED | — |

## 6. Resources, receipts, manifest

| run | wrapped | exit | wall | peak job memory | receipt |
|---|---|---|---|---|---|
| `b21_01_p1_type_test` | yes (60 s / 512 MiB) | **1** | `1.451 s` | `109.7 MiB` (114982912 B) | `results/logs/b21_01_p1_type_test_resources.json`, `.pid` (pid 39336) |
| `b21_01_p1r_type_test` | yes (60 s / 512 MiB) | 0 | `24.530 s` | `294.1 MiB` (308387840 B) | `results/logs/b21_01_p1r_type_test_resources.json`, `.pid` (pid 26216) |

Wrapped budget `25.98 s` of `180 s`; **two** launches of the permitted three; **no cap hit** (the
larger peak is 57% of the memory cap, the longer wall 41% of the wall cap). The first launch died at
1.45 s on my own bug — `analysis/b21_01_types.py` balanced the column tensor but did not reshape it
from `(16,)*5` to `(4,4)*5`, so the ten labels did not match the five axes and `np.tensordot` raised
`ValueError: shape-mismatch for sum`. The fix is the new `col_arr`; no other line of the computation
changed. Its receipt is kept and is bound by the manifest. **No unwrapped numerical run** (G19 as
B21-10 R22 defines it): the only unwrapped commands were read-only `git`, `Get-Process`, `Get-FileHash`
and the manifest/seal script. `PYTHONDONTWRITEBYTECODE=1` on both launches; `Get-Process python*` empty
before each.

Work done by the successful run, from its own counters: 192 half-tensor evaluations (15.362 s),
15 runner evaluations (6.774 s), 31 column tensors, 5 flag-locus points, 24 `B`-pairings checked two
ways, 24.471 s elapsed against a 52 s internal deadline — no stage was skipped and `log` is empty.

**Inputs (G9/G10), hash-pinned in the pilot's own output.** `paired_runner.py` `33c81c96…` and
`p6_basis.json` `aaee6ec0…` and `n02_definition.json` `ffeead80…` at commit `82633a60`;
`b18_02_carrier.py` `8670040e…` at `75ddb900`; the three G8 certificates `ac93ff59…`, `07d066b8…`,
`34900ea6…` and `p2_reduction.json` `6aa3e283…` read locally against the hashes B20-01's
`MANIFEST.json` (`0e5fd026…`) binds. The pinned runner and carrier are materialised under
`results/b21_01/pinned/`: **nothing under `results/b20_01/` was written**, and the patched runner's
hash equals the one B20-01 binds. That non-modification is verified, not asserted: after sealing, all
20 files B20-01's `MANIFEST.json` binds were re-hashed against it — 20 checked, 0 mismatches.

`results/b21_01/MANIFEST.json` binds every file of this packet with sha256 and byte count, together
with the pinned-input hashes the pilot recorded; `results/b21_01/SEAL_LOG.txt` prints every count it
writes. The report does not name its own hash. The hash table is in `SEAL_LOG.txt`.

**Deviations.** (1) Two launches, not one: the first was my own crash, which the constraints allow
under a new name with the receipt kept. (2) The pilot materialises the pinned runner and carrier under
`results/b21_01/pinned/` rather than reusing B20-01's copies in place, so that the sealed packet is not
written to; the bytes are identical and the equality is recorded. (3) The manifest binds the two
receipts as well as the step-4 files. (4) `MANIFEST.json` and `SEAL_LOG.txt` are not bound by
`MANIFEST.json`. (5) This report is over the 200-line guide; §§0–2 were written and saved before the
run and were not compressed afterwards, because editing a pre-registration after seeing the result is
worse than an overrun.
