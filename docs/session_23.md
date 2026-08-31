# Session 23 (2026-08-31) — the World-B transport formula: refuted, then proved

Branch `s23-transport`, cloned from public `main` at tip `5cdc29c`. Cloud
container only; the durable folder was **not** owned and nothing was written to
it (rule 9). Mathematics and exact arithmetic; **no engine run, none required**,
and nothing here touches `det_3` or any work in flight on other branches.

Deliverables: `docs/transport_formula.md` (the mathematics),
`paper/det3-conductor.tex` (revised — see §6, **flagged for the integrator**),
this record. Pre-registrations: `results/PREREG_transport.md` (`41d1389`),
`results/PREREG_transport2.md` (`2a82158`).

---

## 1. Headline

**Theorem 3.1's equality is FALSE, and the corrected statement is a theorem at
every degree.**

    c(λ) = ⌊(λ₁ − 2λ₃)/6⌋ − π(λ),
    π(λ) = 1  iff  λ₁ = λ₂  and  λ₁ − 2λ₃ ≡ 1 (mod 6),   else 0,

for every λ with `m(λ) > 0`. First counterexample to the uncorrected formula:
`λ = (17,17,2)` at `δ = 12`, `m = 1`, shadow `⌊13/6⌋ = 2`, conductor `1`.
Confirmed by two independent routes. It sits one degree past the range on which
Theorem 3.1 was tested, which is why it was never seen.

Three further results:

- **The orphan locus is finite: exactly four weights**, `(10,1,1)`, `(13,1,1)`,
  `(11,11,2)`, `(17,17,5)`, at every degree — verified exhaustively over all
  `λ` with `λ₁ − λ₃ ≤ 300`, with a character estimate for finiteness.
- **The paper's orphan-duality question is answered.** The orphan locus is
  stable under `λ ↦ λ* ⊗ det^k` with stabiliser **exactly `6Z`**, because
  `det|_H` has order exactly 6. That twist exchanges `p = λ₁−λ₂` with
  `q = λ₂−λ₃`, which is precisely why the two `q = 0` orphans pair with the two
  `p = 0` ones. It is an elementary character fact and — contrary to the guess
  in Remark 3.4 — **not** the key to the attainment proof.
- **Remark 3.4's "attainment fails exactly on empty support" is also false.**
  `(23,23,8)`, `(29,29,11)`, `(35,35,14)` have `m(λ) > 0`, shadow pole 1, and
  deficit 0.

## 2. The reduction that did the work

The transversal family `f_s = x²y + s y³ + z³` is a **single torus orbit of a
single fixed point of the open orbit**: its Waring-line matrix factors as
`A · diag(ρ⁻¹, ρ², 1)` with `A` constant and `s = ρ⁶/3`. So there is no pole
calculus to do; the conductor is

    c(λ) = (1/6) · max { ν : pr_ν( B · S_λ^H ) ≠ 0 },

the top nonvanishing `τ`-weight of one linear-algebra object. This replaces the
random-dual `sympy` pole computations of `wk2_s3`/`wk2_s4` (approximate,
slow, three random trials per class) by an exact integer computation that runs
the whole `δ ≤ 20` regression in seconds.

Written in the shape model, the two facts that close the argument are:

- **`N_k ≡ 0 (mod 3)` for every admissible shape** — forced by the `μ₃³`
  conditions `n_i ≡ 0 (mod 3)`, and independent of `k`;
- **Young symmetrisation is a pure parity filter**: the two permutations of the
  `k`-pair contribute `F(X,Y) + (−1)^{λ₁−a_k} F(−X,−Y)`, so only the drops
  `T ≡ λ₁ − a_k (mod 2)` survive.

Together they force every achievable `ν` to be divisible by 6 — the
single-valuedness of `F(f_s)` in `s`, recovered combinatorially — and reaching
`6⌊μ/6⌋` requires `a_k + 2q_k̄ ∈ {ε, ε−3}`. If `λ₁ = λ₂` then all `a_k = 0`, that
quantity is even, and for `ε = 1` neither value is available. That is `π`.

This is the exact analogue of World A, where "the phase survives exactly when
`k ≡ b + (p−q)/4 (mod 2)`, which coincides with the integrality parity". World A
has defect identically zero; World B does not, and that is the sharpest
difference between the two cases after the level-2 tower.

## 3. What makes the theorem finite

`det|_H` has order exactly 6, so `m(λ)` and the defect depend only on
`(p, q, r mod 6)`. A sweep over `(p, q, j)` is therefore an **exhaustive**
statement, not a sample. Attainment is proved by an explicit construction
(rules, no search: put the target slot at `s ∈ {ε, ε−3}` and push the other two
strictly out of range) that covers 45513 of 45593 classes with `p, q ≤ 150`; the
80 exceptions lie in `q ≤ 12, p ≤ 18` and were settled by full brute force over
all admissible shapes.

## 4. Prediction ledger

