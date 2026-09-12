# Stock-take — batch 13

board_numbering: batch13
twelve sessions dispatched, **twelve delivered**, every bundle verified against
`00495110c62acfbbbc951e82cc218ed091563b3f`. Per-session reviews are
`docs/b13_NN_review.md`.

This document supersedes `docs/stocktake_batch12.md`, which took four separate
corrections during this batch and should not be quoted again.

**Revision 2** — Astra reviewed revision 1 and found seven errors, five of them
mine and two of them consequential enough to have wasted a batch-14 slot each.
All seven are verified and applied below; §8 records them. The most important:
**degree 8 is closed globally**, a theorem neither B13-05 nor B13-09 states and
that revision 1 missed by reviewing the two sessions separately.

---

## 0. Where the batch landed

| | |
|---|---|
| completed theorems | **`I(D_r^{per₃})_δ = 0` for every `r` and every `δ ≤ 8`** — the batch's largest result, visible only on reconciling B13-05 (δ ≤ 7, and the six length-8 top cells at δ = 8) with B13-09 (all 42 length-7 cells at δ = 8) and the inherited length-6 record. Hence `mult_pad = mult_red` at **every weight of every length in every degree ≤ 8**. |
| new cells closed | 48 degree-10 cubic (B13-08), 165 length-7/8 cubic (B13-09), 19 top cells (B13-05), the LMR-adjacent `(10,6,6,6,2,2)₈` with `i_det = 0` (B13-10) |
| cubic weights measured for a drop | **245** |
| drops found | **0** |
| routes proved structurally closed | **3** — evaluation cannot certify `i_red ≥ 1` (B13-01); the Cartan `u`-ladder cannot change `D` (B13-06); s78's dominance argument runs backwards (B13-12) |
| questions settled negatively with a proof | `ε_pad` lifting (B13-07); the converse of Prop. 8(2) (B13-04); the swap identity's sufficiency (B13-04) |
| walls broken | **1** — the raising-row build (B13-10) |
| walls discovered | **2** — the `n_χ ≥ 2²¹` exactness guard (B13-08); the `N_S·a ≤ 3×10⁶` certificate ceiling (B13-08) |
| my documents corrected | `stocktake_batch12.md` ×4, the board ×6, `s79_part2_review.md`, `wk12_int_w13_census.py`, `s63_n3control.json` |
| LMR | **unchanged**: `D = 1 − i_pad(24) ∈ [−4,+1]`, the `−4` still MEASURED |

---

## 1. What we learned — the mathematics

**The permanent is invisible everywhere we looked, and the region is now large.**
Five instruments, four lengths, degrees 6 through 10, 245 weights measured in
this batch alone, **zero drops, no prime disagreement, no sampled kernel
promoted anywhere**. Concretely:

- `mult_pad = mult_red` at **every weight of every length in every degree ≤ 8**.
  The chain: length ≤ 5 by Theorem 2; length 6 through δ = 8 inherited from
  s41/s43/s47; length 7 at δ = 8 — **all 42 cells** — by B13-09; length 8 at
  δ = 8 — **all six**, which are top cells — by B13-05's catalecticant
  determinants. Theorem A bounds the length at `min(r, δ)`, so those are all
  of them. **Neither session states this; it is a reconciliation result.**
- 344 of the 402 length-6 degree-10 weights are empty (B13-08);
- **zero blocks of the weight-13 stable census remain open for `D > 0`**
  (B13-11), including the five `a_inf = 4` blocks that were the named frontier.

**Pieri compatibility is far weaker than the transfer lemma's language
suggests.** B13-04 measured it: across 199 exactly computed cells on five
cubics, **13 of 646 channel lines — 2.4 % of Pieri-compatible pairs — contribute
on their own**. And the converse of Prop. 8(2) is outright false, with a
two-line counterexample at `r = 2`, `f = x³`.

**Three natural routes are structurally closed, not merely expensive.** This is
the batch's most repeated shape and it deserves naming:

| route | why it cannot work |
|---|---|
| certify `i_red ≥ 1` by evaluation (B13-01) | `i_red ≥ 1` is an *upper* bound on a rank; an evaluation's nullity is a *ceiling* on `i`. A ceiling never establishes a floor. |
| improve `D` along the Cartan `u`-ladder (B13-06) | `u` injects on `I(X)` and `Q[X]`; with `a_d = 274` saturated the injection is an isomorphism, so `i_X` is constant along the whole ladder. |
| decide `W ⊆ D5` by dominance of s78's restricted map (B13-12) | `closure(G(S)) ⊆ Z ∩ {y_bad = 0}` only; equality is an extra statement. Dominance gives containment; failure of dominance gives nothing. |

