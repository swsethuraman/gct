# Batch 11 — the consolidated plan

Two boards were drafted for this batch: mine, and Sol's reply to it
(`sol_feedback1.txt`).  Sol adopted the architecture — **ten ungated sessions,
two gated** — and proposed two pre-batch checks and five modifications.  This
document is the merge.  Every number below is either banked in this repository,
verified here while the plan was being written, or labelled as a hypothesis.

The design principle is unchanged and is the one thing batch 10 got wrong:

> **Fund the bottleneck redundantly; do not make the entire batch wait for it.**

Batch 10 had one gate — an explicit basis of the 274-dimensional LMR source —
feeding four consumers.  The gate did not open, and session 65 never ran.
Batch 11 attacks that source three independent ways (C1, C2, S5) and keeps the
remaining nine sessions productive if all three fail.

---

## 1. The two pre-batch checks

### P0-B is already closed

Sol asks that the `a_∞ = 1` weight-13 stable lines be finished before S4 spends
theory time on `a_∞ = 2, 3`, naming `ρ = (7,2,2,1,1)` in particular.

**They were finished during batch 10, here.**  All three weight-13 shapes with
`a_∞ = 1` — `(7,2,2,1,1)`, `(5,5,1,1,1)`, `(5,3,3,1,1)` — have `i_det^∞ = 0`.
They were run after correcting S1's raising-operator formula, which was written
in the divided-power normalisation and does not pair with the plain-coefficient
substitution; both conventions give a one-dimensional kernel, so the
multiplicity check cannot see the mismatch, and the test as specified would have
produced an unfalsifiable negative.  Recorded in `docs/stocktake_batch10.md` §2
row 10 and §5.

**Consequence: S4 opens at `a_∞ = 2, 3` immediately.**  There is no risk of
jumping over a positive stable equation at weight 13 with `a_∞ = 1`; that region
is empty.

### P0-A — the unpadded `n = 3` permanent test

Sol is right that this is the highest-expected-value finite computation the
programme has, and it does not deserve a session.  It was run here while this plan was being
written; the result is §1.1, and it is positive.

**What it is.**  At the `n = 3` member of the LMR family,
`λ = (19,7,2⁵)`, `δ = 12`, `r = ℓ(λ) = 7`, `a = 6`, with `mult_det = 5` and
`i_det = 1` already measured at both house primes, measure `mult_{per₃}` and
hence `i_{per₃}`.  Then `D = i_det − i_per = 1 − i_per`, and

    mult_per = 6  ⟹  i_per = 0  ⟹  D = +1.

Only the positive branch is rigorous: `rank_p ≤ rank_Q ≤ a`, so a measured rank
of 6 forces `mult_per = 6`.  A rank of 5 is suggestive and requires comparing
the two kernel lines; below 5 the multiplicity points the wrong way.

**Why the direction is favourable, and why this does not contradict
`stocktake_batch10.md` §6.**  §6 proves that the *padded* `n = 3` cell can never
carry an obstruction: `per₂` and `det₂` are both rank-4 quadratic forms in four
variables, hence `GL`-equivalent, so the padded `per₂` in degree 3 is `ℓ·det₂`
up to `GL`, which is the block split `diag(ℓ, A₂)` inside `det₃`; therefore
`P ⊆ D` and `D ≤ 0` always.  **P0-A is a different pair of varieties.**  It
compares the *unpadded* `per₃` against `det₃`, both cubics in nine variables
restricted to `r = 7`:

    ambient                       Sym³(C⁷)                    dim 84
    det₃ cubics in 7 variables    9r − 16 = 47
    per₃ cubics in 7 variables    9r −  4 = 59

so the determinant variety is the **smaller** one, `I(D) ⊇ I(P)` is the
plausible direction, and `D = i_det − i_per ≥ 0` is the favourable orientation —
the exact opposite of the padded `r ≤ 5` cells, where permanental cubics are
dominant (`9r − 4 ≥ C(r+2,3)` for `r ≤ 5`) and containment forces `D ≤ 0`.  At
`r = 7` neither variety fills the ambient, so the comparison is not vacuous.

**What a positive result would and would not mean.**  It would *not* be a new
theorem: `per₃ ∉ closure(GL₉·det₃)` follows already from the dimension count
above (`59 > 47`), and independently from the banked `dc̄(per₃) ≥ 5 > 3`.  It
would be **the first complete, exhibited multiplicity obstruction the programme
has ever produced** — a representation whose multiplicity in the coordinate ring
of the permanent variety strictly exceeds its multiplicity in that of the
determinant, computed end to end by the programme's own machinery, at a carrier
of `n_χ = 17 047` rather than `3.10×10⁷`.  Since `P ⊆ D ⟹ I(D) ⊆ I(P) ⟹
i_det ≤ i_per`, a strict `i_det > i_per` certifies `P ⊄ D` on its own terms.
That is a positive control the programme has never had; every control in the
record so far is a calibration or a negative.

### 1.1 P0-A result — `D = +1`, at both house primes

