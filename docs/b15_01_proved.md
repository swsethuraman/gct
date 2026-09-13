# B15-01 proof fragment

Model: gpt-6-astra. This is a per-slot record; it does not edit the shared
theorem index. Native S74 and B14-07 sources retain their original attribution.

## Independently recomputed dimensions

**EXACT.** For V of dimension at least 9, use the positive coefficient-weight
convention, n=4, degree 14 and lambda=(25,17,2,2,2,2,2,2,2). Then

    dim HW_lambda(Sym^14(Sym^4 V)) = 93,
    dim N14 = dim HW_lambda(Sym^14 V tensor Sym^14(Sym^3 V)) = 159.

The first calculation uses all 52,157 terms of the exact Newton expansion
h14[h4]. The second uses all 8,667 terms of h14[h3] and the complete 27
interlacing partitions mu with lambda/mu a horizontal 14-strip. Every channel
agrees with the B14-04 input. Rational Newton coefficients are cross-checked
by an independent modular recurrence at both house primes on the cubic side.
Outer-rim Murnaghan--Nakayama characters pass small hook and orthogonality
controls. These computations are independent of point evaluation ranks.

Verifier: `analysis/b15_01_members.py audit`, using the accepted
`tools/verify/ci73_dimension.py`. Evidence: `results/b15_01/dimension.json`
and `results/b15_01/ambient.json`. The definition of the normalization module
uses the same equivariant multiplication map and Pieri convention as CI73.

## Integral membership of the exported constructions

**EXACT.** A mixed filling with fourteen valence-one letters, fourteen
valence-three letters, two height-nine columns, fifteen height-two columns,
and eight singletons defines an integral highest-weight polynomial in N14.
Its defining formula is the initial-column Leibniz sum: assign all row
permutations to each ordered column, multiply their signs, and evaluate a
letter of row multiplicity alpha as alpha!*c_alpha of its form. Equal-type
letters use the same linear or cubic form. No orbit averaging is used.

Each initial-column determinant is invariant under the relevant upper
unipotent subgroup and has weight epsilon1+...+epsilon_h. Equivariant letter
evaluation therefore gives weight lambda and bidegree(14,14). This argument
establishes membership even when the resulting polynomial is zero.

The degree-13 constructions are multiplied by

    t(ell,c) = ell_0*m_(3,0^8)(c) = 6*ell_0*c_(3,0^8)(c) = u(ell*c)/4.

Appending a singleton linear letter and three singleton occurrences of a
cubic letter implements exactly this product. It changes bidegree by(1,1)
and weight by(4,0^8). The fraction in t=u/4 does not introduce a modular-only
source: the direct formula for t is integral.

Hybrid diagrams also permit valence-four letters evaluated on f=ell*c.
If q is the number of quartic letters, l the number of explicit linear
letters, and c the number of explicit cubic letters, the conditions
q+l=q+c=14 give the same bidegree (14,14). Equivariant multiplication and the
same initial-column alternation prove membership in N14. A compact hybrid
diagram can therefore represent a sum of many ordinary mixed diagrams.

For any ordered four slots, the exact factorial-symbol identity is

    m_(i1,i2,i3,i4)(ell*c)
      = sum_(s=1)^4 ell_(is) * m_(i1,...,omit is,...,i4)(c).

Here m indexed by slots means alpha!*c_alpha for the resulting multiplicity
vector alpha. There are alpha_i equal choices of a slot in row i, and
alpha_i*(alpha-e_i)! = alpha!, which proves the normalization. Replacing a
quartic letter by its cubic and linear pieces at one chosen slot preserves
the column shape. Each of the four diagrams is individually a genuine member;
their sum is the unsplit diagram. This permits use of the degree-13 completing
source15 without a full expansion of all its quartic letters.

Exchanging one occurrence of the added cubic singleton letter with an old
cubic occurrence preserves every letter's valence and all column heights.
The constructor rejects repeated labels within a column. Thus these
exchanges also give explicit genuine members. Their enumeration is a finite
construction family, not a spanning theorem for N14.

Each source pullback is separately defined by

    G_i(ell,c)=F_i^native(ell*c)*u(ell*c)^(14-rung_i),
    u(f)=24*c_(4,0^8)(f).

Equivariance of multiplication gives membership in N14. Native indexing,
including the first 39 coordinates, is unchanged. The polynomial uses the
first nine row coordinates, so an identity on all reducible nine-variable
forms extends to larger ambient spaces by restricting an arbitrary reducible
form to those coordinates. This is functorial extension of an equation; it
does not replace the independent padding variable by a nine-variable point.

