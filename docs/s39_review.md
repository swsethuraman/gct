# Integrator review — session 39 (the long-weight occurrence screen, ℓ=6–10)

2026-09-02.  Branch `s39-longweights`, delivered head `5d01eda` (14 commits on
`e9cb8dd`; the doc's `81e4623` is an ancestor, later cleanup commits on top —
benign, matches the narrative).  Prereg first.  This is a negative result, so
the verification is inverted: the risk is a masking bug (inflated `m_det` or
deflated `a` hiding a real cell), and I checked that the screen *could* have
fired.

## 1. Verification — the margins are real

I recomputed `a` and `m_det` at the fire-risk cells with my own code (Kostant
alternation for `a`, Murnaghan–Nakayama for `m_det`, shared with neither of the
session's engines):

- the tightest family `(4δ−10, 2,2,2,2,2)`: `a = 1`, `m_det = 13` (verified at
  δ=8,9), **margin 12 exactly** — the `m_det` is not inflated;
- the ℓ=7 and ℓ=8 tight cells `(20,2^6)` and `(18,2^7)` at δ=8: `m_det = 18, 21`,
  margins 17 and 20 — matching the screen's tightest-margin column exactly;
- the balanced max-`a` cells `(11,8,6,4,2,1)` and `(14,9,6,4,2,1)`:
  `a = 91, 504` exactly.

So both fire-risk extremes — smallest `m_det` (peaked) and largest `a`
(balanced) — reproduce, and every one has `a < m_det`.  Combined with the
exhaustive enumeration (candidate count = banked count at all 22 chunks,
79,255 weights), the silence is genuine and complete, not an artefact.  The
session's own guardrails (two 61-bit primes + CRT, per-cell bound and parity
asserts, its C engine validated against the house routines and s38's full
length-5 table before use, then re-verified against a character-free reduced
kernel after) are exactly the right discipline for a null result, and they
agree with my pass.

## 2. The ℓ ≤ 10 bound is sound and it closes the region

The new proved bound: the padded permanent is concise in ten variables, so
`P_r ⊆ Sub_{10}`, whose coordinate ring carries only weights of length ≤ 10;
hence `mult_pad = 0` for `ℓ(λ) ≥ 11`.  This is the standard subspace-variety
concision fact, and the session's elementary weight-domination proof is
correct.  With it the region a **permanent-specific** obstruction can occupy is
now bounded on all four sides:
\[
  a \ge 1,\qquad \lambda_1 \ge \delta,\qquad 6 \le \ell(\lambda) \le 10 .
\]
`ℓ ≤ 10` (this session), `ℓ ≤ δ` (Pieri), `λ_1 ≥ δ` (Kadish–Landsberg via (★)),
`a ≥ 1` (BIP silent at (3,4)).  Rows 11–16 carry `mult_pad = 0 ≤ mult_det` — the
wrong sign, never an obstruction.  **On the lower bound (corrected s49):**
`ℓ ≥ 6` is where the permanent first *enters* (`docs/washout_lemma.md` Thm 6),
**not** a proof that no obstruction exists at `ℓ ≤ 5`; washout (`P_r = R_r`,
`r ≤ 5`) says only that any `D > 0` there would be a *reducibility* obstruction,
not a permanent one, and does not preclude it.  What actually closes `ℓ ≤ 5` is
containment at `ℓ ≤ 4` (`D ≤ 0` proved, `docs/r4_containment.md`) and
*measurement* at `ℓ = 5` (`D ≤ 0` at every cell reached; `R_5 ⊆ D_5` is open).
So `ℓ ≥ 6` bounds the *permanent-sensitive* region — the right statement for
paper 2 — and it is what makes the screen exhaustive there; it is not a
four-sided proof that the search space for *any* obstruction is `6 ≤ ℓ ≤ 10`.

## 3. What the result establishes

The occurrence route — the arithmetic mechanism that pinned the determinant's
ideal at n=3 — is now **retired at n=4 across every length that can carry the
permanent**: length 5 by s38, lengths 6–10 here, exhaustively, 79,255 cells,
zero one-bit and zero forced.  And the session explains *why* the n=3
precedent does not transfer, which upgrades the finding from "silent" to
"structurally silent": at n=3 the one-bit cells lived at ℓ near n²=9, the edge
of the Kronecker length bound where the coefficient is sparse; at n=4 that edge
is near 16, outside the pad-eligible region ℓ ≤ 10 entirely, and inside ℓ ≤ 10
the stabiliser room `m_det` is large — and *growing* with length (the tightest
margin widened from 7 at ℓ=5 to 12 at ℓ=6). That widening is evidence, not
proof, that the silence persists at δ ≥ 13 and would persist at any reachable
length; the pre-registered stop at δ=12 is honest about where measurement ends.

This is the negative backbone of paper 2's obstruction chapter, and it is a
strong one: not "we looked and found nothing" but "the arithmetic route is
provably empty in a region closed on all four sides."

## 4. The handoff is exact

What s39 leaves untouched is precisely what s41 now hunts: the **multiplicity
route**, `mult_det < a ≤ m_det`, which needs a rank measurement and is
invisible to arithmetic.  s39 has done the arithmetic screen's whole job and
handed the frontier to the rank sweep with the region already bounded — the
peaked cells it identifies cost `n_χ = 200` under the reduction, well within
reach.  And s42's reducible-locus table will supply the pad side for those same
cells.  The three sessions compose cleanly: s39 says the arithmetic is empty
and the region is closed; s41 measures the six-row determinant onset and checks
the permanent there; s42 makes that check one-sided.

## 5. Process

Prereg first; the C engine validated before use and re-verified after; the
final δ=12 chunk split across both cores from opposite ends with atomic appends
and dedup-by-weight checked in agreement; kills by explicit PID with read-back
(no `pkill -f` — the rule finally held for a full session); nothing over 5 MB
committed; five insurance bundles. A model null-result session, and the kind of
exhaustive negative that is only convincing because the discipline is visible.

## 6. Standing after session 39

Arithmetic obstruction route: retired at n=4, region closed on all four sides.
Remaining: the multiplicity route at 6 ≤ ℓ ≤ 10 (s41 in flight), and the
untested δ ≥ 13 (expected silent by the widening margin, not measured). Paper 2
gains the ℓ ≤ 10 theorem and the exhaustive screen as its negative half.
