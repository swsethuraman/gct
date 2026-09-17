# B19-05 — Intake: every existing exclusion and screen, reconciled in one table

**Worktree start state** (recorded before any write, per preamble):

```
git rev-parse HEAD          ca3d6d807e70e74069816f558d7d0b9b11cb7272
git rev-parse HEAD^{tree}   2fcc712f1cae827a4185c6e9aea318eac725dd48
```

**Status line:** COMPLETE (intake). Written incrementally; §6 is the closing ledger.

## 0. Plain terms

Slots 01 and 02 have not reported, so no candidate is assessed here and **nothing is
nominated**. What this document does is put every cell the programme has already
closed, and every screen it has already run, into one table with the argument that
closes each, the degree, and which of `a`, `s`, `U`, `b`, `q` is actually known there.
Where a value is not known it is written `unknown`. Where a value was carried from one
regime to another (a stable tail value used at a finite degree; a five-variable
identification used above five variables; an inherited completeness premise), the
row says so and says whether the justification still holds.

Three things came out of the reconciliation that the batch should know before 01/02
report:

1. **The ten ten-row cells are excluded by two different strengths of argument.** The
   `d = 27` cell has a determinant *evaluation* floor `m_det >= 418 > U = 288`, which
   excludes it unconditionally (given `U`). The other nine have exact `m_det` only
   under the inherited B15 premise that the finite determinant ideal is the stable
   ideal intersected with the finite filtration (the "S57" identification). Under that
   premise `i_det` is exact and the exclusion holds; without it, `i_det` is a floor
   and a floor excludes nothing. Both the B17-12 closeout and the B18-12 ledger say a
   version of this, but they say opposite versions (B17-12: "exact, conditional";
   B18-12: "floor, `m_det` unknown"). The table below records the premise explicitly
   so both readings are reconciled rather than averaged.
2. **All 23 degree-five five-row cells and 4 degree-six five-row cells are closed at
   the cell level**, with `D = 0` exactly in 26 of the 27 and `D <= 0` in the
   rectangle `(4^5)`. These are the only cells in the admissible range 5–10 closed
   by a *lower* bound on `m_det`, and they are closed because `a = 1` (or `a = 2`)
   made one evaluation decisive. `s`, `U`, `b`, `q` are irrelevant to those closures
   and are recorded only where they happen to be on disk.
3. **Every screen in the tree is a screen, not an exclusion**, and the table labels
   each one by exactly what it retired.

The one outstanding batch-18 item assigned here, the degenerate generic-quartic
control of B18-05, has been re-run with full monomial support and is now a
non-vacuous check: see §5 and the addendum appended to `docs/b18_05_report.md`.

## 1. Sources read, with what each is used for

| Source | Path | Used for |
|---|---|---|
| B19 preamble, board §05, slot brief | `Claude_Handover_B15_B18/batch19_launch/`, `BATCH19_PROPOSED_BOARD.md` | rules, conventions, gate |
| B18-12 ledger | `B15-12/docs/b18_12_ledger.md` §§1, 2b, 4a–4c | the ten cells as last recorded; the accepted base |
| B17-12 initial ledger and closeout | `B15-12/docs/b17_12_report.md`, `b17_12_closeout.md` | the ten cells' provenance and the direction rules |
| B15–B17 summary | `Claude_Handover_B15_B18/SUMMARY_B15_B17.md` | the four B16 cells, the six B17 screens, the degree-7 screen |
| Batch 16 stocktake and intake | `Batch16/STOCKTAKE.md`, `Batch16/INTAKE.json` | what B16 accepted about the four cells and the tail filtrations |
| B16-04 proof | `B15-04/docs/b16_04_proof.md` | the completeness premise behind "exact `i_det`" |
| B18-06 sweep and report | `B15-06/docs/b18_06_sweep.md`, `b18_06_report.md` | the 23 degree-five and 4 degree-six cells; the degree-7 screen's admissible rows; census facts |
| B18-05 report and evaluator | `docs/b18_05_report.md`, `analysis/b18_05_psi.py` | the degenerate control (§5) |

Nothing from slots B19-01 or B19-02 was read; neither exists yet.

## 2. The reconciled table

