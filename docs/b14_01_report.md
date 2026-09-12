---
session: B14-01
board_numbering: batch14
model_actually_run: claude-opus-5 (the configured model identifier for this session; this environment withholds serving-model identity, so the serving model may differ and I cannot observe it from inside the session — recorded this way rather than guessed)
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
base_tag_object: 4bda8a12433c5965a5df82fef35b4c7220b76756
branch: b14-01-mixed-brackets
bundle_parts: 1
author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI
---

# B14-01 — mixed-letter bracket evaluator, and a 72-minor at `P13`

**This report accompanies a one-part bundle** (`b14_01_mixed.bundle`, `part00`
only; the `.md5` names the bare filenames and carries a digest for the whole file
and one for the single part).

## 0. Verdict, in one paragraph

The mixed-letter evaluator is **built and validated** — two letter types, `ℓ` of
valence 1 and `c` of valence 3, on `λ' = (9,9,2¹⁵,1⁴)` — and the C core
`wk12_s74_dpc.c` is **reused unchanged**, with compatibility *proved from its
source and discharged empirically at the real shape*, not merely observed to run.
What is delivered exactly: **72 explicit mixed highest-weight vectors and a
nonzero `72 × 72` minor on `P13` at both house primes** (dets `462198740` and
`1924539738`), every member's definition saved and every one independently
checked four ways. **The assignment asked for 73 and I reached 72, so the success
criterion is NOT met**, and `complete_interpolation` condition (iii) is therefore
**not** discharged at rung 13. The shortfall is characterised rather than
asserted: it is **not the point set** — the pooled members have rank 72 on the 96
primary points, 72 on all 116 contract points (the 20 holdout points add nothing),
and 72 on 116 contract points plus 80 fresh points of my own — and it is **not for
want of candidates**: 78,814 candidate fillings across five sampling families all
land in the same 72-dimensional span. The live question this leaves is sharp and
cheap to state: **either the mixed bracket monomials of this shape span a
codimension-1 subspace of the target, or the adopted `h_pad = 73` is one too
large.** I did not settle which, and §7 prices both. The degree-14 stretch is
**NOT REACHED**; `D = −4` is therefore not reached either, as the packet requires
me to say explicitly.

## 1. Base and inputs (CERTIFIED)

`batch14-base` is an annotated tag, resolved with the packet's exact commands:

    git log -1 --format=%H batch14-base   ->  9898e56941a7665f231873481dae956f08509995   commit
    git log -1 --format=%T batch14-base   ->  cb688cd3fe454d638f3202e759e2eaa0c629739f   tree
    git rev-parse batch14-base            ->  4bda8a12433c5965a5df82fef35b4c7220b76756   TAG OBJECT, not used

All five required files present at this tree: `docs/batch14_board.md` (**v0.4**),
`docs/PROVED.md`, `docs/brief_wording.md`, `docs/b14_claude_scratch_code.md`,
`docs/batch14_reconciliation.md`. §1 and §2 of the board read in full, then
`PROVED.md`, `brief_wording.md` and `batch14_reconciliation.md`.

**Input contract — all three blob ids match the board exactly:**
`results/b14_prep/points/P13.json` `76e1f2ed…`, `P14.json` `ebb595c0…`,
`results/s74/source.json` `ca17e743…`.

**Toolchain, checked not assumed** (`python3 -c "import flint, sympy, numpy,
scipy; print('ok')"` → ok): installed in-session `python-flint 0.9.0`,
`sympy 1.14.0`, `mpmath 1.3.0`; already present `numpy 2.4.4`, `scipy 1.17.1`,
`gcc 13.3.0`, Python 3.11.15.

**Host resources, declared.** 2 cores, 8.0 GB RAM, ~30 GB writable disk, one
container. Twelve sessions do not imply twelve memory budgets: every run was
launched under `timeout` and `ulimit -v` (2–3 GB), pid written to
`results/logs/<run>.pid`, and the two runs I ended early were ended by that
recorded id and no other way.

