# B26-10C: independent review of the Astra results A26-01 and A26-03

**REVIEWER ONLY / UNCOMMITTED.** Cross-lineage review: Claude (Opus 5.5) reviewing packets produced
by Astra. I produced neither packet. Zero pilots and zero mathematical programs. Every
mathematical check below is a hand derivation or a READ of committed bytes.

| packet | registered outcome here | scope |
|---|---|---|
| A26-01 (producer outcome 2, scoped containment) | **ACCEPT** | Theorem A exactly as stated: the symmetric padded family `S` lies in `D`, so every five-center (indeed every) coefficient equation vanishes on `S`. Nothing about general padding `P`. |
| A26-03 (producer outcome 3, rejection) | **ACCEPT** | The one redesign is admissible, highest-weight, nonzero and sees `B²`, and it is strictly positive on the literal determinant `Q²`. It is therefore not a determinant equation. Its padding value remains unresolved. |
| Integrator's general reading of A26-03 (typed question, Part 2 item 4) | **REPAIR** | True for single fully paired contractions after two wording repairs (§2.4): positivity needs the two copies in each pair to be in the same order (otherwise the value is nonzero but carries a global sign); and "signed columns" should read "signed linear combinations". It covers the old expander family at `n = 4`. |

**Achievement levels.** Neither packet reaches a coefficient equation that is nonzero on padding.
A26-01 is scoped geometric containment/no-go. A26-03 is a visible nonzero coefficient function plus
a rejection certificate. There is no source condition, no separation on padding, no positive
multiplicity gap and no asymptotic lower bound. A25-10's programme decision stays "no construction
ready." **No five-row determinant equation is known to be nonzero on padding.**

## 0. Preflight and bindings

| item | observed |
|---|---|
| start (UTC) | 2026-09-23T02:50:37Z |
| worktree / branch | `work/batch15_workers/B15-10`, `b15-10-portable-witness` |
| HEAD | `901b0fe656b941e41ba8e7a045611ba971e03329`. This is exactly the expected PART 19 commit, not a descendant. |
| `git status --porcelain` | two pre-existing untracked files, `results/logs/b15_10_runtime_native_20260913.pid` and `…_resources.json`. Left alone. |
| output paths | `docs/b26_10c_review.md` and `results/b26_10c/` were both absent before writing |
| AGENTS.md / CLAUDE.md | none in the worktree |
| `B26_COMMON.md` raw SHA-256 | `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` (matches the launch-protocol table) |
| `B26-10C.md` raw SHA-256 | `0d5d4fcd85bb47180393ac2b5bedff547d394fbc1c6f604bb6e06353f756cc4b` (matches the launch-protocol table) |
| `BATCH26_LIVE_LEDGER.md` raw SHA-256 | `8260cd3772c5208960b941d6243962e0e42012317f173dc48c68f28ac231de14` |
| A26-03 content commit | `git log batch15-launch -- results/a26_03/MANIFEST.json` returns exactly one commit: **`f7967d17935d6256e7744f6457b45a3787b6940f`** (PART 23B) |

**Manifests.** A26-01's `MANIFEST.json` at `7464a2bd` has SHA-256 `983328d6…65f3` and A26-03's at
`f7967d17` has `23698789…0a46`. Both match the brief. Both manifests contain CRs (119 and 47), and
both files are committed `-text`, so each hash names the committed blob, which equals the raw
bytes. Every other input I relied on is LF-only, so its blob hash equals its raw hash. The full
list is in `results/b26_10c/INPUT_BINDINGS.md`.

The brief's header reads "Integrator draft, 2026-09-23", while `LAUNCH_PROTOCOL_B26.md` lists its
hash. The hash matches, so I treat this as the adopted brief.

---

## Part 1: A26-01

### 1.1 Identity (C): CONFIRMED (hand derivation)

Take `M_u = [a d e; −d b (u−1)f; −e −(u+1)f c]`. The six Leibniz terms `sgn σ · Π m_{iσ(i)}` are:

