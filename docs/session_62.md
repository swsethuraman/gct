# Session 62 — the last-born scalar, two positive controls, the cost curve

2026-09-07. Branch `s62-gram` off `main` at `226b4ef1` (ancestry gate passed).
Pre-registration `results/PREREG_s62.md` before any measurement. Bundle
`s62_gram.bundle` (single ref `refs/heads/s62-gram`, prerequisite `226b4ef1`,
121 KiB), head **`74f898651020c906714fa1a00ef0702b5304a4d9`**, MD5
`49741b0d30a9cedf33d634cdfd0ec427`; fast-forwards `main` in a fresh clone of
`226b4ef1` (ancestor test re-run before applying). Nothing pushed. Report
`docs/s62_report.md`; cost curve `results/s62_cost.md`/`.json`; certificates
`results/certs/s62/` (44, all PASS `tools/verify`); code `analysis/wk10_s62_*.py`.

**The batch-10 preamble and plan the brief cites exist in no clone** (`work/`,
`gct-rewrite/`, `work-preRewrite/` on the laptop, and no public branch); worked
from the brief's C1 and the two mid-session integrator notes.

## Verdict

The room-one scalar `s` (a within-degree Schur complement, integrator note 1)
vanishes at the `n = 3` LMR cell and only there. Banked:

1. **`n = 4`, `δ = 2,3,4` reproduced through the block Gram** — 40 constituents,
   `rank_Q G_λ = a`, `i_det = 0`, no room-one `s` zero. `Σa_λ² = #orbitals =
   3,9,43`; the five `δ=4` multiplicity-2 cells match the brief; **`β_4` is
   noncentral** (`G_λ` not proportional to `N_λ` at any of them).
2. **Two positive controls, both a rank drop.** `n = 2` `(2^δ)` is a *proved*
   drop (disc of a rank-≤4 form): Foulkes Gram full rank at `δ=3,4`, rank 0 at
   `δ=5,6` — the explicit Gram/Schur machinery validated end to end at the
   theorem boundary. `n = 3` LMR `(19,7,2^5)_{12}`: `mult_det = 5 < a = 6`,
   `i_det = 1` at both primes.
3. **Cost curve.** Enumeration route dead at `δ=5` (measured 174 ns/element,
   `δ=5` one pass 7.4 min ≈ 24 h/cell, matching s56). The reduced-route support
   `|S| ~ n_λ ~ 10^11` at the LMR cell puts that route out of reach too.

## The `n = 3` LMR control — precise logic (integrator note 2)

a-sequence measured 2,4,5 at `δ=9,10,11` (full rank, `nullity[E;ev]=0` at one
prime proves `mult_det=a` over `Q`) and the drop to `mult_det=5` **only** at
`δ=12` — the control is two-sided. **The engine did not independently certify a
rank drop; it confirmed it does not over-report rank.** Random evaluation
under-reports rank, so the measurement gives rigorously only `i_det ≤ 1`
(`rank_p=5 ⟹ rank_Q≥5`); `i_det ≥ 1` is LMR; together `i_det = 1`. Independently,
the **predecessor route** — `mult_det(11)=5` full rank `⟹ mult_det(12)≥5` (Lemma
L) `⟹ i_det(12)≤1 ⟹ =1` with LMR — is the 273/274 argument at `n=3`, end to end.

The exhibited integer HWV (240 510 monomial terms, weight `(19,7,2^5)`, max
`|coeff| 544`) is the programme's **first exhibited element of `I(D)^{HWV}` with
`i_det>0`**: `E·v=0` over `Z` on the full sparse `E`, vanishes at 28 fresh `det_3`
pencils over `Z`, nonzero at a generic cubic (independent rebuild
`wk10_s62_n3check.py`). Finite-point vanishing is Schwartz–Zippel evidence of
ideal membership, not a proof — the rigorous `i_det≥1` stays LMR + predecessor.
`hwv` cert kind is `n=4`-only, so it ships as the artefact + checker.

## Corrections folded in

- Integrator note 1: `s = c − bᵀA⁻¹b = det B/det A = ‖(I−P)T(v)‖²`, `A` the
  *within-degree* Gram on `J(M_{δ−1})` (implemented so from the start); three
  forms asserted equal at every room-one cell. Predecessor-full-rank lower bound
  (`det A ≠ 0`) valid mod `p` (`rank(MᵀM) ≤ rank M`); a claimed `s=0` is char-0.
- Adversarial-review fix (SERIOUS): the `|S|` cost framing conflated three
  scales. `|S|` (reduced-route) = orbit-basis support `≤ n_λ`; `Σ|O| = |H|` is
  the enumeration cost. Field renamed (`H_total`, not `N_S`); LMR `|S| ~ n_λ ~
  10^11`, out of reach either way.

## For session 63

Report `|S|` at `r=9` first; the Foulkes/reduced Gram cannot reach `δ=24`
(`|S| ~ 10^11`); run the direct `λ`-block (evaluation) route as the `n=3` control
is done here. C2 reduction validated in miniature (the predecessor route); run
`det A_24` at both primes (mod-`p` valid for the lower bound). Do not attempt
`δ=23,24` by enumeration.

## Engineering

`analysis/wk10_s62_gram.py` (general-`n` Foulkes enumeration, orbitals, block
Gram, room-one Schur, centrality); `wk10_s62_run.py` (n=4 δ≤4); `wk10_s62_n2.py`
(proved control); `wk10_s62_n3.py` + `wk10_s62_n3check.py` (LMR control via the
s42/s45 evaluation engine, block-Wiedemann, one prime for full-rank
predecessors, both + integer vector for the drop); `wk10_s62_cost.py`;
`wk10_s62_isotypic.py` (P3). Two house primes for every mod-`p` claim; nothing
over 5 MB committed (the 14 MB `δ=4` count cache and the 68 MB monomial expansion
kept local, regenerate from code); no session-link trailer, per standing rule
and as s49/s56/s59.