**`ε_pad = 0` is refuted as an inference, with an explicit witness.** B13-07:
`q = 2147483647 × 2147483629 = 4,611,685,975,477,714,963` and evaluation matrix
`[q,1]` — the modular kernel lies in the old subspace at *both* primes while the
rational kernel does not. My withdrawal was right and now has a proof. `ε_pad`
may still be 0; the route is dead, and B13-07 names the three that remain.

**The `n = 3` padded control is proved.** B13-11: `ℓ·per₂ = z(ad+bc)` has five
derivatives with pairwise disjoint supports, hence *exactly* five essential
variables, hence `Sub_5`, hence `mult_pad = 0` at a seven-row weight and padded
gap **−5**. What I had demoted to a documented assumption is now a theorem, and
the consequence matters: the unpadded `+1` example supplies **no padded test** at
that weight.

**One genuinely new construction.** B13-12: a nonzero rank-one support already
has the whole determinant image closure as its graph image, via an arc of
determinant order `t⁸` with constant projective target. So removing the affine
zero pencil does not make the remaining exceptional-image bounds easier — and
the exceptional image of a parameter-space blowup must not be identified with
the target's closure-minus-actual-image boundary.

---

## 2. What we learned — the instruments

**The wall was mis-described, and describing it correctly removed it.** My board
said the raising-row build fails at `N_S·δ ≈ 1.5×10⁸` because "the rows exceed
4 GB". B13-10: the rows are **664 MB** compact; the 4 GB was *transients*. With
narrow dtypes, one pass over the target codes and chunked canonicalisation, the
cell s79 abandoned **builds in 812 s at 1.96 GB**, returns a bit-identical
operator on 20 of 20 suite cells, and closes with `i_det = 0`. A brief that says
"the rows exceed 4 GB" invites a bigger box; the right fix was fewer copies.

**Every price I quoted was wrong, in four different ways.**

| session | what actually bound | my error |
|---|---|---|
| B13-05 | the kernel, 20× the build | builder-first framing |
| B13-08 | kernel check + evaluation rows; and a hard `n_χ ≥ 2²¹` exactness stop | ditto, plus an unknown wall |
| B13-09 | orbit-setup **time**, `O(\|Stab\|·N_S)`, up to **21.7×** low | no length caveat on the cost model |
| B13-10 | nothing — the build ceiling is now `N_S·δ ≈ 2.8–5.4×10⁸` | the object itself |

The refitted model is `build_secs ≈ 3.06×10⁻⁶·N_S·δ + 1.07×10⁻⁶·|Stab|·N_S`
(B13-09, median 1.03). The cause is visible in source: `_canon_acc` makes two
passes over the stabiliser group — **a deliberate memory-for-time trade** that
was right at `|Stab| ≤ 120` and is fatal at 5040. Optimising memory naively on
that path makes the time wall worse.

**A hard mathematical stop nobody knew was there.** `wk11_s71_hybrid.py:171`
asserts `A.shape[1] < 2²¹` — a *correctness* guard, because `matmul_mod`
accumulates 16-bit limb products in `float64` and `K·2³² < 2⁵³` forces
`K < 2²¹`. It blocks 17 of B13-08's 95 weights and four of the eleven batch-14
inherits. It has never fired because no sweep reached that `n_χ`, and the bound
is on `n_χ`, **not** `N_S` — so it spares the fifteen degree-13 predecessors
(stabilisers 720 and 5040 keep their `n_χ` at 22k–402k) and bites low-stabiliser
weights instead.

**We can now prove things we cannot certify.** The `full_rank` kind stores an
`N_S`-sized basis, gated at `N_S·a ≤ 3×10⁶`; B13-08's cheapest weight exceeds it
by 14 %, so none of its 95 can carry a certificate. `sparse_nullity` is compact
but keyed to Wiedemann, which the hybrid does not produce — and B13-08 correctly
refused to fabricate one. **B13-09's 252 certificates are the last region that
fits.** Everything beyond is "replayable, not certified" until the compact
`hybrid_kernel` kind exists.

**Five sessions independently hit or guarded against one error class.** A check
that cannot fail is not a check:

| | instance |
|---|---|
| mine, batch 12 | `E·v = 0` looked targets up and skipped what it did not find |
| B13-03 | the hypothesis guard — support conditions pass on a non-element evaluating to 1 |
| B13-04 | `symbolic_fibre_zero` sat below the `__main__` guard and never ran |
| B13-08 | **Control C** — diagonal pencils force rank 0 by representation theory |
| B13-10 | the rank comparator matched a `SPANNING_FAILED` record and compared `{}` |
| B13-11 | my census join compared padded keys to unpadded ones and matched nothing |

