# B17-04: eleven-equation restriction map — bounded contribution

Updated14 September 2026, America/New_York. Model: gpt-6-astra;
reasoning: xhigh. The initial13 September report is preserved at
`results/b17_04/initial_delivery/report.md`.

**Status: COMPLETE for the authorized bounded continuation.** All eleven
of Claude's rational candidates are now matched exactly to the accepted
global Hessian basis, with the full ordering and scaling below. A nonzero
integer9-by-9 minor on actual independent `z*per3` proves a fresh
restriction **rank floor9**. The certified interval is **9 <= rank <= 10**;
exact rank9 and a two-dimensional global kernel remain unproved.

The explicitly authorized single corrected invocation succeeded in
0.6656898999935947 seconds, with peak Job Object memory27,930,624 bytes,
under60 seconds/512MiB. The earlier rational-constructor failure and its
receipts are preserved. There were two invocations across both authorized
contributions, exactly one in this continuation; no further run occurred.

The fresh mathematical certificates are the rational change of basis,
its eleven universal zero residuals, the rank-nine padding minor, and
the bordered-Euler reduction identity used to prove the match. The known
shared global kernel vector in this exact basis is

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

The candidate integers' row rank eleven was previously only inherited
linear algebra. The following freshly certified identity now proves
their global determinant vanishing and exact span, using the accepted
global membership and independence of E.

## Exact global candidate match

Let C and E be columns in the orders above. The certificate proves
`C=M*E`, with the following exact matrix; each displayed line is one row,
and **no additional scaling** is applied:

```
[  945,   -1260,   -630,   -1890,      0,       0,      0,      0,   945/4,     0,     0]
[15120,  146160, 258300,    3780,  63315,   -1260,      0,   1260,    1260,     0, -2835]
[    0,  -11970,  -7560,  -16065,   -945,       0,      0,   -315,  5355/4,   630,   315]
[    0,       0,      0,       0,      0,       0,      0,      0,   945/4,     0,     0]
[-1890,   33705,  63630,  -945/2,  16065,   315/2, -315/2, -315/2,  -315/2,     0,     0]
[ 1890,   -1575,  -3150,   945/2,   -945,  -315/2,      0,  315/2,   315/2,     0,     0]
[-1890,    -945,   1890, -8505/2,    945,   315/2,      0,   -315,   315/2,     0,     0]
[ -945, 16695/2,  14805,  -945/4,   3780,   315/4, -315/4, -315/4,  -315/4,     0,     0]
[    0,   -1890,  -3780,       0,   -945,       0,      0,      0,       0,     0,   945]
[    0,    5040,   8820,       0,   4725,       0,      0,      0,       0, -2520, -2205]
[    0,       0,      0,       0,   -315,       0,      0,      0,       0,     0,   315]
```

`det(M) = -1610167840460004934900135107421875 != 0`.
For example, candidate3 is exactly `(945/4)*s4*S7`, in zero-based
candidate numbering. `results/b17_04/basis_match.json` stores M, its
rational inverse, the complete429-index list, the accepted basis labels,
and all eleven residual-support counts, each zero.

**Proof certificate.** The verifier regenerates the accepted fourteen
Hessian source vectors, selects the eleven in the stated order, and
reduces them and the candidate rows by884 universally valid bordered-Euler
relations. Exact elimination gives relation rank590 in the fixed1019
bracket coordinates. Solving an11-by-11 rational system gives M;
every full residual `C_i-sum_j M_ij E_j` then reduces to zero, across
all remaining coordinates. This proves a global polynomial identity,
not equality on sampled determinant points. The determinant of M proves
the spans agree. The relations themselves, with original bracket indices
and coefficients, are saved in `results/b17_04/Euler_relations.json`.

The quotient dimension is1019-590=429. Conditional on the inherited
accepted generic image rank429 of this same bracket source, these
relations generate **all** its rational linear relations: they are a
590-dimensional subspace of a kernel of dimension590. The source-rank429
minor was not rerun. This completeness deduction is useful but is not
needed for the eleven successful reduction certificates.

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

