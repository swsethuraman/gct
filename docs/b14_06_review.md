# Integrator review — B14-06

**Verdict: ACCEPT.** The slot the board called *"the only check that could
falsify the stable reformulation the programme leans on"*. It did not falsify it,
and combined with `lmr_D_upper` it closes B13-06's best target — which its own
report says is unavailable.

Branch `b14-06`, tip `cdd682fc`, 3 commits over `9898e569`. md5 on whole and
`part00`. Intake CLEAN (after a fix to my own gate, below). Pre-registration
first.

## Replayed on my host

| tail | family | rank, `2147483647` | rank, `2147483629` |
|---|---|---|---|
| `(17,2⁷)` | GEN | **274** | **274** |
| | DET | **273** | **273** |
| | PAD | **269** | **269** |
| | RED | **269** | **269** |
| | NEG | **0** | **0** |
| | DET* (C6, off `M_ℓ`) | **274** | **274** |
| `(19,2⁷)` | GEN / DET / PAD | **392 / 390 / 377** | **392 / 390 / 377** |
| | DET* | **392** | **392** |
| `(21,2⁷)` | GEN | **533** | **533** |

C4 agrees with the Weyl alternation on all twelve small tails (1,1,3,4,8,9 and
1,1,3,4,9,11). C1 returns exactly one bracket at tail `(2⁸)` with value
`8!·det(N₂)`. Every control ran with a twin that had to fail, and did.

The DET* rows matter: the instrument returns 274 and 392 when the determinantal
structure is removed, so **273 and 390 are detections, not undersampling**. And
`r_DET = 274` was pre-registered as a conflict with `lmr_ranks`, so 273 was a
reachable failure rather than a foregone conclusion.

The construction is genuinely different — no raising operator, no weight-space
enumeration, no `u`-tower, no transport exponent, no CRT. At the LMR tail the
existing route needs a 7.21×10⁹-dimensional weight space, so any reproduction had
to be a different construction. That is what makes this an independence test.

## It closes B13-06's best target

§5.3 derives `D((71,19,2⁷)₂₆) ≤ 2 − p` from its own new floor
`mult_det(target) ≥ 390`, and states that **`p ≥ 2` is not certified anywhere in
this tree**. That was true of the frozen base it worked from. `lmr_D_upper`
certifies `p = 3`.

    D((71,19,2⁷)₂₆) ≤ 2 − 3 = −1

Links, each checked here:

- `a((71,19,2⁷),26) = 392` banked, **equal** to `a_∞(19,2⁷) = 392` which I
  reproduced from my own derivation reviewing B14-04 — so `a = a_∞`, the cell is
  **stable**, and that is what lets the stable-tail values transfer to it;
- `transport_lemma_T` on `q62 = 8c₀c₂ − 3c₁²`, a nonzero HWV of weight `(6,2)` at
  degree 2 (B14-05 §2), carries `(65,17,2⁷)₂₄` → `(71,19,2⁷)₂₆` and carries **all**
  `p` directions, so `i_pad(target) ≥ 3` and `mult_pad(target) ≤ 389`;
- against `mult_det(target) ≥ 390`, replayed here at both primes.

Recorded as `b13_06_best_target_closed`, conditional on the banked 392 and on
`lmr_D_upper`'s own condition. **`(69,21,2⁷)₂₆` does not close this way**:
`a = 531 < 533 = a_∞`, so that cell is not stable and no stable value transfers.

It also flags a coincidence worth keeping: its determinant floor 390 at the
`(19,2⁷)` stable tail is numerically equal to the banked ambient
`a((63,19,2⁷),24) = 390`, and these are different numbers about different cells.
390 and 391 remain single-route.

## Its eighth instance is a real contribution

C6 first **passed for the wrong reason**. Perturbing `N_d` alone leaves `Z`
entirely, and the "corrupted" family read rank **340** — above `a = 274`, which is
impossible for the rank of a 274-dimensional space of functions. It caught that by
inspecting the number, not from the control's verdict.

The principle it offers is right and I am adopting it: **bound a control's own
output by what is mathematically possible**, because a control that can return an
a priori impossible number is not yet a control. Its C4 failure has the same
shape — generating "generic points" as independent random `(s,u,N)` leaves `Z`
and inflated a rank to 17 against `a_∞ = 9`.

## Defects

**D4, mine:** board slot 6 says *"sharing no code with s69/s74"*, but the
reformulation's third implementation is **s79**, which the same slot lists as an
input. s79 is the module a worker is most likely to copy from and the exclusion
list should have named it.

**D1 and D2**, the dispatch message and the bundle command: sixth and fifth
sessions to report them respectively.

**D3** is the runtime asking for a session-link trailer. The session declined and
documented why, correctly: the repository's rule governs.

**My own gate, second defect of its kind.** Intake FAILED on two files for
containing a session-link URL. Both are prose explaining the rule and why the
session declined it; every commit message is clean. I had hit the identical false
positive in my own integrator note a day earlier and reworded around it. Check 9
now distinguishes a live link from a quoted placeholder ending in an ellipsis.
Fixing it introduced a second bug — the strip set included `.`, so it ate the
very ellipsis it was testing for and every placeholder still read as live — found
only because I tested both directions instead of only the rejection. Both
directions pass now, and the selftest still rejects a real link.

## Open, priced

`mult_det` at `(19,2⁷)` is a floor, so `i_det^∞ ∈ {1,2}` there; deciding needs the
upper half, which evaluation cannot supply. `a((71,19,2⁷),26) = 392` is inherited,
not checked by this instrument. `(21,2⁷)` has only `a_∞`. No exact rational
arithmetic — everything mod two primes, which is what floors require. And the
enumerator assumes `λ̄' = (col,col,1^k)`; general tails need more block
bookkeeping, priced at a fraction of a session.
