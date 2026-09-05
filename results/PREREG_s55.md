# PRE-REGISTRATION — session 55, the equation census below degree 24

Committed **before** any computation of this session. Branch `s55-census`,
off `main` at `eb8cecb37b0ee30d5be76ccbd816ee142618882c` (sync baseline,
rule 10; the ancestor test is trivially satisfied since the branch is cut from
that commit).

Nothing below has been measured at the time of this commit. The literature
reading recorded in §0 was done first and is stated as prior information, not as
a result of this session; every *number* it contains is re-derived in §2 before
it is used anywhere.

## 0. Prior information carried into the session

From the repository record (not re-established here):

- `D_r^{det_4} = closure{ det_4(s_1A_1 + ... + s_rA_r) } ⊆ Sym^4 C^r`;
  `dim D_5 = 50` in `dim Sym^4 C^5 = 70`, codim 20 (`docs/n4_gate.md`).
- `I(D_4^{det})` is principal of degree `320112` (`docs/e4_hunt.md`).
- onset window for `I(D_5^{det})`: `[8, 405]` (`docs/det_onset.md`).
- Macaulay-minor cap at `r = 6`: 661 certified, 1148 proved (s48/s49).
- The house pre-checks are `docs/brief_wording.md` **§5** (degeneracy direction)
  and **§7** (functoriality). The s55 brief cites "§6" for the first; §6 of the
  committed file is the citation-corrections section. This is recorded as a
  brief error, not silently reinterpreted.

From the literature, read before this commit:

- Landsberg–Manivel–Ressayre, *Hypersurfaces with degenerate duals and the
  Geometric Complexity Theory Program*, arXiv:1004.4802, Comment. Math. Helv.
  88 (2013) 469–484. Theorem 2.3.1: `Dual_{k,d,N}` has equations spanning the
  `SL_N`-module of highest weight
  `Omega(k,d) = (d-1)(d-2)(k+2) w_1 + (d(k+2)-2k-5) w_2 + 2 w_{k+3}`,
  of degree `(k+2)(d-1)`.
- Alper–Bogart–Velasco, arXiv:1505.02205, FoCM 17 (2017), Thm 1.2:
  `dc(f) >= codim Sing(f) + 1` when `deg f > 2` and `codim Sing(f) > 4`.
- Hüttenhain–Lairez, arXiv:1512.02437, C. R. Acad. Sci. Paris 354 (2016):
  the boundary of `GL_9 . det_3` has exactly two irreducible components.
- Farnsworth, arXiv:1505.05079: symmetric border rank `R_S(det_4) >= 38`,
  improving a previous bound of 36.
- Bürgisser–Ikenmeyer–Panova, arXiv:1604.06431, JAMS 32 (2019), Thm 1.5:
  no occurrence obstructions **for `n >= m^25`**.

## 1. What this session will and will not do

It will produce one row per construction in `docs/equation_census.md`, with the
columns the brief asks for, and it will re-derive every degree it quotes.

It will **not** attempt to construct a new equation. A construction below 24 is
an outcome the session can only *report* if it falls out of a re-derivation; it
is not something the session is set up to search for.

## 2. The measurements, fixed now

All exact: integer or `Z/p` arithmetic through `python-flint`, no floating
point. Two primes (`p = 2147483647`, `p = 1000003`) plus a rational
re-computation on the small cells. Every run bounded by `timeout` and
`ulimit -v`, pid to `results/logs/`.

### M1 — the LMR weight arithmetic (row 1, row 2)

Compute, symbolically in `(k,d)`, the partition `lambda(k,d)` from
`Omega(k,d)` and its size, and check `|lambda| = delta * d`.

- **Positive result** (i.e. the reading is confirmed): `|lambda(k,d)|`
  identically equals `(k+2) d (d-1)`, so `delta = (k+2)(d-1)`, and the two
  instances come out as `lambda(4,3) = (19,7,2^5)`, `delta = 12` and
  `lambda(6,4) = (65,17,2^7)`, `delta = 24`.
- **Falsifier**: any other value of `|lambda|/d`. In particular a value of 12 at
  `n = 4` would confirm the printed Theorem 1.0.2 rather than Theorem 2.3.1 and
  would change the whole table.
- Also recorded: `ell(lambda) = k+3`, and hence the smallest `r` for which the
  module is nonzero.

**Prediction (prior 0.9):** `delta = 24` at `n = 4`; the "n(n-1) = 12" reading in
LMR's printed Theorem 1.0.2 is a typo, contradicted by its own highest weight.

### M2 — Hessian rank on the hypersurface (rows 1, 2; the degeneracy direction)

In `r = 10` variables, at exact rational points, compute
`rank Hess(P)(x)` for `x` a point of `{P = 0}`, and hence
`dim X^* = rank - 2` at a generic smooth point of each irreducible component:

