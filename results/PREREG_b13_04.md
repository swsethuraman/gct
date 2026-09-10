# Pre-registration — B13-04 — sharpen the cubic-to-quartic transfer

board_numbering: batch13
session: B13-04
model: Claude Fable 5.1 (configured model id `claude-fable-5-1`; the serving
model is not independently observable from inside the session and is recorded
as configured)
date: 2026-09-09, 11:10 America/New_York
base: `git rev-parse main` = `00495110c62acfbbbc951e82cc218ed091563b3f`
branch: `b13_04`
freeze check: `docs/batch13_board.md`, `docs/batch13_corrections.md`,
`docs/stocktake_batch12.md`, `docs/batch13_worker_preamble.md` all present in
the clone (451 / 141 / 181 / 212 lines).

## Preflight

| item | value |
|---|---|
| host | 2 CPU (Intel Xeon @ 2.80 GHz), 7 GB RAM, no swap, ~30 GB free disk; a shared cloud container, so this is the whole budget for the session |
| python | 3.11.15 |
| pre-installed | numpy 2.4.4, scipy 1.17.1 |
| installed here | python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0 (`pip install python-flint sympy numpy scipy`) |
| Singular / msolve | not checked; not needed by this session's plan |
| run bounds | every computation launched with `timeout` and `ulimit -v`, pid written to `results/logs/<run>.pid`; one heavy run at a time; `ulimit -v` at most 4 GB (the host has 7 GB total) |

## The two objectives this session serves

    1.  a positive multiplicity obstruction      D = mult_pad - mult_det > 0
    2.  permanent-specific equations             mult_pad < mult_red

B13-04 is about objective 2's mechanism: **when does a cubic ideal constituent
`S_ν ⊆ I(D_r^{f})_δ` actually produce an additional padded equation at a
quartic weight `λ`**, i.e. `mult_P(λ,δ) < mult_R(λ,δ)`.  Nothing here bears on
objective 1 directly; `docs/batch13_corrections.md` §1 governs.

## Questions

Q1 (theory).  Restate Proposition 8 of `docs/transfer_lemma.md` as an exact
criterion: express `mult_R(λ,δ) − mult_P(λ,δ)` as the dimension of the
intersection of the multiplication pullback's image with `Sym^δ V ⊗ I(D)_δ`,
and give it in a per-constituent form (a Pieri lift, or its fixed-factor
equivalent) that a brief can quote.  Relate it to S4's factorization
`rank T_pad = rank S − dim(S(M_λ) ∩ K)` (`results/astra/S4/S4_report.md`,
PROVED there) — this session does not claim that identity as new.

Q2 (converse).  Is Pieri compatibility plus `S_ν ⊆ I(D)_δ` sufficient for
`mult_P(λ,δ) < mult_R(λ,δ)`?  Expected answer: no.  Deliver a counterexample
with a proof, or a sufficient condition if none is found.

Q3 (audit).  Re-derive the horizontal-13-strip predecessors of
`λ₁₃ = (21,17,2⁷)` independently of `results/logs/wk12_int_pred13_audit.log`
(own enumerator; `a` by `tools/verify/pleth.py`; `N_S` by
`tools/verify/chi_build.weight_monomials_count`), and reconcile.

Q4 (quantifier).  State the length quantifier for predecessors once, precisely,
with the restriction lemma (`docs/washout_lemma.md` §1) and Theorem 2 (`k ≤ 5`)
as the rule for when a shorter predecessor may be ignored.

Q5 (price).  Price, for the next batch, what the sharpened criterion costs at
`λ₁₃` and what it does not buy.

## Instruments

- Hand proofs, checked by machine where the objects are small.
- A new, self-contained instrument `analysis/wk13_b04_model.py` (this session's
  own code; shares no code with `analysis/`): builds weight spaces of
  `Sym^δ(Sym^n C^r)` from exponent tuples keyed by tuple (never by list index —
  the two `exps` orderings in the repository are opposite), raising operators by
  the FORMAT.md rule `E_ij c_α = (α_i+1) c_{α+e_i−e_j}`, highest-weight spaces
  as exact rational kernels (`flint.fmpq_mat`), the multiplication pullback
  `μ*(q_β) = Σ_i ℓ_i c_{β−e_i}`, the fixed-factor restriction
  `ρ(h)(c) = h(x_1·c)`, evaluation at integer points, ranks exactly over `Q`
  (`fmpz_mat`/`fmpq_mat`) and modulo both house primes 2147483647 and
  2147483629 (`nmod_mat`).