Conventions for every row. `a` first, always. `q` = a certified global ideal
**floor** (`i_det >= q`, from equations valid on the whole closure). `i_det` is
written as exact only where the source proves exactness and the row names the
premise. `m_det` lower bounds come from evaluations at actual determinant points
(`r_det`); `m_det` exact means `r_det = a - q`. `U = min(a, T)` with `T` the
product-map target multiplicity; a `T` quoted from the Astra census is the
five-variable product ceiling, valid as an exact ceiling for five-row cells by the
accepted B17-08 identification, and only a (larger-family) ceiling for six or more
rows. `s` = symmetric rectangular Kronecker, transposition included, quoted only
where a source computed it as such. `b` = certified boundary rank; no cell anywhere
has `b >= 1`, so `b = 0` in every row and the column is omitted. Closure label:

- **CLOSED-U** : unconditional given the named `U`: a determinant evaluation floor
  `r_det >= U` (or `r_det = a`).
- **CLOSED-P** : closed under a named inherited premise, stated in the row.
- **CLOSED-Z** : closed by `i_pad = a` (padding side vanishes), `D <= 0` with
  `m_det` unknown.
- **SCREEN** : the row's certificate route is retired; `D` is not bounded.
- **OPEN** : named in a source, not closed.

### 2.1 Regime facts (not cells)

| Regime | Statement | Argument | Label |
|---|---|---|---|
| every `lambda` with `ell(lambda) <= 4`, every `d` | `K_det ⊆ K_pad`, so `D <= 0` | B17-03 main theorem (accepted 03-C) | CLOSED-U (theorem) |
| every `lambda` with `ell(lambda) > 10`, every `d` | `m_pad = 0`, so `D = -m_det <= 0` | ten essential variables of `z·per3` (B15-12 scope correction, B17-03) | CLOSED-Z (theorem) |
| `ell(lambda) = 5`, some `d <= 4^49` | a determinant equation not vanishing on padding exists | B17-01 + B17-03 + B18-01 Thm E (accepted by slot 10) | separation only; **no sign for `D`** |
| `6 <= ell <= 10` | no theorem either way; the padding variety at length `L` is `P_L`, dimension `10L - 5` for `L >= 6`, not all linear x cubic | B18-10 §9 (accepted, B19 preamble) | OPEN regime |

### 2.2 The ten ten-row cells, `lambda = (4d - t - 16, t, 2^8)`

Common premise **P-S57**: the finite determinant ideal in these cells equals the
stable ideal intersected with the finite ambient filtration (B15's "S57"
identification), together with the stable tail-19 equality `429 - 418 = 11`
(stable `a`, a determinant evaluation floor 418, eleven global equations). Under
P-S57 the B16-04 filtration dimensions are the *complete* ideal in each finite
cell (B16-04 §§4–5; B16 INTAKE line 55; SCREEN_REPORT §"Six nearby finite cells").
Without P-S57 they are floors `q`, and a floor excludes nothing. `U` is the
split-cubic source ceiling (B16-12 ring-map review, Kadish–Landsberg product map),
stable value carried to each finite degree; the B17 planning screen recomputed the
finite ambient corrections and states the ceilings as inherited from B16 — I did not
find a per-degree recomputation of `T` and record the carry as part of the premise.

| d | t | `a` (source) | `q` (floor, PROVED globally) | `i_det` exact? | `m_det` | `r_det` (evaluation floor) | `U` | `s` | `D` bound | Label |
|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---|
| 23 | 15 | 189 (B16-02) | 1 | yes under P-S57 | 188 under P-S57 | none recorded | 158 | unknown | `<= -30` | CLOSED-P |
| 25 | 17 | 294 (B16-02) | 4 | yes under P-S57 | 290 under P-S57 | none recorded | 218 | unknown | `<= -72` | CLOSED-P |
| 26 | 17 | 294 (B16-02) | 4 | yes under P-S57 | 290 under P-S57 | none recorded | 218 | unknown | `<= -72` | CLOSED-P |
| 27 | 19 | 429 (B15-06, B16-02) | 11 | **yes** (floor 11 + `r_det = 418`) | **418 exact** | **418** (B15-06 pilot, replayed at two primes) | 288 | unknown | `<= -130`; padding floor 243 gives `D in [-175, -130]` | **CLOSED-U** |
| 23 | 17 | 292 (B17 planning, finite correction -2) | 2 | yes under P-S57 | 290 under P-S57 | none recorded | 218 (carried) | unknown | `<= -72` | CLOSED-P |
| 24 | 17 | 293 (finite correction -1) | 3 | yes under P-S57 | 290 under P-S57 | none recorded | 218 (carried) | unknown | `<= -72` | CLOSED-P |
| 23 | 19 | 419 (finite correction -10) | 4 | yes under P-S57 | 415 under P-S57 | none recorded | 288 (carried) | unknown | `<= -127` | CLOSED-P |
| 24 | 19 | 424 (finite correction -5) | 7 | yes under P-S57 | 417 under P-S57 | none recorded | 288 (carried) | unknown | `<= -129` | CLOSED-P |
| 25 | 19 | 427 (finite correction -2) | 9 | yes under P-S57 | 418 under P-S57 | none recorded | 288 (carried) | unknown | `<= -130` | CLOSED-P |
| 26 | 19 | 428 (finite correction -1) | 10 | yes under P-S57 | 418 under P-S57 | none recorded | 288 (carried) | unknown | `<= -130` | CLOSED-P |