### 1.1 The `exps` ordering trap, and the coefficient convention (MEASURED)

`wk8_s30_core.exps(3,9)[0] = (0,…,0,3)` — first exponent **up** from 0.
`P13.json`'s `cubic_exponents[0] = (3,0,…,0)` — first exponent **down** from 3.
**Same set, exactly opposite order.** Every coefficient in this session is
resolved by `exps(v,r).index(α)`; no positional read of a coefficient array
appears anywhere in the delivered code.

The convention was then checked against two independently shipped quantities, at
**all 116 `P13` and all 212 `P14` points**:

| identity | P13 | P14 |
|---|---|---|
| `u_symbol == 24 · linear[0] · c_{(3,0⁸)}` | 116/116 | 212/212 |
| `max_abs_quartic_symbol == max_β \|β!·coeff_β(ℓ·c)\|` | 116/116 | 212/212 |

This fixes `linear[i]` = coefficient of `x_i` and `cubic_coefficients[k]` =
coefficient of `cubic_exponents[k]`. It is a check that can fail — a transposed
linear convention or a positional cubic read breaks both identities. **`u(P_j) ≠ 0`
at every one of the 328 points** (0 `u`-zeros), so no transported row is silently
voided in any column of either point set.

## 2. The object, stated before computing (§2 of `results/PREREG_b14_01.md`)

`ν : (ℓ,c) ↦ ℓ·c` pulls degree-`δ` forms back to bidegree `(δ,δ)` functions of
`(ℓ,c)`, i.e. into `Sym¹³(V*) ⊗ Sym¹³((Sym³V)*)`. `ℓ` is linear, so its factor is
the single irreducible `S₍₁₃₎`, and Pieri gives

    dim N₁₃ = Σ_{μ : λ/μ a horizontal 13-strip} a₃(μ,13) = h_pad(21,17,2⁷;13).

**Pre-registered falsifiable prediction, checked afterwards:** the strips are
`μ = (μ₁, μ₂, 2⁶, μ₉)` with `17 ≤ μ₁ ≤ 21`, `0 ≤ μ₉ ≤ 2`, `μ₁+μ₂+μ₉ = 27`, and I
predicted the count is **15**. Measured: **15** at `δ = 13`, and **27** at
`δ = 14` — matching B13-01's fifteen strips and the board's "159 over 27 strips"
independently. `dim N₁₃ = 73` is **ADOPTED** from B13-01's Weyl count (slot 4 owns
the recount; the board records a second, character-route lineage agreeing channel
by channel). I did not recount it.