Run here on the same instrument session 63 used, so the two numbers come from one
engine on one build (`analysis/wk11_int_p0a.py`, `results/wk11_int_p0a.json`,
876 s):

| prime | `i_det` | `mult_det` | `i_per` | `mult_per` | `D` |
|---|---|---|---|---|---|
| 2 147 483 647 | 1 | 5 | **0** | **6** | **+1** |
| 2 147 483 629 | 1 | 5 | **0** | **6** | **+1** |

The determinant column reproduces s63's positive control exactly, on an
independently written driver.  The whole measurement was then run a second time
after the terminology correction of §10, and returned the same four numbers at
both primes (876 s and 1 532 s; the difference is machine load, not the result).

**The result is rigorous, and the two sides are rigorous for different reasons.**

- `i_per = 0`.  `mult_per = 6 = a` was measured as a rank mod `p`, and
  `rank_p ≤ rank_Q ≤ a`, so `rank_Q = 6` and `i_per = 0` over `Q`.  There is no
  Schwartz–Zippel caveat in this direction: the caveat is that vanishing at
  finitely many points does not prove ideal membership, and here nothing vanishes.
- `i_det = 1`.  The measurement gives `i_det(Q) ≤ 1`; the lower bound
  `i_det(Q) ≥ 1` is LMR's theorem at this cell, which is exactly what made s63's
  measurement a control rather than an observation.  So `i_det = 1` exactly.

Hence `mult_per = 6 > 5 = mult_det`, so `P₇ ⊆ D₇` is impossible (containment
would give a surjection `C[D₇] ↠ C[P₇]` and hence `mult_P ≤ mult_D` at every
`λ`): **`per₃` is not in the closure of `GL₉·det₃`, certified by an exhibited
multiplicity obstruction with `D = +1`.**

**It is a multiplicity obstruction, not an occurrence obstruction** — Sol's
correction, and it is the stronger reading.  The standard distinction is

    occurrence obstruction    mult_pad(λ) > 0 = mult_det(λ)
    multiplicity obstruction  mult_pad(λ) > mult_det(λ), both possibly positive

and here `mult_det = 5` and `mult_per = 6` are **both nonzero**, so `S_λ` occurs
in both coordinate rings and no occurrence obstruction is present.  The
distinction matters beyond bookkeeping: in the padded permanent-versus-
determinant setting Bürgisser–Ikenmeyer–Panova rule out occurrence obstructions
over the range of `n` the programme cares about, while multiplicity obstructions
remain open — which is why `D = mult_pad − mult_det` is the programme's chosen
quantity in the first place.  The programme's first `D > 0` is therefore of the kind the literature
leaves open, which is the kind it needs to be.

**What this is worth, stated honestly.**  The *statement* is not new and is not
even hard: `dim P₇ = 59 > 47 = dim D₇`, so the containment fails by a dimension
count.  What is new is the *certificate*.  This is the programme's first
`D > 0` of any kind, and it is a **positive control** in the strict sense — the
instrument pointed at a pair where a separation is known to exist, returning the
separation.  Every control in the record until now was a calibration (`n = 2`,
where a theorem fixes both sides), a negative (`mult_det = a` at all 419 `r = 5`
cells), or one-sided.  It also exercises the entire comparison pipeline end to
end — build, raising kernel, two evaluation families against one source, two
primes — which is precisely what C6 must do at `n = 4`.

**Three things it is not.**  It is unpadded, so it says nothing about the padded
model; `docs/stocktake_batch10.md` §6 proves the padded `n = 3` cell can never
carry an obstruction, and that proof stands.  It is `n = 3`.  And it does not
bear on the `n_χ` wall — the cell is `17 047` coordinates.

**One consequence for the board, which is new and nearly free.**  The same
orientation holds at `n = 4`: with `dim{det₄ forms in r vars} = 16r − 30` and
the `per₄` stabiliser of dimension `2n − 2 = 6` giving `16r − 6`,

    ambient Sym⁴(C⁹)                dim 495
    det₄ forms in 9 variables       16·9 − 30 = 114
    per₄ forms in 9 variables       16·9 −  6 = 138

so at the LMR cell the *unpadded* `per₄` comparison is favourably directed as
well.  Measuring `i_{per₄}` there costs **one more evaluation family against a
source that already exists** — no new build, no new kernel.  It is the `n = 4`
positive control the programme has never had, and it is what distinguishes
"no obstruction at LMR" from "the instrument is blind at `n = 4`" if the padded
comparison comes back `D ≤ 0`.  It goes into C6 Mode A as a required third
column, and into C4's stable cells wherever they are already being evaluated.

---

## 2. Three measurements made while writing this plan

These are new, they were cheap, and each one changes a brief.

### 2.1 The LMR ladder does not thin downward

C1's mission is to grow the source from `δ = 12` to `δ = 24` along the ladder
`λ_δ = (4δ − 31, 17, 2⁷)`.  The unstated assumption is that the bottom of the
ladder is cheap.  **It is not.**  Counting weight-`λ` degree-`δ` monomials in
the 495 degree-4 exponent vectors on nine variables, by an unbounded-knapsack
recursion over the exponent vectors (`analysis/wk11_int_ladder_size.py`):