**Reconciliation note.** The B17-12 ledger writes "exact `i_det`, exact `m_det`,
conditional on the accepted global ideal completeness". The B18-12 ledger writes
"`i_det` (floor)" and "`m_det` unknown (`<= 290`)" for the six B17-screen rows while
keeping the same `D` upper bounds. The second is internally inconsistent: with a
floor only, `m_det <= a - q` is an upper bound on `m_det`, and `D <= U - m_det`
needs a lower bound. Both are reconciled by the P-S57 column: the six rows are
closed exactly as strongly as the four B16 rows (all under P-S57), and one row,
`d = 27`, is closed unconditionally. P-S57 is a B15 premise accepted through every
batch since; nothing in the tree contradicts it; it has not been re-proved in B18
or here. **The ten cells stay closed. Do not rank-hunt here.** What changes is only
the label a later session should copy.

### 2.3 Other inherited exact cells outside the admissible range or at its edge

| d | lambda | `ell` | `a` | `i_det` | `m_det` | `U` / `m_pad` info | `s` | `D` bound | Argument | Label |
|---:|---|---:|---:|---:|---:|---|---|---:|---|---|
| 14 | (21,21,2^7) | 9 | unknown | 0 | `= a` | none | unknown | `<= 0` | B16-07: determinant ideal 0 in this rung | CLOSED-U |
| 15 | (25,21,2^7) | 9 | unknown | 0 | `= a` | padding **ideal** floor 3 (transport) | unknown | `<= -3` | B16-07 | CLOSED-U (`D = -i_pad`) |
| 24 | (65,17,2^7) | 9 | unknown (not extracted) | 1 (inherited CI73) | `a - 1` | `i_pad in [4,5]` (u^10 transport of a degree-14 five-space) | unknown | `[-4, -3]` | B15-01, under transport premises | CLOSED-P |
| `>= 16` | tail (21,2^7) ladder | 9 | stable 533 | stable 4 | stable 529 | — | unknown | `<= 0` for `d >= 16` | B15-05 stable ideal 4 + B15-01 four transported padding equations; "if Slot 01's premises pass" (B15 stocktake item 5) | CLOSED-P (conditional cross-family) |
| 19 and `delta >= 19` | (4δ-19,4,3,2^6) | 9 | 2 | 0 | 2 (exact minor) | `m_pad <= a` only | unknown | `<= 0` | B16-09, stable identification inherited | CLOSED-U at `d = 19`; CLOSED-P for the family |
| 8 | (13,11,3,2,1,1,1) | 7 | 2 | 0 | 2 | `m_pad = 2` (exact padding minor) | 2442 | **`= 0`** | B15-03 | CLOSED-U |
| 8 | (12,11,4,2,1,1,1) | 7 | 3 | 0 | 3 | `U = 3` | 4545 | `<= 0` | B15-04 | CLOSED-U |
| 8 | (11,11,5,2,1,1,1) | 7 | 4 | `<= 1` | `>= 3` | `U = 3` | 4347 | `<= 0` | B15-04 (`r_det = 3 >= U`) | CLOSED-U |
| 7 | nine cells (11,8,5,1^4), (13,5,5,2,1^3), (15,4,2,2,2,2,1), (13,6,3,3,1^3), (12,8,3,2,1^3), (13,7,2,2,2,1,1), (11,9,3,2,1^3), (12,7,4,2,1^3), (14,5,3,2,2,1,1) | 7 | 1 each (inherited count) | 0 | 1 | none needed | 1168, 1227 for the first two (B15-12); others unknown | `<= 0` | B15-02: exact nonzero integer value of the unique highest-weight vector at a determinant point | CLOSED-U |
| stable, `r = 7, 8`, `t = 21` and 20 lower odd tails at `r = 7, 8` | families | 7, 8 | 378 / 460 stable | 0 | `= a` (full rank) | pad floors 372 / 443 | unknown | `<= 0` every valid rung | B15-06 full-rank pilots + ideal-multiplication transport (proof C6), stable theorem inherited | CLOSED-P (family; per-rung `a` unknown here) |

