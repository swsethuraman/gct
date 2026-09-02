# Integrator review — session 35 (theory: attacks on the onset window)

2026-09-01.  Branch `s35-theory`, tip `5b068bd` onto `c02cee8` (ancestry gate
`63fe705` passes; cloned fully current).  Both banked results re-verified from
scratch, and the headline's *interpretation* corrected below after a referee-style
control test.

## 1. The catalecticant finding: real arithmetic, but it detects padding, not the permanent

The rank drop is solid and reproduces independently.  Over the prime
`2147483647`, from random data, no shared code:

| F | vars | rank | expected |
|---|---|---|---|
| generic quartic | 5 | 15 | 15 |
| pad `l·c` | 5 | 10 | 10 |
| generic quartic | 4 | 10 | 10 |
| `det_4` pencil | 4 | 10 | 10 |
| pad `l·c` | 4 | 8 | 8 |

and the extremal 9-minor (weight `(10,10,10,6)`, confirmed two ways) is nonzero
at a `det_4` pencil and zero at a pad point.  So there is a genuine covariant in
`I(D_4^pad)_9 \ I(D_4^det)_9`, and `D((10,10,10,6,0),9) <= -1` holds: the two
closure multiplicities are provably unequal.  As a statement about these two
varieties, at exact arithmetic, it is correct.

**But the control test changes what it means.**  The reason `l·c` degenerates
is that a form with a linear factor has second partials confined to
`l·V^* + span{∂c}` — a property of the *linear factor*, and of nothing else.  I
tested `l·q` for arbitrary cubics `q` (three random, a Fermat cubic, a monomial
cubic, and a two-linear-factor form):

```
r = 4:  every  l·(cubic)  -> rank 8   (irreducible quartic -> 10)
r = 5:  every  l·(cubic)  -> rank 10  (irreducible quartic -> 15)
```

The permanent plays no role.  The covariant separates **reducible-with-a-linear-
factor from irreducible**, not permanent from determinant.  And at `ell = 5`
this is not even a contingent fact: the length-5 restriction of the padded
permanent is `l·(arbitrary quinary cubic)` — the permanent's identity is already
washed out by restriction to five variables, exactly as `docs/sweep62.md` §4
notes for the whole `ell = 5` regime.  So no length-5 equation *can* be
permanent-sensitive, this one included.

**What the cell is, stated without inflation.**  It is the first cell where the
pipeline exhibits `mult_pad != mult_det` by exact arithmetic — a real
milestone for the machinery — and it is a legitimate element of `I(D_5^pad)`
(the programme's `D_5^pad` *is* the reducible locus `{l·c}` by definition, so a
covariant cutting reducibility is a pad-side equation by construction).  It
confirms Direction 1's premise concretely: pad's ideal is nonempty, classical,
and begins cheaply (degree 9, five orders of magnitude below the determinant's
own first equation at 320112).  That contrast is worth stating in the paper.