| `δ` | `λ₁` | `a_δ` | `N_S` | `n_χ ≈ N_S/|Stab|` | fraction of LMR |
|---|---|---|---|---|---|
| 12 | 17 | 2   | 5.14×10¹⁰ | 5.10×10⁶ | 0.16 |
| 13 | 21 | 39  | 8.09×10¹⁰ | 1.61×10⁷ | 0.52 |
| 14 | 25 | 93  | 1.06×10¹¹ | 2.11×10⁷ | 0.68 |
| 15 | 29 | 145 | 1.26×10¹¹ | 2.49×10⁷ | 0.80 |
| 16 | 33 | 188 | 1.39×10¹¹ | 2.75×10⁷ | 0.89 |
| 17 | 37 | 219 | 1.47×10¹¹ | 2.91×10⁷ | 0.94 |
| 18 | 41 | 241 | 1.52×10¹¹ | 3.01×10⁷ | 0.97 |
| 19 | 45 | 255 | 1.54×10¹¹ | 3.06×10⁷ | 0.99 |
| 24 | 65 | 274 | 1.56438903314×10¹¹ | 3.104×10⁷ | 1.00 |

The stabiliser is `S₇` on the seven 2's throughout, doubled at `δ = 12` where
`λ₁ = λ₂ = 17`; `n_χ` is quoted as `N_S/|Stab|`, which is the orbit count to
within a handful (the orbits are essentially all free).

**The count is validated at the top of the ladder.**  At `δ = 24` it returns
`N_S = 156 438 903 314` and `N_S/|Stab| = 31 039 464.94`, against s57's banked
`N_S = 156,438,903,314` and `n_χ = 31,039,465` — an exact match, digit for
digit, by a completely different method (s57 enumerated; this counts).  At the
bottom, `N_S(12) = 51 446 325 457`.

**Three consequences.**

1. **The carrier saturates by `δ = 16`.**  Walking the ladder upward is not a
   cost-reduction strategy.  Whatever saving C1 achieves must come *entirely*
   from support restriction, whose measured density is `0.20–0.26` — and that
   density was measured at `δ = 4`, not here.  This belongs in C1's
   pre-registration as a stated expectation, not discovered at 3 a.m.
2. **`δ = 12` is the one genuinely cheaper rung**, at a sixth of LMR, and it is
   cheap for an accidental reason (the extra factor of two in the stabiliser).
   It is also the rung where `a_δ = 2` — the smallest nullity anywhere on the
   ladder.  A nullity-2 kernel in `5.1×10⁶` columns is the single most
   favourable case for a black-box method, and the repository already carries a
   Wiedemann binary (`WIED_BIN`).  **`δ = 12` is where C1 should begin and where
   its instrument should be calibrated**, not because it is representative but
   because it is the only rung where success is plausible on the first night.
3. **The hoped-for cheap falsifier at the bottom of the ladder does not exist in
   the form I wanted.**  Lemma L gives `i_X(δ) ≤ i_X(δ+1)` for every
   `GL`-stable ideal `X`, pad included, so a live low rung would transport
   upward.  But `i_pad(12) ≥ 1` does not kill `D > 0` outright: it would force
   `i_det(24) ≥ 2`, hence `i_det(23) ≥ 1`, hence a determinant equation of
   degree 23 at `ℓ = 9` — which s57 argues against but has not excluded.  So it
   is a strong conditional kill, not an absolute one, and it costs `5.1×10⁶`
   columns, not `10⁴`.  Worth doing as a by-product of C1's rung 12; not worth a
   session.

### 2.2 The last two rungs are room-one, and `det A₂₄` is the room-one denominator

The `a`-ladder is `2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274`
for `δ = 12…24` (s57, re-verified by s63 in `results/s63_aladder.json`).  Its
last two increments are both exactly one.  So `δ = 23` and `δ = 24` are
**room-one rungs** in the sense of the room-one memo, and at `δ = 24` the Schur
complement reads

    G₂₄ = [[A₂₄, b], [bᵀ, c]] ,   s = c − bᵀA₂₄⁻¹b = det G₂₄ / det A₂₄ ,
    s = 0  ⟺  the equation is born  ⟺  i_det(24) ≥ 1,

with `A₂₄` the **degree-24** Gram restricted to the transported predecessor
`J(M₂₃)` — the corrected denominator, not the predecessor's own Gram.

**This identifies C3's second rank with C1's terminal step.**  `det A₂₄ ≠ 0` is
not an independent computation bolted onto the source construction; it is the
last rung of the ladder C1 is climbing.  Two operational consequences:

- C1 and C3 must use the same definition of `A₂₄`, written into both
  pre-registrations, or their results will not compose.