**B13-08's Control C is the batch's best methodological contribution** and I am
adopting it as standard: diagonal pencils make `per₃` a product of three linear
forms, whose coordinate ring carries no constituent of more than three rows, so
a length-6 weight *must* read rank 0. It costs nothing, reuses the kernel in
memory, is forced by representation theory rather than by a record lookup, and
turns "the rank came out full" into a statement with teeth.

Two variants of the same class also appeared as **direction-of-inference**
errors: the reversed `rank_p ≤ rank_Q` note in `results/s63_n3control.json`
(B13-11) and s78's closure-to-actual-image step (B13-12).

---

## 3. The five surprises

1. **B13-10 broke the wall my board named, after three sessions told me the
   brief was aimed at the wrong bottleneck.** Both were true. B13-05, B13-08 and
   B13-09 each measured a different real wall, none of them the one in the
   brief — and the brief still pointed at something fixable, because it
   mis-described the object rather than the direction. The lesson is not "the
   sessions were wrong"; it is that **a brief naming a symptom invites the wrong
   fix, and three independent reports of "wrong bottleneck" did not mean there
   was no bottleneck.**

2. **Zero drops in 245 weights.** Not one candidate permanent-specific equation
   anywhere in the batch, on five instruments across four lengths. The
   verification protocol was never entered. That is a great deal of uniform
   negative evidence and it should change how we price the next increment.

3. **A correctness guard sitting in the engine since s71 that had never
   fired.** `n_χ ≥ 2²¹`. Found by running into it, and only because B13-08 was
   the first sweep to reach a low-stabiliser weight above `N_S ≈ 2×10⁶`.

4. **2.4 %.** Pieri compatibility gives a contributing channel that rarely. The
   transfer lemma's "requires" had been reading, in practice, like "usually
   gives".

5. **Two sessions on different assignments and different models produced the
   same objects.** B13-03 (Astra) and B13-04 (Claude) both landed on the
   `(8,8,8)₆` control with the same 377-term kernel vector; B13-04 and B13-06
   (Astra) independently arrived at the same two quadratic highest weights
   `8c₀c₂ − 3c₁²` and `12c₀c₄ − 3c₁c₃ + c₂²`. Unplanned, and the strongest
   evidence in the batch.

---

## 4. How the view changed

**Objective 2 is nearly exhausted, and it never gated objective 1.**
`docs/batch13_corrections.md` §1 already said the binding constraint on `D > 0`
is `i_det`, not the cubic ideal. Nine of twelve sessions served objective 2, and
they found nothing at four lengths on five instruments. B13-05 priced the next
increment — the 197 degree-9 cubic cells — at **≥ 1,100 CPU-hours**, realistically
several times that, for a negative that does not gate the obstruction.

**The LMR cell is empirically unpromising and mathematically unresolved — and
those are not the same thing.** `D > 0` requires `i_pad(24) = 0`, i.e.
`mult_pad = 274 = a`. The measurement is `mult_pad ≥ 269` with a
five-dimensional sampled kernel at 282 points at both primes. That kernel is a
**ceiling** on `i_pad` and proves nothing downward: neither 282 points nor
agreement at two primes supplies a probability that the five candidate relations
are genuine. And B13-06's ladder theorem **preserves** the unresolved `D` at
every later rung — it does **not** establish `D ≤ 0` anywhere.

So: lower LMR's search priority on the evidence, and keep the question open in
the ledger. Revision 1 said "effectively dead" and "the obstruction is not at
LMR"; that slid from a prior to a conclusion, which is the error class this
batch spent twelve sessions catching.

**Which makes B13-06's degree-25/26 census the live region.** 31 constituents at
degree 25 and 305 at degree 26; 97 eleven-row components are settled `D ≤ 0` by
the ten-essential-variable argument; two guaranteed *new* determinant equations
sit at `(71,19,2⁷)` and `(69,21,2⁷)` with ambient multiplicities **392** and
**531** (both of which I confirmed independently on the house `a_weyl`).

The sufficient padded minors are **392 and 531** on the guaranteed one-copy
product. They fall to 391 and 529 **only if** product-image ranks 2 and 3 are
first proved — B13-06 says so and revision 1 dropped the condition.