## Stored exact source arithmetic and height

**EXACT for the stored matrix.** A14 has source rows and point columns.
Its recorded 88-minor is nonzero over Z. The five supplied integer columns K
have rank 5 and A14^T*K=0 on all 192 primary and 20 holdout columns. Altering one
kernel coefficient is detected. The three effective CI73 degree13 kernel
columns, extended by 54 zero rows, have rank 3 and their union with K has
rank 5. This checks coordinate compatibility; CI73 supplies their inherited
global vanishing.

For the given coefficient bounds, every quartic factorial symbol is at most
1176 in absolute value. Two height-nine columns and fifteen two-columns give
at most (9!)^2*2^15 summands. Each degree-14 source value is therefore bounded
by H=(9!)^2*2^15*1176^14. Both the seven-prime product and 2^256 exceed 2H.
`source_audit.json` records the integer bound, moduli, positive signed margins
and the 12 specifically identified fresh exact source evaluations. The other
stored identities are not described as fresh geometric replay.

## Partial interpolation and transport

Let E:N14->Q^s be evaluation at explicit rational points. A nonzero r-minor
of integral members proves rank(E)>=r over Q. Because dim N14=159,
dim ker(E)<=159-r. If five independent source polynomials give a rational
sampled kernel K, and their exact point identities are established, then

    dim ker(pullback) >= max(0,5-(159-r)).

This is rank-nullity for the pullback restricted to the five-dimensional
space spanned by those polynomials. It does not infer ideal membership from
modular zero evaluations. Rank 159 makes E injective and proves all five
identities globally. Rank 158 proves at least four independent equations;
smaller ranks do not improve the inherited floor 3 unless another argument
is supplied.

Multiplication by u^10 is injective in the ambient coefficient domain and
sends degree14 weight(25,17,2^7) to degree24 weight(65,17,2^7). The true
independently padded permanent z*per3 is reducible, so P is contained in R.
Thus k independent reducible equations transport to k independent padded
equations. This uses no assertion that the full padded and reducible ideals
are equal in degree14.

Inherited degree24 premises: a=274, m_det=273 and m_pad>=269, as scoped in
the accepted CI73 receipt and ACCEPTED_STATE.md. Hence i_pad<=5 and
D=m_pad-m_det=1-i_pad. With five transported equations D=-4; with four,
D<=-3. The inherited three equations alone gave D in [-4,-2]. To apply the
improved partial-interpolation bound, both the normalization minor and fresh
exact source identities must pass, together with source completeness.

## Verified degree-14 partial certificate

**EXACT over Q.** The shared verifier accepted
`results/b15_01/certificate.json` under the strict partial profile
`quartic_lmr_degree14_ci158`. Its freshly evaluated normalization minor has
rank 158, prime 2147483647 and determinant 823506578. The fresh
generic source minor has rank 93 and determinant 702376822
at the same prime. Together with independently recomputed dimensions
a14=93 and h14=159, this proves source completeness and that the evaluation
kernel in N14 has dimension at most one.

All 93-by-158 source entries were freshly reconstructed as signed integers
under the bound H above. The five supplied integer columns have rank five,
A^T*K=0 exactly and rank_Q(A)=88. Thus the five-dimensional source subspace
maps into a space of dimension at most one, proving

    4 <= i_red14 <= 5.

This proves existence of at least four independent global equations in the
five-dimensional supplied subspace. It does not identify an explicit fourth
coefficient vector or assert that either remaining supplied column vanishes
individually. All genuine members used for the minor have complete integral
definitions and explicit compatible evaluation points in the certificate.

The native-degree evaluator followed by exact multiplication by u gives the
same source polynomial as the lifted filling. Full-subset contraction order
optimization for 14 quartic letters affects cost only; the accepted signed
Leibniz backend and factorial-symbol construction are unchanged. Integer,
modular and old/new-order controls checked this transport in 68 entries.
All first 93 literal degree-24 definitions also match multiplication by
u^10; extending a relation to that source adds 181 zero rows.

With the explicitly inherited degree-24 premises in the preceding section,
injective transport and P contained in R give

    4 <= i_pad24 <= 5,    D_LMR in [-4,-3].

The full rank-159 interpolation claim and D_LMR=-4 remain open. Evidence:
`shared_verifier_report.md`, `verification.json`, `fresh_target_minor.json`,
`generic_source_minor.json.gz`, `fresh_source_values.json.gz`,
`kernel_comparison.json` and the nine rejected altered-input cases in
`shared_verifier_controls.json`, all under `results/b15_01/`. The report
includes the exact replay command and separates inherited premises from
freshly checked arithmetic.
