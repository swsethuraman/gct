# Session 79's Part 2 — verified, and one gap that matters

The bundle came in **three** parts, not two; `part00` was missing from the chat
and I staged it from `Projects\gct` directly.  Reassembled, md5
`2b352f31…f033` matches and the bundle verifies (HEAD `c20fb6f4`, base
`afb8c33`).  Merged at `0ed24cc`.  `analysis/wk12_int_s79_part2_verify.py`:
**17 of 18**, the one failure a deliberate flag, below.

## 1. What reproduces

| | |
|---|---|
| 682 six-row cells delivered, all distinct | **PASS** |
| `i_det = 0` at every one | **PASS** |
| `mult_pad = mult_red` at every one | **PASS** |
| `i_per4 = 0` at every one | **PASS** |
| 59 reducible drops; 58 with ≥ 2 trailing 1s; histogram `{1:1, 2:7, 3:51}` | **PASS** |
| the largest bite is `−25` at `(13,9,9,3,1,1)₉` | **PASS** |
| `a` at a stratified sample of quartic cells, by my own Weyl alternation | **PASS** |
| the degree-9 cubic scan: 210 distinct weights, `Σa = 592`, `max a = 9` | **PASS** |
| every degree-9 and degree-10 cubic record reports `mult = a` at **both** primes | **PASS** |
| my Weyl alternation reproduces `a(μ,9)` at all 210 scanned weights | **PASS** |
| the scan covers every length-**exactly-6** partition of 27 with `a ≥ 1` (331 candidates) | **PASS** |

## 2. The gap — `I(D₆^{per₃})₉ = 0` is not yet established

The scan ran the 210 weights of length **exactly** 6.  There are

> **365 further partitions of 27 of length ≤ 5 with `a(μ,9) ≥ 1`, `Σa = 1213`**
> — by length: 1 at ℓ=1, 11 at ℓ=2, 48 at ℓ=3, 117 at ℓ=4, 188 at ℓ=5; the
> largest are `a = 11` at `(13,8,4,2)` and `(11,8,4,2,2)` —

and **none of them was scanned**.  `Σa = 1213` is more than twice the 592 the
scan covered.

They are not optional.  `I(D₆^{per₃})₉ = 0` is a statement about the whole
degree-9 part, and Prop. 8(2) pairs a six-row `λ` with a `μ` such that `λ/μ` is a
horizontal 9-strip — `μ` interlaces `λ`, so `μ₆` may be 0 and a `μ` of length 5
pairs with a `λ` of length 6.  So a permanent-specific equation at a six-row
degree-10 weight could sit at a `μ` the scan never looked at.

**What is established** is the length-exactly-6 part of `I(D₆^{per₃})₉`, which is
a real result and covers those `λ` whose partner `μ` has six parts.  What is not
established is the theorem as stated, or its Prop. 8(1) consequence at every
six-row weight of degree 9.

**Closing it is cheap and it is the first task of batch 13.**  A weight of length
`k < 6` sees only `Sym³Cᵏ`, so its multiplicity is the length-`k` one and its
`N_S` is *smaller* than the length-6 weights already done.  s79 spent 5 884 s on
the 210; the 365 shorter ones should cost the same order or less on the same
instrument, and the same gap applies to the degree-10 scan, which counted only
length-6 weights among its 402.

This is not a fault in the measurements — every rank s79 reports reproduces.  It
is a scope statement that was written one quantifier too wide, and the honest
correction is to narrow the claim until the 365 weights are run.

## 3. What Part 2 is worth, gap included

Even restricted to length-6 weights, the picture is the one the goal cell
showed:

- 682 six-row cells, `δ ≤ 12`, tail weights 13–23: no determinant equation, no
  permanent-specific equation, no `per₄` equation;
- 69 first stable cells closing 63 tails for every degree by Proposition S;
- and `mult_pad = mult_red` everywhere, at a **third** length.

Together with s64 at `r = 5`, s74 and my own rung-13 measurement at `r = 9`:
three lengths, four instruments, no exception.  And Prop. 8(2) is the mechanism
— it says where to look next, and it says the looking is on the cubic side.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
