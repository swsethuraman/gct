# Pre-registration — B24-04 pilot 3 (`b24_04_p3_close`)

Written and hashed after pilots 1 and 2 were read and before pilot 3 was written or run. The pilot
prints this file's sha256 and pilots 1 and 2's output sha256 in its own output. This is the
**third and last** pilot of the slot's budget.

## Part A — the one class pilot 2 left open

Pilot 2 decided ten of its eleven classes: PROVED trivial. One stalled:

> block `11:1,4,4,0` (dimension 7), `s_rep <= 0`: 2737 drawn, 126 accepted, **rank 6 of 7**.

`s_rep = 0` in this block is rigid. The block has `#a = 1, #r = 4, #c = 4, #S = 0`, with column 0
carrying three non-`K` slots and columns 1-3 two each. A column with no repeated type cannot be
`(r, r)` or `(c, c)`; and a three-slot column drawn from `{r, c}` alone must repeat. Hence
`s_rep = 0` forces **`cols[0]` to be a permutation of `(a, r, c)` and each of `cols[1..3]` a
permutation of `(r, c)`** — 48 column assignments in all, with the ten triples still free.

Part A samples that family **directly** (no rejection), under a fourth seed `20260921`, and tracks
the rank in batches of 50. Stops at: rank 7; 2500 accepted; 600 consecutive accepted with no rise;
or its share of the deadline.

- **rank reaches 7** -> `s_rep` is **trivial** here too, and then **every** statistic tried in this
  slot other than `s_a` is trivial in every class examined. PROVED (a modular rank is a floor, G27).
- **rank stalls at 6** with a sample an order of magnitude larger than pilot 2's -> reported as
  **MEASURED candidate only**: a codimension-1 subspace of one 7-dimensional block. It is recorded
  that even if real this is **not** a grading of `F^L_{-1}` — `s_rep` would be non-trivial at one
  threshold in one block of four and trivial in the other three, so its graded count has no
  Kostka-Foulkes shape.

## Part B — control on the Question 1 theorem, and its price

§2 of the report proves: for `lambda = (nd - t, lambdabar)` with `|lambdabar| = t < d`, every
monomial of the `lambda`-weight space of `Sym^d(Sym^n C^r)` is divisible by `c_{n e_1}^{d-t}`, so
every such weight vector factors as `c_{n e_1}^{d-t} * g` with `deg g = t`; and hence a separating
equation in that cell forces one of degree `t`. Part B is the arithmetic control on the counting
half of that proof. It computes

> `N_S(lambda, d)` = the number of multisets of at most `d` nonzero vectors `alphabar` in
> `Z_{>=0}^{r-1}` with `|alphabar| <= n`, summing to `lambdabar`

by dynamic programming, and checks:

- **C1 calibration against B23-06** (independently produced, `feed104e`, §2.3 table):
  `lambdabar = (2,2,2,2)`, `d = 5`, `r = 5`, at `n = 4, 5, 6` must give `N_S = 553, 621, 641`.
- **C2 the factorisation, by literal enumeration** (not by the DP) for small cells with `t < d`:
  `(n,r,d,lambdabar) = (3,3,5,(1,1))` and `(3,4,6,(1,1,1))`. Every weight-`lambda` monomial must
  contain `n e_1` at least `d - t` times, and the count must equal the count at degree `t` for
  `mu = lambda - (d-t) n e_1`. A single counterexample refutes the theorem and will be reported.
- **C3 the price.** The stable value (`d >= t`) of `N_S` for every four-part `lambdabar |- t`,
  `n = r = 5`, `t = 4..16`, and for two shapes at `t = 18, 20, 22, 24`: the most concentrated
  `(t-3,1,1,1)` and the flattest. The minimum is reported as a **minimum over the shapes
  evaluated**, never as a proved global minimum.

## Scope

Nothing here is claimed about Kronecker coefficients, about any other weight space, or about
plethysm in general. Producer-only (G18). One wrapped pilot, 60 s / 512 MiB, deadline-guarded at
55 s, JSON written after each part.
