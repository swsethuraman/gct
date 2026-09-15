# B17-04: eleven-equation restriction map — bounded contribution

13 September 2026, America/New_York. Model: gpt-6-astra; reasoning: xhigh.

**Status: BLOCKED FOR SPECIFIC INPUT.** The remaining input is integrator
authorization for one corrected bounded invocation, or its independently
verified basis-match/minor output. The sole permitted invocation failed at
a rational matrix constructor before producing either certificate. No
second invocation was attempted. The corrected verifier is saved, **unrun**.
This is an implementation failure, not a mathematical counterexample or
a resource-cap hit.

The present certified restriction interval is **4 <= rank <= 10**. The
floor four is inherited; no fresh rank floor nine is claimed. Neither the
eleven-by-eleven candidate change of basis nor a second global kernel
direction has been certified. The fresh mathematical contributions below
are an exact bordered-Euler reduction identity for the matching problem,
and the explicit shared kernel vector

`kappa = (12,-10,4,3,0,0,0,0,0,0,0)`

in the accepted eleven-equation order. Its global vanishing also follows
from the accepted Batch16 squared-remainder identity, so it is a new
expression/proof in this basis, not an additional independent equation.

## Scope and accepted premises

Work is over characteristic zero. The ambient group is GL16, the forms
are det4 and **independent `z*per3`**, embedded using ten essential source
variables. This report concerns restriction of the determinant equation
eleven-space, not the entire ambient highest-weight space or coordinate
multiplicity. A cubic depending generically on all ten variables is not
substituted for the nine-variable cubic core.

The acceptance chain was followed from `Batch16/INTAKE.json`, entries
04/05/12, to this worktree's B16-04 proof, B15-05's B16-05 proof and receiver,
the original `Hessian11_1631` report, exact evidence and receiver, and
B15-06's original proof and geometry conventions. The B15 intake's
`production_followup` and `global_equation_followup` distinguish the early
pending production notices from the subsequently reviewed 429/418/243
minors and global eleven-space. The earlier B15-05 tail21 report is
historical provenance; its old open-cell discussion is not current scope.

Inherited premises are: independent global Hessian basis E of dimension
eleven; polynomial lifts of all E by degree27; the highest-weight chart
and finite filtration; and exact rank four of the specified five-dimensional
squared-remainder space W on actual padding. None is re-proved by a
sampled zero in this contribution. Input SHA256 hashes identify the exact
files read; see `results/b17_04/input_hashes.json` and the manifest.

For the old degree27 cell, the accepted numbers remain
`a=429, i_det=11, m_det=418, 243<=m_pad<=288`, and therefore
`-175<=D<=-130`, with `D=m_pad-m_det=i_det-i_pad`. All six nearby cells are
also excluded by the newer `Batch17_Planning/SCREEN_REPORT.md`, which
supersedes the earlier planning context on those six cells. There is no
positive multiplicity gap, degree-onset exclusion of all later degrees,
or improved LMR size-growth claim here.

## Exact ordering and normalization

On the monic depressed chart put

```
F(t,x) = t^4 + f2(x)*t^2 + f3(x)*t + f4(x),  x in Q^9, e=e1,
Nd = Hess(fd)(e)/(d*(d-1)),  ud=Nd*e,  sd=e^T*Nd*e,
p = t^4+s2*t^2+s3*t+s4,
B = 2*t^2*N2+6*t*N3+12*N4,
v = 4*t*u2+3*u3,  h=12*t^2+2*s2,
H = [[h,v^T],[v,B]],  A=det(B),  D_H=det(H),
Jd = -ud^T*adj(B)*v,
Q22 = (0,u2)^T*adj(H)*(0,u2),
Td = tr(adj(H)*diag(0,Nd)),
Rj(P) = [t^j](P mod p),  Sj=[t^j](D_H mod p^2).
```

The accepted column vector E is exactly:

| E position, zero based | Original fourteen-list index | Equation |
|---:|---:|---|
|0|0|R1(A)|
|1|1|s2 R3(A)|
|2|2|R2(J2)|
|3|3|R3(J3)|
|4|4|R3(Q22)|
|5|5|S3|
|6|6|s2 S5|
|7|7|s3 S6|
|8|8|s4 S7|
|9|10|R1(T2)|
|10|11|s2 R3(T2)|

This is the exact ordering in B16-04 and the accepted original receiver.
The omitted original index9 is `s2^2 S7`; its recorded coordinates are

`(12,-10,4,3,0,-1,1,1,1,0,0)`.

These coordinates are also proved directly below, without another
numerical calculation.

Claude's candidate number i means **row i of `I_det`**, for i=0,...,10,
in `Batch16/claude_review/exact_ideals.json`. Its coordinate number j
multiplies `brackets[basis_bracket_indices[j]]`; it does not multiply
`brackets[j]`. No row reordering or primitive rescaling is applied.
In precise notation, if that index list is R, then