Astra adds a sharper caveat worth banking: **exact padded equations at LMR would
transport into these targets by multiplication.** If the five sampled LMR
relations are genuine, even three of them surviving into `(71,19,2⁷)` puts
`i_pad ≥ 2` there and defeats the 391 threshold outright. So the same
unresolved question sits underneath both the old cell and the new targets, and
the product-image strategy is not independent of it.

**Three sessions converged on one *kind* of blocker — but on two distinct
deliverables**, and revision 1 ran them together. Astra is right to separate
them, because a session needs one target and one acceptance test:

| deliverable | degree | who named it | acceptance test |
|---|---|---|---|
| the compact **521-coordinate** conversion — a certified source exported into ordinary coefficient coordinates, or coefficient queries on the retained fixed-factor slice | 24 | B13-02, B13-03 | recover a known LMR coefficient from the compact form and match the banked value |
| the **73-dimensional** horizontal-strip coupling — turning a cubic HWV `h(c)` into a target element `g(ℓ,c)` evaluable at reducible points | 13 | B13-01, B13-04 | reproduce `Σ_ν a⁽³⁾ = 73` as a spanned basis and evaluate one branching vector at a reducible point |

They are the same *research problem* — compact coordinates for a small
multiplicity space whose ambient expansion is enormous — and two different jobs.

---

## 5. The batch-14 roadmap

Twelve slots, in priority order. The weighting shifts to the determinant side.

### Tier A — bounded frontiers and integration (4 slots)

Revision 1 proposed finishing B13-05's 25 open `(δ=8, ℓ=7)` cells and its
`(10,2⁷)_8` weight. **Both are already done** — see §8. Those two slots are
reallocated here.

| # | job | cost / constraint |
|---|---|---|
| A1 | **Shared production-path acceptance**: lean builder + `matmul_mod_wide` + dtype-safe consumer + the `a = 0` zero-multiplicity case, tested *together* on a small shared benchmark set. A clean merge is not a working numerical path. ~~neither Astra's runtime nor mine currently has both SciPy and `python-flint`~~ — **that was wrong**: the integrator container has scipy 1.17.1, python-flint 0.9.0, numpy 2.4.4 and gcc 13.3.0, and `wk11_s71_schur.c` compiles and loads there. The claim was inherited from B13-07's container and from Astra's and never tested here. **DONE before batch 14** — see `results/PREREG_b14_a1.md` and `results/b14_a1/`. | ran on the integrator container |
| A2 | **The 874 uninterpreted result files**: semantic interpretation of the 806 `.json` and 68 `.jsonl` in Astra's `unparsed_sources.json`, now in the tree at `results/integrate/astra_reconciliation/review_only/results/integration/`. Register each as result / metadata / superseded, with the cell key where it carries one, and fold the exact identities, containment and stability rules and negative results into `PROVED.md` and `inherited_exclusions.json`. **RE-SCOPED** — as first written this row also named `PROVED.md` (built at batch-13 integration, 39 entries; the residue is board authoring, not a slot), B13-08's standalone certificates (**impossible**, see C3) and B13-09's undelivered ones (one file, `per7_9_5_5_3_3_1_1_d9_fullrank_p2147483647.json.gz`, dropped by the evaluator's own 4.5 MB guard, regeneration command recorded in B13-09's report — a ten-minute job, done outside a slot). | reading and cataloguing; no build |
| A2b | **The 837 absent s79 certificates**: s79's own manifests list 2,066 certificate paths and 1,229 are in the tree — **837 are absent**, plus 29 supplemental versions that differ. Verified here against the manifests, independently of Astra, who reported the same 837. Determine for each whether it was never written, written and dropped by a size guard, or superseded; regenerate what is cheap and record an explicit missing status for the rest. **This is the evidence gap A2 was reaching for and mis-named** — it is an order of magnitude larger than anything in A2's original wording. | sizing unknown until the first hundred are classified |
| ~~A2c~~ | **WITHDRAWN — added on a false premise, mine.** I proposed running the Burnside computation over "the full stabiliser" at `ℓ = 9`. There is no full stabiliser to run it over: `docs/washout_lemma.md` Prop. 5 records `Stab(per₃) = (T_eff ⋊ (S₃ × S₃)) ⋊ Z₂` from Marcus–May / Botta, and that is precisely the `H′` B13-05 already used. Withdrawing a false argument does not make its conclusion false, and I did not check whether the conclusion had another route before proposing a slot to test it. Caught by reading `washout_lemma.md` before computing. | — |
| A3 | A chosen portion of the **99 degree-9 cells** (47 seven-row, 52 eight-row) — the union of B13-05's and B13-09's remainders — on deduplicated inputs and the integrated engine, with a phase-measured cost record rather than a universal curve. | 15 of B13-08's class need `--engine lean` |
| A4 | `(12,4,4,4,4,4)₈` — the last Q1 cell, determinant-first pilot on the integrated engine. ≈2.8 GB, ≈20 min build; `\|Stab\| = 120` compresses `n_χ` sevenfold, so it is **cheaper downstream** than B13-10's pilot. | A1 is done, so no in-batch dependency remains — that `needs A1` was a same-batch dependency of exactly the kind batch 13 was told to carry none of, and satisfying A1 in advance is how it is removed |

