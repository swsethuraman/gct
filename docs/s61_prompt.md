# Session 61 — the full polar profile of `per_3`, and a verdict on the microlocal branch

One bounded computation with a decision attached.  It is the only concrete new
calculation to come out of the five external reviews, and it either finds a
second conormal signal or retires the branch permanently.

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

## 1. The determinant's profile, and the one slot that separates

For `X_det = {det_4 = 0} ⊂ P^15` the dual is the Segre `P^3 × P^3`, so the
conormal multidegrees are

    (δ_0, …, δ_6) = (4, 12, 36, 68, 84, 60, 20),      δ_k = 0 for k ≥ 7.

Both endpoints check: `δ_0 = deg det_4 = 4`, `δ_6 = deg(P^3×P^3) = C(6,3) = 20`.
The vanishing `δ_7(det_4) = 0` is the key fact — it is exactly
`dim X^∨_det = 6`.

The padded permanent has `dim(dual) = 7` (s50, by Katz; the integrator upgraded
that from six sampled points to the identity
`det H_P = −(3/2)·x_0^8·per_3·det H_{per_3}`, so the rank drop on `{per_3 = 0}`
is a closed form).  Hence `δ_7 > 0` for the pad and `= 0` for the determinant,
and that separates.

**But that separation is the LMR dual-defect condition again** —
`δ_7 > 0 ⟺ dim X^∨ ≥ 7`, whose complementary closed locus is what LMR's
degree-24 equations cut out.  Nothing new.

## 2. The question this session answers

> Is the dual-dimension slot the **only** place the permanent's conormal exceeds
> the determinant's, or does some lower slot `k ≤ 6` also violate?

Compute the full profile of the `3×3` permanent cubic `per_3 ⊂ P^8`:

    (δ_0, δ_1, …, δ_7)

and compare componentwise against `(4, 12, 36, 68, 84, 60, 20, 0)`.

**If some `k ≤ 6` violates** — say `δ_5 ≫ 60` or `δ_6 > 20` — there is a
conormal inequality independent of dual defect.  That is worth having, because
it might algebraize differently from LMR's degree-24 module, and degree is the
programme's binding constraint.

**If every lower slot satisfies the determinant bound and only `δ_7` differs**,
then the entire microlocal signal at `(3,4)` collapses to the dual defect we
already have.  **Park the branch** and say so — a clean retirement with a reason
is a good outcome for a bounded run.

## 3. Method and calibration

Saturated polar ideals over a finite field: impose generic linear conditions on
the gradient, saturate away from the singular locus, count the zero-dimensional
fibre.  Several primes, several patches, several random coefficient choices.

**Calibrate first on the determinant**, where every entry is known
independently from the Segre description: reproduce `(4,12,36,68,84,60,20)` and
`δ_7 = 0` before trusting any permanent value.  If the method cannot reproduce a
profile we know in closed form, its permanent numbers mean nothing.

An external review reports `δ_7(per_3) = 6`, obtained across four independent
prime/patch/coefficient choices and labelled a strong computational measurement
rather than a characteristic-zero proof.  **Treat that as a target to
reproduce or refute, not as an input.**

## 4. A citation you must not build on

The external session that proposed this run cites two June 2026 preprints by
Sheshadri (arXiv:2606.13628 and 2606.15970) for a conormal specialization
theorem.  **The integrator has failed to locate either across six attempts** —
four keyword searches, two direct `arxiv.org/abs/` fetches that returned no
title, author or abstract, and an exact-identifier search — while the *same*
tooling successfully read arXiv:1004.4802 and arXiv:1512.02437 in the same
sessions.  Non-existence cannot be proved, but the evidence is substantial.

**Requirement:** this session's conclusions must not depend on those papers.
The `δ_7` separation stands on LMR's dual-defect result, which is independently
established.  If you locate the preprints, record the identifier and a quoted
theorem statement; if you do not, proceed without them and say so.  Do not cite
a paper you have not read.

## 5. Scope discipline

This is **one bounded run**, not the opening of a microlocal programme.  Do not
develop characteristic-cycle machinery, vanishing cycles, or a general
specialization theory.  Compute eight numbers, compare them to eight numbers,
and give a verdict.

## 6. Success

**Success:** the determinant profile reproduced as calibration, and the
permanent profile computed with the primes, patches and saturation recorded.

**Best outcome:** a slot `k ≤ 6` where the permanent exceeds the determinant —
a conormal signal independent of dual defect, with an estimate of what degree
its algebraization would sit at.

**Equally good outcome:** every lower slot clean, so the branch retires with a
reason rather than by neglect.

## 7. Report

`docs/s61_report.md` with both eight-entry profiles side by side, the
calibration, and the verdict.  Deliver as a bundle.
