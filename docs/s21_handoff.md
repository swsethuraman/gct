**Status change, and a priority change. Read before continuing.**

Your degree-24 work is **merged and pushed**. `main` is now at `5cdc29c` on
`https://github.com/swsethuraman/gct`, and it contains your branch's full
history — including the pre-registration commit `f9b4485`, with its original
timestamp. The `s21-degree24` branch has been deleted locally because it was
fully merged; nothing was lost.

The theory session's work is merged too, and that is what changes your queue:
**the totals law is now Theorem 5.5 in the paper, with a proof.** It is no
longer a conjecture. That raises the stakes on the value below.

**Before anything else:** re-clone or `git fetch` and start a fresh branch off
current `main`. Do not continue on the old branch — its content is already in
`main` and you would re-apply it.

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s21-xm3
```

Push only that branch, never `main`. If your push is still refused by the git
proxy, keep committing locally and send a `git bundle` of the branch at each
milestone, as before — that worked.

---

## Job 1 — TOTAL at X₋₃. This preempts everything.

**Pre-registered by session 22, before any measurement:**

```
TOTAL(X_-3) = -3,456,432,000 = -3 x 1,152,144,000 = 151,200 x (-22,860)
```

Inputs are in the repo: `inputs/evalin/f1Xm3_00.txt` … `f1Xm3_35.txt`. One value
is already banked from session 16:

```
f1Xm3_00 = +893,138,400 = 151,200 x 5907
```

Assemble the orbit exactly as `results/results_T4.md` assembles TOTAL(X₄) —
orbit representatives with weights summing to 36.

**Why this one, and why now.** Session 22's proof is a parity argument: it turns
on `det(transpose) = (−1)³ = −1` on M₃, on 6 being even so `det(q)⁶` drops, and
on the transpose coset therefore not contributing. Every total ever measured
sits at Ψ ∈ {0, 1, 4} — all non-negative. **Ψ = −3 is the first value that can
detect a sign error in that argument**, and nothing else in the banked set can.

It is demanding in the same way X₄ was: the one banked value is *positive*
(+5907 in cofactor units) while the predicted total is *negative* (−22,860), so
the unmeasured values must overturn it — exactly as at X₄ six unmeasured values
had to contribute +8,485,344,000.

**Read `PROJECT_NOTES.md` sessions 15 and 16 side by side before you start.**
Session 15 proved a theorem by interpolation, closed every measured class, and
pre-registered four completing runs; all four hit. Session 16 then ran one
off-locus point, got `f1X4_00 = −308,145,600` against a pre-registered
`+434,851,200`, and the theorem was retracted. Session 22's situation has the
same shape, and now the claim is in the paper.

**If the value does not match:** do not adjust anything to fit. Report the
mismatch, log it as a refutation in the session-16 style, and name which of the
proof's two consumed inputs it falsifies. Theorem 5.5 then gets retracted and
the paper reverts to the conjecture form — that is a result, and the record
already contains three refutations kept honestly. If it does match, say so
plainly: it is the first confirmation at a negative gauge value and the first
independent test of the χ ↔ det² identification.

## Job 2 — deliver the second bracket structure

Your last report had this still running, forced to `−3,520,661,760,000` by the
ratio `35/246` you committed at `b0401a8` before either value existed. That is a
genuine independent check — a different pair-degree profile, so not an S₈
relabelling. It is not yet in the repository. Commit it to
`results/results_deg24.md` and say whether it landed on the forced value.

## Job 3 — scope degree 30, do not launch it

`⟨18,24⟩` is every multiple of 6 from 18 up **except 30**, so this single value
determines the entire invariant semigroup. But your own note records why it is
not a one-number question: the ambient dimension at δ=30 is **4**, so
nonvanishing is one evaluation while vanishing needs all four; and the bracket
problem is 10 brackets over 30 letters, exceeding `br2.c`'s 63-bit packing and
the container's disk.

Produce the scoping document — wider state or a factoring, what each costs — and
stop there. Launching before the packing question is settled repeats the week-3
disk failure that cost a day.

## Job 4 — is Φ₁₈ primitive?

The canonical integral choice is the primitive generator of the rank-one lattice
of integral invariants in degree 18, the convention under which
`Ψ = −I₆^prim` has coefficient 1. Our reported

```
Phi_18(det_3) = -877,879,296,000 = -2^16 3^7 5^3 7^2
```

is in the engine's normalisation. Nobody has checked whether that is primitive.
The content divides `gcd(Φ₁₈(det₃), Φ₁₈(per₃)) = 2^16 · 3^4 · 5 · 7`, a weak
bound. Either compute the content of the explicit invariant, or tighten the gcd
over further integer evaluation points until it stabilises. The same question
applies to Φ₂₄. If either normalisation is a proper multiple, the quoted
factorisation must be divided through and restated — Remark 4.7 currently flags
this as open, and it is the part of the paper a reader is most likely to quote.

---

## Standing

Pre-register before every value. Exact arithmetic only. Regression suite before
any reported number: `quad = 24`, `quad0 = 0`, `quadq raw 6×4 = 24`;
`det3 L2 = 29/29/29` through `L6 = 1818118/2336283/2686868`;
`f1C_00 L7 = 54685987/100774838/141001840`,
`L8 = 128027708/422952740/603408404`. Two independent routes for anything
reported. The container is scratch — it has now been lost six times — and the
repository is the only durable copy.
