# B15-05 proof fragment: stable ideal bound and finite transport

Model: gpt-6-astra, xhigh. This per-slot fragment leaves shared records untouched.

## Claim 1: sufficient determinant threshold

**Status: EXACT conditional implication.** Let n=4 and let
lambda(d)=(4d-35,21,2,2,2,2,2,2,2), d>=15. In the polynomial-coordinate
convention C[Sym^4 V*]=Sym(Sym^4 V), write a(d) for ambient multiplicity,
i_X(d) for ideal multiplicity and m_X(d)=a(d)-i_X(d) for coordinate
multiplicity. X is the determinant or independently padded permanent orbit
closure; statements here concern closures, not orbit normalization rings.

Assume the inherited stable ambient dimension a_inf=533 at tail
(21,2^7), Proposition S's injection of finite highest-weight ideals into
the stable ideal, and the three accepted degree-13 padded equations at
(21,17,2^7). If a rationally valid stable determinant evaluation matrix
has rank at least r, then for every d>=15,

    i_det(d) <= 533-r,   i_pad(d) >= 3,   D(d) <= 530-r.

Thus r>=530 excludes positive D throughout this family.

**Proof of the ideal upper bound.** Put V'=C^8 and
Z=Sym^2 V'* + Sym^3 V'* + Sym^4 V'*. Proposition S identifies the stable
determinant locus with the closure of characteristic coefficients
(e2,e3,e4) of traceless 4x4 pencils in eight variables. The highest-weight
ambient space of tail (21,2^7) has dimension 533. Evaluation rank r on
points of this locus bounds the dimension of its vanishing subspace by
533-r. Every finite ideal vector maps injectively to that subspace:
restrict to c0=1, then use the depression slice that removes the cubic
coefficient of s0. On c0!=0, homogeneity recovers the original polynomial
from this restriction. Thus a zero restriction implies the polynomial
vanishes on a dense open subset of the ambient vector space and is zero.
The highest-weight root invariance permits the depression slice, and
determinant points depress to traceless-pencil points. Ideal membership
is preserved. This argument requires no equality a(d)=a_inf.

**Proof of the padded lower bound.** Use ordinary binary quartic
coefficients cj=[s0^(4-j)*s1^j]F. The nonzero polynomial

    q44 = 12*c0*c4 - 3*c1*c3 + c2^2

has degree 2 and weight (4,4). The raising operator E01 acts by
E01(cj)=(5-j)*c(j-1), so

    E01(q44) = 12*c0*c3 - 12*c0*c3 - 6*c1*c2 + 6*c1*c2 = 0.

All other raising operators vanish because these monomials involve only
the first two variables. For each of the three inherited equations Fi,
q44*Fi is a padded equation of degree 15 and weight (25,21,2^7).
Multiplication by the nonzero polynomial q44 is injective in the ambient
polynomial ring, so all three remain independent. Multiplication by
u^(d-15), where u=24*c0, preserves their independence, ideal membership
and highest-weight property and gives lambda(d). This uses ideal
multiplication in a domain; no regularity assertion in a quotient is
needed. Since D=i_det-i_pad, the displayed bound follows.

**Verifier.** `analysis/b15_05_tail21.py controls` checks q44's raising
derivative and an altered coefficient over Q. `transport` separately
checks degrees, partitions and the scoped ledger at d=15,16,24,25,26,35,100.
The algebra above proves the statement for every integer d>=15; those
finite checks alone are not an all-degree proof.

**Inherited dependencies.** B14-04 stable multiplicity; S57 Proposition S;
B14-05 transport lemma; B14-08 witness w_2_4_4; accepted CI73 three global
degree-13 reducible equations. A reducible equation vanishes on
independently padded forms z*per3 because each is reducible. No equality
of padded and reducible coordinate multiplicities is assumed at degree 15
or above. The original ambient has 16 variables; the nine-row computation
uses the standard length-nine restriction convention of these references.

## Claim 2: finite degree 26 does not use stable coordinate ranks

**Status: EXACT implication with inherited a(26)=531.** At degree 26,
the partition is (69,21,2^7). With a padded ideal floor of 3,

    U_pad = min(a, h_pad, a-L_pad, other valid upper bounds)
          <= 531-3 = 528.

