# s81 — close the degree-9 cubic theorem at `r = 6`, then degree 10

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

Session 79 reported `I(D₆^{per₃})₉ = 0` and, through Prop. 8(1), that
`mult_pad = mult_red` at every six-row weight of degree 9.  **The scan covered
the weights of length exactly 6.**  It is one quantifier too wide.  Close it.

## What is true going in

- The scan ran all 210 length-exactly-6 partitions of 27 with `a(μ,9) ≥ 1`,
  `Σa = 592`, `mult = a` at both primes at every one.  I verified that: the 210
  are complete among the 331 length-6 candidates, and my own Weyl alternation
  reproduces every `a`.
- **365 further partitions of 27 of length ≤ 5 have `a ≥ 1`, `Σa = 1213`** — by
  length: 1, 11, 48, 117, 188; the largest are `a = 11` at `(13,8,4,2)` and
  `(11,8,4,2,2)`.  **None was scanned.**
- They are not optional.  Prop. 8(2) pairs a six-row `λ` with a `μ` such that
  `λ/μ` is a horizontal 9-strip; `μ` interlaces `λ`, so `μ₆` may be 0 and a
  length-5 `μ` pairs with a length-6 `λ`.
- A weight of length `k < 6` sees only `Sym³Cᵏ`, so its multiplicity is the
  length-`k` one and its `N_S` is **smaller** than the length-6 weights already
  done.  s79 spent 5 884 s on the 210.

Details and the derivation: `docs/s79_part2_review.md` §2.

## Task

1. The 365 length-≤5 weights, on `analysis/wk12_s79_per6.py` unchanged, both
   primes, in `N_S` order, a drop re-checked in the same call at `3a + 24` fresh
   points (seed 907) as s79 did.
2. Then degree 10 **completely**: the 106 unreached length-6 weights (`Σa = 379`,
   `N_S` from `1.71·10⁶` to `2.73·10⁷`) **and every weight of length ≤ 5**, which
   s79's census never enumerated.  Report the length-≤5 degree-10 census
   yourself; do not assume it.
3. Control before the queue: reproduce s47's `(7,5,4,4,2,2)₈`, `mult = a = 1`,
   and s43's `(11,4,4,2,2,1)₈` and `(10,6,4,2,1,1)₈` at `mult = a = 2`.  A
   nonvanishing test at `a = 1` cannot tell one point family from another; a
   rank-2 test can fail.

## Predictions and falsifiers

- **P1 (0.7):** all 365 empty, so `I(D₆^{per₃})₉ = 0` as stated and
  `mult_pad = mult_red` at every six-row weight of degree 9 is a theorem.
- **P2 (0.3):** a nonzero weight.  Then the preamble's protocol takes over
  **before it is reported anywhere**, and the quartic confirmation is sought at
  the `λ ⊇ μ` with `λ/μ` a horizontal 9-strip.  Stop the scan at the first one.
- **F1:** any `δ ≤ 8` re-run disagreeing with s37/s41/s43/s47 — stop, report.
- **F2:** your degree-9 length-≤5 census disagreeing with the 365 / `Σa = 1213`
  above — report it as a defect in this brief and use your own number.

## Deliverables

`results/PREREG_s81.md`; `results/s81_per6.jsonl` (every weight, both primes,
cost); the two censuses you computed; the corrected statement of what
`I(D₆^{per₃})₉` and `I(D₆^{per₃})₁₀` now are, with the unreached region priced;
`docs/s81_report.md`; bundle + `.md5`.