`a` for the B15-02 cells is "inherited ambient-one counts" (B15 stocktake); the
sweep-style in-script recount that B18-06 introduced was not done for them, and I
record that rather than assert it. For (12,4,4,4,4,4) at `d = 8` B15-12 lists
`a = 4`, `U = 1`, `s = 804` and an "inherited `r_det_lb = 4`"; if that floor is
accepted, `D <= 1 - 4 = -3` (CLOSED-U); I did not locate the floor's source and
leave the row at **SCREEN + unlocated floor**. (11,10,6,2,1,1,1) at `d = 8`
(`a = 7`, `U = 4`, `s = 10463`) is **OPEN**: B15-12 only shows `s >= a`.

### 2.4 The 23 degree-five five-row cells (all closed at cell level)

`a = 1` in every cell, recomputed in-script by B18-06's Weyl alternant for the 19
swept cells, recomputed by the B18-06 review for the P1 cells, and from the Astra
census for `(4^5)`. `s` and `T` from the Astra census (`s = (g + t)/2` with `g`
ordinary and `t` the transpose trace, i.e. the symmetric coefficient as the preamble
defines it); `U = min(a, T)`.

| lambda | `a` | `s` | `T` | `U` | `m_det` | `m_pad` | `D` | Closed by | Label |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| (12,2,2,2,2) | 1 | 8 | 2 | 1 | 1 | 1 | **0** | Prop. 4.1 (Hessian covariant) + P1 C0 + sweep R02 | CLOSED-U |
| (9,7,2,1,1) | 1 | 15 | 2 | 1 | 1 | 1 | **0** | P1 C1 + sweep R01 | CLOSED-U |
| (7,7,4,1,1) | 1 | 19 | 2 | 1 | 1 | 1 | **0** | P1 C3 | CLOSED-U |
| (11,4,2,2,1) | 1 | 25 | 5 | 1 | 1 | 1 | **0** | sweep S01 | CLOSED-U |
| (10,5,3,1,1) | 1 | 32 | 4 | 1 | 1 | 1 | **0** | sweep S02 (first padding point was a recorded zero; second nonzero) | CLOSED-U |
| (10,5,2,2,1) | 1 | 36 | 7 | 1 | 1 | 1 | **0** | sweep S03 | CLOSED-U |
| (8,7,3,1,1) | 1 | 23 | 3 | 1 | 1 | 1 | **0** | sweep S04 | CLOSED-U |
| (9,5,4,1,1) | 1 | 35 | 5 | 1 | 1 | 1 | **0** | sweep S05 | CLOSED-U |
| (9,6,2,2,1) | 1 | 39 | 7 | 1 | 1 | 1 | **0** | sweep S06 | CLOSED-U |
| (8,5,5,1,1) | 1 | 23 | 2 | 1 | 1 | 1 | **0** | sweep S07 | CLOSED-U |
| (10,4,2,2,2) | 1 | 35 | 5 | 1 | 1 | 1 | **0** | sweep S08 | CLOSED-U |
| (9,5,3,2,1) | 1 | 77 | 8 | 1 | 1 | 1 | **0** | sweep S09 | CLOSED-U |
| (9,4,4,2,1) | 1 | 51 | 6 | 1 | 1 | 1 | **0** | sweep S10 | CLOSED-U |
| (8,6,3,2,1) | 1 | 77 | 7 | 1 | 1 | 1 | **0** | sweep S11 | CLOSED-U |
| (8,5,4,2,1) | 1 | 89 | 9 | 1 | 1 | 1 | **0** | sweep S12 | CLOSED-U |
| (8,6,2,2,2) | 1 | 44 | 5 | 1 | 1 | 1 | **0** | sweep S13 | CLOSED-U |
| (7,6,4,2,1) | 1 | 75 | 6 | 1 | 1 | 1 | **0** | sweep S14 | CLOSED-U |
| (7,5,4,3,1) | 1 | 80 | 4 | 1 | 1 | 1 | **0** | sweep S15 | CLOSED-U |
| (8,4,4,2,2) | 1 | 66 | 3 | 1 | 1 | 1 | **0** | sweep S16 | CLOSED-U |
| (7,4,4,4,1) | 1 | 25 | 2 | 1 | 1 | 1 | **0** | sweep S17 | CLOSED-U |
| (6,6,4,2,2) | 1 | 52 | 2 | 1 | 1 | 1 | **0** | sweep S18 | CLOSED-U |
| (6,4,4,4,2) | 1 | 34 | 1 | 1 | 1 | 1 | **0** | sweep S19 | CLOSED-U |
| (4,4,4,4,4) | 1 | 5 | **0** | **0** | unknown | **0** | `<= 0` | B18-01 Prop. 8.4 (null cone, `i_pad = 1 = a`), independently `T = 0` in the census | CLOSED-Z |