| σ | term |
|---|---|
| id | `abc` |
| (12) | `−m12 m21 m33 = −d(−d)c = cd²` |
| (13) | `−m13 m22 m31 = −e·b·(−e) = be²` |
| (23) | `−m11 m23 m32 = −a(u−1)f·(−(u+1)f) = (u²−1)af²` |
| (123) | `m12 m23 m31 = d(u−1)f(−e) = −(u−1)def` |
| (132) | `m13 m21 m32 = e(−d)(−(u+1)f) = (u+1)def` |

These match PROOF §2's list. The sum is `abc+be²+cd²+(u²−1)af²+2def`.

For the permanent of `A_sym = [a d e; d b f; e f c]`, the six terms are:

- `abc`;
- the transpositions give `cd²`, `be²` and `af²`;
- the two 3-cycles give `def` each.

The sum is `abc+af²+be²+cd²+2def`. The difference, times `l` (because
`det diag(l,M) = l·det M`), is `(u²−1−1)·l·a·f² = (u²−2)·l·a·f²`. This is (C) exactly.

A remark, not needed for acceptance (hand derivation): the scalar `√2` is forced for any entrywise
scaling of a symmetric pattern. Suppose `det(A_sym ∘ ε)` equals `per A_sym` for a scaling `ε` with
unit diagonal. Then `ε_ij·ε_ji = −1` for each pair. The two 3-cycle products `x` and `y` then
satisfy `x + y = 2` and `xy = −1`, so `x = 1 ± √2`. `M_u` has `x = 1−u` and `y = 1+u`.

### 1.2 Admissibility: CONFIRMED (READ plus hand derivation)

READ from A25-05 `STRUCTURAL_MAP.md` §1 at `eb53b97c`: `P = closure{l·per_3(A(x))}`, with `l`
and all nine entries of `A` arbitrary linear forms.

In the row order `(z, A11, A12, A13, A21, A22, A23, A31, A32, A33)`, the rows
`(l,a,d,e,d,b,f,e,f,c)` impose exactly `A12=A21`, `A13=A31` and `A23=A32`. That is a linear
restriction of the 50-parameter substitution. PROOF §1 says explicitly that no equality with the
product locus `{lC}` is assumed, and none is used.

A25-04's integer witness (READ, `81967dde` report and `CONSTRUCTION_AND_PROOF.md` §4) is
`z = x1` with matrix `[[x1+x5,x2,x3],[x2,x1−x5,x4],[x3,x4,x1]]`. That is `s = 0` of A26-01's `F_s`.
So the report's "covers every fixed variable change of A25-04's old witness" holds.

### 1.3 Kernel: CONFIRMED against A25-05

READ from A25-05 `STRUCTURAL_MAP.md` §1 table, row `m = 5`, and `FIVE_CENTER_REDUCTION.md` §1: the
omitted space is `K_5 = span{q_i = Π_{j≠i} x_j}`.

Hand check: `E_5` consists of the `α` with some `α_i ≥ 2`. Its complement among degree-4
exponents in five variables is the squarefree quartics, and there are `C(5,4) = 5` of them. So
`|E_5| = 70 − 5 = 65 = 15·5 − C(5,2)`. A26-01's statement agrees with A25-05's committed text.

### 1.4 Map factorization and descent: CONFIRMED (hand derivation)

`R_u` is linear over `K = Q(√2)`: its entries are `±` the input forms and `(u∓1)f`. Also
`φ(R_u(q)) = det diag(l, M_u) = l·det M_u`. Reducing (C) modulo `u² − 2` gives `π∘φ∘R_u = s`
over `K[q]`, which is (F). Pulling back gives `s* = R_u*∘φ*∘π*`, so `h ∈ ker(φ*π*)` implies
`s*(h) = R_u*(0) = 0`. That is (I), for every `h` in the whole coefficient ring.

`h|_Y = 0` is equivalent to `h∘π∘φ = 0` as a polynomial, because `Y` is the closure of `π(D)`,
`D` is the closure of `im φ`, and the field is infinite.

Descent: for rational `h`, the polynomial `s*(h)` lies in `Q[q]`. Its image in `K[q]` is 0. The
map `Q[q] → K[q]` is injective, because it is base change along the field extension `Q ⊂ K`,
which is free with basis `{1, √2}`. So `s*(h) = 0`. No denominators appear anywhere.

### 1.5 Closure: CONFIRMED (hand derivation)

