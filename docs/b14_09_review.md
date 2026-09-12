# Integrator review — B14-09

**Verdict: ACCEPT.** The slot the board demoted, and it returned two corrections
to banked material plus an instrument that makes a previously unaffordable table
cost seconds. I implemented its central identity myself and it holds.

Branch `b14_09_sixrow_d10`, tip `ac70a9c0`, 10 commits over `9898e569`. md5
verifies. Intake CLEAN — and my refined check 9 correctly read its prose mention
of the session-link rule as a placeholder, which is the B14-06 fix working.

## I implemented the identity and it holds

`n_chi = (1/|G|)·Σ_g χ_μ(g)·|Fix_X(g)|`, with the Young subgroup `Stab_W(μ)`, the
sign twist on odd repeated parts, and `|Fix_X(g)|` as an unbounded knapsack over
the `⟨g⟩`-orbits of `exps(n,r)`. Written from the stated identity, sharing nothing
with the delivery.

| check | result |
|---|---|
| my `n_chi` vs theirs, 18 sampled cells of B13-05's 222 | **18 of 18 agree** |
| my group order vs the recorded `stab` | **exact on all 18** |
| pre-registered `n_chi` vs builder-measured, all decided cells | **32 of 32** |
| decided cells reading `units = 0`, i.e. `mult = a`, both primes | **32 of 32** |

## Correction 1: `n_chi_lb` is not a lower bound

`results/b13_05_final.json` carries `n_chi_lb` on 222 open cells, equal to
`N_S/|Stab|` — verified, `604420/4 = 151105`. Of the 18 I recomputed, **10 fall
strictly below it**. They report 135 of 222, ratios 0.2586–2.0433, measured sum
85,260,365 against 91,516,374 recorded.

**I have not renamed the field.** It is banked data other sessions may have
pinned by blob, and renaming it mid-batch is the wrong trade. Indexed instead as
`nchi_lb_field_is_false`, carrying their reasoning as the justification: *a
machine-readable field whose name asserts a bound that does not hold is worse
than a prose error, because the next consumer will not re-derive it.*

## Correction 2: confirmed and fixed in the code

`analysis/wk13_b08_per6_lean.py` line 58 read *"(every weight with `N_S / |Stab|`
above that)"* — the retired identity, sitting in the docstring a worker reads
**while routing a cell**. The count of 17 is right; they measured all 95 and got
17 with zero disagreements. The rule is not. Removed, with the measured spread
0.355–2.9595 over the 402 in its place and the note that correct routing here was
luck rather than a criterion. The board was corrected in batch 14; the code
comment had not been.

## C5 is a genuine registered prediction

`sizing.json` was committed at `08734607`, **before** the first decision record —
I checked the commit order. Every subsequent build measures `n_chi` again by
enumerate-and-canonicalise, sharing no code with the character sum, and the two
agree at 32 of 32. A sizing table that cannot be checked is a table of
assertions; this one is a prediction with 32 independent tests against it.

Measured side by side in its C4: `(4,4,4,4,4,4)₈`, `|Stab| = 720`,
`N_S = 1,080,580` — `orbit_setup_arr` **427.63 s**, character sum **0.28 s**, same
answer. That gap is why the table did not exist.

## What it did not reach, and why that reads correctly

None of the 19 cells with `n_chi ≥ 2²¹` was decided, and the report explains
rather than glosses: the decision cost is superlinear in exactly the quantity
that puts them over the guard. Its fitted law —
`decide_secs ~ n_chi^1.224 · a^0.084` — is the useful artefact, because it shows
the queue's `N_S` ordering orders by the wrong variable. Rank 402 is the largest
cell by `N_S` and has the **smallest** `n_chi` of all 58.

The `ulimit -v` lesson is concrete and actionable: address space, not resident
memory, and the hybrid kernel's peak is set by `n_chi`, so seven cells that had
**built successfully** died in the kernel phase under a 3 GB bound. Its proposed
rule — bound from measured `n_chi`, not `N_S` — needs a number nobody had before
this session.

It is also correct that this advances neither objective: a permanent-specific
equation would *raise* `i_pad` and therefore *lower* `D`. The board demotes the
slot on exactly that and the report agrees rather than arguing.

## Its defect 3 is a real inconsistency, and it is mine

Board §5 says `--base <the commit in your packet>` while the packet says,
correctly, that it cannot contain that commit and that the value lives in the
dispatch message. With no dispatch message arriving — **now reported by eight
sessions** — the chain has no terminal. The tag is the only thing in the
repository that resolves it, so §5 should name the tag and the peel command.
That, plus B14-07's tag-annotation suggestion, is the batch-15 fix.

Its defect 6 is also fair: "record the model that actually ran this session"
assumes one model per session, and B13-08 had two. A `models: [(model, phase)]`
field makes that recordable.

## Owned rather than left to a reviewer

It caught a hand-typed figure in its **own** commit message — "0.84–1.35" where
the true spread over the 402 is 0.355–2.9595 — and notes that the report
generator exists precisely so a hand-typed number gets caught against the
artefact. That is the right instinct and the right place to say it.