- **The branch where `A₂₄` is singular is a win, not a blocker.**  `det A₂₄ = 0`
  means `mult_det(23) < 273`, i.e. `i_det(23) ≥ 1`, i.e. a determinant equation
  at `ℓ = 9` of degree 23 — strictly stronger than LMR, and s57 calls
  `(61,17,2⁷)₂₃` "the sharpest single test of nothing below 24 that exists".
  C3's brief must say this, because a worker who reads `det A₂₄ ≠ 0` as the
  success condition will report the good outcome as a failure.

### 2.3 The birth arithmetic — no rung needs more than 54 new vectors

The ladder theorem says multiplication by `u = c_{(4,0,…,0)}` carries
highest-weight vectors injectively up the ladder, so
`dim J(M_{δ−1}) = a_{δ−1}` exactly and

    M_δ = J(M_{δ−1}) ⊕ B_δ ,   dim B_δ = a_δ − a_{δ−1} .

The birth sequence is therefore `2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1`,
summing to 274.  Sol calls this the Ramanujan question — compute the difference
equation, not the enormous coefficient — and it is right that this is the
algorithmic content of C1.  Concretely:

- **The nullity to be found at each rung is `dim B_δ ≤ 54`, not `a_δ ≤ 274`,**
  provided the raising system is deflated by the `a_{δ−1}` known transported
  vectors.  Deflation by known kernel vectors is exactly what makes a block
  method cheaper, so this is not a bookkeeping remark.
- **It supplies Sol's completeness certificate cheaply.**  Sol's modification A
  is right that a restricted nullspace of dimension `a_δ` proves nothing unless
  the omitted raising equations are provably irrelevant.  The per-rung form is:
  the transported `a_{δ−1}` vectors lie in the restricted nullspace; the
  restricted nullspace has dimension exactly `a_δ`; and the `≤ 54` new vectors
  pass the **full** raising action, including target rows outside the current
  support.  That is `≤ 54` genuine-highest-weight verifications per rung instead
  of 274, and the ambient `a_δ` is independently known, so the count certifies
  completeness.

---

## 3. The consolidated board

### Claude

| | mission | gate | success | kill |
|---|---|---|---|---|
| **C1 — ladder source** | **Seed step first** (§5 iii): materialise and certify the two `M₁₂` highest-weight vectors at `n_χ ≈ 5.1×10⁶` by the best available black-box/nullspace method, and report failure there as the first wall rather than assuming the seed. Then build `M_λ` rung by rung along `λ_δ = (4δ−31,17,2⁷)`, `δ = 12→24`, by support-restricted transport plus a **deflated** birth-space solve of dimension `a_δ − a_{δ−1} ≤ 54`; never form the full carrier. Per-rung completeness certificate as in §2.3. | none | the seed, then all 274 genuine highest-weight vectors with per-rung transition data; or the first `k` rungs certified with a cost curve | the seed cannot be materialised in budget — which is itself the result, since `δ = 12` is the cheapest point on the ladder; or live support grows to carrier scale at a rung whose `a_δ` is small |
| **C2 — compact circuit** | Exploit `(65,17,2⁷) = (2⁹) + (63,15)`; represent source and highest-weight vectors as contraction/bracket circuits rather than coordinate vectors. | none | reproduce the `n = 3` `U_D` exactly, then reach `n = 4` | fails the exact `n = 3` control |
| **C3 — the two ranks** | `rank S_{λ,24}` (the `274 × 521` reducible-normalisation split) **first**; then `det A₂₄` at both house primes, with §2.2's branch reading. Report all four outcomes with the semantics of §4C — in particular `rank S = 274` does **not** establish padded full rank. | see §5 — split gate | `rank S = 274` **and** `A₂₄` nonsingular ⟹ `i_det = 1` and the `i_pad = 0` route stays open, for C6 to settle; **or** `A₂₄` singular ⟹ `i_det(23) ≥ 1`, stronger | `rank S < 274` ⟹ `mult_pad ≤ mult_red < 274` ⟹ `i_pad ≥ 1`, which with `i_det = 1` gives `D ≤ 0`: **the LMR cell dies to a 274 × 521 rank** |
| **C4 — `r = 5` closure falsifier** | Exhaust the 1 075 stable closing cells in increasing **certified cost order**, using degeneration and hybrid certificates where they apply; stop immediately on `i_det > i_red`. | none | one cell with `i_det > i_red` kills `R₅ ⊆ D₅` | no falsifier after the affordable prefix; report the cost curve and where it flattened |
| **C5 — `r = 5` upper bound** | Implement the special-fibre / exhaustion bound. **Not another lower-bound arc search.** Prove every remaining component has fixed-factor image `< 35`. | none | the bound, on all remaining components | discover a rank-35 component — which settles the question the other way |
| **C6 — the decision table** | Mode A: `i_pad`, `i_{per₄}` (§1.1) and `i_det` at LMR from whichever source lands, with `U_P`, `U_D`, `dim(U_D ∩ U_P)` and the three-outcome table. Mode B (default): the same pipeline up the `n = 3` ladder `λ_δ = (3δ−17, 7, 2⁵)`, `δ = 12, 13, 14`, starting from the `D = +1` of §1.1 — does the obstruction survive transport, or does `i_per` become positive above it? | none (§5) | exact `D` and its orientation at whichever `n` is reached; in Mode B, the first three rungs of a `D`-ladder | Mode B also unavailable — cannot happen, the cell builds in 274 s and the run is 876 s |

