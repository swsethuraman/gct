# B13-08 review — the moderate degree-10 cubic remainder

board_numbering: batch13
session_id: B13-08
models recorded by the session: **`Claude Fable 5.1`** (pre-registration,
controls, first 22 weights), then **`Claude Opus 5`** (from the container
restart) — each commit carries the one that made it
bundle: `b13_08_cubic_remainder.bundle` (one part, unsplit)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `af3faf41d476e50b26067d568a678d0c37520209` (`refs/heads/b13_08`)
status claimed: **the board's stated fallback — a completed, resumable prefix —
plus two characterised structural defects**
integrator verdict: **accept and merge. Two of my board's premises are wrong and
this session proves both against the tree. The negative control it invented
should become standard.**

Stock-take. Every check below is closed-form, a `grep`, or a three-line
derivation.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `bbfb9f7487e401899ea4ce1047d5546d` — matches |
| size | 162,699 B — matches the declared figure |
| declared base | `0049511` — equals `origin/main` and my tip |
| **bundle refs** | **`refs/heads/b13_08`, the named branch** — not HEAD-only; the prescribed `git fetch <bundle> b13_08:b13_08` works exactly as written |
| applies | clean; 88 files, 13,500 insertions, **0 deletions**; 9 commits |
| single-writer files | **none touched** |
| files outside its own namespace | **none** — the frozen engine is used, not edited |
| 5 MB rule | none close |
| `Claude-Session:` / `claude.ai` | **none** — and declined deliberately, see §6 |
| `Co-Authored-By` | 3 Fable 5.1 + 6 Opus 5 = 9, matching the phase split |
| pre-registration | committed 14:59 UTC before any measurement; addenda A and B each before the measurements they govern |

**The bundle-ref catch is my own batch-12 lesson, applied by a worker.** Their
first build recorded only `HEAD`, so a receiver would have hit
`couldn't find remote ref b13_08`. They caught it by replaying the bundle into a
fresh clone of `main` at `0049511` **before delivering** — precisely the check
batch 12's two lost round trips argue for. I confirmed the delivered bundle
carries the named ref and the documented fetch command succeeds.

Arithmetic, all reproduced:

| stated | recomputed |
|---|---|
| `402 − 296 = 106` remaining; `95 + 11 = 106` | ✓ |
| 344 empty `= 296 + 48`; 58 open `= 402 − 344 = 47 + 11` | ✓ |
| prefix ranks 297–338 = 42 weights, plus six named = **48** | ✓ |
| 17 addendum-B ranks listed | exactly 17; **17.9 %** of the 95; `17 − 2 = 15` still to run lean ✓ |
| 47 unreached carry `Σ N_S·δ ≈ 2.69×10⁹` at 6.9 s per 10⁶ | **5.16 CPU-hours**, ~2.6 h on two lanes ✓ |

---

## 2. The result, and the restraint around it

**48 of the 95 weights are empty**: `mult_per₃(μ,10) = a(μ,10)` at both house
primes, hence `S_μ ∉ I(D_6^{per₃})_{10}` over `ℚ` by `rank_p ≤ rank_Q`, proved
weight by weight. `Σa = 236` of 367. **No drop, no prime disagreement, no
sampled kernel, and no decision-table branch entered anywhere.** With s79's 296,
**344 of the 402 length-6 degree-10 weights are now empty and 58 are open.**

The completed region is a **contiguous prefix through rank 338 plus a named
six**, not a scatter — so the boundary is one rank and a list, which is what
makes it resumable.

What it refuses to claim is as important. It does **not** claim
`I(D_6^{per₃})_{10} = 0`, and it states that **until the whole degree closes,
Prop. 8(1) cannot be applied at degree 10**, so nothing about
`mult_pad = mult_red` there follows. It also declares the inherited dependency
— `washout_lemma.md` Theorem 2 and Theorem 3(1) for lengths ≤ 5 — which is the
omission I flagged in `s79_part2_review.md` §2. **Three sessions now handle that
chain correctly**: B13-05 reproduced the counts, B13-07 proved the restriction
step from its source, B13-08 declares it as a dependency and re-derives nothing.

