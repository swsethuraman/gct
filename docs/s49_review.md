# Integrator review — session 49

**Accepted, with one correction to apply at merge.**  Every item was verified by
an independent route before this was written.

## 1. Reproduced

**Cap arithmetic (2.1).**  Rebuilt from `h_d = [t^d](1+t+t^2)^6` and
`dim Sym^d C^6`: `792 / 126 / 666 / 120 / 672` at `d = 7` and
`1287 / 90 / 1197 / 140 / 1147` at `d = 8`, every entry matching the report's
table.  The corrected logic — usable minor is `(determinantal rank) + 1`, not
`ρ_d` — gives **661 certified** (rank 660 at `d = 7`) and **1148 proved** (GN
ceiling 1147 at `d = 8`).  The paper-1 check is right: `prop:jaccap` takes
`65 = 64 + 1` because the five-row drop is exactly one, so the slip was specific
to the six-row case where the drop is `C(6,5) = 6`.

**The window lemma (2.5, Theorem C).**  The proof is correct.
`e_k(1, ω, …, ω^{j−1}) = ω^{k(k−1)/2}·[j,k]_ω` is the Cauchy `q`-binomial
theorem; the product formula for `[j,k]_q` is a polynomial identity and may be
evaluated at `q = ω` because no denominator `1 − ω^t` vanishes for
`t ≤ j ≤ m − 1`; the `j + 1 ≤ m` eigenvalues `ω^k` are distinct; and the orbit
of a vector under a diagonalisable operator with distinct eigenvalues spans the
eigenlines it meets (Vandermonde).  Spot-checked beyond the session's `m ≤ 40`
at `m = 41, 61, 97`: every window product has all `j + 1` coefficients nonzero
for every `j < m`.  **`r = 3` density is now proved for all `m`**, and Theorem
C's "finitely many evaluations" gap is closed.

**The verifier (2.7).**  `selftest.py` passes six cases including three
negatives.  I then ran my own adversarial test on a real committed certificate
(`10_8_7_1_1_1_d7_int`, 16,344 terms):

| corruption | expected | got |
|---|---|---|
| none | PASS | **PASS** |
| one coefficient `+1` | FAIL | **FAIL** |
| `λ → (9,9,7,1,1,1)`, same size | FAIL | **FAIL** |
| `δ → 8` | FAIL | **FAIL** |
| vector unchanged, claim "vanishes on det pencils" | FAIL | **FAIL** |
| vector unchanged, claim "nonzero on padded permanent" | FAIL | **FAIL** |

The last two are the ones that matter: a **correct vector with a wrong claim**
about what it certifies, which is our recorded failure mode, and the semantic
layer catches both.  The format's decision to rebuild evaluation points from
substitution data rather than accept bare coefficients is what makes that
possible.  50/50 committed certificates PASS.

**Provenance (2.6).**  Honest: protocols were pre-registered
(`2e06e3f`, `902cccd`), concrete seeds were committed with results
(`e50575a`, `ddb76cd`).  Not a p-hacking risk given the drop reproduces at every
seed and prime and is certified over `Q`, and fixed going forward by banking seed
`20260905` before any run.  Stated exactly at the strength it deserves.

**Process.**  No single-writer file touched.  No new blob over 5 MB (largest
3.5 MB; the 4.97 MB `(15,9,9,1,1,1)` certificate correctly kept out).  Zero
session links in five commit messages.  The worker refused a mid-session
attribution reminder asking for a session-link trailer, citing the standing
constraint — **that refusal was correct**.

## 2. The correction

The brief's §2.8 asked for the removal of "onset ≥ 10" **and any lower bracket
on the onset**.  The report handles the first correctly — the only `≥ 10` in the
repository is the `r = 4` statement, which is exhaustive per degree and stays.
But it then writes the corrected six-row bracket as

    9 ≤ onset I(D_6^{det_4}) ≤ 661

in `docs/s49_report.md` line 37 and `docs/sixrow_cap_closed.md` line 11, and
**`≥ 9` is not earned.**  `results/sixrow_record.md` says so in terms: "not a
statement about the degrees themselves — the balanced corner at `δ = 8, 9` and
every `λ_1 < δ` cell above `n_χ ≈ 3·10^5` remain unmeasured"; and
`(9,8,5,2,2,2)_7` was not reached.  The measured set is not exhaustive at any
degree `≥ 7`, so no lower bracket above the trivial one is established.

The source is `docs/s44_review.md` line 6, which I wrote.  The audit verified
everything the brief pointed it at and inherited the one claim that came from
the integrator.  That is the shared-spec failure class from our own list, and it
is worth recording as an instance.

**Fix at merge**, three files: strike `9 ≤` and restate as "`≤ 661` certified,
`≤ 1148` proved; `mult_det = a` at all 193 measured cells through `δ = 9`, with
the measured set not exhaustive at any degree `≥ 7`".

## 3. Flags acknowledged

- `docs/s43_review.md` never existed.  My error in the brief and the batch
  sheet; the withdrawal it pointed at was done in the record.  Dangling
  reference, nothing lost.
- The three `results/s36_cells/*.txt` blobs (12–13 MB) are already on the
  post-batch rewrite list; the worker was right not to touch another session's
  data.
- `docs/longweight_hunt.md` — a pre-existing filename carrying a §4 word.  Not
  the worker's doing; add a rename to the rewrite list.

## 4. Where this leaves the batch

s49 was gating: nothing else was trusted until it passed.  It passes.  The
verifier is real, adversarially tested, and every session from here delivers
certificates in `gct-cert/1`.  s50's `results/s50_controls.json` should be the
first thing converted and run through it.
