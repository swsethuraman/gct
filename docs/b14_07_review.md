# Integrator review — B14-07

**Verdict: ACCEPT.** The degree-14 source half is now exact, and its kernel
independently confirms B14-02's relation space — the number `lmr_D_upper` rests
on — from a different matrix at different points with a different transport.

Branch `b14-07-deg14-source`, tip `4e4c56f4`, 5 commits over `9898e569`. Both
digests in the sidecar correct, size 1147400, intake CLEAN, pre-registration
first.

## Verified here in exact ℤ

| claim | result |
|---|---|
| `rank_ℚ(A14)` on 192 primary columns | **88** |
| `k = 93 − rank` | **5** |
| `rank(K14)` | **5** |
| **`A14ᵀ·K14 = 0`** | **all 192×5 entries zero** |
| C8 holdout: `K14` annihilates the 20 unfitted columns | **all zero** |
| `H₁₄ = 2¹⁵·(9!)²·1176¹⁴` | recomputed to the reported integer, **195 bits** |
| largest actual entry | **134 bits**, ratio `3.05×10⁻¹⁹` |
| rank at all seven primes | **88** at every one |
| `u`-zeros in 212 × 7 | **none** |

## Its kernel confirms B14-02's 3-space

The five kernel vectors have supports **36, 37, 37, 87, 89**. The three supported
inside the 39 degree-≤13 rows span **exactly B14-02's 3-space** — union rank 3,
checked here over ℚ.

Two sessions, two different matrices — `39 × 96` at `P13` with transport `13 − d`
versus `93 × 212` at `P14` with transport `14 − d` — the same relation space,
neither knowing the other's answer. That is precisely what a genuine degree-13
relation must do: multiplication by `u` sends `F^{up13}` to `F^{up14}`, so the
same coefficient vector is a relation at both rungs. It corroborates the
`i_red(13) = 3` that `lmr_D_upper` rests on, and the entry now records it.

## `D = −4` does not follow, and the session is right not to reach

Lemma CI at rung 14 needs **159** exhibited members of `N₁₄`. This slot supplies
pullbacks of its 93 source rows, spanning rank **88**. The shortfall is **71**, and
only mixed brackets close it — slot 1's degree-14 stretch produced none. So `k = 5`
stays a **ceiling** on `i_red(14)` and `D` remains in `[−4, −2]`.

The rung-13 trick does not repeat: there, 72 mixed members plus one source
pullback made exactly `73 = dim N₁₃`. At rung 14 the gap is 71, not 1.

## Timing: the memo's figure is replaced by a fact

**57 minutes** on two cores for 136,332 evaluations, against the memo's
"indicative seven hours". The whole margin is the evaluator: the compact DP is
**730×** faster than the s69 circuit, and a session reaching for `fast_eval_c`
would have needed ~63 hours and delivered a prefix. That matches B14-02's
independent **756×** at degree 13 — two sessions, same ratio, different degrees.

Its measured 134-bit maximum against a 195-bit bound is a real datum for
degree 15+: it notes that five primes would have sufficed *a posteriori* and then
refuses to draw the licence, because an observed maximum cannot retroactively
justify a modulus. Correct, and the right instinct.

## Its eighth instance is its own

C3's first failure arm perturbed symbol index 7 — which that filling never reads
— so the corrupted input produced a bit-identical value and the arm reported "no
discrepancy". Fixed two ways: perturbing an index the filling *provably* reads,
and doubling every symbol so `F_T` must scale by `2^d`.

It also caught, by inspection rather than by running it, that C1 and C3 compared
values for equality **without checking they were not both zero** — and its own C9
proves whole families of points make every row vanish. Both now record nonzero
counts: C1's is 372 of 372.

C6 is what makes "exact" load-bearing: Identity 3 over ℤ with no modulus
anywhere, reproducing the CRT integer digit for digit at three entries, one per
rung, the rung-14 one negative so the signed lift is exercised.

## Defects, and one I am adopting

**D1 is the right fix and I am taking it — for batch 15, not now.** Put the
expected commit and tree in the **tag annotation**: the tag is already the name,
the annotation is not part of the commit it names, and one command reads it. That
removes the dispatch-message dependency **seven sessions have now reported
missing**. I am *not* re-annotating `batch14-base` mid-batch: a re-annotated tag
is a new tag object, and the running sessions recorded `4bda8a12`.

**D3, worth passing to the remaining five:** this session started with no
repository. The laptop clone's 183 MB pack would not cross the device bridge;
cloning the remote worked. The packet anticipates only "your clone predates the
freeze" and says to stop — stopping would have been wrong.

**D4 is fair.** The packet's `n_χ` / `matmul_mod_wide` / `certificate_ceiling`
material is load-bearing for slots 9 and 12 and irrelevant to a dense exact
matrix. A preamble that does not distinguish per-slot relevance costs reading
time twelve times over.

**D5 is fair and lands on my board text.** Board §7 item 2 calls the best outcome
"`i_red(14) = 5`, giving `D_LMR = −4` exactly", which reads as though the nullity
were the value. The packet's own "two objectives" section is careful; §7 is not.

**Minor:** the sidecar puts an md5 line and a sha256 line in one `.md5` file, so
`md5sum -c` warns on line 2. Both values are right and both verify. B14-04 and
B14-05 shipped separate files, which is the better shape.
