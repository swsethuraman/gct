# Exact padding-factor fibers and an actual-padding control

UNCOMMITTED / NOT RELEASED. PROVED by hand, producer-only, except the explicitly named optional C_PER transfer. This file works with genuine padding l per3(A) whenever it states actual-padding membership.

## 1. Complete fixed-factor kernel formula

Let l=sum a_i x_i be nonzero, and put r=#{i<=m:a_i!=0}. On all cubics consider C -> pi_m(l C). Then

    ker(C -> pi_m(l C))
      = span{degree-three monomials independent of every selected xi with ai!=0,
             and of degree at most one in every selected xi with ai=0}.

There is no degree restriction beyond total degree three on unselected variables. Its dimension is

    k(m,r)=[t^3] (1+t)^(m-r)/(1-t)^(5-m).

**Proof.** In the polynomial domain in xi over the other variables, deg_i(l C)=deg_i(l)+deg_i(C) for C nonzero. Membership in K_m means deg_i(l C)<=1 for each i<=m. If ai!=0 this forces deg_i(C)=0; if ai=0 it forces deg_i(C)<=1. These conditions are also sufficient, and the generating function counts their monomial basis. Multiplication by nonzero l is injective. QED.

For a fixed l with all selected ai nonzero, the kernel consists exactly of cubics in the 5-m unselected variables. Its dimensions are 4,1,0 for m=3,4,5. Thus the fixed-factor linear images have dimensions 31,34,35. For five centers, the stronger statement is

    k(5,r)=binom(5-r,3),

so any l supported on at least three coordinates has **zero** fixed-factor kernel. This support condition is equivalent to l(v_i) being nonzero at at least three of the five fixed independent centers.

**Consequence, PROVED.** If m=5, l has at least three nonzero coordinates, and a completion of pi_5(l C) is still divisible by l, it must equal l C itself. In particular a construction restricted to det diag(l,M3(x)) succeeds exactly when C already has a 3-by-3 linear determinantal representation. This does not prohibit an irreducible completion, a completion with a different linear factor, or a closure point of the determinant projection. No general containment verdict follows.

## 2. Explicit recovery of C when all ai are nonzero

Write C=sum d_beta x^beta and F=l C. All right-hand coefficients below are retained at five centers:

    d_(3ei) = c_(4ei)/ai,
    d_(2ei+ej) = (c_(3ei+ej)-aj d_(3ei))/ai,
    d_(ei+ej+ek) = (c_(2ei+ej+ek)
                    -aj d_(2ei+ek)-ak d_(2ei+ej))/ai,

with distinct i,j,k in the last line. These recover the five cubes, twenty square-times-linear coefficients, and ten squarefree cubic coefficients. Redundant choices of i in the last line yield compatibility conditions on the data; they are padding conditions, not determinant equations. No unknown squarefree quartic coefficient was used.

On the open set where the five pure-power coefficients are nonzero, a possible l can be normalized by a1=1. Each a_j, j=2,...,5, must make the binary form F(x1,xj) divisible by x1+a_j xj. All five coefficients of each binary restriction are retained. Each equation F(-a_j,1)=0 has degree four and nonzero leading coefficient, so there are at most four possibilities per j. Thus the five-center projection of the full product locus has at most 4^4=256 distinct form completions on this open set: for each possible l the preceding formulas determine C uniquely. This is a finite upper bound, not a claim of generic injectivity or of determinant membership. The open set is nonempty even on actual padding, e.g. l=sum xi and C=l^3, realized by a diagonal permanent matrix.

## 3. Dimension of the projected full product locus

For m=3,4,5 put k=4,1,0 respectively. **PROVED:**

    dim closure(pi_m(R))=39-k=35,38,39.

Upper bound: on the dense open set a1...am!=0, scale l so a1=1, leaving four parameters. Subtract from C its pure-unselected cubic part, which belongs to the fixed-factor kernel. The resulting dense image uses 4+(35-k) parameters. Density of this source open set and polynomial continuity cover its image closure; special factors cannot enlarge the total image dimension.

Lower bound: take l=x1+...+x5 and C=x1^3. A tangent variation is l deltaC+x1^3 deltal. Suppose its projection is zero and call this quartic q in K_m. Reduce modulo l by eliminating x2 (available because m>=3). Every monomial of q has degree at most one in both x1 and x2; substitution therefore gives a polynomial of degree at most two in x1. But x1^3 deltal modulo l has degree at least three in x1 unless deltal modulo l is zero. Hence deltal=b l and q=l R, where R is in the k-dimensional cubic kernel of section 1. Necessarily deltaC=R-b x1^3. The differential kernel has dimension exactly k+1 inside the forty-dimensional (l,C) parameter space. Its rank is 39-k.

A nonzero rank-(39-k) minor gives (39-k) algebraically independent output coordinates by the lowest-homogeneous-term argument used in PRIOR_CHECKS.md. Combined with the upper bound this proves the dimension exactly. This hand proof computes a linear kernel symbolically; no program or numerical rank was run.

The tangent calculation uses arbitrary cubic variations. It is **not** a full-rank certificate for the actual permanent parametrization at C=x1^3. For actual padding it gives only an upper bound until the separate cubic-permanent dominance premise C_PER is used. Modulo C_PER, P=R and these three dimensions are exact for actual-padding closures as well.

## 4. Exact containment for a genuine actual-padding family

Take arbitrary linear forms a,b,c. Set z=x1, d=x2, e=x3, f=x4, and form the symmetric permanent matrix

    A=[a d e; d b f; e f c].

Direct six-term expansion gives

    per3(A)=abc+a f^2+b e^2+c d^2+2def.

The integer-sign matrix

    H=[a d e; -d b f; -e -f c]

has determinant abc+a f^2+b e^2+c d^2: the two cubic cycle terms cancel. Therefore the actual determinant pencil diag(z,H) satisfies

    z per3(A)-det diag(z,H)=2 x1 x2 x3 x4 in K_5.

This proves exact equality of their retained data for m=3,4,5 in the canonical frame. The same holds under simultaneous GL5 transport of centers and forms, and under the analogous assignment to any four distinct coordinate variables. Diagonal entries a,b,c remain arbitrary. This is a proper specified subfamily, not all padding.

In particular use the actual integer T from A25-04:

    z=x1, a=x1+x5, b=x1-x5, c=x1,
    y12=y21=x2, y13=y31=x3, y23=y32=x4.

Its permanent padding is

    F_T=x1^4+x1^2(x2^2+x3^2+x4^2-x5^2)
        +x1 x5(x4^2-x3^2)+2x1x2x3x4.

An explicit integer determinant completion is

    det [x1       0          0       0
          0   x1+x5         x2      x3
          0      -x2     x1-x5      x4
          0      -x3        -x4     x1]
      =F_T-2x1x2x3x4.

Every determinant equation in the maximal five-center ring vanishes at this actual T. This is a genuine new exact control, stronger than checking a few candidate equations. It cannot witness separation in this ring in any degree. The factor l=x1 has r=1, with four invisible cubic directions by section 1, so there is no conflict with generic fixed-factor rigidity.
