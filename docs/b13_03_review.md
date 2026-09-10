# B13-03 review — exact reducible membership

board_numbering: batch13
session_id: B13-03
model recorded by the session: `gpt-6-astra`, reasoning effort `xhigh`
bundle: `b13_03_exact_reducible_membership.bundle`
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `3fbe1ebc659b2d74f2e5b1761df34c3ec787f691` (`refs/heads/b13-03`)
status claimed: **success — complete exact control and reusable algorithm**
integrator verdict: **accept the delivery; merge pending the deferred verification pass**

This review is a stock-take, not the verification pass. Per instruction the
arithmetic here is limited to checks that cost nothing: checksums, the bundle
diff, and closed-form dimension counts. Every rank, kernel and membership
claim below is recorded as *delivered*, not as *verified*.

---

## 1. What was checked here (zero-cost)

| check | result |
|---|---|
| md5 of bundle | `f32c492e4db666b118caf4a54361c242` — matches delivered |
| sha256 of bundle | `c27f3600…a002e86` — matches delivered |
| `part00` vs whole | **byte-identical** (`cmp` clean); the split was a no-op at 103,593 B |
| declared base | `0049511` — equals `origin/main` and my local tip |
| `git bundle verify` | "is okay"; two refs, HEAD and `refs/heads/b13-03` |
| bundle applies | fetches clean onto `0049511`; 31 files, 199,126 insertions, **0 deletions** |
| single-writer files | **none touched** (`det3-conductor.tex`, `det4-onset.tex`, `PROJECT_NOTES.md`, `boundary_deficit.html`) |
| 5 MB rule | largest file in the delivery is well under; repo maximum unchanged at 4.62 MB |
| session-link URL in any file or message | **none** |
| `docs/b13_03_report.md` vs top-level copy | same sha256 `30163e6a…` — genuinely identical, not a drifted duplicate |

Closed-form dimension counts, all reproduced exactly:

| stated | recomputed | agrees |
|---|---|---|
| quartic coefficients at `r = 9` = 495 | `C(12,4) = 495` | yes |
| cubic coefficients at `r = 9` = 165 | `C(11,3) = 165` | yes |
| full quartic degree-6 source dim = 38,760 | `C(20,6) = 38760` | yes |
| full bidegree target = 140,140 | `C(8,6)·C(15,6) = 28 · 5005` | yes |
| `(9,24)` uncompressed source ≈ 1.31×10⁴¹ | `C(518,24) = 1.307×10⁴¹` | yes |
| `(9,24)` full bidegree target = 1.39×10³⁷ | `C(32,24)·C(188,24) = 1.0518×10⁷ · 1.322×10³⁰` | yes |
| `(9,24)` unweighted fixed-cubic target = 1.32×10³⁰ | `C(188,24) = 1.322×10³⁰` | yes |

The 140,140 factorization is worth recording on its own: it confirms the
target is bidegree `(6,6)` in (three linear coefficients, ten cubic
coefficients), which is what a degree-6 source in quartic coefficients must
pull back to along `ℓ·c`. The cost boundary is not an estimate — it is a
count, and it is right.

The hypothesis-guard witness also settles by inspection. For
`ℓ·q = (x₁+x₂+x₃)(x₁³+x₂³+x₃³)` the coefficients of `x₁⁴`, `x₂⁴`, `x₃⁴` are
each 1, so `c_{(4,0,0)}c_{(0,4,0)}c_{(0,0,4)}` evaluates to `1`. The guard is
a real guard.

---

## 2. The result

**First batch-13 session to return its primary objective.** B13-02 returned a
bounded fallback; B13-03 returns the thing it was asked for.

Delivered, exactly, over ℚ and at both house primes:

- Control at `λ = (8,8,8)`, degree 6, ternary quartics. Source dim 38,760;
  weight-monomial count 561; raising matrix 1,056×561 of rank **559**; highest
  weight source dim **2**; restriction rank **1**; `i_red = 1`; kernel
  `(1,0)`.
