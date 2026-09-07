# Session 73 (C6) — the decision table, and the `D`-ladder at `n = 3`

Batch 11, **ungated** — it has a default mode that produces a number from
material already in the repository, and a second mode it switches to if a source
lands.  It subsumes the Mode A content of session 65, whose gate never opened in
batch 10; **65 stays a gap in the numbering** and this session does not pretend
to be it.  **Read `docs/batch11_worker_preamble.md` first**, then
`docs/batch11_plan.md` §1, §1.1 and §5(i), `docs/s65_prompt.md` (the unrun brief
— its Mode A tasks are correct and unchanged), `analysis/wk11_int_p0a.py`,
`results/wk11_int_p0a.json`, `analysis/wk10_s63_n3control.py`, and
`results/certs/19_7_2_2_2_2_2_d12_n3_permanent_*` (the first `n = 3`
certificate, a worked example of the format).

## Where you start: the programme's first `D > 0`

At the `n = 3` member of the LMR family, `λ = (19,7,2⁵)`, `δ = 12`, `r = 7`,
`a = 6`, both house primes:

    i_det = 1,  mult_det = 5      (session 63; reproduced on an independent driver)
    i_per = 0,  mult_per = 6      (batch-11 pre-batch check P0-A)
    D = i_det − i_per = +1

`i_per = 0` is rigorous — `mult_per = 6 = a` was measured mod `p` and
`rank_p ≤ rank_Q ≤ a` — and `i_det ≥ 1` is LMR's theorem at this cell, so `D = 1`
holds over `Q`.  Both multiplicities are nonzero, so this is a **multiplicity
obstruction, not an occurrence obstruction**; use that term.  The separation it
certifies is also visible from `dim P₇ = 59 > 47 = dim D₇`, so the content is the
certificate, not the statement.  It is the comparison at the *unpadded* `per₃`,
which is a different pair of varieties from the programme's padded model —
`docs/stocktake_batch10.md` §6 proves the padded `n = 3` cell can never carry an
obstruction, and that proof stands.

## Mode B — the default, and a genuinely open question

**Does the obstruction survive transport up the ladder?**

The `n = 3` ladder is `λ_δ = (3δ − 17, 7, 2⁵)`, and `δ = 12` gives `(19,7,2⁵)`.
Lemma L makes `i_det(δ)` and `i_per(δ)` **separately non-decreasing**, so their
difference need not be monotone in either direction.  Every outcome is
interesting:

    1, 1, 1, …    a persistent obstruction family
    1, 0, 0, …    the permanent catches up, and the obstruction is a low-degree accident
    1, 2, …       D grows

Nobody knows which.  The cell builds in 274 s at `n_χ = 17 047` and the full
two-form run took 876 s, so `δ = 12, 13, 14` is an affordable night.

For each rung: build the cell, compute the `a`-ladder value independently,
measure `i_det`, `i_per` and `i_pad` on the **same** source, and produce

- `U_D = ker T_det` and `U_P = ker T_per` as explicit bases in the same `χ`
  coordinates, and `dim(U_D ∩ U_P)`;
- the three-outcome table of session 65's brief, at `n = 3`;
- a `sparse_nullity` certificate for every full-rank claim, and the kernel
  vectors exhibited for every positive nullity.

The verifier now accepts `n ∈ {3,4}` and has a `permanent` point family for the
unpadded `per_n` pencil (`tools/verify/FORMAT.md`); use it rather than
inventing a format.

Also carry the transported vectors explicitly: `u = c_{(3,0,…,0)}` at `n = 3`
carries `M_{δ−1}` into `M_δ` injectively, so at each rung you can check
`dim J(M_{δ−1}) = a_{δ−1}` and read off the birth space, exactly as session 68
does at `n = 4`.  That is a free cross-check on both engines.

## Mode A — if a source lands

If session 68, 69 or Sol's S5 delivers an LMR source basis before your
checkpoint, switch.  The tasks are session 65's, unchanged, plus one column:

1. `i_det` at LMR, from the source, both primes.
2. `i_pad` at LMR — session 64's padded evaluator on the same source
   coordinates; that engine exists and is calibrated on 48 cells.
3. **`i_{per₄}`, the unpadded permanent at LMR** — new, and nearly free, since
   it is one more evaluation family against a source that already exists.  The
   orientation is favourable there too (`16·9 − 30 = 114` for `det₄` against
   `16·9 − 6 = 138` for `per₄` inside `dim Sym⁴C⁹ = 495`), so it is the `n = 4`
   positive control the programme has never had.  **It is what distinguishes
   "no obstruction at LMR" from "the instrument is blind at `n = 4`"** if the
   padded comparison comes back `D ≤ 0`.  Report it as a required third column,
   not an extra.
4. `U_D`, `U_P`, `dim(U_D ∩ U_P)`, and the three-outcome table at LMR.

Set the checkpoint time in your pre-registration and honour it.  Do not wait
past it: Mode B is not a consolation, it is the session's default deliverable.

## Success

Mode B: three rungs of the `n = 3` `D`-ladder with certificates, and an answer
to whether `D = +1` persists.  Mode A: the exact LMR `D` with its orientation
and the three-outcome table.

## Stopping rules

- Any `D > 0` at any cell goes through the verification protocol before it is
  reported anywhere, including in conversation.  You will be reporting at least
  one, so read the protocol before you start.
- A rung where `i_per` disagrees between primes halts that rung; report the
  disagreement.
- If a rung's measured `a_δ` disagrees with the independent Weyl-alternation
  value, halt — that is an instrument defect, not a discovery.

## Deliverables

`results/PREREG_s73.md` with the Mode A checkpoint time stated;
`docs/s73_report.md`; the `D`-ladder table as `results/s73_dladder.md` and
`.jsonl`; `U_D`, `U_P` and their intersection as artefacts at every rung;
certificates in `results/certs/`; code under `analysis/wk11_s73_*.py`; bundle
`s73_decision.bundle` + `.md5`.
