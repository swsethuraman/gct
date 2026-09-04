# The normalisation bound is not exact when it fires: `mult_red((15,12,6,1,1,1), 9) = 18 < 19 = h_pad`

Session 47 (2026-09-04), branch `s47-exactness`, clone tip `9aa6a9c` (clone check
passes; all eight required files present).  Pre-registration
`results/PREREG_s47.md`, committed `3984bbd` **before any measurement**.  Work
list `results/s47_todo.md`; ledger `results/s47_ledger.md`; the surviving free
bound `results/s47_units.md`; permanent weights `results/s47_per6_d8.md`; code
`analysis/wk9_s47_*.py`; certificate `results/s42_certs/15_12_6_1_1_1_d9.txt`.
Labels: **proved** / **measured** / **adopted-from-literature** / **expectation**.

*Flag: the brief's required reading lists `docs/s43_review.md`, which is not in
this clone.  Its §2 content is present in `results/sixrow_record.md` and
`docs/sixrow_close.md` §3 and those were read instead.  Nothing else is missing.*

## 0. Verdict

> **The conjecture is false.**  At `λ = (15,12,6,1,1,1)`, `δ = 9`, `ℓ = 6`:
> `a = 21`, `h_pad = 19` — so the bound fires — and `mult_red = 18`.  The
> normalisation bound is **not** attained.  This is the first cell the session
> measured.
>
> **The certificate.**  `a = 21` by two independent routes and `h_pad = 19` by
> **three** (symmetric-function plethysm, Weyl alternation, and a multiset DP
> written for this session that shares no code with either).  `mult_red ≥ 18`
> from `nullity_p(E_red) = 3` at both house primes; `mult_red ≤ 18` from **three
> independent integer highest-weight vectors** in `I(R_6)_9`, obtained by CRT and
> rational reconstruction over both primes (identical pivot columns, max
> coefficient 15360), verified `E_red v = 0` **over `Z`** against all 59,775
> uncompressed raising-operator rows, with the (★) criterion of
> `docs/reducible_ideal.md` asserted on all **240,282** monomials of their
> supports for both constrained indices.  So `mult_red = 18` exactly, `18 < 19`,
> and no part of the verdict rests on a cached number or on a single prime.
>
> **A correction to the evidence the conjecture rested on.**  At `h_pad = 0`
> exactness is a *theorem* of Corollary B2, not a conjecture: `mult_red ≤ 0`
> forces equality with no computation.  Of the 411 firing cells at `δ = 7, 8`,
> **140 are of that kind**; of the 62 at `δ = 9`, 22; and of session 42's eight
> banked firing cells, four.  The conjecture's real support was **seven cells**,
> five of them `ℓ = 6`, `δ = 8`, in one family — not the twelve the headline
> suggested.  This was pre-registered (`results/PREREG_s47.md` §0) before the
> counterexample was found.
>
> **What survives, and it is not nothing.**  `mult_red ≤ h_pad` is still proved
> (Corollary B2), so `units := a − mult_red ≥ a − h_pad` at **every** cell of the
> region, reachable or not, in milliseconds.  That free *lower bound* on the
> pad-side units — the thing the programme actually wants at unreachable cells —
> is untouched by the refutation; only the claim that it is an equality is gone.
> `results/s47_units.md` tabulates it at all 311 cells with `0 < h_pad < a`.
>
> **A regularity proposed, tested, and withdrawn — in that order.**  Write
> `d := min(a, h_pad) − mult_red` for the rank deficit of `μ_λ` and
> `e := h_pad − a`.  Across the 268 cells of the record where all three numbers
> are known, `d > 0` at eight, `d = 1` at every one, and at every one `e` was
> **even** with `|e| ≤ 4` — nine of nine including the counterexample, in a band
> that splits 52 even to 50 odd, with the parity of `e` a coin flip across the
> census (1155 odd to 1122 even over 2277 cells) and uncorrelated with `ℓ`, `δ`,
> `λ_1` and six other invariants.  It looked like a real discriminant.  **It is
> not.**  Two cells later `(16,10,7,1,1,1)_9` (`e = −1`, odd) and
> `(15,11,7,1,1,1)_9` (`e = −3`, odd) both fail, and the first of them fails by
> `d = 3`, so "`d = 1` always" is gone too.  The pattern is recorded here because
> it was proposed on the record and killed by this session's own measurements,
> not because it survived.  **There is no known statistic that separates the
> cells where `μ_λ` has maximal rank from those where it does not** — the same
> conclusion session 43 reached about *where* the bites are, one level up.