| # | prediction | outcome |
|---|---|---|
| P1 | the torus reduction reproduces the banked `δ ≤ 10` conductor table | **HIT** — 380/380 weights, 0 mismatches, no `ν ∉ 6Z` |
| P2 | symmetrisation cancels by parity only | **HIT** — Lemma D, and 147056 direct tests |
| P3 | attainment holds whenever `m(λ) > 0` | **REFUTED** — `(17,17,2)`, falsifier F3 fired |
| P3' | if P3 fails, the failure is governed by the nonnegativity arithmetic, small `p`/`q`, with an explicit side condition | **HIT** — the failure locus is exactly `p = 0`, `ε = 1` |
| P4 | orphan locus stable under `λ* ⊗ det^k` exactly for `6 | k`; not the key to the proof | **HIT** on both halves (invariance checked for `k = 1…24`) |
| P5 | non-attainment happens exactly on empty support | **REFUTED** — the parity family is mostly `m > 0` |
| C1 | the corrected law | **HIT** — 2361 weights `δ ≤ 20`, family to `δ = 28`, 600-weight sample at `δ = 21…28`, all against the independent multiplicity tables |
| C2 | no failure with `p ≥ 1` | **HIT** — G2 not fired over 45521 classes |
| C3 | every family member fails | **HIT** — G3 not fired |
| C4 | the drop is exactly one ray step | **HIT** — G4 not fired |
| C5 | the `p = 0` orphans are the `m = 0` members of the family | **HIT** |

Two pre-registered hypotheses refuted (P3, P5), both kept. The refutation was
committed (`c1629a8`) **before** the corrected law was written down, and the
corrected law was pre-registered (`2a82158`) **before** any of its confirming
computations were run.

## 5. Honest boundary

Proved outright, no computation: the torus factorisation (symbolic identity),
the spanning and class lemmas, `N_k ≡ 0 (3)`, the parity filter, the
periodicity in `r`, and **Theorem 1 (the obstruction)** — hence the refutation.
The counterexample `(17,17,2)` needs none of this machinery to state or check.

Proved modulo an explicit finite verification: **Theorem 2 (attainment)**. The
construction is by rules and its `T = 0` / `T = 1` coefficient computation is
elementary; what is verified rather than written out in closed form is that its
range conditions hold outside 80 explicit classes.

Not proved: (i) the orientation of the `τ`-grading in the criterion was pinned
by consistency with the independently-proved block-order bound and by a
2361-weight regression, not by tracking the `V ↔ V*` dualisation through
Peter–Weyl — bookkeeping, but not yet done; (ii) normality of `Ω̄` is quoted
(hypersurface, singular locus of codimension 3), not verified here; (iii) the
explicit constant in the orphan-finiteness character estimate was not computed —
the exhaustive sweep is the actual evidence.

## 6. Paper revision — FLAGGED

The paper is in submission preparation, so this is recorded loudly: **the branch
contains a paper edit, and the integrator should decide whether it ships now or
is held.** The case for shipping now: Theorem 3.1 as printed is **false**, and
the counterexample is one degree outside its stated verification range. The case
for holding: the replacement is a strictly bigger claim (unconditional in the
degree) whose attainment half rests on a finite verification, and it changes the
abstract.

What changed: abstract (World-B sentence); Theorem 3.1 (restated with `π`,
unconditional in `δ`, proof sketched); the block-order paragraph (what it cannot
see); Remark 3.4 (rewritten — failure locus, finiteness of the orphan locus,
the duality answer, the false sentence removed with its counterexamples given);
Question 7.1 (replaced by the sharper general conjecture: floor minus a defect
determined by the order of the stabiliser character on the degenerating slot,
with two named tests, one of them `det_4`'s first deficit weight); §6 verification
protocol (the new independent-route regression). Compiles clean, 18 pages, no
undefined references, no LaTeX warnings.

## 7. Assets added

    analysis/wk2_s23_transport.py   the criterion: exact m(lambda) over Z[zeta_3]
                                    (162 elements, 21 character classes), the
                                    straightened S_lambda model, the shape
                                    enumeration, theta_B_weight, conductor_fast,
                                    and construct() -- the attainment rules
    analysis/wk2_s23_sweep.py       the P1 regression and the attainment sweep
    analysis/wk2_s23_lemmas.py      L1-L5, the exact lemma checks
    docs/transport_formula.md       the mathematics
    results/PREREG_transport.md     pre-registration 1
    results/PREREG_transport2.md    pre-registration 2

`wk2_s23_transport.py` supersedes the pole-order computations in
`wk2_s3_wedges.py` and `wk2_s4_sweep.py` for this question: those use random
duals and `sympy` radical simplification and are both slower and approximate.
They are left in place as the historical route, and they agree.

## 8. What this opens

- **§7(4), the general conjecture, is now better posed.** The right shape is not
  `⌊μ_max/|w_N|⌋` but that minus a defect determined by the order of the
  stabiliser character acting on the degenerating slot. World A: order 2, defect
  identically 0. World B: order 2, defect supported on one congruence family.
  A world whose stabiliser character has order `> 2` should show a defect
  exceeding 1 — that is the first test, and `σ_r(v_d(P^n))` with a larger
  symmetric stabiliser is the natural place to look.
- **`det_4`'s first deficit weight** is now a sharper question: does it carry a
  defect? Question 7.5 already says a negative answer to 7.1 would show up there
  first, and now we know what to look for.
- **The level-2 tower (§7(1), roadmap R4)** is untouched and remains the hard
  open end of World B.
- **Roadmap R5 ("which empty-support weights kill the shadow maximum") is
  closed**: four weights, two dual pairs, and the question it was really asking
  — where attainment fails — has a different and larger answer.