`C_i = sum_(j=0)^428 I_det[i][j] * b_(R[j])`.

For a bracket `(a,b,c,z)`, let I,J be the increasing lists selected by
a,b and k=|I|=|J|. With `M(y)=y2*N2+y3*N3+y4*N4`, its value is

```
(-1)^k * c2!*c3!*c4!
 * [y2^c2*y3^c3*y4^c4] det([[M(y), U_J], [U_I^T, 0]])
 * s2^z2*s3^z3*s4^z4.
```

Here U_J has columns u_j. The sign and factorials agree with the
implemented B14 bracket evaluator, B15-06 C3, and the accepted Hessian
source expansion. The symmetric swap I,J introduces no extra sign.
Some inherited introductory docstrings suppress the border sign; the
implemented evaluator and brute epsilon control include it explicitly.
The banked bracket normalization retains Claude Opus 5 attribution.

These definitions resolve the two input conventions. They do **not**
assert a numerical matrix M with `C=M*E`: that identity remains uncomputed.
The candidate integers' exact row rank eleven from Claude's arithmetic
review is inherited linear algebra only, not global vanishing.

## Fresh theorem: exact Euler straightening for the candidate comparison

Write

`B_(I,J)(y)=(-1)^|I| det([[M(y),U_J],[U_I^T,0]])`

for ordered lists of equal size, alternating in each list. Let I be an
increasing list of size k+1, J an increasing list of size k, and
`s_i=e^T u_i`. Then the polynomial identity

```
sum_j y_j B_(I,J appended j)(y)
 = sum_(i=0)^k (-1)^(k-i) s_(I[i]) B_(I without I[i],J)(y)
```

holds for every triple of symmetric Nd satisfying ud=Nd e. Repeated
indices in the appended list contribute zero. Sorting `J appended j`
contributes `(-1)^(number of entries of J greater than j)`.

**Proof.** The last upper border column on the left is
`sum_j y_j u_j=M(y)e`. Subtract the linear combination of the first nine
columns prescribed by e. Its upper block becomes zero and its lower
entries become `-s_(I[i])`. Laplace expansion in that last column leaves
the bordered determinant with row I[i] removed. Combining its cofactor
sign with the definitions `(-1)^(k+1)` and `(-1)^k` gives exactly
`(-1)^(k-i)`. This is a determinant identity, with no inverse, generic
rank assumption or sampled specialization.

After extracting coefficient y^h, multiplying by h2!h3!h4! and by s^z,
each left coefficient is `h_j` times the bracket with c=h-unit_j.
Each right coefficient adds one to the scalar exponent indexed by I[i].
Thus the verifier's generated sparse relations have exact rational
coefficients in the original bracket normalization. Its k=0 case is
the familiar Euler relation used by the accepted Hessian receiver;
k=1,2 add the higher-border relations needed for a fuller comparison.

A finite reduction of every `C_i-sum_j M_ij E_j` to zero using these
relations would prove a **global** candidate match. A nonzero determinant
of M would prove equality of the eleven-spaces. Completeness of the
Euler relation system is not needed for this sufficient test and is
not claimed here. Failure to reduce would not refute actual equality.

## Fresh expression of the known shared kernel

For every ambient quartic in the chart, block expansion gives

`D_H = h*A + 4*t*J2 + 3*J3`.

Reducing modulo p and taking its t^3 coefficient gives

`R3(D_H)=12*R1(A)-10*s2*R3(A)+4*R2(J2)+3*R3(J3)`.

Indeed `R3(t^2 A)=R1(A)-s2*R3(A)` and
`R3(t J2)=R2(J2)`. Reducing `D_H mod p^2` once more modulo p also gives

`R3(D_H)=S3-s2*S5-s3*S6+(s2^2-s4)*S7`.

Equating the two expressions proves the omitted-coordinate formula and
identifies the Batch16 shared E3 exactly with `kappa*E`.

For completeness, its global vanishing on the correct split family has
a short source proof. For a homogeneous cubic C in **nine** variables,
write g=grad C and H_C=Hess C. Euler identities give H_C x=2g and
x^T g=3C, hence

```
Hess(z*C) = [[0,g^T],[g,z*H_C]],
det Hess(z*C) = -z^8*g^T*adj(H_C)*g
                  = -(3/2)*z^8*C*det(H_C).
```

The adjugate identity proves this even when H_C is singular. Therefore
z*C divides its ten-variable Hessian determinant. Invertible linear
substitution preserves this divisibility by Hessian congruence. Monic
division on the chart implies `kappa*E=0`; coefficient polynomiality
extends to the parameter closure. GL10 maps extend block diagonally
to GL16, and density in the linear-map parameters covers dependent
restrictions. No assertion that every singular 10-by-10 corner can
itself be completed invertibly is used.