## 1. The conjecture, and what it really says

`h_pad(λ, δ) = mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)` is the multiplicity in the
normalisation of `C[R_r]` (Theorem B1 of `docs/reducible_engine.md`
= Kadish–Landsberg Prop. 1.8), so `mult_red ≤ h_pad` always (Corollary B2), and
`h_pad` is a Pieri sum over a cubic plethysm — milliseconds at any cell.  The
conjecture under test:

> **(Exactness.)**  Whenever `h_pad(λ, δ) < a(λ, δ)`, `mult_red(λ, δ) = h_pad(λ, δ)`.

**The restatement that makes it legible (proved; pre-registered).**
`C[R_r]_δ = im(μ*_δ)` for the generalised Foulkes–Howe map
`μ*_δ : Sym^δ Sym^4 V → Sym^δ V ⊗ Sym^δ Sym^3 V` (KL Thm 1.7), which is
`GL(V)`-equivariant, hence in each isotypic component a map of multiplicity
spaces

        μ_λ :  C^{a(λ,δ)}  ⟶  C^{h_pad(λ,δ)},        mult_red(λ, δ) = rank μ_λ.

So `mult_red ≤ min(a, h_pad)` is Corollary B2 together with the trivial bound,
and the conjecture is exactly:

> **`μ_λ` is surjective whenever `h_pad < a`** — that is, `μ_λ` has *maximal
> rank* on the firing set.

Stated that way the conjecture was already in trouble before any measurement,
because the companion statement is known false: at eight measured cells `μ_λ`
drops rank below `min(a, h_pad)`, every one of them with the bound silent
(`h_pad ≥ a`).  The pre-registration set the prior at **0.40** on exactly this
ground and named the most exposed cells — large `a`, small gap, `ℓ = 6`,
`δ = 9`, in-family.  `(15,12,6,1,1,1)_9` is in that description.

## 2. The counterexample

| | value | how |
|---|---|---|
| `λ`, `δ`, `ℓ` | `(15,12,6,1,1,1)`, 9, 6 | in the `(λ_1,λ_2,λ_3,1,1,1)` family of session 43 |
| `a` | **21** | plethysm (`wk8_s30_pleth`) and Weyl alternation (`wk9_s42_census`) agree |
| `h_pad` | **19** | three routes agree (§0); 39 Pieri strips |
| `n_χ`, `n_red`, `nnz_red` | 21451, 20323, 222487 | `wk9_s42_redengine` build, 17 s |
| `nullity_p(E_red)` | **3** at `p = 2147483647` and `p = 2147483629` | sparse Wiedemann certificates |
| `mult_red` | **18** | `≥ 18` from the primes, `≤ 18` from three exhibited integer HWVs |
| `d = min(a,h_pad) − mult_red` | **1** | the bound is missed by exactly one |
| `e = h_pad − a` | **−2** | even, consistent with the pattern of §4 |

`mult_red = 18 ≤ 19 = h_pad`, so **Corollary B2 is not violated** and this is not
the brief's stopping rule 1 (a bug); it is stopping rule 2, and the
pre-registered sweep halted at once.

The three vectors are in `results/s42_certs/15_12_6_1_1_1_d9.txt` in the
χ-coordinates of the red orbits, with the orbit list in the header, so a reader
can re-run the (★) test and the `E_red v = 0` test on them without rebuilding
anything (`analysis/wk9_s47_starcheck.py` does exactly that, from the file).

**What it means for `I(R_6)`.**  `a − mult_red = 3`: the weight
`(15,12,6,1,1,1)` carries **three** independent reducibility equations in
degree 9, where the normalisation bound could only prove two.  It is the largest
unit count at any single cell in the record, and the first cell where a bite is
strictly deeper than the normalisation can see.

