# The retroactive ambient audit: how much of the corpus was ever informative?

Session 25, branch `s25-race`, 2026-08-31.  Clone tip `3dfd524`.
Pre-registration: `results/PREREG_s25.md` (committed before any computation).

**Headline.**  Session 24's 742 zeros are **97.0% structurally forced** — but
only **25.2%** by the mechanism the critique identified (`a = 0`).  The other
71.8% are forced by two mechanisms the critique did not name: **hypersurface
blindness** (24.5%) and **saturation at the ceiling**, `mult_A = mult_B = a`
(47.3%).  Twenty-two cells (3.0%) survive as genuine interior coincidences, and
every one of them has `mult_A = mult_B = a - 1` exactly.  The saturation-law
hypothesis should be retired — but on the honest ground that 80.9% of the
zeros are cancellations between two *hypersurface* closures, whose
multiplicity functions are determined by the ambient plethysm and the degree
and weight of one equation, with no boundary geometry in them at all.

---

## 1. Method, and two bugs of my own

`a(lam,delta)` = multiplicity of `S_lam` in `Sym^delta(Sym^d C^N)`.  Every
routine here was written fresh: Murnaghan–Nakayama by **rim-hook removal on
the diagram** (not the beta-number formulation `scripts/ambient_screen.py`
uses), validated by full column orthogonality `sum_lam chi^lam(rho)
chi^lam(sig) = z_rho [rho = sig]` for `S_1..S_8`, and only then compared with
the screen — 0 disagreements over every `(lam, rho)` through `S_8`.

Two errors of mine were caught by the calibration battery before any result
was formed, and are recorded because the discipline requires it:

* the ambient lookup stripped trailing zeros when *storing* `lam` but not when
  *querying* it, so `a((4delta, 0), delta)` returned 0 instead of 1.  This
  inflated the World A `a = 0` count from 27 to 40 and produced an apparent
  disagreement with the brief.  There was no disagreement.
* a Gaussian-binomial helper counted compositions rather than partitions.

After the fixes, every calibration in the brief's §4 reproduces exactly,
including `World A, delta <= 14: a = 0 in 27 of 221; a >= 2 in 134`, and the
World A ambient agrees between the plethysm route and the Gaussian-binomial
route at all 221 weights.  The seven World A closure tables were rederived from
scratch and agree with the committed session-24 tables in all 1568 cells.

## 2. Session 24's cell set, reproduced

Ordered pairs `(A,B)` of the seven `Sym^4 C^2` orbit closures with `B` not
contained in `A`, all weights `delta <= 14`: **6944 cells**.  Favourable cells
(`P <= 0` and `Def < 0`, the deficit pushing towards an obstruction):
**1292**.  Of those, `D = 0`: **742**.  The full distribution of `D` —
`{0: 742, -1: 311, -2: 140, -3: 71, -4: 19, -5: 8, -6: 1}` — reproduces
session 24 exactly.

## 3. The classification of the 742

Three mechanisms force `D = 0` without any statement about boundaries:

1. **`a = 0`.**  Both closure counts are 0 by ambient arithmetic.
2. **Hypersurface blindness** (session 24, Prop. 4).  Two orbit closures that
   are hypersurfaces of the same degree and `GL`-weight have *identical*
   multiplicity functions, since
   `0 -> C[W]_{delta-e} (x) det^w -> C[W]_delta -> C[X]_delta -> 0`
   is exact and the outer terms do not see which `F` was used.  In World A that
   is exactly the pair `{Ac, D}`, both degree 6 and weight `det^12`.
3. **Saturation at the ceiling**, `mult_A = mult_B = a`.  Both closures carry
   the whole ambient isotypic piece — neither has any degree-`delta` equation
   in it — so `D = 0` is forced from *above* by the same cap.

| bucket | cells | share |
|---|---|---|
| forced — `a = 0` | 187 | 25.2% |
| blind — the `{Ac,D}` pair | 182 | 24.5% |
| ceiling — `mult_A = mult_B = a` | 351 | 47.3% |
| empty — `a >= 1` but both counts 0 | **0** | 0.0% |
| **interior — `0 < mult_A = mult_B < a`** | **22** | **3.0%** |
| **forced by some structural mechanism** | **720** | **97.0%** |

The `empty` bucket is exactly zero: in World A there is no favourable cell
where the ambient had room and both closures declined to use it.

## 4. The sharper cut: hypersurfaces

Four of the seven closures (`Iz`, `Jz`, `Ac`, `D`) are hypersurfaces, and for
those `mult(lam) = a(lam,delta) - a(lam - w.1, delta - e)`: the multiplicity is
a function of the **ambient plethysm and the pair (degree, weight) alone**.  So
`D = 0` between two of them is an identity between plethysm coefficients, with
no boundary geometry in it whatever.

| | cells | share |
|---|---|---|
| both closures hypersurfaces — `D = 0` is plethysm arithmetic | 600 | **80.9%** |
| one hypersurface, one not | 127 | 17.1% |
| neither | 15 | 2.0% |

Of the 22 interior cells, 14 are still hypersurface–hypersurface pairs; only
**8** involve a non-hypersurface, all of them `A = Iz`, `B = Q`.