### Sol

| | mission | why now |
|---|---|---|
| **S1 — a cheaper determinant equation** | Not "does the LMR family have a smaller member" — it does not, below the known case. The question is whether **any other explicit determinant-orbit equation exists in a dramatically cheaper cell**. Exhaustive primary-literature and constructive audit over the named mechanism families (§10). **Cost-indexed**: every candidate returned as `(r, δ, λ, a_δ, n_χ, expected support)`, never as a citation, so that a beautiful but computationally useless result is visibly useless. | A guaranteed determinant equation at `r = 5, 6, 7, 8` would give a positive kernel cell with a manageable carrier and delete four batches of pain. |
| **S2 — wreath/`Θ` intertwiner at `q = 2`** | An actual `R₂`, an actual `S₂`, a verified commutative square on tiny `n, δ`, injectivity on at least one multiplicity block, explicit row-growth bookkeeping. | The only surviving credible asymptotic route. If `q = 2` cannot be made natural, general `q` dies cheaply. |
| **S3 — `r = 5` exhaustion theorem** | Turn s66's measured singular-stratum picture into a finite exhaustion / upper-bound theorem. Shares one written target statement with C5 (§5). | The exact missing implication for `R₅ ⊄ D₅`. |
| **S4 — stable `a_∞ = 2, 3`** | In this order: all weight-13 `a_∞ = 2`; then `a_∞ = 3`; **stop at the first nonzero stable ideal**; if all die, formulate the resulting stronger stable dead-region theorem. Exact low-rank tests on `M₆`, not another census. P0-B is closed, so it opens immediately. | Independent second determinant-equation laboratory; 44 of 47 weight-13 shapes are still open and need ranks, not scalars. |
| **S5 — intrinsic wreath source** | Does `[λ]^{S₄≀S_δ}` admit a Bratteli / Jucys–Murphy / partition-algebra recursion whose live state count tracks `a_δ` rather than `dim[λ]`? Pre-register the maximum live state count at `δ = 12, 14, 16, 18`. | Third and most theorem-oriented attack on the bottleneck; the one route nobody has tried. |
| **S6 — adversarial audit** | Read **code and docs**, explicitly ignoring session conclusions until the underlying implementation has been checked. What machinery already exists that the board thinks is missing? Which dead routes died mathematically and which only in one implementation? Which assumptions are merely inherited? Given every inequality now known, which numerical outcomes at LMR still permit `D > 0`? Then draft the batch-12 board. | Batch 10 specified four items as missing that were already in the repository. This is the direct fix. |

---

## 4. Sol's five modifications

**A — C1 needs a completeness certificate. Accepted, and made concrete.**  Sol
is right that a restricted nullspace of dimension `a_δ` proves nothing by
itself.  §2.3 gives the per-rung form, which costs `≤ 54` full raising
verifications rather than 274.  Into the pre-registration verbatim.

**B — C4 cost-ordered, not "run all 1 075 regardless". Accepted.**  Buildable is
not overnight-cheap.  The logic Sol states is the reason C4 is worth
reinstating and should be quoted in its brief: `R₅ ⊆ D₅ ⟹ I(D₅) ⊆ I(R₅) ⟹
i_det ≤ i_red` at every cell, so **one** exact cell with `i_det > i_red` kills
containment.  That is an unusually clean falsifier and it does not require the
exhaustion theorem C5/S3 are chasing.  C4 becomes a falsifier sweep that stops
when the information rate flattens.

**C — C3 runs `rank S_{λ,24}` first, with no fallback to the carrier engine.
Accepted.**  The ordering is right: `rank S < 274` makes padded full rank
impossible before any permanent-specific cubic block is touched.  And s63
quantified the carrier wall on all three existing realisations, so a fallback
there is not a contingency, it is a way to spend a night reconfirming a
measurement.  **Amended twice.**  By §2.2: `det A₂₄ = 0` is the *stronger* outcome, and the
brief must say so.  And by Sol's second point here, which is a correction to my
wording: **`rank S = 274` does not establish padded full rank 274.**  `S` is the
universal reducible-normalisation stage; the permanent-specific cubic stage can
still drop rank afterwards, so `rank S = 274` gives `i_red = 0` and leaves
`i_pad` unknown — C6 must still determine it.  The converse is the valuable one
and my kill line understated it: since `mult_pad ≤ mult_red = rank S`, a
`rank S < 274` forces `i_pad ≥ 1`, and with `i_det = 1` that gives `D ≤ 0` at
LMR **before any permanent-specific block is touched**.  Both semantics go in
the C3 row verbatim, because the four outcomes are not symmetric and a worker
reading "success = 274" will mis-report two of them.

**D — S2 starts at `q = 2` only. Accepted without change.**  The five concrete
requirements Sol lists are the brief.

