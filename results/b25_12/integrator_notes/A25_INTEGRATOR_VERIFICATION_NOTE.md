# Integrator verification note — A25-01 and A25-02

**For intake by the B25-12 coordinator.** Written by the integrator (Claude, Cowork), 2026-09-21.
**This is not a review and it accepts nothing.** A25-10 is the reviewer for both packets and
governs. Both packets remain **UNCOMMITTED / NOT RELEASED** and this note does not change that.
Its purpose is to put one independent check on the record before A25-10 runs, so the reviewer
can choose whether to rely on it or redo it.

## What was checked, and against which bytes

The integrator worked from copies of the two reports uploaded by the user, **not** from the local
packets. Hashes of those copies:

| report | bytes | sha256 of the copy checked |
|---|---|---|
| `a25_01_report.md` | 8,176 | `76a231daea64473e39fd44acf8751e8dde4a3cf9ebc99958d4df96de42c05b10` |
| `a25_02_report.md` | 10,077 | `fc291cb906bd5dc3fbdc41344d4586239b18cc388833858739f800321cbaeb53` |

**The coordinator should confirm these match the local packets' bytes before relying on this
note.** A25-02 disclosed that its raw and filtered git bytes differ, so a mismatch is possible and
would not by itself indicate a problem — but it would mean this note was checked against a
different object.

The supporting files the reports cite — `PROOFS.md`, `CONSTRUCTION.md`, `IMPLICATIONS.md`,
`SCOPE_MATRIX.md`, `APPLICATIONS.md` — **were not read.** Everything below is checked against the
report text alone.

---

## A25-01 — the section theorem

### Verified: INDEPENDENT EVALUATOR (exact symbolic computation)

The construction in the report's §2 was rebuilt from its printed definitions and computed exactly
in `sympy` over `Q(a, r₁…r₄, q₁₁…q₄₄)`. **Every stated identity holds exactly:**

- `tr(u_i u_j) = 0`, `tr(v_i v_j) = 0` and `tr(u_i v_j) = δ_ij` for `u = (E₁₂, E₁₃, E₁₄, E₂₃)`,
  `v_i = u_iᵀ` — all sixteen of each.
- With `G` as printed, `D_i = u_i + ½ Σ_j G_ij v_j`, `C_i = (r_i/4)I₄ + D_i`, `B₁ = diag(a,1,1,1)`,
  `B_{i+1} = P_a C_i`, and `F = det(x₁B₁ + Σ y_i B_{i+1})`:
  - `[x₁⁴]F = a` ✓
  - `[x₁³ y_i]F = a·r_i`, i.e. `= p_i`, for all four `i` ✓
  - `[x₁² y_i y_j]F = q_ij` for all ten `i ≤ j` ✓ — **including the factor-of-½ asymmetry between
    the square and mixed cases** that the report states.

**All fifteen section identities are exact.** The printed formulas
`G_ii = 3r_i²/4 − 2q_ii/a` and `G_ij = 3r_ir_j/4 − q_ij/a` are correct.

This is a second lineage on the core computation, obtained outside the producing session. **It is
the certificate the report's own §5 names as "the one next certificate"** — independent
verification of the fifteen universal section identities. A25-10 may treat this as discharging it,
or redo it; the script is below so it can be replayed rather than trusted.

### Assessed: READ only

The inference chain — a rational section on `{a ≠ 0}` ⟹ the parametrisation is dominant onto
`Spec R2` ⟹ `R2 → C[X]` is injective (the composite with localisation `R2 → R2[a⁻¹]` is the
identity inclusion) ⟹ `K ∩ R2 = 0` — **reads as sound.** This part was not independently
evaluated; it is a short argument and A25-10 should read it for itself.

### One arithmetic error found

The report's §4 gives **`binom(77,8) = 21,042,084,900`**, attributed "as priced in B23-02".
The correct value is **`binom(77,8) = 21,042,072,975`**. The difference (11,925) is immaterial to
the infeasibility argument, which only needs the order of magnitude. **But the attribution means
either B23-02 printed the wrong figure or A25-01 miscopied it**, and A25-10 should check B23-02's
text to say which, since a wrong figure in a committed packet will propagate.

The report's other quoted binomial, `binom(22,14) = 319,770` for `dim U₈`, is **correct**.

### Frame, recorded so it is not over-read

Fifteen coordinates of a 65-parameter family being algebraically independent is close to the
generic expectation. **The report says this itself** — it closes one framed family, not row 12,
not all allowed jets, not combinations of frames — and that scoping is correct. The theorem's
value is that the corner is now closed by proof rather than by expectation, not that a likely
survivor has been killed.

