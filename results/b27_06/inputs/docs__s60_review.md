# Integrator review — session 60, the balanced length-5 complement and the closing sweep

**Accepted.**  The delivery is intact, the census and the ladder arithmetic
reproduce here independently, and the session did the harder of the two
available things: it turned a sampling sweep into a closure programme
mid-flight and produced **the first permanently closed length-5 tails in the
programme**.  One caveat belongs beside the headline (§3) and one correction of
mine belongs in the record (§4).

## 1. Delivery

Bundle delivered in two parts.  `md5` of each part and of the reassembled
bundle match the manifest (`43766776cc6d6b37fd617e8efe7d8cdd`).  Four commits,
pre-registration `c308f306` before any multiplicity.  No single-writer file
touched, no blob over the limit (largest 1.27 MB), no session link in any
commit, `Co-Authored-By` on each.  Verifier report as committed:
**PASS 362, FAIL 0, UNPARSEABLE 0, ERROR 0**.

## 2. Reproduced independently

Everything below was computed here, with my own code, before this was written.

| claim | reproduced |
|---|---|
| census sizes: length-5 cells with `a > 0` at `δ = 6…9` | **105 / 239 / 435 / 708** — my own enumeration of the 164 / 291 / 480 / 748 partitions into exactly 5 parts, `a` by Kostant alternation |
| `a` at all twelve reducible-bite cells | **12 / 12 exact** |
| `n_χ = N_S` when the parts of `λ` are distinct | **4 / 4 exact**, including `(10,8,7,6,5)_9` at **39 069 764** |
| `N_S` column of the ledger at repeated-part cells | **7 / 7 exact** |
| the tail census: `t`, `a_∞`, `δ_close` | **1 075 / 1 075 identical** to my independent length-5 ladder census |
| `λ_1 ≥ 3δ` at a closing cell | **0 of 1 075**, matching 0 of 2 107 here |

The tail agreement is the one that matters most: two independently written
ladder computations, one by plethysm DP here and one by the session's own
`wk9_s60_tails.py`, agree on the stable value and the closing degree of every
tail in the census.  With the ladder theorem proved, that makes the 99 closures
statements about every degree, not just the measured ones.

## 3. The caveat that belongs beside the headline

"`mult_det = a` at every one of the 419 measured cells" is the result, and it is
right to lead with it.  But **264 of those 419 rest on the algorithmic
single-prime nonsingularity certificate and carry no `gct-cert/1` file**; 155 do
(§7 of the report).  The session says this plainly in §7 and §9 and registered
the gap in the pre-registration rather than discovering it afterwards, which is
the right handling — but the two numbers should travel together whenever the 419
is quoted.  The 362 verifier passes cover the dense-route cells; the sparse-route
proofs are reproducible from the recorded seeds and levels and are not
independently checked by anything.

Adding a `gct-cert/1` kind for the Wiedemann nonsingularity certificate — the
seeds, the levels, the pinned evaluation rows, the checked kernel candidates —
is now the single highest-value change to the certificate format, because it
would convert 264 algorithmic proofs into checkable ones and every future sparse
cell with them.

## 4. A correction of mine, for the record

Mid-session I reported the `n_χ` column as defective and low by 2–5×, and asked
for it to be replaced.  **That was wrong.**  What I had computed was `N_S`, the
full weight-space dimension; `n_χ = dim V_χ` is the stabiliser reduction and is
the column count of the matrix actually ranked.  The tell was in my own data —
every distinct-part weight agreed exactly, every repeated-part weight did not —
and I read past it.  The session was right to keep its values, and its ledger
now states the distinction explicitly ("the two are never the same quantity
unless `Stab` is trivial"), which closes the ambiguity.  Verified here after the
fact at eleven cells: `N_S` matches the ledger's `N_S` column at seven
repeated-part cells, and `n_χ = N_S` exactly at the four distinct-part cells.

The practical consequence is in my direction's favour and I understated it: the
closure queue I sent was sorted by `N_S`, and re-sorting by `n_χ` makes the cheap
end **far** cheaper than I claimed — `(12,2,2,2,2)_5` is `n_χ = 56`, not 553.
The session's own table is the right one to walk: 34 tails close at `n_χ ≤ 3000`,
73 at `≤ 10 000`, 127 at `≤ 30 000`, **199 at `≤ 100 000` settling 775 census
rungs**.

## 5. What the session established, in order of weight

1. **99 permanently closed tails** — 57 by a closing-cell rank at `δ_close` from
   5 to 17, 42 by census cells that already sat at or above their tail's
   `δ_close`.  These are the first length-5 statements that hold in *every*
   degree, and the first length-5 measurements above `δ = 10` at all.
2. **`δ = 6` is complete** at every balance — 105 cells, the "only skewed weights
   were measured" objection closed outright at that degree.
3. **The three-type classification** — 98 empty (`i_det(∞) = i_red(∞) = 0`), 1
   reducible-first (`(4,4,4,4)`, `i_red(∞) = 1`), **0 of the type that could host
   `D > 0`**.  This is more useful than balance and should be the organising
   table of any successor.
4. **`h_pad` is not tight at length 5 either.**  Eleven cells with
   `mult_red < a`, eight strictly below the bound, six with `h_pad ≥ a` so the
   bound would have allowed full rank.  M3 refuted, and the same failure s47
   found at length 6.  `docs/reducible_engine.md` §B's "exact where it fires" is
   now false at both lengths; flagged, not edited, correctly.
5. **Orientation.**  All 419 measured cells satisfy `i_det ≤ i_red`, eleven
   strictly — the inequality `R_5 ⊆ D_5` implies.  The multiplicity record leans
   toward containment; s59's geometry leans away.  The session states this
   without pretending it is a contradiction, and §4 explains why the balanced
   region can never be more than a sample.

## 6. Small things

- §0's "465 of the 2 506 census cells are settled beside the 362 measured
  directly" is ambiguous about whether the 465 includes the 362.  The per-degree
  columns sum to 362 measured and 367 tail-settled, so the two sets overlap; say
  which number is the union.
- The int64 multiset code overflows at `δ ≥ 19` and blocks the closing cells of
  **183 tails**.  A hashed or two-word monomial code is the one change that
  unblocks them, and it belongs in the successor's brief as a named engineering
  deliverable rather than a footnote.
- Starting `E_red` at compression level `(12,2)` rather than `(3,2)`: take it.
- B3 was refuted by over-delivery (13.7 % of the `δ = 9` complement against a
  predicted `< 10 %`), which is the good kind.

## 7. Verdict

Accepted and merged.  The successor on this track is not another balanced sweep
— §4 of the report proves that cannot close anything — but a walk down
`results/s60_tail_census.md` in `n_χ` order, closing tails at a few minutes each,
with the int64 monomial code fixed so the 183 deep tails come into range.  On
present evidence that closes on the order of 200 tails for the cost of the last
few hours of this session, and every one is a statement about all degrees.
