# Pre-registration — session 35 (theory: new attacks on the onset window, delta in [9, 405], ell >= 5)

Committed before any direction is generated, ranked, or tested.  This session
pre-registers the **rubric**, not predictions: the deliverable is a ranked list
of theoretical directions, and the ranking must be against criteria fixed in
advance, so that a direction cannot be promoted after the fact because its
first test happened to go well.

Branch `s35-theory`; clone tip `c02cee8`; ancestry gate
(`git merge-base --is-ancestor 63fe705 HEAD`) passed.  No session-35 collision
found in the record (no `s35`/`session_35` files on `main`).

## 1. The scoring rubric (fixed now, applied later)

Every direction D gets a score

    score(D) = I(D) x P(D) / C(D)

- **I — impact if it works**, 1–5:
  - 5: directly produces an obstruction candidate cell (`D > 0` with the one
    remaining unknown named and attackable), or proves multiplicity blindness
    (`D <= 0`) over a stated degree range of the window.
  - 4: collapses the onset window by an order of magnitude, converts the hunt
    from two unknowns to one at all weights (e.g. pad's ideal weight-by-weight),
    or removes the `N_S` memory wall for a class of cells in the window.
  - 3: a new structural theorem about either ideal that redirects where compute
    should go (new banked constraint on where `D > 0` can live).
  - 2: calibration or anchor result (dates an onset, pins a degree) without
    redirecting the hunt.
  - 1: incremental bookkeeping.
- **P — probability of working**: subjective, but each P must cite the
  mechanism it leans on (a known theorem, a validated pipeline, a literature
  anchor).  "Working" means the direction delivers its stated decisive output,
  in either direction — a clean negative that closes a route counts as working.
- **C — cost of finding out**, in days-to-first-decision in this container:
  the cost of the *first falsifiable test*, not of full development.
  Allowed values 0.5, 1, 2, 4, 8.  Anything whose first test needs more than a
  day is capped at rank by C >= 2; anything needing hardware this programme
  does not have is inadmissible (see discards).

Ranking is by score, descending; ties broken by smaller C, then by larger I.
The two rival global hypotheses — a `D > 0` witness exists in the window
versus multiplicity blindness (`det_units <= pad_units` everywhere reachable)
— are treated as rivals of equal standing: a direction scores the same
whether its decisive output favours one or the other.

## 2. The keep rule (verbatim, per the brief)

**Every direction kept must name a falsifiable first test costing at most a
day in-container, and must state what would kill it.**  A direction with no
kill condition is not a direction; it is a mood.

## 3. Discard criteria (any one suffices)

1. Re-derives a banked result, or re-proposes a killed route: counting /
   dimension-crossover arguments for onset degrees (killed by s31 at `n = 3`;
   the integrator states the same Hilbert comparison kills them at `n = 4`),
   rung-climbing at `r = 4` (closed by s33 at degree ~3.2e5), or sweeping
   `delta <= 8` (owned by compute, s34 in flight).  Per-weight arithmetic
   screens (`a` vs an upper bound on `mult`) are NOT the killed route — that
   mechanism produced the only exactly-pinned ideal components on record
   (s28, `delta = 10`, lengths 8–9) — but any global "dimensions force a
   kernel at degree X" claim is.
2. First test not runnable here: needs more than ~1 day, more than ~7 GB, or
   external compute.
3. Leans on a house failure class without naming and addressing it:
   regime transfer, quotient/hypersurface blindness, shared-spec correlation,
   lowest-invariant bias.
4. Cannot state what would kill it.
5. Contains only a seed (A)–(D) as given in the brief, with nothing sharpened,
   demolished, or added — the brief's own words: a report that contains only
   the four seeds has added nothing.

## 4. Standing discipline inherited

- Exact arithmetic only: ranks by flint `nmod_mat` over the two house primes
  `P1 = 2147483647`, `P2 = 2147483629`; no hand-rolled elimination (two
  sessions' self-tests have failed at it).  Rank claims at random points are
  lower bounds on generic ranks; any generic-rank upper-bound claim must say
  where it comes from (Schwartz–Zippel with stated box, or structure).
- Every computed statement labelled proved / measured / expectation, at every
  occurrence.
- `D = mult_pad − mult_det = det_units − pad_units`; an obstruction is
  `D > 0` at a single cell; `D < 0` is the expected direction and is not an
  obstruction.  Pre-registered verbatim so a pad-side bite cannot drift
  upward in the report.
- Anything found in the literature is adopted-not-certified until re-derived,
  and labelled with its source.
- If a first test of a top-two direction fires in the obstruction direction
  (`D > 0` at a specific cell), this session does NOT declare an obstruction:
  it records the cell, the evidence, and the missing certificate, and stops —
  the s34 obstruction protocol (independent re-derivation by the integrator)
  applies to theory sessions too.

## 5. What the session will not do

No sweeps; no touching single-writer files (`paper/det3-conductor.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html`); no pushes (bundle
delivery only); no renumbering if a session-35 collision surfaces later —
flag and carry on.
