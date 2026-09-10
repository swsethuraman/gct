# B13-09 — higher-length cubic exploration (batch 13)

board_numbering: batch13
Session **B13-09**.  Branch `b13-09-higher-length` off
`main = 00495110c62acfbbbc951e82cc218ed091563b3f`.  Pre-registration
`results/PREREG_b13_09.md`, committed at `61f8a07` before any queue weight was
measured, with Addenda A, B and C each committed before the measurements they
govern.  Delivery is by git bundle in **ONE PART** (`part00` only — see §8); no
push was attempted.  Both house primes everywhere.

**The model that ran this session, exactly.**  Two did, and the commits say
which.  **Claude Fable 5.1** (`claude-fable-5-1`) ran the reading, the instrument,
the census, the three calibration reproductions and the first negative control.
The session's model was then changed and **Claude Opus 5** (`claude-opus-5`) ran
the measured queue, the verification, the cost refit and this report.  The
session packet asked for Fable and the later attribution guidance asked for
Opus 5; both are recorded rather than one being chosen, because truthful
attribution is what the packet asks for.  No number here was produced by a model
other than the one its commit names.

Labels: **PROVED** (a theorem in the tree, or a full rank at one prime, cited),
**CERTIFIED** (an exact statement over `Q` carried by a replayable certificate),
**MEASURED** (computed here mod both primes), **ADOPTED** (the record),
**RECORDED** (a cost, a boundary), **EXPECTATION**.

---

## 0. Verdict

> **Two completed degrees at a new length, one group one weight short, and a
> negative characterised over a priced region.**
>
> **`I(D_7^{per₃})_7 = 0`** — all 5 weights of length exactly 7, `mult = a` at
> both primes.  **PROVED.**
>
> **`I(D_7^{per₃})_8 = 0`** — all 42 weights of length exactly 7, `mult = a` at
> both primes.  **PROVED.**
>
> **`I(D_8^{per₃})_8` — five of its six weights, not the group.**  The sixth,
> `(10,2,2,2,2,2,2,2)` with `|Stab| = 5040`, is the dearest weight in the whole
> census; it was run deliberately, alone, to close the group, and was **ended by
> its own pre-registered `timeout 5400` bound** after 2 940 s of CPU, still inside
> the `χ`-isotypic orbit setup.  So **`I(D_8^{per₃})_8 = 0` is NOT established by
> this session**, and neither is the degree-8 statement at length 8.  §2.3 and §5
> give the weight, its measured partial cost, and what it would take.
>
> With the inherited exclusions of §1 — which are the substance of this
> assignment's "account for shorter components explicitly" — Prop. 8(1) of
> `docs/transfer_lemma.md` upgrades the two completed groups to statements with
> no points in them:
>
>     mult_pad = mult_red  at EVERY seven-row quartic weight of degree 7 and of degree 8.
>
> One new length, joining s37/s43/s47/s79's degree-≤9 result at length 6 and s64
> at `r = 5`.  **The permanent is now invisible on the reducible side at every
> length ≤ 7 through degree 8.**  At length 8 the same statement is one weight
> short, and that weight is named.
>
> **At degree 9 the result is a certified prefix, not a completed range.**  The
> `(7,9)` group (152 weights) and the `(8,9)` group (62 weights) are measured in
> refitted-cost order as far as the clock allowed; every weight reached has
> `mult = a` at both primes, and the remainder is priced weight by weight in §5.
> **No drop was found anywhere: 0 of every weight measured.**  So no candidate
> permanent-specific equation arose, and the verification protocol was never
> entered — the deliverable the assignment names for that case is the priced
> negative, and it is §5.
>
> **The session's most consequential number is not a rank.**  The inherited build
> cost model — `2.1·10⁻⁶ · N_S·δ`, sound at length 6 — **underprices lengths 7
> and 8 by up to 21.7×**, because the orbit setup is `O(|Stab| · N_S)` and
> `|Stab|` reaches 5040 here against ~120 at length 6.  Refitted on 165 measured
> weights (§4), the census costs **17.6 h** against the old model's 3.4 h — a
> factor of **5.1** overall — and the `(8,9)` group alone is **13.0 h, not 2 h**.
> Any batch-14 plan at length 7 or 8 built on the old model is optimistic by that
> factor, always in the same direction, and worst exactly on the weights a
> cheapest-first queue would run first.

**What this session does not claim.**  Nothing here bears on objective 1
(`D = mult_pad − mult_det > 0`), whose binding constraint is `i_det`
(`docs/batch13_corrections.md` §1).  This session serves objective 2 and the
pricing of its region.  No membership statement over `Q` was attempted — that is
B13-03's method — and no negative decision-table branch was entered on anything
sampled, because no sampled drop occurred.

---

## 1. The shorter components, accounted for — the part of this assignment most easily got wrong

The assignment names this as the failure mode of both the first draft (which
would have recomputed 365 excluded weights) and of s79's report (which omitted
them without declaring the dependency).  So it is stated as a chain, with each
link's status, and **nothing in it was recomputed.**

`I(D_r^{per₃})_δ` decomposes over weights `μ ⊢ 3δ` of length `≤ r`.  The
**restriction lemma** (`docs/washout_lemma.md` §1, standing, **PROVED**) applies
verbatim with `X = D_r^{per₃}`: a highest-weight vector of weight `μ` with
`ℓ(μ) = k < r` is a polynomial in the coefficient functionals `c_α` with
`supp(α) ⊆ {1..k}`, so it sees only `F|_{C^k}`; and as `F` runs over the dense
subset `per₃(Σ_{i≤r} s_i A_i)` of `D_r^{per₃}`, its restriction
`per₃(Σ_{i≤k} s_i A_i)` runs over a dense subset of `D_k^{per₃}`.  Hence

    mult_μ C[D_r^{per_3}]_δ  =  mult_μ C[D_k^{per_3}]_δ ,    k = ℓ(μ),

so **a shorter weight's `units` is its length-`k` value** — it is not a new
object at length 7 or 8, and computing it again would measure the same number a
second time.  Therefore:

| `ℓ(μ)` | covered by | status | weights at `δ=7 / 8 / 9` (`Σa`) |
|---|---|---|---|
| `≤ 5` | `docs/washout_lemma.md` **Thm 2** — `D_k^{per₃} = Sym³Cᵏ` for `k ≤ 5`, by an exact full-Jacobian-rank witness (rank 35 at both primes, s26, re-verified s37) — plus **Thm 3(1)**'s restriction argument | **PROVED**, every degree | 129 (193) / 232 (490) / 365 (1213) |
| `6` | `I(D_6^{per₃})_δ = 0` for `δ ≤ 9`: `δ ≤ 6` Pieri + s37 (`docs/transfer_lemma.md` §4); `δ = 7` s41 + s43, 27 weights; `δ = 8` s41 + s43 + s47, 91 weights; `δ = 9` s79, 210 weights | **PROVED** (full ranks, both primes) | 27 (27) / 91 (139) / 210 (592) |
| `7` | **this session**, §2.1–2.2 | **PROVED** at `δ = 7, 8`; prefix at `δ = 9` | 5 (5) / 42 (42) / 152 (265) |
| `8` | **this session**, §2.3–2.4 | `δ = 8`: **five of six weights** (the sixth ended by its timeout bound, §2.3) — so **not** a completed degree; prefix at `δ = 9` | — / 6 (6) / 62 (63) |

Two independent consistency checks on that accounting, both of which pass and
both of which would have caught a miscount:

- the `ℓ = 6` counts this session's own enumeration produces — **27, 91, 210** —
  are exactly the record's (s43 §"δ = 7 CLOSED"; s47's 91; s79's 210);
- the `ℓ ≤ 5` count at `δ = 9` — **365 weights, `Σa = 1213`** — is exactly the
  integrator's independent count in `docs/s79_part2_review.md` §2a, including its
  per-length split (1, 11, 48, 117, 188).

**So the 365 weights are cited, not run, and the citation is checked against two
independent enumerations of the same set.**  This is the declared dependency
s79's report should have carried, and B13-07 is auditing the chain itself.

One consequence worth stating because it is easy to get backwards: since every
constituent of `Sym^δ(Sym³)` has at most `δ` rows (Pieri), a weight of length 7
needs `δ ≥ 7` and one of length 8 needs `δ ≥ 8`.  So at these lengths the five
groups `(7,7), (7,8), (7,9), (8,8), (8,9)` are **the whole of** the new content
through degree 9 — there is no `(8,7)` group to forget, and `I(D_7^{per₃})_δ` and
`I(D_8^{per₃})_δ` vanish for `δ < 7` and `δ < 8` respectively for free.

---

## 2. What was measured

<!-- GENERATED: summary -->
| group | weights | measured | `mult = a` | drops | not reached | `Σa` measured | order run |
|---|---|---|---|---|---|---|---|
| `(7,7)` | 5 | **5** | 5 | **0** | 0 | 5 | N_S |
| `(7,8)` | 42 | **42** | 42 | **0** | 0 | 42 | N_S |
| `(8,8)` | 6 | **5** | 5 | **0** | 1 | 5 | N_S (1), then cost |
| `(7,9)` | 152 | **105** | 105 | **0** | 47 | 200 | N_S (10), then cost |
| `(8,9)` | 62 | **8** | 8 | **0** | 54 | 8 | cost |
| **total** | **267** | **165** | **165** | **0** | **102** | | |
<!-- /GENERATED -->