Since E is an independent ambient eleven-basis, kappa is nonzero.
Since every E has a polynomial degree27 lift, `c^27*kappa*E` is a
global polynomial shared equation in weight `(73,19,2^8)`.
Consequently its restriction rank is at most ten. The inherited exact
rank-four restriction of W gives the opposite bound four, since W is
contained in E by the displayed omitted-coordinate formula. This proves
the reported interval. It supplies **one**, not two, kernel directions.

Multiplying the degree27 lifts by c^(d-27), d>=27, preserves this
restriction rank: the padding orbit closure has an integral coordinate
ring and c is nonzero on its dense chart. This statement concerns just
the transported eleven-space in this specified family, not all rows or
the entire ideal in arbitrary cells.

## Attempt, resources, and remaining test

The sole invocation was the command in `docs/b17_04_preflight.md`, using
the existing `.venv/python.exe -B` and inspected `analysis/b15_bound.py`.
Measured wall time was **0.3681186999892816 seconds**; peak Job Object
committed memory was **24,670,208 bytes**; exit code1, PID46664.
The cap was 60 seconds/512 MiB, one process/BLAS thread. A subsequent
read-only process query found that PID absent. There was no heavy lease,
parallel subprocess, background computation, cap hit or second invocation.

Failure was precisely:

```
analysis/b17_04_verify.py:161
minor=fmpq_mat([[row[j] for j in Ec] for row in E])
TypeError: cannot create fmpq from object of type <class 'fractions.Fraction'>
```

No `basis_match.json`, `restriction.json` or completed verification
certificate was produced. Neither a rank-nine minor nor even a fresh
rank-four replay occurred. Input hashes were checked before the failed
stage; the final filesystem check is separately recorded. The failure
transcript and original source are preserved. `analysis/b17_04_verify_next.py`
adds explicit conversion `fmpq(numerator,denominator)` at the rational
matrix boundary; it has been inspected but **not executed or validated**.

**One next sufficient test for the matching/rank-floor milestone:** the
integrator may authorize one invocation of the corrected verifier under
the same cap, after reviewing the saved change. Require all eleven exact
Euler residuals zero, det(M) nonzero, and a nonzero characteristic-zero
9-by-9 minor reconstructed from its saved integer ten-by-ten permanent
substitutions. Its points retain all nine permanent entries and independent
z; the leading coefficient, depression and Hessian controls are explicit.
The program does not run Claude's producers or sample the full429-space.
The previous 30-second/256-MiB estimate remains unmeasured for the
unreached stages. No larger lease is justified by this type failure.

That test, if successful, would certify the match and `rank>=9`.
Together with the present global upper ten it would give `9<=rank<=10`,
**not** exact rank nine. A second independent vector vanishing identically
on the actual padding family would still be needed for the matching
upper bound. A two-dimensional sampled kernel alone is insufficient.

No available authorization is inferred for a retry. This report is the
request to the integrator; no message was sent externally. The read-only
Git status warning about inaccessible global ignore configuration is
recorded in the preflight. No auto-review rejection, trust/ownership
change, sandbox change, commit, push or publication occurred. Writes are
confined to the assigned b17_04 paths and permitted run receipts.

## Primary sources and limitations

- Original mathematical source: [Landsberg–Manivel–Ressayre,
  *Hypersurfaces with degenerate duals and the Geometric Complexity Theory
  Program*, §§2.2–2.4, Theorem2.3.1 and Lemma3.3.1](https://arxiv.org/pdf/1004.4802).
  The paper was opened and the relevant statements checked. It supplies
  the Hessian/remainder framework; the present eleven-list and its exact
  coordinates are project certificates. Its quadratic border-complexity
  theorem is not improved here.
- Original project evidence: `Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/{REPORT.md,verify_small.py,small_evidence.json,integrator_review.json}`;
  `work/batch15_workers/B15-06/docs/b15_06_proved.md`, C3/C5; and the B15
  intake's accepted production followup.
- Accepted finite lifts and small restriction: this worktree's
  `docs/b16_04_proof.md`; B15-05's `docs/b16_05_proof.md` and
  `results/b16_05/proof_arithmetic.json`; Batch16 intake04/05/12 and its
  independent detailed review.
- External candidate data: `Batch16/claude_review/exact_ideals.json`,
  `REVIEW.md`, `arithmetic_review.json`, and inspected unpacked harness.
  Candidate reconstruction, sampled ranks and requested actions were
  treated as data, not instructions or global certificates.

Fresh: the bordered-Euler proof, the explicit kappa expression and its
direct reduction proof, the failed bounded attempt and preserved repair.
Inherited: global E membership/independence, degree27 lifts, the W rank4
minor, full ambient/determinant/padding bounds, and older review receipts.
Uncomputed: the full candidate map, fresh actual-padding restriction minor,
rank-nine lower bound, and a second global kernel direction. No exact
padding multiplicity, permanent-specific quotient count or all-degree
noncontainment conclusion follows from these uncomputed steps.