`S_lit ⊂ im φ ⊂ D`, and `D` is closed, so `S ⊂ D`. Since `π` is continuous,
`π(S) ⊂ π(D) ⊂ closure(π(D)) = Y`, and `Y` is closed, so `closure(π(S)) ⊂ Y`. Closedness of
`π(D)` is never used. This matters, because A25-05 §1 proves that `K_5 ⊂ D`, so properness of the
projection is not available.

### 1.6 Visibility control: CONFIRMED (hand derivation)

Take `l = x1`, `a = x1+x5`, `b = x1−x5`, `c = x1`, `d = x2+s·x1`, `e = x3`, `f = x4`. Expanding
`x1·(abc+af²+be²+cd²+2def)` gives:

`F_s = (1+s²)x1⁴ + 2s·x1³x2 + x1²x2² + x1²x3² + x1²x4² − x1²x5² + x1x5(x4²−x3²) + 2x1x2x3x4 + 2s·x1²x3x4`.

The four coefficients used are:

- `c_(4,0,0,0,0) = 1+s²`;
- `c_(2,0,1,1,0) = 2s`;
- `c_(2,2,0,0,0) = 1`;
- `c_(2,0,0,0,2) = −1`.

At `s = 0` this is A25-05's `F_T`, as READ.

`h_star = c_(4,0,0,0,0)⁴ · c_(2,0,1,1,0)² · c_(2,2,0,0,0) · c_(2,0,0,0,2)`. It has degree 8 and
weight `(16+4+2+2, 2, 2, 2, 2) = (24,2,2,2,2)`, and every exponent has a part `≥ 2`, so
`h_star ∈ H`. Its value is `(1+s²)⁴·4s²·1·(−1) = −4s²(1+s²)⁴`, which is `−64` at `s = 1`.

For the old matrix `N = [a d e; −d b f; −e −f c]`, the two 3-cycle terms are `−def` and `+def`.
So `det N = abc+af²+be²+cd²`, and `F_s − x1·det N = 2x1x2x3x4 + 2s·x1²x3x4`. Also
`h_star(x1·det N) = 0`, because its `c_(2,0,1,1,0)` vanishes.

The label "not a determinant equation" is correct: `F_1 = det diag(x1, M_√2) ∈ im φ` and
`h_star(F_1) = −64 ≠ 0`, so `h_star ∉ I(Y)`. The packet presents it only as a visibility control.
The claimed basis element `c_(4,0,0,0,0)⁶ c_(0,2,2,0,0) c_(0,0,0,2,2)` also has weight
`(24,2,2,2,2)`.

### 1.7 Exclusions: CONFIRMED, row by row against the committed statement cited (READ)

| EXCLUSIONS row | committed text read | agreement |
|---|---|---|
| B22-02 L1 (§1.1) | `e22a41b1:docs/b22_02_report.md` §1.1, ledger row L1 | yes: the direction of semicontinuous thresholds is stated as in §1.1 |
| L2 (Lemma 1.2) | same, Lemma 1.2 | yes |
| L3 (Lemma 1.3), B22-10 caveat | Lemma 1.3; L3 row "instance rests on … CERTIFIED exact ranks" | yes: A26-01 restricts it to specified-minor extraction and does not claim every kernel construction |
| L4 (Lemma 1.4(a)–(c)) | Lemma 1.4 | yes: invariants vanish on `P5`; a cubic covariant sends `lC` to `l²·m` |
| L5 (Lemma 1.5) | Lemma 1.5 | yes: vacuous for `N ≤ 8` |
| L6 (Lemma 1.6) | Lemma 1.6 and ledger L6: "right-way clause CONDITIONAL…; `onset I(D35) ≥ 8` ADOPTED" | yes: the statuses are kept. A26-01's closing sentence ("every selected cubic in the literal det3 image") follows from 1.1, since `per A_sym = det M_√2` is a 3×3 linear determinant |
| GKZ corrected scope | `82633a60:…/scope_corrigendum/REVISED_VERDICT.md` | yes: all-`k` first-differential rank thresholds at 5 and 16 variables, plus the two 16-variable second-differential cases; not all GKZ methods |
| A25-02 Application 3 | `5007de86:results/a25_02/APPLICATIONS.md` §3 and the report line 42 | yes. The committed text says "floor is a historical CERTIFIED-modular input" and "the uniform ceiling is proved". A26-01 writes "determinant floor 299 is historical CERTIFIED-modular evidence" and does **not** say "premise-free". Its degree argument (a homogeneous ideal generated in degree 299 has zero degree-8 part) is correct: `M_7`'s entries are linear in the coefficients |
| B25-04 plus erratum | `92a7d054` report §4.2; `9e12d789` erratum rows 1a, 1b, 2 | yes: "every component `< D*`", even unbounded tails, and the `t ≤ d` restriction are all as corrected |
| A25-04 ten-minor theorem | `81967dde` report: "no nonzero polynomial in those ten minors is a global determinant equation"; `h0` rejected at 256 | yes |
| A25-05 completion of old T | `eb53b97c:docs/a25_05_report.md` "Exact actual-padding control": for `z = x1`, `d = x2`, `e = x3`, `f = x4`, with arbitrary `a,b,c`, the difference is `2x1x2x3x4` | yes: the shear example correctly exits that family, and (C) covers it |

