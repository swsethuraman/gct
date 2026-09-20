# B23-10 — verdicts formed before reading the deliverable's own defence

Byte-preserved; corrections only in `docs/b23_10_review.md`, with a pointer back.

```
git rev-parse HEAD          2efb7aaf1927e8d2785dfbbcc78b847592c204f5
git rev-parse HEAD^{tree}   d922720ff27092578b8c59aefc80f6216c1a5a73
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-19T01:40:49Z
```

---

## Q1 — the two defects alleged against B22-10, and the dimension reversal

**Written before opening** B23-04 `GAPS.md`, B23-03's report, or the B23-12 ledger. My only sources are
the brief's one-line summaries and B22-10 itself at `2efb7aaf` (sha256 `86d8caf9…`), which I re-read
(lines 65–66, 175, 303–311, 427, 439–440). Method: READ.

**G-17 (cap minors on the plane family).** B22-10 §7 says "The cap minors do vanish on the plane family
too (rank 64 there, pilot 2)". Its evidence was `rank M_4 = 64` at **one** random cubic through a
plane — an exact rank over `Q` (Bareiss), not a modular one as the allegation reportedly says. Either
way it points in the wrong direction. A rank at one point is `<=` the generic rank, so it gives a
**floor** on the family's generic rank (`>= 64`). "The 65-minors vanish on the family" is the
**ceiling** `<= 64`, and one point cannot supply it. B22-10's own S18 labels the same data MEASURED,
but §7's sentence and its conclusion ("the right-way cubic separation survives the correction") state
it as fact. **Pre-formed: over-stated on its evidence (should have read MEASURED at one point); B23-04
was right to call it OPEN; whether Prop. 2.5 closes it depends on its proof, which I will check.**

