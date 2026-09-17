# B19-01 review — the Silence theorem

Report: `work/batch15_workers/B15-01/docs/b19_01_report.md`, 297 lines,
sha256 `aa136106…`.

## Verdict

**ACCEPT.** A ceiling theorem with a decidable test, a counterexample to exactness, and
a cost reduction — three of the four outcomes the brief asked for, from one session.
Every number I could check, I checked, and all of them hold.

## 1. Verified independently

| Claim | My check |
|---|---|
| band empty for `ell <= 5` | **0 members at `d = 5, 6, 7, 8`** across every length up to 5 |
| at `ell = 6` the band is the single rectangle `((2d/3)^6)` | at `d = 6`: **exactly one member, `(4,4,4,4,4,4)`** |
| counterexample cell `a = 1` | **`a = 1`**, by monomial DP in six variables plus the Weyl alternant |
| `g = 13` | **13**, from `S_24` characters by Murnaghan–Nakayama |
| `s = 10` | **10**, same lineage |
| `b = 0` there | follows: `lambda_1+lambda_2+lambda_3 = 12 = 2d`, so the band condition holds with equality |

Controls on my own implementations: `g(mu,mu,(24)) = 1`; `f^(6^4) = f^(4^6) =
140,229,804` by transpose symmetry; and `sum_lambda a · dim S_lambda(C^6) =
C(131,6) = 6,249,655,776` exactly.

**The arithmetic behind the band scope is clean enough to state without computing.**
For `lambda ⊢ 4d` with `ell` rows, the top three parts sum to at least `(3/ell)·4d`. At
`ell = 5` that is `2.4d > 2d`, so the band is empty — which is exactly why twenty
controls never met it. At `ell = 6` it is `2d`, with equality only when all six parts
are equal. Hence the single rectangle. The theorem's reach is forced by a counting
argument, not by anything about the implementation.

**On the caught bug.** The first version dropped the `chi_R(eta^2)` term of (3.1) —
which is precisely the term separating the symmetric `s` from the ordinary `g`. My
independent `s = 10`, computed as `(chi^2 + chi(g^2))/2`, confirms the corrected code.
The disclosure is exact and the correction is right.

## 2. One precision point

The report says the band is "non-empty for lengths six to ten". At `ell = 7` through
`10` I find that unconditionally true. **At `ell = 6` it holds only when `3 | d`**,
because `(2d/3)` must be an integer: at `d = 6` there is one member, and at
`d = 5, 7, 8` there are **none**.

This does not touch the counterexample — `d = 6` satisfies `3 | d`, which is why the
chain "band needs `ell >= 6`, `a > 0` needs `ell <= d`, so the first testable cell is
`d = 6`" lands where it does. But the sentence as written could propagate as "there is
always a length-six band cell", and there is not.

## 3. What the theorem does and does not close

**It closes:** any six-to-ten-row cell whose top three parts sum to at most `2d`. In
such a cell `b = 0`, so `B = min(a, s)` and a gap certificate — which needs
`b >= max(0, s - U + 1)`, here 10 — is impossible. The statement is about
`S_lambda W`, so no better carrier implementation defeats it. That is a genuine
method ceiling, not a limitation of one instrument.

**It does not close five rows**, and the report says so in its own words: *"everything
at length five"* still lacks a proof. The band is empty there, so the Silence theorem is
silent about exactly the cells the search wants. Combined with batch 18 — all
degree-five five-row cells closed, first possible five-row separator at degree six or
more — the live question is **five rows at degree `>= 6`**, and this theorem says
nothing about it either way.

The board should not read "the arc is blind" as general. It is blind in a precisely
identified region that does not include the target.

**The counterexample is strong on its own terms.** At `(4^6)`, `d = 6`: `ker C` has
dimension `s = 10` while `m_det <= a = 1`. Nine dimensions the arc admits that cannot
extend. Any exactness conjecture for this instrument is refuted, and it took no carrier
run to refute it.

## 4. The operational payoff, and what I would do with it

**Free pre-filter.** Before budgeting carrier time on any six-to-ten-row cell, add three
parts of `lambda` and compare with `2d`. If the sum is at most `2d`, the instrument is
provably blind. That costs nothing and it should be in the board's decision rule.

**Levi reduction.** `b <= dim((S_lambda W)_{<0})^L` for the grading-preserving subgroup
`L`, a finite branching number — about 10,505 triples at `d = 7`, minutes against the
hours-to-days of a carrier run. I have **not** independently verified that count or the
commutation argument; both are marked as the slot's, pending slot 10.

**A recommendation for slot 03.** Its gate is "hold until 01 or 02 supplies a question
that needs this computation." B19-01 supplies a method but not yet a target cell, so the
gate is only half met. There is a bounded, valuable task that needs no nomination:
**implement the Levi reduction and validate it against B18-02's twenty certified
controls, where `b` is already known to be `s - a`.** A new cheap method whose first
outputs reproduce twenty known values is worth far more than the same method applied
first to an unknown cell. If it disagrees anywhere, that is a finding too.

## 5. What enters the index

| id | statement | status |
|---|---|---|
| `silence_theorem` | If `lambda_1 + lambda_2 + lambda_3 <= 2d` then the forbidden subspace of `S_lambda W` is empty, so `b = 0` and `B = min(a, s)`. The statement is about `S_lambda W`, so no carrier implementation can defeat it | PROVED (slot); scope recomputed here |
| `band_scope` | The band is empty for `ell <= 5` at every `d`, because the top three of `ell` parts sum to at least `(3/ell)·4d` and `2.4d > 2d`. At `ell = 6` it is the single rectangle `((2d/3)^6)`, **and only when `3 | d`**. Non-empty for `ell = 7..10` | PROVED; recomputed here at `d = 5,6,7,8` |
| `arc_is_not_exact` | At `d = 6`, `lambda = (4^6)`: `a = 1`, `g = 13`, `s = 10`, `b = 0`. `ker C` has dimension 10 while `m_det <= 1` — nine dimensions the arc admits that cannot extend. No gap certificate is possible in a band cell, since that needs `b >= s - U + 1 = 10` | PROVED; all four values recomputed here |
| `three_part_prefilter` | Before budgeting carrier time on a six-to-ten-row cell, compare `lambda_1+lambda_2+lambda_3` with `2d`. At most `2d` means provably blind. Costs nothing | PROVED corollary |
| `levi_reduction` | The skew-degree projection commutes with the grading-preserving subgroup `L`, so `b <= dim((S_lambda W)_{<0})^L`, a finite branching number — about 10,505 triples at `d = 7`, minutes rather than days | PROVED (slot); **count and commutation not verified here** |
| `five_rows_still_open` | The band is empty at five rows, so the Silence theorem says nothing there. Whether `b > s - a` is possible in five-row cells — the cells the search wants — remains open, and no cell with `m_det < a` has been analysed | RECORDED, open |

## 6. Carry-forward

1. Add `3 | d` to the `ell = 6` band statement before it is quoted anywhere.
2. Add the three-part pre-filter to the board's common decision rule.
3. Slot 03: scope to validating the Levi reduction against the twenty known controls.
   That needs no nominated cell and is the right first use of a new cheap method.
4. Slot 10 should verify the Levi commutation argument and the 10,505 count; I did not.
