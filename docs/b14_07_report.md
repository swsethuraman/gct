# B14-07 — exact degree-14 source matrix at `P14`

**Delivery: one part (`part00`); the bundle needed no split.** Branch
`b14-07-deg14-source`, cut against `batch14-base`.

**Model that actually ran this session: `claude-opus-5` (Claude Opus 5).** The
packet names "Claude"; this is the serving configuration, recorded per the
packet's own instruction and board §5.

**Base, resolved not inherited.** Tag object
`4bda8a12433c5965a5df82fef35b4c7220b76756`; **commit
`9898e56941a7665f231873481dae956f08509995`**; **tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f`**.

**Host resources, declared.** One container: **2 cores, 7 GB RAM, ~30 GB disk.**
Twelve sessions do not imply twelve independent budgets; if the other five flint
slots are sized against this class they are sharing it.

---

## 1. Result

**CERTIFIED — the exact degree-14 source matrix and its exact rational left
kernel.**

| quantity | value | label |
|---|---|---|
| `A14` | `93 × 192` exact **signed integer** matrix (+ 20 holdout columns computed separately) | **CERTIFIED** |
| `rank_ℚ(A14)` on the 192 primary columns | **88** | **CERTIFIED** |
| `k = dim` **left** kernel `= 93 − rank_ℚ` | **5** | **CERTIFIED** |
| `A14ᵀ · K14 = 0` over ℤ | verified, exactly | **CERTIFIED** |
| `rank(K14)` | **5** | **CERTIFIED** |
| `rank_p(A14)` at all seven primes | **88** at every one | **MEASURED** |
| `u(P_j) ≠ 0` | at all 212 points and all 7 primes | **MEASURED** |

`K14` is delivered as five primitive integer vectors of length 93 in
`results/b14_07/K14.json`; largest entry `7.759 × 10²²`.

**What this is not.** It is a **source-matrix** result. It is **not**
`i_red(14)`, and it is not labelled as such anywhere in this delivery. It becomes
an ideal kernel only after the degree-14 target certificate (slot 1's stretch),
the recount (slot 4) and the interpolation check (slot 3) all pass. Per
`PROVED.md: evaluation_cannot_certify_i_ge_1` and `rank_floor`, nothing here
establishes `i ≥ 1` for anything.

**Orientation, stated because the board records two sessions getting it
backwards.** Source vectors are ROWS, points are COLUMNS, so relations live in
the **LEFT** kernel: `Σᵢcᵢ Fᵢ` is a candidate relation iff `cᵀA14 = 0`. The right
kernel `A14·K = 0` has dimension ≥ 99 here and is not the object wanted.

## 2. The height bound, re-derived

The board said re-derive rather than inherit, so:

From the Leibniz form (`wk11_s69_circuit.brute_force_eval`), `F_T` is a signed sum
of `2^{n2}·(h!)²` terms, each a product of `d` symbols, so

    |F_T(f)| ≤ 2^{n2} · (h!)² · M^d,     M = max_α |α! · c_α(f)|.

With `f = ℓ·c`, all coefficients in `[−7,7]`, and `|α| = 4` having `k` distinct
indices with parts `aᵢ`: `c_α(f) = Σ_{i:αᵢ≥1} ℓᵢ c_{α−eᵢ}`, so
`|m_α| ≤ (∏aᵢ!)·k·49`. Over the partitions of 4 that is maximised at `α = (4,0,…)`:
`24·1·49 = 1176`, against 588, 392, 294, 196 for the others. Hence

    H₁₄ = 2¹⁵·(9!)²·1176¹⁴ = 41752117405971316170471859365816782308304944383288095539200

195 bits; `2H₁₄` 196 bits; the seven-prime product 217 bits; margin
**2.522 × 10⁶**. **This equals the delivered `source_value_bound` exactly.** I
record that as *confirmation by the same route* — the derivation in `P14.json`
names the same factors — and therefore **not** method diversity. If the programme
wants the bound itself double-sourced, that is a different derivation, not a
re-run of this one.

**MEASURED, and useful for pricing rung 15+:** the largest entry actually
occurring is `1.2748 × 10⁴⁰` — **134 bits against a 195-bit bound**, a factor of
`3.05 × 10⁻¹⁹`. The gap is intrinsic, not a benign point set: the bound assumes
all `2¹⁵·(9!)²` terms (≈52 bits of prefactor) attain the maximum and add
constructively, whereas the sum is alternating and cancels. **Five primes would
have sufficed a posteriori** (155 bits > 135). That is *not* a licence to use
five: the a priori bound is what makes signed reconstruction valid, and an
observed maximum cannot retroactively license a modulus. It is, however, a real
datum for anyone deriving a *sharper* a priori bound before costing degree 15 or
16 — where seven primes will stop being enough long before the true entries
demand it.

## 3. Timings — the memo's figure is replaced by a measurement

| item | measured on this host |
|---|---|
| `fast_eval_c` (s69 Identity 3 circuit) | **41 s** per evaluation |
| `dp_eval_compact` (s74 compact-state DP) | **0.056 s** per evaluation |
| full matrix, 93 × 212 × 7 primes = 136,332 evaluations | **3,402 s (57 min)**, 2 processes, 2.22–2.80 s per point |
| signed 7-prime CRT over 19,716 entries | 0.2 s |
| `rank_ℚ` of the 93 × 192 integer matrix | 3.6 s |
| exact-integer Identity-3 evaluator (C6) | ≈ **14 min per entry** |

**The memo's "indicative seven hours across seven primes" is not validated and is
not adopted.** The real figure on a 2-core container is under one hour. The whole
margin is the evaluator: the DP is **730×** faster than the circuit, and a session
that reached for `fast_eval_c` would have needed ~63 hours and would have
delivered a prefix. Slot 2 should expect the same ratio at degree 13.

## 4. Controls — every one run twice, and one of mine was void

Each control has a true arm and a deliberately-wrong arm that **must** fail. Both
outcomes are in `results/b14_07/controls.json`.

| id | control | true arm | failure arm |
|---|---|---|---|
| **C1** | compact DP vs banked `rows_native` (`results/s74/columns_red_2147483647.json`), all 93 rows × 4 of s74's own red points | **372/372 exact**, and **372/372 nonzero** | two letters swapped in a tall column → detected |
| **C2** | row-system identity at degree 14: literal filling climbed to 14 == native × `u^(14−d_i)` | 5/5 | transport exponent `13−d_i` → detected |
| **C3** | **independent algorithm**: Identity 3 (`fast_eval_c`) vs the compact DP | 2/2, both values nonzero | (a) perturb a symbol the filling provably reads → detected; (b) every symbol doubled (wrong tensor normalisation) → detected |
| **C4** | `u(P_j) ≠ 0` at every point, every prime | 0 u-zeros in 212 × 7 | a point with `ℓ₁ = 0` forces `u = 0` → detected |
| **C5** | signed CRT round trip | exact on `\|x\| ≤ H₁₄` incl. `±H₁₄` | an integer of size `M−1` wraps → detected |
| **C6** | **exact integer** evaluator, no modulus at all | **3/3 exact**, one entry per rung (12, 13, 14), incl. a negative value | reconstructed entry altered by 1 → detected |
| **C7** | primality of all seven CRT primes, re-verified in-house (Miller–Rabin, bases 2..37) | 7/7 | — |
| **C8** | **holdout**: `K14` must annihilate the 20 columns it was not fitted on | **annihilates all 20, exactly** | a random vector must not → detected |
| **C9** | `negative_control_forced`: a point of span 3 `< ℓ(λ) = 9` must read zero on every row | **all 93 rows read 0** | a generic full-span point reads nonzero → detected |

**Free control that could have failed and didn't.** My own reconstruction of
`f = ℓ·c` from `P14.json` independently reproduces both the declared `u_symbol`
and the declared `max_abs_quartic_symbol` for **all 212 points**. Had the point
contract's coefficient convention been anything other than "plain coefficients,
`cubic_exponents` give the order", this would have tripped on point 0.

### 4.1 C3 was void as I first wrote it — the eighth instance

`PROVED.md: check_must_be_able_to_fail` lists six instances in batch 13 and the
board adds a seventh (the integrator's empty-census reachability script). **Here
is an eighth, and it is mine.** My first C3 failure arm incremented symbol index
7. That filling never reads index 7, so the corrupted input produced a bit-
identical value and the arm reported "no discrepancy" — a control that could not
fail, exactly the shape the board warns about, written by someone who had just
read the warning.

Fixed two ways rather than one: the arm now perturbs an index the filling
**provably does** read (obtained by passing the identity list as the symbol vector
and reading back which indices `letter_tensors` returns), and a second arm doubles
every symbol, which must scale `F_T` by `2^d`. Both now fail.

**A second defect of the same class, caught by inspection rather than by running
it:** C1 and C3 compared values for equality without checking they were not both
zero. Two evaluators agreeing on 0 is not agreement, and `C9` proves that whole
families of points make every row vanish. Both controls now record the nonzero
count; C1's is 372 of 372.

### 4.2 C6 is what makes the word "exact" load-bearing

Everything else in this delivery is modular arithmetic plus a reconstruction
argument. C6 is the only step that leaves the modular world entirely: Identity 3
carried out over ℤ with no modulus anywhere, integer determinants throughout, on
a filling and a point taken from the real input. It reproduces the CRT-
reconstructed integer **digit for digit** at all three entries:

| entry | rung | value |
|---|---|---|
| row 0, `P14-000` | 12 | `2987150143434821999318203681996800` |
| row 2, `P14-001` | 13 | `46899756296168423620687776621527040` |
| row 92, `P14-002` | 14 | `−4355584619767984529907311522193408` |

The third is negative, so the signed lift through the 217-bit modulus is exercised
and not merely the positive branch. This is what the board means by "a small exact
integer evaluator independent of the fast modular path"; the board also says a
fresh modular check alone would not do, and I have not counted one as if it would.

**C8 is the control I would keep if I could keep only one.** The kernel is
computed on 192 columns and then tested against 20 columns it never saw. A
left-kernel vector that failed there would be an artefact of the point set rather
than a candidate relation, and nothing else in this slot would have revealed it.
All five vectors annihilate all 20 held-out columns exactly.

## 5. Exploratory — not pre-registered, and labelled as such

Reported because it is exact and free, not because it was asked for.

| quantity, all on `P14`'s 192 primary columns, all exact over ℚ | value |
|---|---|
| the 39 rows born by degree ≤ 13: rank | 36 |
| the 39 rows born by degree ≤ 13: left nullity | **3** |
| all 93 rows: rank | 88 |
| all 93 rows: left nullity | **5** |
| `dim(K14 ∩ {vectors supported on the 39 degree-≤13 rows})` | **3** |
| independent relations first appearing at rung 14 | **2** |

Three of the five kernel vectors are supported entirely inside the first 39 rows;
the other two have support 87 and 89. So the kernel splits exactly `3 + 2` along
the rung boundary.

**Two things this is not.** It is **not** slot 2's object: slot 2 computes a
`39 × 96` matrix at `P13` with transport exponent `13 − d_i`, whereas this is a
row sub-block of a degree-14 matrix at `P14`. Different matrix, different points,
different transport. And it is **not** a verification of Lemma T — Lemma T is a
statement about multiplication being injective on ideals, and this is a nullity of
a sampled evaluation matrix. It is consistent with the sampled ladder profile in
`results/s74/ladder_ranks.json` (`i_red = 3` at δ=13, `5` at δ=14) and it is now
exact rather than modular, which is the only new thing in it.

## 6. What I did not do, priced

| not reached | why | price to finish |
|---|---|---|
| **C6 on more than three entries** | the exact-integer Identity-3 evaluator costs 310–503 s per entry; the matrix has 19,716 | the three covered are `(row 0, P14-000)` rung 12, `(row 2, P14-001)` rung 13, `(row 92, P14-002)` rung 14 — one per rung, and the rung-14 one is negative, so the signed lift is exercised. All of it is ≈2,300 CPU-hours. A *statistically* useful sample — 40 entries spread over rungs and points — is ≈4.6 CPU-hours and is the sensible next increment. |
| a **second derivation** of `H₁₄` | mine reaches the delivered number by the delivered route, so the bound is single-lineage even though it is now twice-computed | a genuinely different bound — e.g. through the `α!` normalisation and a Cauchy–Schwarz or Hadamard argument on the tall-column determinants rather than term-counting — is a few hours of paper work and would likely be *much* sharper than 195 bits, given §2's measured 134 |
| `i_red(14)` | not this slot: needs slot 1's degree-14 target minor, slot 4's recount of 159, slot 3's verifier | unchanged by this delivery except that the source half is now exact |
| the **degree-15** source block | out of scope | the 145-row block would cost ≈1.6× this one on the same host (52 more rows, one more transport step); the binding constraint will be the height bound, not the evaluator — at degree 15, `H₁₅` is 205 bits and seven primes give 217, a margin of only ~6×10³ |
| anything about `D` | `D = −4` needs slot 1's stretch; if that does not land, `D = −4` is not reached and this matrix does not supply it | — |

## 7. Defects in the assignment

The packet asked for these.

**D1 — the packet's own base rule cannot be satisfied as written.** The packet
says "Your dispatch message states the expected commit and tree… They are
deliberately not written into this file." **No dispatch message accompanied this
packet**, so there was no value to check the tag against and the cross-check the
rule exists to provide was unavailable. I recovered it another way — `git
ls-remote` peels the tag server-side and prints `refs/tags/batch14-base^{}`, which
agrees with the local `git log -1 --format=%H` — and that is a genuinely
independent second peel, so the base here is as well-attested as the rule
intended. But the mechanism the packet specified did not exist. The rule that a
packet cannot name its own commit is right; the conclusion that the value can
therefore live in a dispatch message only works if the dispatch message is
actually sent. **Suggestion: put the expected commit and tree in the tag
annotation** — the tag is already the name, the annotation is not part of the
commit it names, and `git cat-file -p batch14-base` is one command. The annotation
currently explains how to resolve the tag but does not state the tree.

**D2 — the delivery command in the packet produces a bundle that fails the
packet's own gate.** The packet says:

    git bundle create b14_07_<name>.bundle batch14-base..HEAD

That writes a bundle carrying **only `HEAD`**. `tools/delivery/check_delivery.py`
check 5 exists precisely to catch this ("HEAD-only bundles (a fetch by branch name
then fails)" — named in the tool's own docstring as one of batch 13's four
recurring defects), and board §5 says "Bundle carries the named ref". So a session
following the packet literally, then running the gate the packet also mandates,
gets a DEFECT. The command that satisfies both is the one the checker prints:

    git bundle create <file> batch14-base..<branch> <branch>

I used that. Note this is the *fourth* time the delivery instruction on this batch
has been wrong, after the three the packet itself confesses to.

**D3 — no clone.** This session started with no repository at all. The packet
anticipates only "your clone predates the freeze" and says to stop. Stopping would
have been wrong: the base was obtainable. The user's laptop clone is fully packed
and its 183 MB main pack would not cross the device bridge, so I cloned
`https://github.com/swsethuraman/gct.git`, which carries `batch14-base` as an
annotated tag resolving to the identical object. **Recorded for the other eleven
sessions: the bridge cannot move this repository; the remote can.**

