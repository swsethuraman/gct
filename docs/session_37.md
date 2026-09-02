# Session 37 (2026-09-02) — theory: the washout, the transfer, and the DIP technique

Branch `s37-dip` on clone tip `5367c75` (the integrator's s35 review).
Ancestry gate `git merge-base --is-ancestor c02cee8 HEAD` passed;
`docs/s35_review.md` present.  No session 36 or 37 on `main` — no
renumbering needed.  Pre-registration `results/PREREG_s37.md` committed
first (`ce2e657`), before any computation or literature reading.
Single-writer files untouched.  Delivery by bundle only.

## Deliverables

| file | content | headline |
|---|---|---|
| `docs/washout_lemma.md` | D1 | `P_r = R_r` for `r <= 5` (one-point Jacobian ⇒ dominance, re-verified at a fresh point); the finite-generic-stabiliser page for `per_3` (all `r >= 1`) and `det_4` (`r >= 3`, `r = 2` explained); `dim D_6^{per_3} = 50` exact; all dimension tables unconditional; **no cell below length 6 can be permanent-sensitive** |
| `docs/transfer_lemma.md` | D2 | `D_P <= D_R`: `D < 0` transfers, `D > 0` does not, `R_r`-computations are a complete screen; the pipeline computes `P_r`; **the permanent only erases**; Prop. 8: the permanent can be felt only where `I(D_r^{per_3})_delta != 0` — at `r = 6` not below `delta = 7` (Pieri through 5, measured empty at 6) |
| `docs/dip_transfer.md` | D3 | DIP's mechanism is ambient-vs-stabiliser (no HWV evaluation) = the house's `a > m_det` screen; any DIP-type cell is permanent-insensitive (theorem); their no-go does not transfer as a theorem but blindness is promoted in precise form; `x_0·per_3 ∉ closure(GL_16·det_4)` proved in-house from Theorem 5; BIP's `n >= m^25` is silent at `(3,4)` — the `a >= 2` gate flagged; three candidates |
| `docs/blindness_slab.md` | D4 | Theorem A with proof; strict cells `D((8,8,8),6) = D((12,8,8),7) = −1`; pad onset `5` or `6` (two named cells decide, see below); the `lam_5 = 1` sub-slab: pad jets 34-dim, all actual reducible det jets `<= 33`-dim (every s32 stratum 29/30 at first order, S-Z certified), generic block limit negative — open as a border question; Dimca Thm 3.1 + Koszul bookkeeping pins `dim M(f)_{3d−5} = smooth + def_{2d−5}`; the s35 cap `<= 300` is a theorem modulo Kleiman |

Exact checks (`analysis/wk9_s37_*.py`, outputs in `results/s37_*.log`):
`jacobian` (fresh-point ranks, 3.8 s), `onsets` (house pipeline: `R_3`
through `delta = 7`, `R_4` through `delta = 5`, `R_5` at `delta = 5`,
`D_6^{per_3}` through `delta = 6` — the first attempt at `delta = 6` was OOM-killed at 3.3 GB because it built raising-operator matrices for `a = 0` weights; the rerun pre-filters by plethysm `a` and caps `N_S` at 7000), `jet` (block-limit planes), `jetbranch`
(first-order jets per s32 stratum, exact over `Q` and two primes),
`ell6` (the length-6 `(a, N_S)` list at `delta = 6`).

## Background scans at the time of bundling

- `results/s37_onset_R5_d5.log` — length-5 weights at `delta = 5`, pad:
  21 of 23 `a > 0` cells measured, all `mult = a` (no bite); `(6,4,4,4,2)` and `(4,4,4,4,4)` above the memory cap, unmeasured — so the pad onset is 5 or 6, decided by those two cells
- `results/s37_onset_per6_d6.log` (`_d56.log` is the OOM-killed first attempt, `delta = 5` only) — length-6 weights of
  `Sym^6(Sym^3 C^6)` against `D_6^{per_3}`: all four `a > 0` cells measured, `mult = a`: `I(D_6^{per_3})_6 = 0` — the permanent is invisible at `r = 6` through `delta = 6`

## What changed in the picture

1. The hunt below length 6 is a hunt about the reducible locus; the s35
   correction is now a theorem with a precise boundary (`ell = 6`,
   `delta >= 7`).
2. Every obstruction, at any length, is an `(R_r, det_4)` obstruction; the
   permanent can only erase.  DIP's method — which the house has been
   running as Direction 4 — can only find `(R_r, det_4)` cells.
3. The set-theoretic separation of the pair is known (Theorem 5 +
   restriction; LMR), so the programme is, like DIP, exhibiting the
   multiplicity method on a known non-containment.  That is the honest
   frame for paper 2.
4. Two `D < 0` cells at `delta = 6, 7` (length 3), earlier than s35's.
5. The `lam_5 = 1` sub-slab is the first place a border phenomenon is
   structurally possible at `ell = 5`; the cheap cells there are the right
   next measurement, as s34 already planned.
6. The `<= 300` cap is now literature-backed (Dimca 2013, Thm 3.1).

## Process

- Pre-registration before reading: the DIP expectation ("explicit HWV
  evaluated at structured points") was **wrong** — the mechanism is a
  plethysm/stabiliser count — and is recorded as such in
  `results/PREREG_s37.md` versus `docs/dip_transfer.md` §2.  The verdict
  the prereg named as the "success" branch (no-go transfers, blindness
  promoted) is the one that materialised, in a sharper form.
- One correction during writing: an early draft of the transfer lemma
  said `I(D_6^{per_3})` is "zero through `delta = 4` (measured)"; the
  Pieri bound `ell <= delta` makes it zero through `delta = 5` for free,
  and the document was corrected before commit.
- The `delta = 7` length-6 enumeration (`ell6`) timed out at 10 minutes
  and was dropped; `delta = 6` suffices for the candidate list.
- `python-flint` had to be installed in the container (`pip`, 0.9.0).
- A `pkill -f` with a pattern that matched its own restart command killed
  the restarted scan once — the house's own standing warning, re-learned;
  the second restart used explicit PIDs.

## One sentence for the next brief

Below length 6 the hunt is provably about `{l·c}` versus the determinant
and the permanent can only ever *erase* an obstruction, so the next
measurements should be the cheapest `ell = 5`, `lam_5 = 1` cells at
`delta = 7, 8` (a border phenomenon is now structurally possible there)
and the Kronecker/pipeline pair at `((14,2,2,2,2,2), 6)` and
`((10,8,3,1,1,1), 6)` (computable against `{l·c}` without loss, since
`I(D_6^{per_3})_6 = 0`), with `docs/transfer_lemma.md` Theorem 3 as the
standing rule for reading any `D > 0`.