**What the cell is not.**  It is not an obstruction (`D < 0` is the expected
direction — pad's variety is smaller, its ideal wakes first), and it is not
evidence about the permanent.  It should never be written up as "the
determinant and the permanent differ"; the honest sentence is "the reducible
locus is catalecticant-degenerate and the determinant pencil is not," which is
classical in spirit and new only in its explicit weight and cheap degree.  The
obstruction question is untouched, in both directions.

**A forward caveat this exposes, worth banking.**  Because `D_5^pad = {l·c}`
with `c` arbitrary is *larger* than the true padded-permanent orbit closure
`{l·(g·per_3)}`, it has fewer equations, so `mult_pad` here over-estimates the
real target's multiplicity.  A future `D > 0` candidate computed against `{l·c}`
therefore does **not** automatically transfer to the real permanent — it must
be re-checked against the actual orbit, or shown to use permanent-specific
structure.  (`D < 0` cells like this one *do* transfer, since enlarging the
variety only lowers `mult_pad` further.)  This is the precise sense in which
the length-5 framing has washed the permanent out, and it is the thing to keep
honest when the hunt eventually turns up a `D > 0`.

## 2. The soft link is softer than stated — principality is essentially free

The `det_units((10,10,10,6),9) = 0` line was flagged as resting on the
unwritten finite-stabiliser page.  It does not need it:

- `D_4^det` is the image of an irreducible variety (4-tuples of `4x4`
  matrices), hence **irreducible**.
- It is a **proper** subvariety of `Sym^4 C^4`: a generic quartic surface is
  not linear determinantal (Beauville, already cited).  So `dim <= 34`.
- s33's Jacobian rank `34` at a point gives `dim >= 34`.  Hence `dim = 34`,
  codimension exactly 1.

An irreducible codimension-1 subvariety of affine space has a **principal**
prime ideal (the coordinate ring is a UFD).  Its generator spans a `GL_4`-stable
line — a rectangular semi-invariant of weight `(k^4)` — so the ideal's lowest
degree is a *rectangular* rung, and s33 certified no rectangular equation below
degree 10 (`mult = a` at rungs 4,6,7,8; `a(9) = 0`).  Therefore
`I(D_4^det)_9 = 0` in every weight, and `det_units((10,10,10,6),9) = 0`
rigorously — no page, no adopted LLV degree required.  The one-cell direct
measurement remains worthwhile as an independent confirmation and I still
recommend it for s36, but the cell stands on its own now.

## 3. The defect route: arithmetic all confirms

Every number reproduces independently: `deg(rank≤2 in 4×4) = 6·(10/3) = 20`
(codim 4, so a generic `P^4` meets it in 20 points and misses `σ_1`);
smooth `(R/J_F)_7 = [t^7](1+t+t^2)^5 = 30`; cubics in `P^4` number
`C(7,4) = 35`, 20 general points leave 15, measured `h^0(I_Z(3)) = 16` gives
defect 1; factoriality degree `2d−5 = 3` and Jacobian defect degree `3d−5 = 7`
are the right classical degrees, so `(R/J)_7 = 31` reads as defect 1.  The
day-one `18`-vs-`20` bug was the integer-division trap the degree formula sets
(`10/3` must stay rational), caught within the hour by the independent Hilbert
measurement — good process.  The `405 → ~300` cap is honestly labelled as
evidence-plus-mechanism with two open dependencies, and the session itself notes
those covariants vanish on pad too, so they move the ceiling without separating.
The durable product is the **structural identification**: `D_5^det` sits inside
the non-Q-factorial 20-nodal locus, the clean `n = 4` analogue of the `n = 3`
six-nodal story, and it is on firm ground.

## 4. The ranked program is the session's real value — with a re-rank

Seven directions scored against a rubric committed first (`db40e1c`, before any
direction).  My steers, sharpened by the control test above:

- **Direction 1 (pad ideal by Kempf collapsing, 7.0) still leads**, but its
  framing needs §1's correction baked in: it computes the ideal of the
  *reducible locus*, which is a classical object and largely permanent-agnostic
  at `ell = 5`.  Its value is real but is *efficiency* (pad side by table
  lookup, no `N_S` wall), not *insight into the permanent*.  Fund it as a tool,
  not as a source of obstructions.
- **Direction 3 (mine DIP) I would move to the top and run first.**  It is the
  only place the thing we are hunting was actually exhibited, it is pure reading
  with no compute risk, and — this is the point the catalecticant episode makes
  sharp — DIP's whole contribution is separating the *split/reducible* structure
  from the target in a way that survives being about the actual object.  That is
  exactly the gap §1 exposes in our own pad-side finding.  Their technique is
  the one most likely to tell us whether a permanent-*sensitive* separator can
  exist at all at these lengths, or whether everything cheap is reducibility.
- **Direction 5 (blindness half-theorem) quietly banked a real partial result**:
  `D <= 0` on the whole `ell <= 4` slab through degree 9 is now a theorem (length
  theorem + s33), with strict cells exhibited.  That belongs in paper 2 whether
  or not the `ell = 5` half ever closes.

## 5. Standing after session 35, corrected

The window `[9, 405]` gained a defect-identified, evidence-capped ceiling near
300 (real structure) and a proved-but-shallow `D < 0` cell at the bottom whose
mechanism is reducibility, not the permanent (milestone for the machinery, not
for the mathematics of separation).  The obstruction question is untouched in
both directions.  The genuine lesson the session hands forward is the one the
control test forces: **at `ell = 5` the permanent has already been replaced by an
arbitrary cubic, so no separator found there can be permanent-specific — the
permanent only re-enters at lengths where the cubic factor has room to carry its
structure.**  That reframes the hunt and is worth its own line in the s36 brief.

For s36, in order: (1) the DIP reading pass — cheapest, and it calibrates
whether the whole `ell = 5` hunt can ever be permanent-sensitive; (2) stand up
Direction 1's Koszul route against the s30 `mult_pad` anchors, sold as an
efficiency tool; (3) the one-cell `mult_det((10,10,10,6),9)` confirmation, now
insurance rather than necessity.  Process on s35 itself was exemplary — rubric
pre-registered before ideas, both tests run with exact arithmetic, the one bug
caught by an independent measurement and recorded, single-writer files
untouched.  The correction here is to its *interpretation*, not its conduct.
