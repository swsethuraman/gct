# Session 69 (C2) — the compact circuit: source vectors as contractions, not coordinates

Batch 11, **ungated, runnable immediately**.  The second of three independent
approaches to the same bottleneck; it differs from session 68 in its failure
mode, which is the point of running both.  **Read
`docs/batch11_worker_preamble.md` first**, then `docs/batch11_plan.md` §2.1 and
§4 (the diagnosis and why redundancy at the bottleneck is the batch's design),
`docs/stocktake_batch10.md` §4, `docs/lmr_cell.md`, and
`analysis/wk10_s63_n3control.py` with `results/artefacts/s63_n3_ideal_vectors.npz`.

## The question

Sessions 62–64 measured the wall in **coordinates**: every realisation of `M_λ`
the programme owns needs `≥ 10⁷` of them.  Is the wall in the object or in the
representation?

    dim M_λ  =  274   ≪   the size of every known realisation of M_λ

That is the diagnosis in one line (plan §9), and it is a statement about
*algorithms*, not about size.  This session asks whether the 274 vectors have a
short description — a contraction or bracket circuit — that never mentions the
`3.10×10⁷` coordinates at all.

## The structural handle

    (65, 17, 2⁷)  =  (2⁹)  +  (63, 15)

The tail-of-twos part `(2⁹)` and the two long rows are structurally different
objects, and the LMR shape is the sum.  A highest-weight vector of a
two-row-plus-tail shape is a natural candidate for a circuit built from
determinantal brackets on the tail and symmetrised products on the long rows.
The question is whether that description can be made exact, evaluated, and
raised — not whether it is suggestive.

## The control you must pass first

**Reproduce `U_D` at the `n = 3` cell, exactly.**  Session 63 banked the
one-dimensional ideal highest-weight vector at `λ = (19,7,2⁵)`, `δ = 12`, `n = 3`
in `results/artefacts/s63_n3_ideal_vectors.npz` (shape `(1, 17047)`, prime
`2147483647`).  A circuit representation that cannot reproduce that vector — up
to scalar, in the same `χ` coordinates — is not a representation of the object.

This is not a formality.  It is `1/1800` of the LMR carrier, the answer is in
the repository, and a circuit that fails it has told you in an hour what would
otherwise take a night.  **Do this before anything at `n = 4`.**

## The functoriality pre-check applies

`docs/brief_wording.md` §7.  Before building, answer in writing: does your
representation compute the same functional on `Sym^δ(Sym⁴ C^r)` that the
coordinate one does, or an invariant that merely correlates with it?  The
programme is valid because containment forces `mult_λ C[P] ≤ mult_λ C[D]`; a
circuit that computes something else, however elegant, does not inherit that.

## Tasks

1. State the circuit representation precisely, with its evaluation semantics and
   its raising-operator action.  Both must be defined before any computation.
2. Reproduce the banked `n = 3` `U_D` exactly.  Report the comparison.
3. Reproduce `a = 6` at that cell — the whole highest-weight space, not one
   vector — and check independence.
4. Measure the circuit's size as a function of `δ` at `n = 3` for
   `δ = 12, 13, 14` along `λ_δ = (3δ − 17, 7, 2⁵)`.  A representation whose size
   grows like the carrier has not solved anything; say so with the numbers.
5. Only then, `n = 4`.  Begin at the ladder bottom `(17,17,2⁷)`, `δ = 12`, where
   `a = 2` — the same seed session 68 is approaching from the other side.  If
   you produce it and session 68 does not, say so plainly; that is the batch's
   best possible outcome for this pair.
6. If you reach `n = 4` at any rung, hand the vectors over in the same `χ`
   coordinates the rest of the batch uses, with the conversion documented.

## Success

The `n = 3` control passed exactly, a measured size curve in `δ`, and either the
`n = 4` seed or a precise statement of what the circuit cannot express.

## Stopping rules

- **Failing the exact `n = 3` control stops the session at `n = 3`.**  Report
  what the circuit produced and how it differed.  Do not proceed to `n = 4` on a
  representation that does not reproduce a banked vector.
- Circuit size growing at carrier rate in `δ` is a negative result: report the
  growth law and stop.
- Do not build the full carrier as a cross-check at `n = 4`; that wall is
  measured and reconfirming it is not a use of a night.

## Deliverables

`results/PREREG_s69.md`; `docs/s69_report.md`; the circuit specification as
`docs/compact_circuit.md`; the `n = 3` comparison and the size curve as
`results/s69_sizes.md` and `.jsonl`; any `n = 4` vectors as artefacts in `χ`
coordinates; code under `analysis/wk11_s69_*.py`; bundle `s69_circuit.bundle`
+ `.md5`.