A26-01 does not use B17-01, C_PER or C_DUBE.

### 1.8 Priority: DEFER on priority only; this does not affect correctness

I ran two brief web searches on 2026-09-23 around 02:55Z:

- "permanent of symmetric 3x3 matrix equals determinant sqrt(2) determinantal representation";
- "symmetric permanent determinantal complexity 3x3 symmetric matrices per_3".

The results were listing pages only. Neither search surfaced a statement that `l·per` of a
symmetric 3×3 matrix of linear forms, or `per A_sym` itself, is a linear determinant. **I read no
primary source**, so there are no URLs, versions or hashes to record.

The statement is short and of classical Pólya type (see the remark in 1.1), so a prior statement
in the permanent/determinant literature is plausible. The search was too brief to rule one out.
The priority question is therefore **UNREAD / open**. The packet itself makes no priority claim
(PROOF header: "No claim of literature priority is made").

### 1.9 A26-01 claim-level table

| # | claim | check | verdict |
|---|---|---|---|
| A1 | Identity (C), all 12 terms | hand | ACCEPT |
| A2 | `S_lit` is an explicit restriction of actual padding; no product-locus premise | READ plus hand | ACCEPT |
| A3 | `K_5 = span{q_i}`, 65 retained coordinates | READ (A25-05) plus hand | ACCEPT |
| A4 | (F), (I) in the whole ring; descent from `Q(√2)` to `Q` | hand | ACCEPT |
| A5 | `closure(π(S)) ⊂ Y` without closedness of `π(D)` | hand | ACCEPT |
| A6 | Coefficients `1+s², 2s, 1, −1`; `h_star(F_1) = −64`; `h_star ∈ H`; labelled not a determinant equation | hand | ACCEPT |
| A7 | Exclusions against cited statements; Application 3 labelled correctly | READ | ACCEPT |
| A8 | Literature priority | brief search, no primary source read | DEFER (priority only) |
| A9 | Scope: nothing about all of `P`; the general five-center comparison is OPEN | READ | ACCEPT |

**Packet verdict: ACCEPT at Theorem A's scope.**

---

## Part 2: A26-03 (content commit `f7967d17`)

### 2.1 Construction: CONFIRMED (hand derivation)

- **Representatives:** 5 `a`-stars and 5 `b`-stars (height 5), 23 pairs (height 2) and 1 merged
  column (height 4), which is 34 in all. Doubled, that gives 20, 46 and 2 columns: 68 columns.
- **Shape:** `λ1 = 68` columns and `λ2 = 68` of height at least 2. `λ3 = λ4 = 20 + 2 = 22`, and
  `λ5 = 20`. So the shape is `(68,68,22,22,20)`, of size `100+92+8 = 200 = 50·4`, with tail 132.
- **Content:** every label occurs 4 times. `a_ij` sits in its star and in either its pair or the
  merged column, each doubled. No column repeats a label.
- **Relation to the old shape:** this agrees with the old K5,5 base, whose shape at `k = 5` was
  `(70,70,20,20,20)` (B26-02 item 1). Merging 4 height-2 columns into 2 height-4 columns gives
  the new shape.

