# B18-05 review — the eleven-equation restriction rank

Report: `work/batch15_workers/B15-05/docs/b18_05_report.md`. Started from `39a9154b`,
tree `d66688de`. Code `analysis/b18_05_psi.py`, `analysis/b18_05_proof.py`.

## Verdict

**ACCEPT, conditional as the slot labels it.** The rank is 9. The structure lemma I
did not merely reproduce — I re-derived it, and it is correct. One thing needs
repairing, and it is cheaper than the sentence describing it.

## 1. The structure lemma, proved here independently

For `F = z·C(y)` with `C` a cubic on the complementary nine-space, the Hessian is, in
block form `(1 + 9)`:

```
Hess F = [[ 0      , (grad C)^T ],
          [ grad C ,  z·Hess C  ]]
```

- **At `z = 0`** this is `e_0 g^T + g e_0^T` with `g = (0, grad C)`, which has **rank 2**
  whenever `grad C != 0`. The slot's "rank two at the root of the linear factor" is
  immediate from the block form.
- **At `C = 0`, `z != 0`**, Euler's identity for a cubic gives `g^T y = 3C = 0` and
  `(Hess C) y = 2 grad C`. So a vector `(alpha, y)` is annihilated exactly when
  `alpha·g + 2z·g = 0`, i.e. `alpha = -2z`. And `(-2z, y) = -(3z·e_0 - x)` where
  `x = (z, y)`. **That is precisely the slot's kernel vector `3z·zeta - nu·x`.**

Numerically confirmed at six random instances of each case: rank 2 every time at
`z = 0`; corank exactly 1 every time at `C = 0`, with `Hess F · (3z·zeta - x) = 0`
exactly. The lemma is not merely certified at sample points — it follows from Euler,
and the slot's kernel vector is the right one.

From the certificate: the two kernel vectors are independent (I checked the rank of
the pair is 2), so `11 - 2 = 9` matches the recorded `model_rank`, and `Gamma` has four
coefficients — one linear root and three cubic roots, as the lemma requires.

## 2. Direction of inference — exemplary

The report says, of its own fourteen zeros:

> "a sampled zero is a ceiling, never membership: **these fourteen zeros prove nothing
> about the global rank.**"

and keeps `9 <= rank <= 10` open until the proof closes it. The Schwartz–Zippel figure
(`~2·10^-14`) is used to say route 2 is closed *in practice*, explicitly not as proof.
The rank-9 floor comes from B17-04's accepted nonzero minor — a floor from a nonzero,
the one direction that is valid — and the ceiling from two explicit kernel vectors.
Floor and ceiling meet at 9. Both used correctly.

## 3. The one thing to repair

The generic-quartic control came back `w_E_nonzero = false`. The slot diagnoses it
correctly: the sparse random quartic had no `t^k x_1^(4-k)` monomials, so `p = t^4`,
every `E` vanished, and the control measured nothing. It calls it "a bad control, not
evidence about `w`" and leaves it, on the grounds that ambient independence of `E` is
inherited from B17-04.

I would not leave it, and here is why it matters more than the report allows.

**That control is the only in-batch check of the premise that makes the result
informative.** If `E` were *not* an independent ambient basis, then `w·E` could be
identically zero on the whole ambient, the rank would be 9 everywhere, and "the
restriction rank on actual padding is 9" would be a true but vacuous statement — no
drop from 11, nothing about padding. The entire structural reading ("both
padding-satisfied equations are consequences of product structure alone") rests on
`w·E` being nonzero somewhere off the product family.

The report is right that the premise is inherited and accepted. But a sub-second
re-run with a genuinely generic quartic converts an inherited premise into a checked
one, in the one place where its failure would empty the result. The slot already did an
unwrapped diagnostic of the degeneracy; doing the repaired control costs the same.

**Requested before this enters the index:** one repaired generic-quartic control
showing `w·E != 0` at a quartic with full monomial support.

## 4. The structural content, which is the real result

The eight zeros on the wider family `z · (arbitrary nine-variable cubic)` are the
informative ones. `Psi` is **not** a permanent-specific identity — it is a property of
the whole product family. So both padding-satisfied relations in this space come from
product structure, not from the permanent.

The consequence the slot draws for Slot 06 is valid and does **not** depend on the
contested premise: evaluate a candidate determinant equation at product points; a
nonzero value certifies it is not of product type. That is a sampled nonzero used in
the only direction it permits, and it is a necessary condition for any separator, since
padding *is* a product.

## 5. What enters the index

| id | statement | status |
|---|---|---|
| `product_hessian_structure` | For `F = z·C(y)` with `C` a cubic on the complementary nine-space, `Hess F` has rank 2 at the root of the linear factor and corank exactly 1 at each root of the cubic, with kernel `3z·zeta - x`. Both halves follow from the block form and Euler's identity for `C` | PROVED; re-derived independently here |
| `eleven_equation_rank_is_nine` | The eleven-equation restriction rank on actual padding is exactly 9, kernel exactly `span(kappa, w)` — **conditional on the inherited degree-27 polynomial lifts and B17-04's `GL16`-to-`10x10` restriction argument**, neither re-proved | PROVED conditional |
| `psi_is_product_not_permanent` | `Psi = w·E` vanishes on the whole family `z · (any nine-variable cubic)`, not only on actual padding. The two padding-satisfied relations are consequences of product structure, not of the permanent | MEASURED at 6 padding and 8 wider-family points; **held pending the repaired generic-quartic control** |
| `product_type_filter` | A candidate determinant equation that is nonzero at a product point is certified not of product type. Since padding is a product, this is a necessary condition for any separator, and it costs one evaluation | PROVED |

## 6. Carry-forward

1. Repair the generic-quartic control. Sub-second, and it is the only cheap check of
   the premise that keeps the result from being vacuous.
2. `eleven_equation_rank_is_nine` never travels without its two inherited conditions.
3. The second `git status --porcelain` disclosure in this batch. Both slots did the
   right thing; the fault is that my preamble and my permission list disagree. Fixing
   the preamble is on me.