Every `D = 0` here is exact: `m_det >= 1` and `m_pad >= 1` by exact nonzero integer
values of an exactly verified highest-weight vector at substitutions checked to be
restrictions of invertible ones, with `a = 1`. These are the only cells in the
programme where `D` is known exactly to be zero by evaluation on both sides. The
sweep (19 cells) was released after the B18-06 review; its acceptance at batch level
is the B19 preamble's "all 23 degree-five five-row cells are excluded", and its
per-cell certificates are `B15-06/results/b18_06_sweep/S01..S19.json`. No separate
slot-10 review of the 19 is on disk; I record that, not a doubt.

### 2.5 The four degree-six five-row cells, and the Prop. 4.1 family

| d | lambda | `a` | `s` | `T` | `U` | `m_det` | `m_pad` | `D` | Closed by | Label |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 6 | (16,2,2,2,2) | 1 (census; review recount) | 8 | 3 | 1 | 1 | 1 | **0** | Prop. 4.1 | CLOSED-U |
| 6 | (15,3,2,2,2) | 1 | 15 | 5 | 1 | 1 | 1 | **0** | P1 C2 (modular nonzero minors on actual substitutions) | CLOSED-U |
| 6 | (11,9,2,1,1) | 1 | 22 | 3 | 1 | 1 | 1 | **0** | P1 C4 | CLOSED-U |
| 6 | (14,4,2,2,2) | 2 | 45 | 10 | 2 | 2 | 2 | **0** | P1 C5 (all six 2x2 minors nonzero, both sides) | CLOSED-U |
| 7 | (20,2,2,2,2) | 1 (ADOPTED: degree-7 screen `a < 2`, Prop. 4.1 `a >= 1`) | unknown | unknown | unknown | 1 | 1 | **0** | Prop. 4.1 | CLOSED-U with `a` ADOPTED |
| `d >= 8` | (4d-8,2^4) | not certified | unknown | unknown | unknown | `>= 1` | `>= 1` | `<= a - 1` | Prop. 4.1 | not closed unless `a = 1` |