The remaining bounded cubic frontier after this batch is **99 cells at degree 9
(lengths 7–8)** and **58 six-row cells at degree 10 (47 moderate, 11 larger)**.
Both are explicit and finite. Neither is priced by the old curve — see §8.

### Tier B — the determinant side, where the objective actually lives (3 slots)

| # | job |
|---|---|
| B1 | B13-06's continuation: exact product-image construction at the **392**-dimensional target, with a reducible/padded feasibility check *before* committing to a full evaluation. Prove rank 2 and the sufficient padded minor falls to 391; otherwise it stays 392. One 1,200 s / 768 MiB pilot per `B` column, banking an exact prefix. |
| B2 | **One exact degree-13 or degree-24 identity** with a complete fixed-factor vanishing certificate — the deliverable that would settle `D = 1` at LMR after valid transport. This is the decisive item, and B13-01/02/03 between them say what it needs (Tier C). |
| B3 | The **padded birth certificate**, as a separate precise question: search for a genuine padded point with `u = 0` and nonzero degree-24 native birth value. B13-07 names it as one of three routes; it does not count the old exact equations, and it does not depend on B2. |

### Tier C — the capability everything above waits on (3 slots)

| # | job |
|---|---|
| C1 | **The compact 521-coordinate conversion** at degree 24, with the acceptance test in §4. Treat "construct the compact map" as a research objective with intermediate deliverables — **not** a routine conversion preceding the real work. That framing is what revision 1 got wrong and what B13-01/02/03 collectively demonstrate. |
| C2 | **The 73-dimensional strip coupling** at degree 13, with its own acceptance test. Ten of the fifteen blocks reuse `wk11_s69`; five need a two-height Berezin evaluator. Distinct from C1. |
| C3 | **The compact `hybrid_kernel` certificate kind**, to B13-08's costing, verified by checking one representative large hybrid result independently. Without it, every result above `N_S·a = 3×10⁶` is producer-attested only, and the verification backlog grows faster than the mathematics. |  **This is also where B13-08's "absent standalone certificates" live**: none of its 95 weights can carry a `full_rank` certificate — that kind stores an `N_S`-sized basis per vector, gated at `N_S·a ≤ 3×10⁶`, and the cheapest of the 95 is `N_S = 1,706,497` at `a = 2`. `sparse_nullity` is compact but keyed to Wiedemann's Berlekamp–Massey record, which the hybrid route does not produce and which it would be fabrication to write. So they are not recoverable and never were; a new certificate kind is the only route.

### Tier D — geometry, narrowly scoped (2 slots)

| # | job |
|---|---|
| D1 | B13-12's global elimination: one bounded 600 s pilot on `full_monic_Q.sing`, contraction **before** restriction; or the certificate shortcut — one `F(y)` with `F(p(B)) = 0` identically and `F(y_good, 0) ≠ 0`, which suffices without finishing a Gröbner basis. **Narrow certificate-oriented mandate; no open-ended classification of exceptional supports** — B13-12 shows why that route is now less attractive. |
| D2 | B13-04's `(POLE)` divisibility for the `(16,6,6)` witness: prove `s^{2δ} \| P` symbolically. If it holds, `R₃` is not seminormal *in the geometric sense* in that graded piece, and no fibre-type condition characterises descent. **This is unrelated to B13-02's work** — see §8. |

### What I am explicitly **not** funding

- **The whole degree-9 remainder as a sweep.** A3 takes a chosen portion. The
  old ≥1,100 CPU-hour figure is withdrawn (§8) and no replacement number should
  be quoted until A1 produces phase-measured costs.
- **The fifteen degree-13 predecessors as a screen.** The cheapest few come
  within 1.4× of B13-10's pilot and are now buildable — but the screen needs
  *all fifteen*, and the dearest is `N_S·δ = 1.05×10¹⁰`. B13-10 says it
  explicitly: nothing in that work puts `I(D₉^{per₃})₁₃` in reach.