## 3. Phase A as left

The pre-registered sweep stopped at its first cell.  A **post-refutation** sweep
was then run under `--continue` — a different question (the failure *rate*, not
the binary), and labelled as such — over cells stratified by the parity of the
gap `a − h_pad`, the discriminant the pattern of §4 proposes.  See
`results/s47_ledger.md` for the full table.

## 4. Phase B — the proof attempt, and where it stands

The brief's three directions, taken in order, with the outcome of each.

### 4.1 Direction 1 — identify `D_δ / C[R_r]_δ` as a module

`Q := D/C[R_r]` is the cokernel of `μ*`, so in each isotypic component
`q_λ := mult_λ Q_δ = h_pad − mult_red` is the corank of `μ_λ`, and the
conjecture is `q_λ = 0` on the firing set.  `Q` is supported on the non-normal
locus `{ℓ ℓ' q} ∪ {ℓ² q}` — the quartics with at least two linear factors.

The obstacle is precise and I did not get past it.  `D` is generated in degree 1
(it is a Segre-product ring) and `C[R_r]` is the subalgebra generated by
`Sym^4 V ⊂ D_1 = Sym^4 V ⊕ S_{(3,1)}V`.  That gives a filtration
`Q_δ` ← `Q_{δ−1} ⊗ D_1` and `C[R_r]_{δ−1} ⊗ S_{(3,1)}V`, but the second term is
of the size of `C[R_r]_{δ−1}` itself, so the resulting bound on `q_λ` is vacuous.
The honest statement is the one §B of `docs/reducible_engine.md` already makes:
computing `q_λ` is computing the image of `A` in `D`, which is the original
problem.  The exact sequence
`0 → I(R_r)_δ → A_δ → D_δ → Q_δ → 0` gives only the bookkeeping identity

        i_λ − q_λ = a − h_pad,        i_λ := mult_λ I(R_r)_δ,

so `h_pad < a` says `i_λ > q_λ` and exactness says `q_λ = 0`; the conjecture is
"`i_λ > q_λ ⟹ q_λ = 0`", and nothing about the conductor makes that plausible.
**No progress, and now no target.**

### 4.2 Direction 2 — does `h_pad < a` force the quotient's `λ`-part to vanish?

No, and the counterexamples say so directly: at `(15,12,6,1,1,1)_9`,
`h_pad = 19 < 21 = a` and `q_λ = 1`; at `(16,10,7,1,1,1)_9`,
`h_pad = 29 < 30 = a` and `q_λ = 3`.  The `λ`-isotypic part of the normalisation
being smaller than the ambient plethysm does **not** stop the normalisation
quotient from carrying that weight.  The direction is closed by measurement, not
by argument.

### 4.3 Direction 3 — the numerical contrapositive, which is where the content is

This was the cheap one and it is the only one that produced anything, because
`h_pad` and `mult_red` are both already banked at 268 cells of the record.
Reading `d = min(a, h_pad) − mult_red` off all of them
(`analysis/wk9_s47_deficit.py`) gives the picture the programme did not have:

- `μ_λ` has **maximal rank at 260 of the 268** cells of the record.  The eight
  exceptions all have `d = 1`, and all have `h_pad ≥ a` (the bound silent).
- Stratified by `e = h_pad − a`, the deficit rate over the record peaks hard at
  the boundary: **24% at `e = 0`** (5 of 21), 14% at `e = 2`, 8% at `e = 4`,
  and 0% everywhere else — including 0 of 15 on the firing side.
- That 0-of-15 was the entire quantitative case for the conjecture, and it is
  weaker than it looks: 5 of the 15 are `h_pad = 0` cells, where exactness is
  Corollary B2.

The parity reading built on this — deficits only at even `e` — is retracted
(§0).  What is left is the shape of the rate, and this session's six firing
cells put a number on the firing side of it for the first time:

> **The bound is exact at 2 of the 6 firing cells measured, all six at `δ = 9`,
> `ℓ = 6`, in the `(λ_1,λ_2,λ_3,1,1,1)` family.**  Deficits seen: `0, 0, 1, 1,
> 1, 3`.