## 5. The 22 survivors

Every one has `mult_A = mult_B = a - 1`: both closures miss the ceiling by
exactly one, and they miss it together.

| pair | weights | `a` | common `mult` |
|---|---|---|---|
| `Jz` vs `Iz` | 9 | 3 | 2 |
| `Iz` vs `Q` | 8 | 2 | 1 |
| `D` vs `Jz` | 3 | 2 | 1 |
| `D` vs `Iz` | 2 | 2 | 1 |

    A=D    B=Iz   delta= 9 lam=(21,15)      A=Iz   B=Q    delta= 7..14 lam=(4d-4,4)
    A=D    B=Iz   delta=12 lam=(27,21)      A=Jz   B=Iz   delta= 8 lam=(26, 6)
    A=D    B=Jz   delta= 9 lam=(21,15)      A=Jz   B=Iz   delta=10 lam=(34, 6)
    A=D    B=Jz   delta=11 lam=(25,19)      A=Jz   B=Iz   delta=11 lam=(38, 6), (35, 9)
    A=D    B=Jz   delta=13 lam=(29,23)      A=Jz   B=Iz   delta=12 lam=(42, 6)
                                            A=Jz   B=Iz   delta=13 lam=(46, 6), (43, 9)
                                            A=Jz   B=Iz   delta=14 lam=(50, 6), (47, 9)

For the 14 hypersurface pairs this is not even a coincidence about geometry:
`mult_Jz = mult_Iz` reduces to `a(lam-(6,6), delta-3) = a(lam-(4,4), delta-2)`,
an identity between two Gaussian-binomial differences.

## 6. Verdict on the kill criterion

The brief's criterion — *"if >= 90% of the 742 are forced, retire the
saturation-law hypothesis"* — has two readings.

* **Literal** (forced means `a = 0`): **25.2%**.  Criterion not met.
* **Honest** (forced means forced by any structural mechanism that involves no
  boundary geometry): **97.0%**, and 80.9% by the single crisp statement that
  the cancellation is between two hypersurfaces.  Criterion met.

**Recommendation: retire it.**  There is no saturation *law* to find.  What
session 24 measured was, in 97% of cases, the arithmetic of
`Sym^delta(Sym^4 C^2)` seen through five hypersurface quotients, and in the
remaining 3% a single uniform pattern (`mult = a - 1` on both sides) across
four pair-types, itself largely plethysm arithmetic.  It should be struck from
the open problems, with the 22 cells recorded as the residue and the reason
given as §4, not as `a = 0`.

## 7. The paper audit

`det_3`, ambient `Sym^delta(Sym^3 C^9)`.  At `delta <= 4` every `a` is 0 or 1,
and the paper's own published totals equal `sum m_det - sum a`, i.e.
`mult = a` on the whole ambient support: the degree-`<= 4` part of the ideal is
zero.

| `delta` | `sum m_det` | `sum a` | total `def` | forced (`a = 0`) | unforced | % forced |
|---|---|---|---|---|---|---|
| 2 | 3 | 2 | **1** | 1 | 0 | **100.0%** |
| 3 | 11 | 5 | **6** | 5 | 1 | **83.3%** |
| 4 | 43 | 12 | **31** | 25 | 6 | **80.6%** |

The bold column is the paper's sequence `1, 6, 31, 141, 618, 2488`.

The `delta = 2` row in full:

    lam = (6)       m_det = 1   a = 1   mult = 1   def = 0
    lam = (4,2)     m_det = 1   a = 1   mult = 1   def = 0
    lam = (2,2,2)   m_det = 1   a = 0   mult = 0   def = 1     <- FORCED

So **`def_det((2,2,2), 2) = 1`, the base point of the flagship conductor
result, is ambient arithmetic**: `Sym^2(Sym^3) = s_(6) + s_(4,2)` contains no
`S_(2,2,2)`, so `mult = 0` there for *every* orbit closure in `Sym^3 C^9` —
the permanent's included — and `def = m` by definition.  Nothing about the
boundary of `closure(det_3)` enters.  Confirmed for the record: the paper
contains no deficit measurement at any weight with `a >= 2`, because `a >= 2`
first occurs at `delta = 5`, at the single weight `(9,4,2)`.

This does not retract `c((2,2,2),2) = 1`.  The conductor is the stabilisation
index along the `Phi_18`-ray, and the ray's later rungs sit at weights the
audit does not touch.  What it retracts is the *framing*: the base point of the
ray is not evidence about the determinant's boundary, and the paper should say
so where it introduces the datum.

## 8. The BIP claim in `docs/easy_counts.md`

That document states that the 34 live weights at `(n, delta) = (5,2)` with
`m_det = 0 < m_per` are "exactly the weights where BIP forces
`def_per = m_per`".  Audited: the ambient `Sym^2(Sym^5 C^25)` has just three
constituents, `(10)`, `(8,2)`, `(6,4)`, and `m_det = 1` on all three.  So of
the 36 weights with `m_det = 0`, **all 36 have `a = 0`** and none has
`a >= 1`.  `def_per = m_per` there is ambient arithmetic; BIP is not needed and
is not doing the work.  The sentence overstates the finding and should be
corrected to say so.