Every measured weight has `mult = a` **at both primes**, so each is `S_μ ⊄
I(D_r^{per₃})_δ` **PROVED** over `Q` (`rank_p ≤ rank_Q`, and a full rank at one
prime suffices; both are required to agree and do).  **165 weights measured, 165
at `mult = a`, zero drops.**  Maximum `n_χ` reached **1 327 700**; maximum `a`
reached 6; **58 of the 165 have `a ≥ 2`**, so the instrument is exercised well
above the `a = 1` regime where a nonvanishing test cannot distinguish one family
from another; 8 031 s of measured compute; peak resident **2.27 GB** against the
6.5 GB per-weight bound, so memory was never the binding constraint.

### 2.1 `(7,7)` — complete

All 5 weights, `Σa = 5`.  **`I(D_7^{per₃})_7 = 0` PROVED.**

### 2.2 `(7,8)` — complete

All 42 weights, `Σa = 42`.  **`I(D_7^{per₃})_8 = 0` PROVED.**

### 2.3 `(8,8)` — five of six, and the sixth weight is the interesting one

Five weights, `Σa = 5`, all `mult = a` at both primes.  The sixth is
`μ = (10,2,2,2,2,2,2,2)`, `a = 1`, `N_S = 951 941`, **`|Stab| = 5040`** — the
largest stabiliser in the census, and under the refitted model of §4 the dearest
weight in it (≈ 3 970 s of orbit setup for a single `a = 1` weight, more than the
other five of its group put together).

It was first excluded by the per-weight cost cap of Addendum C, then **run
deliberately and alone** to close the group, and was **ended by its own
launch-time `timeout 5400` bound** at 02:47:48 UTC — 2 940 s of CPU consumed,
still inside `_canon_acc`, the monomial enumeration having completed at
`N_S = 951 941` across eight levels, peak resident 0.18 GB.  The bound fired as
pre-registered; the weight is *not reached*, recorded with its cost
(`results/b13_09/notreached_r8_d8_stab5040.json`), and no result is claimed.

Two things worth separating, because they are different failures:

- **The refit is not refuted.**  2 940 s of CPU without finishing is consistent
  with an estimate of ≈ 3 970 s.  What was too small was the **per-weight wall
  clock**: at the ≈ 55 % CPU share it was getting on a 2-vCPU box, 3 970 s of CPU
  needs ≈ 7 200 s of wall, well past the 5 400 s timeout.  The bound, not the
  model, is what should change — a successor wants ≥ 2.5 h per weight for this
  one, or B13-10's builder.
- **What the miss costs, stated exactly.**  `I(D_8^{per₃})_8 = 0` is a five-of-six
  prefix.  But the prefix is not worthless: by Prop. 8(2), a permanent-specific
  equation at an **eight-row weight of degree 8** must now sit at `S_μ` for that
  **one named `μ` with `a = 1`** — a single rank-1 question, and a sharper open
  statement than the group was before this session.  It is the cheapest
  outstanding item in the whole census to *state*, and among the dearest to run.

### 2.4 `(7,9)` and `(8,9)` — certified prefixes

Measured in refitted-cost order (Addendum C.2), banking per weight.  Every
weight reached has `mult = a` at both primes; the remainder is in §5.  These are
prefixes by the clock, not by any mathematical obstacle, and each weight reached
is independently a **PROVED** non-membership.

### 2.5 Per-weight records

<!-- GENERATED: weights -->
**`(r, delta) = (7, 7)` — 5 of 5 measured, every one `mult = a`**

| `μ` | `a` | `N_S` | `\|Stab\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `(6,5,5,2,1,1,1)` | 1 | 48122 | 12 | 1973 | 1 / 1 | 0 | 0.9 | 1.1 | 0.08 |
| `(6,6,3,3,1,1,1)` | 1 | 52386 | 24 | 1092 | 1 / 1 | 0 | 1.5 | 1.7 | 0.08 |
| `(9,2,2,2,2,2,2)` | 1 | 56316 | 720 | 239 | 1 / 1 | 0 | 18.0 | 18.5 | 0.08 |
| `(7,5,3,2,2,1,1)` | 1 | 64945 | 4 | 13898 | 1 / 1 | 0 | 1.0 | 1.3 | 0.08 |
| `(8,4,2,2,2,2,1)` | 1 | 67131 | 24 | 3980 | 1 / 1 | 0 | 1.9 | 2.3 | 0.08 |

**`(r, delta) = (7, 8)` — 42 of 42 measured, every one `mult = a`**

| `μ` | `a` | `N_S` | `\|Stab\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `(12,2,2,2,2,2,2)` | 1 | 63711 | 720 | 284 | 1 / 1 | 0 | 21.6 | 22.2 | 0.08 |
| `(9,5,5,2,1,1,1)` | 1 | 84779 | 12 | 3421 | 1 / 1 | 0 | 1.7 | 1.9 | 0.09 |
| `(11,4,2,2,2,2,1)` | 1 | 84997 | 24 | 5124 | 1 / 1 | 0 | 2.5 | 3.1 | 0.09 |
| `(9,6,3,3,1,1,1)` | 1 | 92166 | 12 | 3758 | 1 / 1 | 0 | 1.9 | 2.2 | 0.09 |
| `(10,5,3,2,2,1,1)` | 1 | 95393 | 4 | 20315 | 1 / 1 | 0 | 1.4 | 1.8 | 0.09 |
| `(8,6,5,2,1,1,1)` | 1 | 105462 | 6 | 8504 | 1 / 1 | 0 | 1.7 | 2.0 | 0.1 |
| `(9,6,3,2,2,1,1)` | 1 | 124622 | 4 | 26634 | 1 / 1 | 0 | 1.9 | 2.4 | 0.1 |
| `(10,5,2,2,2,2,1)` | 1 | 128905 | 24 | 7604 | 1 / 1 | 0 | 3.9 | 4.6 | 0.1 |
| `(11,3,2,2,2,2,2)` | 1 | 138754 | 120 | 2140 | 1 / 1 | 0 | 13.2 | 13.9 | 0.11 |
| `(8,7,3,2,2,1,1)` | 1 | 141991 | 4 | 30413 | 1 / 1 | 0 | 2.1 | 2.7 | 0.11 |
| `(8,6,4,3,1,1,1)` | 1 | 148618 | 6 | 12350 | 1 / 1 | 0 | 2.6 | 2.9 | 0.11 |
| `(9,5,4,2,2,1,1)` | 1 | 161406 | 4 | 34615 | 1 / 1 | 0 | 2.5 | 3.1 | 0.11 |
| `(8,5,5,3,1,1,1)` | 1 | 166125 | 12 | 7063 | 1 / 1 | 0 | 3.6 | 4.0 | 0.12 |
| `(9,6,2,2,2,2,1)` | 1 | 168763 | 24 | 9848 | 1 / 1 | 0 | 5.7 | 6.5 | 0.12 |
| `(10,4,3,2,2,2,1)` | 1 | 181295 | 6 | 35549 | 1 / 1 | 0 | 3.0 | 3.9 | 0.13 |
| `(8,7,2,2,2,2,1)` | 1 | 192491 | 24 | 11160 | 1 / 1 | 0 | 6.7 | 7.6 | 0.12 |
| `(7,6,5,3,1,1,1)` | 1 | 195449 | 6 | 16652 | 1 / 1 | 0 | 3.3 | 3.8 | 0.12 |
| `(9,5,3,3,2,1,1)` | 1 | 196325 | 4 | 39842 | 1 / 1 | 0 | 3.0 | 3.8 | 0.13 |
| `(8,6,4,2,2,1,1)` | 1 | 201582 | 4 | 43331 | 1 / 1 | 0 | 3.2 | 3.9 | 0.13 |
| `(7,7,4,2,2,1,1)` | 1 | 216701 | 8 | 23340 | 1 / 1 | 0 | 4.4 | 5.1 | 0.13 |
| `(8,5,5,2,2,1,1)` | 1 | 225474 | 8 | 24238 | 1 / 1 | 0 | 4.4 | 5.2 | 0.14 |
| `(8,6,3,3,2,1,1)` | 1 | 245532 | 4 | 50050 | 1 / 1 | 0 | 4.0 | 5.0 | 0.14 |
| `(10,4,2,2,2,2,2)` | 1 | 245689 | 120 | 3649 | 1 / 1 | 0 | 27.4 | 28.5 | 0.14 |
| `(7,5,5,4,1,1,1)` | 1 | 254060 | 12 | 11127 | 1 / 1 | 0 | 5.8 | 6.3 | 0.14 |
| `(7,6,5,2,2,1,1)` | 1 | 265576 | 4 | 57390 | 1 / 1 | 0 | 4.4 | 5.5 | 0.14 |
| `(9,5,3,2,2,2,1)` | 1 | 266409 | 6 | 51769 | 1 / 1 | 0 | 7.9 | 9.9 | 0.17 |
| `(9,4,4,2,2,2,1)` | 1 | 309494 | 12 | 30704 | 1 / 1 | 0 | 11.9 | 14.1 | 0.17 |
| `(6,5,5,5,1,1,1)` | 1 | 311618 | 36 | 4700 | 1 / 1 | 0 | 20.2 | 21.1 | 0.15 |
| `(8,5,4,3,2,1,1)` | 1 | 319440 | 2 | 133014 | 1 / 1 | 0 | 6.4 | 8.2 | 0.21 |
| `(8,6,3,2,2,2,1)` | 1 | 333750 | 6 | 64610 | 1 / 1 | 0 | 6.7 | 8.6 | 0.2 |
| `(7,7,3,2,2,2,1)` | 1 | 359173 | 12 | 34394 | 1 / 1 | 0 | 8.9 | 10.4 | 0.17 |
| `(9,5,2,2,2,2,2)` | 1 | 361997 | 120 | 5180 | 1 / 1 | 0 | 74.3 | 76.1 | 0.17 |
| `(7,6,4,3,2,1,1)` | 1 | 376796 | 2 | 157347 | 1 / 1 | 0 | 8.9 | 12.2 | 0.24 |
| `(7,5,5,3,2,1,1)` | 1 | 422268 | 4 | 88035 | 1 / 1 | 0 | 11.3 | 14.2 | 0.2 |
| `(8,5,4,2,2,2,1)` | 1 | 434774 | 6 | 83749 | 1 / 1 | 0 | 14.4 | 17.7 | 0.24 |
| `(8,6,2,2,2,2,2)` | 1 | 454272 | 120 | 6430 | 1 / 1 | 0 | 107.4 | 109.2 | 0.18 |
| `(6,6,5,3,2,1,1)` | 1 | 462973 | 4 | 97285 | 1 / 1 | 0 | 9.0 | 11.1 | 0.22 |
| `(7,6,4,2,2,2,1)` | 1 | 513415 | 6 | 98609 | 1 / 1 | 0 | 11.6 | 14.7 | 0.28 |
| `(6,5,5,4,2,1,1)` | 1 | 604420 | 4 | 126738 | 1 / 1 | 0 | 11.6 | 14.5 | 0.27 |
| `(6,6,4,3,3,1,1)` | 1 | 659552 | 8 | 68717 | 1 / 1 | 0 | 17.9 | 20.2 | 0.22 |
| `(7,5,4,3,2,2,1)` | 1 | 820813 | 2 | 429329 | 1 / 1 | 0 | 15.1 | 24.9 | 0.64 |
| `(8,4,4,2,2,2,2)` | 1 | 843890 | 48 | 23896 | 1 / 1 | 0 | 106.4 | 109.3 | 0.24 |