Formula (1) follows from multilinearity, as in B26-02 item 2. The highest-weight argument (a
unitriangular map fixes the top minors; the torus exponent is `λ_i`) is the same one B26-02 item 1
confirmed. It does not use semistandardness. Nonzeroness follows from (4).

### 2.2 Visibility: CONFIRMED (hand derivation)

- **Identity (2).** `(x_i+x_j)⁴+(x_i−x_j)⁴ = 2x_i⁴+12x_i²x_j²+2x_j⁴`. Summing gives
  `(1/3+2/3)Σx_i⁴ + 2Σx_i²x_j² = B²`.
- **Truncation (3).** A label outside `E` that gets an `h_r` puts a zero top-2 vector into a pair
  column. If three or more labels of `E` get `h_r`'s, the merged column has three vectors in
  `span(e3,e4)`. So `f(q0+sB²)` has degree at most 2 in `s`, and all summands are nonnegative.
- **(4).** Every star gets all five colours, so each has `|V(0..4)| = 288`. The merged column has
  colours `0,1,2,3`, giving `V = 12`. Exactly 5 of the remaining 23 pairs have `i+j ≡ 4`, because
  `(0,0)` and `(0,2)` are not among them; each of those gives `|0−4|² = 16`. So
  `C0 ≥ 288^20 · 12² · 16^5`.
- **(5).** In `a`-star 0 put `e3` at `a00`, with the other entries `L1..L4`. Deleting the `x3`
  coordinate leaves exponents `(0,1,3,4)`. The determinant is `V(1,2,3,4)·e2(1,2,3,4) = 12·35 = 420`.
  In the merged column `(e3, L1, L2, L3)`, the exponents are `(0,1,3)`, so the determinant is
  `V(1,2,3)·e1 = 2·6 = 12`. With weight 1/3, `C1 ≥ (1/3)·420²·288^18·12²·16^5`.
- **(6).** In star 0, `e3`, `L1`, `e4`, `L3`, `L4` leave exponents `(0,1,4)` at nodes `1,3,4`:
  `det[[1,1,1],[1,3,81],[1,4,256]] = 444 − 175 + 1 = 270`. Equivalently `V(1,3,4)·h2(1,3,4) = 6·45`.
  In the merged column `(e3, L1, e4, L3)`, the determinant is `|1 1; 1 3| = 2`. With weight 1/9,
  `C2 ≥ (1/9)·270²·288^18·2²·16^5`.

All three bounds hold. Since `C1, C2 > 0`, the function sees `B² ∈ Sym⁴⟨x3,x4,x5⟩`, a direction
to which the old family is exactly blind (B26-02 item 6).

### 2.3 Determinant rejection: CONFIRMED (hand derivation)

- **Moments.** The weights of `ρ` on `{0,±1,±2}` are `1/2, 1/6, 1/12`. The moments are
  `m0 = 1`, `m1 = m3 = 0`, `m2 = 1/3+2/3 = 1` and `m4 = 1/3+8/3 = 3`. Then
  `E[(v·x)⁴] = m4·Σx_i⁴ + 6·m2²·Σ_{i<j}x_i²x_j² = 3Q²`. Every other monomial carries an odd moment.
  This gives (7).
- **`det K_Q`.** `Pf = K12·K34 − K13·K24 + K14·K23 = zw + uv + t² = Q`, and the lower triangle is
  minus the upper, so `det K_Q = Q²`. The `x1` coefficient is `diag(J,J)`, with determinant 1. So
  `Q²` lies in the normalized chart.
- **Degree bound.** Each `Δ_c` is multilinear in the vectors of its column. A label has exactly
  four column occurrences because the content is `50 × 4`. So each scalar coordinate has degree at
  most 4 in `P`.
- **Grid lemma.** Induction on variables with 5 grid values against degree at most 4 is standard
  and correct. `P` has integer coefficients and is a product of squares. So some point of `G^250`
  gives `P ≥ 1`, and every point gives `P ≥ 0`.
- **Bound (8).** `min w = 12^{−5}` per label, so `f(Q²) ≥ 3^{−50}·12^{−250}`.

The rejection holds. `f ∉ I(D_5^{det_4})`.

