# Session 70 (C3) — the two ranks at LMR, and which of them needs a source

Batch 11, **partially gated** — and your first hour decides how much of it is.
**Read `docs/batch11_worker_preamble.md` first**, then `docs/batch11_plan.md`
§2.2, §3 (your row), §4C, §5(ii) and §6, which together are this brief's
mathematics.  Then `docs/reducible_engine.md`, `docs/reducible_ideal.md`,
`analysis/wk9_s42_hpad.py`, `analysis/wk9_s60_cell.py`, `docs/s60_report.md`
§ (the eleven `mult_red < a` cells) and `docs/s64_report.md`'s calibration table.

## The two numbers

At the LMR cell `λ = (65,17,2⁷)`, `δ = 24`, `a = 274`, `h_pad = 521`:

    rank S_{λ,24}      the 274 x 521 reducible-normalisation split;  rank S = mult_red
    det A₂₄            the degree-24 Gram restricted to J(M₂₃), a 273 x 273 determinant

**Run `rank S` first.**  It is the cheaper number, it is the one that can settle
the cell on its own, and its outcome tells you whether `det A₂₄` is worth the
night.

## Part A — the determination, in your first hour, ungated

`det A₂₄` needs the explicit source.  **Does `rank S_{λ,24}`?**

`S` comes from S3's padded factorization `M^{(4)}_λ → ⊕_μ M^{(3)}_μ → ⊕_μ M^{(3)}_μ/K_μ`
together with the `h_pad` Pieri identity of session 42, which is implemented and
proved (`analysis/wk9_s42_hpad.py`, Kempf collapsing).  `h_pad(LMR) = 521` is
computed and banked.  If `S`'s rows are indexed by the Pieri shapes and its
columns by the ambient multiplicity rather than by explicit source vectors, then
`S` is computable from `λ` and `δ` alone and this half of your session is
ungated.

**Settle that in writing and take the corresponding branch.**  Report the
determination either way, with the construction written out — nobody has written
it down, and the answer is reusable whichever way it goes.

## Part B — `rank S_{λ,24}`, and what each outcome means

The four outcomes are **not symmetric**, and a session that reads
"success = 274" will mis-report two of them.  Use these semantics exactly:

- **`rank S < 274`.**  Then `mult_pad ≤ mult_red = rank S < 274`, hence
  `i_pad ≥ 1`.  With `i_det = 1` that gives `D ≤ 0`: **the LMR cell is settled
  against a `D > 0`, by a `274 × 521` rank, before any permanent-specific block
  is touched.**  This is the strongest cheap outcome available in the batch and
  it is a full result.
- **`rank S = 274`.**  Then `i_red = 0`.  It does **not** establish padded full
  rank: `S` is the universal reducible-normalisation stage, and the
  permanent-specific cubic stage can still drop rank afterwards.  So `i_pad`
  remains unknown and session 73 must determine it.  Say exactly this in your
  report; do not write that padded full rank is established.

## Part C — `det A₂₄`, and why the singular branch is the better one

The `a`-ladder ends `…, 272, 273, 274`: the last two increments are exactly one,
so `δ = 23` and `δ = 24` are **room-one** rungs, and

    G₂₄ = [[A₂₄, b], [bᵀ, c]] ,   s = c − bᵀA₂₄⁻¹b = det G₂₄ / det A₂₄ ,
    s = 0  ⟺  the equation is born  ⟺  i_det(24) ≥ 1

with `A₂₄` the **degree-24** Gram restricted to the transported predecessor
`J(M₂₃)` — the corrected denominator, not the predecessor's own Gram.  Session
68 is computing the same object as its terminal rung; use the plan's definition
verbatim so the two compose.

- `det A₂₄ ≠ 0` gives `i_det = 1` outright.
- **`det A₂₄ = 0` is the stronger outcome**, not a failure: it means
  `mult_det(23) < 273`, i.e. `i_det(23) ≥ 1`, i.e. a determinant equation at
  `ℓ = 9` of **degree 23** — strictly stronger than LMR, and session 57 calls
  `(61,17,2⁷)₂₃` the sharpest single test of "nothing below 24" that exists.

Both primes.  `rank(MᵀM) ≤ rank(M)` holds in every characteristic, so the
nonsingularity step is characteristic-free; `rank(Θ*Θ) = rank Θ` is char-0 only
and must not be used here.

## The ungated fallback — required, not optional

If no source lands and `rank S` turns out to be source-dependent, **do not idle
and do not fall back to the LMR carrier-space engine** that session 63 measured
dead on all three realisations.  Instead:

1. Document the source-dependence precisely — that is Part A's deliverable and
   it stands on its own.
2. Implement the same `S` construction on two banked, manageable `n = 4` cells
   and report their exact ranks and costs.  Both are *discriminating*
   (`mult_red < a`), so they calibrate `S` against banked truth rather than
   against a tautology:

        (8,4,4,4,4)_6    a = 2,  h_pad = 1,  mult_red = 1,  i_red = 1,  mult_pad = 1
        (12,9,9,1,1)_8   a = 7,  h_pad = 6,  mult_red = 5,  i_red = 2,  mult_pad = 5

   so `S` is `2 × 1` and `7 × 6` there, and a correct construction returns
   `rank S = 1` and `rank S = 5`.  Both are strictly below `a` — exactly the
   regime that matters at LMR.  A construction that returns `a` at either cell
   is wrong, and finding that out is worth more than an LMR number you could not
   have trusted.

## Success

The Part A determination in writing; `rank S` at LMR with the correct semantics
attached, or the two calibration ranks; and `det A₂₄` at both primes if a source
is available.

## Stopping rules

- A calibration cell disagreeing with its banked `mult_red` halts LMR use of `S`
  immediately.  Report the mismatch; it is more valuable than a workaround.
- Do not attempt the LMR carrier build under any circumstance.
- If `rank S < 274`, that settles the cell — report it and do not spend the rest
  of the night on `det A₂₄`, whose answer no longer changes the verdict.

## Deliverables

`results/PREREG_s70.md`; `docs/s70_report.md` with the Part A determination in
its first paragraph; the `S` construction written out in `docs/s_split.md`;
ranks and costs as `results/s70_ranks.md` and `.jsonl`; certificates for any
exact rank claim in `results/certs/`; code under `analysis/wk11_s70_*.py`;
bundle `s70_tworanks.bundle` + `.md5`.