**G-18 (S11's "iff").** S11: "rank 3 iff `P` divides every `3 × 3` minor". Rank 2 mod `P` already
gives `P | every 3 × 3 minor` of the exact rows, so that condition is **necessary** for rational rank
3 but not sufficient: it also holds when all the minors are zero, i.e. rational rank 2. The correct
statement is B22-01's: rational rank 3 "would require `P` to divide every `3 × 3` minor"
(equivalently, rank 3 iff some minor is nonzero over `Q` and all are divisible by `P`). §3.2's
"possible exactly when" has the same error. **Pre-formed: the allegation is right; corrigendum to S11
and §3.2.**

**Dimension reversal.** B22-10's numbers are Jacobian ranks into `C^70`, i.e. **affine** dimensions:
the plane (template) family `>= 35` affine, `{l·C : C ∈ D35}` `= 33` affine. S24 and §7 line 310 say
so ("33 affine (32 projective)"). So B22-10's data are `>= 34` projective against `32` projective —
the same as B23-03's reported "34 projective against 32", as far as the lower bound goes. B22-10 does
**not**, in committed bytes, say "projective dimension >= 35"; that part of the allegation, as the
brief summarises it, is not supported by the text. But B22-10's §1 ("not 32 — the record is off by
one") and §7's bold line ("The record's 'dimension 32' is off by one") are **wrong**: the record's 32 is
the correct projective dimension, and B22-10's own next sentence says so. What survives is narrower: the
record put `D45`'s affine 50 beside this projective 32 — a convention mix, not an arithmetic error.
**Pre-formed: B22-10's measurements stand; its "off by one" sentences are withdrawn; "32 was right"
(projective) is correct; the mix-of-conventions remark stands only if B22-02 quoted `D45` affine,
which it did ("dim 50").** On G24: the gate is vindicated, not undermined — its own author broke it.

---

## Q2 — B23-03 Proposition 2.5, Theorem 3.2, and G-A1, from the statements

**Written 2026-09-19T01:43:33Z.** Read so far in `docs/b23_03_report.md` at `3bcad666`: "Plain terms" and §0 (lines
28–71), the first four lines of Prop. 2.5 (306–309, statement plus the definition of `g`), and
Theorem 3.2's statement (407–410). Not yet read: the rest of §2.5, §2.6, §3, §5, any pilot output.
Method: READ + INDEPENDENT (hand).

**Prop. 2.5 — expect PROVED, by this mechanism.** Take `Pi = {x_1 = x_2 = 0}`, `C = x_1 q_1 + x_2 q_2`,
`u = (d_3 q_1, d_4 q_1, d_5 q_1)`, `v = (d_3 q_2, d_4 q_2, d_5 q_2)` (vectors of linear forms), and
`g = u × v` (quadrics). Then `sum_{j=3..5} g_j d_j C = x_1 (g·u) + x_2 (g·v) = 0` identically, so
`(0, 0, g_3, g_4, g_5)` is a quadratic syzygy of the partials: a kernel vector of `M_4`. If the five
partials are linearly independent, the 10 Koszul syzygies are independent, and any Koszul syzygy with
`g_1 = g_2 = 0` has the form `a × (x_1 u + x_2 v)` (`a` constant), whose entries lie in `(x_1, x_2)`.
`u × v` restricted to `Pi` is generically nonzero, so `g` is not Koszul, `dim ker >= 11`, and
`rank <= 64`. That holds on a dense open subset of the irreducible `Sigma_Pi`; `{rank <= 64}` is
closed, so it holds on all of `Sigma_Pi`, which is exactly what "every member" needs. "Generic value
exactly 64" also needs one point of exact rank 64 (a floor). For the witness
`q_1 = x_3^2 + x_4^2`, `q_2 = x_5^2 + x_3 x_4`: `u = (2x_3, 2x_4, 0)`, `v = (x_4, x_3, 2x_5)`,
`u × v = (4 x_4 x_5, −4 x_3 x_5, 2x_3^2 − 2x_4^2)`, and the third entry is not in `(x_1, x_2)`, so
the witness syzygy is non-Koszul. I will replay `rank M_4 = 64` at the witness exactly, and the
syzygy identity. **If the proof in §2.5 has this shape, it closes G-17.**

**Thm 3.2 — expect PROVED if three things are present.** (1) A padding **ceiling** valid on all of
`P_N`: `J_{lC} ⊆ (l, C)` gives `dim (S/J_{lC})_k >= HF_{S/(l,C)}(k)`, hence
`rank M_k(lC) <= dim S_k − [dim S'_k − dim S'_{k−3}]` (`S'` in `N − 1` variables), which extends to the
closure by semicontinuity. (2) Determinant-side **floors** at explicit points: a modular rank is a
floor, which is the safe direction. (3) An argument for **all** `k`. That cannot be a finite
computation. The natural route is a proved ceiling on `dim (S/J_F)_k` at an explicit determinantal
`F`, via a regular sequence of length 4 (`grade J_F >= 4`, since `dim Sing = N − 5`), giving
`dim(S/J_F)_k <= [t^k](1−t^3)^4/(1−t)^N`, followed by a polynomial inequality in `k` (the "Newton
certificate"). **The weak point I expect:** whether `grade >= 4` at the explicit point is *certified*
or only measured. If it is only measured, the tail is MEASURED and the theorem is PROVED for the
finitely many `k` computed.

**G-A1 — expect genuinely open.** The classification treats *direct* points (`det A = l C`). A point
of `closure(im phi) \ im phi` of the form `l C*` with `C*` smooth is excluded by nothing listed:
excluding it needs the boundary of `phi` — limits of pencils through the singular-pencil locus `Z`
and their jets, B20-10 R11's territory, conditional on EH C1/C3. A smooth-`C*` boundary point is not
known to exist: B17-01-C excludes one specific `F*`, not all.

---

## Q3 — B23-01 §3 (the second-prime test), before §§1, 2, 4, 5

**Written 2026-09-19T01:44:22Z.** Read: `docs/b23_01_report.md` at `cc14e88c`, §3 only (lines 182–231). Method: READ.

- **The test is the one B22-10 §4 priced:** a second prime (`P_2 = 524269`), three certified points,
  `3 × 15 = 45` evaluations, all twenty `3 × 3` minors. **All vanish mod `P_2`: outcome (b).** That is
  MEASURED evidence at a second prime and changes no label. Notably it is weaker than the `P` result
  in one respect: at `P_2` there is no injectivity certificate (`det E` is certified mod `P` only), so
  rank 2 at three points is a *sampled* statement at `P_2`, not a polynomial identity mod `P_2`. `Q`
  form: still OPEN.
- **The reconstruction** `alpha ≡ 737/646`, `beta ≡ −1421/969` (common form `(2211, −2842)/1938`,
  `1938 = 2·3·17·19`) is a MEASURED candidate, correctly labelled. I will verify arithmetically
  that both residues lift consistently.
- **Height 2000.** On the usual per-coefficient height (`H(a/b) = max(|a|, |b|)`), `737/646` has
  height 737 and would be found by any search to 2000. So **if the old claim was per-coefficient it is
  false and must be struck, or scoped**; if it bounded a common-denominator triple, `2842 > 2000` and it
  stands as stated but must say so. I expect the definition to be recoverable from the prose of
  `routeA` §5.3 / `arc_target` C3 even though the code is gone, and I will look there before ruling.
  B23-01 declining to resolve it is correct for a producer.

## Q4 — B23-02 Proposition 1.1, from the statement

**Written 2026-09-19T01:44:22Z.** Read: lines 68–95 (the statement and the first four lines of the proof of (a)).
Method: READ.

**Expect PROVED on classical inputs.** (a) is Eagon–Northcott/Hilbert–Burch for the maximal minors of a
`3 × 4` matrix of grade 2: perfect, unmixed, saturated, generated in degree 3. (b) The degree-4 part is
`S_1·I_3`, of dimension `4N − 3` (the three degree-4 syzygies), which Laplace identifies with
`{det[B; m]}`. (c) Scheme-theoretic containment puts `F` in the saturated ideal in degree 4, hence
`F = det[B; m]`. (d) follows. **Consequence:** the containment condition *is* determinantal
membership, so row 10 collapses into the question of which quartics are determinants — row 11's
territory (`ker phi^*`), as the title says. Caveat to check: (c) needs *scheme-theoretic*
containment; a set-theoretic version needs `I_3(B)` radical (true for generic `B`, since unmixed and
generically reduced), so any use of (c) for non-reduced degenerate members must say so.

---

## Q5 — Paper 1 Prop. 4.1 (bracket census) against Bürgisser–Ikenmeyer arXiv:1511.02927

**Written 2026-09-19T01:46:42Z.** Formed before opening B23-05's `GAPS.md`, `CHANGES.md`, `READINESS.md`, or the edited
paper. Sources read:

- Paper 1 **as archived**: `paper/det3-conductor.tex` at `82633a60` (sha256 `dd0d2abf…`), lines
  160–176 (intro claim) and 470–545 (Prop. `prop:census`, its proof, its corollary).
- BI: arXiv PDF v2 (current) fetched to the scratchpad, sha256
  `a4138fc3ef45f144f367f227514b8345ddd74690c19ca07e1ef4be707fd6ea7b` (v1:
  `c2584469cc1591b010ae758a7027367a1008ca61156e302762ce2bae64b8c62a`); text read from the ar5iv
  HTML rendering, sha256 `14b94adfa7b05d1dc143aca55cea25ed26d67384759886a466938e44df41cbca`: Prop. 3.24
  with its proof, and Appendix §7.1 (Prop. 7.1, Cor. 7.2, Prop. 7.3). There is no local PDF text tool,
  so the reading is of the rendering, not of the hashed PDF bytes.

**The two statements.** *Paper:* `D` odd, `m | δD`, `k = δD/m`; if `δ > C(k, D)` then
`C[Sym^D C^m]^{SL_m}_δ = 0`. *BI Cor. 7.2:* `D` odd, `m | dD`; `dim C[Sym^D C^m]^{SL_m}_d` is at most the
number of `d`-element **sets** of `D`-subsets of `{1..dD/m}` in which each number occurs in exactly `m`
subsets. With `d = δ` and `k = dD/m`: if `δ > C(k, D)` there is no set of `δ` *distinct* `D`-subsets of
`[k]` at all, so BI's count is 0. **The paper's Prop. 4.1 is therefore the vanishing case of BI
Cor. 7.2, a direct special case of it.** And BI's own Prop. 3.24(3) — "no nonzero `SL_m`-invariant in
degree `2m` if `C(2D, D) < 2m` … it suffices to show that there are less than `2m` distinct cardinality
`D` subsets of `{1..2D}`" — is exactly this census at `δ = 2m`, `k = 2D`.

**Pre-formed ruling: the census is not new as a result; it is contained in BI Cor. 7.2, and its
mechanism is BI's in Prop. 3.24(3).** "Equivalent" overstates it in one direction. Cor. 7.2 is
*stronger*: it counts, and it also enforces the regularity constraint (each number in exactly `m`
subsets), so it can vanish where `δ <= C(k, D)`. The paper's statement uses only the pigeonhole case.
And Prop. 7.3 (a tableau strengthening, stated by BI *without proof*) is not needed for the implication
at all. So the right description is "a special case of BI Cor. 7.2", not "equivalent to Cor. 7.2
with Prop. 7.3". The consequence the paper draws, `e(det_3) >= 18` "with no computation", also follows
from BI's own Cor. 7.2 at `m = 9`, `D = 3` (`δ = 12`: `k = 4`, only 4 distinct 3-subsets for 12 letters)
together with BI's period theorem. The intro's framing ("turns out to need no computation … already
excludes every smaller degree") needs the attribution.

**The proofs differ in language, not in substance.** BI go through `mult_λ(O(Sym^D)_d) =
mult_{λ^t}(Λ^d Λ^D C^m)` for odd `D` (their [34, Fact 6.1]) and bound by a weight-space dimension, where
`Λ^d` is what forbids repeated `D`-subsets. The paper goes through the FFT for `SL_m` (bracket monomials)
and a transposition sign `(−1)^D = −1` that kills repeated rows. Both are the same antisymmetry. The
bracket proof is elementary and self-contained and needs no plethysm fact, which is worth **one sentence**
in a remark ("an elementary proof via the first fundamental theorem"), not a novelty claim. Run in full,
the bracket argument bounds the dimension by the number of admissible row-*sets*, i.e. it reproves
Cor. 7.2 itself, not just the pigeonhole case; the remark may say so.

---