- `F0` accepted as an ideal element (377 nonzero integer terms). `F1`
  rejected — exact value **729** at the supplied reducible point. A
  non-element with a certificate is worth as much as the element.
- Mixed basis `(F0+F1, F1)`: neither vector is an ideal element, exact kernel
  `(1,−1)`. **Cancellation between source vectors is handled**, which is the
  failure mode a naive per-vector test would miss.
- Unique Pieri predecessor `(8,8,2)`; separate 54×38 raising matrix of rank
  37, giving multiplicity 1 and `h_red = 1`.
- Independent verifier `analysis/b13_03_verify.py` importing **no** producer
  routine: brute-force source enumeration, occurrence-by-occurrence
  derivatives, literal labeled-factor expansion, separate dense modular
  elimination. Int64 exactness justified by `(p−1)² + (p−1) < 2⁶³`.
- Additional controls: `(4,4)` in two variables and `(4,4,0)` in three, source
  dim 1 rank 1; `c_{(4,0,0)}^δ` rejected at degrees 1 and 2; six malformed
  inputs rejected; a rational row `(1/2,1/3)` with kernel `(2,−3)`.
- A certified rational reducible ideal element at `(8,4,4,4,4)`, degree 6,
  **five variables**: 19,834 distinct integer terms, all four simple raising
  derivatives vanishing over ℤ, every coordinate-factor support restriction
  zero, nonzero by explicit coefficient and by replayed determinant-point
  values. Scope stated honestly — neither the whole highest-weight space nor
  the full symbolic pullback was computed.

The binary `(4,4)` control deliberately exercises the non-birational parameter
quotient: a general binary quartic has four linear factors up to scale, so the
factorization must not be called a normalization. That is the sort of care
that has been missing elsewhere.

---

## 3. Why this matters to the board

**It confirms B13-02's cost verdict from an unrelated direction.** B13-02
priced the *realization* space at `(41,17,2⁷)` — 6,711,509,400 monomials, 14.7
TB, 156–2,811 serial years. B13-03 prices the *ambient membership* space at
`(9,24)` — `1.31×10⁴¹` source monomials, `1.39×10³⁷` target, `1.32×10³⁰` even
after fixing the cubic. Different question, different session, different
machine, same conclusion: **the dense ambient route is excluded, and the
missing piece is the compact conversion.** Two independent confirmations of a
cost boundary is a programme-level finding, not a session finding.

B13-03 names the consequence itself and names it correctly: the next
integration job is to export a certified source into ordinary coefficient
coordinates, or to implement coefficient queries against its retained
fixed-factor slice. That is the same 521-coordinate conversion B13-02 identified
as missing. **The two sessions have converged on one blocker.**

**It is directly consumable now.** The board did not make B13-01 or B13-05 wait
on B13-03, so nothing is stalled — but `analysis/b13_03_exact.py` takes either a
supplied rational source or `--cell n:r:degree:λ₁,…,λ_r`, which makes it usable
by both without adaptation. That is a bonus, not a dependency.

**It costs nothing to run.** Primary control 0.496 s; full pullback 0.047 s;
five-variable check 0.459 s; CLI 0.381 s at 24.4 MiB; verifier 2.812 s at 50.0
MiB. Against caps of 600 s and 768 MiB. B13-02 overran its budget 18× twice.
The contrast is the point: the expensive sessions are expensive because they
are working in the ambient space, and B13-03 is cheap because it is not.

---

## 4. Deviations, all self-reported

**The toolchain gap is now confirmed twice and is a host problem, not an
accident.** B13-02 and B13-03 both report no `python-flint`, SymPy, SciPy,
psutil, Singular or msolve, and both report `pip install` blocked by
**WinError 10013** — a network permission refusal, not a missing package.
Two of two sessions on the same host. The remaining ten will hit it.
This needs a decision before more sessions land, not after.

B13-03 routed around it cleanly (Python integers, `Fraction`, and int64
modular arithmetic with an explicit overflow bound), so its results are not in
doubt. But `python-flint` is a pre-registered constraint for exact linear
algebra, and a session that needs a real exact-LA library rather than a
hand-rolled substitute will simply fail.