P1's `D = 0` verdicts are modular (nonzero minors mod `p` of an integral kernel whose
reduction was shown to have dimension exactly `a`), which is the valid direction:
a nonzero residue is a nonzero integer. `a` for the P1 cells was independently
recomputed by the B18-06 review. Degree six has 105 five-row cells (38 with `a = 1`)
and 59 six-row cells; **101 five-row and all 59 six-row degree-six cells are OPEN**,
including the two B18-06 named but did not run: (8,7,7,1,1) (`a = 2`, `s = 30`,
`T = 2`, `U = 2`; over the memory cap for P1's method) and the six-row (14,2^5)
(`a = 1`, `s = 13`, `T = 2`, `U = 1`).

### 2.6 Screens (nothing here bounds `D`)

| Screen | Range | What it computed | What it retired | What it did not | Source |
|---|---|---|---|---|---|
| Astra symmetry census | `d = 5, 6`, every cell of every length (95 and 299 cells) | `a`, ordinary `g`, transpose trace, `s`, `T`, `U = min(a,T)` | nothing: `symmetry_deficit_cells = 0` (no cell has `s < a`) and `headroom_cells = 0` (no cell has `U > min(a,s)`), so the symmetry-only certificate `B = min(a,s) < U` is unavailable in every cell at these degrees | any `D`; any boundary loss `b` | `Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json` |
| degree-7 symmetry screen | `d = 7`, tails of size `<= 10`, length 2–6, `a >= 2`: 114 shapes, 31 eligible | same quantities, `B = min(a,s)` | the symmetry-only certificate with `b = 0` in those 31 shapes; **only two** of the 31 have length 5–10: (18,5,2,2,1) `a = 2, U = 2, g = 93, s = 53`; (18,4,2,2,2) `a = 3, U = 3, g = 61, s = 47` | any `D`; boundary improvements; all other degree-7 cells; 29 of 31 rows were already closed by B17-03 | `Batch17_Planning/degree7_screen.json`; B18-06 §1.3 |
| B17 finite screen | the six `2^8` cells of §2.2 | finite `a` corrections; carried `q`, `U` | the six cells (under P-S57) | — | `Batch17_Planning/finite_screen.json`, SCREEN_REPORT |
| B15-12 seven-cell symmetric bound | `d = 7, 8`, seven cells | `g`, `s`, `U_det = min(a,s)`, `U_pad` | nothing by itself: `s > a` in all seven | — | B15-12 |
| B17-08 E24 generation route | all degrees | types of polynomial multiples of the nine-row generator | that one generation route from five to eight rows | the full determinant ideal (B17-01/03 prove five-row equations exist) | B17-08, accepted 04_08 |
| B18-06 Lemmas 3.1–3.2 | all degrees | types of every certified det4 equation in the tree and of Hessian `k`-minors, `k >= 9` | those mechanisms from lengths `<= 8` | the full ideal | B18-06 |
| B18-06 §1.4 | `d = 5, 6` lengths 5, 6 | `b_required = s - U + 1` ranking | nothing; it is a price list (minimum 8 at (12,2^4), 15 at (9,7,2,1,1), both since closed) | — | B18-06 |
| B18-05 rank | the eleven-equation restriction at `d = 27`, tail 19 | restriction rank of `E` on actual padding | the question "9 or 10" (exactly 9, under recorded premises; now with a non-vacuous control, §5) | any multiplicity; the cell was already closed | B18-05 + this intake |

### 2.7 Cells named in a source and **not** closed (for the record, not as candidates)

| d | lambda | `ell` | `a` | `s` | `U` | Why it is open | Source |
|---:|---|---:|---:|---:|---:|---|---|
| 6 | (8,7,7,1,1) | 5 | 2 | 30 | 2 | P1 excluded it for memory; not swept | B18-06 §6.1 |
| 6 | (14,2,2,2,2,2) | 6 | 1 | 13 | 1 | six rows; not run | B18-06 §6.1 |
| 6 | the other 100 five-row and 58 six-row cells | 5, 6 | census | census | census | never tested | Astra census |
| 7 | (18,5,2,2,1) | 5 | 2 | 53 | 2 | symmetry screen only | degree-7 screen |
| 7 | (18,4,2,2,2) | 5 | 3 | 47 | 3 | symmetry screen only | degree-7 screen |
| 8 | (11,10,6,2,1,1,1) | 7 | 7 | 10463 | 4 | symmetry screen only | B15-12 |
| 8 | (12,4,4,4,4,4) | 6 | 4 | 804 | 1 | closed only if the inherited `r_det_lb = 4` is accepted; source not located here | B15-12 |
| 8 | B15-03 secondary cell | ? | 4 | unknown | `<= 2` (`h_pad = 2`) | counted, never evaluated; partition not extracted in this pass | B15-03 §"secondary" |

None of these is nominated. The gate forbids it, and nothing in this table
supplies a reason: every open cell has `s >= a`, hence `B = min(a, s) = a`, hence
no headroom without a certified `b`, and no cell has a `b`.

## 3. Direction of inference, checked per argument type, and every conflict resolved

**Argument types in §2 and their direction.**

- *Determinant evaluation nonzero* (`r_det`): a nonzero exact integer, or a nonzero
  residue mod `p` of an integral quantity, at a point that is an actual restriction
  of `det4`, gives `m_det >= r_det`. Lower bound on `m_det`, upper bound on `D`.
  Correct in B15-02/03/04/06, B16-09, B18-06 P1 and sweep, Prop. 4.1. ✓
- *Global ideal floor* (`q`): equations proved on the whole closure give
  `i_det >= q`, i.e. `m_det <= a - q`. This bounds `D` from **below**, never above.
  Used as an exclusion only when combined with exactness (P-S57) or with an
  evaluation floor; §2.2 labels each row accordingly. ✓ after relabelling.
- *Padding ceiling* (`U`): `m_pad <= U`. Excludes only against a determinant
  **floor** `>= U`. ✓ everywhere it is used; the B18-06 §1.4 and degree-7 rows use
  it only as a screen.
- *Padding vanishing* (`i_pad = a`): `m_pad = 0`, so `D = -m_det <= 0`. ✓ for
  `(4^5)` and for `ell > 10`.
- *Symmetry bound* (`s`): `m_det <= min(a, s)`. Upper bound on `m_det`; **cannot
  exclude**; a screen only. Every source in §2.6 says so. ✓
- *Sampled zero*: never used as an exclusion anywhere in §2. The one recorded
  sampled zero (sweep S02, first padding point) was superseded by a nonzero. ✓

**Conflicts between sources, and the resolution adopted here.**

| Conflict | Sources | Resolution |
|---|---|---|
| six B17-screen cells: `i_det` exact (B17-12, SCREEN_REPORT) vs floor with `m_det` unknown (B18-12 §4a) | B17-12 §"Inherited finite stocktake"; B18-12 §4a | exact **under P-S57**, floor otherwise; §2.2 carries the premise in every row. The `D` bounds are valid only under P-S57 in nine rows and unconditionally in one. |
| "ten explicitly excluded cells" never printed as a list under that name | B18-06 §1.1 (ADOPTED identification) | the four B16 + six B17 rows of §2.2; identification now printed here, still ADOPTED |
| `s` for (12,2^4) at `d = 5`: `s = g = 8` | census; B18-06 control (e); B19 preamble | agree |
| `U` for the ten cells carried from the stable tail | B16-12 ring-map review; SCREEN_REPORT "inherited from accepted Batch16" | carried as part of the premise; not recomputed per degree in any source read |
| `a = 1` at `(20,2^4)`, `d = 7` | B18-06 (from the screen's `a < 2` plus Prop. 4.1's `a >= 1`) | ADOPTED; the screen JSON row for that shape was not printed here |
| B15-02's nine cells: `a = 1` "inherited" | B15 stocktake | recorded as inherited, not recounted |
| (12,4,4,4,4,4) `d = 8`: `r_det_lb = 4` "inherited" | B15-12 table | floor's source not located; row left SCREEN + unlocated floor |

**Values carried across a regime boundary, each with its justification named.**

1. Stable-tail `U` (158/218/288) at finite degrees 23–26: justified by the
   split-cubic source argument being a statement about the product family in every
   degree, with finite carriers recorded in `finite_screen.json`; whether the finite
   `T` was recomputed I could not confirm. Carried under P-S57.
2. Five-variable product ceiling `T` for the six-row cell (14,2^5): valid as a
   ceiling because the honest six-variable padding variety `P_6` lies inside the
   generic-product variety (B18-10 §9, B18-06 claim 9). Not exact.
3. Stable-family exclusions of B15-06 and B16-09 to every finite rung: justified
   by the inherited stable theorem (S57 Prop. S) plus ideal multiplication; recorded
   as CLOSED-P.

## 4. Gate compliance, and what this intake will do when 01/02 report

- No degree-six census was run. No Kronecker screen was run at any degree. No
  excluded cell was reopened. No cell is nominated. The small-`s` ranking of B18-06
  §1.4 appears in §2.6 as a price list only.
- One bounded computation was run (§5), on the control the brief assigned, 3.9 s.

When slot 01 or 02 names a cell, the assessment will fill one row of the §2 form
in this order and stop at the first missing entry: `a` (certified, `>= 1`); the cell
not in §2.2–2.5; `s` computed **for that cell** as the symmetric coefficient; `T`
and `U = min(a, T)` with the padding variety named (`R135` only at five rows;
`P_L` above); any proved `B` or `q` with its argument and direction; the required
rank `B + 1`; the actual-padding evidence (points written as `(z·per3) ∘ T`); and
measured costs. A cell with `s >= a` and no certified `b` has `B = a` and no
headroom, and will be recorded as such, not nominated.

## 5. The batch-18 item: B18-05's generic-quartic control, repaired

The original run-1 control drew 60 random monomials of the 715 available and, by
chance, none of the five `t^k x_1^(4-k)` monomials except `t^4`; so `p(t) = t^4`,
every chart polynomial was constant, all eleven `E` vanished, and `w·E != 0` was
never tested. Re-run here with three quartics carrying **all 715** monomials
(nonzero integer coefficients, `[t^4] = 1`), through the unchanged B18-05 evaluator
imported from `analysis/b18_05_psi.py`:

| item | value |
|---|---|
| original control reproduced | 46 nonzero monomials; `p = t^4`; all `E = 0` (degenerate, as recorded) |
| full-support seeds 190501–190503 | all five `t^k x_1^(4-k)` present; `p(t)` has nonzero `t^0, t^1, t^2`; interpolated degrees `A:18, J2:17, J3:17, Q22:18, D_H:20, T2:18`; all eleven `E` nonzero |
| `w·E` | nonzero at all three seeds (e.g. `4839473560902601997041993972171460577182755285131437126272942080`) |
| `kappa·E` | nonzero at all three seeds |
| det4 control | all `E = 0`, `w·E = 0` (unchanged) |
| run | `b19_05_control_20260915_01`, wrapper `b15_bound.py --seconds 60 --memory-mb 512`, exit 0, 3.9 s, peak Job memory 37.6 MB |
| files | `analysis/b19_05_control.py` (SHA256 `8429fbad…ab7e6`), `results/b19_05/control_full_support.json` (`d6d1c017…2ea162`), receipt `results/logs/b19_05_control_20260915_01_resources.json` (`529853da…0924`) |

**CERTIFIED:** `w` and `kappa` are not ambient linear relations among the eleven
`E`; the vanishing of `w·E` on the product family is a genuine restriction identity,
and the B18-05 rank-9 result is non-vacuous. The addendum is appended to
`docs/b18_05_report.md` (nothing above it changed; the file is tracked, so
`git status` shows it as modified, as the brief authorised).

## 6. Labelled claims, resources, next test, status

| # | Claim | Label |
|---|---|---|
| 1 | Provenance `ca3d6d80…` / `2fcc712f…`; footprint: `docs/b19_05_intake.md`, `analysis/b19_05_control.py`, `results/b19_05/`, two wrapper receipts, and the authorised addendum to `docs/b18_05_report.md` | MEASURED |
| 2 | The ten `2^8` cells are closed; nine under P-S57, `d = 27` unconditionally given `U = 288` | ADOPTED (sources named), with the premise made explicit |
| 3 | The B18-12 §4a labelling "floor, `m_det` unknown" together with its `D` column is direction-inconsistent; the B17-12 labelling is the consistent one | PROVED (elementary) |
| 4 | All 23 degree-five and 4 degree-six five-row cells are closed at cell level; 26 with `D = 0` exact, `(4^5)` with `D <= 0` | ADOPTED from B18-06 / B18-01 certificates and the B19 preamble; `a`, `s`, `T`, `U` transcribed from the census |
| 5 | Every screen in the tree retires a certificate route, none bounds `D`; the degree-7 screen touches two admissible cells | ADOPTED, with the JSON re-read here |
| 6 | Named open cells of §2.7 are open; none is nominated | MEASURED (from sources) |
| 7 | `w·E != 0` on the ambient chart; B18-05 rank-9 non-vacuous | CERTIFIED (exact values, wrapped run) |
| 8 | Any candidate, any `b >= 1`, any positive `D` | NOT REACHED (by design of this pass) |

**Honest negatives.** `s` is unknown in all ten `2^8` cells and in most §2.3 rows.
`a` is unknown for the B16-07 cells and the B15-01 cell as read here. The finite
`T` for the ten cells was not found recomputed. The B15-03 secondary cell's
partition was not extracted. None of these unknowns was filled with an estimate.

**Resources.** One wrapped `python3` run (3.9 s, 37.6 MB). Source reading only
otherwise. No lease. Git: the two `rev-parse` calls and `git status --porcelain`.

**One next sufficient test, and its price.** Not a census. When 01/02 name a cell
`(d, lambda)` with `a >= 1`, `ell = 5`: compute `s` for that cell as the symmetric
coefficient and `U = min(a, T)`; if `s >= a`, the only route is a certified `b`, and
the test is B19-06's. If a cell with `1 <= min(a, s) < U` appears, the sufficient
test is the B18-06 ladder at that cell: exact `h`-basis, one determinant
evaluation, one actual-padding evaluation, priced from the measured sweep (2–14 s,
under 100 MB for `K <= 11640`). Nothing to run until a cell exists.

**Status: COMPLETE (intake). No nomination. Waiting on slots 01 and 02.**
