# The certificate domains and their dimensions

All new derivations below are labelled **HAND**. **READ** references name the exact committed source through INPUT_BINDINGS.json. **COMPUTED** statements name a shipped finite certificate. No external PRIMARY source is claimed.

## 1. Closed known-in region and the partition

**HAND definitions:** E=C^50, A in C^45, l in C^5, Phi(A)=per_3(A), F(l,A)=l Phi(A). Put K=D35 union Sigma_Pi, where D35 is the cubic determinant closure and Sigma_Pi is the locus of cubics containing a plane, including zero. Sigma_Pi is closed: its projectivization is the proper image of the incidence over Gr(3,5). D35 is closed by definition. Both are cones.

**READ:** B23-03 Theorem 2.1, §§2.4–2.6, and B23-10 §§3.0,3.4 give

    H := {lC : C in K} = closure(D45_literal intersect {lC}) subset D45.

**HAND:** H is closed as an affine cone: projective multiplication on P^4 x P(K) is proper. If F=lC!=0 has another linear-factor presentation l'C' with l' not proportional to l, then l' divides C. Therefore C contains a hyperplane, hence a plane, so C belongs to K. Consequently F=lC belongs to H iff C belongs to K, for every nonzero l. This verifies that the criterion is independent of which linear factor an input T designates as padding.

**READ + HAND:** K consists of singular cubics. The generic cubic determinant has six distinct singular points, as in the committed cap note; the discriminant is closed, so all of D35 is singular. For C containing the plane Pi=V(a,b), write C=a Q1+b Q2. The two quadrics restrict to Pi=P^2 and have a nonempty common zero locus there; at every such point all partials of C vanish. Thus Sigma_Pi is singular too.

**HAND:** define

    I   = {l=0} union {Phi(A) in K},
    II  = {l!=0, Phi(A) smooth},
    III = {l!=0, Phi(A) singular, Phi(A) notin K}.

They are disjoint and exhaustive. **READ:** I is contained in F^-1(D45); II is disjoint from it by accepted C1. **READ + HAND:** III has no literal determinant points by the B23-03 case analysis. Any membership in D45 there must be through a coefficient limit leaving the product locus before taking the limit. Neither commuting intersection with closure nor a finite matrix specialization is permissible. This is the remaining unknown, not an asserted theorem that III is disjoint from D45.

## 2. Dimensions of I and II

**HAND:** I is closed. The explicit identity

    per[[a,b,c],[d,e,f],[g,h,0]]
      = det[[-a,b,c],[d,-e,f],[g,h,0]]
      = afh+bfg+cdh+ceg

places the full A33=0 subspace into I. This subspace has eight freely chosen five-variable forms and an arbitrary padding form, dimension 45. Its nonzero-output and rank-five-T conditions hold on a nonempty open subset, so the same lower bound remains valid with those restrictions. The l=0 subspace independently has dimension 45. The symmetric-A subspace has dimension 35 and its literal lift is READ from A26-01.

**COMPUTED:** the B17 replay certifies one smooth Phi(A*). **HAND:** the discriminant pullback is consequently a nonzero polynomial in A. Its zero locus is a proper hypersurface in C^45, of dimension 44 (it is nonempty, for example at A=0). II is a nonempty open subset of E and has dimension 50. The complement of II is the union of this dimension-44 locus times C^5 with {l=0}, hence has dimension 49. Thus dim I is between 45 and 49, and dim III is at most 49.

## 3. A fixed one-node permanental cubic

**HAND construction:** take the ambient permanent point

    q = [[1,2,3],[4,5,6],[91,104,-333]].

Its permanent is `13*(-333)+1*6*104+2*6*91+3*4*104+3*5*91=0`. The nine permanent cofactors, in row-major order, are

    g=(-1041,-786,871,-354,-60,286,27,18,13).

In particular q is a smooth point of the ambient permanent hypersurface. For r=1,2,3,4 let V_r have first eight row-major entries `13*r^i`, i=0,...,7, and ninth entry `-sum_(i=0..7) g_i*r^i`. Then g dot V_r=0. Define

    A^dagger(x)=x0*q+x1*V_1+x2*V_2+x3*V_3+x4*V_4,
    C^dagger=per_3(A^dagger(x)).

This construction is fixed before its run, without a parameter sweep. It makes [1:0:0:0:0] a singular point of the restriction. It does not assume that this is the only singularity; that is checked next.

**COMPUTED, run 3:** TANGENT_CERTIFICATE.json records all five matrices, all 35 cubic coefficients and the following results:

* Every row of the degree-six gradient-ideal matrix has zero x0^6 coefficient.
* After deleting that column, a specified 209-square minor has nonzero integer determinant, residue 54422 mod 65521.
* The four-by-four Hessian of C^dagger(1,x1,...,x4) at the origin has determinant -863583313736999047506762240.
* A specified 35-square minor in the full 45-by-35 parameter differential is nonzero over Z, residue 5949 mod 65521.

**HAND:** rank 209 and the zero x0^6 column imply that the degree-six gradient ideal is exactly the span of all degree-six monomials except x0^6. In particular it contains x1^6,...,x4^6. Its common projective zero set is therefore just [1:0:0:0:0]. The nonzero Hessian makes that point an ordinary node. A reducible cubic in P^4 has factors of positive degrees whose intersection has dimension at least two and is singular along that intersection. Hence this one-node cubic is irreducible.

## 4. Why the one-node cubic is outside K

**READ:** the generic cubic determinant has six distinct singular points (cap note §§0–2.2, n=3). **HAND:** at six distinct projective points, degree-six forms have at least six independent evaluation functionals. To separate one of the points from the other five, multiply five linear forms, one vanishing at each other point and nonvanishing at the selected point; multiply by a further linear form nonzero there. Therefore the degree-six gradient matrix has rank at most 210-6=204 at a generic cubic determinant. Rank at most 204 is closed in coefficient space, so it holds throughout D35. The computed rank 209 excludes C^dagger from D35. This uses the committed generic-six-point statement; no assertion about six reduced nodes at every boundary point is needed.