**The failed first witness, handled correctly.** The first primary run stopped
at a proposed rejection-point assertion because the hand-selected cubic also
lay in `F1`'s zero set. That is a poor witness choice, not a map discrepancy —
and the session says so, retains both the failed log and the retry, banks
nothing from the failed witness, and finds the recorded witness at index 0 of
a bounded deterministic eight-point search. This is the behaviour the protocol
asks for and it is the first time it has been exercised on a failure.

**Attribution is not uniform across the batch.** B13-03's git author is
`swsethuraman <swamijs@gmail.com>`; B13-02's is `Codex Astra`. Neither carries
the `Co-Authored-By: Claude Opus 5` trailer. B13-03's report and prereg front
matter both record `model: gpt-6-astra`, which is the material requirement and
is satisfied; the git author line is cosmetic drift. Worth normalizing in the
preamble for batch 14 rather than chasing now.

**`.pid` files are recorded but not committed — and that is my rule
conflicting with itself.** `delivery_checksums.sha256` lists six `.pid` files;
none reach the tree, because `.gitignore:51` (`results/logs/*.pid`, added at
`5435f7c`, the s71 BLAS pin) excludes them, while 946 pid files committed
before that line remain tracked. B13-03 did what was asked — recorded the pid,
hashed the file — and the repository silently dropped it. **The house rule and
the repository config disagree.** Mine to fix, not theirs.

**My S4 packaging defect is now confirmed independently.** B13-02 reported that
S4's REPLAY.md refers to `inputs/s1_checks.py` and `src/run.ps1`, neither of
which I staged. Checked: `results/astra/S4/` has no `inputs/` directory at all,
and REPLAY.md invokes `$S4Root\src\run.ps1` twice. B13-03 consumed S4's
material anyway — `calibrate.py`, `s64_control.json`,
`s64_r5_exact_kernel.json.gz`, the report — and re-derived the fixed-factor
lemma rather than replaying it, so it was not blocked. Still my defect to
close.

---

## 5. What B13-03 does *not* claim

Recorded because the restraint is load-bearing: no new LMR rank, no membership
claim at the goal cell, no degree-23/24 equality, no sign claim on `D`. The
sampled reducible nullity 5 remains a **sampled deficiency** — a floor on the
rank and a ceiling on `i`, exactly as the corrected discipline requires. The
positive-claim protocol was not activated and no `Q` stage was constructed.

LMR is unchanged at `D ∈ [−4,+1]`.

---

## 6. Delivery hygiene

Front matter carries `board_numbering` and `session_id` throughout. Six
commits, each a real increment with a legible subject line, prereg first.
`delivery_checksums.sha256` hashes 59 files — 31 written plus the inputs the
session *read*, including `docs/batch13_board.md`, `docs/brief_wording.md`,
`docs/reducible_ideal.md`, `docs/transfer_lemma.md` and the S4 artifacts.
**Hashing the inputs as well as the outputs is new**, and it is an advance on
B13-02's already-good hygiene: it makes the provenance of a result checkable
without trusting the narrative. Adopt it as the convention.

---

## 7. Actions

1. **Decide the WinError 10013 question before more sessions land.** Two of two
   confirm it. Either warn the ten outstanding sessions that exact-LA libraries
   are unavailable and to plan for hand-rolled bounded arithmetic, or get the
   host's network permission fixed.
2. Stage the two missing S4 files (`src/run.ps1`, `inputs/s1_checks.py`) or
   amend S4's REPLAY.md to stop referring to them.
3. Reconcile `.gitignore:51` with the pid-recording rule — either untrack the
   946 legacy pid files or carve out an exception; do not leave the rule and
   the config contradicting each other.
4. Carry the input-hashing convention into the batch-14 preamble, together with
   a fixed git author/trailer convention.
5. On the deferred verification pass: reproduce rank 559 of the 1,056×561
   raising matrix and the 54×38 rank 37 independently; re-evaluate `F1` at the
   supplied point to confirm 729; re-check the `(1,−1)` mixed kernel; and
   spot-check the five-variable element's four vanishing derivatives.
