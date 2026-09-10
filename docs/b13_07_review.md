# B13-07 review — independent S79 audit

board_numbering: batch13
session_id: B13-07
model recorded by the session: `gpt-6-astra`, reasoning effort `xhigh`
bundle: `b13_07_s79_audit.bundle` (one part, `part00` byte-identical)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `293e45b78cc0bce9fed8e098f2527b1d62d12034` (`b13-07`)
status claimed: **verified prefix and precise bounded fallback**
integrator verdict: **accept and merge. The audit does its job, states its
coverage exactly, and returns one result that settles a question I had left
open on intuition.**

Stock-take. Arithmetic here is closed-form or a three-line check.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `95b55dde5c71a02dc011516390ff2aa1` — matches, whole and `part00` |
| sha256 | `9a7205b5…3b04f6721` — matches, whole and `part00` |
| `part00` vs whole | **byte-identical**; 265,549 B, matching the manifest |
| declared base | `0049511` — equals `origin/main` and my tip |
| `git bundle verify` | "is okay" |
| applies | clean; 219 files, 57,633 insertions, **0 deletions**; 45 commits |
| single-writer files | **none touched** |
| files outside its own namespace | **none** — every changed path is `*b13_07*` |
| 5 MB rule | none close |
| `Claude-Session:` / `claude.ai` | **none** |
| `Co-Authored-By` | absent on all 45 (Astra pattern; model recorded in front matter and manifest) |

The namespace check is worth stating plainly: **an audit that changes nothing it
audits.** S79's records are read and cross-checked, never edited.

Everything numeric reproduces:

| stated | recomputed |
|---|---|
| 365 shorter weights by length `1,11,48,117,188` | sums to **365** ✓ |
| 57 partitions of 13 with ≤ 5 parts; buckets `10,4,5,2,5` | `p(13, ≤5) = 57` ✓; positives `4+5+2+5 = 16` ✓ |
| 35 drops at degree ≥ 10: `15+12+8` | **35** ✓, and `31 + 4 = 35` ✓ |
| 59 deficiencies `= 24 + 35` | **59** ✓ |
| 187 unreplayed `= 119 + 68`; 46 certificates `= 23 × 2` | ✓ both |
| 2,066-file manifest `= 1200 + 29 + 837` | **2066** ✓ |
| 5,623.5 s of historical cost | 93.7 min ✓ |

---

## 2. The result that matters: `ε_pad` is settled, negatively and rigorously

I withdrew "proved" on `ε_pad = 0` because lifting the mod-`p` containment
`ker(T_pad) ⊆ uM₂₃` to `ℚ` needs no rational ideal element to have a birth
coefficient divisible by **both** house primes — a coefficient of magnitude at
least `4.6×10¹⁸`. That was an argument about magnitudes, not a proof that the
inference fails.

**B13-07 supplies the witness, and it is exactly that magnitude.** Put
`q = 2147483647 × 2147483629 = 4,611,685,975,477,714,963`. Take a
two-dimensional source with old subspace `span(e₀)` and evaluation matrix
`[q, 1]`. Checked:

- `q ≡ 0` at both primes, so the matrix reduces to `[0, 1]` and its kernel is
  `{x₁ = 0} = span(e₀)` — **inside the old subspace at both primes**, every
  modular kernel vector with zero birth coordinate.
- Over `ℚ` the primitive kernel vector is `(1, −q)`, whose birth coordinate is
  `−q ≠ 0`.

So the inference fails **even for an integer matrix, a primitive kernel vector,
and an independent ambient source**. My withdrawal was right, and it now has a
proof rather than a hunch.

The boundary is drawn correctly and I want it on the record: *"This is a
counterexample to the argument, **not** a counterexample about the actual padded
variety."* `ε_pad` may still be 0. What is dead is the route.

