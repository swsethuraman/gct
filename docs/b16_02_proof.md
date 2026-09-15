# B16-02: finite ambient census and exclusions

Characteristic zero; ordinary quartic coefficient convention. The ambient
multiplicity is `[S_lambda C^16] Sym^d(Sym^4 C^16)`. All four partitions have
ten rows, so specialization to ten variables preserves their multiplicities.
Independent padding always means the ten-variable polynomial `z*per3`, with
`z` independent of the nine matrix variables.

## Fresh finite-stability lemma

Let `tau` be a nonempty partition of size `n`, let
`lambda=(4d-n,tau)` be a partition, and suppose

    2d-n+2 > tau_1.                                      (1)

Then its finite quartic ambient multiplicity equals

    [s_tau] Sym(Sym^2 V' + Sym^3 V' + Sym^4 V').           (2)

Here `dim V' >= length(tau)`. This is a sufficient onset, not a claim of the
minimum onset of an arbitrary tail. The proof is an exact finite character
calculation and does not replace a finite count by a stable count without
establishing equality.

Write the ten-variable character using one variable `x0` and residual
variables `y`. A quartic coefficient monomial has tail degree `j=0,1,2,3,4`.
Let `G_(b,m)` be the residual character of the part of
`Sym(Sym^2 V' + Sym^3 V' + Sym^4 V')` having `b` factors and tail weight `m`.
It is Schur-positive, and nonzero only if `2b<=m<=4b`.

The coefficient of `x0^(4d-n)` in the finite ambient character is the sum
of `G_(b,m) h_L(y)` with `m+L=n` and `b+L<=d`. The missing factors are
filled uniquely by the weight-zero generator `x0^4`. To extract the full
highest-weight multiplicity, multiply by the positive-root denominator.
Its roots involving the first variable contribute

    product_i (1-y_i/x0) = sum_k (-1)^k e_k(y) x0^(-k).

The remaining root factors extract the coefficient of `s_tau` in the
residual symmetric character. Thus, for each `G_(b,m)`, put `L=n-m`,
`D=d-b`; the residual multiplier is

    H_(L,D) = sum_{0<=k<=L, L-k<=D} (-1)^k e_k h_(L-k).   (3)

Identity (1) implies `d>=floor(n/2)`, so every relevant `b<=floor(n/2)`
has `D>=0`. If `L=0`, (3) is 1. If `0<L<=D`, (3) is zero by `E(-u)H(u)=1`.
If `L>D>=0`, the Jacobi-Trudi hook identity gives

    H_(L,D) = (-1)^(L-D) s_(D+1,1^(L-D-1)).              (4)

The identity also holds in finitely many residual variables, where hooks
of excessive height vanish. Its sign is material: for `L=D+1`, it is
`-h_L`. Small exact controls verify every instance with `1<=L<=8`.

Only (4) could cause a finite correction. But `L>D` implies
`m-b<=n-d-1`, while `m>=2b`; hence `b<=n-d-1`. The hook's first row is

    D+1 = d-b+1 >= 2d-n+2 > tau_1.

Every Schur constituent of `G_(b,m) * s_hook` contains the hook diagram,
by the Littlewood-Richardson rule. None can be `tau`. Consequently all
finite corrections vanish, leaving only the terms `G_(b,n)` in (2).
This proves the lemma. No chart polynomial lift or geometric rank is
assumed in this character argument.

For `tau=(t,2^8)`, `n=t+16`, condition (1) holds for `d>=t+8`.
For the requested degrees 23,25,26,27 the minimum hook first rows are
17,19,21,21, respectively, exceeding the tail first rows 15,17,17,19.
The sizing certificate explicitly enumerates every possible correction
carrier `(b,m)`; each is excluded by this same first-row argument.

## Fresh arithmetic

For the symmetric-function series `F=sum_n F_n u^n` in (2),

    F_0=1,
    n F_n = sum_(m=1)^n L_m F_(n-m),
    L_m = sum_(j in {2,3,4}, j|m) sum_(rho partitions j)
          (j/z_rho) p_((m/j)rho).

This follows by differentiating the logarithm of the symmetric-algebra
character. The multiplicity is `sum_rho [p_rho]F_n * chi_tau(rho)`.
Coefficients are exact rationals, not multiplied by `z_rho`. The count
certificates retain every partition, numerator, denominator, character and
signed subtotal, not only a final integer. Fresh results:

| d | lambda | n | finite a = stable a | power-sum terms |
|---:|---|---:|---:|---:|
| 23 | (61,15,2^8) | 31 | 189 | 3522 |
| 25 | (67,17,2^8) | 33 | 294 | 5126 |
| 26 | (71,17,2^8) | 33 | 294 | 5126 |
| 27 | (73,19,2^8) | 35 | 429 | 7365 |

The producer adapts the attributed B14-04/B15-06 power-sum recurrence and
uses the preserved S30 beta-number Murnaghan-Nakayama character code.
Its controls compare 94 small finite cells against direct `h_d[h_4]`
and the first-row branching formula (3), and verify 36 identities (4).
The control `(d,lambda)=(2,(4,2,2))` has finite a=0 but stable a=1,
demonstrating that omission of the onset condition is detectable.

The standalone receiver regenerates the series with a different rational
backend, enumerates connected skew rim strips geometrically rather than
using beta-number moves, checks character dimensions/orthogonality,
validates complete partition support and all arithmetic, and rejects
missing/duplicate/altered certificate data. It uses the same underlying
exponential character identity, so this is independent implementation
and character enumeration, not a different mathematical count formula.

## Inherited premises and fresh finite consequences

The frozen B15-06 report/proof, accepted intake and Dream review supply:

* At ten rows and tail `(19,2^8)`, stable ambient 429 and genuine determinant
  evaluation rank at least 418. Thus the full stable ideal has dimension
  at most 11. Hessian11 supplies eleven independent global equations,
  proving equality. The native determinant minors were not rerun here.
* Multiplication by the nonzero highest-weight slice polynomial
  `s2^((19-t)/2)` injects the determinant ideal at tail `(t,2^8)` into that
  at tail `(19,2^8)` for `t=15,17`. This is an injection in a polynomial
  domain, not an addition of tensor multiplicities. Therefore the full
  stable determinant ideal is at most 11 for both lower tails as well.
* S57's chart identifies each finite ambient highest-weight space with a
  subspace `A_d` of the stable space `A_inf`, and the finite ideal with
  `A_d intersect K_X`. Thus finite ideal dimensions are at most the
  corresponding stable ideal dimension.
* The split-cubic product-map proof, accepted in Dream_Upper288, bounds
  the actual padding coordinate multiplicity by 158,218,218,288 in the
  four cells. The ceiling 218 at d26 follows by the same cubic chart and
  Pieri channel argument: `mu=(3d-14-b,b,2^7)`, `2<=b<=17`. These are
  source ceilings, not measured image ranks. No equality with a source
  multiplicity is inferred.
* The given determinant ideal floors are 1,2,2,5; multiplying the d25
  pair by the nonzero leading coefficient supplies the stated d26 pair.
  These floors alone do not imply the exclusions below.

Our fresh finite equality `dim A_d=dim A_inf` strengthens the filtration
statement to `A_d=A_inf` in every requested cell. Hence all its coordinate
and ideal multiplicities have reached their stable values. In particular,
the accepted tail-19 values apply already at degree27:

    i_det=11, m_det=418, 243<=m_pad<=288,
    141<=i_pad<=186, -175<=D<=-130.

This is a dimension/filtration consequence. It does not itself provide
explicit coefficient expansions of all eleven degree27 equations. The
four independent stable tail-17 equations in Hessian11 similarly imply
`i_det>=4` already at degrees25 and26; the requested floor2 remains listed
separately to preserve the supplied/fresh distinction.

## Exact exclusion arithmetic and rank thresholds

Put `h` equal to the accepted padding source ceiling. Since
`i_pad=a-m_pad>=a-h` and the full `i_det<=11`,

    D = m_pad-m_det = i_det-i_pad <= 11+h-a.

| d | a | given q | h | i_pad lower | full i_det upper | D upper |
|---:|---:|---:|---:|---:|---:|---:|
| 23 | 189 | 1 | 158 | 31 | 11 | -20 |
| 25 | 294 | 2 | 218 | 76 | 11 | -65 |
| 26 | 294 | 2 | 218 | 76 | 11 | -65 |
| 27 | 429 | 5 | 288 | 141 | 11 | -130 |

All four finite cells are excluded under the named accepted geometric and
padding premises. Failure of `q+r>a` alone is not the exclusion argument.

| d | padding rank needed with given q | needed even at q=11 | ideal q needed if r=h |
|---:|---:|---:|---:|
| 23 | 189 | 179 | 32 |
| 25 | 293 | 284 | 77 |
| 26 | 293 | 284 | 77 |
| 27 | 425 | 419 | 142 |

Each required padding rank exceeds the source ceiling, and each required
ideal dimension in the last column exceeds the full upper bound 11.
There is no sufficient positive witness consistent with these premises
in these cells. For a different cell, the sufficient witness remains a
global determinant ideal floor q and an actual independent-ten-variable
padding coordinate rank floor r with `q+r>a` in that same finite cell.
Earlier rungs outside the proved onset require their own finite counts
and padding/ideal comparisons; this census does not exclude them.
