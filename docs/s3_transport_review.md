# The `u`-transport, verified — and S3's δ=13 conversion

The reasoning side asked for one thing explicitly: *"With the established
multiplication-by-`u` transport and its determinant-side injectivity, the
certificate should raise our degree-24 determinant lower bound from 2 to 39.
We should explicitly verify that transport when reviewing the package."*  This
is that verification.  `analysis/wk12_int_transport_check.py`, **20 of 20
checks pass**, and it is independent of anything S1 or S3 computed.

## 1. The mechanism, derived here before reading how it was implemented

Evaluation at a point is a ring homomorphism, so `(u^k w)(P) = u(P)^k · w(P)`.
The transported matrix is therefore the base matrix with **column `j` scaled by
`u(P_j)^k`**, and the transported minor is the base minor times `∏_j u(P_j)^k`.
Two consequences:

- **The transport of a rank floor is unconditional.**  It needs neither
  primality of the ideal nor `u ∉ I` — only that no sampled point is a `u`-zero.
  Any nonzero `k×k` minor at rung `d` becomes a nonzero `k×k` minor at rung 24.
- **`u`-zeros are the one hazard.**  A point with `u(P) = 0` voids every
  transported row in its column silently.  At a determinant point
  `u(P) = det A₁`; at a padded point `u(P) = ℓ₁ · per B₁`.  Both are generic
  but neither is automatic, so they must be recorded per point, not assumed.

The prime-ideal proposition is what makes the transport **exact** rather than a
floor: `ker T_X ∩ u^k M_{d−k} = u^k(I(X) ∩ M_{d−k})`, so
`rank T_X|_{u^k M_{d−k}} = a_{d−k} − i_X(d−k)`.  The multi-step version follows
from the one-step version by primality applied `k` times, and `u^k M_{d−k} ⊆ M_d`
holds in degree (`k + (d−k) = d`), in weight (`λ_{d−k} + k·(4,0,…,0) = λ_d`) and
in highest-weight-ness (`E_{ij}(u^k w) = u^k E_{ij}(w)`, since `E_{ij}u = 0`).
All three checked.

## 2. S1's banked artefact reproduces exactly

`results/astra/S1/transported_det_lower_bound_2.json` records a 2×2 matrix and
its determinant at each prime, with `u_values = [1193, 196]` at points S1 did not
deliver.  I could not replay it from the points, so I recovered the base matrix
by dividing the scaling back out — and it is **s1's own `4_det_<p>` control
matrix, entry for entry, at both primes**, with the determinant equal to the
base minor times `∏ u_j^12`.  So:

- the recorded matrix **is** `base · diag(u^12)`, unnormalised, at both primes;
- the recorded determinant **is** `base minor × ∏_j u_j^12`, at both primes;
- the base minor agrees with S1's own recorded control minor;
- neither seed point is a `u`-zero.

**Delivery gap, recorded not as an error but as a standard:** the artefact is not
replayable from what was delivered, because the two points it used are not in the
package.  Any transported certificate must ship its points, or the seed and the
generator that made them.

## 3. The same bound from the repository's own data

Independently of S1: `results/s69_n4_seed.json` carries twelve integer
determinant pencils.  `u(P) = det A₁` is nonzero at all twelve, recomputed
exactly over `Z`, and the 2×2 determinant minor is nonzero at both primes
(`1361963321`, `596224962`).  So `rank T_det(24) ≥ 2` reproduces from the
repository alone.

## 4. S3's δ=13 conversion

The claim: a complete 39-dimensional conversion at rung 13 with generic and
determinant rank 39 at both primes, hence `i_det(13) = 0`, hence
`rank T_det(24) ≥ 39`.

- **`a₁₃ = 39` re-derived from a cold cache** by my own Weyl-alternation census
  (`wk9_s42_census.a_weyl`), not read from `results/s63_aladder.json`:
  `a₁₂ = 2`, `a₁₃ = 39`, `a₁₄ = 93`, births 37 and 54 — the banked profile.
  `results/logs/wk12_int_fresh_a13.log`.
- **The report's own arithmetic is coherent**: `6,084 = 4 × 39²` — two matrices
  (generic, determinant) at two primes on a 39×39 grid.
- **`rank T_det(13) = 39` forces `rank_generic = 39`**, since the determinant
  orbit sits inside the ambient and a smaller sampled generic rank would be
  inconsistent.  The generic column is therefore a control, not an independent
  input.
- **The lower bound needs less than the report claims.**  `rank T_det(24) ≥ 39`
  needs only 39 vectors in `M₁₃`, a nonzero 39×39 determinant minor at one
  prime, and no `u`-zero among those points.  `a₁₃ = 39` and primality are
  needed only for the *stronger* statement `i_det(13) = 0`.
- Sampling is on the safe side here: a nonzero minor is a rank floor, so
  `i_det(13) ≤ 0`, and `a₁₃ = 39` closes it to `= 0`.

**Verdict: sound, and the machinery is what matters more than the number.**

## 5. Superseded, and by what

Session 74's complete 274-row source gives `rank T_det` on the **transported
δ=23 rows** equal to 273 at both primes, so `i_det(23) = 0` and — with `b₂₄ = 1`
and LMR — `i_det(24) = 1` exactly.  The determinant column is closed.  S3's 39
is the same argument nine rungs lower, and it is now a rung of a ladder whose top
has been reached rather than the frontier.

What is *not* superseded is the transport itself.  It is the reason the
determinant column closed without a single δ=24 candidate, and it is the reason
`ε_pad = 0` is provable from s74's data (`docs/s74_checkpoint_review.md` §4).
The exact statement `rank T_X|_{uM₂₃} = 273 − i_X(23)` is now load-bearing on
both sides of the programme.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