### 2.4 The general statement (typed question): REPAIR

**Integrator's reading:** "every fully paired, distinct-labels-per-column contraction at `n = 4` is
strictly positive on `Q²`".

**Smallest correct statement (hand derivation).** Let `T` be any five-row filling with content
`d × 4`. Its columns have height at most 5, and semistandardness is not required. Suppose its
multiset of columns can be partitioned into pairs of columns with the **same label set**. Then
exactly one of the following holds:

- (i) some column repeats a label, and then `f_T ≡ 0`;
- (ii) otherwise `f_T(Q²) = ε_T · 3^{−d} Σ_v Π_a w(v_a) P_T(v)`, with
  `|f_T(Q²)| ≥ 3^{−d}·12^{−5d} > 0`.

In case (ii), `ε_T = ±1` is the product of the signs of the permutations relating the two members
of each pair. If both members of every pair are written in the same order, `ε_T = +1` and the value
is strictly positive.

The proof is §2.3 verbatim. It uses only three facts:

- content `d × 4`, which gives degree at most 4 per coordinate;
- the pairing, which gives `Π_c Δ_c = ε_T·Π Δ²`;
- the positive quartic moment identity for `Q²`.

So no such `f_T` is a determinant equation. The same holds for any linear combination of such
nonzero `f_T`, `Σ c_T f_T`, whose coefficients satisfy `c_T·ε_T ≥ 0` and are not all zero.

**The two repairs to the integrator's wording:**

1. "strictly positive" holds only under same-order pairing. For general pairing the correct word is
   "nonzero". This does not change the rejection.
2. The reopening condition should read: a candidate escapes this obstruction only if it is
   (a) a single contraction with at least one column not matched by a partner with the same label
   set, or (b) a linear combination whose signed coefficients `c_T ε_T` are not all of one sign.
   "Unpaired or signed columns" should be read in this sense. Escaping the obstruction is necessary,
   not sufficient. The argument says nothing about whether an unpaired contraction vanishes on
   `Q²`.

**Does it cover the old expander family?** Yes, at `n = 4`. There the old family has no singleton
columns (`n − 4 = 0`). Every column is doubled with one shared ordering (B26-02 item 4, READ). All
labels in a column are distinct (B26-02 item 1). So `f_{H,4}(Q²) > 0` for every 5-regular seed `H`.
This is a second rejection of every individual member, independent of B26-02's `D_4 = (A+B/2)²`
argument. It also rejects nonnegative combinations. For signed combinations it proves nothing,
while B26-02 §3 showed that the common pair `(p4, D4)` cannot witness separation for any
combination.

**Not covered:** `n > 4`, where the old family has unpaired singleton columns and the point would
have to be an `n`-form. I do not extend the statement there.

### 2.5 B25-04 side: `50 < D*` is not decidable from committed text

READ: B25-04 `92a7d054` §0 defines `D* := min{deg f : f ∈ I(D_r^{det_n}), f|_{P_r} ≠ 0}`. The
record's only bound is the floor `D* ≥ 8`, which is ADOPTED in the same regime (erratum
`9e12d789`, "What stands"; B22-02 L6). I found no committed upper bound. Even finiteness of `D*`
rests on the record's adopted noncontainment premises (A25-02 report line 48).

The ">300" figure in the GKZ reconciliation and B22-02 §1.2 is the onset **conjecture**, not a
bound. So "`50 < D*`" is **undecidable from the committed record**. A26-03's CHECKPOINT §2 states
this correctly ("in that excluded family iff `50 < D*`"). The question is moot for the verdict,
because `f ∉ I(D)` by §2.3, and B25-04 Theorem B concerns only separating functions. Graph check:
the tableau graph is connected, with 50 vertices. I did not attempt to decide the inequality.

### 2.6 A26-03 claim-level table