**And the report says exactly what would settle it**: a rational functional on
the restriction image annihilating `uM₂₃` but not the birth; or an integer
padded point with `u = 0` and nonzero degree-24 native birth (searched for, not
found); or a rational row-space certificate with a justified old-row rank upper
bound — noting that the existing 269-minor is a *lower* bound and therefore
cannot supply it. Until then, `ε_pad ∈ {0,1}` and the unconditional
`D = 1 − i_pad(24)`, with no exact `i_red` and no `D = −4` claimed.

**The same report keeps the other direction straight**, which is what makes it
trustworthy. Both house primes exceed the tensor degrees (27 and 13), so the
Schur algebra is semisimple in that polynomial degree, the modular multiplicity
spaces match the characteristic-zero lattice, and a full set of modular
highest-weight vectors with independent evaluations **does** certify injectivity
over `ℚ`. It then flags the asymmetry itself: *"merely counting supplied vectors
would not be an upper bound on an arbitrary modular kernel."* Full rank lifts;
containment does not. One document, both halves, no confusion between them.

---

## 3. The inherited dependency, proved from its source

This closes my own `s79_part2_review.md` §2 issue properly. I corrected it by
citing `washout_lemma.md` Theorem 2 — an adoption. B13-07 re-derives it:

- **The s37 point is recovered from its actual generator**
  (`random.Random(20260902*1000+5)`, five row-major 3×3 integer matrices in
  `[−10⁶, 10⁶]`), not taken on trust.
- The exact 35 × 45 Jacobian, with **two nonzero 35-minors** — residues
  `1263013162` and `1627206724` at the two house primes, plus an actual nonzero
  integer determinant by Bareiss.
- All 45 derivative columns cross-checked by **exact** finite differences, valid
  because each entry parameter occurs at most linearly in the permanent, so
  `f(A+1) − f(A)` *is* the derivative. A neat observation that turns a numerical
  method into an exact one.
- A zero-Jacobian control returning rank zero.

Then the support argument: a highest-weight polynomial of weight `μ` of length
`k` has every coordinate monomial's exponent sum equal to `μ`, so all its
factors use only the first `k` variables; its value on a six-variable cubic
equals its value on the restriction; the restrictions of `D_6^{per₃}` are dense
in `D_k^{per₃} = Sym³Cᵏ`; hence an ideal vector at such a weight is the zero
polynomial. **This proves the missing declared dependency at every degree, not
just degree nine**, and the 365 shorter constituents need no evaluation at all.

The transposed-JSON convention is stored beside the numbers rather than left to
be inferred — the right habit after this programme's ordering traps.

---

## 4. Honest coverage, and one correction to the record

**This is a verified prefix, and the report never pretends otherwise** — the
status field says so, the ledger says so per row, and the fallback is enumerated
rather than gestured at. 46 certificates covering 23 weights at both primes were
replayed and pass; **187 weights remain adopted from S79's record**, split into
119 with 238 omitted expanded certificates and 68 for which no expanded
certificate was ever written under the size rule. `coverage.json` carries every
one with its multiplicity, original cost, missing state and exact driver
arguments with isolated output paths. *"No other Batch 13 session is needed to
specify or resume this work."*

**The correction: 31 → 35.** S79's boundary paragraph counts Q2 alone; Q1
contributes four more, so the sampled drop comparisons at degree ≥ 10 total 35 —
15 at degree ten, 12 at eleven, 8 at twelve — with the four Q1 cells listed
explicitly, and `24 + 35 = 59` total deficiencies. Verified.

Attached to it, unprompted, is the discipline correction: *"The determinant
result alone implies `D ≤ 0` in those cells; no positive reducible ideal
dimension is needed. Several older prose conclusions about permanent
invisibility remain stronger than sampled equality warrants."*

**The sign-convention catch is the right kind of care.** Principal minors use
`e_d`; S79 stores `(−1)^d e_d`. Total weight 13 is odd, so every evaluation
differs by exactly one global minus sign — **checked entry by entry, not assumed
from the parity argument**, with the generator ordering detected rather than
presumed and every source monomial verified. *"Nothing is silently skipped."*

