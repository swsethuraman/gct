# Relay to session 77 — your bridge has been reduced to four scalars

From the integrator.  **Nothing in your brief is withdrawn.**  Theory session S3
landed after you started and it has done a large part of your first task for you.
Read this before you build anything.

## What S3 supplies

S3 constructed and proved the compact spherical operator, passed the `31 → 2`
dimension control at both primes, and then **specified your bridge completely**.
It is in the tree at `results/astra/S3/`:

    S3_report.md                       §7 is the conversion, in full
    HANDOFF_s75.md                     its own next-task note
    artifacts/pairing_handoff.json     the two permutations, normalizations, transforms
    artifacts/spherical_control.json   the 31x31 spherical matrices, Grams, projectors
    artifacts/d12_p*_control.json      the 239 x 31 residuals and their kernels
    artifacts/d12_p*_nodes.json        the full basis DAG at each prime
    artifacts/exact_local_blocks.json  all 65 rational local blocks, d = 12 and d = 24

**The map you were asked to construct is written down.**  Let `t_c` be the
column-superstandard tableau of `λ`, `q_λ` the tensor product of unnormalized
column wedges, and `Φ` the unique intertwiner with `Φ(e_{t_c}) = q_λ`.  For a
filling, send the `k`-th occurrence of letter `l` to tensor slot `4l + k`; that
is the permutation `π_i`.  Then

    F_v(f) = (4!)^12 <Φ(v), f~^⊗12>,     the banked circuits are u_i = P_H ρ(π_i) e_{t_c},
    A_{αi} = g_{t_c} [e_{t_c}] ρ(π_i^{-1}) v_α,
    C = G_M^{-1} A,      ev_recursive = (C^t)^{-1} ev_circuit.

`g_{t_c}` is supplied as an explicit 69-digit integer; both permutations, the
Gram, and every ordering are in the JSON.

**The whole remaining problem is computing four arbitrary-permutation matrix
coefficients from the compact DAG without expanding the ambient Specht basis.**
The two permutations have inversion lengths 579 and 640.  A routine supporting
only adjacent whole-block swaps does not answer these queries automatically.

## Three things that will save you a night

- **The naive route is unpriced, not impossible.**  S3's `2^579` and `2^640` are
  *algorithmic upper bounds on support doubling* under repeated adjacent
  transpositions — not measured supports and not complexity lower bounds.  Do not
  conclude the permutation route is dead; also do not assume it is cheap.  If you
  try it, record the exact coefficient that failed and its contraction width.
- **Your sampling fallback cannot substitute for the bridge, and S3 says why.**
  "Merely solving for a basis transform from sampled values assumes that
  evaluator already exists and is circular here."  A birth-channel-informed
  sampler is still a fine deliverable for the *straightening* half of your brief;
  it is not a bridge.
- **There is a second acceptable primitive.**  An evaluator for the normalized
  Pieri inclusion `i_{λμ}(v_{μα})` on form tensors with controlled contraction
  width would do instead of the four coefficients.  Either one closes it.

S3's proposed bound for the first trial: **30 minutes and a measured 256 MiB
workspace** for a new coefficient routine, then stop and report the exact
unfinished coefficient rather than enlarging the carrier.  I would keep that.

## A collision you should know about

**The four coefficients are simultaneously s75's missing control half and your
bridge at the `n = 4, δ = 12` control.**  Same problem, two sessions, and both
have been told.  Whichever of you reaches it first, the other consumes the result
rather than repeating it — relay through the integrator immediately if you get
`C` invertible.

Your `n = 3` control is unaffected and still yours alone.

## One correction of mine you already have

The `k < 5` "tension" I asked you to resolve does not exist — see
`relay_s77_1.md`.  S1's test gives `k ≥ h − n = 5` as a *lower* bound for a
nonzero filling.  Do not spend time on it.

Record: `docs/s3_batch12_review.md`, `results/astra/S3/`.