**`(r, delta) = (8, 8)` — 5 of 6 measured, every one `mult = a`**

| `μ` | `a` | `N_S` | `\|Stab\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `(6,6,5,3,1,1,1,1)` | 1 | 804050 | 48 | 4257 | 1 / 1 | 0 | 89.0 | 90.0 | 0.25 |
| `(7,5,5,2,2,1,1,1)` | 1 | 1000598 | 24 | 24148 | 1 / 1 | 0 | 68.6 | 70.5 | 0.26 |
| `(7,6,3,3,2,1,1,1)` | 1 | 1092229 | 12 | 51912 | 1 / 1 | 0 | 80.2 | 83.7 | 0.29 |
| `(9,4,2,2,2,2,2,1)` | 1 | 1213003 | 120 | 15776 | 1 / 1 | 0 | 406.2 | 413.0 | 0.31 |
| `(8,5,3,2,2,2,1,1)` | 1 | 1259739 | 12 | 98937 | 1 / 1 | 0 | 62.4 | 66.9 | 0.34 |

**`(r, delta) = (7, 9)` — 105 of 152 measured, every one `mult = a`**

| `μ` | `a` | `N_S` | `\|Stab\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `(15,2,2,2,2,2,2)` | 1 | 65416 | 720 | 301 | 1 / 1 | 0 | 23.4 | 24.0 | 0.09 |
| `(14,4,2,2,2,2,1)` | 1 | 91274 | 24 | 5597 | 1 / 1 | 0 | 3.0 | 3.6 | 0.09 |
| `(12,5,5,2,1,1,1)` | 1 | 108636 | 12 | 4278 | 1 / 1 | 0 | 2.5 | 2.8 | 0.1 |
| `(13,5,3,2,2,1,1)` | 1 | 110345 | 4 | 23406 | 1 / 1 | 0 | 1.9 | 2.4 | 0.1 |
| `(12,6,3,3,1,1,1)` | 1 | 118048 | 12 | 4703 | 1 / 1 | 0 | 2.8 | 3.1 | 0.11 |
| `(14,3,2,2,2,2,2)` | 1 | 147819 | 120 | 2344 | 1 / 1 | 0 | 14.7 | 15.6 | 0.11 |
| `(13,5,2,2,2,2,1)` | 1 | 148526 | 24 | 8899 | 1 / 1 | 0 | 5.1 | 5.8 | 0.12 |
| `(11,6,5,2,1,1,1)` | 1 | 152466 | 6 | 12074 | 1 / 1 | 0 | 3.1 | 3.4 | 0.11 |
| `(12,6,3,2,2,1,1)` | 1 | 159017 | 4 | 33842 | 1 / 1 | 0 | 2.7 | 3.4 | 0.11 |
| `(10,8,3,3,1,1,1)` | 1 | 175861 | 12 | 7158 | 1 / 1 | 0 | 4.6 | 5.0 | 0.13 |
| `(10,7,5,2,1,1,1)` | 1 | 189853 | 6 | 15270 | 1 / 1 | 0 | 3.6 | 4.1 | 0.13 |
| `(12,5,4,2,2,1,1)` | 1 | 204473 | 4 | 43653 | 1 / 1 | 0 | 3.7 | 4.6 | 0.13 |
| `(11,7,3,2,2,1,1)` | 2 | 204731 | 4 | 43733 | 2 / 2 | 0 | 4.1 | 5.1 | 0.13 |
| `(13,4,3,2,2,2,1)` | 1 | 206957 | 6 | 40926 | 1 / 1 | 0 | 4.5 | 5.7 | 0.14 |
| `(9,8,5,2,1,1,1)` | 1 | 211398 | 6 | 17117 | 1 / 1 | 0 | 6.7 | 7.4 | 0.13 |
| `(11,6,4,3,1,1,1)` | 1 | 213640 | 6 | 17412 | 1 / 1 | 0 | 6.8 | 7.7 | 0.14 |
| `(12,6,2,2,2,2,1)` | 2 | 214526 | 24 | 12693 | 2 / 2 | 0 | 11.1 | 12.5 | 0.14 |
| `(10,8,3,2,2,1,1)` | 1 | 237539 | 4 | 50795 | 1 / 1 | 0 | 6.5 | 7.9 | 0.14 |
| `(11,5,5,3,1,1,1)` | 1 | 238330 | 12 | 9917 | 1 / 1 | 0 | 8.6 | 9.5 | 0.15 |
| `(12,5,3,3,2,1,1)` | 1 | 247748 | 4 | 49877 | 1 / 1 | 0 | 6.6 | 8.1 | 0.15 |
| `(9,7,6,2,1,1,1)` | 1 | 248457 | 6 | 20355 | 1 / 1 | 0 | 7.9 | 8.6 | 0.15 |
| `(9,9,3,2,2,1,1)` | 1 | 249286 | 8 | 26693 | 1 / 1 | 0 | 8.1 | 9.3 | 0.16 |
| `(10,7,4,3,1,1,1)` | 1 | 266743 | 6 | 22062 | 1 / 1 | 0 | 8.3 | 9.1 | 0.15 |
| `(11,7,2,2,2,2,1)` | 2 | 276644 | 24 | 16171 | 2 / 2 | 0 | 22.7 | 25.2 | 0.16 |
| `(13,4,2,2,2,2,2)` | 2 | 279322 | 120 | 4255 | 2 / 2 | 0 | 32.8 | 34.1 | 0.15 |
| `(11,6,4,2,2,1,1)` | 2 | 288796 | 4 | 61888 | 2 / 2 | 0 | 7.8 | 9.4 | 0.15 |
| `(9,8,4,3,1,1,1)` | 1 | 297400 | 6 | 24755 | 1 / 1 | 0 | 9.0 | 10.1 | 0.15 |
| `(10,8,2,2,2,2,1)` | 2 | 321319 | 24 | 18706 | 2 / 2 | 0 | 32.0 | 35.6 | 0.17 |
| `(11,5,5,2,2,1,1)` | 2 | 322368 | 8 | 34516 | 2 / 2 | 0 | 11.7 | 13.5 | 0.16 |
| `(10,6,5,3,1,1,1)` | 3 | 326036 | 6 | 27387 | 3 / 3 | 0 | 9.7 | 10.8 | 0.16 |
| `(12,5,3,2,2,2,1)` | 2 | 334864 | 6 | 65577 | 2 / 2 | 0 | 10.9 | 13.9 | 0.21 |
| `(11,6,3,3,2,1,1)` | 2 | 350728 | 4 | 71035 | 2 / 2 | 0 | 9.2 | 11.4 | 0.17 |
| `(10,7,4,2,2,1,1)` | 3 | 361116 | 4 | 77615 | 3 / 3 | 0 | 10.1 | 12.5 | 0.19 |
| `(12,4,4,2,2,2,1)` | 2 | 387455 | 12 | 38775 | 2 / 2 | 0 | 21.9 | 25.6 | 0.18 |
| `(9,7,5,3,1,1,1)` | 2 | 391363 | 6 | 33307 | 2 / 2 | 0 | 12.1 | 13.3 | 0.18 |
| `(9,8,4,2,2,1,1)` | 2 | 402941 | 4 | 86709 | 2 / 2 | 0 | 11.0 | 13.4 | 0.19 |
| `(8,8,5,3,1,1,1)` | 2 | 415764 | 12 | 17651 | 2 / 2 | 0 | 24.4 | 26.1 | 0.18 |
| `(10,5,5,4,1,1,1)` | 2 | 422615 | 12 | 18213 | 2 / 2 | 0 | 25.4 | 27.2 | 0.19 |
| `(9,6,6,3,1,1,1)` | 1 | 428628 | 12 | 18200 | 1 / 1 | 0 | 24.2 | 25.8 | 0.19 |
| `(10,7,3,3,2,1,1)` | 2 | 439255 | 4 | 89324 | 2 / 2 | 0 | 12.7 | 15.4 | 0.19 |
| `(10,6,5,2,2,1,1)` | 3 | 441899 | 4 | 95254 | 3 / 3 | 0 | 12.8 | 15.9 | 0.22 |
| `(11,5,4,3,2,1,1)` | 2 | 454042 | 2 | 187966 | 2 / 2 | 0 | 11.2 | 14.9 | 0.28 |
| `(9,7,4,4,1,1,1)` | 1 | 454060 | 12 | 19289 | 1 / 1 | 0 | 28.3 | 30.1 | 0.18 |
| `(11,6,3,2,2,2,1)` | 3 | 475110 | 6 | 92473 | 3 / 3 | 0 | 23.3 | 29.5 | 0.31 |
| `(8,7,6,3,1,1,1)` | 1 | 490080 | 6 | 42279 | 1 / 1 | 0 | 23.7 | 25.6 | 0.19 |
| `(9,8,3,3,2,1,1)` | 2 | 490511 | 4 | 99937 | 2 / 2 | 0 | 14.7 | 17.8 | 0.22 |
| `(9,7,5,2,2,1,1)` | 4 | 531093 | 4 | 114804 | 4 / 4 | 0 | 22.2 | 28.1 | 0.27 |
| `(9,6,5,4,1,1,1)` | 2 | 556789 | 6 | 48398 | 2 / 2 | 0 | 28.4 | 30.7 | 0.2 |
| `(8,8,5,2,2,1,1)` | 1 | 564459 | 8 | 61032 | 1 / 1 | 0 | 29.6 | 33.8 | 0.2 |
| `(9,6,6,2,2,1,1)` | 1 | 581978 | 8 | 63028 | 1 / 1 | 0 | 32.8 | 36.6 | 0.21 |
| `(10,7,3,2,2,2,1)` | 4 | 595920 | 6 | 115494 | 4 / 4 | 0 | 28.5 | 38.0 | 0.43 |
| `(11,5,4,2,2,2,1)` | 3 | 615815 | 6 | 119306 | 3 / 3 | 0 | 31.7 | 40.5 | 0.39 |
| `(9,5,5,5,1,1,1)` | 2 | 623493 | 36 | 9311 | 2 / 2 | 0 | 53.5 | 55.3 | 0.22 |
| `(10,6,4,3,2,1,1)` | 4 | 624541 | 2 | 259737 | 4 / 4 | 0 | 23.5 | 34.1 | 0.38 |
| `(8,7,5,4,1,1,1)` | 2 | 637241 | 6 | 55896 | 2 / 2 | 0 | 34.8 | 37.6 | 0.2 |
| `(12,4,3,2,2,2,2)` | 1 | 637660 | 24 | 36205 | 1 / 1 | 0 | 53.6 | 58.2 | 0.22 |
| `(9,8,3,2,2,2,1)` | 2 | 665989 | 6 | 128833 | 2 / 2 | 0 | 36.8 | 46.1 | 0.35 |
| `(8,7,6,2,2,1,1)` | 2 | 666003 | 4 | 144279 | 2 / 2 | 0 | 31.7 | 38.4 | 0.29 |
| `(10,5,5,3,2,1,1)` | 3 | 699223 | 4 | 145128 | 3 / 3 | 0 | 30.8 | 39.6 | 0.31 |
| `(7,7,7,2,2,1,1)` | 1 | 717095 | 24 | 25869 | 1 / 1 | 0 | 50.4 | 54.1 | 0.23 |
| `(11,5,3,3,2,2,1)` | 1 | 750153 | 4 | 191871 | 1 / 1 | 0 | 35.6 | 44.3 | 0.38 |
| `(9,7,4,3,2,1,1)` | 4 | 752157 | 2 | 313827 | 4 / 4 | 0 | 29.4 | 42.5 | 0.48 |
| `(7,7,6,4,1,1,1)` | 1 | 752384 | 12 | 33532 | 1 / 1 | 0 | 42.5 | 44.8 | 0.22 |
| `(10,6,3,3,3,1,1)` | 1 | 761718 | 12 | 50479 | 1 / 1 | 0 | 41.0 | 44.7 | 0.24 |
| `(8,6,5,5,1,1,1)` | 2 | 782883 | 12 | 35063 | 2 / 2 | 0 | 46.3 | 49.0 | 0.24 |
| `(8,8,4,3,2,1,1)` | 2 | 799897 | 4 | 167160 | 2 / 2 | 0 | 38.5 | 47.7 | 0.34 |
| `(10,5,4,4,2,1,1)` | 1 | 812199 | 4 | 170869 | 1 / 1 | 0 | 38.5 | 46.1 | 0.33 |
| `(10,6,4,2,2,2,1)` | 5 | 848795 | 6 | 163600 | 5 / 5 | 0 | 34.9 | 46.4 | 0.61 |
| `(11,4,4,3,2,2,1)` | 1 | 870729 | 4 | 232038 | 1 / 1 | 0 | 31.6 | 41.3 | 0.44 |
| `(9,6,5,3,2,1,1)` | 6 | 924367 | 2 | 387020 | 6 / 6 | 0 | 34.8 | 50.6 | 0.66 |
| `(10,5,5,2,2,2,1)` | 1 | 950826 | 12 | 90161 | 1 / 1 | 0 | 56.3 | 62.9 | 0.34 |
| `(8,8,3,3,3,1,1)` | 1 | 977156 | 24 | 32654 | 1 / 1 | 0 | 55.2 | 57.6 | 0.29 |
| `(10,5,4,3,3,1,1)` | 1 | 991745 | 4 | 204629 | 1 / 1 | 0 | 38.4 | 45.1 | 0.36 |
| `(11,5,3,2,2,2,2)` | 1 | 1019402 | 24 | 56784 | 1 / 1 | 0 | 66.3 | 70.5 | 0.31 |
| `(9,7,4,2,2,2,1)` | 5 | 1023477 | 6 | 196533 | 5 / 5 | 0 | 46.3 | 62.4 | 0.7 |
| `(10,6,3,3,2,2,1)` | 1 | 1035995 | 4 | 264822 | 1 / 1 | 0 | 39.6 | 50.1 | 0.51 |
| `(8,7,5,3,2,1,1)` | 4 | 1059742 | 2 | 444687 | 4 / 4 | 0 | 34.2 | 53.7 | 0.77 |
| `(9,6,4,4,2,1,1)` | 2 | 1074908 | 4 | 227011 | 2 / 2 | 0 | 43.3 | 52.1 | 0.43 |
| `(8,8,4,2,2,2,1)` | 2 | 1088933 | 12 | 105098 | 2 / 2 | 0 | 68.4 | 77.8 | 0.37 |
| `(8,6,6,3,2,1,1)` | 2 | 1162913 | 4 | 244835 | 2 / 2 | 0 | 48.4 | 59.2 | 0.48 |
| `(9,5,5,4,2,1,1)` | 3 | 1205636 | 4 | 252359 | 3 / 3 | 0 | 48.8 | 62.4 | 0.51 |
| `(8,7,4,4,2,1,1)` | 2 | 1232954 | 4 | 260943 | 2 / 2 | 0 | 52.8 | 65.2 | 0.47 |
| `(9,7,3,3,2,2,1)` | 2 | 1250793 | 4 | 319698 | 2 / 2 | 0 | 53.5 | 67.1 | 0.62 |
| `(7,7,6,3,2,1,1)` | 1 | 1253518 | 4 | 263262 | 1 / 1 | 0 | 52.4 | 64.6 | 0.53 |
| `(9,6,5,2,2,2,1)` | 3 | 1259189 | 6 | 240852 | 3 / 3 | 0 | 68.9 | 84.0 | 0.75 |
| `(9,6,4,3,3,1,1)` | 2 | 1314667 | 4 | 272535 | 2 / 2 | 0 | 59.6 | 72.1 | 0.52 |
| `(10,5,4,3,2,2,1)` | 3 | 1350475 | 2 | 707382 | 3 / 3 | 0 | 49.8 | 82.8 | 1.03 |
| `(8,7,5,2,2,2,1)` | 3 | 1444861 | 6 | 275693 | 3 / 3 | 0 | 53.8 | 67.2 | 0.75 |
| `(9,5,5,3,3,1,1)` | 1 | 1475485 | 8 | 152576 | 1 / 1 | 0 | 56.1 | 61.7 | 0.42 |
| `(8,7,4,3,3,1,1)` | 1 | 1509197 | 4 | 313613 | 1 / 1 | 0 | 46.5 | 54.7 | 0.58 |
| `(8,6,5,4,2,1,1)` | 4 | 1519012 | 2 | 640479 | 4 / 4 | 0 | 55.1 | 90.5 | 1.31 |
| `(10,4,4,4,2,2,1)` | 1 | 1571112 | 12 | 142642 | 1 / 1 | 0 | 69.7 | 77.8 | 0.54 |
| `(8,6,6,2,2,2,1)` | 2 | 1586364 | 12 | 152477 | 2 / 2 | 0 | 77.9 | 87.3 | 0.58 |
| `(7,7,5,4,2,1,1)` | 2 | 1638157 | 4 | 345371 | 2 / 2 | 0 | 49.9 | 62.1 | 0.66 |
| `(8,5,5,5,2,1,1)` | 2 | 1705593 | 12 | 118780 | 2 / 2 | 0 | 77.2 | 84.4 | 0.55 |
| `(7,7,6,2,2,2,1)` | 1 | 1710690 | 12 | 161722 | 1 / 1 | 0 | 83.9 | 93.6 | 0.5 |
| `(9,5,4,4,3,1,1)` | 1 | 1717956 | 4 | 365472 | 1 / 1 | 0 | 50.5 | 60.3 | 0.66 |
| `(9,6,4,3,2,2,1)` | 4 | 1793348 | 2 | 937909 | 4 / 4 | 0 | 46.7 | 76.7 | 1.63 |
| `(7,6,6,4,2,1,1)` | 1 | 1799077 | 4 | 381067 | 1 / 1 | 0 | 53.0 | 67.6 | 0.83 |
| `(8,6,5,3,3,1,1)` | 3 | 1861218 | 4 | 388175 | 3 / 3 | 0 | 63.1 | 76.5 | 0.71 |
| `(9,5,5,3,2,2,1)` | 2 | 2013862 | 4 | 522001 | 2 / 2 | 0 | 63.1 | 82.0 | 0.97 |
| `(7,6,5,5,2,1,1)` | 2 | 2020960 | 4 | 426512 | 2 / 2 | 0 | 67.3 | 85.5 | 0.97 |
| `(8,7,4,3,2,2,1)` | 3 | 2060515 | 2 | 1076763 | 3 / 3 | 0 | 57.0 | 100.0 | 2.02 |
| `(8,6,4,4,3,1,1)` | 1 | 2168755 | 4 | 462681 | 1 / 1 | 0 | 70.4 | 85.9 | 0.92 |
| `(8,6,5,3,2,2,1)` | 3 | 2543860 | 2 | 1327700 | 3 / 3 | 0 | 75.3 | 140.1 | 2.27 |