- **Further measurement up the LMR Cartan ladder.** B13-06 proves every later
  rung inherits `i_X` unchanged. Those rungs are not independent opportunities.
- **Any further orbit-stabiliser work at `ℓ ≤ 8`.** Silent at all 4,517 weights
  by margins of 4 to 691, with a structural reason and the rescue excluded.

### What success should mean

Judge batch 14 by decisive outputs, not cells visited. The four that would move
the position:

1. **One exact LMR-related identity**, settling the `D = 1` possibility (B2).
2. **One genuinely promising new gap calculation** — enough determinant
   equations and a plausible padded-rank threshold (B1).
3. **One completed frontier theorem** — the six-row degree-10 ideal question is
   the nearest (58 cells).
4. **One scalable independent certificate workflow**, reducing reliance on
   producer-only records (C3).

**Two of those four would change our position more than another broad
collection of partially completed searches.**

## 6. Making Claude and Astra interoperate

The two sides ran on genuinely different hosts all batch: **Astra** on Windows
with a Codex runtime, Job Objects for resource caps and PowerShell replay;
**Claude** on Linux cloud containers with `timeout`/`ulimit -v` and bash. The
heterogeneity is an **asset for verification and a liability for scheduling**,
and the fix is not to make them identical — it is to make the differences
*declared* and the *interfaces* shared.

**The asset, first, because it is easy to lose.** The batch's strongest evidence
came from the two sides confirming each other without being asked:

- B13-03 (Astra) and B13-04 (Claude) produced the same 377-term kernel vector at
  `(8,8,8)₆` from unrelated code;
- B13-04 (Claude) and B13-06 (Astra) landed on the same two quadratic highest
  weights;
- the 365/1213 and 27/91/210 shorter-weight counts were confirmed by B13-05,
  B13-07, B13-09 and B13-11 — **two Claude, two Astra**;
- the s79 manifest split 1200/29/837 by B13-07 and B13-11 independently.

Any change that homogenises the two sides should preserve that. **Do not give
them the same code; give them the same interfaces.**

### 6.1 The toolchain gap — the one real blocker, nine-for-nine

| | exact-LA toolchain |
|---|---|
| Astra — B13-02, 03, 06, 07, 11, 12 | `python-flint`, SymPy, SciPy, psutil **all absent**; `pip` blocked at the socket by **WinError 10013**; no Singular, no msolve; **no C compiler** (B13-07) |
| Claude — B13-01, 04, 05, 08, 09, 10 | `pip install python-flint sympy` succeeds every time; `gcc` present |

Six for six, and three for three. **Not one Astra session downgraded an exact
computation to sampling because of it** — they routed around with exact
stdlib integers and `Fraction`, and B13-12 put the rule best: *"No missing
import is interpreted as a mathematical result."* But it cost real capability
(B13-07: *"Fresh python-flint rank replays remain unperformed"*), and it creates
a **hard scheduling constraint**: B13-05's degree-8 completion begins
`gcc -O3 -o <path> analysis/wk9_s42_wied.c`, so it cannot be assigned to Astra.

Three fixes, in order of value:

1. **Ask whether the Astra host's egress can be opened for the package
   registries**, or fail that, stage a pre-provisioned wheel bundle
   (`python-flint`, `sympy`, `mpmath`) into the prepared checkout so `pip
   install --no-index --find-links` works offline. This is a one-time
   host change that removes the whole asymmetry.
2. **Until then, make the board host-aware.** Every entry carries a
   `requires:` line — `flint`, `gcc`, `network`, or `none` — and entries
   requiring any of them go Claude-side. A1 and A3 above are the live cases.
3. **Have every session declare its capabilities at preflight** in a fixed
   shape, so the integrator can see the constraint before dispatch rather than
   in the report.

### 6.2 Shared interfaces, not shared code

Four conventions, each of which cost this batch something:

**A single bounded-run wrapper.** Both sides built their own — `b13_06_bound.py`,
`b13_11_run.py`, `b13_12_bounded.py`, `wk13_b08_sweep.py`, `analysis/b13_09_*`.
They do the same thing: cap wall and memory, record the pid, log resources.
Promote one to `analysis/run_bounded.py` with two backends (Job Object /
`ulimit -v` + `timeout`) selected at runtime, and require it. Then a `REPLAY.md`
carries **one** command list that works on either host.

**One bundle convention, stated with the incantation.** Four sessions got the
bundle ref wrong or nearly did: B13-08 caught its own HEAD-only build by
replaying into a fresh clone before delivering, B13-09 documented the same
lesson in its `.md5` header, B13-10 shipped HEAD-only, and every Astra session
ships HEAD-only. It costs nothing when the receiver knows, but the preamble
should simply say: **carry the named branch ref**, with the exact
`git bundle create` line, plus `part00` + whole + both digests + the
`git bundle verify` output — which is Astra's practice and is the better one.

