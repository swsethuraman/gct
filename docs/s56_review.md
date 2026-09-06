# Integrator review — session 56, the Foulkes engine

**Accepted.**  The engine was built, it calibrates 40/40, and — the finding that
matters more than the calibration — **it cannot reach any cell the programme
cares about, and the session measured the wall rather than guessing at it.**

## 1. Reproduced here

| claim | reproduced |
|---|---|
| `\|H_{4,δ}\| = 35, 5 775, 2 627 625` at `δ = 2, 3, 4` | **exact** |
| `\|H_{4,5}\| = 2 546 168 625` | **exact** |
| `(8,4,2,2)_4`: `a = 1`, `sk = 11` | **exact** (own plethysm and own character sum) |
| `(6,4,4,2)_4`: `a = 1`, `sk = 10` | **exact** |

## 2. What the calibration is and is not

It is **not** tautological.  `Θ⁺` could have had a kernel at some cell and does
not: `mult_det = a` at all 40, so `Θ⁺` is injective through `δ = 4`.  That is
`i_det = 0` re-proved in a category with no determinant, no highest-weight
vectors, no pencils and no evaluation points — four independent things the other
engine relies on and this one does not touch.

The two sharp cells are the best part.  At `(8,4,2,2)_4` the target has room for
eleven copies and the rank is 1; at `(6,4,4,2)_4`, room for ten and the rank is
1.  **The source dimension `a` binds, not the Kronecker room `sk`** — one more
independent refutation of `sk/a` as a mechanism, from the one engine that sees
both dimensions and the rank at once.

It is **not** a test of the onset, and the session says so in its own words: it
cannot exhibit a disagreement about a nonzero ideal because the programme has no
banked cell with `mult_det < a`.  It would have *detected* an equation at
`δ ≤ 4`; there is none there.

## 3. The wall, and why it is the session's real output

`|H_{4,5}| = 2.5 × 10⁹`, the engine is quadratic in that module, and the
measured consequence is ~24 h for the cheapest length-5 cell with 192 weight
passes needed per cell.  So:

- the six-row cells (`δ = 6…10`) — **out of reach**;
- length-5 at `δ ≥ 5` — **out of reach**;
- and a fortiori the LMR cell at `δ = 24`, and the `n = 3` LMR positive control
  at `δ = 12`.

**This does not open the gate; it characterises it.**  The stock-take's item 1
("build `Θ⁺` and validate it against a known rank drop") is now answered in two
halves: the construction is right and validated, and *this* construction can
never see a rank drop, because every cell where one could live is beyond it.

## 4. The continuation, stated more precisely than the report does

The report's rule is right — the continuation must avoid materialising
`H_{4,δ}` — and it names two candidates (a Kostka/RSK contraction of `b^μ`, or a
direct decomposition of `Sym^δ(Sym^4)` against `Sym^2[δ^4]`).  There is a third
framing, and I think it is the one to brief:

> Session 58 showed that the **target dimension** `sk(λ, 4×δ)` has a reduction
> whose cost is driven by the tail `|λ̄|` and in which `N` does not appear at
> all — the LMR cell in 0.2 s against `p(96) = 1.2 × 10⁸`.  The open question is
> whether the **rank** admits the same reduction.

That is a well-posed question with a worked precedent in the same programme, and
it is the difference between a session that might succeed and a session that
restates the wall.  s58's §1 (Jacobi–Trudi along `λ`'s own first row, then
Frobenius reciprocity on the rectangle) is where it would start; the object to
push through it is the Gram kernel `K(π,π')` and its Hadamard square, not the
module `H_{4,δ}`.

## 5. Corrections it flags

The `tools/verify/verify.py` bug is real and worth fixing rather than
working around: a `matrix` certificate whose `nonvanishing_minor` determinant
exceeds ~4 300 digits fails the `content` line on Python's integer-to-string
limit **after** the rank checks have passed.  It is a display limit masquerading
as a verification failure, and the fix is one call to
`sys.set_int_max_str_digits`.  Left for the next housekeeping pass, since
`tools/verify` is shared.

Its second item is not a correction but a cross-engine confirmation, and a good
one: this session's independently computed `sk` equals `occurrence_screen.md`'s
`m_det` column at all 23 `δ = 5` rows and the `(16,2⁴)_6` anchor.

## 6. Hygiene

Pre-registration `5d63e7c` before any computation, three commits, no
single-writer file touched, no blob over the limit, no session link, and the
mid-session reminder requesting one was declined as the standing constraint
directs.  Eight certificates, full suite 58/58.  Seven of seven predictions,
twelve of twelve structural checks, no cell disagreed.  Accepted and merged.
