# B17-05: the complete degree-26 flag multiplication image

**COMPLETE for the specified finite target.** The full image of the one LMR
flag module `E24` multiplied by all quadratic coefficient polynomials has
multiplicity **5** in degree26, weight `(69,19,2^8)`. Its three multiplier
parts have image dimensions **1,3,1**, with independent combined images.
The accepted complete determinant ideal has multiplicity10 in this cell,
so its quotient by this image has dimension **5**. Five explicit quotient
representatives and nonzero exact modular minors are delivered below.

This finishes the degree26 five-channel image that B16-06 left partial.
It does not finish degree27, the full nonflag degree24 remainder ideal,
or any saturation. There is no determinant-size improvement or positive
multiplicity gap. Research: gpt-6-astra, xhigh, existing B15-05 worktree;
2026-09-13 local date (run timestamp 2026-09-14 UTC).

## Precise finite statement and hypotheses

Work over Q, or C after scalar extension. Let `V=C^16`, let quartic forms
belong to `Sym^4(V*)`, and use ordinary coefficient functions
`c_alpha(G)=[x^alpha]G`. Thus their polynomial coordinate ring is
`A=Sym(Sym^4 V)`, with coefficient-degree piece `A_d`. All partitions
below label polynomial representations in this coordinate-ring convention.

Let `E24` be the **specified nonzero flag copy**
`S_(65,17,2^7) V` in `A_24`, obtained by the LMR ordinary 9-minor remainder
construction with the binary plane contained in the Hessian 9-plane.
Set `Jflag=(E24)`, and fix

```
d = 26,  lambda = (69,19,2,2,2,2,2,2,2,2).
mu_lambda: Hom_GL16(S_lambda V, E24 tensor A_2)
        -> Hom_GL16(S_lambda V, A_26).
```

Here the map is polynomial multiplication. The dimensions in this report
are dimensions of these multiplicity spaces, not dimensions of the full
Schur modules. In particular `Jflag_26 = image(E24 tensor A_2 -> A_26)`.

**Theorem.** `rank_Q(mu_lambda)=5`; its five-dimensional source has zero
kernel. The source parts `S8`, `S62`, `S44` of `A_2` have image dimensions
1,3,1, and their sum is direct in this multiplicity space. Under the
accepted B16-04 completeness/finite-filtration premises,

```
dim Hom_GL16(S_lambda V, I(det4)_26 / Jflag_26) = 10 - 5 = 5.
```

The rank-five assertion uses the accepted nonzero flag circuit and its
global vanishing, but does not require completeness of the determinant
ideal. The quotient assertion additionally uses the accepted full ideal
dimension10 and polynomiality of the listed B16-04 basis vectors. Neither
premise is inferred from newly sampled zeros.