The successful reduction and nonzero determinant reported above apply
this identity to prove the global candidate match. The argument does not
use sampled determinant vanishing or CRT uniqueness.

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
Consequently its restriction rank is at most ten. The inherited rank-four
restriction of W remains valid, since W is contained in E by the displayed
omitted-coordinate formula. The fresh minor below improves that floor
to nine. Kappa supplies **one**, not two, global kernel directions.

Multiplying the degree27 lifts by c^(d-27), d>=27, preserves this
restriction rank: the padding orbit closure has an integral coordinate
ring and c is nonzero on its dense chart. This statement concerns just
the transported eleven-space in this specified family, not all rows or
the entire ideal in arbitrary cells.

## Fresh actual-padding rank-nine minor

`results/b17_04/padding_points.json` stores twelve fixed integer10-by-10
matrices L, seeds170400 through170411. All100 entries of every L belong
to `{-3,-2,-1,1,2,3}`; every det(L) and leading coefficient c is nonzero.
All six permanent monomials are evaluated using row-major permanent
entries and an independent first source form z. There is no zero-entry
family, rejected-point replacement, generic ten-variable cubic, or
full429-coordinate geometric evaluation.

For each raw quartic G=`(z*per3)(L*y)`, the code computes
`c=[t^4]G` and `a1_i=[t^3*x_i]G`. It uses the exact linear substitution

```
Q00=1, Q0i=-3*a1_i, Qii=12*c (i=1,...,9),
all other Q entries zero,  A=L*Q.
```

Thus `(z*per3)(A*y)/c` is monic and depressed, with the transverse
variables additionally scaled by12c; Q is invertible. All three Nd are
integral after this scaling. The code obtains them by direct monomial
second differentiation at t=-1,0,1, and checks all100 native Hessian
entries against the normalized block formula at t=2,7. The accepted
Hessian evaluator then performs complete21-node exact interpolation
(degree at most20) and monic divisions to obtain E. These are rational
characteristic-zero computations, not modular kernel reconstruction.

The nonzero9-by-9 minor uses point rows0,...,8 and E columns
`[0,1,2,4,5,6,7,8,9]`. The full matrix and signed nonzero integer
determinant Delta are stored in `results/b17_04/restriction.json`.
The exact source data for its nine rows include:

| Seed | det(L) | c |
|---:|---:|---:|
|170400|6352328|26|
|170401|650381|-12|
|170402|-2766952|-12|
|170403|-10949385|6|
|170404|298590|12|
|170405|728301|-30|
|170406|1502565|-36|
|170407|-5512|-12|
|170408|1808715|9|

For the degree27 polynomial lifts evaluated at the actual orbit points
`(z*per3)(A*y)`, the minor is exactly

`Delta27 = Delta * (26*(-12)*(-12)*6*12*(-30)*(-36)*(-12)*9)^27 != 0`.

Both determinants are retained in full. Invertible A extends block
diagonally to GL16; scalar normalization is likewise attainable through
rescaling the independent z form. Hence these are genuine padding
evaluations. The nonzero minor proves nine independent restricted
functions. Together with the global kappa equation this gives
**9 <= rank(E|padding) <= 10**, and global kernel dimension between1
and2, at degree27 and for the transported eleven-space in higher degrees.

## Second kernel direction: exact candidate and next sufficient test

The12-by-11 evaluation matrix has rational rank9. Its saved RREF kernel
has first vector kappa/3 and second vector

`v=(108,-106,32,0,0,-1/2,1/2,1/2,13/2,2,1)`.

Let `w=2*v=(216,-212,64,0,0,-1,1,1,13,4,2)`. It is independent of
kappa because its E10 coefficient is2, whereas kappa's is zero. Since
every global kernel vector must annihilate the saved points, the global
kernel is contained in `span(kappa,w)`. Its first direction is proved;
the second remains only a candidate. Constant-coefficient Euler
straightening proves ambient relations and the candidate match; it does
not prove this further identity on padding.