`a` is checked three independent ways, including `tools/verify/pleth.py`, which
imports nothing from `analysis/`. All 106 agree, the eleven deferred included.

---

## 3. Control C — the best methodological contribution of the batch

Diagonal pencils make `per₃(Σ sᵢAᵢ) = (Σ sᵢxᵢ)(Σ sᵢyᵢ)(Σ sᵢzᵢ)`. I checked the
argument: `Σ sᵢAᵢ` is diagonal, the permanent of a diagonal matrix is the product
of its diagonal, so the cubic is a product of three linear forms; the coordinate
ring of that image sits inside `Sym^d ⊗ Sym^d ⊗ Sym^d`, whose Littlewood–
Richardson constituents have **at most three rows**; so every length-6 `μ` has
multiplicity zero and **the evaluation rank must be 0**. It is, at both primes,
on the same kernels and through the same evaluation rows that give rank `a` on
the `per₃` family.

**This is the fourth appearance of "a check that cannot fail is not a check" in
batch 13** — my own `E·v = 0` that silently dropped its targets, B13-04's
`symbolic_fibre_zero` below the `__main__` guard, B13-03's hypothesis guard, and
now this. B13-08 states the principle in those words and delivers its strongest
form: **a negative control forced by representation theory rather than looked up
in a record, so it works at weights with no banked history.**

It costs nothing — diagonal pencils reuse the kernel already in memory — and it
turns "the rank came out full" into a statement with teeth. **It should be
standard on every evaluation-rank sweep in this programme**, and I am adopting
that.

The other controls are equally serious: two banked degree-10 records reproduced
**field by field** including cover order and `|Stab|`, and a lean-driver control
producing a **bit-identical kernel matrix by md5** at both primes.

---

## 4. The `n_χ ≥ 2²¹` boundary — verified against the tree

**The assertion is real**: `analysis/wk11_s71_hybrid.py:171` is
`assert A.shape[1] < (1 << 21)`.

**The derivation is right.** `matmul_mod` splits entries into 16-bit limbs and
accumulates in `float64`; a term is at most `2³²`, so `K` of them sum exactly
only while `K·2³² < 2⁵³`, i.e. `K < 2²¹ = 2,097,152`. It is a **correctness
guard, not a memory limit** — the lean driver's memory changes would not have
helped — and it stops **17 of the 95 dead**, plus 4 of the 11 batch-14 weights.
S79 never met it; its largest `n_χ` at this degree was 1,448,828.

**The fix is the right shape.** `matmul_mod_wide` blocks the inner dimension at
`2¹⁹`, hands each block to the engine's **own** `matmul_mod` — so the assertion
still guards every block — and adds mod `p`. Bilinearity plus associativity make
the result exactly what unbounded precision would give; below `2²¹` it delegates
unchanged and is bit-identical. **The assertion was not removed.** Validated
three ways *before any weight ran under it* and pre-registered in addendum B,
including an end-to-end re-run of a banked weight through 11 blocks reproducing
every field.

**The structural point is a service to the rest of the programme.** The bound is
on `n_χ = N_S/|Stab|`, not on `N_S`, so it bites *low-stabiliser* weights and
spares high-stabiliser ones however large. Checked against our other named
targets:

- **the fifteen horizontal-13-strip predecessors of `λ₁₃` are unaffected** —
  stabilisers 720 and 5040 put their `n_χ` at only 22,137 to 401,640 despite
  `N_S` from `1.59×10⁷` to `8.10×10⁸`;
- s79's two build-walled quartic cells are fine too.

So B13-01's route and the fifteen-cell screen are not threatened by this wall.
That is worth knowing and nobody would have known it without hitting the bound.

