# Pre-registration — session 41: the six-row frontier

Written **before any measurement**.  Branch `s41-sixrow`, 2026-09-02.
Brief: `docs/s41_prompt.md` (committed verbatim in this clone).

**Clone state.**  Tip `5aa564b` (paper-1 bracket patch + paper-2 draft);
ancestry gate `git merge-base --is-ancestor 5aa564b HEAD` passes;
`docs/s40_review.md` and `analysis/wk9_s36_stabred.py` present.  No
session-41 collision (`git log --all`, filename sweep of `docs/`, `results/`,
`analysis/`).  Session 39 has not landed (only `docs/s39_prompt.md` exists);
nothing here depends on it.

**Engineering.**  Container: 7 GB RAM (~6.5 usable), 2 cores, `python-flint`
0.9.0, `nmod_mat` for every rank and nullspace, house primes
`(2147483647, 2147483629)`; no hand-rolled elimination.  Logs under
`results/logs/`; per-cell pickles in `/root/s41/` (not committed); anything
committed stays under 5 MB.  Multi-worker only via the claim queue of
`analysis/wk8_s30_run62c.py` (`O_CREAT|O_EXCL` claims, PID-owned, a claim
released only when its owner is dead; the memory guard waits, never skips;
kill by explicit PID after read-back, never `pkill -f`).

**Convention (verbatim from `docs/s34_prompt.md`, so it cannot drift).**
`D := mult_pad − mult_det`.  An obstruction is `D > 0` — the padded permanent
strictly exceeding the determinant at a weight.  `D < 0` (the pad side biting
first) is the *expected* direction — pad's variety is smaller (`55 < 66` at
`r = 6`), so its ideal should switch on earlier — and it is **not** an
obstruction.  A `D < 0` cell cannot be upgraded into a claim it is not.  Only
`D > 0` triggers the protocol of §5.

## 0. What is inherited and used (all proved or measured elsewhere)

- `D > 0` needs `mult_det < a`, since `mult_pad ≤ a` always.  The six-row
  determinant ideal is empty (`mult_det = a`) at every reachable cell of
  `δ = 6, 7` (s36: 34 cells with `a ≥ 2`, 24 cells with `a = 1`).  So the
  first job is the **six-row onset**: the first `(λ, δ)` with `ℓ(λ) = 6` and
  `mult_det(λ, δ) < a(λ, δ)`.
- Obstruction cells need `λ_1 ≥ δ` (Corollary B of `docs/reducible_ideal.md`),
  `6 ≤ ℓ(λ) ≤ 10`, and `a ≥ 1` (BIP is silent at `(3,4)`, `docs/s37_review.md`
  §2b).  The onset itself is not restricted by `λ_1 ≥ δ`; the census lists the
  `λ_1 < δ` cells separately (they are balanced and, as will be seen, out of
  reach).
- The permanent enters only at `ℓ ≥ 6`, `δ ≥ 7` (washout + Pieri delay);
  at `r = 6`, `mult_pad ≤ mult_red` with a strict gap iff a permanent-specific
  equation exists, and by Prop. 8 of `docs/transfer_lemma.md` such a gap at
  degree `δ` requires `I(D_6^{per_3})_δ ≠ 0` inside `C[Sym^3 C^6]`.
- Pad points are true padded-permanent restrictions `l(s)·per_3(A(s))`
  (`per_padded(3,4)` through `restrict()`), never `l·(random cubic)`.
- The pipeline is `analysis/wk9_s36_stabred.py` (the stabiliser reduction,
  lemma proved in `docs/stabiliser_reduction.md` §1, validated in
  `results/stabred_validation.md`), used unchanged; the point-free `mult_red`
  is `analysis/wk9_s36_red.py` (criterion (★), a theorem in
  `docs/reducible_ideal.md`).

## 1. Sizes, the frontier, and one engineering addition (stated before use)

**Memory model, inherited.**  s36 measured the resident set while the
compressed matrix is assembled at `~1.7e-8·n_χ²` GB and the *peak* inside
flint's `nullspace` at `~2.4e-8·n_χ²` GB (three `8n_χ²` copies: the matrix,
its rref, the `n×n` nullspace buffer); 5.6 GB survived at `n_χ = 15328`, 6.1
GB was killed at 16005.  **Frontier of the inherited route: `n_χ ≤ 15,500`.**
The census reports both constants per cell; feasibility is decided by the peak.