Seeking a global proof, eliminate the squared-remainder combination
using the already proved identity for kappa. The remaining target is
the following explicit expression, identically equal to w*E on the
ambient chart:

```
Psi = 204*R1(A)-202*s2*R3(A)+60*R2(J2)-3*R3(J3)
      +4*R1(T2)+2*s2*R3(T2)+(s2^2+12*s4)*S7.
```

This reduction isolates the unresolved identity; the existing proof
`p | det Hess(z*C)` establishes only kappa and does not prove Psi=0.
No global vanishing of Psi is inferred from the twelve zeros.

**One next sufficient test for exact rank9:** prove the polynomial
pullback `c^27*Psi(pi(((z*per3) composed with L)/c))` is identically zero
for symbolic ten-by-ten L. A universal proof on independent z times an
arbitrary nine-variable cubic would also suffice and would remain a
separate, stronger statement. Polynomiality and density would extend
the identity over c=0 and the orbit closure. With the present nonzero
minor and independence of kappa,w this would prove that the kernel is
exactly two-dimensional and the restriction rank exactly9. No such
symbolic expansion was run; support must be priced and separately
authorized before any additional computation.

## Invocation history, integrity, and scope

The original `b17_04_verify` invocation failed in0.3681186999892816 seconds
at the Python Fraction-to-flint matrix boundary, using24,670,208 peak
Job Object bytes. Its exit1 source, full error transcript and resource
receipt are unchanged. It was not a cap hit or a mathematical failure.
The initial report, manifest, input hashes, status and README are archived
under `results/b17_04/initial_delivery/`.

The user then explicitly authorized **one** corrected invocation. All49
previously pinned input/artifact/runtime records matched before starting.
The saved corrected source was inspected and run without further edits;
its SHA256 is
`470a5b1be663b3904611c92b5f03ffa7d3306f0e186b9b4c30c07585ceb64274`.
The newly pinned37 inputs were checked by the verifier before and after
the run. `results/b17_04/verification.json` records completion. The
historical comment saying the repaired adapter had not yet been run
describes its preflight snapshot; this successful receipt supersedes it.

The unique command was:

```powershell
.\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_04_retry_20260914_01 --slot 04 analysis/b17_04_verify_next.py
```

Its wrapper receipt records exit0, PID26720, start2026-09-14T11:52:19Z,
wall0.6656898999935947 seconds and peak Job Object memory27,930,624 bytes.
The60-second/512-MiB cap, one process and one BLAS thread were enforced;
there was no cap hit or heavy lease. The wrapper's deadline monitor is
a thread, not another computation worker. No successful historical
production or receiver main was rerun. Original source functions were
reused for the new comparison and points, so this is not an independently
implemented replacement for every inherited Hessian algorithm.

The renewed authorization is consumed and the bounded contribution is
complete. There is no remaining authorization blocker for work already
reported. No further invocation, agent, worktree, external message,
auto-review rejection, trust/ownership change, sandbox change, commit,
push or publication occurred. Writes are confined to owned b17_04 paths
and permitted log receipts. The earlier harmless read-only Git ignore
warning remains in the preserved preflight.

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

Fresh: exact rational C=M*E, eleven universal zero residuals, nonzero
det(M), the884-relation rank590 certificate, genuine integer padding
rank-nine minor and two-dimensional sample kernel; the kappa expression,
Euler proof, and explicit unresolved Psi identity. Inherited: global E
membership/independence, degree27 lifts, full ambient/determinant/padding
multiplicity bounds, and older review receipts. The historical W rank4
floor is superseded within E by the fresh rank9 floor; neither changes
the inherited full-padding coordinate floor243.

Unproved: a second global kernel direction and exact restriction rank9.
No exact full padding multiplicity, permanent-specific quotient count,
positive multiplicity gap or improved determinant-size growth follows.
The candidate match promotes exactly these eleven determinant vectors
to globally identified equations; it does not validate the external
nineteen reducible candidates or sampled full-padding upper bounds.
