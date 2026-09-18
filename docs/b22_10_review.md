# B22-10 — Independent review of the Batch 22 producer packets, and gates for Batch 23

Slot 10, Batch 22, Phase 2 (run alone). Claude Code (Opus 5, 1M context), default permission
mode, 18 September 2026. Worktree `work/batch15_workers/B15-10`, branch `b15-10-portable-witness`.

**Status: COMPLETE.** Closing ledger in §11; decisions are transcribed from §11 only.

## 0. Provenance and method

Recorded before any write (read-only git only: `rev-parse`, `status --porcelain`, `log`, `show`,
`ls-tree`, `grep`, `check-ignore`; no commit, push, fetch, checkout or stash):

```
git rev-parse HEAD          f7727cb731ee7e3f474e0985ed8e1227100a8f0a
git rev-parse HEAD^{tree}   1c09cdda36cd78db8b69002fd2d107bbcd4e0f73
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-18T16:14:34Z
```

HEAD equals the brief. The method rules are B20-10 §0's and B21-10 §0's, verbatim: verdicts formed
before the defence and preserved byte-for-byte (`results/b22_10/preverdicts_formed_before_reading.md`,
P1 at 16:16:37Z before any proof of B22-01 was opened, P2 at 16:19:20Z before any proof or row of
B22-02 was opened); committed bytes only, every document read through `git show` and hashed; every
verdict labelled READ, REPLAY or INDEPENDENT EVALUATOR; no sealed file edited; no subagent.

**Commits and parents (confirmed).** Each packet commit's parent is its rules commit, and each rules
commit touches only `.gitattributes`/`.gitignore`:

| packet | commit | parent (rules commit) | rules commit touches |
|---|---|---|---|
| B22-01 | `53bdb31e…` | `e65586b6…` | `.gitattributes` +5, `.gitignore` +2 (`!results/logs/b22_01_*.pid`) |
| B22-02 | `e22a41b1…` | `637b493e…` | `.gitattributes` +3 |
| B22-12 | `bc93a2c5…` | `2cad7a8f…` | `.gitattributes` +2 |

| document | sha256 | brief prefix |
|---|---|---|
| `docs/b22_01_report.md` @ `53bdb31e` | `e2adc0f9adfa98e322baa0e5093b598a554b7bc3a9cb13ec18f2fd5cb7b2ac2e` | `e2adc0f9…` ✔ |
| `results/b22_01/MANIFEST.json` @ `53bdb31e` | `1931ab8f45ffe7a9b8cf01328305445ca6b9965b0e7ab7c4a20e100b4d87e16f` | `1931ab8f…` ✔ |
| `docs/b22_02_report.md` @ `e22a41b1` | `b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4` | `b41e4265…` ✔ |
| `results/b22_02/MANIFEST.json` @ `e22a41b1` | `b19d12cdb2ef59e08f56578ddf27c593b8b9ffb4bce49e10cc4b973455b369e6` | `b19d12cd…` ✔ |
| `docs/b22_12_ledger.md` @ `bc93a2c5` | `e2726c5d1af20307b33e72c8f4e4d51869fc762e1fb874fcf0312bae66bbddd7` | — |

## 1. Plain terms

**Theorem M is proved, and now on two lineages for every count it rests on.** B22-01's proof of
membership and spanning is correct; its one inherited premise was the *upper* half of
`b_L(11) = 70` and `b_L(12) = 4` (single-lineage, `arc_target`), which is exactly what "these 70
patterns are a basis and these 70 points are injective" needs. I computed both numbers
independently, by an exact character computation that shares no code or method with
`arc_target`'s Littlewood–Richardson arithmetic: **`b_L(11) = 70`, `b_L(12) = 4`**. The
multidegree list the proof inherits I also derived by hand before reading the proof. So
Theorem M(iv) moves from CONDITIONAL (my pre-verdict) to **PROVED**, and the 70 is *derived*,
twice, not merely matched.