Here h_pad is the pullback-space dimension; no numerical h_pad bound is
asserted. If stable r>=530, Claim 1 gives i_det(26)<=3 and hence
m_det(26)>=531-3=528, enough for exclusion. It does not claim a finite
coordinate rank of 530. If r is smaller, Claim 1 gives only D<=530-r;
a positive upper bound is not a positive gap.

**Verifier.** `transport` stores the finite arithmetic separately from
the stable evaluation. Dependencies are as in Claim 1 and the inherited
degree-26 ambient multiplicity 531.

## Claim 3: modular minor interpretation

**Status: EXACT conditional implication.** Every exported nonzero minor
from the evaluator is a rational rank floor if its source and point
definitions, symmetry, Euler identities and geometric replay all pass.

The sources are the B14-06 double-epsilon contractions with nineteen
singleton slots. Each symmetric tensor places at most one slot in either
epsilon. Each source is a highest-weight polynomial of tail (21,2^7).
The ordered (a,b,c,z) list, factorials c2!c3!c4!, and sign (-1)^sum(a)
are retained. Interpolation recovers the homogeneous coefficient of a
determinant polynomial of degree at most eight; its Vandermonde inverse
only computes that coefficient and does not change the source.

For determinant points the eight matrices Ak are explicit integral
traceless matrices and F=det(s0*I4+sum xk*Ak). Hence c0=1 and the
depressed coefficients are e2,e3,e4. Dividing derivatives by d and
d(d-1) converts ordinary coefficients to symmetric tensors. These
denominators are units at both house primes, so each matrix is the
reduction of a single rational evaluation matrix. A nonzero minor modulo
either prime is nonzero over Q. No integer uniqueness or CRT claim is
made. Bracket spanning is unnecessary for a floor; the inherited exact
ambient dimension supplies the upper dimension in Claim 1.

For generic controls the saved symmetric matrices Nij define actual
homogeneous forms

    f_d = N00*x0^d + d*sum(i>0) N0i*x0^(d-1)*xi
          + binom(d,2)*sum(i,j>0) Nij*x0^(d-2)*xi*xj.

This gives u=N[:,0] and s=N[0,0] exactly. Generic control data therefore
lie in Z. The rank guard rejects any value above 533.

**Verifier.** `controls` includes independent known liveness at tail
(2^8), direct epsilon contraction in dimension 3, altered factorial/sign
and inconsistent-jet checks, and shifted DETQ jet agreement. `defect`
returns nonzero on an intentionally altered stored value. `replay`
regenerates all selected minor values from the explicit point files using
a different interpolation seed and compares entries and determinants.
The inherited mathematical source construction is B14-06; new code
orchestration is not an independent reimplementation of its evaluator.

## Claim 4: completed rank floor and its finite consequence

**Status: REPLAYED_RANK_FLOOR.** The pilot produced nonzero determinant
minors of size 529 at primes 2147483647 and 2147483629. Their determinants
are respectively 1967323645 and 262406295. Generic minors of size 533
have determinants 1828515817 and 1852112970. All four minors were
regenerated from the explicit geometric points with a changed
interpolation seed, checking 1,127,860 entries and all four determinants.

By Claim 3 these give m_det_inf>=529 and a_inf>=533 over Q. With the
inherited exact a_inf=533, i_det_inf<=4. Claim 1 then gives
i_det(d)<=4 and D(d)<=1 for every d>=15. The sufficient threshold 530
was not attained. At d=26, m_det>=527 and m_pad<=528 use a(26)=531.

**Verifier and artifacts.** `analysis/b15_05_tail21.py replay`;
results/b15_05/replay.json, pilot.json, the four actual minor NPZ files,
their certificate JSON row/column indices, det_points.npz, gen_points.npz
and source.json. The generic pivot columns form the ambient basis for
the four modular sampled kernel candidates at each prime. Their
sampled vanishing is freshly checked; global ideal membership is
**CANDIDATE**, not a proved equation. No positive gap or exclusion follows.

**Dependencies.** Claims 1 and 3, with their inherited premises; the new
minor replay is fresh. The research stopped at the preregistered fixed
sample cap, with no resource limit or extension. The next sufficient
witness is a 530-dimensional determinant floor or a fourth independent
global padded direction at degree 15 that persists along this family.
