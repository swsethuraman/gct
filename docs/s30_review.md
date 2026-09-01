# Integrator review — session 30 (the 62 at `delta = 6`, `ell >= 5`)

2026-09-01.  Branch `s30-sweep62`, tip `19098b3` onto `13fb170`.  Verified
against: my session-29 verification notes, session 26's Jacobian tables,
session 27's ledger, the padded-locus theorem (`docs/l5_containment.md`), and
independent recomputation of every checkable number below.

## 1. Gates, in the pre-committed order

**The witness gate is real, and it is the right witness.**  The calibration
kernel `(12, -3, 1)` on `(c40 c04, c31 c13, c22^2)` is exactly the
`alpha!`-conjugate of the classical binary-quartic invariant's monomial vector
`(1, -4, 3)`: rescaling by `(4!0!·0!4!, 3!1!·1!3!, (2!2!)^2) = (576, 36, 16)`
gives `(576, -144, 48) = 48·(12, -3, 1)`.  Integer for integer, this is the
discriminator my session-29 check derived independently (there normalised as
`(1, -1/4, 1/12)`).  The two rules agree on kernel *dimension* and differ on
kernel *vectors*, so the "41 of 48 discriminate" framing in the session doc is
the correct one to quote — a battery is evidence only through the parts that
could have failed.

**The nine re-certified unchanged (P1).**  With this, the action-rule bug is
fully closed out: sessions 26 and 27 published `a` and `D` values, which the
bug provably cannot touch, and the only rule-sensitive quantities on the record
(the nine `mult` values) are now re-derived under the corrected rule and
unchanged.  No published number anywhere in the programme rests on the wrong
rule.

## 2. Ledger arithmetic — all verified

25 of 62 cells; ambient units 83 of 189 = 43.9% (their 44%).  All weight sums
are 24 (`n = 4`, `delta = 6`).  The interleave commitment was kept: both
`a = 7` cells (the global maximum over all 62, not just the reachable ones)
and the most balanced reachable cell (`(8,7,7,1,1)`, balance 7) were measured.
The sceptical re-run branch never fired because no cell came in below `a` on
either side.  `rank(R) = N_S - a` asserted per cell; `a` agreed with the
plethysm route at every cell.

## 3. The codimension table upgrades from certificate to theorem

The session labels the table a probabilistic certificate (generic Jacobian
rank, three points, two primes).  Assembled with what the programme already
holds, it is better than that:

- **The pad row is theorem-exact.**  `per_3`'s restrictions fill all of
  `Sym^3 C^r` for `r <= 5`: the Jacobian at a single exact point has full rank
  35 at `r = 5` (session 26), and full rank at one point proves dominance —
  that direction is not probabilistic.  So `D_r^pad` is the
  linear-times-cubic locus and the padded-locus formula gives
  `dim = r + C(r+2,3) - 1 = 12, 23, 39` exactly.
- **The det row is pinned by a sandwich.**  The measured Jacobian ranks
  15, 34, 50 are lower bounds; the stabiliser count
  `min(C(r+3,4), 16r - 30)` gives upper bounds 15, 34, 50.  Lower meets upper
  at every `r`, so the dimensions are exact.  The one soft link is the upper
  bound's hypothesis — a generic `r`-tuple of `4x4` matrices has finite
  simultaneous stabiliser in `Stab(det_4)` for `r >= 3` (the `n = 4` analogue
  of Lemma 5b).  That is one page to write, and then the entire table — and
  with it "the two ideals differ at `r = 5`" — is unconditional.

**What the table does and does not force, stated precisely.**
`39 < 50` forces `D_5^det` not to fit inside `D_5^pad`, so the pad ideal
eventually exceeds the det ideal in total size — separation in the `D < 0`
direction.  Session 32's Theorem 5 (`D_5^pad` not inside `D_5^det`) forces the
ideals to differ in the obstruction-relevant direction *as sets*.  Neither
statement yet produces a weight with `mult_pad > mult_det`: set-level
differences and aggregate dimension gaps can coexist with per-weight ties in
kernel dimension.  "A multiplicity obstruction must exist at `r = 5`" is not
yet a theorem, and nothing in this session's write-ups claims it — keep it
that way when quoting.

## 4. Flags — none touching a reported number

(a) **Two RSS constants.**  `session_30.md` §3(c) fits `~5.2e-8·N_S^2` GB;
`sweep62.md` §6 fits `~7.5e-8·N_S^2` from the OOM kills.  The largest
*completed* cell (`N_S = 9224`, 4.8 GB) sits at `5.6e-8`, and at that constant
the next cell up (`N_S = 9882`) needs ~5.5 GB against the 6.5 GB budget —
likely feasible.  The reachability frontier was drawn from the conservative
fit; the "would not start" sentence should not be quoted as a measurement.
Immaterial to the results, and moot under the stop-at-`delta=6`
recommendation.

(b) **The `e` recommendation is endorsed, with a literature-first order.**
The `r = 4` determinantal hypersurface is the surface analogue of a classical
story: for *plane quartics* the corresponding object is the Lüroth
hypersurface, degree 54, whose determination is a famous and nontrivial
classical-modern effort.  Whether the degree of the determinantal-quartic-
surface hypersurface is in the literature should be settled before any
computation is designed; either answer shapes the session.

## 5. Standing after session 30

The `delta = 6` chapter at `r = 5` is closed by argument rather than by
exhaustion: both ideals are empty in every measured component, the dimension
table says they are nonzero varieties' ideals with onsets above `delta = 6`,
and the untested `balance <= 6` corner is honestly labelled expectation.  The
axis is now the degree.  In order: pin `e` at `r = 4` (one number, calibrates
the onset scale), then `delta = 7` at `ell = 5`, cheapest cells first.

## 6. Process record

Five failures, none touching a number; two promoted to standing house rules:
a cleanup routine must know what is still running before it releases anything
(the live-claim release was caught within a minute, but only by eye), and
`pgrep -f`/`pkill -f` self-matching has now cost two sessions — kill by
explicit PID, read back first, never by a pattern that appears in the killing
command line.  The claim-file design that emerged (`O_CREAT|O_EXCL`,
PID-owned, released only when the owner is dead) is the right primitive and
future multi-worker sessions should start from it rather than rediscover it.