- Cubic-ideal membership in the models is CERTIFIED by exact symbolic
  substitution `c = f(A·s)` with symbolic `A` (polynomial identity over `Z`),
  never inferred from evaluation.

## Objects

Model A ("triple root"): `r = 2`, cubic `f = x₁³`, `D = D_2^{x₁³}` = the
Veronese cone `{m³}`, `P = {ℓ·m³}`, `R = Sym⁴C²` (every binary quartic is
reducible), `δ = 2`, quartic weights `λ ∈ {(6,2), (4,4)}`, cubic constituent
`ν = (4,2)` (`I(D)_2 = S_{(4,2)}`, the 2×2 catalecticant minors).  Both weights
are Pieri-compatible with `ν`.  Prediction (from the hand computation done
before this file was written, to be confirmed by machine): gap 0 at `(6,2)`,
gap 1 at `(4,4)`.

Model B ("two-variable cubics"): `r = 3`, cubic `f = x₁³ + x₂³` in `N = 2`
variables, `D = D_3^{f} = Sub_2(Sym³C³)` (cubics depending on two linear
forms; its GL₂-orbit is dense in `Sym³C²`), `P = {ℓ·c : c ∈ Sub_2}`,
`R = {ℓ·c}`.  Degrees `δ = 3` and `δ = 4`.  Quartic weights: every `λ ⊢ 4δ`
with at most 3 parts and `a^{(4)}(λ,δ) > 0`.  Cubic weights: every `ν ⊢ 3δ`
with at most 3 parts and `a^{(3)}(ν,δ) > 0`.  For each `(λ,δ)`: `a^{(4)}`,
`mult_R` (three ways: fixed-factor rank over `Q`; reducible-point evaluation
over `Q`; both primes), `mult_P` (padded points `ℓ·f(A s)`, over `Q` and both
primes; and fixed-factor `h(x₁·f(As))`), `gap = mult_R − mult_P`; for each
`ν`: `a^{(3)}`, `i^{(3)}(ν,δ)` with certified kernel vectors; the Pieri
predecessor list; `Σ_ν i^{(3)}`; and the exact criterion value
`dim(ρ(H_λ) ∩ J^λ)` computed by linear algebra over `Q`.  The consistency
`gap = criterion` is a check of the theorem's implementation, not evidence for
the theorem.  Each Pieri-compatible pair `(ν, λ)` with `i^{(3)}(ν,δ) ≥ 1` is
classified as contributing or not.

Goal-cell numbers (no computation beyond plethysm and counting): the fifteen
predecessors of `λ₁₃`, their `a`, `N_S`, lengths; `Σ_ν a^{(3)}(ν,13)`;
`a^{(4)}(λ₁₃,13) = 39` (from `docs/rung13_reducible.md`, to be reproduced by
`tools/verify/pleth.py` if the DP box permits, else RECORDED from the log).

## Stopping rules

- Model A: unbounded in practice (seconds).  Model B: each degree launched
  with `timeout 1800` and `ulimit -v 4000000`; if `δ = 4` does not complete
  within the bound, report `δ = 3` only and price `δ = 4`.
- Symbolic membership certificates: `timeout 1800`; if a certificate does not
  finish, the corresponding `i^{(3)}` is reported as MEASURED (sampled) and the
  criterion value that depends on it is reported as conditional.
- No computation at the goal cell beyond plethysm coefficients and monomial
  counts.  The fifteen predecessor cells (`N_S` from `1.6·10⁷`) are not run
  here: above this host's budget and outside this session's mission.

## What counts as a negative, and what is not a result

- A Pieri-compatible pair with `i^{(3)}(ν,δ) ≥ 1` and gap 0 is a **negative for
  the converse** (the deliverable of Q2), reported with its exact certificate.
- Model B showing no such pair is a negative for finding a "generic-looking"
  counterexample there; Model A's counterexample stands on its own proof.
- A disagreement between the exact criterion and the direct measurement in a
  model is an **instrument defect**, to be found and fixed before anything is
  reported; it is never a result.