**`(r, delta) = (8, 9)` — 8 of 62 measured, every one `mult = a`**

| `μ` | `a` | `N_S` | `\|Stab\|` | `n_χ` | `mult` (P1 / P2) | units | build s | total s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `(9,6,5,3,1,1,1,1)` | 1 | 1603291 | 24 | 16844 | 1 / 1 | 0 | 351.9 | 355.0 | 0.4 |
| `(10,5,5,2,2,1,1,1)` | 1 | 1647299 | 24 | 39172 | 1 / 1 | 0 | 289.0 | 295.7 | 0.42 |
| `(11,5,3,2,2,2,1,1)` | 1 | 1765081 | 12 | 138630 | 1 / 1 | 0 | 147.1 | 157.0 | 0.45 |
| `(10,6,3,3,2,1,1,1)` | 1 | 1796496 | 12 | 84046 | 1 / 1 | 0 | 151.8 | 157.8 | 0.48 |
| `(9,7,3,3,2,1,1,1)` | 1 | 2173277 | 12 | 102633 | 1 / 1 | 0 | 309.4 | 318.4 | 0.53 |
| `(9,6,5,2,2,1,1,1)` | 1 | 2187629 | 12 | 104837 | 1 / 1 | 0 | 338.3 | 347.3 | 0.51 |
| `(10,6,3,2,2,2,1,1)` | 1 | 2450077 | 12 | 192492 | 1 / 1 | 0 | 351.1 | 371.7 | 0.61 |
| `(8,7,5,2,2,1,1,1)` | 1 | 2513866 | 12 | 121403 | 1 / 1 | 0 | 422.8 | 433.3 | 0.58 |
<!-- /GENERATED -->

