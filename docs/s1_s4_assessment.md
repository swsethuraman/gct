# Integrator assessment — S1 and S4, with S1's three tests run here and settled

## Part I — S1: the weight-13 tests, executed

S1 proposed reducing the first open stable question to an explicit polynomial
identity on five traceless `4×4` matrices, and nominated three multiplicity-one
tails at weight 13.  **The test is small enough that it was run here rather than
assessed.  All three are settled, and all three are negative.**

### Confirmed exactly

| `ρ` | `a_∞` | raw weight space | S1's figure |
|---|---|---|---|
| `(7,2,2,1,1)` | **1** | **2182** | 2182 ✓ |
| `(5,5,1,1,1)` | **1** | **2480** | 2480 ✓ |
| `(5,3,3,1,1)` | **1** | **5240** | 5240 ✓ |
| `(2,2,2,2,2)` | **1** | 1238 | (calibration) |

Newton identities as stated (`g_2 = −½tr A²`, `g_3 = −⅓tr A³`,
`g_4 = ⅛(tr A²)² − ¼tr A⁴`) are correct for `det(zI − A) = z⁴ + g_2z² + g_3z + g_4`
at `tr A = 0`; re-derived here.

### The correction — the raising-operator formula in the memo is the wrong normalisation

S1 gives `E_{i,i+1} y_{d,α} = α_{i+1} y_{d,α+e_i−e_{i+1}}`.  The substitution
`y_{d,α} ↦ [s^α] g_d` is the **plain-coefficient** convention, and in it the
operator is

    D y_{d,α} = (α_i + 1) y_{d, α+e_i−e_{i+1}}

which is `tools/verify/hwv.py`'s banked convention.  Derivation:
`A_{i+1} ↦ A_{i+1} + εA_i` is `s_i ↦ s_i + εs_{i+1}` inside `A(s)`, so
`g_d = Σ_α c_α s^α` acquires new coefficient
`c_β + ε(β_i + 1)c_{β+e_i−e_{i+1}}` at `β`.

The two are conjugate by `y_α ↦ y_α/α!` — with `β = α+e_i−e_{i+1}` one has
`β_i = α_i+1` and `α_{i+1} = β_{i+1}+1`, so the rescaling ratio is exactly
`α_{i+1}/(α_i+1)`.  **Both therefore give a one-dimensional kernel**, so the
`a_∞ = 1` check does not detect the mismatch, and **a non-highest-weight vector
evaluates to something nonzero generically — so the verdict would have looked
identical.**  As specified, the test would have produced an unfalsifiable
negative.

**The check that caught it, and which any future stable test must include:** a
genuine highest-weight vector's substituted polynomial is *invariant* under
`A_{i+1} ↦ A_{i+1} + εA_i` for every `i`, because the one-parameter subgroup
fixes it.  That is convention-independent.  Under S1's formula this fails at
every `i` and every `ε` tested, including at the calibration weight; under the
corrected formula it passes everywhere.

### The results

Run in the corrected convention, three independent random traceless
`5`-pencils over `p = 2147483647` each, `analysis/wk10_int_stable_hwv.py` and
`analysis/wk10_int_stable_subst.py`:

| `ρ` | HWV support | `F(g_2,g_3,g_4)` at 3 pencils | HWV check | verdict |
|---|---|---|---|---|
| `(2,2,2,2,2)` | 73 / 1238 | nonzero ×3 | **PASS** | `i_det^∞ = 0` — matches Theorem P |
| `(7,2,2,1,1)` | 118 / 2182 | nonzero ×3 | **PASS** | **`i_det^∞ = 0`** |
| `(5,5,1,1,1)` | 120 / 2480 | nonzero ×3 | **PASS** | **`i_det^∞ = 0`** |
| `(5,3,3,1,1)` | 486 / 5240 | nonzero ×3 | **PASS** | **`i_det^∞ = 0`** |

Each is **exact**: nonzero modulo one prime proves nonzero over `Z`, so a single
point certifies it.  No genericity assumption, no rank, no large target — exactly
as S1 designed.

The `(2,2,2,2,2)` row is the calibration and it lands where Theorem P says it
must: the peaked family has `a_∞ = 1` with the bordered discriminant as unique
highest-weight vector, nonzero at a generic pencil, hence `i_det^∞ = 0`.

### What this means, and what it does not

**Three tails are now permanently dead at every degree.**  `i_det` is
non-decreasing in `δ` and constant for `δ ≥ t`, so `i_det^∞ = 0` forces
`i_det(δ) = 0` for every `δ`.  That is three new closures at weight 13, banked
by a route that touches no Foulkes block.

**It does not prove `m_0(6) ≥ 14`.**  S1 says 47 partitions of length ≤ 5 have
nonzero stable multiplicity at weight 13; three of them have `a_∞ = 1` and are
now closed.  The other 44 have `a_∞ ≥ 2` and need a rank, not a single
polynomial.  S1's own escalation rule said to test the three and then decide —
the three are done, and the answer is that the weight-13 frontier is not closed
by them.

**The instrument is validated and it is cheap.**  Under two minutes per
multiplicity-one shape.  Its natural continuation is `a_∞ = 2` and `3` shapes at
weight 13, where the test becomes "is the `2`- or `3`-dimensional space of lines
entirely killed on `M_6`" — a small rank instead of one scalar, still with no
Foulkes target.  That is a well-posed follow-on and the record now has the code
for it.

## Part II — S4: agreed, with one cross-check

**The retirement of the `60 + 4` programme is right** and matches the measured
tangent data in `docs/rees_boundary_audit.md`.  **The primitive family as first
priority is right**, and the `n = 3` reason — compression analysis provably
misses a boundary component there — remains the strongest argument in the track.

**The chart is clean and correct.**  With `π : Λ²E → Q` and
`A_π(e)(v) = π(e ∧ v)`, every `A_π(e)` kills `e` (since `π(e∧e) = 0`) so has
rank ≤ 3, which is exactly the bounded-rank-three primitive family.  Building
the incidences as flag conditions on a `4 × 6` matrix — the common right kernel
being `π(v ∧ E) = 0`, i.e. `ker π ⊇ v ∧ E` — is far better than searching for
them.

**Cross-checked here:** the claim that the cheap border `3×3` determinant route
is closed at `r = 5`.  `dim{det_3 cubics in 5 vars} = 9·5 − 16 = 29` against
`dim Sym³C⁵ = C(7,3) = 35`, so a general quinary cubic is not a border `3×3`
determinant.  ✓  The same formula gives `dim X_{1+3} = 73 ⊂ dim D_9 = 114` in
`docs/one_plus_three_assessment.md`, so the two assessments are consistent.

**The decisive number is well chosen.**  `dim A_x = 35` affirmative,
`≤ 34` for every classified component negative, with the Jacobian-rank search
tried before any primary decomposition — that is the right order, and it is the
first `r = 5` brief that names a finite object rather than "more Rees order".

**The gap S4 names is the real one** and it should stay named: the exhaustion
statement — that every exceptional component over the primitive locus either
dominates the generic stratum or lies over one of finitely many classified
degenerations — is not proved.  Without it, `dim A_x ≤ 34` on the components
examined does not give `R_5 ⊄ D_5`.  C5 should report the components it
certifies and the exhaustion question separately, and not let the second be
carried by the first.