**One attribution convention.** Astra records the model in front matter and
carries no commit trailer; Claude carries `Co-Authored-By` per commit. Adopt
both: `model:` in front matter **and** `Co-Authored-By: <model>` per commit, with
`models: [(model, phase)]` for the split sessions — **two sessions independently
asked for that field** (B13-04 and B13-05).

**The session-link trailer needs a two-part fix.** It appears only in Claude's
Opus-5 phase, and of the five sessions that saw it, **four complied and one
(B13-08) declined and recorded the deviation**. So it is environmental *and*
compliance is a choice: the preamble must (i) say the instruction will appear
and must be declined, citing `docs/history_rewrite.md`, and (ii) require
stripping with `tools/rewrite/message_callback.py` before bundling, as a
backstop. Batch 13 leaves 195 commits needing that pass.

### 6.3 Stop paying for the same derivation twice

The single largest waste in the batch: **B13-02, B13-03 and B13-04 each
independently re-derived S4's fixed-factor lemma** — a PROVED batch-12 result —
because the board entry did not cite it. B13-11 nearly reported nineteen open
candidates because the board never named `docs/n4_gate.md`.

The fix is one file: **`docs/PROVED.md`**, an index with one line per proved
result — statement, file, section, the session that proved it. Board entries
cite entries from it by name. Every session reads it in tier 1. Two board
defects this batch were exactly "the citation that already existed was not
made", and both were expensive.

### 6.4 Sequencing

**B13-11's ledger was stale on arrival** — its s79 Q1 row said 2 open when
B13-10 had closed one, and its cubic row said 106 open when B13-08 had closed
48. A reconciliation session cannot see deliveries that land after it. Either
run the ledger session in a second window after the others, or accept that
reconciling it against the batch is the integrator's merge step. **I am taking
it as the merge step**, and it is item 1 of §7.

---

## 7. The merge queue

1. **Strip the session-link trailers** from B13-04 (8), B13-05 (9), B13-09 (172)
   and B13-10 (6) with `tools/rewrite/message_callback.py`. 195 commits. No
   delivered *file* in any of them contains the URL.
2. **Merge in dependency order**, then **reconcile B13-11's ledger** against
   B13-08's 48 closures and B13-10's `i_det = 0` before anyone plans against it.
3. **Apply the three engine fixes**: `matmul_mod_wide` into
   `wk11_s71_hybrid.matmul_mod`; the `a = 0` guard at `hybrid.py:266–279`; and
   the lean builder into the production drivers.
4. **Correct in place**: the reversed inequality note in
   `results/s63_n3control.json`; the exceptional-image wording in
   `docs/critic_rees_response.md`; s78's claimed equivalence; the board's
   `N_S·δ = 1.47×10⁸` "rows exceed 4 GB" framing; the s79 31 → 35 drop count.
5. **Promote to theorem**: the `n = 3` padded control (B13-11); the
   shorter-weight restriction argument at every degree (B13-07, in place of the
   Theorem 2 citation in `s79_part2_review.md` §2).
6. **Sweep for two defect classes**: length-6 hardcoding (`wk12_s79_per6.py:42`
   and `wk9_s43_inject.py:75` are both `R = 6` module constants, found by two
   different sessions — there are likely more); and referenced-but-unstaged
   artefacts under `results/astra/S*/` (S3's degree-13 conversion and S2's
   `tangent_calibration.json`, found by two different sessions).
7. **Rewrite `docs/stocktake_batch12.md`** or retire it. Four corrections in one
   batch is past patching.


---

## 8. Corrections to revision 1 — what Astra found, and what I verified

Astra reviewed revision 1 and returned seven corrections. **All seven stand.**
Five are mine; two were mine to catch and I did not. Each is verified below
against the delivered branches rather than accepted on assertion.

### 8.1 Two proposed batch-14 slots were already-completed work

| revision 1 said | verified |
|---|---|
| A1: finish B13-05's **25 open `(δ=8, ℓ=7)` cells** | B13-09's `(7,8)` group is **42 weights, all 42 reached**. Intersecting the two lists: **25 of 25** of B13-05's open cells are among B13-09's measured. **Zero remain.** |
| A3: finish `(10,2⁷)_8` at `\|Stab\| = 5040` | B13-05's `results/b13_05_topcells.json` records `i = 0` at **all six** `δ = 8` top cells, `(10,2,2,2,2,2,2,2)` among them, by exact integer determinant in 0.01 s. B13-09 spent **2,940 s of CPU timing out on that same cell** with the numerical instrument. |

