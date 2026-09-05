# Pre-registration — session 49 (foundations audit; verifier)

Branch `s49-audit`, off `eb8cecb` (main tip at clone).  Written and committed
**before any rank, Jacobian, certificate or verifier run** in this session.
Labels: **proved** / **measured** / **certified** / **adopted-from-literature**
/ **expectation**.  Directions of inference, standing: a rank modulo `p` at an
integer point is a *lower* bound on the rank over `Q` at that point, and a rank
at a point is a *lower* bound on the generic rank of the family.  A measured
full rank is therefore a proof of full rank; a measured drop is a certificate,
never a proof.

This is an audit session: no new science, no new cells.  Every measurement
below either re-derives a committed number from scratch or exercises the
verifier.  Seeds are fixed here, before any run, because §2.6 of the brief
found that no earlier session fixed its seeds in a committed artefact before
running.

## Fixed constants (all runs)

- House primes: `p1 = 2147483647`, `p2 = 2147483629`.
- Base seed: `SEED = 20260905`.  Every random object is drawn from
  `random.Random(SEED + <named offset>)` with the offset stated in the log line
  that reports the object; no other randomness.
- Ladder box `±10^6`; certificate box `±10^12`; certificate primes 62-bit,
  descending from `2^62 − 1`, first-`k` with product exceeding twice the
  Hadamard bound.
- Every run bounded by `timeout` and `ulimit -v`, pid in `results/logs/<run>.pid`.

## M1 — the two cap degrees at `(n, r) = (4, 6)` (brief §2.1)

**What is computed.**  `dim S_d`, `h_d = [t^d]((1 − t^3)/(1 − t))^6`,
`ρ_d = dim S_d − h_d`, the Gulliksen–Négård value `H_{S/J(M)}(d)` and ceiling
`dim S_d − H_{S/J(M)}(d)`, for `d = 4..9`; the rank of the degree-`d` Macaulay
matrix of the six partials at three fresh determinantal pencils and both primes
for `d = 7, 8`; and a multimodular certificate at **size 661** for `d = 7` at
three fresh pencils from `±10^12`.

**Predictions.**
- M1a (**prior 0.97**): `ρ_7 = 666`, `h_7 = 126`, `ρ_8 = 1197`, `h_8 = 90`,
  ceiling at `d = 8` is `1147`; determinantal rank `660` at `d = 7` and `1146`
  at `d = 8` at every pencil and prime.
- M1b (**prior 0.97**): at each certificate pencil `rank_p M_7 = 660` at every
  prime in the run, so every `661 × 661` minor vanishes over `Z` and
  `rank_Q M_7 = 660` exactly at that pencil (the mod-`p` value being the lower
  bound and the certificate the upper bound).
- M1c (**proved before running, from the numbers above if they reproduce**):
  the smallest usable minor is (generic determinantal rank) + 1, so the caps are
  **1148 proved** (`1147 + 1`, from the GN ceiling) and **661 certified**
  (`660 + 1`), not 1197 and 666.  Paper 1's `prop:jaccap` is *predicted* free of
  the slip because the drop there is exactly 1 (`65 = 64 + 1`); to be checked by
  reading, not by editing.

**What would count as a problem.**  Any pencil or prime returning a rank other
than the predicted one (a bug, or a wrong object); a certificate that does not
close at 661 (the Hadamard bound is smaller at 661 than at 666, so it must).

## M2 — Theorem C, density at `r = 3` for every `m` (brief §2.5)

**Claim to be proved on paper and then checked.**  At the point
`A_1 = I`, `A_2 = diag(ω, ω², …, ω^m)`, `A_3 = P` (the cyclic shift matrix
`P_{i,i+1} = 1`, indices mod `m`), with `ω` a primitive `m`-th root of unity,
the sub-permanents of `A(s) = s_1 A_1 + s_2 A_2 + s_3 A_3` are
`q_ii = ∏_{r≠i} x_r` and, for `i ≠ j`, `q_ij = s_3^{|U|−1} ∏_{r∉U} x_r` with
`U` the cyclic interval from `j` to `i`, `x_r = s_1 + ω^r s_2`; these span
`Sym^{m−1} C^3` by a `q`-binomial argument, so `dΦ_{m,3}` has full rank
`C(m+2, 2)` there and `Φ_{m,3}` is dominant for **every** `m`.

**What is computed.**  With `p` a prime `≡ 1 (mod m)` and `ω` a primitive
`m`-th root of unity mod `p`: (a) the rank of the Jacobian of `Φ_{m,3}` at that
point, computed by a generic sub-permanent routine that knows nothing of the
closed form, for `2 ≤ m ≤ 9`; (b) the window-product spanning lemma (rank of
the `m` cyclic-window products of length `j` in `Sym^j C^2`, all `1 ≤ j ≤ m−1`)
for `2 ≤ m ≤ 40`.

**Predictions.**  M2a (**prior 0.9**): rank `= C(m+2, 2)` at every `m` tested.
M2b (**prior 0.9**): window rank `= j + 1` at every `(m, j)`.  A failure at any
`m` refutes the written proof and Theorem C(iii) is restated as *proved on the
checked range, conjectural beyond*, which is the fallback the brief allows.

## M3 — the verifier over every certificate on record (brief §2.7)

**What is computed.**  `tools/verify/` is run over every certificate converted
into the declared format from `results/s42_certs/`, `results/s41_cells/`,
`results/s43_cells/` and the session-45/46/47 lift files.  Layer 1 recomputes
ranks over `Q` and two primes, minors over `Z`, nullity certificates.  Layer 2
recomputes the weight, applies every simple raising operator `E_{i,i+1}` over
`Z` (integer vectors) or modulo the recorded prime (mod-`p` vectors, reported
as such and never as integer certificates), checks `|λ| = 4δ`, variable count
`= ℓ(λ)`, degree `= δ`, and evaluates the vector at fresh points of the claimed
variety built from the recorded substitution data.

**Predictions.**  M3a (**prior 0.8**): every integer certificate passes both
layers.  M3b (**prior 0.6**): at least one certificate on record fails a
*format* check (missing substitution data, a vector recorded only in
pipeline-relative coordinates) and has to be reported as *unverifiable as
stored* rather than as *verified*; this is a finding about the record, not
about the mathematics.  M3c (**prior 0.9**): no certificate fails a semantic
check that survives re-examination.

## M4 — the degeneracy-direction test set (brief §2.9)

Three fixed points are committed under `tools/verify/testset/`: a `det_4`
pencil in six variables, a reducible `ℓ·c` with `c` a random cubic, and the
full ten-variable `x_0 · per_3`, all with integer coefficients drawn from
`random.Random(SEED + 4900)`.  As the worked example, the Macaulay corank
`dim (S/J_F)_d` is evaluated at all three for `d = 4..8`.  Prediction
(**prior 0.9**, it is Proposition D): the pad points are at least as degenerate
as the determinant at every `d ≥ 5`, i.e. the statistic points the wrong way.

## Stopping rules

1. If M1 reproduces, the two cap documents are corrected in place and the
   report records the corrected numbers.  If M1 does not reproduce, nothing is
   corrected and the discrepancy is the report.
2. M2 is written as a theorem only if the checks pass; otherwise as an
   expectation with the checked range stated.
3. The verifier is delivered whether or not every certificate passes; failures
   are listed per file with the failing check named.
4. Budget: no single run over 40 minutes wall clock; nothing over 5 MB committed.
