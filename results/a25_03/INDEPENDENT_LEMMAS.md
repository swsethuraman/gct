# Independently checked elementary inputs

UNCOMMITTED / NOT RELEASED. PROVED by hand here, producer-only. A25-01/02 are provisional uncommitted inputs, not independently accepted packets. Their current manifest entries were verified before their use as bound research inputs. The present main theorem has its own proof and requires no conditional result from either packet.

## 1. Verification of the A25-01 single-frame argument

In a single frame write a=[x1^4]F, p_i=[x1^3 y_i]F and q_ij=[x1^2 yi yj]F. Let

    u=(E12,E13,E14,E23),   v_i=u_i^T.

The identity E_ab E_cd=delta_(bc) E_ad shows tr(u_i u_j)=tr(v_i v_j)=0 and tr(u_i v_j)=delta_(ij). Thus for any symmetric G, the traceless matrices

    D_i=u_i+(1/2) sum_j G_ij v_j

satisfy tr(D_i D_j)=G_ij: the two mixed terms each contribute one half, and the two same-type terms vanish. This construction is rational and works also for degenerate G.

For a!=0 put r_i=p_i/a and

    G_ii=3 r_i^2/4-2 q_ii/a,
    G_ij=3 r_i r_j/4-q_ij/a (i<j),
    C_i=(r_i/4) I4+D_i.

The permutation expansion gives the second-degree term of det(x1 I4+Y) as

    (x1^2/2)((tr Y)^2-tr(Y^2)).

Consequently tr C_i=r_i and tr(C_i C_j)=r_i r_j/4+G_ij yield square coefficient q_ii/a and mixed coefficient q_ij/a. Let P_a=diag(a,1,1,1), B1=P_a and B_(i+1)=P_a C_i. Multiplicativity gives the desired coefficients (a,p,q) in det(sum x_i B_i). All formulas are regular over Q[a,a^-1,p,q].

A relation pulling back to zero would therefore map to zero under the injective localization Q[a,p,q] -> Q[a,a^-1,p,q], and must itself be zero. This verifies A25-01's all-degree, single-frame result independently. It also covers pairs with proportional center lines, whose actual joint space is just this 15-dimensional space by FRAMES.md. It was not used to infer the distinct-center result.

## 2. Coefficient equations and closure

A polynomial h lies in ker phi* exactly when h(phi(B))=0 for every pencil B: this is the definition of pullback. Polynomial zero sets are Zariski closed, so this is equivalent to h vanishing on the closure of the determinant image. No parameter necessity, source test or fibre-constant function is substituted for h. The polynomial ring on independent joint coordinates injects into the full ring on the 70 quartic coefficients because the linear coefficient projection from W is surjective.

## 3. Why mixing padding-blind generators cannot help

Define actual padding precisely as P_T=(z per3) composed with T, T:V -> C^10 linear, and let P be the affine Zariski closure of this image. For any A in GL(V), P_T(Ax)=P_(T A)(x), so P is GL(V)-stable without assuming an identification with all products lC.

If g_i vanish on P, every finite sum sum_i a_i g_i with polynomial a_i vanishes on P. Every GL(V) translate also vanishes by stability; the same applies to ideal combinations of these translates. This independently verifies the A25-02 elementary closure implication. It says nothing about mixing arbitrary jet coordinates, which are not assumed padding-blind. The distinct-frame no-go follows from the differential proof, not from this ideal observation or the single-frame theorem.