---

## A25-02 — the typed scope matrix

### Assessed: READ only

**Theorem A** — *`H` contains an equation nonzero at the padding point iff `p ∉ row(Q)` iff
`rank([Q;p]) = rank Q + 1`* — **reads as correct.** Writing `h = Σ c_j h_j`, `h ∈ ker φ*` iff
`c ∈ ker Q`, and some such `c` has `p·c ≠ 0` exactly when `p ∉ (ker Q)^⊥ = row(Q)`. Elementary,
and the right finite statement of the missing certificate.

**The framework finding lands on the integrator.** A25-02 was the integrator's proposal to compute
the intersection of the exclusions. Its answer — that they concern different types of object and
a six-way intersection without bridging maps is ill-typed — is recorded here as a finding against
that proposal. It is the second time a producer has found an integrator question malformed rather
than hard (B23-02's row-10 result was the first).

### Not verified — flagged for A25-10 first

**Application 3's two numbers.** The exclusion of large-minor extraction from `M₇` on all of `P5`
rests on a uniform padding ceiling of **245** below a certified determinant floor of **299**. If
both hold, it is a new premise-free exclusion and **the most consequential claim in either
packet.** The integrator did not check either number and recommends A25-10 check them before
anything else in A25-02.

---

## Two flags for the reviewer, neither a quality claim

**Elapsed time.** A25-01 records its first substantive checkpoint at `00:45:06Z` and its
construction frozen at `00:46:10Z`. A25-02 is timed from `00:44:57Z` and frozen by `00:46:29Z`, and
lists reading across roughly fourteen packets' worth of sections. The A25-01 mathematics checked
above is correct, so this is not a claim that anything is wrong. It is a factor A25-10 should weigh
in deciding how much of A25-02's scope matrix rests on reading done in that window versus on prior
familiarity — the same way B22-10 was told to weigh a producer's model choice.

**Byte preservation.** A25-02 disclosed that raw and filtered git bytes differ for its report.
That is a delivery-pass item and must be resolved before commit, as PART 14 did for `B23-04` and
`B23-05`.

---

## Replay script — the A25-01 section check

Requires `sympy`. Runs in a few seconds. Prints `True` on the last line when all fifteen hold.

```python
import sympy as sp
def E(a,b):
    M=sp.zeros(4,4); M[a-1,b-1]=1; return M
u=[E(1,2),E(1,3),E(1,4),E(2,3)]; v=[m.T for m in u]
assert all(sp.trace(u[i]*u[j])==0 for i in range(4) for j in range(4))
assert all(sp.trace(v[i]*v[j])==0 for i in range(4) for j in range(4))
assert all(sp.trace(u[i]*v[j])==(1 if i==j else 0) for i in range(4) for j in range(4))
a=sp.symbols('a',nonzero=True); r=list(sp.symbols('r1:5'))
qs=list(sp.symbols('q11 q12 q13 q14 q22 q23 q24 q33 q34 q44'))
idx=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
qd=dict(zip(idx,qs))
G=sp.zeros(4,4)
for i in range(4): G[i,i]=sp.Rational(3,4)*r[i]**2-2*qd[(i,i)]/a
for i in range(4):
    for j in range(i+1,4):
        G[i,j]=G[j,i]=sp.Rational(3,4)*r[i]*r[j]-qd[(i,j)]/a
D=[]
for i in range(4):
    S=sp.zeros(4,4)
    for j in range(4): S+=sp.Rational(1,2)*G[i,j]*v[j]
    D.append(u[i]+S)
C=[sp.Rational(1,4)*r[i]*sp.eye(4)+D[i] for i in range(4)]
x1=sp.symbols('x1'); ys=list(sp.symbols('y1:5'))
M=x1*sp.eye(4)
for i in range(4): M+=ys[i]*C[i]
P=sp.Poly(sp.expand((sp.diag(a,1,1,1)*M).det()),x1,*ys)
ok = sp.simplify(P.coeff_monomial(x1**4)-a)==0
ok &= all(sp.simplify(P.coeff_monomial(x1**3*ys[i])-a*r[i])==0 for i in range(4))
for (i,j) in idx:
    mon = x1**2*ys[i]**2 if i==j else x1**2*ys[i]*ys[j]
    ok &= sp.simplify(P.coeff_monomial(mon)-qd[(i,j)])==0
print("all fifteen section identities exact:", ok)
```

Output when run by the integrator: `all fifteen section identities exact: True`.
