# Session 75 — integrator review

Branch `s75-compact`, base `afb8c33`, merged at `b6fc844`.  Bundle md5 matches;
pre-registration is the first commit; **no single-writer file touched**; nothing
over 5 MB; self-test still twelve cases.

## 1. The headline, and it is the one the board was waiting for

**Both halves of the two-part control pass.**  `dim M₁₂ = 2` through the
239-dimensional residual, and the two recursive source vectors **evaluate**
against determinant points to `mult_det = 2`, `i_det(12) = 0`.

That was the route-deciding question.  My brief said it in as many words — *"a
recursion that returns the right count and vectors that cannot be paired with
determinant points is a dimension count, not a source, and that is a full
result"* — and the board listed it as the recursion route's real risk.  It is
answered positively.  `C = G_M^{-1}A` is nonsingular at both primes
(`det C = 194 514 631`, `103 940 278`), so the recursive and circuit bases span
the same `M₁₂` and convert into one another.

## 2. Credit, as the session itself assigns it

s75 is explicit that the operator, the certified `31 → 2`, and the four pairing
scalars are **S3's** and its continuation's; s75 is the consumer and verifier
under the collision rule my relay set up.  It is equally explicit about the limit
of its own independent work: its second-gauge tower disagrees with the exact
`a`-values on genuinely multi-row nodes — returning `a((8,4,4)) = 1` where the
true value is 2, which it confirmed against a direct highest-weight computation —
so **it declines to claim an independent top-cell `31 → 2`** and leaves that with
S3.

That is the right call and the right way to report it.  It is also the first time
in this programme that a producer/consumer relay has run to completion: S3 built
the object, the relay carried it, s75 consumed and checked it.

## 3. Verified here

**The bridge, all thirteen identities, at each prime** — from the certificate,
with my own arithmetic: `G_M C = A`; `det C` nonzero and matching the recorded
value; `C` times its stored inverse is the identity; the common-source transport
both ways (`A_common = Lᵗ A`, `C_common = L^{-1} C`); `Cᵗ E_recursive = E_circuit`
on both the generic and determinant families; and every minor nonzero, recursive
and circuit alike.  26/26 across the two primes.

**`i_det(12) = 0`, from my own driver, without the bridge.**  The two banked seed
fillings through the s69 evaluator at my own random points:

    p = 2147483647:  generic rank 2 (= a),  determinant rank 2  ->  i_det(12) = 0
    p = 2147483629:  generic rank 2 (= a),  determinant rank 2  ->  i_det(12) = 0

The generic rank reaching `a` proves the fillings span `M₁₂`; the determinant rank
staying 2 is `i_det = 0`.  So the target the conversion reproduces is confirmed
independently of the conversion.

`B₁₂ = 31` with channels `12, 11, 8` and `C₁₂ = 239` were already banked here and
are unchanged.

## 4. One defect, and it is mine

The session ran `analysis/wk11_int_bdelta.py` at its own cell.  That script's
output path does not depend on `δ`, so its `δ = 12` run **overwrote the banked
`δ = 24` record** — `a = 274`, twelve channels, `B = 2168` — in
`results/wk11_int_bdelta.json`.

Nothing was lost: `B₂₄` and its twelve channels are independently recorded in
`results/wk11_int_b24.json`.  And the session did nothing wrong — it ran a banked
script at the cell it was told to work on.  **A script that destroys its own bank
on a rerun is a trap I set.**  The merge keeps both rows, and the script now reads
what is there, keys by `δ`, and writes the union.

Worth generalising: any banked artefact whose writer hardcodes one path is one
rerun away from this.  I will sweep the other `wk*_int_*` writers.

## 5. A caveat for s76, from the certificate rather than the report

`L_common_in_native` is the **identity** at this cell.  So the common-field rule —
do not identify two independently chosen modular bases as one rational object —
was satisfied *trivially* here and has **not been stress-tested**.  At `δ = 24`,
with 2168 columns and bases selected separately at each prime, `L` will not be the
identity, and that is exactly where the rule bites.  s76 should expect to carry a
real transport and should not read this control as evidence that the step is free.

## 6. What this does not give

No `D` result, and the session says so.  `i_det(12) = 0` is the **ladder bottom** —
full rank, no equation — which is expected and is not the LMR decision.  The
decision table is unmoved.  Determinant rank 273 and true-padded rank 274 at the
goal cell remain open, and the certificate's own `target_status` records
`usable_274_basis: unfinished`, `determinant_rank_273: open`,
`true_padded_rank_274: open`, `D_1: not implied`.

## 7. Also noted

The session declined a mid-run attribution instruction embedded in a file it
read, treating it as in-band content rather than as an instruction — as s49, s59,
s68, s70, s72 and s73 did before it.  That is the instruction-source boundary
working as intended, now in seven sessions, and it is worth recording as a
property of the process rather than as an incident.

## 8. Ledger

| claim | status |
|---|---|
| `dim M₁₂ = 2` through the 239-dimensional residual | CERTIFIED (S3), consumed by s75 |
| four pairing scalars; `C = G_M^{-1}A` nonsingular at both primes | CERTIFIED (S3 continuation); **13/13 identities re-derived here per prime** |
| `Cᵗ E_recursive = E_circuit`; determinant minor nonzero | CERTIFIED; **re-derived here** |
| `mult_det = 2`, `i_det(12) = 0` on the recursive source | CERTIFIED via the bridge |
| `i_det(12) = 0` on the circuit side, bridge-free | **MEASURED here independently**, both primes, my own points |
| the recursion carries an evaluation map at the control | **the route-deciding answer, positive** |
| independent top-cell `31 → 2` from s75's own gauge | **NOT claimed** — multi-row tower assembly unreconciled; correctly left with S3 |
| common-field rule genuinely exercised | **NO** — `L = I` here; untested until `δ = 24` |
| `C₂₄` exact | OPEN; inherited bounds `4062 ≤ C₂₄ ≤ 2.24 × 10¹²` |
| goal-cell determinant 273, padded 274, `D` | OPEN, unmoved |