**HAND, plane-family exclusion:** fix a plane Pi=V(a,b). A general pair of restricted quadrics Q1|Pi,Q2|Pi has four distinct common points. Nonemptiness of that open condition is explicit: in plane coordinates (u,v,w), use u^2-w^2 and v^2-w^2. The four points are (u:v:w)=(+/-1:+/-1:1). For C=a Q1+b Q2, those four points are singular. Degree-six evaluation at four distinct points has rank four by the same product-of-linear-forms argument. Thus rank of the degree-six gradient matrix is at most 206 on a dense subset of the linear space (a,b)_3. Closedness extends this bound to every such cubic, and change of variables extends it to all of Sigma_Pi. Again rank 209 excludes C^dagger. This argument avoids assuming that a special plane section has four distinct points.

**HAND conclusion:** C^dagger lies in the singular locus of coefficient space minus K. Taking l=x0 gives a point of III. Its T has rank five: if the entries of A spanned at most four variable directions, choose an unused fifth variable y. Every parameter derivative of per_3(A) would be a quadratic in the four used variables times one linear form. Its coefficient differential would have rank at most `dim Sym^3(C^4)+dim Sym^2(C^4)=20+10=30`, contradicting the computed rank 35. No D45-closure verdict is inferred for x0*C^dagger.

## 5. The dimension-49 lower bound

**HAND:** let Delta be the discriminant locus of singular cubics in C^35. It is a hypersurface smooth at a cubic with exactly one ordinary node. Here is the local argument used, rather than a genericity assertion: dehomogenize at the node. The four equations for a critical point have invertible derivative in the four spatial coordinates, namely the nondegenerate Hessian. Thus the critical point is locally a unique algebraic/analytic function of the coefficients. Singularity is the one further equation that the value of the cubic at that critical point is zero. Its derivative in the constant coefficient of the dehomogenized cubic (the x0^3 coefficient) is 1. Projectivity of the singular-point incidence and uniqueness of the node exclude additional branches coming from other projective points. Consequently Delta is locally smooth of codimension one.

**COMPUTED:** dPhi at A^dagger has rank 35. **HAND:** Phi is therefore a submersion there, and Phi^-1(Delta) is locally smooth of dimension 45-1=44. Since K is closed and C^dagger is outside it, removing Phi^-1(K) leaves a nonempty open part of this dimension-44 locus. Nonzero l varies in a five-dimensional open set. This produces dimension 49 inside III. Together with §2's upper bound, dim III=49. The rank-five frame condition is open and contains the constructed point, so it does not change this lower bound.

**HAND scope:** this is the dimension of a *not-yet-classified-in-the-closure* set, whose literal nonmembership is known. It proves neither that the whole set is outside D45 nor that a single point of it is a new boundary determinant. The certified-out set in this packet remains the smooth class II.

## 6. The expander padding point has a closure certificate

**READ:** B26-02 uses `p4=zw Q`, `Q=zw+uv+t^2`, and compares it to the different determinant `(zw+(uv+t^2)/2)^2`. Its classification only excludes a literal symmetric permanent and a smooth cubic; it does not decide D45 membership. **READ:** B23-03 already places p4 in T2 because wQ contains a hyperplane. The following independent HAND certificate is useful because it displays the limit explicitly.

**HAND:** for a nonzero scalar s put

    w_s = w+s^2 z,
    r_s = (s^2 z-w)/(2s),

    N_s = [ w_s/(4s^2)     u        t-r_s
                    -v    w_s          0
              -(t+r_s)      0        w_s ].

Expanding the first row gives

    det N_s = w_s [ w_s^2/(4s^2) + uv + t^2-r_s^2 ]
            = w_s [zw+uv+t^2] = w_s Q,

since `w_s^2/(4s^2)-r_s^2=zw`. Thus `det diag(z,N_s)=z(w+s^2 z)Q`. These determinant coefficients are polynomial in s and tend to zwQ at s=0, although the entries of N_s have poles. This is a valid coefficient-closure certificate. It does not claim finite matrix specialization at s=0 or literal representability of p4.

**HAND extension:** every product l*w*Q of two linear forms and a quadric in five variables is in D45 in closure. One direct argument, independent of the plane-family certificate, is that on the dense open set where Q has rank five and the covector w has nonzero dual norm, completing the square and splitting the remaining four-dimensional quadratic form into two hyperbolic planes gives `Q=k*w^2+a*c+b*d`. Then

    det [[k*w,a,b],[-c,w,0],[-d,0,w]] = w Q.

Multiplying by l gives a literal 4x4 determinant on this dense open set of (l,w,Q). The inverse image of closed D45 under (l,w,Q)->lwQ is closed, so it contains every specialization. Over C the quadratic-form decomposition is elementary linear algebra; no rational decomposition is promised for every rational input. The explicit p4 limit above uses only rational Laurent functions.

## 7. The retained failed example

**COMPUTED:** run 2 tested exactly the input NODAL_INPUT.json and returned rank 203 modulo 65521, not the proposed 209. The script stops at that negative result and never substitutes another point internally. It supplies neither a unique-node certificate nor a characteristic-zero rank equality. **HAND:** its A33=0 condition triggers §2's determinant identity, so it belongs to I and cannot certify a point in III. The negative is retained because hiding it would misrepresent the compute history. Run 3's input is a separately specified tangent construction with no identically zero entry; its positive conclusions rest on complete nonzero integer minors, not on the failure of run 2.
