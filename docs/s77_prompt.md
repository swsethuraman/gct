# Session 77 — the deterministic basis: the bridge first, then straightening

*(the reconciled proposal's s76.  Read the preamble first.)*

## What S1 established, and what it retired

**Retired, and narrowly:** unrestricted Plücker expansion as the route to the
goal-cell basis.  Every one of the 113 saved fillings exceeded a deliberately
small 64-term cap under the specified reducer — but that is not the reason.  The
reason is that **there is no independence theorem after the umbral contraction
and identical-letter symmetrization**.  A larger cap does not revive the route; a
triangularity theorem does.  Do not re-run unrestricted expansion.  Do not treat
the adjacent question as retired with it.

**Banked, and they are your tools:**

- column antisymmetry and the repeated-letter zero;
- identical-letter relabeling and whole-column permutation;
- pure-`u` removal: a letter in only its `n` singleton columns gives
  `F_T = n! u F_deleted`;
- a proved unshared-column vanishing test: tall columns sharing `k` letters with
  `h − k > n` force `F_T = 0`, so `k < 5` at `n = 4, h = 9`.  It does **not**
  prove the stronger empirical `k ≤ 4` at `n = 3`, and authorizes deleting no
  further overlap sector;
- the short-column Plücker rule `[a b][c d] = [a d][c b] − [a c][d b]` with the
  strictly decreasing energy `E(T) = Σ_{short (a,b)} (b − a)²`, which terminates.

Note the tension worth resolving early: the proved bound is `k < 5` at `n = 4`,
and the `δ = 24` birth representative found by the integrator has `k = 9`.
Reconcile the two statements before you use either — one of them is about a
different quantity or a different convention, and finding out which is cheap and
load-bearing.

## The mission, in this order

**First, the bridge.**  An explicit map

    S5 Pieri state  ⟶  s69 bracket filling

so that a deterministic basis from the recursion is evaluable through the fast
circuit oracle.  This is the composition of batch 11's two results, and it is the
answer to the recursion route's real risk — that it returns vectors which cannot
be paired with determinant points.  S1 is explicit that the abstract conversion
`x = y A^{-1}` from an existing invertible evaluation matrix is a
*post-construction* conversion and circular as a basis-selection algorithm.  What
is wanted is a canonical filling attached to a Pieri path, with explicit
treatment of tall-column overlap, and no coordinate expansion.

**Controls, both mandatory:**

- `n = 3` LMR cell: reproduce the six-dimensional source and the exact banked
  determinant ideal line (`results/artefacts/s69_banked_n3_d12.json`, 17,047
  coordinates).
- `n = 4, δ = 12`: reproduce the two-dimensional source and its determinant-full
  evaluation.

**Second, and only after the bridge has been tried**, straightening against the
residue: structured fillings, tall-column overlap, ladder birth channels,
pivoting.  Use the birth quotient — testing is now against `b_d`, not `a_d`
(`docs/batch12_s1_s2_consolidated.md` §1, and `analysis/wk12_int_birth_probe.py`
for a working example).

## What "better" means here, quantitatively

Discovery is no longer the binding constraint: the integrator filled the birth
ranks at `δ = 20, 21, 22, 23` in about two minutes on fresh random streams, and
at `δ = 14` every filtered draw raised the rank.  So a deterministic basis is
worth having for *assembly and certification*, not for rescuing a stalled search.
Measure against that baseline, not against the historical 12–15 CPU-hour
estimate, which came from a different host and an unfinished run.

## Success

A deterministic or near-deterministic construction whose circuit evaluations span
the two control sources exactly, and a measured comparison against the birth-quotient
random stream on at least two rungs of the `n = 4` ladder.

## Stopping rules

- The change of basis provably requires carrier-sized intermediate expansion:
  state it cleanly, identify what structure survives, stop.
- No canonical basis map exists: deliver instead a birth-channel-informed
  sampling distribution and the measured reduction in draws per accepted class,
  against the baseline above.

## Deliverables

`results/PREREG_s77.md`; the map or the characterised obstruction; both controls
reproduced; the measured comparison; `docs/s77_report.md`.