The primary construction is [Landsberg–Manivel–Ressayre, arXiv:1004.4802v1,
§§2.2–2.3 and Theorem2.3.1](https://arxiv.org/pdf/1004.4802). Setting their
form degree to4 and dual-dimension parameter to6 gives equation degree24
and weight `48 omega1 + 15 omega2 + 2 omega9`, hence `(65,17,2^7)`.
The paragraph following that theorem explicitly retains planes outside
the Hessian subspace; it does not identify their full remainder module
with the single flag module.

## Five polynomial circuits and their highest weights

It suffices to construct five independent products using the first ten
variables. Polynomial multiplication and the flag module embed naturally
into sixteen variables; the exhibited highest weights have length10.
The LR upper bound below is also computed for the sixteen-variable target.

Use parameter vectors `a,b` and a covector `n` in dimension10, with the
`det(V)^2` twist understood when representing a 9-plane by its cofactor
covector. Put `c=G(a)`, `p(t)=G(ta+b)`, `H(t)=Hess G(ta+b)`, and

```
F(a,b,n) = c^16 [t^-1] n^T adj(H(t)) n / p(t).
R = a.d_b, C = b.d_a, Da = d_a.d_n, Db = d_b.d_n,
u = n(a), v = n(b).
```

The residue is at infinity. The adjugate has t-degree18, so at most15
reciprocal coefficients occur. Multiplication by `c^16` makes `F` a
polynomial of coefficient degree24 and parameter degrees `(63,15,2)`.
The accepted B16-06 flag projector is

```
Fh = F - v DbF/24 + u C DbF/1752 - u DaF/73
   + v^2 Db^2F/1104 - u v C Db^2F/40296 + u v DaDbF/1752
   + u^2 C^2 Db^2F/5802624 - u^2 C DaDbF/126144
   + u^2 Da^2F/10512.
```

Operators act on `F` to their right. B16-06 proves `DaFh=DbFh=RFh=0`,
preservation of the nonzero incidence class, and that its coefficient
module is precisely `E24`. Its proof uses the six multiplicity-one dual
Pieri constituents and trace eigenvalues `0,73,24,144,96,46`. This is an
inherited, reviewed projection theorem, not a projection inferred from
our new minor.

Define `cj=[t^(4-j)]G(ta+b)` and the genuine quadratic coefficient covariants

```
q8  = c0^2,
q62 = 8 c0 c2 - 3 c1^2,
q44 = 12 c0 c4 - 3 c1 c3 + c2^2.
```

These are highest covariants for `S8,S62,S44` in
`A_2 = S8 + S62 + S44`. Indeed `R cj=(5-j)c_(j-1)` for `j>=1`, so `R`
kills all three displayed covariants. Form symmetric two-tensors

```
M8  = Hess_a(q8),                M60 = Hess_b(q62),
Mab = sym(d_a d_b q62),          Maa = Hess_a(q62),
M51 = Mab + C M60/6,
M42 = Maa + C Mab/2 + C^2 M60/20,
M44 = Hess_b(q44).
```

Here `sym` averages a matrix with its transpose. These parameter
derivatives do not change the coefficient degree2 or the coefficient
module of the covariant. The free tensor indices are reserved for
contraction with the two n-indices of `Fh`.

For completeness, the raising relations are
`R M60=0`, `R Mab=-M60`, `R Maa=-2Mab`.
Since `[R,C]=a.d_a-b.d_b`,
`R C M60=6M60`, `R C Mab=-C M60+4Mab`, and
`R C^2 M60=10 C M60`. Thus `R` kills `M51` and `M42`.
The parameter bidegrees of `M8,M60,M51,M42,M44` are respectively
`(6,0),(6,0),(5,1),(4,2),(4,2)`.

Write `<M,Fh>=sum Mij d_ni d_nj Fh`. For `R M=0` of bidegree `(m,n)`,
put `h=m-n` and define

```
T_r(Fh,M) = sum_(i=0)^r a_i <C^(r-i) M, C^i Fh>,
a_0=1,
a_(i+1) = -a_i (r-i)(h-r+i+1) / ((i+1)(48-i)).
```

Because `Fh` has a-degree minus b-degree48,
`R C^i Fh=i(49-i)C^(i-1)Fh`. The analogous formula holds for `M` with
48 replaced by h. Adjacent terms in `R T_r` cancel by the displayed
recurrence. This proves that the five circuits

```
P1=T_2(Fh,M8),   P2=T_2(Fh,M60),   P3=T_1(Fh,M51),
P4=T_0(Fh,M42),  P5=T_0(Fh,M44)
```

are highest vectors, each of coefficient degree26 and parameter bidegree
`(67,17)` after contracting n. The determinant twist gives the required
weight `(69,19,2^8)`. For r2 the coefficients are `1,-5/24,5/376`;
for r1 they are `1,-1/12`. All operations are equivariant contractions
and parameter derivatives of elements of `E24` times elements of `A_2`.
Therefore the five circuits lie in the **actual multiplication image**
and are global determinant equations.

Finally the LR counts are

| Quadratic coefficient module | Target tensor multiplicity |
|---|---:|
| S8 | 1 |
| S62 | 3 |
| S44 | 1 |
| Total | 5 |

They are freshly recomputed for this one target using the pinned accepted
LR-tableau enumerator. This gives an upper bound5 on the full image,
independently of whether the displayed circuits are independent.

## Exact bounded evaluation and the matching lower bound

The executable [analysis/b17_05_verify.py](../analysis/b17_05_verify.py)
evaluates the five circuits in the exact field `F_2147483647`. It uses
14 fixed integer ambient jet points, saved in full in
[image_certificate.json](../results/b17_05/image_certificate.json).
At each point `a=e0,b=e1`, and

```
G(t,x)=t^4+f2(x)t^2+f3(x)t+f4(x),
Nd=Hess(fd)(e1)/(d(d-1)), ud=Nd e1, sd=e1^T Nd e1,
H(t)=[[12t^2+2s2,(4t u2+3u3)^T],
      [4t u2+3u3,2t^2 N2+6t N3+12N4]].
```

The symmetric matrices `Nd` are freely realizable second jets of
homogeneous forms `fd` at `e1`. These are actual ambient quartic points.
They are not asserted to be determinant points or padding points.

Every adjugate and determinant polynomial is reconstructed from all21
t-nodes `0,...,20`, a sufficient degree bound. Every sampled Hessian is
invertible modulo the prime. Its inverse is used only to evaluate the
adjugate, not to define a global equation. The reconstructed adjugates'
t-degrees19 and20 are checked to vanish.

For the parameter derivatives, write
`Lj=[t^-1]t^j adj(H)/p` and `Kj=[t^-1]t^j det(H)/p^2`.
Homogeneity and residue differentiation give

```
C Lj=(16+j)L_(j+1),    C Kj=(14+j)K_(j+1).
```

For example a homogeneous rational function `Q(ta+b)` of degree h satisfies
`C Q=t(hQ-t Q')`; taking the residue of `t^j` gives the factor `h+j+2`.
Here h is14 and12 respectively. Hence five-slot Taylor series in
`a -> a+z b` give exactly all derivatives needed: `Fh` is differentiated
at most twice, its projector contains at most two C derivatives, and the
maximum retained order is4. The largest source data are the 100 entries
of each small matrix. No full coefficient polynomial is expanded.

The evaluator uses the B16-06 proved residue identities for `DaF,DbF` and
their traces. At **every** point it independently compares the resulting
contractions against the accepted rational formulas for `P25`, `P26_62`
and `P26_44`, evaluated by the original exact integer Hessian code. Our
Hessians of the quadratic multipliers are twice B16-06's divided tensors;
the assertions explicitly check this factor2. All42 comparisons pass.

The five image columns at the first five points, seeds `917050..917054`,
have determinant

```
77620181 (mod 2147483647), nonzero.
```

All fixed rational denominators are units modulo this prime. This is a
nonzero specialization of a rational determinant, so the five original
characteristic-zero polynomial circuits are independent. Combining this
lower bound5 with the LR upper5 proves the full image rank exactly5,
and proves that the three module images are independent of one another.
No sampled rank plateau is used as an upper bound.

## A complete finite quotient basis

Use the accepted B16-04 stable coordinates, in the **eleven-position** order

```
E=(R1(A), s2 R3(A), R2(J2), R3(J3), R3(Q22),
   S3, s2 S5, s3 S6, s4 S7, R1(T2), s2 R3(T2)),
A=det B, B=2t^2 N2+6t N3+12N4,
Jd=-ud^T adj(B)(4t u2+3u3),
Q22=(0,u2)^T adj(H)(0,u2),
Td=tr(adj(H) diag(0,Nd)),
Rj(U)=[t^j](U mod p), Sj=[t^j](det H mod p^2).
```

Positions `E0,...,E10` here are consecutive positions, not the original
fourteen-source indices. For a general quartic let `pi(G/c)` denote its
normalized depressed chart, with `c=G(a)`. Define five actual polynomials
by the following rational chart formulas and their accepted polynomial
extensions:

```
Q0=c^26 (2 E0 + E1)(pi(G/c)),
Q1=c^26 (-2 E0 + E2)(pi(G/c)),
Q2=c^26 (-8 E0/9 + E3)(pi(G/c)),
Q3=c^26 (4 E0 + E4)(pi(G/c)),
Q4=c^26 (275 E0/3 + E5)(pi(G/c)).
```

These are the first five vectors in the pinned B16-04 degree26 kernel.
Its universal pole calculation proves their polynomiality and its global
Hessian identities prove determinant vanishing. They therefore belong to
`I(det4)_26` in the same weight as the multiplication image.

The first ten points, seeds `917050..917059`, evaluated on
`(P1,P2,P3,P4,P5,Q0,Q1,Q2,Q3,Q4)` give a ten-by-ten determinant

```
1583314678 (mod 2147483647), nonzero.
```

The entire matrix is retained, with rational coordinates of all five Q's.
A duplicate-row mutation gives determinant zero. Thus the ten polynomials
are independent in characteristic zero. Since the full finite determinant
ideal multiplicity is10 by accepted B16-04, they span it. Consequently
`[Q0],...,[Q4]` form a basis of the five-dimensional quotient by the
**full** `Jflag` image in this cell. In particular `Q0` is an explicit
nonzero quotient representative. The quotient assertion concerns kernel
position inside the ideal; it is not a padding coordinate-rank result.

## Provenance, resources, and limits

The acceptance chain is `Batch16/INTAKE.json`, slots04 and06, together with
the independent slot12 supplement
`Batch16/reviews/12_milestone/b16_12_receive04_05_06_08.md`, followed to
the original B15-04 and B15-06 proof/code/certificate files. The original
global Hessian source is the pinned
`Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631` packet.
Its then-provisional status language is superseded only to the extent
explicitly accepted in the later intake. The B13 LR implementation and
Claude Opus5 B14 bracket conventions retain their original attribution.

**Fresh:** the five-channel construction and raising proof; evaluation of
all five actual multiplication circuits; the matching rank-five minor;
the quotient basis and augmented minor; exact LR replay for this target;
42 inherited-formula comparisons; one duplicate-row control. All52
declared B16-04/06 artifact hashes were freshly checked and matched.

**Inherited:** the nonzero global LMR flag copy and harmonic projector;
the original Hessian identities and coefficient conventions; B16-04's
degree26 polynomiality and full ideal dimension10; its stable completeness
and compatible finite chart. The old full-space determinant and padding
rank calculations were not rerun. Fresh execution of their small evaluator
is identified as a control, not as an independent proof of those premises.

The one authorized scientific run used the existing `.venv/python.exe -B`
and inspected `analysis/b15_bound.py`, at60 seconds /512 MiB, one process
and one BLAS thread. It exited0 in **0.4007313 seconds**, with Job Object
peak committed memory **21,037,056 bytes**. The process exited; there was
no retry, second scientific run, heavy lease, background computation or
subprocess. The wrapper's inherited metadata labels say Batch15/B15-05;
the `b17_05_image` receipt name binds this B17-05 run. The pre-run estimate
and exact command are in [b17_05_preflight.md](b17_05_preflight.md).

Thirty inputs were hash-pinned before execution. The hashes, current
accepted-delivery checks, executable, arithmetic certificate, operation
receipt and resource record are bound in
[delivery/b17_05/MANIFEST.json](../delivery/b17_05/MANIFEST.json).
There were no automatic approval rejections. Read-only Git inspection
returned HEAD `5a019b2fb24fecf208118e628772b373235a6d61` and pre-existing
untracked B16 files; it warned that the user's Git ignore file was
inaccessible. No trust/configuration change was attempted. Writes are
confined to the assigned B17-05 paths. No commit, push or publication.

Let `R24` instead be the span of **all** ordinary degree24 9-minor
remainders with unrestricted binary planes, and `J24=(R24)`. We have not
computed `J24_26,lambda`, and do not assert any Q survives modulo it.
No claim is made about `J24:f^infinity` or `Jflag:f^infinity` for a chosen
chart denominator or discriminant f; such a saturation is a different
ideal and can change membership. The full degree27 `Jflag` image is also
uncomputed. Only the single degree26 target above was priced and run.

The inherited Batch17 finite screen gives in this cell
`a=428, i_det=10, m_det=418, m_pad<=288`, hence `D<=-130`.
This remains an excluded cell for a positive multiplicity gap. A source
ceiling is not a lower bound on actual padding, and our ambient minors
do not evaluate padding. Actual padding means independent `z*per3`,
embedded in16 variables, not `per4` or a generic cubic in ten variables.
Any positive certificate still requires one finite cell with a global
determinant coordinate upper B and actual padding coordinate lower r>B,
where `D=m_pad-m_det=i_det-i_pad`. No all-degree exclusion follows from
the present image result.

The LMR benchmark is a determinant **size** lower bound, not an equation
degree: [Theorem1.0.1](https://arxiv.org/pdf/1004.4802) proves border
determinantal complexity at least `m^2/2`. Nothing here improves that
growth or provides a new positive gap.

**One next sufficient test for the integrator:** in the same degree26
weight, compute the full unrestricted `R24 tensor A2` multiplication
image and decide whether adjoining the specified `Q0` increases its rank.
A complete image upper certificate matched by minors, plus an augmented
rank increase, would prove survival modulo `J24`; a polynomial identity
expressing Q0 in that image would prove membership. All nonflag channels
must be included. That larger source is not priced or launched here;
request a separate measured preflight and integrator resource review
before granting any larger lease. No extra lease is needed for the
completed five-channel result, and none is self-issued.