**Addition: the in-place kernel route.**  `nmod_mat.rref(inplace=True)`
exists in python-flint 0.9.0.  Measured this session before anything else
(`/tmp/memtest.py`, random `(n+64)×n` matrices of nullity 3, `VmHWM` after
`clear_refs`): `nullspace()` adds 2.04 (n = 4000) and 1.96 (n = 8000) further
copies of the matrix; in-place `rref` adds 0.76 and 0.62.  So the peak of the
in-place route is `≈ 1.6–1.8` copies against `≈ 3` — model
`1.4e-8·n_χ² + 0.4` GB — and the same certificate chain applies:
`rank(Agg) ≤ rank_p(M) ≤ rank_Q(M) = n_χ − a(pleth)`, and the assert
`n_χ − rank(Agg) = a` forces equality throughout.  The kernel is read off the
rref (pivot columns, one vector per free column) and **every kernel vector is
then multiplied against the uncompressed sparse rows of all five raising
operators and asserted to vanish mod `p`** — a certificate that the exhibited
vectors lie in `ker_p(M)` itself, not only in `ker(Agg)`.  Elimination happens
only inside flint.

*Pre-registered validation of the addition (part of P1):* on the six
validation cells of `results/stabred_validation.md` Part 2 and on the three
reproduced ℓ = 6 cells below, the in-place route must give the same `a`, the
same `mult_det`, `mult_pad`, and an **identical kernel span** (rank of the
stacked kernels `= a`) as the exact / compressed routes, at both primes.  If it
passes, its pre-registered frontier is **`n_χ ≤ 20,000`** (predicted peak
≤ 6.0 GB), to be confirmed by the `VmHWM` of the first cells above 15,500,
which the ledger records; cells above 20,000 are stated unreachable.  If it
fails, the inherited compressed route stands at 15,500 and the new route is
not used.  Either way every cell above the operative frontier is stated
unreachable, never approximated.

**Time model.**  flint `rref` at `n = 8000` took 75 s; cubic scaling puts a
`20,000` cell at `~20 min` per prime plus assembly and evaluation — under an
hour per cell, two primes.  The session banks in the pre-registered order
until its time runs out and states where it stopped.

## 2. Phase 0 — the census (arithmetic, no measurement)

Every `λ ⊢ 28` (`δ = 7`) and `λ ⊢ 32` (`δ = 8`) with `ℓ(λ) = 6` and
`a(λ, δ) ≥ 1`; those with `λ_1 ≥ δ` form the obstruction-eligible census, those
with `λ_1 < δ` are listed as onset-only.  Per cell:

- `a` by **two independent routes**: (A) the Frobenius/power-sum plethysm
  `h_δ[h_4]` (`analysis/wk8_s30_pleth.amb`, cross-checked cell by cell against
  the separately written `scripts/ambient_screen.a`); (B) **Kostant
  alternation** `a = Σ_{w ∈ S_6} sgn(w) · m(w(λ+ρ) − ρ)` with `m(μ)` the
  weight multiplicity of `Sym^δ(Sym^4 C^6)`, read from one dense
  generating-function table per `δ` (`numpy`, exact integers) — a route that
  shares no formula with (A).  Both must agree at every cell.  (At every
  *measured* cell the definition — kernel dimension — is the third route.)
- `m_det(λ)` by `analysis/wk9_s38_screen.py`'s batched route after its
  self-test reproduces the `n = 3` anchors `Σ m_det = 3, 11` (δ = 2, 3) and
  `m_det((2,2,2)) = 1`; cross-checked against `scripts/ambient_screen.m_det`
  on a sample, as the screen does.  Flag `a > m_det` (arithmetic-forced
  det-side equation) versus `a ≤ m_det` (any onset there is a pure rank drop).
- `N_S` (generating-function DP), `|Stab_W(λ)|`, `n_χ` (orbit enumeration
  where `N_S ≤ 4·10^5` and the bound `N_S/|Stab|` is `≤ 40,000`; otherwise
  the lower bound, marked `~`), balance `λ_1 − λ_6`, predicted assembly RSS
  `1.7e-8·n_χ²`, predicted peak `2.4e-8·n_χ²` (inherited route) and
  `1.4e-8·n_χ² + 0.4` (in-place route), and the feasibility verdict.

`results/sixrow_census.md` is published before any measurement, with the
feasibility line (cells and ambient units reachable per degree, per `a`, per
balance) and the s36-banked cells marked.

**Phase 0b — the permanent's own ideal at `r = 6`, degrees 7 and 8.**
Cheap and decisive for the pad side: for every length-6 weight `μ ⊢ 3δ` with
`a(μ, δ) ≥ 1` in `Sym^δ(Sym^3 C^6)` (`δ = 7, 8`; 56 coefficients, tiny
`N_S`), measure `mult_{per_3}(μ, δ)` with the unreduced pipeline
(`wk8_s30_core.measure`, `per_form(3)` points, both primes).  If every cell
returns `mult = a` then `I(D_6^{per_3})_δ = 0` and, by Prop. 8(1),
**`mult_pad = mult_red` at every weight of that degree** — the permanent adds
nothing anywhere at `δ ≤ 8`, as a theorem-plus-measurement rather than cell by
cell.  Any `mult < a` names the weights `μ` whose Pieri transports are the
only cells where `mult_pad < mult_red` is possible; those cells are then
flagged in the census.

