# Integrator note 1 to session 64 — the padded factorization, verified and repriced

Written on receipt of the external S3 memo, while session 64 is running.  Three
of its claims are reproduced here independently, one is a provenance
correction, and one number that S3 did not compute has been computed and it
changes how session 64 should spend its time.

## 1. Reproduced independently — the padded Gram formula is right

S3's combinatorial Gram for `x_0·per_3`,

    K_pad(G) = Σ_{M_0 ∈ PM(G)}  E_3(G − M_0)² ,
    E_3(H)   = Σ_{M_1 ∈ PM(H)}  2^{c(H − M_1)} ,

over the degree-4 bipartite overlap multigraph of two Foulkes block partitions,
was implemented here from the formula alone (`analysis/wk10_int_padgram.py`,
sharing no code with the memo).  At `δ = 2` the three pair-orbital values are

    overlap type (0,4) : 20 736
    overlap type (1,3) :  2 592
    overlap type (2,2) :  1 152

**exactly as reported.**  The resulting `35 × 35` integer Gram on `H_{4,2}` has
**rank 35 over `Q`** — stronger than the modular check in the memo — so
`mult_pad = a` at all three `δ = 2` constituents.  The formula is accepted.

Also reproduced: at `λ = (65,17,2⁷)`, `δ = 24`, the horizontal 24-strips
`λ/μ` with `|μ| = 72` number **exactly 48**, of lengths 8 and 9 only.

## 2. Provenance — the central identity is session 42's, and it is proved

    h_pad(λ,δ)  =  Σ_{λ/μ horizontal δ-strip}  a_3(μ, δ)

is **already in the repository**, implemented in `analysis/wk9_s42_hpad.py` and
proved in `docs/reducible_engine.md` §B: the Kempf collapsing
`q : Tot(O(−1) ⊗ Sym³V*) → W` has
`H⁰(Z, O_Z) = ⊕_δ Sym^δ V ⊗ Sym^δ(Sym³ V)`, the Segre-product ring, which is the
normalisation of `C[R_r]` (finite, birational, normal source) — whence
`mult_pad ≤ mult_red ≤ h_pad`, **proved**.  The Pieri sum is then
`s_{(δ)}·s_μ = Σ_{λ/μ horiz. δ-strip} s_λ` applied to that tensor product.  It
has been computed across the whole census since session 46
(`results/s46_census7_hpad.json`, `s46_census8_hpad.json`) and costs
milliseconds.

This is not a criticism of S3 and it does not reduce the memo's value.  **What
is genuinely new is the reading**, and it is a real upgrade: `h_pad` is not
merely a bound but the *intermediate multiplicity space* of an explicit two-step
map, the deficit `h_pad − mult_pad` is exactly the cubic-permanent kernels, and
quotienting blockwise turns a bound into a construction.  Attribute the identity
to session 42 and the factorization to S3 (house rule 13).

## 3. The number nobody computed — and it could have ended the track

Because `mult_pad ≤ h_pad` is proved, **`D > 0` at the LMR cell requires
`h_pad(LMR) > mult_det = 273`.**  That is a pure plethysm computation: no
ranks, no evaluation points, no engine.  Had it come back at 273 or below,
sessions 63, 64 and 65 would all have been dead before one of them ran.

It was not in the batch plan.  It has now been run
(`analysis/wk10_int_hpad_lmr.py`, log `results/logs/hpad_lmr.log`, 48 shapes,
about 25 minutes):

    h_pad((65,17,2⁷), 24)  =  521          a = 274,  mult_det = 273

**Two readings, and the second is the sharper.**

1. `521 > 273`, so the cheap screen does not exclude an obstruction at LMR.
   The track is alive.
2. `521 > 274 = a`, and `mult_pad ≤ a` always — so **the pad-side ceiling is
   entirely vacuous at LMR.**  The screen that settles cells elsewhere
   (`h_pad = 0` at `(8,4,4,4,4,4)_7` proves `D = −2` outright, whatever
   `mult_det` is) has *nothing at all* to say here.

So LMR is not merely un-excluded; it is beyond the reach of every cheap test the
programme owns.  A rank is genuinely required, which is the strongest available
argument that sessions 63 and 64 are worth their cost.

## 4. Amendments to your task list

**Adopt the exact factorized route as the primary architecture.**

    M^(4)_λ  --S--> ⊕_{λ/μ horiz δ} M^(3)_μ  -->  ⊕_μ M^(3)_μ / ker Θ^{per_3}_{μ,δ}

The split map is universal — factor each quartic into its linear and cubic
parts — and its target is `h_pad`-dimensional, so at LMR the work list is 48
blocks and nothing larger.  `analysis/wk9_s42_hpad.py`'s `pieri_strips` already
enumerates the shapes; `results/logs/hpad_lmr.log` lists all 48 with their
`a_3(μ,24)`.

**Keep `ev_pad` as the fast branch, and understand what it does and does not
give.**  If evaluation of the 274 common-source vectors at padded-permanent
points returns rank 274 modulo one house prime, then `rank_p ≤ rank_Q` gives
characteristic-zero full rank, hence `i_pad = 0`, hence with session 63's
`i_det = 1`, **`D_LMR = 1`** — with none of the exact machinery.  A *deficient*
modular rank proves nothing and must return to the factorized route.  Note the
fast branch is gated on the same wall as session 63: building and evaluating the
common source at `r = 9`, `δ = 24`.  It removes the exact padded machinery from
the critical path; it does not remove the bottleneck.

**Add the kernel calibration, which your brief lacked.**  `(8,4,4,4,4)` at
`δ = 6`, `r = 5`: `a = 2`, `mult_det = 2`, `mult_red = 1`, `h_pad = 1`
(`docs/reducible_ideal.md`, `docs/s60_report.md` §3, `docs/reducible_engine.md`).
So the padded engine must return `mult_pad ≤ 1` — **a genuine kernel in a
two-dimensional source**, which is what every other calibration in your brief
lacks, all of them being full-rank negatives.  State it as the inequality: the
record pins `mult_red = 1` and `h_pad = 1`, so `mult_pad ∈ {0,1}`; an engine
returning 2 is defective.

**Verify the Gram formula yourself at `δ = 2` before using it at scale**, against
the three values in §1.  They are cheap and they are the only independent check
of the padded Gram that exists.

## 5. What has not been checked

The identity `mult_pad = rank[(⊕_μ Θ^{per_3}_{μ,δ}) ∘ S_{λ,δ}]` — that the
composite's rank *is* the padded multiplicity — is the one load-bearing claim of
the memo that is neither reproduced here nor banked in the repository.  It
requires the split map to be exactly the dual of multiplication, and the `r = 5`
calibrations in §4 are what test it.  **Treat it as unchecked until a
calibration confirms it**, and report the calibration before reporting any LMR
number that depends on it.

## 6. A note on process discipline, since it cost me a shell

While ending the background plethysm run I matched on the process name rather
than on the recorded id in `results/logs/hpad_lmr.pid`, and ended my own shell
along with it.  `docs/brief_wording.md` §1 exists for exactly this and the rule
is not ceremonial: **end a run only by its recorded id.**  The run itself was
bounded and its result was already on disk, so nothing was lost.
