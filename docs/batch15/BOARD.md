# Batch 15 — twelve parallel Astra sessions

Prepared 13 September 2026. All twelve use `gpt-6-astra`, with xhigh reasoning recommended. This is a launch-ready local proposal and packet; no workers have been dispatched from the old conversation. The new integrator can launch from the annotated `batch15-base` tag after its final preflight. The external dispatch manifest carries the exact commit and tree.

We now have enough machinery to test smaller cells and new shapes systematically. The original LMR cell cannot yield positive D: its remaining job is exact negative closure. The most direct positive opportunities in this board are the unexcluded degree-eight cells in03/04. They are testable candidates, not evidence that an obstruction probably exists there. The one-dimensional cells in02 are cheaper diagnostics. Sessions07/09/12 pursue mechanisms that could produce a determinant upper bound when evaluation alone stalls.

| Session | Job in simple terms | Concrete success or useful negative |
|---|---|---|
| 01 | Finish the two missing global reducible relations | Degree14 complete interpolation159, five global relations, D_LMR=-4; otherwise an exact remaining gap |
| 02 | Test nine very small one-dimensional cells | One determinant nonzero retires each cell; a positive requires proved determinant vanishing and padded nonzero |
| 03 | Test the first two-dimensional opportunity | Degree8 (13,11,3,2,1^3); determinant rank2 excludes, one global determinant equation plus padded rank2 gives D>=1 |
| 04 | Test complementary small multiplicities | Degree8 (11,11,5,2,1^3) and (12,11,4,2,1^3); determinant rank3 excludes either |
| 05 | Decide whether the next stable family is also excluded | Tail(21,2^7), stable determinant floor530 plus three transported padded equations |
| 06 | Find fresh families within measured cost | Exact census, fresh exclusions and at most three validated pilots outside solved tails |
| 07 | Build a valid projected product map | Presentation-independent, equivariant, ideal-preserving map; or an exact counterexample to the proposed construction |
| 08 | Evaluate shapes our current backend cannot handle | Three/unequal-column bracket evaluator with independent exact controls and a costed full-height instance |
| 09 | Turn determinant rank deficiencies into global proofs | Small complete pullback or symbolic determinant identity instrument with justified parameterization |
| 10 | Make large existing conclusions easy to verify | Compact geometric certificate for (12,4^5)_8, first one determinant witness, then its full D=-3 result |
| 11 | Make all banked results searchable and usable | One scoped bounds/evidence consumer, prioritized recovery of missing evidence, no silent promotion of recorded claims |
| 12 | Audit padding scope and test exact determinant bounds | Settle the length9/10 theorem question where possible; bounded character/stabilizer upper-bound pilot |

Every session starts from banked inputs and has an independent fallback. Optional later relays:03/04 candidate equations to09;07 validated maps to06;08 new shapes to06;12 useful bounds to02–04; all evidence into11 and the integrator. A relay must include immutable definitions and checks before consumption. It never justifies assuming another live session's promised result.

All twelve tasks may begin together. Start heavy numerical work in01 and02 only; other tasks begin with proof, code, exact sizing and small controls. The new integrator assigns the next free numerical lease to03/04, then05 and later pilots. This avoids twelve simultaneous memory-heavy jobs on one machine. Use separate worktrees and one numeric process per job by default.

The common preamble sets success/stop criteria, precise proof thresholds, resource limits, liveness controls, data conventions and bundle delivery. Each detailed brief adds exact inputs and its own productive fallback. Shared theorem and exclusion files have one integrator writer; each worker returns a per-slot proof fragment. Budget and missing-dependency checks occur before expensive work. Historical Claude and Astra implementations remain available with their attribution.

Judge the batch by certified positive inequalities, precise exclusions and independently controlled new capabilities. A rank plateau does not certify an equation. Repeated full determinant ranks in the affordable panel argue for changing degree or shape; a working global determinant instrument would justify following its candidates. A successful projected map matters only if its determinant advantage exceeds the entire padded ideal, not merely the image of known relations.

Read `ACCEPTED_STATE.md`, `CONTRACT_REVIEW.md`, `WORKER_PREAMBLE.md`, `BOOTSTRAP.md`, then the twelve files in `briefs/`. `results/b15_prep/slots.json` lists hashed slot inputs; `TOOL_INDEX.json` names the reusable entry points and their limitations. The external dispatch manifest is authoritative for the base hash.
