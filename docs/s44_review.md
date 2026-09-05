# Integrator review — session 44 (the six-row cap)

2026-09-03.  Branch `s44-sixrowcap`, head `d3f06c6` (5 commits on `0c229c1`;
pre-registration `2e06e3f` before any rank).  Pure additions, no file over
5 MB added, no session link in any of its own commits or scripts.  The verdict
`onset I(D_6^{det_4}) ≤ 661` (no lower bracket is established; see `results/sixrow_record.md`) is accepted, with the labels as the session
assigned them.

## 1. Verification — the ladder reproduces from scratch

I rebuilt the whole thing with my own polynomial arithmetic and my own
Macaulay assembly (flint used only for the rank), fresh pencils, both house
primes:

| `d` | rows × cols | `ρ_d` | smooth | determinantal | drop | padded permanent | drop |
|---|---|---|---|---|---|---|---|
| 4 | 36 × 126 | 36 | 36 | 36 | 0 | 36 | 0 |
| 5 | 126 × 252 | 126 | 126 | 126 | 0 | 116 | 10 |
| 6 | 336 × 462 | 321 | 321 | 321 | 0 | 271 | 50 |
| 7 | 756 × 792 | **666** | 666 | **660** | **6** | 526 | 140 |
| 8 | 1512 × 1287 | 1197 | 1197 | 1146 | 51 | 917 | 280 |

Every number matches `results/s44_ladder.md` exactly, including the two that
carry the argument: no drop at `d = 4, 5, 6`, and a drop of exactly six at
`d = 7`.  Both anchors also reproduce with my code — `(3,5,4)`: 75×70,
generic 65, determinantal 64; `(4,5,7)`: 350×330, generic 300, determinantal
299 — so the harness really is the five-row cap theorem, and paper 1's
`δ_0 ≤ 65` is the same construction.

**Theorem A checks out arithmetically.**  With the Gulliksen–Négård resolution
`1, 16, 30, 16, 1` in degrees `0, 3, 4, 5, 8`, I get `H_{S/J(M)}(d) = 40, 60,
80, 100, 120, 140` for `d = 3..8` (`= 20d − 20` from `d = 5`), so the ceiling
`dim J(M)_8 = 1147 < 1197 = ρ_8`, and at `d = 9`, `1842 < 1952`.  With
`J_F ⊆ J(M)` by Jacobi's formula the conclusion follows, and it needs no
computation.  **This is the session's real deliverable and it is a theorem.**

**The no-drop-at `d ≤ 6` argument is genuinely a proof**, and the direction of
each inequality is right: a rank mod `p` is a lower bound on the rank over `Q`,
a rank at a point is a lower bound on the generic rank, and `ρ_d` is an upper
bound for every form — the three close only because the measured value *equals*
`ρ_d`.  §4's analysis of why the same reasoning does *not* prove the `d = 7`
drop is correct and is the most careful piece of epistemics the programme has
produced.  The Hadamard/multimodular certificate is sound as stated (each row
of `M_7` is an isometric placement of a partial's coefficient vector, so the
bound applies), and what it pins — `rank_Q M_7 ∈ [660, 665]` at three explicit
pencils, with genericity left to Schwartz–Zippel at `2.4·10⁻²⁷` — is exactly
what the document claims and no more.

## 2. One correction, in our favour

`docs/sixrow_cap.md` §9 flags that it could not confirm the journal reference
for Dimca's theorem, which paper 1 carries in its bibliography.  I confirmed
it from a citing paper: **Bull. Math. Soc. Sci. Math. Roumanie Tome 56(104)
No. 2 (2013), 191–203**.  Paper 1's `\bibitem{Dimca13}` is correct; adding
"No. 2" would make it complete.  Nothing to fix before arXiv.

## 3. One addition — the `C(r,5)` guess is not pinned by its data

The measured drops at `d = 3n−5` are `0, 1, 6` at `r = 4, 5, 6`.  `C(r,5)`
fits, and the session is right to call it a guess — but it is worth recording
*how* underdetermined it is.  `(r−4)(2r−9)` fits the same three points and
gives `15` at `r = 7`, against `C(7,5) = 21`; `C(r−3,2)` fits two of the three.
So the proposed `(n,r) = (5,7)` test is not merely the next data point, it is
**discriminating** — two natural formulas differ there by 6.  That raises its
value above the session's own ranking of it, and the `12012 × 8008` rank it
needs is well within a session's budget.

## 4. What it means for the programme

The session's premise failed and it says so plainly, which is the right way to
report it.  A drop at `d = 4` would have put an equation in degree 36 and made
the six-row question directly measurable; the drop is at `d = 7` and the cap is
666, three orders of magnitude above the `n_χ ≈ 20,000` frontier.  It points at
no reachable cell, and Phase 4.2 was correctly skipped under the pre-registered
rule.  **The measuring route is not made unnecessary** — s45's frontier work is
exactly as important as it was yesterday.

The minors are not separators, and the reason is the structural one predicted
in advance: `ℓ·per_3` is reducible, singular in codimension 2 against the
determinantal curve, so it drops earlier (from `d = 5`) and much harder (140 at
`d = 7` against 6).  This is the transfer lemma in a new costume, and it is
worth stating as a general principle in paper 2: **any construction that
detects excess singularity can only give `D ≤ 0`**, because the padded
permanent is always the more singular object.  That closes off a whole family
of approaches, cheaply and permanently.

Three things landed that were not asked for and are worth keeping: the singular
curve (degree 20 = `ν(4)`, arithmetic genus 21, `J(M)/J_F` of finite length
140); the first drop sitting at `d = 3n−5` for every `r ≤ 6`, i.e. the five-row
cap degree does not move when the fifth row becomes a sixth; and — if the
literature check holds — Theorem A as the first degree bound of any kind on the
ideal of a locus of determinantal hypersurfaces, with Reichstein–Vistoli's own
disclaimer as evidence the question was open.  That last one is a result
independent of GCT and belongs in paper 2 on its own merits.

## 5. Nits

- §12 "It was killed **by that recorded pid**" → the house form is "ended by
  that recorded id" (`docs/brief_wording.md` §1).  The Schwartz–Zippel "kill a
  nonzero polynomial" is standard usage and stays.
- The Beauville and Piontkowski readings came from an automated skim with
  ProjectEuclid blocking direct fetch; before either is cited in print, one of
  us should read them.
- `analysis/wk9_s44_exact.py` is left in the tree as a slow route with a
  docstring explaining why; that is fine, but the doc should say once that
  `wk9_s44_certify.py` supersedes it, which §12 does.

## 6. Process

Pre-registration before the first matrix, with priors on the alternatives and a
stopping rule that was actually honoured when the cap came in above 200; both
primes and multiple seeds at every measurement, re-run at two further coefficient
boxes in a separate verification pass; a genuine prediction (`r = 4`, no drop
anywhere) run *because* the guess implied it; and the one wrong prediction
(P1′, drop of one) reported as the most interesting line in the scorecard.  The
refusal to push the branch against the brief's explicit instruction was also
correct — delivery is the bundle.