| # | claim | check | verdict |
|---|---|---|---|
| B1 | Content `50 × 4`, shape `(68,68,22,22,20)`, columns, normalization; admissible, highest-weight, nonzero | hand | ACCEPT |
| B2 | `f(q0+sB²) = C0+C1·s+C2·s²` exactly, with bounds (4)–(6) | hand | ACCEPT |
| B3 | Moment identity (7) and `det K_Q = Q²` in the normalized chart | hand | ACCEPT |
| B4 | Degree at most 4 per coordinate; grid lemma; `f(Q²) ≥ 3^{−50}·12^{−250}` | hand | ACCEPT |
| B5 | Padding value unresolved; no `f(p4) ≠ f(D4)` claim | READ | ACCEPT (scope statement) |
| B6 | Producer's scoped structural remark (§3: "entirely paired … no repeated label … positive on `Q²`") | hand | ACCEPT (same-order pairing, as in the packet's construction) |
| B7 | Integrator's general reading | hand | REPAIR (§2.4) |
| B8 | `50 < D*` status | READ | undecidable from the record, and moot |
| B9 | Application 3 wording (CHECKPOINT §2) | READ | ACCEPT: "ceiling 245 proved; floor 299 CERTIFIED-modular at one prime" |

**Packet verdict: ACCEPT at outcome 3 (rejection) for the one redesign.**

---

## 3. Source and method ledger

| source | label | use |
|---|---|---|
| A26-01 report, PROOF, EXCLUSIONS, VERIFICATION_COST, MANIFEST @ `7464a2bd` | READ | object under review |
| A26-03 report, PROOF, CHECKPOINT, MANIFEST @ `f7967d17` | READ | object under review |
| A25-05 `FIVE_CENTER_REDUCTION.md`, `STRUCTURAL_MAP.md`, `PADDING_FIBERS.md`, report @ `eb53b97c` | READ | kernel `K_5`; the `P` definition; old-T control |
| A25-02 report and `APPLICATIONS.md` §3 @ `5007de86` | READ | Application 3 status |
| B26-02 review @ `cdf6839c` | READ | old family structure (items 1, 4, 6; §3) |
| B25-04 report @ `92a7d054`; erratum @ `9e12d789` | READ | `D*` definition, Theorem B, corrected scope |
| B22-02 report @ `e22a41b1` | READ | L1–L6 |
| GKZ `REVISED_VERDICT.md` @ `82633a60` | READ | corrected GKZ scope |
| A25-04 report and `CONSTRUCTION_AND_PROOF.md` @ `81967dde` | READ | ten-minor theorem; the old witness T |
| B22-10 review; GKZ `CLAIM_SCOPE_TABLE`; A26-01 `LIMITATIONS`/`CHECKPOINT`; A26-03 `SOURCE_LEDGER`/`INPUT_BINDINGS` | UNREAD | not load-bearing for any verdict |
| literature on symmetric permanents | UNREAD (search listings only; no primary source read) | priority item 1.8 |
| every calculation in §§1.1–1.6 and 2.1–2.4 | hand derivation | — |

## 4. Limitations

- These are hand checks by a single reviewer. There was no symbolic replay: programs are prohibited,
  and no step is in doubt, so none was priced.
- The review is cross-lineage but not blind. I read the integrator's A26-03 intake note, which
  contains a partial hand check, and the B26-02 audit (Claude lineage).
- A26-01's `VERIFICATION_COST.md` bounds were read but not re-derived term by term; they are not
  load-bearing for correctness.
- The priority question is open.
- The positivity statement in §2.4 is for `n = 4` and single fully paired contractions, or
  same-signed combinations of them. Nothing is said about unpaired columns, signed combinations or
  `n > 4`.
- This report is not an acceptance by the record. That needs a delivery pass and coordinator
  reconciliation.

## 5. Resource receipt

Zero pilots, zero mathematical programs, zero compute lease, zero subagents.

Clock (UTC, 2026-09-23):

- start 02:50:37Z;
- mathematical stop 02:55:53Z, so the substantive interval is at most about 5m16s, spent reading
  and hand-checking;
- packet writing followed.

The 45-minute checkpoint never came due. There were no interruptions.

Administrative operations: `git show`/`rev-parse`/`log`/`status`/`merge-base`/`branch`/
`ls-tree`, SHA-256 hashing, `date`, and two web searches. There were no Git mutations. One transient
hashing buffer was written to the shell's `/tmp` rather than the scratchpad and then deleted. It
held a copy of committed bytes only.

**No five-row determinant equation is known to be nonzero on padding.**