## 3. Predictions

**P1 — validation passes.**  (i) The `l^3 m` witness through the reduced and
unreduced pipelines: `a = 1`, kernel `∝ (12, −3, 1)`, `mult = 0` (the wrong
rule gives `(1, −4, 3)`, `mult = 1`); (ii) `analysis/wk8_s30_calib.py` as-is
prints `CALIBRATION PASSED` — quote the discriminating ratio (41 of 48 World
A cells with `mult < a`), not the pass count; (iii) three of s36's banked
`ℓ = 6` cells reproduce `results/s36_ledger.md` exactly (`a`, `N_S`, `|Stab|`,
`n_χ`, `mult_det`, `mult_pad`, both primes), chosen by a rule fixed now: the
one `ℓ = 6` row with `D ≠ 0`, **`(10,8,7,1,1,1)`** (`a = 3`, `mult_det = 3`,
`mult_pad = 2` — the only discriminating `ℓ = 6` reproduction available), plus
two rows drawn by `sha256("s41 2026-09-02")` from the 17 `ℓ = 6` rows with
`D = 0` and `n_χ ≤ 8000` sorted by `n_χ` (index `h mod 17`, then
`(h div 17) mod 16` of the remainder): **`(13,8,4,1,1,1)`** (exact route,
`n_χ = 1844`) and **`(13,9,2,2,1,1)`** (compressed route, `n_χ = 4747`).
Each is run by s36's route *and* by the in-place route (§1), with identical
kernel spans required.  (iv) The `m_det` self-test anchors `3, 11`.
*Regime:* implementation against the banked record.  *Kill:* any failure →
stop, report, nothing new measured.

**P2 — the six-row determinant ideal does not switch on by `δ = 8` within
reach: every reachable cell returns `mult_det = a`.**  Stated with ~70%
confidence.  *Reasoning:* (a) at `r = 5` the ideal is empty through `δ = 7`
everywhere measured and at `δ = 8` on ~100 peaked cells (s38, s40), with the
cap theorem placing the onset in `[8, 300]` and the s40 conjecture at 300; (b)
the reachable six-row cells are the *peaked* ones (small `n_χ` means a large
weight-stabiliser or a small weight space: long first row, trailing parts
`1, 1, 1` or `2, 2, 2, 2`), and a highest-weight vector of such a weight is
of low order in the trailing variables, so it probes `D_6^{det}` only through
low-order jets in the directions transverse to a five-variable pencil — the
sub-slab s37 reduced to a first-order jet question and found not obviously
deficient; (c) the arithmetic route is predicted silent (P2a).  *Regime:*
this is an extrapolation across length (5 → 6, where the codimension jumps
from 20 to 60 and the singular locus of a determinantal quartic becomes a
degree-20 curve rather than 20 points) **and** across degree (7 → 8); both
are regime changes, which is why the confidence is 70% and not 95%.  Nothing
forces the onset low; nothing forces it high either.  *Falsifier:* any
reachable cell with `mult_det < a` after the sceptical branch (`3a + 24`
fresh det points, seed 907, both primes) — that cell **is** the six-row onset
in reach, is recorded with its degree, weight, and exhibited det-side kernel
(sceptical branch, independent symbolic det pencils), and is the headline
number whether or not `D > 0`.

**P2a — the arithmetic screen is silent at `ℓ = 6`: `a ≤ m_det` at every
census cell of `δ = 7, 8`.**  *Regime:* s38 found `a ≤ m_det` at every
length-5 cell through `δ = 10` with a widening gap; the six-row weights have
larger `a` but the Peter–Weyl room `m_det` grows with the weight as well.
*Falsifier:* any census cell with `a > m_det` — such a cell carries a
det-side equation by arithmetic alone (`mult_det ≤ m_det < a`), is measured
first, and is the onset in reach by itself if reachable.

**P3 — if `mult_det < a` appears, `mult_pad` does not beat it: `D ≤ 0` at the
onset cell.**  Prior on `D > 0` given a det-side bite in reach: ~15%.
*Basis:* (a) the dimension heuristic that has held at every bite so far —
the smaller variety's ideal wakes first, and at `r = 6` the pad side already
bites at `δ = 7` (`(10,8,7,1,1,1)`, a reducibility equation) while the det
side has never bitten; (b) the transfer lemma: passing from `{l·c}` to the
true padded permanent can only lower `mult_pad`, so every permanent-specific
equation pushes `D` down; (c) BIP's theorem does not apply at `(3, 4)` but
its mechanism — orbit-closure coordinate rings of padded forms are
multiplicity-poor at the relevant weights — is the reason occurrence
obstructions are asymptotically absent, and nothing at `ℓ = 6` suggests the
opposite.  *Regime:* heuristic, not a theorem: `R_6` (dim 61) and
`D_6^{det}` (dim 66) contain neither the other, so `mult_red > mult_det` at
the first det bite is arithmetically possible.  *Falsifier:* `D > 0` after
the protocol of §5 — which is the event this session exists to find.