**E — S6 does code archaeology, not report summarisation. Accepted and
strengthened.**  This is the direct lesson of batch 10's corrections ledger:
the Gram/double-coset observation (s56), the `h_pad` Pieri identity (s42), the
padded evaluation family (s36/s41) and an `r = 6` multiplicity separation (s47)
were all specified as missing while already in the code.  Sol's four questions
go in verbatim.  I add a fifth: **S6 drafts the batch-12 board**, because it is
the only session positioned to.

**The `F₄` numerology.**  Sol demotes its own suggestion to a bounded
thirty-minute falsifier inside S6, with an explicit kill.  Agreed, and the kill
should be stated as the default: `274 = 273 + 1` and `273 = dim V_ω^{F₄}` is a
coincidence unless a canonical 26-dimensional object or `𝔣₄` operator algebra is
already latent in the source construction.  If none is found in thirty minutes,
it is killed in writing and not revisited.

---

## 5. My three changes to Sol's board

**(i) C6 is ungated.**  Sol's board has C6 gated on C3 gated on (C1 or C2 or
S5) — a two-deep gate, which is precisely the batch-10 failure mode that killed
session 65.  The fix is not to weaken the gate but to give C6 a default mode
that produces science on its own: **walk the `D`-ladder at the `n = 3` family
member**, starting from `D = +1` at `(19,7,2⁵)₁₂` (§1.1) and continuing to
`δ = 13, 14` along `λ_δ = (3δ − 17, 7, 2⁵)`, where the cell builds in 274 s at
`n_χ = 17 047` and the full two-form run took 876 s.  That is a real open
question — Lemma L makes both `i_det` and `i_per` non-decreasing, so `D` can
die going up, and nobody knows whether this one does — and it is simultaneously
the exact pipeline C6 would run at `n = 4`, debugged in advance at 1/1800 of the
carrier.  If a source lands from C1/C2/S5 before C6's checkpoint, it switches to
Mode A.  **The batch now has zero doubly-gated sessions.**

**(ii) C3's gate is split, and the split is a determination C3 makes in its
first hour.**  `det A₂₄` needs the source.  `rank S_{λ,24}` — the `274 × 521`
reducible-normalisation matrix — may not: if its rows are indexed by the Pieri
shapes and its columns by the ambient multiplicity rather than by explicit
source vectors, it is computable from `λ` and `δ` alone.  C3's first task is to
settle that in writing and take the corresponding branch: ungated if the rank
needs no source, gated on (C1 or C2 or S5) if it does.  Either way C3 reports
the determination, because the answer is reusable and nobody has written it
down.

**(iii) C1 carries the birth-space algorithm, starts at `δ = 12`, and
pre-registers the seed step separately.**  §2.1 and §2.3 give the algorithm; Sol
supplies the missing initial condition, and the point is sharp.  A recursion
`M_δ = J(M_{δ−1}) ⊕ B_δ` needs `M₁₂`, and `M₁₂` is a 2-dimensional kernel inside
`n_χ ≈ 5.1×10⁶` coordinates — the one genuinely hard object in the whole scheme.
Without a separate pre-registration, C1 can quietly become *incremental source
construction assuming we already have the source*, and report a working ladder
algorithm that was never tested against the thing that makes it hard.

So the brief states the seed step as its own pre-registered item, with its own
budget and its own verdict:

> **Seed.**  Obtain the two `M₁₂` highest-weight vectors and certify them
> against the **full** raising action (not the support-restricted one), with
> `dim = a₁₂ = 2` exactly.  Any method is admissible — block Wiedemann,
> structured sparse elimination, or the compact-circuit route if C2 gets there
> first.  If the seed cannot be materialised within the budget, **say so and
> stop**: that is the first wall, it is a reportable result, and it must not be
> described as a failure of the ladder algorithm, which will not have been
> tested.

And there is no cheaper entry point to fall back to: the ladder begins at
`δ = 12` because `4δ − 31 ≥ 17` fails below it, and §2.1 shows every higher rung
is more expensive.  **`δ = 12` is the cheapest point on the LMR ladder, full
stop.**  If the seed is out of reach there, the ladder route is out of reach,
and that is worth knowing on night one rather than after three sessions.

---

## 6. Gate structure

    ungated (11):  C1  C2  C4  C5  C6(Mode B)  S1 S2 S3 S4 S5 S6
    gated  (1):    C3, on (C1 or C2 or S5), and only for its second rank —
                   and possibly not at all, per §5(ii)

The anti-s65 rule for this batch, stated so a worker can apply it without
asking: **no session may have a gate whose opening depends on another gate.**
Every gated session carries a default mode that produces a pre-registered number
from material already in the repository.

C5 and S3 attack the same theorem computationally and theoretically.  **They
share one written target statement, fixed in this plan before either starts**,
or they will produce incomparable partial results:

> *Target (r = 5 upper bound).*  Let `R` be the coordinate ring of the `r = 5`
> model and `J` the ideal of the base scheme of `Φ`.  For **every irreducible
> component `E` of the exceptional divisor `Proj gr_J R`** of the blow-up of
> `Spec R` along `J` that is supported over `Sing V(J)` — including components
> supported over *proper subloci* of an irreducible singular component, over the
> incidence and rank-degeneration strata, and components arising from the
> *embedded, non-reduced* structure of the base scheme — the fixed-factor image
> of `E` has dimension `< 35`.  Together with s66's contact-order lemma, which
> disposes of every component supported over the smooth locus of `V(J)` (there
> the exceptional fibre is `P(im dΦ)` at every order), this exhausts
> `Proj gr_J R` and yields `R₅ ⊄ D₅`.

**Why the quantifier is over the normal cone and not over `Sing V(J)`** —
Sol's correction, and the repository already contains the reason.  s66 §5
measured `in(J) ⊊ in(I₁ ∩ I₂)` at a generic point of every pairwise incidence
(`dim Q₂ = 12 < 16` at `P ∩ SP`, `41 < 69` at `P ∩ coker`, `25 < 49` at
`c21 ∩ c32`, `59 < 144` at `ker ∩ coker`), and concluded that **the base scheme
is generically reduced along every component and non-reduced along every
pairwise incidence** — "the precise sense in which the normal cone of `J`
differs from the normal cone of the reduced base locus, and why the exceptional
fibre over an incidence is larger than `P(im dΦ)`".  A statement quantified over
irreducible components of the reduced singular locus therefore has a real
logical gap: a component of `E` can sit over a proper sublocus or over embedded
structure and be invisible at the generic point of any `Z`.  My earlier wording
had that gap; this one does not.

**And the residue is finite and already named.**  s66 §8 lists exactly four
places a component of `E` could still hide: (1) `P ∩ c21`, whose order-2 image
did not finish in the 25-minute box — the one number of the primitive world not
on the table; (2) the rank-drop strata of `M(a)` at `ker ∩ coker`; (3) contact
order `≥ 4` at the incidences, and order `≥ 3` with `M₁` outside the tangent
spaces where `V(Q₂)` has an extra component (`P ∩ c32`, `SP ∩ c21`); (4) deeper
strata of the rank-`≤2` world.  **C5 and S3 close that list, not an open-ended
survey.**  By the contact-order lemma none of the four can be a smooth point of
`V(J)`, and each is a proper closed subset of a locus already measured.

s66 pushed every measured primitive and compression exceptional image to at most
`29 < 31 < 35` through the reachable orders.  The remaining work is not another
"does something climb?" survey; it is proving that nothing unmeasured can climb.

---

## 7. Priority order

Expected scientific value per unit effort — **not execution order**, since C3
may be gated:

    S1  ≈  C1  >  S5  ≈  C6  >  C2  >  S3  >  C5  >  C3  >  S4  >  C4  >  S6  >  S2

This is Sol's final ordering and I adopt it.  It moves S5 level with C6 rather
than below it, on the argument that S5 changes the complexity class of the whole
project if it works, whereas C6 teaches a finite mechanism — a fair reading of
expected value against certainty, and the execution architecture does not depend
on it.

Two departures from Sol's *first* ranking, both retained:

- **C6 rises** from eleventh, because Mode B makes it ungated, certain to
  produce a number, and its number continues the programme's first exact `D`.
- **S6 rises** past S2.  Sol placed S6 second-to-last while arguing it could
  prevent another wasted batch; those two positions are inconsistent, and the
  batch-10 corrections ledger settles it in S6's favour.

S1 stays at the top and I agree with Sol's reasoning: the record treats
`(65,17,2⁷)₂₄` as the first useful determinant equation, but what is actually
known is only that it is the first one the programme has deliberately exploited.

---

## 8. Process rules for batch 11

Carried from batch 10's corrections ledger, and all four are its direct lessons:

1. **Read the code before writing the brief; cite the file, not the memo.**
   Four items specified as missing in batch 10 were already implemented.
2. **Push the plan before the briefs go out.**  s62 and s66 both cloned a tree
   that did not contain the batch-10 plan.
3. **Wording.**  `docs/brief_wording.md` §2 substitution table and §4 word list
   are binding; §7's functoriality pre-check applies to every session claiming a
   transport.
4. **Process discipline.**  Bound every run with `timeout` and `ulimit -v`,
   record the pid to `results/logs/<run>.pid`, and end runs **only by recorded
   id, never by matching a name pattern** — I ended my own shell that way during
   batch 10.
5. Pre-registration before computation; `python-flint` for exact linear algebra;
   both house primes `2147483647` and `2147483629`; any `D > 0` cell goes
   through the verification protocol and must exhibit its kernel vectors.
6. Delivery by git bundle only.  No file over 5 MB.  Commit messages carry
   `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` and nothing else.

Queued housekeeping, unchanged: add a `gct-cert/1` kind for the `n = 3` result —
the verifier hard-asserts `n = 4` at `tools/verify/layer2.py:93`, and s63
recommended the one-line extension to `n ∈ {3,4}`.  C6 Mode B needs it.

