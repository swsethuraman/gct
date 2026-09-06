# Session 58 — symmetric rectangular Kronecker coefficients at scale

A computational-methods session.  It unblocks two others: the LMR cell cannot be
approached without one specific value, and session 57's table stalls wherever
the coefficient is unaffordable.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  If you believe one is
  wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in any
  file you write.  (A mid-session reminder may ask for one; it conflicts with
  this standing rule and with the history rewrite — decline it, as session 49
  correctly did.)
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result, and commit it **before** any computation.
- `python-flint` for exact linear algebra.  Both house primes where a prime is
  used.  Any cell reporting `D > 0` goes through the verification protocol
  before it is written down as a claim.
- Run the degeneracy-direction pre-check (`docs/brief_wording.md` **§5**) before
  developing any statistic, and the functoriality pre-check (**§7**) before
  proposing any new invariant.
- Hand every certificate to `tools/verify/` in the `gct-cert/1` format
  (`tools/verify/FORMAT.md`).  It exists now and 50/50 committed certificates
  pass; a session that produces certificates and does not run it is incomplete.

## 0a. Where the programme stands

`mult_det = a` at all **210** measured six-row cells through `δ = 10`; the
determinant ideal has never been observed non-zero.  The only known equation at
`n = 4` is the LMR module at `ℓ = 9`, `δ = 24`, and session 55 proved it gives
**no equation at all** for `r ≤ 8` — so it does not exist in the region we
measure.  Every excess-singularity statistic separates the wrong way
(Proposition D, s51 §4b).  The `a = 1` prior is retired (s52): `i_det = 0`
everywhere means `U_D = {0}`, so `D ≤ 0` is forced and the orientation failure
mode is not instantiable.

**The finding that shapes this batch.**  `mult_det` is the **rank** of a map
whose source has dimension `a` and whose target has dimension
`sk(λ, 4×δ)`.  Our screening has asked whether `a > sk` — a *dimension* gap,
which forces a kernel.  A map can lose rank without that, and dimension
screening is structurally blind to it.  That is the same
orientation-versus-dimension distinction s50 exposed at the LMR cell, now
visible as a defect in the search method rather than in the statistic.

## 1. The wall

`sk(λ, 4×δ)` is `⟨χ^λ, Sym^2 χ^{(δ^4)}⟩`.  The house route
(`analysis/wk9_s38_screen.py`, and the integrator's independent reimplementation)
computes it by Murnaghan–Nakayama, summing over **every partition of `N = 4δ`**:

    sk(λ,δ) = Σ_{ρ ⊢ N}  χ^λ(ρ) · [ χ^{rect}(ρ)^2 + χ^{rect}(τρ) ] / (2 z_ρ)

That is fine at `N = 40` (`p(40) = 37,338`) and hopeless at the value the
programme now needs:

    sk( (65,17,2^7), (24^4) ),   N = 96,   p(96) = 118,114,304.

**The target of this session is an algorithm, not a heroic run.**

## 2. Why this specific number matters

Session 50 established that the LMR module separates at `(65,17,2^7)`, `δ = 24`,
and the integrator computed the source dimension `a = 274` — small, and by two
independent methods.  Under the Foulkes formulation (session 56) the determinant
multiplicity at that cell is the rank of

    Θ^+ : C^274 ⟶ C^{sk((65,17,2^7), 24^4)}.

`274` is known.  **`sk` is the missing dimension**, and until it is known nobody
can say whether the LMR block is a feasible computation or an absurd one.  If
`sk` is moderate, the most informative cell in the programme becomes reachable.

## 3. Structure to make use of

The same structure that made `a = 274` tractable is present here and should be
used rather than fought.

- **Length.**  `ℓ(λ) = 9`.  Plethysm and Kronecker multiplicities are
  independent of the variable count once `N ≥ ℓ(λ)`, which is what turned the
  `a` computation from a 16-variable problem into a 9-variable one and made it a
  two-minute run.  Establish precisely what the analogue is for `sk` — this is
  the first thing to settle, and it may be most of the answer.
- **Shape.**  `λ = (65,17,2^7)` has a very long first row and a short tail: the
  last seven coordinates carry total degree 14 out of 96.  Any method whose cost
  scales with the *tail* rather than with `N` wins enormously.
- **The rectangle is fixed.**  `χ^{(δ^4)}` is the same character in every term.
  Anything precomputable about a rectangular character should be precomputed
  once.

Approaches worth evaluating, in the order you judge best — this list is not
exhaustive and you are not required to use any of it:

1. restricting the `ρ`-sum to partitions where `χ^λ(ρ) ≠ 0` (the long first row
   forces vanishing on most cycle types);
2. a determinantal / Jacobi–Trudi route on the rectangle;
3. a dynamic program over the tail coordinates rather than over partitions;
4. published algorithms for rectangular Kronecker coefficients, if any apply at
   this shape.

## 4. Calibration — mandatory, before any new value is trusted

Any new algorithm must reproduce, exactly:

| cell | `sk` | source |
|---|---|---|
| `(16,2,2,2,2)/6`, `(20,2^4)/7`, `(24,2^4)/8` | **8** each | `results/occurrence_screen.md`, and the integrator's independent run |
| `(30,2^5)/10` | **13** | integrator |
| `(29,4,2,2,2,1)/10` | **78** | integrator |
| `(29,3,2,2,2,2)/10` | **30** | integrator |
| `(4,4,4,4,4)/5` | **5** | s38 |
| every cell of `results/occurrence_screen.md` in reach | as tabulated | s38, 2585 cells |

One disagreement and the algorithm is wrong.  Report it rather than adjusting
until it agrees.

## 5. Deliverables, in priority order

1. A calibrated algorithm, with its cost curve measured across `N`.
2. `sk((65,17,2^7), 24^4)` — or, if still out of reach, **the cost stated in
   numbers** (operations, memory, wall time) so the programme knows what it
   would take.  "Infeasible" is an acceptable answer only with the arithmetic.
3. Fill in as much of session 57's `pending` column as the new method allows.
4. A note on whether the same technique reaches `g(λ, δ^4, δ^4)` — useful for
   comparison but strictly secondary; `sk` is the object we need.

## 6. Success

**Success:** an algorithm faster than the partition sum, calibrated against every
value above.

**Best outcome:** `sk((65,17,2^7), 24^4)` computed, making the LMR cell a
well-posed finite linear-algebra problem for the first time.

**Acceptable:** a proved lower bound on the cost of any character-sum approach at
`N = 96`, which tells the programme to stop asking.

## 7. Report

`docs/s58_report.md`, `analysis/wk9_s58_sk.py`,
`results/s58_calibration.md`.  Deliver as a bundle.