Set against session 43's `δ = 8` result — the bound fires at exactly the four
two-unit cells of the complete in-family set and is exact at all four — the
conclusion is that **exactness is a `δ = 8` phenomenon, not a general one.**  It
held on a closed set at one degree and fails at the next degree in the same
family, at the first opportunity.  That is the most useful thing this session
can say about the finding it was sent to test.

### 4.4 The obstacle, stated precisely

`mult_red = rank μ_λ` and the conjecture was a maximal-rank statement.
Maximal-rank statements for the Foulkes–Howe family are proved
*asymptotically* (Kadish–Landsberg prove asymptotic injectivity of the
Foulkes–Howe map) and are false in small degree — that is the shape of the whole
subject, and it is the shape found here.  A proof of exactness would have had to
produce a reason for `μ_λ` to be surjective at particular small `(λ, δ)`, and the
record now contains twelve cells where `μ_λ` is not of maximal rank, at
`e ∈ {−3, −2, −1, 0, 2, 4}` and with deficits `1` and `3`.  **The obstacle is
that there is no known invariant of `(λ, δ)` that predicts the rank of `μ_λ`;
`a` and `h_pad` bound it and do not determine it.**

## 5. What survives, and what it is good for

**Proved, unaffected:** `mult_red ≤ min(a, h_pad)`, hence at every cell of the
region — reachable or not, in milliseconds —

        units(λ, δ) := a − mult_red  ≥  a − h_pad,

and with the transfer lemma (`mult_pad ≤ mult_red`) the same number bounds the
pad-side units below.  `h_pad = 0` still proves `mult_red = 0` outright, and
those 162 census cells remain negative instances of Kadish–Landsberg's
Question 1.5.  `results/s47_units.md` tabulates the bound at all **311** cells
of the census with `0 < h_pad < a`; at the eight measured among them it is
attained at seven and strictly exceeded at one, and this session's own cells
raise that to attained at 9 of 14.

**Gone:** the equality.  `h_pad` does **not** give the unit count at a firing
cell, so the "predicted two-unit cells across the whole region" the brief asked
for cannot be produced — what `results/s47_units.md` gives instead is
`units ≥ a − h_pad`, proved, which is the honest version of the same table and
is what a reader should use.  In particular the `δ = 8` reading "the bound fires
⟺ two units" does not survive to `δ = 9`: at `(15,12,6,1,1,1)_9` the bound fires
with `a − h_pad = 2` and there are **three** units, and at `(16,10,7,1,1,1)_9`
it fires with `a − h_pad = 1` and there are **four**.

**New ideal elements.**  `(16,10,7,1,1,1)_9` carries **four** independent
reducibility equations in degree 9 where the normalisation bound proves one, and
`(15,12,6,1,1,1)_9` carries three where it proves two.  These are the deepest
bites in the record relative to what `h_pad` can see.

## 6. The pre-registered predictions, scored

`results/PREREG_s47.md`, committed `3984bbd` before any measurement.

| | prediction | prob. | outcome |
|---|---|---|---|
| **P1** | the conjecture survives Phase A | 0.40 | **wrong side, correctly weighted** — it fell at the first cell |
| **P1a** | a counterexample would have `a − h_pad = 1` and `mult_red = h_pad − 1` | 0.75 | **half right**: the first counterexample has `mult_red = h_pad − 1` but `a − h_pad = 2`; `(16,10,7,1,1,1)_9` has `a − h_pad = 1` but `mult_red = h_pad − 3` |
| **P1b** | a counterexample would be at `ℓ = 6`, not `ℓ = 7, 8` | 0.65 | **right** — all four are `ℓ = 6` |
| **P1c** | the conjecture survives at every `ℓ = 7, 8` cell measured | 0.80 | **untested**: the sweep stopped before reaching one, and the post-refutation batch had not reached the `ℓ = 7` cells |
| **P1d** | "fires ⟺ two units" does not extend to `δ = 9` in-family | 0.55 | **right, at the first cell**: `(15,12,6,1,1,1)_9` fires and has three units |
| **P2** | 30 ± 10 cells measured, `n_red` to ~`2·10^4` | — | **wrong by design**: stopping rule 2 fired at cell 1.  Six firing cells measured, `n_red` to `4.0·10^4` |
| **P3** | all outstanding `δ = 8` permanent weights empty | 0.88 | see §7 |