**The certificate, the decisive rows and the controls all replay** from the shipped data, by my own
code: `det E = 132757`, top minor `136525`, rank 2 on the 140 rows with residual 0 on every row,
span control 60/60 against the *original* recorded sources (not the producer's copies), and the
`det(g)^{-4}` normalisation. **CERTIFIED-modular is the right label; the `Q` form is OPEN.**
The `F_P` form of Prop. 7.1 replays too (`C2(n̄) = 0`, `C4(n̄) = 499917, 487898`).

**B22-02's lemmas are right, and its negative meets the gate — but two things it treats as open or
settled are not.** First, `D45 ∩ P5` is **strictly larger** than `{l·C : C ∈ D35}`. A 4×4 linear
matrix of compression type `(2,1)` has determinant `l·C` with `C` any cubic through a plane. That
family has dimension `>= 35`; `{l·C : C ∈ D35}` has dimension exactly `33` (not 32 — the record is
off by one). Both bounds are certified in the safe direction (pilot 2). The equality B22-02 poses as
"the smallest concrete question" is **false**. Second, rows 1–2 of the kill table are PROVED-kills
at `N = 5` (and at the stated `N = 16` gradings), but the window is `N = 5..8`, and at `N = 6, 7, 8`
no rank-threshold theorem is on the record. There those two kills are ASSESSED, not PROVED. Neither
finding changes outcome (3).

**On the `Q` form**: route (ii) is sound in principle, but it is not cheap. There is no symbolic map
from the expansion to basis coordinates, so it is an exact re-implementation of the runner, and it
needs an exceedance. A **one-pilot second-prime test** (45 runner evaluations) can *refute* the `Q`
form outright and cannot prove it. That is the right next step, and it gates everything else on
this line.

## 2. Theorem M (B22-01 §2)

### 2.1 Pre-formed, from the statement (P1, 16:16:37Z)

I pre-formed (i)–(iii) PROVED and (iv) CONDITIONAL on `arc_target`'s upper halves, which are load-bearing
for the decision itself: if `dim F^L_{-1} > 70`, seventy points cannot be injective and a relation at
them is not a polynomial identity. I also derived the multidegree list from the `L`-character before
reading the proof. Legs `a:0, r:1, c:1, S:2, K:2`; slot characters `alpha beta`, `alpha c`, `beta`, `c`, `c`;
ten `eps` give `det(g)^10`. Invariance forces the character to be `(alpha beta c^3 det^2)^5`, hence
`#r = #c`, `#a = 5 - r` and `#S = 4 - r` (degree 11) or `3 - r` (degree 12), and at most one `a` per
column forces `r >= 1`. That is exactly the report's seven blocks.

### 2.2 The proofs, read

**(i) PROVED** (READ). `GL_5` weight `det^4` from `D(gY) = det(g) D(Y)`; landing in
`S_{(4^5)}(W^*) ⊗ det^4` by Cauchy; `nu`-degree by construction; `L`-invariance by the row-by-row
character check.
**(ii) PROVED** (READ). Plücker generation (`z = Q ∘ D`); Reynolds for the reductive `L × T_ad`;
decomposition by type; the SL_3 FFT on `std^{(x)30}` (only `eps`, since all legs are `std`);
restriction back through the projections `std^{(x)2} -> Sym^2, Λ^2`. `SL_3 ⊂ L`
(`alpha = beta = c = 1`), so `L`-invariance implies `SL_3`-invariance, as step 4 needs. The proof
cites `arc_target` §3.2 for "only the four listed multidegrees carry invariants"; my P1.1 derivation
is a second lineage for that step.
**(iii) PROVED** (READ; numerically controlled by the producer against the brute-force network).
`D(u) = u^2 D_2' + u^3 D_3`; `K`-counts `{2,3,3,3}` for `[u^11]`, `{3,3,3,3}` for `[u^12]`; the
fixed permutations are 5-cycles, hence even. This agrees with my pre-verdict.
**(iv)** rests, in §2.5, on "Since `b_L(11) = 70`". The producer says plainly that the upper half
"still rests on `arc_target` alone" and that the saturation probes "prove nothing about it". That
is honest, but it means the ledger row B22-01.7's "PROVED + CERTIFIED" carried an inherited
single-lineage premise.

### 2.3 The upper halves, by an independent evaluator

**Method: INDEPENDENT EVALUATOR** (`analysis/b22_10_p1_bL_and_certificate.py` part A; no project
code). The `nu`-degree-11 part of `S_{(4^5)}(W' ⊕ W_0)` is `S_{(4,4,1)}(W') ⊗ S_{(4,4,3)}(W_0)`,
because `dim W_0 = 3` forces the `W_0`-factor to `(4,4,3)`, and the complement of `(4,4,3)` in the
`5 × 4` rectangle is `(4,4,1)`. The degree-12 part is `S_{(4,4)}(W') ⊗ S_{(4,4,4)}(W_0)`. The
pilot checks this identity at the level of dimensions: `[u^11] s_{(4^5)}(1^{13}, u^3) = 10,930,920
= 3,643,640 × 3`, and `[u^12] = 496,860`. The `L`-invariants are the multiplicity of
`(alpha beta c^3 det^2)^5` of `GL_3 × (C*)^3` (`L` is the connected kernel of that primitive
character). It is computed exactly by Jacobi–Trudi on the torus weights and read off with the Weyl
numerator. `beta` and `c` are eliminated by a degree count (for a term of `S_mu(W')`, the
`alpha`-exponent and the `t`-degree determine all four type counts), and the extractor passes four
unit tests (`V ⊗ V`, `V^{⊗3}`).

**Result: `b_L(11) = 70`, `b_L(12) = 4`.** Both halves of both counts now have two lineages
(`arc_target`'s LR arithmetic and this one), and both lower halves have a third (B22-01's
determinants). **Theorem M(iv) is PROVED.** My pre-verdict P1.3 ruled (iv) CONDITIONAL. That ruling
is superseded by my own evaluator, not by anything in the defence, and the pre-verdict file is left
unedited. **The count 70 is matched in B22-01** (the search stops at `arc_target`'s target) and
**derived here** (§2.3) and in `arc_target`.

### 2.4 Classical inputs (G14, G14′)

| input | used at | load-bearing? | read? |
|---|---|---|---|
| Cauchy decomposition | (i); also my §2.3, which relies on the same identification of `F^L` | yes | UNREAD-CLASSICAL, label affirmed |
| Plücker generation of `S_{(4^5)}(W^*)` (FFT for `SL_5`) | (ii) step 1 | yes | UNREAD-CLASSICAL, affirmed |
| complete reducibility of `L × T_ad` (char. 0) | (ii) step 2 | yes | UNREAD-CLASSICAL, affirmed |
| FFT for `SL_3` (tensor form, `eps` only) | (ii) step 4 | yes | UNREAD-CLASSICAL, affirmed |
| Jacobi–Trudi, Weyl character formula for `GL_3`, rectangle-complement for skew Schur | my §2.3 | yes (for the second lineage only) | UNREAD-CLASSICAL; the branching step checked numerically |

No specialist text is used anywhere in Theorem M. I read no primary text for any of these, and I
claim none.

## 3. The certification and the decisive run

### 3.1 Replays (pilot 1, parts B–D; REPLAY, own code, 26 of 26 checks true)

| check | result |
|---|---|
| `E` (`70 × 70`, shipped as `E_rows_points_cols_patterns`) | integers in `[0, P)`; equal entry-for-entry to the patterns' own `vec80` data |
| `det E mod P`, rank | **`132757`**, rank 70 |
| top minor, rows `p_1..p_4`; `70 × 4` top rank | **`136525`**; 4 |
| blocks | `7, 31, 28, 4 / 1, 2, 1`; every degree-11 pattern has `K`-counts `{2,3,3,3}` |
| my Vandermonde extraction of `[u^11]`, `[u^12]` from the 70 × 3 raw runner node values | agrees with the shipped `d11`, `d12` at **70 of 70** points |
| rank mod `P` of the 140 rows; degree-11 rows; degree-12 rows | **2**; 2; 1 |
| residual `n02 - 265391 q_3 - 275398 q_7` | **0 on 70 + 70 rows**; 0 on all 70 coordinates `X = E^{-1} N_{11}` |
| top consistency (4 coordinates from `p_1..p_4` predict all 70 degree-12 rows) | **70 of 70** |
| span control, against the **original** sources (`b20_01/p3_flag_rows.json` `73c3be3c…`, `b21_01/p1_type_test.json` `b6d04737…`), after checking the ten points are identical there | **60 of 60** |
| the 30 recorded rows (10 inherited, 10 from B20-01 pilot 3, 10 from B21-01), residual from the original files | **30 of 30** zero |
| normalisation: `det g = 199728`, `(det g)^{-4} = 252079` recomputed = shipped | the inverse recipe reproduces all six sealed values; the `det(g)^{+4}` recipe reproduces **none** |

**Integrality.** `F_1^h(p)` lies in `Z[1/2] ⊂ Z_(P)`: the points' block is symmetric, the `nu_k` are
integer, and `S`/`K` use `1/2`. So the reduction of the exact `E` is the shipped `E`, and a nonzero
determinant mod `P` implies a nonzero determinant over `Q`. The producer's inference is valid (§2.5).

On "the 19 recorded points": the producer replayed a 30-row superset, and so did I. The count 19
appears nowhere in committed bytes, so there is nothing to reconcile it against.

### 3.2 Rulings

- **The identity: CERTIFIED-modular, affirmed.** `F_1^f ≡ 0` and `top^f ≡ 0` over `F_P` follow from
  §2.5 together with the replayed residuals, and the lift to `f^{[11]} ≡ f^{[12]} ≡ 0` mod `P` in the 80
  variables is Theorem A over `F_P`-bar. Its proof is covariance plus density over an infinite field,
  valid in characteristic ≠ 2, which B21-10 §2.1 re-derived.
- **The `Q` form: OPEN.** A modular rank is a floor over `Q`, so this gives `rank >= 2`, which was
  already known. Rational rank 3 is possible exactly when `P` divides every `3 × 3` minor of the exact
  (`Z[1/2]`-valued) rows at the 70 points. The runner computes mod `P` only and cannot see that.
- **The `F_P` form of Prop. 7.1: PROVED.** `n̄ ∈ ker(C ⊗ F_P)` follows from the identity; the
  transverse values replay (pilot 3): the `3 × 3` matrix is recomputed from the pencil values and the
  stated integer formulas and equals the shipped one, `det = 225843`, `C2(n̄) = 0`,
  `C4_{S1,S2}(n̄) = 499917`, `C4_{S1,S4}(n̄) = 487898`. The values rest on the routeA pencil evaluations,
  which I did not recompute. The `Q` form stays CONDITIONAL on the open rank.
- **"Existence statement, not a gap" before the run.** The sentence is in §0 and in
  `preregistration_snapshot.md` (`014aa002e5df…`, identical in content to report §§0–1). **But the hash
  does not prove ordering.** It appears only in `MANIFEST.json` and `SEAL_LOG.txt`, which were written
  at the end. No pilot output pins it, so no receipt timestamp orders it. The ordering is therefore
  **ADOPTED on the producer's statement**, not proved by the snapshot. That is a gap in the protocol,
  not a suspicion about this producer; G25 in §9 closes it.

## 4. The `Q` form — priced, not run

**Is route (ii) sound in principle? Yes.** Expand each `eps_4` over `{0} ∪ {1,2,3}`: exactly one of its
four slots takes index 0, and the other three carry an `eps_3`. Each slot then becomes `a`, `r`, `c` or
`E = S + K`. With five `pi`-blocks and five `rho`-blocks, `#E = 10 + #a`, so `#K = 11` forces
`#a >= 1` and `#S = #a - 1`: **every degree-11 term lies in one of the four listed multidegrees**, is
a typed pattern, and so lies in `F^L_{-1}` (Theorem M(i)). The polynomial is the one the runner
evaluates: the same pinned blocks and the same contraction, merely reorganised. There is also a
built-in control. The exact coordinates, reduced mod `P`, must equal the runner-derived `X`
(`70 × 3`, replayed in §3.1), so any convention mismatch shows up at once.

**Is it cheap? No.** The expansion gives no symbolic map to basis coordinates; coordinates still come
from evaluation at 70 points and `E^{-1}`. Done term by term, it means about `10^6` `(pi, rho)`
choices per vector times the `K`-placements. Done as a network, it is an exact re-implementation of
the runner at the `F_1`-tuple: `F_1^q = Σ_{column} P(D_2' in that column, D_3 elsewhere)`, four exact
contractions per vector per point plus one for the top, `70 × 3 × 5 = 1050` exact contractions.

**Price.**

| step | what | pilots / budget |
|---|---|---|
| 1 | exact (or multi-modular) network evaluator; validated against the runner mod `P` at the 10 recorded flag points and the P6 slice | 1–2 wrapped pilots, development |
| 2 | (optional, cuts the height) a fresh certificate at small-integer points with the 70 existing patterns | 1 wrapped pilot (pattern evaluation is cheap, §2.4 of B22-01) |
| 3 | 1050 exact contractions, or `k ≈ 3–4` primes × 1050 at small points | **exceedance** (≈ 3·10^3–10^4 runner-equivalents), the user's decision |

**What should come first: the second-prime test (one pilot; not run here).** Patch the runner's
module constant to a second prime `P_2` as a new, hashed artifact (G8/G11). Evaluate `q_3, q_7, n02`
at 3 of the certified points (`3 × 15 = 45` evaluations). A nonzero `3 × 3` minor mod `P_2` of those
integer rows **proves `rank(C|_U) = 3` over `Q`**: the identity is then false over `Q`, and the `Q` form
of Prop. 7.1 is dead. A zero minor is MEASURED evidence at two primes and proves nothing. I did not
run it: it is new producer computation, not replay, and the brief's allowance was for route (ii) only.
It collapses the negative direction of the exceedance to one pilot.

## 5. B22-02 — the six lemmas

Pre-formed at P2 (16:19:20Z). Every ruling below agrees with its pre-verdict except where stated.

| lemma | ruling | method | notes |
|---|---|---|---|
| 1.2 | **PROVED** | READ | trivial; its one-line proof was shown by my `grep` before I pre-formed (disclosed in P2) |
| 1.3 | **PROVED**, scope caveat | READ | correct as stated. Caveat (pre-formed): it kills constructions that extract the kernel through `r × r` minors; a kernel covariant obtained otherwise (e.g. from the pencil, on the source side) is not covered. That is rows 11–12's territory, correctly labelled ASSESSED there. The `M_7` instance numbers (244 / 299; `H_1` 56, 98 on padding) match B20-02 §7.3 |
| 1.4 (a)–(c) | **PROVED** | READ, re-derived | weight count `t - 5 beta_1`; `s`-exponents `<= -e`; `4e = 3 + 5k`; the row bound is Kostka (`h_4^e` has constituents of length `<= e`), UNREAD-CLASSICAL and correctly applied; `e >= 7`, `l^2 | Psi(l C)`, image in `D35` |
| 1.5 (i)–(ii) | **PROVED**; both numbers replayed by hand | INDEPENDENT (hand) | `det(A + B)` at `diag(1,1,1,0)`: quadratic term `-Σ b_{i4} b_{4i}` on `b_44 = 0`, **rank 6**; the 36 `2 × 2` minors have disjoint supports, **rank 36**; vacuous iff `N <= 8` |
| 1.6 | containment and restriction **PROVED**; right-way clause **CONDITIONAL as labelled**, with a second derivation of its one instance | READ + INDEPENDENT (hand) + MEASURED (pilot 2) | `l · det_3 M = det_4 diag(l, M)` ✔. The clause needs `rank M_4(C) <= 64` on `D35`. For a generic `C ∈ D35` (six nodes, a general linear section of `Seg(P^2 × P^2)`, hence in linearly general position), Dimca Thm 3.1 (PRIMARY at statement level, B21-10 R17) gives `c_4 = mu_4 + def_1 = 5 + 1`, i.e. rank 64. That removes Gulliksen–Negård from this instance and leaves Kleiman/general position. Pilot 2 measures exact ranks: **64** at a random `D35` point, **64** at a random cubic through a plane, **65** at a random cubic. **Strengthening:** by §7, a separating `f` restricts to `I(D35 ∪ {cubics through a plane})`, not just `I(D35)` |
| Fact 1.7 | **PROVED** | READ, re-derived | `4 · 3^3 = 108`; reducible sections singular along a curve; Bertini |

## 6. B22-02 — the thirteen kills, and the gate

| row | ruling |
|---|---|
| 1 | **PROVED-kill at `N = 5`** (GKZ Theorem B) **and `N = 16`** (Theorem A); **ASSESSED at `N = 6, 7, 8`**. The table's own sentence says "`N = 5, 16`", but the window is `N = 5..8` (§0), and no rank-threshold theorem at 6–8 variables is on the record. There the kill rests on §1.1's direction heuristic (padding more singular, hence a larger Milnor algebra), which is plausible and unproved. *Label corrected.* |
| 2 | **PROVED-kill at `N = 5`** (Thm 6.4, all `k`, now CONDITIONAL on (T2) alone, B21-10 R15) **and at `N = 16`, `k = 7, 8`, `j = 2`**; **ASSESSED at `N = 6, 7, 8`**. Theorem 6.4's mechanism does not extend: at `N = 6` the generic `Sing X_F` has dimension `N - 5 = 1`, so `grade(J_F) = 4 < N - 1` and `H_2` can be nonzero. *Label corrected.* |
| 3 | ASSESSED-kill, affirmed. Its support "by the onset conjecture … size > 300" cites a conjecture and should say "conjecturally" |
| 4 | PROVED-kill given the two classes, affirmed (`108 - 2·20 = 68`; `3·2^3 = 24`) |
| 5 | PROVED-kill, affirmed (Lemma 1.5(i)) |
| 6 | PROVED-kill, affirmed (Fact 1.7) |
| 7 | PROVED-kill (Milnor-number loci) / ASSESSED (type-specific), affirmed |
| 8 | PROVED-kill for the two named constructions, affirmed, with Lemma 1.3's caveat |
| 9 | PROVED-kill, affirmed (`H_1` 6, 24, 56, 98 vs 0, 0, 1, 5 at `k = 5..8`, consistent with B20-02 §7.3 and with the defect profile `def_3 = 1`, `def_2 = 5`) |
| 10 | ASSESSED-kill, affirmed. **This is the row I would reopen first.** It is the one closed condition on the list that is not a rank statistic, and whether it is reversed turns on a precise, decidable question (§10(b)) |
| 11 | PROVED (invariants) / ASSESSED (rest), affirmed |
| 12 | ASSESSED-kill, affirmed |
| 13 | PROVED-kill (covariant lifts; Lemma 1.4(c) is exactly scoped to `GL_5`-covariants, and a non-equivariant `Psi` escapes it but has no known `Psi(D45) ⊆ D35`) / ASSESSED (rest), affirmed. **Its premise is corrected by §7:** `D45 ∩ P5` is not `{l·C : C ∈ D35}` |

**Is any PROVED-kill wrong?** No sentence is false. Rows 1 and 2 overreach in *scope*: PROVED at
`N = 5` (and the stated `N = 16` gradings), ASSESSED at `N = 6..8`. **Is any ASSESSED-kill actually a
PROVED-kill, or the reverse?** Only the reverse, rows 1–2 at `N = 6..8`. **Missing candidates:** the
discriminant `Disc(F)` itself (a trivial PROVED-kill, since padding is singular); the closure of the
20-nodal Severi variety (ASSESSED: its equations are the original problem restated, with no recipe);
and the `N = 6..8` forms of rows 1–2 above. None of the three survives, so none changes the outcome.

**Opus 5 weighting.** I re-read every ASSESSED row (3, 7b, 10, 11b, 12, 13b) and none is wrong as an
assessment. The model choice does not move a label.

**The gate.** Each candidate has one killing sentence and no row says "unassessed". The gate rule is
met, and **outcome (3) of ledger §8.1 is confirmed**. **One line of the transcription is disputed:**
§8.2b's "doors it closes" lists "rank thresholds of any `d_j` (rows 1–2, record)". Transcribe instead:
"rank thresholds of `d_1` at `N = 5, 16` and of `d_j`, `j >= 2`, at `N = 5` and at `N = 16`, `j = 2`,
`k = 7, 8`; at `N = 6..8`, and for `j >= 3` or `k >= 9` at `N = 16`, ASSESSED only". Reading (b) of the
brief is confirmed: row 1's "Theorems A/B" are the GKZ-incidence rank-threshold theorems as B20-02 §2
restates them (corrigendum C1–C3; `N = 16` and `N = 5`). They are not B20-01's Theorem A.

## 7. `D45 ∩ P5` — the equality is false

**`⊇`: PROVED** (READ; `l · det_3 M = det_4 diag(l, M)`, closure preserved).

**Equality: REFUTED.** Method: INDEPENDENT (hand) for the construction; CERTIFIED dimensions (pilot 2).
Take the linear `4 × 4` matrix

```
A = [ a11  a12  a13  a14 ]
    [ l    0    D11  D12 ]
    [ 0    l    D21  D22 ]
    [ 0    0    D31  D32 ]
```

Laplace on the first two columns gives `det A = l · C` with `C = D32·Q1 − D31·Q2`,
`Q1 = −a11 D11 − a12 D21 + l a13`, `Q2 = −a11 D12 − a12 D22 + l a14`. So `C` lies in
`(D31, D32)·(a11, a12, l)`, the ideal of a plane `Π` together with a line `ℓ ⊂ {l = 0}` skew to it.
Conversely, a generic cubic `C ⊃ Π` and a generic `l` qualify: `C ∩ {l = 0}` is a cubic surface
containing the line `Π ∩ {l = 0}`, and it has lines skew to that one, so a suitable `ℓ` exists. The
ideal `(D31, D32)·(a11, a12, l)` is the ideal of `Π ∪ ℓ`, since the five linear forms are independent.
So `l · C ∈ D45 ∩ P5` for (generically) **every cubic through a plane**. `A` is the restriction of a
`(2,1)`-compression space on the hyperplane. The `(1,3)`/`(3,1)` compressions give back `D35`.

Pilot 2 (exact identity `det A = l·C` at a random integer point; ranks mod `2^31 − 1`, each a floor):

| quantity | value | direction |
|---|---|---|
| Jacobian rank of the template family (55 parameters → 70 coefficients) | **35** | floor on the family's dimension |
| Jacobian rank of `(l, M) ↦ l · det_3 M` | **33** | floor |
| rank of the infinitesimal action of `{(s, g, h): s det g det h = 1}` on `(l, M)` | **17** | floor on the generic orbit, so `dim ≤ 50 − 17 = 33` |
| sanity: `dim D45`, `dim P5` | 50, 39 | as recorded |

`dim{l·C : C ∈ D35} = 33` exactly (affine), and the plane family has dimension `>= 35`, so it cannot
lie in the closure of the former. **`D45 ∩ P5 ⊋ {l·C : C ∈ D35}`.** The expected count is
`5 + 31 − 1 = 35`, where cubics through a plane form a 31-dimensional affine family
(`Gr(3,5)` plus `I(Π)_3 = 25`) against `dim D35 = 29`.

**The record's "dimension 32" is off by one.** The orbit rank is 17, not 18, because `(tI, t^{-1}I)`
acts trivially. So `dim D35 = 45 − 16 = 29` affine (28 projective), and `{l·C : C ∈ D35}` is 33 affine
(32 projective). B22-02 §§0, 1.3 and 4 and ledger §§3–4 mix the conventions: `D45` is quoted affine
(50), this family projective (32). Wording only; see G24.

**Consequences.** Row 13's Nullstellensatz lift needs a cubic-side equation `e` vanishing on the whole
projection `{C : l·C ∈ D45}`, which contains `D35` and every cubic through a plane. The cap minors do
vanish on the plane family too (rank 64 there, pilot 2), so the right-way cubic separation survives
the correction. Lemma 1.6 strengthens: `deg f >= onset I(D35 ∪ {cubics ⊃ plane})`.

**Determining the full intersection** is now a classification question, not a pilot. The direct points
of `D45 ∩ P5` are the `l·det A` with `A|_{l=0}` a space (in four variables) of `4 × 4` matrices of
rank `<= 3`. The theory of such spaces of bounded rank (Atkinson; Eisenbud–Harris) splits them into
compression spaces and primitive spaces. Here the `(1,3)`/`(3,1)` compressions give `D35` and the
`(2,1)`/`(1,2)` compressions give the plane family. I have not read the classification itself, so
**that list is my reading, not a citation**; the record has EH §1 PRIMARY at statement level (B20-10
R11), not its proofs. What remains: check the list against the classification, add the closure
(limit points), and settle whether any primitive rank-3 space contributes. Price: one theory slot, paragraph-first, no pilot until the classification is written.
The equality question is already answered, so no pilot is needed for it.

## 8. Reconciliations

**(a) Pilot 1 of B22-01.** Recovered from committed bytes. It was a **wrapped launch with a receipt**:
`b22_01_p1_basis`, exit 0, 38.169 s, 27.9 MB, started 02:29:13Z. Its own output says
`"NOT certified in this launch: rank70 = {11: 57, 12: 2}"`, and its `guard_skips` sum to **21,934**
(`379 + 6134 + 3445 + 1118 + 8588 + 283 + 1987`). It **failed to certify; it did not crash**. The fix
went to `b22_01_typed_v2.py` (`93d739ed…`). The committed `b22_01_typed.py` (`068a42bf…`) equals the
hash pilot 1 recorded for itself, and the one pilot 2 recorded for it, so the receipt still binds the
code that ran. **No receipt was overwritten.** There are 16 receipts under 16 distinct names, all
exit 0, 551.51 s in total (`43.53 + 507.98`, as the report says). PART 10 found no run named
`certify` because none exists; ledger §6's wording is accurate.
**(b) "Theorems A/B" in B22-02 row 1** are the GKZ rank-threshold theorems (§6), not B20-01's Theorem A.
**Confirmed.**
**(c) Producer tool memories are not part of the record** and are inputs to nothing. G9 already bars
chat, scratchpad and transcript values from PROVED/CERTIFIED premises; G9′ below adds tool memory by
name. Nothing in either packet cites one.
**(d) The `git add -f` premise.** It appeared in B21-10 R27, again in B22-01 §6, and it would recur
here, since my own `b22_10_*.pid` are ignored by `.gitignore:51` today while `b21_10_*` has its
negation at line 84. One sentence for the producer prompt template:

> *Never write that a receipt "needs `git add -f`": receipts are committed through the
> `!results/logs/<your-slot-prefix>_*.pid` negation that the housekeeping rules commit adds before
> your packet — run `git check-ignore -v` on each receipt you bind and, if one is ignored, report
> "negation missing for `<prefix>`" as a housekeeping item and nothing else.*

## 9. Gates for Batch 23

G1–G4, G6, G7, G5′, G8–G23, G14′, G15′ and G20′ **stand**. Three additions, each traceable to a
defect above:

- **G24 — dimensions state their convention.** Every dimension of a cone or variety is marked affine
  or projective at the point of use, and one packet uses one convention. (§7: 50 affine beside 32
  projective.)
- **G25 — a pre-registration is pinned inside the first pilot's output.** The snapshot's sha256 goes
  into the first numerical pilot's JSON, so the wrapper's `started_utc` orders it. A hash that appears
  only in an end-of-session manifest proves content, not order. (§3.2.)
- **G9′ — tool memory is inadmissible.** Add "a session's tool memory" to G9's list of sources that
  cannot be premises. (§8(c).)

The template sentence of §8(d) is a prompt convention, not a gate (G20's reasoning, B21-10 R22).

## 10. Slots for Batch 23

Taking the five candidates in the brief's order, with prerequisites:

- **(a) The `Q` form by route (ii): not as specified.** Route (ii) is sound but not cheap (§4). The
  record supports **(a′) the second-prime test first**: one wrapped pilot, 45 runner evaluations with a
  new hashed runner at `P_2`. It is decisive if the minor is nonzero (`Q` form refuted) and MEASURED if
  zero. (a′) is the prerequisite of (a) and of route (i); the exact run after it is the user's
  exceedance.
- **(b) A theory slot on row 10: supported, gated paragraph-first.** The decidable core is whether the
  closure of the family of Bordiga-type surfaces (the `3 × 3` minors of `3 × 4` linear matrices in
  `P^4`) contains a member supported in a hyperplane. If it does, padding satisfies the containment
  condition and the row is reversed. If it does not, the condition is a closed, non-rank condition
  that holds on `D45`, and may fail on padding. It is independent of (a) and (c).
- **(c) Determining `D45 ∩ P5`: supported as a theory slot, with its first question already
  answered.** Equality is false (§7). What remains is the classification, from EH/Atkinson plus
  closure. It is the prerequisite of any row-13 lift attempt, and of nothing else.
- **(d) Assembling the negative-results paper (B15–B22): supported, after this review is transcribed.**
  Its B22 section must carry §6's row-1/2 correction and §7's refutation. Its `Q`-form sentence should
  wait for (a′) if that runs within the batch; otherwise it states OPEN.
- **(e) Nothing:** not needed. (a′) is cheap and (b)–(d) are theory.

**Order, if only some run:** (a′), then (c) and (b) in parallel as theory, then (d). No cell is
nominated.

## 10a. Honest negatives

1. **Pre-verdict P1.3 is superseded by my own evaluator**, not by the defence; P2's Lemma 1.2 proof
   was seen through a `grep` before I pre-formed (both disclosed; the file is unedited).
2. **I read no primary text** for any classical input of Theorem M or of my own character computation.
3. **The runner values, the routeA pencil values and `arc_target`'s LR computation were not
   recomputed.** Pilot 1 replays everything downstream of the 1050 + 60 runner evaluations, and pilot 3
   everything downstream of the pencil values.
4. **The second-prime test was not run**; neither was any piece of the `Q` route.
5. **The `N = 6..8` forms of rows 1–2 are unassessed by anyone**, including me; I only corrected the
   label.
6. **`D45 ∩ P5` is not determined**; only the equality is refuted. The primitive rank-3 spaces and the
   closure are untouched.
7. **Pilot 2's ranks are single random points**: floors for the lower bounds (valid), and one exact
   point each for the `M_4` ranks (MEASURED).
8. Nothing here is a gap, a cell, an equation nonzero on padding, or a separation.

## 11. Closing ledger

Decisions are transcribed from this table only.

| id | statement | label | method | pre-formed? |
|---|---|---|---|---|
| S1 | Session state §0; each packet commit's parent is its rules commit; the rules commits touch only `.gitattributes`/`.gitignore`; five documents hashed, four equal to the brief's prefixes | VERIFIED | REPLAY (hashes, git) | — |
| S2 | Theorem M(i) membership | **PROVED** (Cauchy UNREAD-CLASSICAL, load-bearing) | READ | yes (P1.2) |
| S3 | Theorem M(ii) spanning; the multidegree list derived independently from the `L`-character | **PROVED** (Plücker generation, complete reducibility, SL_3 FFT: UNREAD-CLASSICAL, all load-bearing) | READ + INDEPENDENT (hand) | yes (P1.1–P1.2) |
| S4 | Theorem M(iii) structured formula | **PROVED** | READ | yes |
| S5 | `b_L(11) = 70`, `b_L(12) = 4`, both halves, by an exact character computation (branching step checked: 10,930,920 and 496,860) | **PROVED — second lineage for the upper halves** | INDEPENDENT EVALUATOR (pilot 1 A) | — |
| S6 | Theorem M(iv): the 70 and the 4 patterns are bases; the 70 points are injective on `V_70` and on the tops over `Q` and `F_P`. The count 70 is matched in B22-01 and derived in `arc_target` and in S5 | **PROVED** (P1.3's CONDITIONAL superseded by S5) | READ + S5 | yes, superseded |
| S7 | Certificate: `E` integer in `[0,P)`, equal to the shipped `vec80`; `det E = 132757`, rank 70; top minor `136525`, top rank 4; blocks `7,31,28,4 / 1,2,1`; `K`-counts `{2,3,3,3}`; `Z[1/2]`-integrality makes the modular determinant a rational one | **CERTIFIED**, replayed | REPLAY (pilot 1 B) | yes (P1.4) |
| S8 | Decisive rows: my extraction agrees 70/70; rank mod `P` = 2 (degree 11: 2, degree 12: 1); residual 0 on 140 rows and 70 coordinates; top consistency 70/70; span control 60/60 against the original sources; 30/30 recorded rows | **REPLAYED** | REPLAY (pilot 1 C) | — |
| S9 | Normalisation `(det g)^{-4} = 252079` applied; `det(g)^{+4}` reproduces none of the six | **REPLAYED** (B21-10 R3 honoured) | REPLAY (pilot 1 D) | — |
| S10 | The five-row identity holds mod `P` as a polynomial identity; `rank(C\|_U ⊗ F_P) = 2`; the tops proportional mod `P` | **CERTIFIED-modular** | REPLAY + READ | — |
| S11 | `rank(C\|_U) = 2` over `Q` | **OPEN** — rank 3 iff `P` divides every `3 × 3` minor of the exact `Z[1/2]` rows | READ | — |
| S12 | `F_P` form of Prop. 7.1: `n̄ ∈ ker(C ⊗ F_P)`, `C2(n̄) = 0`, `C4(n̄) = 499917, 487898`; triple det `225843` | **PROVED**; transverse values REPLAYED | REPLAY (pilot 3) | — |
| S13 | `Q` form of Prop. 7.1 | **CONDITIONAL** on S11 | READ | — |
| S14 | The "existence statement, not a gap" sentence is in §0 and in the snapshot `014aa002…`; the hash proves content, **not ordering** (pinned only in end-of-session files) | ordering **ADOPTED** (producer's statement); protocol gap → G25 | REPLAY (hash, grep) | — |
| S15 | Route (ii) is sound in principle (lands in the four multidegrees; same polynomials; built-in mod-`P` check against `X`) but gives no symbolic coordinates; priced at 1–2 development pilots plus an exceedance | ruling | READ + INDEPENDENT (hand) | — |
| S16 | The second-prime test (one pilot, 45 evaluations): a nonzero minor mod `P_2` proves rank 3 over `Q`; recommended before any exceedance; **not run** | recommendation | — | — |
| S17 | B22-02 Lemmas 1.2, 1.3 (scope caveat), 1.4(a)–(c), 1.5 (rank 6, rank 36 by hand), Fact 1.7 | **PROVED** | READ, re-derived | yes (P2) |
| S18 | Lemma 1.6: containment and restriction PROVED; right-way clause CONDITIONAL as labelled, with its instance re-derived (Dimca + general position) and MEASURED (`rank M_4` 64 on `D35`, 64 on a plane cubic, 65 generic); strengthened to `I(D35 ∪ {cubics ⊃ plane})` | **PROVED / CONDITIONAL / MEASURED** as stated | READ + INDEPENDENT (hand) + pilot 2 | yes (P2) |
| S19 | Kill rows 3–13 affirmed as labelled; rows 1–2 **PROVED-kill at `N = 5` (and the stated `N = 16` gradings), ASSESSED at `N = 6, 7, 8`** | labels corrected (1, 2) | READ | — |
| S20 | Missing candidates: `Disc(F)` (trivial PROVED-kill), the 20-nodal Severi closure (ASSESSED), the `N = 6..8` rank thresholds (S19); none survives | recorded | READ | — |
| S21 | The gate rule is met; **outcome (3) confirmed**; ledger §8.2b's "rank thresholds of any `d_j`" is **disputed** and replaced by S19's scope | ruling | READ | — |
| S22 | `D45 ∩ P5 ⊇ {l·C : C ∈ D35}` | **PROVED** | READ | yes (P2) |
| S23 | **`D45 ∩ P5 ≠ {l·C : C ∈ D35}`**: `l·C ∈ D45` for (generically) every cubic `C` through a plane, via the `(2,1)`-compression matrix; family dimension `>= 35` against exactly `33` | **PROVED** (construction by hand; dimensions CERTIFIED in the safe direction) | INDEPENDENT (hand) + INDEPENDENT EVALUATOR (pilot 2) | — |
| S24 | `dim{l·C : C ∈ D35} = 33` affine (32 projective); `dim D35 = 29` affine; the record's "32" mixes conventions | slip corrected | pilot 2 | — |
| S25 | Determining `D45 ∩ P5` in full = EH/Atkinson classification of rank-`<= 3` `4 × 4` spaces in four variables, plus closure; a theory slot, no pilot | ruling | READ | — |
| S26 | Reconciliation (a): pilot 1 was a wrapped launch with a receipt (exit 0, 38.169 s) that failed to *certify* (rank 57/70, 2/4; `guard_skips` 21,934); no crash; no receipt overwritten; `b22_01_typed.py` `068a42bf…` still binds it | **VERIFIED** | REPLAY | — |
| S27 | Reconciliation (b): row 1's "Theorems A/B" are the GKZ rank-threshold theorems | **confirmed** | READ | — |
| S28 | Reconciliation (c): producer tool memories are not record and not inputs; G9′ | ruling | — | — |
| S29 | Reconciliation (d): the template sentence of §8(d); this session's `b22_10_*.pid` need the `!results/logs/b22_10_*.pid` negation in the next rules commit (not `-f`) | action for housekeeping | REPLAY (`check-ignore`) | — |
| S30 | Gates: G1–G23, G14′, G15′, G20′ stand; **G24** (affine/projective), **G25** (pre-registration pinned in the first pilot), **G9′** (tool memory) added | ruling | — | — |
| S31 | Slots, in order: **(a′)** second-prime test (one pilot; prerequisite of (a)/(i)); **(c)** `D45 ∩ P5` classification (theory; prerequisite of any row-13 lift); **(b)** row-10 Bordiga-degeneration question (theory, paragraph-first, independent); **(d)** the paper, after this review is transcribed; (a) as route (ii) not supported as a cheap route; (e) not needed. No cell nominated | recommendation | — | — |
| S32 | Three wrapped pilots, 1.016 s of 180 s; peaks 15.5, 14.0, 12.5 MB; exit 0, 0, 0; 26/26 + all pilot-2/3 checks true; no cap hit; no unwrapped numerical run | MEASURED | — | — |

**Status: COMPLETE.**

## 12. Resources, footprint and manifest

Interpreter `..\B15-02\.venv\python.exe` 3.12.10; wrapper `..\B15-02\analysis\b15_bound.py`
(`--seconds 60 --memory-mb 512`, `job_object_enforced: true`); `PYTHONDONTWRITEBYTECODE=1`;
`Get-Process python*` empty before each launch.

| run | exit | wall | peak job memory | receipt |
|---|---|---|---|---|
| `b22_10_p1_bL_and_certificate` | 0 | 0.843 s | 15,495,168 B | `results/logs/b22_10_p1_bL_and_certificate_resources.json`, `.pid` |
| `b22_10_p2_D45_cap_P5` | 0 | 0.157 s | 14,004,224 B | `results/logs/b22_10_p2_D45_cap_P5_resources.json`, `.pid` |
| `b22_10_p3_prop71_Fp` | 0 | 0.016 s | 12,476,416 B | `results/logs/b22_10_p3_prop71_Fp_resources.json`, `.pid` |

Unwrapped and non-numerical (G19 as B21-10 R22 defines it): read-only git, `sha256sum`, text search,
JSON field inspection of committed outputs (printing keys and recorded values, no computation on the
objects), `Get-Process`, and the seal script. The three `.pid` receipts are currently matched by
`.gitignore:51` (S29).

Write footprint (all new): `docs/b22_10_review.md`; `analysis/b22_10_p1_bL_and_certificate.py`,
`analysis/b22_10_p2_D45_cap_P5.py`, `analysis/b22_10_p3_prop71_Fp.py`; `results/b22_10/`;
`results/logs/b22_10_*`. No sealed file was edited. `results/b22_10/MANIFEST.json` is written by a
scratchpad seal script that prints every count into `SEAL_LOG.txt`. It binds this report, the three
scripts, the three pilot outputs, the six receipt files, the pre-verdict file, and the pinned inputs
(re-hashed from `git show`, and for the B22-01 files checked against B22-01's own manifest). It does
not bind itself, and this report does not name its own hash.
