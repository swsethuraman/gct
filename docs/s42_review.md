# Integrator review — session 42 (the reducible-locus multiplicity engine)

2026-09-03.  Branch `s42-redengine`, delivered head `bd6ebc2` (13 commits on
`5aa564b`; pre-registration `bb406e0` before any measurement).  Single-writer
files untouched; nothing over 5 MB added (the three 12–13 MB files at the tip
are s36's, already in the repository — the limit was broken in session 36 and
I missed it there).  I audited the checkpoint bundle in depth on 2026-09-02;
this review carries those checks forward and adds the delta.

## 1. What was verified

- **`h_pad` and `a`, rebuilt independently.**  My own cubic-plethysm DP
  (self-tested on `Sym^3(Sym^3 C^3)` and a dimension count of
  `Sym^4(Sym^3 C^4)`) reproduces `a` and `h_pad` at every cell I tried: the
  five s36 bites, four ordinary cells, the four smallest claimed negative
  instances of Kadish–Landsberg Question 1.5, both new degree-8 generators,
  and all 37 rows of s41's ledger.  The bound `mult_red ≤ min(a, h_pad)` holds
  at every one; no violations.
- **The bound itself is sound.**  `C[R_r]_δ ≅ im(μ*_δ) ⊆ Sym^δ V ⊗ Sym^δ Sym^3 V`
  equivariantly, and that target is KL's normalisation (Prop. 1.8).  I fetched
  the paper: Question 1.5 asks whether every `S_π W` occurring in `S^d(S^n W)`
  with `p_1 ≥ d(n−m)` has some copy in `C[F_{n−m}(S^n W^*)]`.  At
  `(n,m) = (4,3)`, `d = 7`, the cell `(7,4,4,4,4,4,1)` has `a = 1`,
  `p_1 = 7 = d(n−m)`, and `h_pad = 0` — so `mult_red = 0`, a negative instance,
  proved by KL's own proposition plus one plethysm coefficient.  Wording for
  paper 2: "we are not aware of a previous instance", not "the first known".
- **Every exact certificate audited.**  I expanded each integer highest-weight
  vector to monomials and checked, with my own code: weight, (★) on every
  monomial, the simple raising operators over ℤ, vanishing at true
  padded-permanent points, non-vanishing at determinant pencils and at a
  generic quartic.  All pass.  Structure worth recording: `(8,4,4,4,4)_6` is
  `c·I_5` and `(12,4,4,4,4)_7` is `c²·I_5` — identical coefficients after
  stripping the top coordinate — so the two five-row bites are propagations of
  the degree-5 invariant, which has 19,834 monomials and largest coefficient
  41,472.
- **The lift tool works on another session's cell.**  I ran
  `wk9_s42_lift.py` at s41's bite `(13,10,6,1,1,1)_8`: 117 s, one integer
  vector, max coefficient 1,280, `E v = 0` over ℤ, proportional mod `P1` to
  s41's mod-`p` vector.  That upgraded s41's `D = −1` there from measured to
  proved, and is the first time one session's engine closed another's open
  certificate.
- **The two new minimal generators.**  `(13,12,4,1,1,1)_8` (`a = 3`,
  `mult_red = 2`) and `(13,10,6,1,1,1)_8` (`a = 9`, `mult_red = 8`).  I
  re-derived `a` at both, enumerated the Pieri predecessors myself (24 and 15;
  22 and 9 of them actually occur), and confirmed each occurring predecessor is
  banked at degree 7 with `mult_red = a` — three of them in s36's red table
  rather than s42's own files, which is legitimate: for `ℓ(λ) = 5` the
  multiplicity is independent of `r ≥ 5` (a weight-`λ` monomial has every
  `α_6 = 0`, `E_{5,6}` acts as zero, and index 6 is unconstrained in (★)).
  **The minimal-generator argument checks out at both cells.**  Both have
  `h_pad = a`, so neither is visible to the normalisation bound — the lift is
  the only route to them.
- **Records.**  201 reached cells across three sweep files plus 11 generator-check
  cells; no duplicates; both primes agree everywhere; 48 s36 validation cells
  reproduced with dense = sparse wherever both ran.

## 2. What the session establishes

The pad side of the obstruction question at `n = 4` is finished as a research
problem.  It is a lookup at every reached cell, a proved bound `min(a, h_pad)`
at *every* cell of the region including unreachable ones, and zero outright at
162 cells.  Since `mult_pad ≤ mult_red` always, and `mult_det = a` at every
cell ever measured, `D ≤ 0` follows without any pad computation wherever the
determinant ideal is empty.  Everything now turns on one number: the degree at
which `I(D_6^{det_4})` becomes nonzero.

Three results are publishable independently of the obstruction search: the
normalisation bound as a screen, the negative answer to KL Question 1.5, and
the two new minimal generators of `I(R_6)` in degree 8.

## 3. Wording and small corrections for the write-up

- "the obstruction hunt at n=4" in §G and the title's framing go to the house
  vocabulary of `docs/brief_wording.md`; "Kills by PID only" in §F likewise.
- `analysis/wk9_s36_sweep.py` and `analysis/wk9_s42_*.py` hard-code a session
  URL into their commit calls.  These must be scrubbed before the repository
  goes public — the pattern is now forbidden by `docs/brief_wording.md` §4.
- "the first known" → "we are not aware of a previous instance", at both the
  KL instance and the generators.
- The det-side certificate of §7 is the successor task; it is session 45's
  brief, written tonight.

## 4. Process

Pre-registration before measurement; the engine validated against 48 banked
cells and 200 synthetic matrices before use; one-sided certificates used
correctly throughout (a mod-`p` nullity of 0 is a proof; a nullity `k > 0` is
promoted only by an exhibited integer vector); Route B closed with a theorem
rather than abandoned; the literature verdict is per-claim and honest, including
the parts that were already known.  Two container resets and one out-of-memory
event survived losslessly by per-cell banking.  This is the strongest-run
session of the programme so far.