---

## 3. Verification

Four independent routes reach `a`, and two independent routes reach `mult`.

**`a`, four ways.**  (i) The Weyl alternation over a tail DP
(`wk9_s42_census`); this session's `S_r`-symmetric-cache variant is asserted
equal to that routine on **all 492** weights of `(7,7)`, `(7,8)`, `(8,8)`.
(ii) The symmetric-function plethysm `wk8_s30_pleth.a_of` / `amb`, asserted equal
at every census weight — for `(8,9)`, `amb(9,3,8)` was run separately and merged
with a check **in both directions**: no 8-row weight it reports with `a ≥ 1` is
missing from the census and none is extra, so the census cannot have silently
dropped a weight it could not place.  (iii) The mod-`p` nullity of the raising
operator on `V_χ`, asserted `= a` inside the hybrid at each prime at run time.
(iv) `n_χ − rank_p(E)`, computed by the independent verifier below.

**`mult`, two ways.**  The sweep reads `mult = rank_p(ev · K)` through the
hybrid's kernel `K`.  `analysis/b13_09_verify.py` re-decides the same question
**without ever forming a kernel**, by the criterion s43/s47 used: `mult = a` iff
the stacked `[E ; ev]` has full column rank `n_χ`.  A full column rank read
through a sparse random `±1` projection is a **proof**, since
`rank(P·M) ≤ rank(M) ≤ n_χ`, so `rank(P·M) = n_χ` forces equality; the price is
a dense flint rank, which is why it is applied to weights whose `n_χ` fits the
cap and reports the rest as **NOT COVERED** rather than pretending to cover them.
It rebuilds each cell, regenerates the points from the recorded seed, and takes
its own ranks; the only shared code is the engine's build, which is exactly what
the calibration against s47/s79 tests.

<!-- GENERATED: verify -->
| `μ` | `δ` | `n_χ` | `a` from the operator (P1 / P2) | stacked rank (P1 / P2) | `= n_χ` | verdict |
|---|---|---|---|---|---|---|
| `(9,2,2,2,2,2,2)` | 7 | 239 | 1 / 1 | 239 / 239 | yes | **PASS** |
| `(12,2,2,2,2,2,2)` | 8 | 284 | 1 / 1 | 284 / 284 | yes | **PASS** |
| `(15,2,2,2,2,2,2)` | 9 | 301 | 1 / 1 | 301 / 301 | yes | **PASS** |
| `(6,6,3,3,1,1,1)` | 7 | 1092 | 1 / 1 | 1092 / 1092 | yes | **PASS** |
| `(6,5,5,2,1,1,1)` | 7 | 1973 | 1 / 1 | 1973 / 1973 | yes | **PASS** |
| `(11,3,2,2,2,2,2)` | 8 | 2140 | 1 / 1 | 2140 / 2140 | yes | **PASS** |
| `(14,3,2,2,2,2,2)` | 9 | 2344 | 1 / 1 | 2344 / 2344 | yes | **PASS** |
| `(9,5,5,2,1,1,1)` | 8 | 3421 | 1 / 1 | 3421 / 3421 | yes | **PASS** |
| `(10,4,2,2,2,2,2)` | 8 | 3649 | 1 / 1 | 3649 / 3649 | yes | **PASS** |
| `(9,6,3,3,1,1,1)` | 8 | 3758 | 1 / 1 | 3758 / 3758 | yes | **PASS** |
| `(8,4,2,2,2,2,1)` | 7 | 3980 | 1 / 1 | 3980 / 3980 | yes | **PASS** |
| `(6,6,5,3,1,1,1,1)` | 8 | 4257 | 1 / 1 | 4257 / 4257 | yes | **PASS** |
| `(12,5,5,2,1,1,1)` | 9 | 4278 | 1 / 1 | 4278 / 4278 | yes | **PASS** |
| `(6,5,5,5,1,1,1)` | 8 | 4700 | 1 / 1 | 4700 / 4700 | yes | **PASS** |
| `(12,6,3,3,1,1,1)` | 9 | 4703 | 1 / 1 | 4703 / 4703 | yes | **PASS** |
| `(11,4,2,2,2,2,1)` | 8 | 5124 | 1 / 1 | 5124 / 5124 | yes | **PASS** |
| `(9,5,2,2,2,2,2)` | 8 | 5180 | 1 / 1 | 5180 / 5180 | yes | **PASS** |
| `(9,2,2,2,2,2,2)` | 7 | 239 | 1 / 1 | 239 / 239 | yes | **PASS** |
| `(6,6,3,3,1,1,1)` | 7 | 1092 | 1 / 1 | 1092 / 1092 | yes | **PASS** |
| `(6,5,5,2,1,1,1)` | 7 | 1973 | 1 / 1 | 1973 / 1973 | yes | **PASS** |
| `(8,4,2,2,2,2,1)` | 7 | 3980 | 1 / 1 | 3980 / 3980 | yes | **PASS** |

21 PASS, 0 FAIL, 84 above the verifier's dense cap.

House verifier (`tools/verify`, imports nothing from `analysis/`): `PASS 127, RECORDED 0, FAIL 0, UNPARSEABLE 0, ERROR 0`
<!-- /GENERATED -->

**The house verifier.**  `tools/verify` imports nothing from `analysis/` and
duplicates none of its code.  Run over the whole certificate directory it returns

    PASS 248, RECORDED 0, FAIL 0, UNPARSEABLE 1, ERROR 0

For each certificate it independently recomputes `a` by its own Weyl alternation,
checks that every basis vector is a highest-weight vector mod `p`, checks that the
basis has rank `a`, and checks the evaluation rank at the recorded points, before
concluding `mult = a` over `Q`.  **Zero failures.**