**P4 — the pad side: `mult_pad = mult_red` at every measured cell**, i.e. no
permanent-specific equation in reach through `δ = 8`; and Phase 0b returns
`I(D_6^{per_3})_7 = 0` (27 cells, ~85%) and `I(D_6^{per_3})_8 = 0` (~65%).
*Regime:* measured empty at `δ = 6`, Pieri-forced empty below; the onset of
`I(D_6^{per_3})` is unknown and codimension 6 in `P^55` leaves room for it
to be low.  *Falsifier:* `mult < a` at any Phase 0b cell (which then names
the only weights where `mult_pad < mult_red` can occur), or
`mult_pad < mult_red` at any swept cell — the first permanent-specific
equation in the programme, to be certified as in s36 §4.1 (fresh points,
both primes, exhibited vector, (★) check) before it is stated.

**P5 — sizes and honesty.**  The in-place route validates and lifts the
frontier to `n_χ ≈ 20,000`; measured `VmHWM` at the first cells above 15,500
lands within 15% of `1.4e-8·n_χ² + 0.4` GB.  Coverage is reported per
degree in cells *and* ambient units, as fractions of what exists.

## 4. The sweep order (exact rule; the census fixes the list)

Applied deterministically to `results/sixrow_census.md` once published:

1. **Arithmetic-forced cells** (`a > m_det`), if any, ascending `n_χ`, reachable
   ones only.
2. **`δ = 7`**: every census cell not banked by s36 (`results/s36_ledger.md`
   Stratum B and `results/s36_aone.md`), reachable at the operative frontier,
   ascending `n_χ`, interleaved 3 : 1 with probes drawn in turn from the
   largest-`a` and the most-balanced reachable unmeasured cell.
3. **`δ = 8`**: the same rule over the `δ = 8` census.

Two workers under the claim queue: worker `small` takes only cells with
`n_χ ≤ 5000` (peak `≤ 0.5` GB) in the same order; worker `big` takes the
rest, one at a time; both wait on the memory guard (`predicted peak ≤ 0.85 ×
MemAvailable`) and never skip.

Per cell: `a` by kernel dimension and by plethysm (asserted equal);
`rank(R) = n_χ − a` asserted; the χ-obstructed fixed rows asserted to cancel;
both sides at `a + 8` points; both primes (must agree); `mult_red` by (★) from
the banked kernel; row banked to `results/s41_ledger.md` and committed before
the next cell; pickle to `/root/s41/`.

**Sceptical branch** (either side `< a`): re-run at `3a + 24` points, seed
907, both primes; the vanishing HWVs exhibited in full monomial coordinates
(`results/s41_cells/`); evaluated by the independent symbolic constructions of
`wk9_s36_bite.py` (true pad, `l·cubic`, generic, det pencils; 20 points each,
fresh seed).  A det-side bite is additionally checked against (★) — a det-side
vector should *not* satisfy (★) (det pencils are irreducible), and the fact is
recorded either way.  Only then does the bite enter the ledger.

## 5. The obstruction protocol (verbatim from the brief)

`D > 0`: STOP-EVERYTHING.  Full protocol: (i) `a` both routes; (ii) `mult_det`
and `mult_pad` re-derived at 3× points, second prime; (iii) the det-side kernel
vector exhibited and shown nonzero at 20 independently built true
padded-permanent points and vanishing at 20 det pencils; (iv) `m_det`
re-derived by a second, independently written implementation
(Murnaghan–Nakayama, calibrated on 3, 11); (v) everything into
`docs/OBSTRUCTION_CANDIDATE.md`, prereg cross-referenced; (vi) end the session
there.  The integrator re-derives before the word is used.

## 6. Kill criteria

- Any P1 failure → stop, report, measure nothing new.
- `D > 0` → §5; the session ends there.
- Memory → the census bounds honesty: a cell that does not fit at the
  operative frontier is stated unreachable, never approximated; a cell killed
  by the OOM killer is recorded as attempted-and-killed with its `n_χ`.
- A compressed-certificate miss (`n_χ − rank(Agg) ≠ a`) → one retry with a
  fresh `P`-seed, then the cell is abandoned and said so.
- Any disagreement between the two `a` routes in the census, or between the
  in-place and inherited kernel routes in validation → stop and report before
  measuring.
