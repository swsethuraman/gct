# Integrator review — B14-04

**Verdict: ACCEPT.** This is the slot the `D ≤ −2` chain rests on, so I derived
the mathematics myself rather than replaying theirs. Everything reproduces.

Branch `b14-04-astra`, head `27be12c0`, 2 commits over `9898e569`. Model
**gpt-6-astra**. sha256 and md5 both match the manifest, size 282438 as declared.
Intake CLEAN. Pre-registration is the first commit. Shared-file edits limited to
`docs/PROVED.md` and its own `PREREG`.

## Reproduced here, from my own derivation

I did not use their formula. Starting from
`Sym(Sym²V′ ⊕ Sym³V′ ⊕ Sym⁴V′)`, whose graded Frobenius characteristic is
`F(t) = ∏_j Σ_d h_d[h_j] t^{jd} = exp(L)` with
`L = Σ_j Σ_r (1/r)·p_r[h_j]·t^{jr}` and `p_r[h_j] = Σ_{σ⊢j} p_{r·σ}/z_σ`,
I built `F_N` to `N = 35` in exact rationals.

| check | result |
|---|---|
| my coefficient set vs theirs, degree 31 | 3522 classes, **0 only-mine, 0 only-theirs, 0 differing** |
| degree 33 | 5126 classes, **0 / 0 / 0** |
| degree 35 | 7365 classes, **0 / 0 / 0** |
| my own Murnaghan–Nakayama (recursive rim-hook removal, no beta numbers, nothing imported), 120 sampled characters | **all agree** |
| `⟨F₃₁, s₍₁₇,₂⁷₎⟩` with only my numbers | **274** |
| `⟨F₃₃, s₍₁₉,₂⁷₎⟩` | **392** |
| `⟨F₃₅, s₍₂₁,₂⁷₎⟩` | **533** |
| their identity-cycle dimensions vs an independent set-partition count | **exact** at all three degrees |

That last row is worth naming: the number of partitions of `N` labelled
positions into blocks of sizes 2, 3 and 4 is 113215155877486062400000,
13867871310296842558720000 and 1844517852226181623941450000 at `N = 31, 33, 35`
— matching their reported identity-cycle values, from a construction that shares
nothing with the symmetric-function route.

**392 and 533 had one lineage this morning** — the scratch stable-slice counter,
which the scratch manifest's caveat 3 flagged as single-route. They now have
three, one of them mine. Caveat 3 is discharged.

## 73 and 159, and a lineage nuance the report glosses

Three implementations now agree channel by channel at both degrees, and I
checked B14-04's channels against both banked routes directly. But the report
says its recounts give 73/159 "a method independent of the scratch Weyl
counter", which is true and slightly less than it sounds:

- **Weyl alternation** (B13-01) — independent
- **power-sum plethysm via the banked `pleth_p` beta-number MN routine** — used
  by the Astra pilot *and* by B14-04's producer. **One lineage used twice, not
  two.**
- **B14-04's verifier** — separate Newton recurrence, border-strip characters,
  no beta numbers. Genuinely new.

So three distinct implementations, not four, and the producer is not one of the
new ones. The report is accurate about its verifier; a reader skimming the
headline could over-count. `lmr_D_upper` now states it the careful way.

## Scope, stated correctly

The report is disciplined about what dimensions do not buy: "proving a target
dimension does not prove that the source image fills it", the stable 533 "does
not by itself certify the finite rung-28 ambient value or an exact first
stabilization degree", and `D ∈ [−4, +1]` on the dimensions alone. All correct
— the interval narrowed for reasons this slot did not supply, and it was right
not to reach for it.

The resource controls are the right shape: a 128 MiB request under a 64 MiB cap
raises MemoryError, and a three-second wait is stopped at ~0.42 s under a 0.4 s
limit. Deliberately failed controls, labelled as such.

## Defects

**PROVED.md section collision.** B14-03 and B14-04 both appended a section "F".
Resolved here — B14-03 keeps F, B14-04 becomes G. This will recur: every Astra
slot appends a section and each picks the next free letter against the frozen
base, which cannot see the others. Integration's problem, not theirs, but the
remaining slots should expect their letter to be renumbered.

**Manifest `prerequisites` field is garbled.** It reads
`"-9898e569… A packet cannot contain its own commit's hash either — the third
time this shape has bitten"` — `git bundle verify` output with the base commit's
*subject line* captured alongside the hash. Harmless to a human, wrong for
anything parsing that field. (The base itself is correct everywhere else.)

**Fourth session to report the packet's bundle and checkout examples.** Its
launch brief governed correctly and the named-ref form was used.