| point | what it is |
|---|---|
| `A` | `P = det_4(sum s_a A_a)`, `A_a` random integer `4x4`, `a = 1..10` |
| `B` | `P` a random integer quartic in 10 variables |
| `C` | `P = l . c`, `l` a random linear form, `c` a random cubic |
| `D` | `P = x_0 . per_3(x_1..x_9)` — the full ten-variable padded permanent |

- **Predictions, logged now:** `A`: rank 8 (`dim X^* = 6`). `B`: rank 10
  (`dim X^* = 8`). `C`: rank 2 on the component `{l = 0}` and rank 10 on
  `{c = 0}`, so `dim X^* = 8`. `D`: rank 2 on `{x_0 = 0}` and rank 10 on
  `{per_3 = 0}`, so `dim X^* = 8`. Prior on the pair (`A` = 8, `D` >= 9): 0.85.
- **What counts as the degeneracy-direction check passing** for the dual-defect
  family: `dim X^*(D) > dim X^*(A)` and `dim X^*(C) > dim X^*(A)`, i.e. the
  padded permanent is *less* degenerate than the determinant. Anything else and
  the row is reported as failing, however good its degree.
- **What settles "is 24 the family floor at `n = 4`"**: the minimal `k` with
  `D_r subset Dual_{k,4,r}` equals `dim X^*(A)`; the family degree is
  `3(k+2)`, monotone increasing in `k`. So `dim X^*(A) = 6` exactly (not less)
  is the whole content, and it is one rank computation.

### M3 — the flattening family (row 4)

`Cat_{2,2}(P) : S^2 (C^{10})^* -> S^2 C^{10}`, a `55 x 55` matrix linear in the
coefficients of `P`; rank at the four points `A`–`D` above, and at `r = 5, 6`.
Also `Cat_{1,3}`.

- **Predictions, logged now:** `rank Cat_{2,2}` = 55 at `B`, 36 at `A`,
  20 at `C`, 18 at `D`. Prior 0.7 on the exact quadruple, 0.9 on the ordering
  `D <= C < A < B`.
- **A positive result for the programme** would be `rank(A) < rank(D)`: then
  minors of size `rank(A)+1` vanish on `D_r` and not at the padded permanent,
  and the family separates at degree `rank(A)+1`.
- **The predicted outcome is the opposite**, and it is a *failure* of the
  degeneracy-direction check: `D` more degenerate than `A` means every
  flattening minor that vanishes on `D_r` also vanishes at the padded permanent.
- Either way the smallest minor size that vanishes on `D_r` is
  `rank(A) + 1`, and that number is the row's degree.

### M4 — the singular-locus / discriminant row

Not previously in the brief's list; added because Alper–Bogart–Velasco's
geometric input is exactly this and it is the only *classical* equation for
`D_r` we can name.

- Re-derive `deg disc(Sym^4 C^r) = r . 3^{r-1}` (GKZ `N(d-1)^{N-1}`), so 405 at
  `r = 5`, and check that `disc` really does vanish on `D_5` by exhibiting the
  singular points of a random determinantal quartic threefold in `P^4`
  (expected: 20 nodes, the degree of the rank-`<=2` locus in `M_4`).
- **Prediction:** exactly 20 singular points, all nodes, for a random pencil.
  Prior 0.85 on 20.
- Degeneracy-direction check: predicted to **fail** trivially, since `l . per_3`
  is reducible and every reducible hypersurface is singular.

### M5 — Plücker route, row 6

No new computation. The deliverable is an estimate of the degree of eliminating
the pencil, with the estimate's basis stated, plus the correction that the
committed `docs/s53_prompt.md` no longer contains the common-isotropic-4-plane
route at all — it was replaced by the Rees-algebra/blow-up formulation, and the
isotropic statement was recorded in `docs/critic_e7_response.md` §5 as a
corollary of Alper–Bogart–Velasco. The brief's row 6 therefore rests on a
superseded draft, and the row will say so.

## 3. Standing predictions about the session's own conclusion

Logged before the census is written:

1. **No construction below degree 24 will be found** at `n = 4`. Prior 0.85.
2. **24 will be shown to be the exact floor of the LMR family** at `n = 4`, by
   the `dim X^*(det) = 6` computation plus monotonicity of `3(k+2)` in `k`.
   Prior 0.8.
3. **The "Landsberg–Ressayre Cayley–Bacharach" row will not survive** as
   described: there is no such paper, and the nearest real object
   (Alper–Bogart–Velasco) gives a numerical bound, not equations. Prior 0.75.
4. **The flattening row will fail the degeneracy-direction check** rather than
   failing on degree. Prior 0.7.
5. **A finding not in the brief:** LMR's module is identically zero for `r <= 8`,
   so its degree 24 and the programme's measured range `delta <= 9` are not
   merely far apart — they are in different cells, and no experiment compares
   them directly. Prior 0.6 that this survives scrutiny.

A refutation of any of these is a result and will be recorded as one.