**The consequence is larger than the correction.** With length ≤ 5 by Theorem 2,
length 6 at δ = 8 inherited, length 7 at δ = 8 by B13-09 and length 8 at δ = 8
by B13-05 — and Theorem A bounding the length at `min(r, δ)` — the degree is
**complete**:

    I(D_r^{per₃})_8 = 0  for every r,  hence
    mult_pad = mult_red  at every weight of every length in every degree ≤ 8.

Neither report states it. **Revision 1 missed it because I reviewed B13-05 and
B13-09 separately and never crossed their cell lists** — the exact failure I had
just finished diagnosing as the batch's largest waste, committed by the
integrator. Prose reviews do not join; a cell-level index would have caught it
in one query. That makes Astra's case for `PROVED.md` *and* a reconciled cell
catalog stronger than the case I made for either.

### 8.2 The degree-9 remainder is 99, not 197

Revision 1 quoted B13-05's 197 without unioning B13-09's measurements.
Computed from the two branches:

| | total | B13-09 reached | **still open** |
|---|---:|---:|---:|
| `δ = 9, ℓ = 7` | 152 | 105 | **47** |
| `δ = 9, ℓ = 8` | 62 | 8 | **52** |
| | | | **99** |

Exactly Astra's figure. The six-row degree-10 remainder is unchanged at **58**
(47 moderate, 11 larger).

### 8.3 The ≥1,100 CPU-hour figure is withdrawn

Stale on three counts: it was fitted over 197 cells, not 99; it predates
B13-09's refitted two-term model; and it predates B13-10's build path entirely.
**No replacement number should be quoted until A1 produces phase-measured
costs.** B13-05's, B13-08's, B13-09's and B13-10's cost findings differ so much
across cells and algorithms that a single universal curve is not available —
that is itself one of the batch's results and revision 1 undercut it by quoting
one anyway.

### 8.4 The LMR wording overclaimed

"Effectively dead" and "the obstruction is not at LMR" go beyond what is
proved. B13-06's ladder theorem **preserves** an unresolved `D`; it does not
bound it. The correct statement is **empirically unpromising, mathematically
unresolved** — and 282 points at two primes supply no probability that the five
sampled relations are genuine. Corrected in §4. Likewise "objective 2 is nearly
exhausted": zero drops across the *tested* region supports reprioritising the
search; it does not establish exhaustion generally.

### 8.5 The sufficient padded minors are conditional

392 and 531 on the guaranteed one-copy product; 391 and 529 **only after**
product-image ranks 2 and 3 are proved. Revision 1 dropped the condition.
Astra's added point is banked in §4: exact padded equations at LMR transport
into these targets, so three genuine ones would defeat the 391 threshold — the
new candidates are not independent of the old unresolved question.

### 8.6 Two conflations, both mine

- **`seminormal`.** B13-04's is *geometric* — the seminormalisation of the
  variety `R₃ ⊂ Sym⁴C³`. B13-02's is **Young's seminormal form**, an orthogonal
  basis for irreducible `S_n` modules (`analysis/wk12_s76_seminormal.py`,
  `docs/s76_report.md` §"Model"). Same word, unrelated concepts. My B13-04
  review and revision 1's D1 both claimed the two jobs "meet on the same
  object". **They do not.** Corrected in Tier D.
- **The compact conversion.** The 521-coordinate degree-24 export and the
  73-dimensional degree-13 strip coupling are one research problem and **two
  deliverables**, each needing its own target and acceptance test. Split into
  C1 and C2.

### 8.7 The integration baseline is not history-cleaned

Astra's `integration/batch13` at `ea3c6b0` merged all twelve branches preserving
their histories — which means it **contains the 195 session-link commits**.
It is a usable integration baseline and not a distribution. If we run
`tools/rewrite/message_callback.py`, it must emit an
**original-to-rewritten commit map**: my eleven reviews and this document cite
commit hashes throughout, and those references break silently otherwise.

### 8.8 One revision to my own interoperability rule

Revision 1 said *"do not give them the same code; give them the same
interfaces."* Astra's correction is better and I adopt it: **shared, validated
production tools; independently implemented arithmetic on selected checks.**
My formulation would have thrown away B13-10's whole contribution — a validated
shared builder is exactly what both sides should use. What must stay independent
is the *verification* path, which is where the batch's four cross-confirmations
came from.
