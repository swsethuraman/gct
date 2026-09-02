# Integrator review — session 40 (the onset cap theorem, and paper 1's bracket)

2026-09-02.  Branch `s40-onset`, head `7e0cc1e` (10 commits on `e9cb8dd`,
prereg first at `d8a50f2`).  The load-bearing claims were re-verified from
scratch; the algebra and the geometry both hold.

## 1. Verification — all pass

**The closed forms.**  `cap(n) = C(3n−1,4) − μ_{3n−5}(n)`,
`5·C(2n,4) − 10·C(n+1,4)`, and `5n(n−1)²(7n−8)/12` agree at n = 2..8:
`5, 65, 300, 900, 2125, 4305, 7840`.  `ν(n) = n²(n²−1)/12` gives
`1, 6, 20, 50, 105, 196`.  The smooth Milnor values μ reproduce
`0, 5, 30, 101, 255, 540`.

**The Gulliksen–Négård identity — the general-n heart.**  From the GN
Hilbert series of `S/J` I recomputed `H_{S/J}(2n−5) = ν(n) − 1`,
`H_{S/J}(2n−4) = ν(n)`, and `ν − H_{S/J}(n) = C(n−1,4)` at **every n from 3
to 10**.  The first of these is what forces `def_{2n−5} ≥ 1` uniformly (since
`def ≥ ν − H_{S/J}(2n−5) = 1`), so the defect step is genuinely proved at
every n, not just measured — subject only to the adopted GN resolution and
its grade-4 specialisation, which are standard (Bruns–Vetter).

**The Jacobian coranks, from scratch, including a value nobody had checked.**
Building the Macaulay matrix of the five partials directly and ranking it mod
a prime: generic corank equals μ and determinantal corank equals μ+1 at n=3
(5→6), n=4 (30→31), and **n=5 (101→102, a 1050×1001 rank)**.  The determinant
pencils lose exactly one dimension in degree 3n−5, three values of n, matching
the report on the nose.  So `cap(n)` is the exact rank of `M_{3n−5}` on
`D_5^{det_n}` at these n, and the family enters the ideal precisely at
`cap(n)`.

**The frame theorem's arithmetic.**  The 30 node conditions (six frame points
× five partials) on the 35 cubic coefficients have rank 30 — independent — so
the cubics singular at the standard frame form a `P^4`, as Theorem 3 needs.
(I did not reproduce the sixth-point Gröbner witness; the rank-30 fact plus
the openness argument is the load-bearing part and it holds.)

## 2. What this delivers

**Paper 1 improves by a real notch.**  The bracket `8 ≤ δ_0 ≤ 80` becomes
`8 ≤ δ_0 ≤ 65` — the Jacobian family beats the discriminant by 19% at n=3,
with a proof (the six nodes cannot impose six conditions on the 5-dimensional
space of linear forms, so the defect is automatic; no geometry adopted at
n=3).  `docs/paper1_delta0_patch.md` is the drop-in text; I'll place it in the
paper pass together with Question 8.5's rewrite.

**Question 8.5's first sub-question is answered.**  `D_5^{det_3}` is the
closure of the cubic threefolds singular at six points in linearly general
position (Theorem 3), so the generic such six-nodal cubic threefold is
determinantal.  That turns the δ_0 hunt into "the first covariant vanishing on
cubics singular at a projective frame" — a classical object (the Segre cubic
lives in that P^4).  This is genuinely new relative to what the paper claimed
and worth a sentence in §8.

**Paper 2 gains a spine.**  One formula, `cap(n) = 5n(n−1)²(7n−8)/12`, caps
the determinant's first five-row equation at every n, proved from a node
count that fails forms of degree 2n−5 by exactly one, and measured fresh at
n = 5, 6, 7 where nothing had been looked at.  The GN remark — that the
`2n²−2` linear syzygies of the minors are the determinant's infinitesimal
stabiliser — is the kind of structural observation that makes a paper, not
just a computation.

**The n=5 anomaly is understood, not papered over.**  The "nodes =
codimension" coincidence of n=3,4 is exactly `C(n−1,4) = 0`; from n=5 it
fails, `D_5^{det_5}` is a superabundant component of the 50-nodal locus, and —
correctly — the cap theorem is untouched because more defect only lowers the
cap.

**The conjecture is stated honestly.**  `onset = cap(n)`: proved at n=2,
open above, and — the session's own framing — the support (§3.1–5) is "the
absence of the mechanisms we know," not evidence for an equation-free range.
The prior stays low-to-moderate.  The one decisive test run, the unique
degree-10 SL_5-invariant of cubic threefolds at n=3, does **not** vanish on
`D_5` (`mult_det = 1`), so no invariant below degree 15 is an equation — 121
empty length-5 cells at δ=8,9 on top.  All in the expected direction; none of
it forces the conjecture, and the session says so.

## 3. Refinements and one correction to carry

- The `I(D_6^pad)` onset was restated: its *length-6 part* begins at 6, while
  the ideal itself begins at 5 (s36's I_5 pulled back).  My s36 review should
  read the same way; noting it here so the record is consistent.
- (★) is now a theorem for every n, r, δ and every padding exponent — the
  general form of s36's criterion, with Kadish–Landsberg as its automatic
  case.  Literature verdict: technique is KL's, the exact criterion not found
  stated.  Fine to claim as a clean statement, not a deep new result.
- Beyond n=7 the dimension/saturation facts are labelled expectation; nothing
  in the paper-facing claims (n=3, and the general cap via GN) depends on
  them.
- Process: one `pkill -f` self-kill, no data lost, recorded.  Fourth session
  bitten — the standing rule clearly is not enough on its own.  I will put a
  `scripts/killpid.sh` helper in the next brief and ban the bare command in
  the pipeline, not just in prose.

## 4. Standing after session 40

The det-side onset is capped by a proved formula at every n and pinned to a
window at n=3 (`[8,65]`) and n=4 (`[8,300]`).  Paper 1 gains a sharper bracket
and an answered sub-question; paper 2 gains its central theorem and the n=5
anomaly.  None of it touches the permanent — length 5 is washed out — so the
obstruction question is exactly where s39 left it.  Next: place the paper
patch; the n=3 length-5 plan (`results/n3_length5_plan.md`) is the cheap way
to move the conjecture's prior, and the n=4 invariant test `(8^5)` at δ=10 is
its one-cell analogue.
