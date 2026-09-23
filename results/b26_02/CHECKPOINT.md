# B26-02 first certificate (checkpoint)

**REVIEWER ONLY / UNCOMMITTED.** Written 2026-09-22T23:47Z, about 6 minutes after the recorded
start (23:41:26Z). That is well before the 30-minute checkpoint. All checks are hand derivations
or READs of committed bytes. Zero programs and zero pilots.

Inputs are the committed blobs at `0d6f5a8cc206e8703e3ebd9c0c45acb88adea0eb`, notes 1, 2 and 3. Each is
LF-only, so its blob equals its raw bytes. The hashes match the brief.

| # | note §  | exact statement | check | verdict |
|---|---|---|---|---|
| 1a | N1 §5 | subdivided filling: d=10k labels, each in 2+2 star columns and n-4 singletons, so content d x n | hand derivation | CONFIRMED |
| 1b | N1 §5 | columns 4k (height 5), 10k (height 2), 10k(n-4) (height 1), so lambda=((10n-26)k,14k,4k,4k,4k), with lambda_1>=lambda_2 iff n>=4 and total 10nk | hand derivation | CONFIRMED |
| 1c | N1 §2 | f_T is a weight-lambda highest-weight function when nonzero; semistandardness is not used | hand derivation (top-minor invariance under unitriangular maps, torus weight = #columns of height >= i) | CONFIRMED |
| 2a | N1 §2, N2 §3 | the power-sum formula equals the multilinear contraction of the symmetric tensor, q(x)=sum q_ijkl x_i x_j x_k x_l, so q_1122=c/6 | hand derivation (l^4 <-> l^{(x)4}) | CONFIRMED. The convention is forced by the formula itself, so BDI's own tensor conventions are not load-bearing. |
| 2b | N3 §3, N2 §6 | singleton legs contract to e1: C_n(q)=(4!/n!) d_{x1}^{n-4} q, and f_{H,n}=f_{H,4} o C_n | hand derivation (d^m l^n = n!/4! l_1^m l^4) | CONFIRMED |
| 3 | N2 §2 | M^{-1}=-I+J/2; a^T M b=a^T c=Q; per_3(Y)=w a^T M b=wQ; z^{n-3} wQ=p_n | hand derivation | CONFIRMED. This is a literal point of the r=5 restriction image of x_0^{n-3} per_3 (B25-04 notation, READ), with no product-locus or universality premise. |
| 4a | N2 §3 | M0=diag(a0 I2,c0 I3), M1=diag(b0 diag(1,-1),0), M2=diag(b0 sx,0); a0=4a/(3 rt2), b0=2a/(3 rt2), c0=b/(3 rt2) | hand coefficient extraction | CONFIRMED |
| 4b | N2 §4 | edge metric K=diag(1,-1,-1) | hand derivation (e X e^T swaps the diagonal and negates the off-diagonal) | CONFIRMED |
| 4c | N2 §4 | the generating polynomial is 5! det(sum y_r M_r)=120 c0^3 y0^3 [a0^2 y0^2 - b0^2(y1^2+y2^2)]; R0=160a^2b^3/(81 rt2); R1/R0=-1/40 | hand derivation (R is symmetric in its slots, so it equals the coefficient divided by binom(5,2)) | CONFIRMED |
| 4d | N2 §5 | surviving colourings are vertex-disjoint cycle unions, 2 colours per cycle, weight 40^{-|E(F)|}; f_{H,4}(aA^2+bAB)=R0^{2k} Z_H, with R0^2=(12800/6561)a^4b^6 | hand derivation (|V(F)|=|E(F)|) | CONFIRMED |
| 4e | N2 §6 | q_n weights 0,2,4 under z->tz, w->w/t; the weight-0 part is alpha_n A^2+beta_n AB with alpha_n=12/[n(n-1)], beta_n=24/[n(n-1)(n-2)]; SL2 invariance plus the t->0 limit | hand derivation | CONFIRMED |
| 5a | N3 §2 | det K=(af-be+cd)^2; Pf(K)=zw+uv/2+t^2/2=A+B/2 | hand derivation | CONFIRMED |
| 5b | N3 §2 | D_n=z^{n-4}(A+B/2)^2 is in the literal pencil image; the x1 coefficient is diag(J,J,I_{n-4}) with det 1, so D_n is in the chart x1 I + sum x_j A_j | hand derivation | CONFIRMED |
| 6a | N3 §3 | f_{H,4}(q+h)=f_{H,4}(q) exactly, for all q and all h in Sym^4(span(x3,x4,x5)) | hand derivation (each label puts 2 legs into {1,2}) | CONFIRMED |
| 6b | N3 §3 | D_4-p_4=B^2/4, and C_n(D_n-p_n)=B^2/[4 binom(n,4)] lies in Sym^4(V) | hand derivation | CONFIRMED |
| 7 | N3 §6 | each individual f_{H,n} is not in I(D_5^{det_n}); every g in the span has g(D_n)=g(p_n), so (p_n,D_n) cannot witness separation for any such g | hand derivation | CONFIRMED, at the scope given in the report |
| C | typed | the cubic wQ | hand derivation | NEITHER: reducible and singular, and not a symmetric permanent of linear forms (see report §4) |

Out of scope and NOT REVIEWED: N1 §3 (the MSS 2-lift sequence and the Ramanujan property) and
N1 §7 (the spectral gap 5/76, the expansion constant and the treewidth bound).

Registered outcome at checkpoint: **ACCEPT** (outcome 1) at the exact scope stated in
`docs/b26_02_review.md`.