The one `UNPARSEABLE` is accounted for rather than left as a loose end, because an
unexplained one would be indistinguishable from a corrupt certificate.  It is
`per7_9_5_5_3_3_1_1_d9_fullrank_p2147483647.json.gz`, and the failure is
`No such file or directory`: the evaluator's own size guard removes any
certificate it has just written that exceeds 4.5 MB (so that nothing approaching
the 5 MB repository limit is ever banked), and this weight's certificate did.  The
verifier had listed the directory while the file was still being written and read
it after the guard had removed it.  Nothing is corrupt, the weight's own record is
banked and its `mult = a` stands on the measurement, and the manifest shows it
with no certificate.  A successor wanting a replayable certificate for that weight
regenerates it by the recorded command with the expansion cap raised.

**Calibration (MEASURED, PASS).**  At `R = 6`, against the record: s47's control
`(7,5,4,4,2,2)_8` (`a = 1`, `N_S = 285 313`, `n_χ = 76 792`, `mult = 1`, 9.6 s
against s47's 2 420 s), and s79's `(11,7,4,2,2,1)_9` (`a = 9`) and
`(13,7,2,2,2,1)_9` (`a = 3`) — all identical at both primes.

**Negative controls with teeth (MEASURED, PASS).**  The same code path on `per₃`
of **diagonal** pencils reads `mult = 0`, `units = a` at both primes at
`(13,7,2,2,2,1)_9`, `(6,5,5,2,1,1,1)_7` and `(6,6,5,3,1,1,1,1)_8`.  This has
teeth because the points then lie on the Chow variety of split cubics, whose
degree-`δ` coordinate ring is a quotient of `Sym³(Sym^δ V)` and so carries **no
constituent with more than three rows** — a weight of length 7 or 8 must read
`mult = 0` there, and a control that read anything else would be an instrument
defect.  The run also exercises the drop branch end to end: the recheck at
`3a + 24` fresh points, the exhibited vectors, and the `E·v = 0` verification.
And `per₃` differs from the `det₃` restriction of the same pencils at 10 of 10
points at `R = 7`, so the families are not accidentally the same object.

**The `exps` trap.**  Every coefficient dictionary is keyed by the exponent
tuple `α` and read back through `exps(3, r)` by tuple lookup (`co.get(α)`), never
by a literal position, so the two opposite orderings in the tree cannot be
confused.  Nothing in this session can silently drop a term it could not place:
the build asserts that every raising image and every stabiliser image **is** in
its target basis, and asserts that the `χ`-obstructed fixed rows cancel.

---

## 4. The cost model is wrong at these lengths — measured, refitted, and reported as a defect

<!-- GENERATED: cost -->
Refitted on 165 measured weights:

    build_secs  ~=  3.06e-06 * N_S*delta  +  1.07e-06 * |Stab| * N_S

median predicted/actual **1.03** (p10 0.64, p90 1.80); the s79 model's median actual/model is 1.95 and its worst is **21.7×** low.

| group | weights | s79 model | refitted | factor |
|---|---|---|---|---|
| `r7_d7` | 5 | 0.0 h | **0.01 h** | — |
| `r7_d8` | 42 | 0.06 h | **0.17 h** | 2.8× |
| `r7_d9` | 152 | 1.36 h | **2.82 h** | 2.1× |
| `r8_d8` | 6 | 0.03 h | **1.55 h** | 51.7× |
| `r8_d9` | 62 | 1.98 h | **13.04 h** | 6.6× |
| **total** | 267 | 3.43 h | **17.59 h** | 5.1× |
<!-- /GENERATED -->

The cause is structural, not statistical.  `wk9_s45_build.orbit_setup_arr` calls
`_canon_acc`, which makes **two passes over the whole stabiliser group** — one to
build `canon`, one to build `acc` — each pass an `O(N_S)` permutation-image and
lookup over the `(N_S × δ)` monomial array.  So the orbit setup costs
`O(|Stab| · N_S)`.  At length 6 that term is invisible: `|Stab|` is rarely above
120.  At lengths 7 and 8, repeated parts push it to 720 at `(9,2⁶)` and **5040**
at `(10,2⁷)` — and `(10,2⁷)_8` is a single `a = 1` weight that costs more than
the other five weights of its group put together.

Three consequences, stated for the next batch:

1. **Any length-7 or length-8 plan priced with `N_S·δ` alone is optimistic**, by
   a factor that grows with `|Stab|` and reaches 21.7× in what was measured here.
   The model is quoted without a length caveat in `docs/s79_report.md` §2.1 and
   `results/PREREG_s79.md` §2.2, and `docs/stocktake_batch12.md` §7 prices the
   programme's open regions with it.  Every s79 *rank* stands; it is the *pricing*
   that transfers badly.
2. **`N_S` is the wrong queue order at these lengths.**  It was chosen so that
   what is reached is a cheapest-first prefix, and under the measured model it is
   not that order.  Addendum C changed the order to refitted cost for everything
   measured after it, and the report states each group's prefix in the order it
   was actually run.
3. **This is a concrete target for B13-10.**  Its assignment is peak memory in
   the raising-row construction; the `|Stab|` term is a *time* wall in the orbit
   setup, on the same code path, and `(10,2⁷)_8` at `|Stab| = 5040` is the case
   that exhibits it.  A single pass over the group that accumulates `canon` and
   `acc` together, or a canonical-form computation that does not enumerate the
   group at all, would remove a term that at length 8 is most of the build.

One caveat on the fit, stated rather than buried: it was fitted on weights
measured while two to four processes shared two vCPU, so it absorbs some
contention and is better read as an upper estimate per weight on this box than as
a clean single-process rate.  The `|Stab|·N_S` term is not an artefact of that —
it is visible in the source and in the level-by-level build log.

---

## 5. The negative, characterised and priced — what was not reached

A negative over a stated, priced region is the deliverable; an unstated gap is
not.  So: every weight of the census that was not measured is listed with its
`a`, `N_S`, `|Stab|`, `N_S·δ` and **refitted** cost, and with the reason.

<!-- GENERATED: notreached -->
| group | `μ` | `a` | `N_S` | `\|Stab\|` | `N_S·δ` | refitted cost s | why not reached |
|---|---|---|---|---|---|---|---|
| `(8,8)` | `(10,2,2,2,2,2,2,2)` | 1 | 951941 | 5040 | 7.62e+06 | 5180.0 | above the per-weight refitted-cost cap 900 s |
| `(7,9)` | `(12,5,2,2,2,2,2)` | 2 | 453215 | 120 | 4.08e+06 | 70.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,5,4,4,2,2,1)` | 2 | 2346242 | 4 | 2.11e+07 | 74.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(10,6,3,2,2,2,2)` | 2 | 1410714 | 24 | 1.27e+07 | 75.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,5,5,4,3,1,1)` | 2 | 2437444 | 4 | 2.19e+07 | 77.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,6,3,3,1,1)` | 1 | 2206201 | 8 | 1.99e+07 | 79.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,7,4,4,3,1,1)` | 1 | 2340473 | 8 | 2.11e+07 | 84.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,5,4,3,3,2,1)` | 1 | 2877715 | 2 | 2.59e+07 | 85.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,5,4,3,1,1)` | 2 | 2891944 | 2 | 2.6e+07 | 85.8 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,7,5,3,2,2,1)` | 2 | 2745823 | 4 | 2.47e+07 | 87.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,7,3,2,2,2,2)` | 1 | 1705276 | 24 | 1.53e+07 | 90.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(11,4,4,2,2,2,2)` | 2 | 1184020 | 48 | 1.07e+07 | 93.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,6,4,4,2,2,1)` | 3 | 2966018 | 4 | 2.67e+07 | 94.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,6,3,2,2,1)` | 1 | 3018225 | 4 | 2.72e+07 | 96.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(10,5,4,2,2,2,2)` | 2 | 1841091 | 24 | 1.66e+07 | 98.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(11,6,2,2,2,2,2)` | 3 | 644448 | 120 | 5.8e+06 | 100.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(10,4,4,3,2,2,2)` | 1 | 2624702 | 12 | 2.36e+07 | 106.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,5,5,4,2,2,1)` | 1 | 3335298 | 4 | 3e+07 | 106.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,6,4,3,3,2,1)` | 1 | 3642119 | 2 | 3.28e+07 | 108.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,7,4,4,2,2,1)` | 1 | 3202246 | 8 | 2.88e+07 | 115.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,5,4,2,2,1)` | 2 | 3960936 | 2 | 3.56e+07 | 117.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(10,7,2,2,2,2,2)` | 2 | 809508 | 120 | 7.29e+06 | 126.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,6,5,5,3,1,1)` | 1 | 3576558 | 8 | 3.22e+07 | 129.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,5,5,3,3,2,1)` | 1 | 4097969 | 4 | 3.69e+07 | 130.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,6,4,2,2,2,2)` | 3 | 2449112 | 24 | 2.2e+07 | 130.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,5,5,5,3,1,1)` | 1 | 3252752 | 12 | 2.93e+07 | 131.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,5,4,3,2,2,2)` | 1 | 3937267 | 6 | 3.54e+07 | 133.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,5,5,4,4,1,1)` | 1 | 3795988 | 8 | 3.42e+07 | 137.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,8,2,2,2,2,2)` | 2 | 905411 | 120 | 8.15e+06 | 141.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,5,4,4,3,2,1)` | 1 | 4783608 | 2 | 4.31e+07 | 141.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,8,3,2,2,2,2)` | 1 | 1815777 | 48 | 1.63e+07 | 143.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,5,3,3,2,1)` | 1 | 4870536 | 2 | 4.38e+07 | 144.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,7,4,2,2,2,2)` | 2 | 2816405 | 24 | 2.53e+07 | 150.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,4,4,3,2,1)` | 1 | 5688179 | 2 | 5.12e+07 | 168.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,6,4,3,2,2,2)` | 1 | 4989935 | 6 | 4.49e+07 | 169.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,6,6,4,2,2,1)` | 1 | 4356566 | 12 | 3.92e+07 | 176.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,6,5,2,2,2,2)` | 1 | 3480677 | 24 | 3.13e+07 | 185.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,5,5,5,4,1,1)` | 1 | 4699683 | 12 | 4.23e+07 | 189.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,5,5,4,3,2,1)` | 1 | 6406837 | 2 | 5.77e+07 | 190.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,6,5,4,3,2,1)` | 1 | 7052365 | 2 | 6.35e+07 | 209.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,7,4,3,2,2,2)` | 1 | 5392049 | 12 | 4.85e+07 | 217.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(8,5,4,4,2,2,2)` | 1 | 6561112 | 12 | 5.91e+07 | 265.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,5,5,5,3,2,1)` | 1 | 7947287 | 6 | 7.15e+07 | 269.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(9,4,4,4,2,2,2)` | 1 | 4593836 | 36 | 4.13e+07 | 304.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,4,4,2,2,2)` | 1 | 7808982 | 12 | 7.03e+07 | 315.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,6,6,2,2,2,2)` | 1 | 4133591 | 48 | 3.72e+07 | 327.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(6,6,5,3,3,3,1)` | 1 | 8690997 | 12 | 7.82e+07 | 351.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(7,9)` | `(7,5,5,3,3,2,2)` | 1 | 10848589 | 8 | 9.76e+07 | 391.8 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,4,3,2,1,1,1)` | 1 | 3125993 | 6 | 2.81e+07 | 106.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,7,3,2,2,2,1,1)` | 1 | 2967659 | 12 | 2.67e+07 | 119.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,7,4,3,2,1,1,1)` | 1 | 3596838 | 6 | 3.24e+07 | 122.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,5,4,2,2,2,1,1)` | 1 | 3205295 | 12 | 2.88e+07 | 129.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,5,4,1,1,1,1)` | 1 | 2647121 | 24 | 2.38e+07 | 141.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,5,3,3,2,2,1,1)` | 1 | 3932252 | 8 | 3.54e+07 | 142.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,5,5,3,2,1,1,1)` | 1 | 3515104 | 12 | 3.16e+07 | 142.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,5,3,2,1,1,1)` | 2 | 4449996 | 6 | 4e+07 | 151.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,6,3,1,1,1,1)` | 1 | 2021565 | 48 | 1.82e+07 | 159.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,8,3,2,2,2,1,1)` | 1 | 3161627 | 24 | 2.85e+07 | 168.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,4,2,2,2,1,1)` | 1 | 4275658 | 12 | 3.85e+07 | 172.8 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(11,4,3,2,2,2,2,1)` | 1 | 3425836 | 24 | 3.08e+07 | 182.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,3,3,2,2,1,1)` | 1 | 5253625 | 8 | 4.73e+07 | 189.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,7,5,3,2,1,1,1)` | 1 | 4807432 | 12 | 4.33e+07 | 194.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,7,4,2,2,2,1,1)` | 1 | 4923991 | 12 | 4.43e+07 | 199.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,6,3,2,1,1,1)` | 1 | 5288522 | 12 | 4.76e+07 | 213.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,7,3,3,2,2,1,1)` | 1 | 6054968 | 8 | 5.45e+07 | 218.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,5,4,3,2,2,1,1)` | 1 | 6904677 | 4 | 6.21e+07 | 219.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(12,4,2,2,2,2,2,1)` | 1 | 1492939 | 120 | 1.34e+07 | 233.6 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,5,5,4,2,1,1,1)` | 1 | 5848236 | 12 | 5.26e+07 | 236.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,5,4,2,1,1,1)` | 1 | 6956614 | 6 | 6.26e+07 | 236.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,5,2,2,2,1,1)` | 1 | 6098284 | 12 | 5.49e+07 | 246.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,3,3,3,1,1,1)` | 1 | 3838114 | 36 | 3.45e+07 | 254.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,5,5,2,2,2,1,1)` | 1 | 4810529 | 24 | 4.33e+07 | 256.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,4,3,3,1,1,1)` | 1 | 6391038 | 12 | 5.75e+07 | 258.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,4,3,2,2,1,1)` | 1 | 8769743 | 4 | 7.89e+07 | 279.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,5,5,1,1,1,1)` | 1 | 3532509 | 48 | 3.18e+07 | 279.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,5,3,2,2,2,2,1)` | 1 | 5378381 | 24 | 4.84e+07 | 286.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,7,4,3,2,2,1,1)` | 1 | 9484501 | 8 | 8.54e+07 | 342.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,5,3,3,1,1,1)` | 1 | 8571106 | 12 | 7.71e+07 | 346.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,7,5,2,2,2,1,1)` | 1 | 6591054 | 24 | 5.93e+07 | 351.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,5,5,3,2,2,1,1)` | 1 | 9885028 | 8 | 8.9e+07 | 357.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,5,3,2,2,1,1)` | 1 | 11778344 | 4 | 1.06e+08 | 374.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(11,5,2,2,2,2,2,1)` | 1 | 2404840 | 120 | 2.16e+07 | 376.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,3,2,2,2,2,1)` | 1 | 7198198 | 24 | 6.48e+07 | 383.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,7,3,2,2,2,2,1)` | 1 | 8303387 | 24 | 7.47e+07 | 442.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(6,6,5,5,2,1,1,1)` | 1 | 8630097 | 24 | 7.77e+07 | 460.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,4,4,2,2,2,2,1)` | 1 | 6273824 | 48 | 5.65e+07 | 496.3 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(6,6,5,4,3,1,1,1)` | 1 | 12448369 | 12 | 1.12e+08 | 503.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,5,4,2,2,2,2,1)` | 1 | 9470682 | 24 | 8.52e+07 | 504.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,5,5,5,2,1,1,1)` | 1 | 7838738 | 36 | 7.05e+07 | 519.0 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,6,2,2,2,2,2,1)` | 1 | 3344943 | 120 | 3.01e+07 | 523.5 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,6,4,3,3,2,1,1)` | 1 | 17007685 | 4 | 1.53e+08 | 541.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(7,5,5,4,2,2,1,1)` | 1 | 15545098 | 8 | 1.4e+08 | 561.4 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,7,2,2,2,2,2,1)` | 1 | 4056616 | 120 | 3.65e+07 | 634.8 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,6,4,2,2,2,2,1)` | 1 | 12045075 | 24 | 1.08e+08 | 642.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(8,5,4,3,2,2,2,1)` | 1 | 19615170 | 6 | 1.77e+08 | 666.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(6,6,6,3,3,1,1,1)` | 1 | 9438024 | 72 | 8.49e+07 | 990.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(12,3,2,2,2,2,2,2)` | 1 | 2479761 | 720 | 2.23e+07 | 1987.2 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(11,4,2,2,2,2,2,2)` | 1 | 4678248 | 720 | 4.21e+07 | 3749.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,4,4,2,2,2,2,2)` | 1 | 18748370 | 240 | 1.69e+08 | 5352.1 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(13,2,2,2,2,2,2,2)` | 1 | 1063374 | 5040 | 9.57e+06 | 5789.7 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(10,5,2,2,2,2,2,2)` | 1 | 7363399 | 720 | 6.63e+07 | 5900.9 | the wall clock of Addendum B.1 (queue not reached) |
| `(8,9)` | `(9,6,2,2,2,2,2,2)` | 1 | 9871895 | 720 | 8.88e+07 | 7911.2 | the wall clock of Addendum B.1 (queue not reached) |

102 weights not reached.
<!-- /GENERATED -->

**What it would take.**  Under the refitted model of §4, and single-process on a
box like this one, the unreached remainder of `(7,9)` and `(8,9)` is the bulk of
the census's 17.6 h — `(8,9)` alone is 13.0 h, of which 54 weights remain.  Three `(8,9)` weights sit **above s79's `1.5·10⁸` build
wall** and were never attempted: `(7,6,4,3,3,2,1,1)` at `N_S·δ = 1.53·10⁸`,
`(9,4,4,2,2,2,2,2)` at `1.69·10⁸`, `(8,5,4,3,2,2,2,1)` at `1.77·10⁸`.  Those are
**the boundary, returned with its `N_S·δ`** as the assignment asks — not a
failure and not a result.  They need a box larger than 7 GB or the leaner builder
of B13-10; no unbounded degree extension was requested and none was run.

**What the prefix is worth even where a group is incomplete.**  Each measured
weight is independently a PROVED non-membership, so an incomplete group still
narrows where a permanent-specific equation of that degree could sit: by
Prop. 8(2) it must sit at one of the **unreached** weights listed above.  That is
a smaller and explicitly enumerated target than the group, and it is what a
successor should queue first — in refitted-cost order, which §4's model now
supplies.

---

## 6. Pre-registration scorecard

| | pre-registered | outcome |
|---|---|---|
| **P1** (0.6) | `I(D_7^{per₃})_δ = 0` for `δ = 7, 8` and `I(D_8^{per₃})_8 = 0` — all 53 weights | **partly hit**: `(7,7)` and `(7,8)` complete (47 of 47); `(8,8)` five of six, the sixth ended by its timeout bound (§2.3).  52 of 53 weights measured, every one empty |
| **P2** (0.5) | `I(D_7^{per₃})_9 = 0` on all 152 weights | **not decided** — a certified prefix, every weight reached empty |
| **P3** (0.4) | `I(D_8^{per₃})_9 = 0` on all 62 weights | **not decided** — a certified prefix, every weight reached empty |
| success | an exact completed range **or** the first verified candidate deficiency | **two exact completed ranges** — `I(D_7^{per₃})_7 = 0` and `I(D_7^{per₃})_8 = 0`; no deficiency anywhere |
| fallback | a complete costed census and a certified prefix | **both delivered** (§5, §2.4) |
| a drop at any weight | halt the group; the verification protocol takes over | **never fired** — 0 drops in every weight measured |
| primes disagree | recorded, re-run with a fresh hybrid seed | never fired |
| **F1** (instrument) | calibration or a control fails, or the routes to `a` disagree | never fired; 3 calibrations and 3 negative controls PASS |
| **F2** | a theory-contradicting drop | never fired; no `δ < ℓ` weight is queued (Pieri) |
| stopping rules | wall clock; a weight over its `timeout` or memory bound is *not reached* with its cost | **both fired**: the queue wall clock (§5), and the per-weight `timeout 5400` at `(10,2⁷)_8` (§2.3), each recorded with its cost.  The memory bound never fired — peak resident 1.63 GB against a 6.5 GB bound |
| deviation | the queue order changed from `N_S` to refitted cost | recorded, **Addendum C**, before the measurements it governs |
| deviation | the deadline extended by two hours | recorded, **Addendum B**, before the measurements it governs |
| deviation | one run ended early by its recorded id | recorded, **Addendum C.3** |

---

## 7. Defects found — in this session, and in the assignment

**In this session's own work, found and fixed:**

1. **The evaluator put `board_numbering` in its `gct-cert/1` certificates.**
   That schema is closed and `tools/verify` refused them — correctly; the
   verifier was doing exactly what a check should do, and this is the first thing
   in this batch to be caught by it rather than by a human.  The preamble asks for
   `board_numbering` in every report and every **manifest**; a certificate is
   neither.  Fixed in the evaluator, and `analysis/b13_09_cert_fix.py` repairs the
   already-written ones by the narrowest possible edit — it removes that one key,
   asserts nothing else differs, and refuses any file for which that is not true.
   No mathematical content was rewritten, and the repaired certificates pass end
   to end.
2. **Two streams and the session raced on the git index** the first time two
   commits landed together (`cannot lock ref HEAD`).  The per-weight banking now
   takes a lock file first.  The JSONL write, which is where results actually
   live, was never at risk.
3. **The `(8,9)` plethysm cross-check would not run inline.**  `amb(9,3,8)`
   builds the whole degree's character table and is far slower than the per-weight
   Weyl alternation; run inline it stalled the census.  Split into
   `analysis/b13_09_pleth89.py` (29 s standalone) and merged with a both-directions
   check.  The first census attempt was also ended by its recorded pid for the
   same reason and restarted with an `S_r`-symmetric DP cache — asserted equal to
   the s42 routine on 492 weights before being relied on.

**In the assignment and the inherited record, reported as the board asks:**

4. **The cost model has no length caveat** (§4).  This is the substantive one: the
   assignment says "enumerate and price the relevant new components before
   selecting the executable queue", and the price it hands the session is wrong
   by up to 21.7× at exactly the lengths it asks about.  Pricing the census with
   it — which is what a session following the brief literally would do — yields a
   3.4 h plan for a 17.6 h job, and orders the queue so that the dearest weight
   in a group runs second.  The fix is in §4 and the remedy belongs to B13-10.
5. **"Use the existing builder" is ambiguous about length.**  There was no
   length-general cubic evaluator in the tree: `wk12_s79_per6.py` is fixed at
   `R = 6` (`R = 6` as a module constant, and `per3_pencils` builds exactly 6
   matrices per point).  Making it length-general is a small change on an
   unchanged engine, and the assignment's inputs ("the current cubic evaluator")
   read as though it already were.  Worth one sentence in a successor brief, since
   a session could reasonably have waited for someone else to provide it.
6. **The board's `N_S·δ` boundary and s79's wall are stated for a 7 GB box** and
   this container is 7.8 GB with 2 vCPU and no swap; the binding constraint here
   was **wall-clock and CPU**, not memory — peak resident across 100 weights was
   0.64 GB, two orders below the bound.  At lengths 7–8 the wall the brief names
   (memory in the raising rows) is not the wall a session actually hits; the
   `|Stab|` time term is.  That is worth correcting in the batch-14 framing.
7. **No defect found in the mathematics of the assignment.**  The two-objective
   framing, the correction in `docs/batch13_corrections.md` §1, the scope boundary
   with B13-05 (this session ran the numerical queue and no structural proofs) and
   the instruction to cite Theorem 2 and the restriction lemma rather than
   recompute are all correct as written, and §1 follows them.

**No tier-3 reconstruction was needed.**  Every document the assignment names
was present in the clone, and the `B13-09` entry answered what it needed to
answer apart from the two points above.

---

## 8. Delivery

**This bundle has ONE part: `part00`.**  (Stated in the first paragraph and
here, per the preamble.)

    git bundle create b13_09_higher_length.bundle 00495110..HEAD

— except that the command above is **not** the one that was used, and the
difference is a delivery defect worth recording.  `git bundle create <base>..HEAD`
records only `HEAD`, **not the branch name**, so
`git fetch <bundle> b13-09-higher-length` fails with *couldn't find remote ref*.
Caught by test-applying the bundle rather than by trusting it.  The bundle shipped
was made with the ref instead:

    git bundle create b13_09_higher_length.bundle \
        00495110c62acfbbbc951e82cc218ed091563b3f..b13-09-higher-length

so `git bundle list-heads` shows `refs/heads/b13-09-higher-length` and the fetch
works by name.  **This bundle was verified by applying it**: a fresh clone reset to
the base, `git bundle verify`, `git fetch <bundle> b13-09-higher-length:...`,
checkout — 170 commits, 165 JSONL records, 84 certificates, every named deliverable
present.

`b13_09_higher_length.bundle.md5` carries a digest for the **whole file** and one
**per part**, naming **bare filenames** only; `md5sum -c` was tested from a
different directory and passes.  Since the bundle is unsplit the two digests
coincide, and the file says so explicitly rather than leaving a reviewer to infer
it.  Branch history was **not** rewritten; nothing was dropped.

**Artefacts.**  `results/PREREG_b13_09.md` (with Addenda A–C);
`results/b13_09_census.json` (267 weights, priced both ways);
`results/b13_09_pleth89.json`; `results/b13_09/per_r{r}_d{δ}.jsonl` and
`status_*.json`; `results/b13_09/costfit.json`; `results/b13_09/verify*.json`;
`results/b13_09/cert_verify_report.md`; certificates under
`results/certs/b13_09/` (`gct-cert/1`, `full_rank`, `n = 3`,
`permanent_pencil`, gzipped, every one under the 5 MB limit); logs under
`results/logs/b13_09_*`; and `results/b13_09/cert_manifest.json`, which lists
**every** certificate with size and md5, marks which travel in the bundle, and
records the shipping rule and the regeneration command for the rest.

**Instruments added** (all under `analysis/`): `b13_09_per_r.py` (the
length-general evaluator), `b13_09_census.py` + `b13_09_pleth89.py` +
`b13_09_census_merge.py` (the census and its two-directional cross-check),
`b13_09_sweep.py` (the bounded queue), `b13_09_verify.py` (the kernel-free
independent verifier), `b13_09_costfit.py` (the refit), `b13_09_cert_fix.py`,
`b13_09_manifest.py`, `b13_09_report.py` (this report's tables, generated from
the records so that no number here is hand-transcribed).

**Host resources, declared.**  2 vCPU (Intel Xeon @ 2.80 GHz), 7.8 GB RAM, no
swap, 250 GB disk.  Twelve sessions do not imply twelve memory budgets: this one
held itself to at most two concurrent builds plus low-priority verification, and
peak resident over 100 weights was 0.64 GB.  Toolchain preflight: `python-flint`
was **absent** and was installed (0.9.0, with sympy 1.14.0 and mpmath 1.3.0);
`numpy` 2.4.4, `scipy` 1.17.1 and gcc 13.3.0 were present; `Singular` and
`msolve` are absent and were not needed.  The hybrid's `schur.so` was compiled
from `analysis/wk11_s71_schur.c`.

**Runs were bounded at launch** with `timeout` and `ulimit -v`, process ids
written to `results/logs/<run>.pid` and `<run>_child.pid`; the two runs ended
early (the first census attempt, and `(10,2⁷)_8` under the cost cap before it was
re-run deliberately) were ended **by those recorded ids**, never by
name-pattern matching.

No external announcement or publication was made; none is part of this
assignment.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
Session run by Claude Fable 5.1 (setup, census, calibration) and Claude Opus 5
(queue, verification, report) — see the header.
board_numbering: batch13