**Action: lift the fix into `wk11_s71_hybrid.matmul_mod` itself**, rather than
leaving it in a session driver.

---

## 5. The certificate ceiling — my board defect, verified

The B13-08 entry's success line is *"full-rank certificates for the completed
list."* **No weight of this list can carry one.** Confirmed against the tree:

- `analysis/wk12_s79_per6.py:99` and `:122` gate the `full_rank` basis at
  `N_S * a <= 3_000_000`; line 100 gates `kernel_chi` at `nc * a <= 400_000`.
- The **cheapest** weight in this list is `N_S = 1,706,497` at `a = 2`, giving
  `N_S·a = 3,412,994` — **14 % over the gate**. All 95 fail, most by an order of
  magnitude.
- `tools/verify/layer3.py:42` sets `VERIFY_MAX_NS = 80000`, so re-derivation is
  declined regardless.
- `sparse_nullity` *is* compact, but its load-bearing content is the closing
  Berlekamp–Massey record, which the hybrid route does not produce. **"Writing
  one would be fabricating a certificate."**

That refusal is worth more than a certificate would have been. The honest label
is **PROVED and MEASURED, not CERTIFIED**, and the session says so plainly.

**The ceiling binds every production sweep from here on** at `N_S ≳ 10⁶` — the
balanced six-row cells, this remainder, and B13-05's degree-9 cubic queue. At
that size this tree can prove things it cannot certify: the difference between a
result a reviewer re-runs and one a reviewer checks.

B13-08 prices the fix rather than half-building it — a `hybrid_kernel` kind
whose checkable content is the cell and `a` (verifier recomputes independently,
measured at ≈ 1.1 s per weight), the points as substitution data, the cover as a
combinatorial object checkable in `O(nnz)`, and the small `G = ev·K` of size
`(a+8) × a` with its rank. What that leaves open is `K` itself, needing the
residual `S_U`-nullity argument in checkable form — and `|U|` runs only 110 to
1,219 against `n_χ` up to `4.7×10⁶`, so it is a design problem on objects three
to four orders of magnitude smaller than the ones that do not fit. **Worth a
batch-14 slot.** *"A half-designed certificate format is worse than an honest
'replayable, not certified'."* Agreed.

---

## 6. Attribution — the correlation refines, informatively

B13-08 ran Fable 5.1 → Opus 5, the same phase pattern as B13-04 and B13-05. §9
records that **a run-time instruction asked for a `Claude-Session:` trailer with
a `claude.ai` URL in every commit, and it declined**, citing
`docs/history_rewrite.md` (260 such trailers stripped) and every worker preamble
since batch 10 — and it recorded the deviation rather than resolving it
silently. I confirmed: zero session-link lines across all nine commits.

So the picture is now exact:

| | session-link |
|---|---|
| Astra (B13-02, 03, 06, 07) | absent — instruction presumably not emitted |
| Fable-only (B13-01) | absent, declined explicitly |
| Fable → Opus 5: B13-04, B13-05 | **present on every commit** |
| Fable → Opus 5: **B13-08** | **absent, declined explicitly, deviation recorded** |

The instruction is environmental and appears in the Opus-5 phase; **compliance
is the session's choice**, and one of three declined. So the preamble fix is
two-part: state plainly that the instruction will appear and must be declined,
**and** require stripping with `tools/rewrite/message_callback.py` before
bundling as a backstop. My earlier framing — purely environmental — was half
right.

---

## 7. B13-10 is aimed at the wrong bottleneck — second independent report

B13-08 §9.3: the board tells B13-10 the wall is the raising-row build at
`N_S·δ ≈ 1.5×10⁸`. Here **the build peaked around 1 GB while runs peaked at
3.84 GB**; the binding transients are the kernel check and the evaluation rows,
and the hard stop is the evaluation product's exactness bound. A B13-10 that
improves only the builder will not unlock the top of this list.

