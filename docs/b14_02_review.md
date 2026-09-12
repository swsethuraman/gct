# Integrator review — B14-02

**Verdict: ACCEPT.** The strongest delivery of the batch so far. Every
load-bearing claim reproduced in exact integer arithmetic here, including the
orientation Astra corrected the board on. One reproducibility gap, and three
defects that matter to sessions still running.

Branch `b14-02-source13`, tip `f0e62626`, 4 commits over `9898e569`. md5 OK on
whole and `part00` (byte-identical), sha256 matches the header line, size 302316
as stated. Intake gate CLEAN. Pre-registration is the first commit.

## Verified here, in exact ℤ

| claim | my check | result |
|---|---|---|
| `rank_ℚ(A) = 36` | `fmpz_mat.rank()` on the shipped 39×96 integer matrix | **36** |
| `rank(K) = 3`, `39 = 36 + 3` | exact rank of `K` | **3**, and 36+3 = 39 |
| **`Aᵀ·K = 0`** | computed `Aᵀ·K` over ℤ: 96×3 | **every entry zero** |
| right kernel is *not* the object | `96 − 36` | **60**, as reported |
| `36×36` rank witness | recomputed the minor from the shipped rows and columns | **3770-bit determinant, nonzero, matches stored** |
| `H₁₃ = (9!)²·2¹⁵·1176¹³` | recomputed from scratch | **exact match, 185 bits; `2H₁₃` needs 186** |
| seven-prime modulus | product of the seven shipped primes | **217 bits, ratio 2.966×10⁹** |
| every entry within bound and signed range | max `|entry|` vs `H₁₃` and `mod/2` | **both hold; 0 zero entries; 79/104/124 bits as stated** |
| R7: rank still 36 over all 116 | built the 39×116 matrix and ranked it | **36** |
| the three vectors annihilate the holdout | `Hᵀ·K` over the 20 holdout points | **all zero** |

**The orientation is right, and it is worth saying why explicitly.** `Aᵀ·K = 0`
means that for every point `j`, `Σᵢ K[i][m]·A[i][j] = 0` — the combination
`Σᵢ K[i][m]·Fᵢ` vanishes at every sampled point. That is the ideal-relation
condition. Had the session computed `A·K = 0` it would have produced a
60-dimensional object and a plausible-looking number. This is the error Astra
caught in board v0.3, and slot 2 is the slot it would have cost.

## The reading is the correct one

`rank(A) = 36` gives `rank(ρ) ≥ 36`, a **floor**, so relations valid on the whole
reducible locus number **at most 3** — a **ceiling**. `k ≥ 1` is not established
and the report says so in three separate places. R6 is CONDITIONAL. `i_red(13)`
is NOT REACHED and not claimed. This is exactly the direction of inference the
programme has repeatedly got backwards, and it is got right here.

## The pre-registered expectation was wrong, and the session is better for it

E1 predicted rank 39 with high confidence and measured 36. The report diagnoses
its own error precisely: s74's `birth_profile` records independence at **generic**
points, and this slot evaluates on the **reducible** locus, where a drop is the
thing `i_red` names. Then C7 discriminates instrument fault from geometry — same
rows, same evaluator, same arithmetic, 41 generic points, **rank 39**. A broken
climb, a wrong exponent or an `exps` slip would have depressed the generic rank
too.

**Gap: the generic-point matrix is not shipped.** `direction_control.json`
carries `{n_points: 41, rank: 39}` and a verdict string, but not the entries, so
C7 is the one load-bearing claim in this delivery I could not recompute — and it
is the control the whole "instrument exonerated" reading rests on. Every other
matrix shipped. Not a rejection: the claim is consistent with everything else and
the 39×96 and 39×20 matrices I *can* check behave exactly as described. But slot
7 should ship its generic-point matrix, and I will ask B14-02 for this one if it
is still resumable.

## Defects, all four confirmed, and two are urgent for running sessions

- **D2 — `P13.json` ships six primes and says `signed_uniqueness_verified: true`.**
  Confirmed: six primes, 186-bit modulus, **1.381×** headroom, against `P14.json`'s
  seven primes, 217 bits, 2.522×10⁶. Board §1 requires seven at degree 13. A
  session reading the pinned contract file alone would use six and believe
  uniqueness verified. **I am not amending `P13.json` while sessions run** — it is
  pinned by blob id `76e1f2ed…` in the board and both B14-01 and B14-02 verified
  against that blob; changing it mid-batch would break the contract it exists to
  provide. Recorded for the batch close instead, and it goes in the next dispatch
  note.
- **D3 — `source.json`'s `literal` is climbed to degree 24.** Confirmed from the
  file's own `row_system` field: `F_{T_i}(f)·msym_u(f)^(24 − d_i)`, and entry[0]
  at rung 12 carries `exponent = 12`. Slot 2 needed 13, **slot 7 needs 14**, and
  neither slot's text warns that the field named `literal` is right for neither.
  This session recomputed the climb from `native` and used `literal` nowhere, and
  its C2 control tested exactly this: exponent `13−d` gives 8/8 identities, `24−d`
  gives 8/8 differing. **Slot 7 is still running and this is the trap most likely
  to cost it silently** — a degree-24 row against an inherited degree-13 bound is
  a bound violation that reconstructs to a wrong integer without complaint.
- **D4 — "the full 39 × 96" does not say *which* 96.** Fair. `P13.json` holds 116.
  The holdout turned out to be the most useful control available, and a session
  that built 39×116 would have had no out-of-sample check left.
- **D5 — the packet's bundle command.** Third session in a row to report it;
  confirmed again. Already corrected in the launch messages.
- **D1 — no dispatch message arrived.** Second session to report it. Its
  recommendation is good and I am taking it: a committed
  `results/b14_prep/dispatch.json` has no self-reference problem, because it is
  not the board and not the packet.

## Controls

The two vacuous controls the session caught in its own work are the most valuable
part of §6, and both are recorded rather than quietly repaired:

- the first must-fail test perturbed a symbol the sampled fillings never use, so
  it "detected" a corruption that was not there. Replaced by a perturbation chosen
  by requiring the definition's own value to move.
- **`flipbits` is a genuine symmetry at even `n2`**, not a bug: flipping every
  2-column bit is the relabelling `s → ~s`, multiplying the sum by `(−1)^{n2}`. A
  battery of only even-`n2` shapes would report an undetectable sabotage mode as a
  passing check. Three odd-`n2` nonzero shapes had to be searched for. The 39 rows
  here have `n2 = 15`, odd, so the mode is live on the real data.

Also banked: `fast_eval_c` is **49.5 s/entry against the DP's 65.5 ms**, a factor
of 756. Spot-check tool only.

## For slot 7, now

- transport exponent is `14 − d`, **not** `source.json`'s `literal` (D3)
- `P14.json` already ships seven primes; the degree-14 bound is 195 bits and the
  headroom 2.522×10⁶ — this session derived both independently and they agree with
  the board's own figures from the other end
- **the seven-hour figure should not be used for planning**: 78 ms/entry measured,
  `93 × 192 × 7 = 124,992` entries, **2.7 core-hours ≈ 1.4 h on two cores**
- ship the generic-point matrix, not just its rank