---

## 9. If all three source attacks fail

The batch's honest output is then a theorem-shaped statement about why, and it
is worth writing: *a multiplicity space of dimension 274 that no available
construction realises below `10⁷` coordinates, on a ladder whose carrier is
already at 16% of full size when the multiplicity is 2.*  §2.1 makes that
sharper than it was yesterday — the cost is not concentrated at `δ = 24`, it is
flat along the whole ladder (89% of full size at `δ = 16`, where `a_δ = 188`,
and 16% at `δ = 12`, where `a_δ = 2`), which says the pathology belongs to the
wreath symmetry and its realisations, not to the degree.  Sol's compression of
the diagnosis is the one to write down:

> `dim M_λ` ≪ the size of every known realisation of `M_λ`.

That is a representation-theoretic *algorithm* problem, not a size problem, and
it is why S5 gets more important as the ladder measurement gets worse, not
less.

And the write-up does not depend on it: twenty-four dead routes, the ladder
theorem, Theorem P, Proposition S, the contact-order lemma, the specialisation
inequality, the conormal certificates, and now the programme's first exhibited
obstruction certificate (§1.1) — a `D = +1` produced end to end by its own
machinery, which is the one thing the record was missing on the positive side.

---

## 10. Sol's review of this plan — four corrections, and the list S1 carries

Sol reviewed the plan above and asked to freeze the architecture with four
corrections.  All four are accepted; the sections above already carry them.
Recorded here so the change is visible rather than silently absorbed.

**1. Multiplicity, not occurrence — my error.**  I described the P0-A result as
an exhibited *occurrence* obstruction.  It is not one: `mult_det = 5` and
`mult_per = 6` are both nonzero, so `S_λ` occurs in both coordinate rings.  It
is a **multiplicity obstruction**, which is both the correct term and the
stronger claim, since occurrence obstructions are ruled out in the padded regime
and multiplicity obstructions are not.  Fixed in §1.1 and in
`analysis/wk11_int_p0a.py`, and the run was repeated so the banked verdict in
`results/wk11_int_p0a.json` carries the corrected reading rather than a
hand-edited one.  The numbers are unchanged.

**2. C3's success semantics were loose.**  `rank S_{λ,24} = 274` does not
establish padded full rank; it clears the universal reducible-normalisation
stage and leaves the permanent-specific cubic stage free to drop rank
afterwards.  The valuable branch is the converse, which my kill line
understated: `rank S < 274 ⟹ mult_pad ≤ mult_red < 274 ⟹ i_pad ≥ 1`, and with
`i_det = 1` that is `D ≤ 0` at LMR, decided by a `274 × 521` rank before any
permanent block is touched.  Fixed in the C3 row and §4C.

**3. The `r = 5` target statement had a logical gap.**  Quantifying over
irreducible components of `Sing V(J)` misses components of the exceptional
divisor supported over proper subloci, over incidence strata, or over embedded
non-reduced structure — and s66 §5 *measured* exactly that non-reducedness at
every pairwise incidence.  The target is now quantified over irreducible
components of the normal cone `Proj gr_J R`, and §6 also pins the residue to the
four loci s66 §8 already names, so C5 and S3 close a finite list.  Fixed in §6.

**4. C1 needed its initial condition pre-registered.**  The birth-space
recursion is only as good as `M₁₂`, and `M₁₂` is the hard object.  The seed step
is now its own pre-registered item with its own verdict, and an unreachable seed
is a reportable first wall rather than a silent assumption.  Fixed in the C1 row
and §5(iii).

### The mechanism families S1 must cover

Sol's list, adopted verbatim.  S1 audits each, and returns every candidate as
`(r, δ, λ, a_δ, n_χ, expected support)` rather than as a citation:

1. Young and Koszul flattenings
2. Hessian and minor equations
3. conductor and non-normality equations
4. singular-locus and Jacobian equations
5. Landsberg–Manivel style modules
6. boundary-component equations
7. equations obtained from dual varieties
8. restrictions and specialisations of larger determinant equations
9. any computational-algebra results on `closure(GL·det₄)`
10. equations of the **orbit** versus the **orbit closure**, carefully
    distinguished

The prize is stated plainly in the brief: one guaranteed determinant equation at
`r = 5, 6, 7, 8` would give a positive kernel cell with a manageable carrier.

### Where the Ramanujan idea actually lives

Not in the birth sequence as a numerical series, and not in a standalone
`q`-series session.  It is in the decomposition `M_δ = J(M_{δ−1}) ⊕ B_δ` with
`dim B_δ` tiny, and the task of constructing `B_δ` directly — the recurrence
rather than the coefficient.  If S5 finds `B_δ` controlled by a partition
algebra, a small Bratteli diagram, a constant-term coefficient or a `q`-difference
recurrence, the programme follows that structure, and only if the resulting
generating series is naturally mock or false modular does mock theta return.
The `F₄` coincidence stays where Sol put it: a thirty-minute falsifier inside
S6, killed in writing by default.