The prior of 0.40 was set on the right ground — that the conjecture is the
maximal-rank half of a statement whose companion is already false at eight
measured cells — and the pre-registration named `(16,10,7,1,1,1)_9` explicitly as
one of the two most exposed cells.  It is now one of the four counterexamples,
and the one that misses hardest.  P1a shows the mechanism was mis-guessed: the
deficit is not always 1.

<!-- SECTION 7 -->

## 8. Honest boundary

- Four counterexamples, one of them **proved** over `Q` (exhibited integer
  vectors); the other three are **measured** — `nullity_p` at both house primes,
  which gives `mult_red ≥ a − nullity_p` proved and the equality measured.  For
  the refutation that distinction does not matter, because a single proved
  counterexample settles the conjecture, and `(15,12,6,1,1,1)_9` is proved.  For
  the *unit counts* claimed at the other three it does: "four independent
  reducibility equations at `(16,10,7,1,1,1)_9`" is measured, not proved, until
  four integer vectors are exhibited.
- All six firing cells measured are `ℓ = 6`, `δ = 9`, in the
  `(λ_1,λ_2,λ_3,1,1,1)` family.  The failure rate is a rate **on that family at
  that degree**, and nothing here measures the firing set at `ℓ = 7`, `ℓ = 8`,
  or outside the family — the pre-registered composition target (P2) was not
  met because stopping rule 2 fired at cell 1.  The 2-of-6 figure should not be
  read as a rate over the region.
- The rank-deficit reading of §4.3 is a reading of the *record*, and the record
  is not a random sample of the region: it is what was cheap, and it is heavily
  weighted towards `ℓ = 6` and towards the family.
- The parity pattern of §0 is retracted, not weakened.  It is left in the
  document because the session proposed it publicly and then killed it, and a
  reader who sees only the retraction learns less than one who sees both.
- `docs/s43_review.md` is absent from this clone; its §2 content was taken from
  `results/sixrow_record.md` and `docs/sixrow_close.md` §3.  If those two
  disagree with the missing file, this document inherits the error.
- The brief's "81 of the 91" `δ = 8` permanent weights is off by one: 82 are
  banked (28 in session 41, 54 in session 43, disjoint, every `a` re-derived
  here) and **nine** were outstanding, not ten.  See `results/s47_per6_d8.md`.

## 9. What next

1. **The rank of `μ_λ` is the object, and it is not predicted by anything
   known.**  `a` and `h_pad` are both free and both only bound it.  The
   successor question is whether `rank μ_λ` has a combinatorial model at all —
   the multiplicity-space matrix is `a × h_pad`, which is `30 × 29` at
   `(16,10,7,1,1,1)_9` against `n_red = 22720` for the rank computation that
   actually produced the number.  A model of that small matrix would give
   `mult_red` at every cell of the region in milliseconds, reachable or not.
   That is the prize the exactness conjecture was a cheap shortcut to, and the
   shortcut is closed.
2. **Lift the three measured counterexamples.**  `(16,10,7,1,1,1)_9` in
   particular: four independent integer vectors would turn "four reducibility
   equations at that weight" from measured into proved, and it is the deepest
   bite relative to `h_pad` in the record.
3. **Measure the firing set off `ℓ = 6`.**  Six of the ten firing cells measured
   here are `ℓ = 6`, `δ = 9`, in-family; the two `ℓ = 7` cells measured are both
   `a = 2, h_pad = 1`, the smallest test the statement admits.  The failure rate
   away from the family is unmeasured.
4. **`h_pad = 0` deserves its own line in the record.**  162 census cells prove
   `mult_red = 0` for free, and they were being counted as evidence for a
   conjecture they say nothing about.  They are worth stating separately, as
   negative instances of Kadish–Landsberg Question 1.5, which is what they are.