**The manifest audit refuses a convenient story.** Of the 2,066 listed files,
1,200 shipped ones exist and match size and MD5; 29 marked unshipped are present
but differ; 837 are absent. The 29 are all supplemental calibration objects, and
rather than blame gzip timestamps the report records their actual and canonical
JSON SHA-256 and declines to treat them as hash-verified final certificates,
because the original bytes are unavailable to check against.

**Third independent confirmation** of the degree-nine census: 210 six-row
positive weights (sum 592, max 9) and 365 shorter ones (sum 1213) — matching
s79's record and B13-05's independent reproduction, now from a third direction.

---

## 5. A scheduling consequence that only appears across two sessions

B13-07's environment is the fourth Astra container and the fourth WinError
10013: no flint, SymPy, SciPy, psutil, Singular or msolve, Python not on PATH,
WMI denied. **And no C compiler.**

That last one matters beyond this session. **B13-05's degree-8 resume recipe —
the cheapest theorem left on the board — begins `gcc -O3 -o <path>
analysis/wk9_s42_wied.c`.** An Astra container cannot build the Wiedemann
binary, so the degree-8 completion has to go to a Claude-side session. That is
a hard scheduling constraint, and it is invisible from either report alone.

The toolchain split is now **seven for seven**:

| | toolchain |
|---|---|
| B13-02, B13-03, B13-06, **B13-07** — Astra | blocked, WinError 10013, 4 of 4 |
| B13-01, B13-04, B13-05 — Fable/Opus | installed cleanly, 3 of 3 |

B13-07 routed around it honestly — exact stdlib arithmetic and the existing
independent NumPy checker instead of flint, **explicitly declaring the deviation
from the tool preference and stating that no floating-point rank was used.** Two
early runs failed (an omitted function argument; the supplemental manifest
mismatch); both were diagnosed and their logs retained.

Resource control is exemplary: 70 bounded jobs, one worker and one BLAS thread
each, a 1.5 GiB Job Object limit, recorded PIDs, ~66 s of summed child wall
time, and the largest commit peak (1.10 GiB, during JSON canonicalization)
reported **with the caveat that it is Windows committed memory, not RSS**. No
numerical job hit its limit.

---

## 6. Also landed during this stock-take

The independent recount of B13-06's new ambient counts, on the house
`wk9_s42_census.a_weyl` rather than B13-06's new implementation:

    a((71,19,2^7); 26) = 392   claimed 392   AGREE   [241 s]

`a((69,21,2⁷);26) = 531` is still running under
`results/logs/wk13_int_b1306_ambient531.{log,pid}`. One of the two numbers the
whole B13-06 continuation is priced against is now confirmed from a second
implementation.

---

## 7. Actions

1. **Merge-ready** — no trailer surgery, nothing outside its namespace.
2. **Route B13-05's degree-8 completion to a Claude-side session.** Astra
   containers have no C compiler and cannot build `wk9_s42_wied.c`. This is the
   cheapest theorem on the board and it must not be scheduled where it cannot run.
3. **Warn the remaining Astra slots** about WinError 10013, the absent exact-LA
   libraries, and the missing C compiler — four for four now.
4. **Fold the `ε_pad` counterexample into `det4-onset.tex`** and into the open
   questions: the inference is refuted by an explicit witness, `ε_pad ∈ {0,1}`
   stands, and the three routes that would settle it are named. This replaces my
   magnitude argument with a proof.
5. **Adopt B13-07's proof of the shorter-weight dependency** in place of the
   Theorem 2 citation in `s79_part2_review.md` §2 — it is stronger and holds at
   every degree.
6. **Apply the 31 → 35 correction** to `s79`'s boundary paragraph and anywhere
   the board quotes it.
7. **Bank `coverage.json` as the standing handoff** for the 187 unreplayed
   degree-nine weights; it is self-contained and needs no other session.
8. On the deferred verification pass: replay two of the 23 replayed weights'
   certificates independently, and re-derive one of the two 35-minors from the
   recovered s37 point.
