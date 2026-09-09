# S9 — sharpen Prop. 8: which quartic weights does one cubic element reach?

`board_numbering: batch13`.  A reasoning session.

## Why

Batch 13 is organised on Prop. 8 of `docs/transfer_lemma.md`:

> **8(2)** `mult_pad < mult_red` at length `r`, degree `δ` **requires**
> `I(D_r^{per₃})_δ ≠ 0`.
> **8(1)** `I(D_r^{per₃})_δ = 0` gives `mult_pad = mult_red` at **every** weight
> of that length and degree.

8(1) is what makes a cubic scan worth more than a quartic sweep.  8(2) is a
*necessary* condition, and the batch is about to spend four sessions on it.
Before batch 14 spends more, the programme needs to know what a **nonzero** `μ`
would actually buy.

## The questions

1. **Is the pairing tight?**  8(2) says a drop at `λ` needs a `μ` with `λ/μ` a
   horizontal `δ`-strip.  Does a nonzero `I(D_r^{per₃})_δ` at `μ` *produce* a
   drop at some such `λ`, or only permit one?  If only permit, a nonzero cubic
   weight is a lead and not a result, and the batch should say so in advance.
2. **Which `λ`?**  Given a nonzero `μ`, name the quartic cells worth measuring,
   in priority order.  A campaign that measures every `λ ⊇ μ` is unaffordable.
3. **The length quantifier.**  `μ` interlaces `λ`, so `μ_r` may be 0 and a `μ`
   shorter than `λ` pairs with it.  Session 79's degree-9 scan restricted to
   length exactly 6 and so missed 365 weights with `Σa = 1213`
   (`docs/s79_part2_review.md` §2).  State the quantifier once, precisely, in a
   form a brief can quote — including whether a `μ` of length `k < r` can ever be
   *ignored* because its `i` is the length-`k` value and that value is already
   known.
4. **Is there a converse at the level of a single weight?**  8(1) is a statement
   about a whole degree.  Is there a weight-by-weight version:
   `I(D_r^{per₃})_δ ∩ (the μ-isotypic part) = 0 ⟹ mult_pad(λ) = mult_red(λ)` for
   the `λ` paired with that `μ`?  If so, the scans become interruptible and a
   partial scan starts to pay.

## What you have

`docs/transfer_lemma.md`; `docs/exactness.md` §7 (`I(D₆^{per₃})_δ = 0` for
`δ ≤ 8`, s37/s43/s47); s79's degree-9 and degree-10 results and their scope;
`docs/stocktake_batch12.md`.

## Deliverable

A sharpened Prop. 8 with the quantifiers explicit and quotable, the priority rule
for `λ` given a nonzero `μ`, and an honest statement of which of the four
questions you could not close.