**D4 — the packet's `n_chi` paragraph is not applicable to this slot and cost
reading time.** The `n_χ`, `N_S/|Stab|`, `matmul_mod_wide` and
`certificate_ceiling` material is load-bearing for slots 9 and 12 and has no
bearing on a 93 × 192 dense exact matrix. Same for the `values_are` rule, which I
followed, and the two-`exps`-orderings rule, which I did need. Not a wrong
statement — a preamble that does not distinguish per-slot relevance, which is a
real cost at twelve sessions.

**D5 — one figure in the packet is stated as fact and is a ceiling.** "At LMR
`a = 274`, `m_det = 273` exactly and `m_pad >= 269`, so `D` lies in `[−4, +1]`."
Correct as written. But the packet then says the batch's best outcome is
"`i_red(14) = 5`, giving `D_LMR = −4` exactly". My exact `k = 5` is a nullity of a
**sampled** matrix and is therefore a **ceiling** on `i_red(14)`; making it an
exact value is what Lemma CI's four conditions are for, and three of them are
other slots' deliverables. The packet's §"two objectives" is careful about this;
the board's §7 item 2 is less so. Worth one clause.

## 8. Reproduction

```
python3 analysis/b14_07_source14.py --all --procs 2        # 57 min, 7 primes
python3 analysis/b14_07_kernel.py                          # CRT, bound check, exact kernel
python3 analysis/b14_07_controls.py --controls C1,C2,C3,C5,C9
python3 analysis/b14_07_controls.py --controls C6 --entries 3   # ~45 min
```

Runs were bounded at launch with `timeout` and `ulimit -v`; pids in
`results/logs/*.pid`; none needed ending early.

Artefacts, all under 5 MB:

| file | what |
|---|---|
| `results/PREREG_b14_07.md` | pre-registration, committed before any entry was computed |
| `results/b14_07/A14_mod_<p>.json` × 7 | per-prime native values and `u`, each with `values_are` |
| `results/b14_07/A14_exact.json.gz` | the exact signed integer matrix, 93 × 212 |
| `results/b14_07/K14.json` | rank, `k`, the five primitive kernel vectors, every verification flag |
| `results/b14_07/controls.json` | every control, both arms |
| `results/logs/b14_07_*.log`, `*.pid` | run logs and pids |

`values_are` on every stored matrix reads: *literal transported fillings at degree
14, `A[i][j] = F_native_i(f_j)·u(f_j)^(14−d_i)`, `u = 4![s₁⁴]f`; NOT u-normalised
(the u-normalised vector is this divided by `24^(14−d_i)`)*.

The `u`-letter index is resolved by `exps(4,9).index((4,0,…,0))` → **494**, never
by a literal; `exps(4,9)[0] = (0,…,0,4)`, confirming `wk8_s30_core.exps` runs the
first exponent **up** from 0.