- Any discrepancy with the audit log's fifteen shapes, `a` or `N_S` values is
  reported as a discrepancy, with both values.
- Sampled ranks are floors: a deficient rank read at points bounds `i` from
  above and never proves `i ≥ 1`.  In the models every `i ≥ 1` claim carries an
  exact certificate; if it does not, it is labelled MEASURED.

## Labels

PROVED (hand proof, machine-confirmed where small) / CERTIFIED (exact over `Q`,
or full rank at one house prime) / MEASURED (sampled, two primes) / ADOPTED
(from the repository's proved documents, cited) / RECORDED (reproduced from a
log without independent re-derivation).

Anything not listed above is exploratory and will be labelled so.

---

## Addendum 1 — 2026-09-09, 20:50 America/New_York (committed before the measurements it governs)

**Why.** The session deadline was extended by two hours.  Two things in the
first pass are worth pushing on, and one is a check I owe the report.

**Change of model, recorded.**  Sessions B13-04's first pass (everything
committed through `2b89394`) ran as **Claude Fable 5.1**.  The session then
reached a model-availability limit and was continued as **Claude Opus 5**
(`claude-opus-5`).  Both are recorded in the report and in the commit
trailers of the parts each produced; no earlier result is restated as Opus's
or as Fable's.

**Q6 — is the swap identity sufficient?**  Lemma F gives a necessary condition
for a weight-`λ⁻` vector `F` to be `ρ(h)` for some quartic highest-weight
vector `h`.  Define

    T^λ  =  { F of weight λ⁻, killed by E_{i,i+1} for i ≥ 2  :
              F(ℓ·q) = F( u_ℓ^{-1}(x₁·q) )  for every ℓ with ℓ₁ = 1
              and every quadric q }.

`ρ(H_λ) ⊆ T^λ` by Lemma F.  Question: is `T^λ = ρ(H_λ)`?  Instrument: the
swap conditions are linear in `F`, so `T^λ` is computed as an exact kernel over
`Q` (`fmpz_mat`) from integer `(ℓ,q)` pairs, saturated (conditions added until
the kernel dimension is stable over at least 20 further pairs and confirmed at
both house primes).  Reported quantities per cell: `dim T^λ`, `mult_R = dim
ρ(H_λ)`, `dim B^λ = Σ_ν a⁽³⁾`, and the dimension of the full `GL_{r−1}`-highest
weight-`λ⁻` space.  **A negative is a cell with `ρ(H_λ) ⊊ T^λ`** — the swap
identity is then strictly weaker than descent, and the excess dimension is the
result.  Equality in every cell is evidence for a conjecture and is labelled
MEASURED, never PROVED; the conjecture is stated as such.

**Q7 — Model D, `r = 4`, for the length quantifier.**  `f = x₁³`
(`D = {m³}`, the Veronese cone) at `r = 4`, `δ = 2` and `δ = 3`, and
`f = x₁³ + x₂³` at `r = 4`, `δ = 3` if it completes inside the bound.  Purpose:
exercise predecessors of length `r − 1` (`μ_r = 0`) alongside length `r` ones
in the same cell, and check operationally that a shorter predecessor carries a
channel of the stated dimension and can contribute.  Same measurements as
Models A–C, plus, per cell, the split of `Σ_ν a⁽³⁾` and `Σ_ν i⁽³⁾` by
predecessor length.

**Q8 — Model B at `δ = 6`,** if it completes inside the run bound.

**Q9 — an independent `a` check.**  For every model cell, `a⁽⁴⁾` and `a⁽³⁾` as
read from the exact highest-weight kernels are compared against the Kostant
alternation of `analysis/wk13_b04_pred13.kostant` (a different formula on a
different data structure).  A disagreement is an instrument defect and halts
the affected model.

**Stopping rules for the addendum.**  Each run bounded with `timeout 2400` and
`ulimit -v 4000000`, pid recorded.  Model D at `δ = 3` and Model B at `δ = 6`
are dropped, and priced, if they do not complete.  Nothing in this addendum
touches the goal cell; the exclusion of the fifteen predecessor cells stands.

**Labels.**  Unchanged.  Everything in this addendum is pre-registered from
this point; results already committed are unaffected.
