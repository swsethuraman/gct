# B25-04 scope erratum, 2026-09-22

Written by the housekeeping pass PART 17d (Claude Code, Claude Opus 5 (1M context)), as ordered by
A25-10 `RELEASE_DECISIONS.md` (sha256 `e7de25427c09249f8b4bc6b676d3d8740cee90f0ebfb6f4fcdceb394e69c2599`),
row B25-04. That row asks for a theory-only scope erratum, capped at 20 minutes with zero pilots. The
acceptance test is **exact agreement with the scoped statements of A25-10 `REVIEW.md` §6** (at
`ab4f527189bea14b5d146f9dc9d5b445844eaff3`). **Zero pilots; no computation.** The sealed report
`docs/b25_04_report.md` and `results/b25_04/MANIFEST.json` (`a33ab4dd…`), both at
`92a7d054369a20854fd51685ee09ecb756344e8d`, are **unchanged**. This erratum corrects them by
reference. It adds no mathematics: every corrected statement below is REVIEW §6's.

## What stands, unchanged

Lemma A (component factorisation) and the symbolic component theorem are **PROVED**, as A25-10 §6
records. Primality of `I(D_r^{det_n})` has the elementary proof given there: `D` is irreducible
because its parameter space is affine irreducible. The tail bound `t ≥ D*` stands, and it is all the
component theorem uses. The numeric floor keeps its regime and premises. The all-components-≤-7
corollary holds **only modulo the record's `D* ≥ 8` floor in the same quinary regime**: B23-06 §2.2
uses the block-diagonal restriction to `D35`, and B22-02 Lemma 1.6 marks `onset I(D35) ≥ 8` as
ADOPTED record-internal. The symbolic `D*` theorem needs no numeric floor.

## Corrections (REVIEW §6, "Finite textual/scientific repairs", items 1–3)

| # | where in B25-04 | as printed | corrected scope |
|---|---|---|---|
| 1a | title (report L1); §4.2 heading; §7 "disconnected fillings" | "disconnected fillings never separate"; "no-go for disconnected fillings" | The no-go is for **single tableau functions whose tableau graph has every component with fewer than `D*` vertices**. A disconnected filling may have a large separating component, and Theorem B does not exclude it. Corrected title: *"Large tail with small treewidth: a single tableau function none of whose components has `D*` vertices never separates"*. |
| 1b | §4.3 first bullet "Nonzero members of every tail"; `THEORY_GATE.md` L28 "nonzero members of every tail" | "every tail" | **Unbounded tails.** The exhibited tails `2j + 4j′` are even. No nonzero member is shown for every tail. |
| 2 | §2.1, the copied final sentence of B24-04's Corollary | "every separating equation is `c_{ne_1}^k` times one whose cell has tail exactly equal to its degree" | Restricted to **`t ≤ d`**. For `t < d`, Theorem 1 supplies the factorisation `f = c_{ne_1}^{d−t} g` with `g` of degree `t`. At `t = d`, tail already equals degree. **For `t > d` the valid conclusion is `t ≥ d ≥ D*`, with no such degree reduction.** Keep `t ≥ D*`. This corrects a quoted overstatement; it does not reject the accepted tail bound. |
| 3a | §4.4 item 2 "B24-04's cycle example is connected"; §7 and `THEORY_GATE.md` L40 "(paths, cycles, trees of cliques)" | a cycle, i.e. a simple 2-regular graph of treewidth 2 | When each label occurs twice, duplicate columns can create parallel edges, which collapse to `K2` in the simple graph. In that example **treewidth is `≤ 2`**: not invariably 2, and not invariably a simple 2-regular graph. |
| 3b | §2.1, B24-04 Lemma 2 `τ(G_T̂) ≤ λ_2 + t − 1` | the bound as an all-shape bound | At `t = 0` the graph is edgeless and `τ = 0`. For a bound valid at every shape, use **`max(0, t + λ_2 − 1)`**. |

These edge cases do not affect the component factorisation (REVIEW §6).

## Not changed by this erratum

- The pilots' disclosures stand as printed: pilot 1's component-product test was vacuous (0 = 0);
  pilot 2 gives nonzero controls from the same evaluator lineage. Both `.pid` receipts are committed
  and bound. No receipt is rewritten.
- The span distinction and the open corner (§4.4 items 1–2, §7 (a)–(b)) stand. Primality controls
  products, not sums.
- The two-row nonvacuity examples (REVIEW §6: `g(p) = 8`, `h(p) = 32` at
  `p = (x1+x2)^5 + (x1−x2)^5`) are the review's own check. No five-row nonvacuity or padding value
  follows from them.