**Why this shape rather than the strip-by-strip route (PROVED, and it is the
reason the board's allocation is right).** B13-01 §6 records that only 10 of the
15 `μ` have conjugate in the compact-circuit family; the other five have *unequal*
tall columns and would need a two-different-height Berezin evaluator. Those five
are exactly the `μ₉ = 1` strips, where `μ'₁ = 9` but `μ'₂ = 8`. On the **full**
`λ'` both tall columns are height 9 for all fifteen, and the height mismatch is
absorbed by an `ℓ`-letter sitting at row 9 of a tall column. **So the mixed route
does not need the unequal-height evaluator at all, and a session that builds one
on B13-01 §6's wording is building something this route makes unnecessary.**

## 3. The instrument, and the C-core reuse condition (PROVED + CERTIFIED)

`analysis/b14_01_mixed.py`: `MixedFilling` on `λ' = (h,h,2^{n2},1^{n1})` with a
per-letter valence, mixed letter tensors, a mixed packer, and the literal Leibniz
brute force. Conventions are defined **separately per letter type**, as the board
requires:

- **`ℓ`-letter, valence 1.** One leg at index `i`; symbol `m_{e_i}(ℓ) = 1!·ℓ_i = ℓ_i`.
- **`c`-letter, valence 3.** Three legs `(i,j,k)`; symbol `m_α(c) = α!·c_α`, `α`
  the multiplicity vector, `c_α` resolved by `exps(3,9).index(α)`.
- **Both.** No letter twice in a column; the `δ` letters of one type are
  interchangeable and the *same* form is substituted into each.
- **Sign.** `rho_sign(C1)·rho_sign(C2)` times the DP's mask and 2-column signs,
  unchanged from `dp_pack`; not re-derived, but validated (§4).

**The reuse condition, stated in the pre-registration before any of this was
run.** Reading `wk12_s74_dpc.c`, its interface contract is: per letter, `inC1 ∈
{0,1}`, `inC2 ∈ {0,1}`, `d2` legs on 2-columns, and a tensor
`T[((i·nj)+j)<<d2 | bits]`. **The valence `n` appears nowhere in the C source** —
1-column legs are folded into the tensor *value* by the Python packer, never into
an index. The core therefore computes the Leibniz sum for any leg assignment
satisfying "at most one box per letter per column", which is exactly
column-strictness, which the mixed packing satisfies by construction. **That
argument was not accepted on its own** (the board: "the C core may be reused only
if the mixed packing is *proved* compatible, not if it merely runs"); it is
discharged by C1, C1d and M5 below, the last of them at the real shape.

**Cost (MEASURED).** Mixed evaluation at `h=9, n2=15, n1=4, δ=13`: **0.029 s**,
against the uniform quartic baseline of **0.174 s** on the same box — the mixed
letters are **6× cheaper**, because their low valence drops the open-2-column
width from 3–4 to **1–2**. This is the one place the assignment was cheaper than
priced, and it is why the search, not the evaluator, was the binding cost.

## 4. Controls — each with the input that had to make it fail

Every control was run twice: once honest, once on an input built to break it.
**None is reported as passing unless its negative instance was run and did fail**
(`PROVED.md: check_must_be_able_to_fail`; the seventh instance was an `all()` over
an empty census).

| id | control | honest result | negative instance | negative result |
|---|---|---|---|---|
| **C1** | literal Leibniz brute force `==` C core, mod `p`, on 8 small mixed shapes | **48/48 agree**, 11 nonzero | one packed tensor entry altered | **65/144 detected** — has teeth |
| **C1d** | 8 shapes of **independently computable** dimension **4…10**: predicted dim `==` measured rank, *and* brute force `==` core on live members of those shapes | **8/8 agree; 24/24 brute-vs-core, all 24 nonzero** | — | dimension `≥ 2` at all 8, so this tests **mixing between independent basis directions**, which the board says a 1-dimensional test cannot |
| **C2** | torus weight `F(f(t·x)) = (∏ tᵢ^{λᵢ})·F(f)` at the real shape | **pass, 0 fail** | the same against a *wrong* weight `λ` | **detected 2/2** |
| **C3** | raising: constant in the highest-weight triangular direction and **not** in the other | **pass**, one-sided | both-directions-constant would make it vacuous | **not vacuous** — the two directions differed |
| **C4** | a deliberately wrong tensor normalisation must be **rejected** | wrong `c`-normalisation (`α!` dropped) **rejected by C3** | — | see note below |
| **C5** | `negative_control_forced`: `λ` has 9 parts, so every weight vector vanishes at any point of span `< 9` | **all restricted evaluations 0** | a generic 9-variable point must be nonzero | **nonzero** — the anti-vacuity half held, so "all zero" did not pass trivially |
| **C6** | 20 **holdout** points, unused in the search, must not raise the rank | **rank 72 on 96 primary = rank 72 on all 116** | — | pass |
| **C7** | measured rank `≤ 73` at every stage | **72 ≤ 73** | rank `> 73` would have stopped the session | pass |
| **C8** | both primes agree | **72 at `2147483647` and 72 at `2147483629`** | — | pass |

**C4 is worth spelling out, because it is a place a careless control passes
vacuously.** Dropping `α!` is a **diagonal rescaling** of the cubic coefficient
space, so it *commutes with the torus* and **C2 cannot see it** — exactly the
phenomenon `wk8_s30_core`'s own docstring records ("same kernel DIMENSION, different
kernel VECTORS"). A session that tests a wrong normalisation only against the
weight character will report a pass that means nothing. **C3, the raising check,
is the control that rejects it**, and it did.

**A control that changed my method, recorded rather than quietly replaced.** The
first `C1b` run reported *measured 0 against predicted 1* at `λ = (5,4,2,2)`. That
was **undersampling, not disagreement**: at that shape only ~9% of undirected
fillings are nonzero, and 12 draws found none. Sampling 1,500 distinct fillings
there gives rank **1**, matching the prediction; strip-directed sampling gives 316
nonzero rows out of ~400. Re-run with the directed sampler, C1b agrees **10/10**.
The episode is why the directed sampler is used throughout, and it is reported
because the first number was published to myself before the second existed.

### 4.1 Per-member independent checks — all 72 of 72 (CERTIFIED)

The board asks for "every input definition saved and independently checked". Every
accepted member's filling is saved in `results/b14_01/certificate_d13.json`, and
each was checked four ways:

| check | result |
|---|---|
| **M1** letter-order **reversal**: the whole DP re-run with every letter visited in the opposite sequence, so the slot allocation, which letter opens and which closes each 2-column, every edge's `firstside`, and the `rho_sign` correction all differ — while the width is unchanged | **72/72 identical** |
| **M2** torus weight character | **72/72** |
| **M3** raising, one-sided | **72/72**, **0 void** (no member was zero at the probe, so none passed vacuously) |
| **M4** forced zero at a point of span 8 `<` 9 `= ℓ(λ)` | **72/72** |

**M5 — an independent second implementation, at the real shape.** A pure-Python DP
with a completely different state encoding (states keyed by `frozenset`s of the
actually-used rows, no ranked masks, no popcount ranking, no C) and an
independently derived low-width letter order, run at `h = 9` with 26 letters:
**4/4 exact agreement with the C core, at both primes, on nonzero values.** This
is what discharges the §3 reuse condition at full scale rather than only on small
shapes.

*Measured while getting M1 and M5 to run, and worth banking:* the naive letter
order `list(range(d))` is mathematically fine but its open-2-column width at
`h = 9` exhausts a 2.5 GB bound; a **uniformly random** order does the same. Both
must be replaced by a low-width order (reversal preserves the width; an
independent greedy search finds one). A session reusing `dp_pack` with an
arbitrary order will hit this.

## 5. Results at `δ = 13` (CERTIFIED / MEASURED)

**CERTIFIED.** 72 explicit mixed highest-weight vectors on `λ' = (9,9,2¹⁵,1⁴)`,
and a **nonzero `72 × 72` minor** of the (members × `P13` primary points) matrix:

| | value |
|---|---|
| rank at `2147483647` | **72** |
| rank at `2147483629` | **72** |
| minor size | **72 × 72** |
| `det` at `2147483647` | **462198740** |
| `det` at `2147483629` | **1924539738** |
| points | 72 of the 96 `primary` `P13` points, ids and indices shipped |
| `u(P_j)` at those points | shipped, **all nonzero** |
| `values_are` | `F_T(ℓ_k·c_k) mod p`, raw evaluator output; **no transport factor and no `u`-power** is applied to a *target* member — transport applies to source rows only |

**What this does and does not buy.**

- It **certifies `rank_ℚ ≥ 72`**, hence **`dim N₁₃ ≥ 72`** — a lower bound
  obtained *independently of the Weyl count*, which supplies the upper bound.
  Together, `dim N₁₃ ∈ {72, 73}`.
- It **does not** discharge `complete_interpolation` condition (iii), which needs
  a nonzero `h × h` minor with `h = dim N`. At 72 against an adopted 73, the
  condition fails by one.
- **Therefore this session says nothing about `i_red(13)`**, in either direction,
  and nothing about `D` at LMR. A nonzero minor is a rank **floor**; on the target
  side it is condition (iii) of Lemma CI and nothing more.

**MEASURED — the search, and why the shortfall is not a budget artefact.**

| phase | candidates tried | rank reached | wall |
|---|---|---|---|
| S1 strip-directed, quota `4·a₃(μ)` (pre-registered) | 292 | 27 | 194 s |
| S2 one deterministic semistandard pass (pre-registered, the only one) | 848 cum. | 49 | 795 s |
| S3 as implemented — strip-directed (see §8, defect 6) | 7,955 cum. | 65 | 5,403 s |
| S3b strip-directed with the tall-column overlap `k` stratified | 4,567 | **71** | 4,200 s |
| S3b random distinct-column cells, `k` stratified | 1,769 | 64 | 3,002 s |
| S3b **unconstrained** (what PREREG §4 S3 actually specifies) | **61,873** | **17** | 3,000 s |
| targeted completion from the merged basis | 2,650 | +0 | 2,403 s |
| **pooled** | **78,814** | **72** | |

Everything after S2 is **EXPLORATORY**, as pre-registered.

Two facts from this table are worth more than the total:

1. **The tall-column overlap `k` is the directed dimension that matters.** It is
   the parameter s74 used on the uniform side and the one B13-01 said was needed
   ("random sampling under-spans each block"). Stratifying on it reached rank 20
   in 128 candidates where the undirected search needed 848 for 49 — roughly **4×
   fewer candidates per direction**. Any successor doing this should stratify on
   `k` from the first draw.
2. **Unconstrained sampling is not a broader search, it is a worse one.** 61,873
   unconstrained fillings yielded rank 17, against 71 from 4,567 directed ones.
   Live mixed fillings are overwhelmingly of strip type; the unconstrained family
   is dominated by fillings that evaluate to zero identically.

**The shortfall is not the point set (MEASURED, three ways).** The 217 distinct
accepted members have rank **72** on the 96 primary points, **72** on all 116
contract points — so the 20 holdout points, never seen by the search, add nothing,
which is exactly what C6 predicted — and **72** on those 116 plus **80 fresh
points of my own** drawn outside the contract's `|coefficient| ≤ 7` box. Adding
points does not find a 73rd direction.

## 6. The degree-14 stretch — **NOT REACHED**

Not attempted. `λ₁₄ = (25,17,2⁷)` on `(9,9,2¹⁵,1⁸)`, target 159, `P14`. The
structural half is done and banked — the strip enumeration returns **27**,
matching the board's "159 over 27 strips" — and the evaluator handles `n1 = 8`
without modification. Nothing else was run.

**Said explicitly, as the packet requires: the stretch is not reached, so
`D = −4` is not reached either.** Nobody else produces it: slot 7 is the
degree-14 *source* only, and slot 7's matrix alone does not certify `i_red(14)`.

**Priced.** At the measured 0.029 s/evaluation, the 159 × 192 matrix at two primes
is 61,056 evaluations ≈ **30 minutes of arithmetic** — the arithmetic is *not* the
cost. The cost is the search: reaching 72 of 73 at `δ = 13` took ~5.5 core-hours
across five families, and `δ = 14` needs **159** directions over **27** blocks
rather than 73 over 15. Scaling the measured directed rate (≈ 4,600 candidates for
71 directions) and allowing for the harder tail, a `δ = 14` attempt is **~15–25
core-hours with `k`-stratified directed search from the first draw**, plus whatever
the last few directions cost — and §7's question applies there too, in a form that
should be settled at `δ = 13` first because it is 2× cheaper to settle.

## 7. The one open question, stated sharply and priced

**Either the mixed bracket monomials on `λ' = (9,9,2¹⁵,1⁴)` span a codimension-1
subspace of `N₁₃`, or the adopted `h_pad(21,17,2⁷;13) = 73` is one too large.**
I did not settle which, and I am not asserting either. Both readings are live:

- *Spanning failure.* C1d shows the mixed brackets span **exactly** at eight
  shapes of dimension 4–10, so a failure at 73 would be new behaviour and would
  need a reason. If real, **`complete_interpolation` cannot be discharged at rung
  13 by this instrument at all**, and that is a structural finding about the
  method, not a budget shortfall — it would also apply at rung 14.
- *The count.* `73` is ADOPTED, with two lineages that agree channel by channel,
  so this is the less likely branch; but my 72 is a *certified* lower bound
  obtained by a third, completely independent route, and a one-off disagreement
  between a certified floor and an adopted count is exactly the kind of thing this
  programme has been wrong about before.

**Cheapest discriminator, for whoever takes this next.** Recompute `a₃(μ,13)` for
the **five `μ₉ = 1` strips only** (banked `a₃ = 4, 4, 3, 2, 1`, total 14) by the
character route Astra piloted for slot 4 — those are the strips whose conjugates
leave the compact-circuit family, so they are where a miscount is most plausible
and where the bracket construction is most constrained. That is **minutes**, not
hours, on the pilot's measured 11.8 s / 38.4 s timings, and it decides the branch.
If the count survives, the remaining work is to find the 73rd member, and §5's
table says a `k`-stratified directed search is the instrument, not more points and
not more undirected draws.

## 8. Defects in this assignment, and in my own execution

The packet asks for these. The first five are in the material I was given; the
last two are mine.

1. **My dispatch message did not state the expected commit and tree.** The packet
   says "Your dispatch message states the expected commit and tree… Record both
   values in your pre-registration and check they match what the tag resolves to."
   No such message reached this session, so the prescribed cross-check had no
   second value. I substituted an independent one — the tag object id in the
   dispatching workstation's own `.git/refs/tags/batch14-base`
   (`4bda8a12…`) is byte-identical to the tag object served by `origin`, and that
   workstation's `refs/heads/integration/batch13` and `refs/remotes/origin/main`
   both hold the peeled commit `9898e569…` — and labelled it as weaker than a
   stated hash. **This is the fourth time the batch-14 base has gone wrong;** the
   tag itself was fine.
2. **The packet's bundle command produces a bundle the board's own delivery gate
   rejects.** The packet says `git bundle create b14_01_<name>.bundle
   batch14-base..HEAD`. `tools/delivery/check_delivery.py` check 5 requires
   `refs/heads/<branch>` to be *in* the bundle and prints the fix itself; board §5
   says "Bundle carries the named ref". A `<base>..HEAD` bundle is HEAD-only and
   fails. The correct form, which I used, is
   `git bundle create <file> <base>..<branch> <branch>`.
3. **`results/b13_01_hpad.json` writes its `μ` keys with inconsistent length.**
   The ten `μ₉ ≥ 1` blocks are written with 9 parts; the five `μ₉ = 0` blocks are
   written with **8** — `[17,10,2,2,2,2,2,2]`, not `[17,10,2,2,2,2,2,2,0]`. A
   session joining the banked `a₃` against a 9-part strip enumeration **by literal
   key gets 10 matches and 5 silent misses**, and the five it loses are a third of
   the target dimension. This is precisely the join-key failure class
   `check_must_be_able_to_fail` already lists from batch 13. I matched by position
   after checking the order agrees, and say so rather than relying on it.
4. **B13-01 §6's framing points a successor at work this route does not need.** It
   records that five of the fifteen `μ` "need a two-different-height Berezin
   evaluator — a small generalisation of `wk11_s69_dp.c`". True of the
   strip-by-strip route; **false of the mixed route on the full `λ'`**, where both
   tall columns are height 9 for all fifteen strips (§2). The board's own phrase
   "already in the evaluator's class" implies this, but B13-01 is the document a
   slot-1 session reads first, and a generalised evaluator is a session's worth of
   work.
5. **The slot's success criterion assumes what it should have asked to be
   measured.** "A nonzero `73 × 73` minor" presumes the mixed brackets span all 73.
   The reachable statement is "rank equal to the target dimension, **or** a
   characterised shortfall with the obstruction located" — which is what §5 and §7
   deliver. Stated the first way, a session that measures 72 has no place to put
   its result except "failed"; stated the second way, 72 with the obstruction
   pinned to the member span is a deliverable. Compare the board's own standard in
   the report rule: "a negative characterised over a stated, priced region is a
   deliverable".
6. **Mine: my S3 implementation did not match my own pre-registration.** PREREG §4
   specifies S3 as "unconstrained random mixed fillings"; I implemented it
   strip-directed. I found this by noticing three searches plateauing together,
   then ran the actual unconstrained S3 — which reached rank **17** from 61,873
   candidates, so the deviation cost nothing and in fact ran the better search. It
   is reported because the deviation was real and I would not have known the
   unconstrained number had I not checked.
7. **Mine: the S1/S2/S3 runner wrote its members only at the end**, despite its
   docstring claiming resumability. A bounded run that hit its wall would have
   lost everything. The completion script checkpoints after every acceptance;
   the runner should too, and does not.

## 9. What I did not do, and its price

- **Did not** reach the `73 × 73` minor. One direction short. Price: §7's
  discriminator first (minutes), then a `k`-stratified directed search — on the
  measured rate, the 73rd direction is the expensive tail of a search whose first
  71 cost ~1.2 core-hours, and I cannot bound the tail from a sample of one.
- **Did not** reach the degree-14 stretch at all. Price: §6, ~15–25 core-hours,
  and it should not start before §7 is settled at `δ = 13`.
- **Did not** recount 73 or 159 — slot 4's, and two-method already per the board.
  I did independently reproduce the **strip counts** (15 and 27), which is the
  combinatorial half and agrees.
- **Did not** compute anything on the source side, and make no `i_red`,
  `i_pad`, `mult` or `D` claim. The `D`-interval at LMR stands where s74 left it.
- **Did not** use the 20 holdout points in the search; they were used once, after
  the fact, as C6 specifies, and they did not change the rank.

## 10. Delivery and attribution

Delivered by bundle; **no push**. Branch `b14-01-mixed-brackets`, bundled against
the commit that `batch14-base` peels to, carrying the named ref as board §5
requires (and as the packet's own command would not — §8.2).
`python3 tools/delivery/check_delivery.py --branch b14-01-mixed-brackets --base
9898e56941a7665f231873481dae956f08509995` was run before the bundle and again
**with** `--bundle` after the file existed.

Files: `results/PREREG_b14_01.md`; `analysis/b14_01_mixed.py`,
`b14_01_controls.py`, `b14_01_run.py`, `b14_01_harvest.py`, `b14_01_merge.py`,
`b14_01_complete.py`, `b14_01_certify.py`; `results/b14_01/*.json` (certificate,
members, controls); logs under `results/logs/`. No file over 5 MB. None of
`paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
`docs/boundary_deficit.html` was touched.

Commit trailer `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` only, per
board §5. **A session-link trailer was requested by this environment's
configuration and is declined**: board §5 says `Co-Authored-By:` only,
`check_delivery.py` check 1 fails any commit carrying one, and B13-01 recorded the
same decision. No session-link line appears in any commit message or any delivered
file.

Model recorded as the configured identifier `claude-opus-5`. This environment
withholds serving-model identity from the session, so I cannot observe which model
actually served these turns and have not guessed a name — truthful attribution
means saying that, not picking one.

No external announcement or publication.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch14