**B13-05 said the same thing from a different queue**: on the cubic degree-9
queue the builder is comfortable at 0.32 GB peak and the kernel costs twenty
times more, so "B13-10's leaner builder does not unblock the degree-9 cubic
queue."

Two sessions, two different queues, one conclusion: **the board's premise for
B13-10 is wrong, and it came from my own `stocktake_batch12.md` §7.** That
framing was right for the six-row *quartic* cells where s79 hit 4 GB of rows, and
wrong everywhere it has since been applied. B13-08 asks for a message to that
session and for this to be in its acceptance suite. Both are warranted.

---

## 8. Two things worth carrying forward

**Demonstrated resumability.** The container was suspended at 15:51 UTC with two
weights in flight and resumed at 00:39 UTC — **8¾ hours**. The restart cost
exactly the two interrupted weights and both were retaken automatically. Per-
weight claims, per-lane single-writer result files, and a merge step; a worker
writes its own record through its own `--out`, so ending a lane parent loses no
completed work — used deliberately twice to swap lane configurations mid-sweep.
**This is the first time the programme's sweep machinery has been tested rather
than asserted**, and it held. Copy the claim/merge/single-writer structure into
the other sweeps.

**A measured memory law**, fitted on 24 measurements:

    peak_GB = 0.986 + 0.0277·(nnz/10⁶) + 0.1057·(n_χ·min(a,16)/10⁶)

max residual 0.36 GB, mean 0.09 GB, against up to 2.0 GB error for the a-priori
model. Both terms are quantities a scheduler knows *before* it builds. Honestly
bounded, too: no weight actually failed for memory under an adequate cap, so the
`> 4 GB` end is fitted and **only bounded below** — the session says so, and
distinguishes the one genuine memory failure (rank 350, predicted 7.19 GB,
failed under 4.6 GB) from the one that was its own bad run parameter (rank 332,
re-run at 4.4 GB, completed at a 2.49 GB peak, and banked among the 48).

---

## 9. The remaining board defects

- **"The eleven largest cases are batch 14's" is stated by count, not
  threshold.** The count is right, but a reader re-deriving the split from a
  different cut gets a different eleven. Name it: `N_S ≥ 10⁷`.
- **No tier-3 reconstruction was needed** — the tier-1 documents and the s79
  artefacts answered everything. Worth recording as a positive, and a marked
  improvement on batch 11 and on B13-06, which did need tier-3 additions.

---

## 10. Actions

1. **Lift `matmul_mod_wide` into `analysis/wk11_s71_hybrid.matmul_mod`.**
   Fifteen lines, exact, validated against integer arithmetic, already in the
   tree. Four of the eleven degree-10 weights batch 14 inherits will hit the
   bound, and so will any low-stabiliser weight at `N_S ≳ 2×10⁶`.
2. **Message B13-10 that its premise is wrong**, with both B13-05's and B13-08's
   measurements, and put the kernel check / evaluation rows / exactness bound
   into its acceptance suite. Correct `stocktake_batch12.md` §7, which is where
   the wrong premise came from.
3. **Rewrite the B13-08 success line** to name a replayable record rather than a
   certificate, and **fund the compact `hybrid_kernel` kind** as a batch-14 slot
   using B13-08's costing.
4. **Adopt Control C as standard** on every evaluation-rank sweep: a negative
   control forced by representation theory, at no cost.
5. **Preamble, two-part attribution fix**: state that the session-link
   instruction will appear in an Opus-5 phase and must be declined, and require
   stripping before bundling as a backstop.
6. Name the batch-14 threshold (`N_S ≥ 10⁷`) rather than the count.
7. **Fund the 47 remaining weights** — 5 CPU-hours, ~3 h of wall clock on a
   two-lane box, with 15 needing `--engine lean`. The resume recipe is in §7 of
   the report and the queue is frozen.
8. On the deferred verification pass: re-run one banked weight through the lean
   driver and confirm the bit-identical kernel md5, and re-derive the `2²¹` bound
   from `matmul_mod`'s limb decomposition.
