# Astra dream: symmetry must buy multiplicity headroom

13 September 2026. Standalone exploratory planning. No Batch17 launch or reopening of completed work. Results from closed batches are inherited from the supplied context, not reproduced here.

## Verdict

The intuition has a precise, useful version: **select representations where the full determinant stabilizer leaves fewer available copies than an independently certified collection of coordinate functions on actual padding.** The relevant statistic is a representation-specific invariant dimension, including transpose, rather than the size of a symmetry group.

There is no positive multiplicity witness in this session. There are three useful negative signals and one constructive route:

* Exact character calculations show that the full determinant orbit bound is at least the ambient multiplicity in **all 435 ambient representation types in degrees 1–6** for det4. Thus symmetry alone cannot furnish a multiplicity certificate in this range. This does **not** determine possible determinant boundary losses.
* The ambient-group dimension heuristic is backwards: unused variables already give independent z*per3 a 96-dimensional stabilizer subgroup, compared with dimension 30 for det4.
* A particularly tempting cheap padding probe cannot work: **setting any one of the nine entries of per3 identically to zero makes z*per3 a specialization of det4.** A successful padding lower-bound construction must retain information from the full permanent support.
* The best surviving approach is a strict two-stage procedure: first certify positive headroom using the rectangular/transpose bound and the correct padding-source ceiling; then seek a small exact coefficient minor on invertible transforms of the full z*per3. No headroom means no rank hunt.

The smallest proposed next experiment is the single finite screen specified in §7. It returns one qualified candidate or a negative result, not a list of unpriced cells.

## 1. Conventions and exact inequalities

Work over C. Put N=n², V=C^N, G=GL(V), W=Sym^n(V*), with

\[
(g\cdot f)(x)=f(g^{-1}x),\qquad
A_d=\mathbb C[W]_d=\operatorname{Sym}^d(\operatorname{Sym}^nV).
\]

For a partition λ of nd with at most N rows, let V_λ=S_λV and

\[
A_d=\bigoplus_\lambda V_\lambda\otimes M_{\lambda,d},
\quad a_{\lambda,d}=\dim M_{\lambda,d}.
\]

For f≠0, write X_f=closure(G·f), H_f=Stab_G(f), and m_f(λ,d) for the multiplicity of **V_λ**, not V_λ*, in C[X_f]_d. Both objects being compared use this same G and ambient A_d.

Restriction and the homogeneous-space description give

\[
A_d\twoheadrightarrow\mathbb C[X_f]_d
\hookrightarrow\mathbb C[G/H_f],\qquad
0\le m_f(\lambda,d)\le
\min\{a_{\lambda,d},\dim(V_\lambda^*)^{H_f}\}.                 \tag{1}
\]

The orbit multiplicity is exactly dim(V_λ*)^{H_f}; the closure inequality can be strict. The orbit ring may also contain rational G-representations that are not polynomial; (1) concerns the specified polynomial type. Its central character fixes the homogeneous degree: tI acts on V_λ by t^{nd}.

Here is an intrinsic rank formulation. A multiplicity vector φ∈M_{λ,d}=Hom_G(V_λ,A_d) determines

\[
E_f(\phi)(v)=\phi(v)(f)\quad (v\in V_\lambda).
\]

Then E_f:M_{λ,d}→V_λ* has rank m_f(λ,d) and image in (V_λ*)^{H_f}. Indeed its kernel consists exactly of the copies whose entire G-span vanishes on f and hence on X_f. This formulation distinguishes **the image dimension** from **its position**.

For the projective stabilizer K_f={h:h·f=χ_f(h)f}, the correct refinement is

\[
\operatorname{im}E_f\subseteq
\{w\in V_\lambda^*:h w=\chi_f(h)^d w\text{ for every }h\in K_f\}.       \tag{2}
\]

It is χ_f^d on the dual, not an untwisted fixed space of K_f. This follows from E_{h·f}=hE_f and homogeneity. For tI, χ_f(tI)=t^{-n}, agreeing with the t^{-nd} action on V_λ*.

If X_pad⊆X_det, restriction C[X_det]_d→C[X_pad]_d is surjective, so

\[
m_{\rm pad}\le m_{\det}\quad\hbox{in every cell}.
\]

Consequently D=m_pad−m_det>0 is sufficient for noncontainment. Writing i_f=a−m_f gives D=i_det−i_pad. Noncontainment itself does not require D>0: restriction kernels can be differently positioned even when i_det<i_pad.

### The full determinant stabilizer

Identify V with n×n input matrices and use L_{A,B}(X)=AXB^T. For n≥3,

\[
H_{\det}=\big((SL_n\times SL_n)/\mu_n\big)\rtimes\langle\tau\rangle,
\quad\tau(X)=X^T.
\]

The kernel in the connected presentation is {(ζI,ζ^{-1}I):ζ^n=1}. Equivalently the connected group is the image of det(A)det(B)=1. The projective character under our action is

\[
\chi_{\det}(L_{A,B})=(\det A\det B)^{-1},\qquad\chi_{\det}(\tau)=1.
\]

The orbit dimension is N²−(2n²−2); for n=4 this is 226. The stabilizer and orbit-multiplicity formula are recorded in [BLMW, §5.2, Proposition 5.2.1](https://arxiv.org/pdf/0907.2850v2); their convention places forms in a covariant space, so the duals must be translated as above.

Put q=nd and R=(d^n), a rectangle with **n rows of length d**. Branching V_λ* to GL_n×GL_n leaves, under SL_n×SL_n, exactly the (R,R) channel. Its dimension is

\[
g_\lambda=g(\lambda,R,R).
\]

On this channel transpose swaps the two Specht factors. Thus

\[
s_\lambda=\dim\operatorname{Hom}_{S_q}([\lambda],\operatorname{Sym}^2[R]),
\qquad m_{\det}\le\min(a,s_\lambda)\le\min(a,g_\lambda).             \tag{3}
\]

There is no additional (−1)^d transpose factor in these conventions. One-dimensional det^d factors swap with sign +1. Using X→AXB^{-1} instead would require corresponding duals/characters on the second factor.

The exact character formulas used in the calculation are

\[
g_\lambda=\sum_{\rho\vdash q}\frac{\chi_\lambda(\rho)\chi_R(\rho)^2}{z_\rho},
\quad t_\lambda=\sum_{\rho\vdash q}\frac{\chi_\lambda(\rho)\chi_R(\rho^{[2]})}{z_\rho},
\quad s_\lambda=\frac{g_\lambda+t_\lambda}{2}.                       \tag{4}
\]

Here z_ρ is the centralizer order; ρ^[2] is the cycle type after squaring a permutation. The trace formula follows from Tr(swap∘(T⊗T))=Tr(T²). The discarded dimension is (g−t)/2, which need not equal g/2.

If q_det is a certified determinant ideal floor, the available upper bound is

\[
B=\min\{a,s_\lambda,a-q_{\det}\}.                               \tag{5}
\]

Do not add the stabilizer deficit a−s to q_det without proving independence of those equation spaces. An actual padding floor r>B proves D≥r−B>0.

### The correct padding ceiling

Let k=n−m>0, and let Y be the closure of forms l^k C with C having at most m² essential variables. Multiplication from V*×Sub_{m²}(Sym^m V*) contains X_pad in its image closure. Pullback into bidegree (kd,d), followed by Pieri, gives the rigorous ceiling

\[
U=\min\left\{a,\sum_{\substack{\mu\vdash md,\ \ell(\mu)\le m^2\\
                    \lambda/\mu\text{ horizontal strip of size }kd}}
       a_\mu(d[m])\right\},\qquad m_{\rm pad}\le U.                \tag{6}
\]

The source is Sym^{kd}V⊗C[Sub_{m²}(Sym^mV*)]_d. Pullback is injective on the image coordinate ring; it need not fill the source. This proves (6) without assuming normality or surjectivity of a padding map. In particular λ₁≥kd and ℓ(λ)≤m²+1 are necessary. The latter is **10**, not 9, for independent z*per3.

Replacing the core coordinate ring by that of the actual permanent can tighten this ceiling, but still supplies a ceiling, not a floor. [Kadish–Landsberg, Theorems 1.2–1.3, 1.7 and Proposition 1.8](https://arxiv.org/pdf/1204.4693) distinguish the padding ideal, the image map, and the normalization. None identifies our actual padding image with generic reducibles.

The operative screen is

\[
\boxed{U>B.}                                                     \tag{7}
\]

With symmetry alone, this requires s_λ<U≤a, equivalently t_λ<2U−g_λ. This is a meaningful quantitative interpretation of “group resonance.” If U≤B, the proposed certificate fails; it is not an exclusion of the actual cell unless B is also the exact determinant multiplicity. The complete Batch16 ideal dimensions do permit those stronger exclusions in the four closed cells.

## 2. Three mechanisms, ranked by evidence

| Rank | Mechanism | Evidence and assessment |
|---|---|---|
| 1 | A small rectangular invariant channel, sharpened by its transpose trace, paired with actual permanent coefficient independence | Exact determinant upper bound and an exact certificate format. Best justified search framework. Fresh degrees 1–6 calibration is negative; no positive cell identified. |
| 2 | A mismatch between signed determinant row/column actions and unsigned permanent actions | Exact character mismatch; valuable for organizing coefficients and rejecting bad probes. The degree-one counterexample below disproves its sufficiency for multiplicity. Restricted equivariant-complexity results do not bridge that gap. |
| 3 | Failure of determinant orbit functions to extend to its boundary, detected through common matrix blocks across derivatives | Can reduce m_det below s_λ, so it addresses what mechanism 1 misses. Existing global Hessian equations support boundary-sensitive work, but no new shared-jet identity or size-dependent theorem is proved here. Lowest current evidence. |

### Why “more symmetry” is insufficient

For an actual inclusion H₁⊆H₂, fixed-space dimensions decrease in that order. H_det and H_pad are not being compared through such an inclusion. A scalar number dim H provides no representation-by-representation ordering.

In fact take V=C^{10}⊕C^6, with padding using the first summand. All input transformations

\[
\begin{pmatrix}I_{10}&0\\C&D\end{pmatrix},\quad
C\in\operatorname{Mat}_{6\times10},\ D\in GL_6,
\]

fix padding. Their dimension is 60+36=96, greater than 30 for H_det. This also gives dim X_pad≤256−96=160, without needing the full padding stabilizer. These global dimensions do not rule out an exceptional multiplicity gap.

For a finite group F, dim T^F=|F|^{-1}Σ_h Tr(h|T), not a lower bound dim T/|F|. A nontrivial one-dimensional character has no invariants. A division formula is justified only with an additional structural proof, for example a genuine permutation basis and its orbit count.

### An exact sign mismatch that gives no gap

Write padding as x44*per3 on the leading 3×3 block. For P,Q∈S₃, set

\[
\widehat P=\operatorname{diag}(P,\operatorname{sgn}P),\qquad
\widehat Q=\operatorname{diag}(Q,\operatorname{sgn}Q).
\]

Both matrices have determinant 1, so X→P̂XQ̂^T belongs to H_det4. It acts on padding by ε(P,Q)=sgn(P)sgn(Q). Hence E_pad lands in the ε^d-character space while E_det is fixed. For odd d the characters differ.

Nevertheless, at d=1 the ambient module is the irreducible S_(4)V, and both nonzero polynomials generate it dually: a=m_det=m_pad=1. The mismatch separates vectors inside a representation, **not the numbers of copies**. At even d this particular mismatch disappears. Moreover τ fixes both original polynomials, so counting the entire τ-odd part of S_λV* as padding freedom is wrong.

[Landsberg–Ressayre, Theorems 2.1 and 2.8](https://people.tamu.edu/~jml/LRpermdet8-4.pdf) prove, for m≥3, equivariant determinantal complexity binomial(2m,m)−1 and the lower bound 2^m−1 when a representation respects the left monomial group. These are bounds on symmetry-respecting **realizations**. Their Theorem 2.13 gives the same binomial bound for regular equivariant realizations of determinant. Thus imposing such a realization condition cannot silently replace the unrestricted orbit-closure problem.

## 3. A proved candidate lemma: cheap sparse padding probes can be doomed

**Lemma (proved here as a planning filter).** Let Y be a 3×3 matrix of arbitrary linear forms, one of which is identically zero. Then z*per3(Y) belongs to the det4 orbit closure. More generally, if signs can convert per_m(Y) into det_m(S∘Y), then z^{n−m}per_m(Y) is a specialization of det_n.

**Proof.** Permute rows and columns to put the zero in position (3,3), which preserves the permanent. For

\[
Y=\begin{pmatrix}a&b&c\\d&e&f\\g&h&0\end{pmatrix},\qquad
Y'=\begin{pmatrix}-a&b&c\\d&-e&f\\g&h&0\end{pmatrix},
\]

direct expansion gives

\[
\operatorname{per}(Y)=afh+bfg+cdh+ceg=\det(Y').
\]

Therefore z*per(Y)=det(diag(Y',z)). In general use diag(S∘Y,zI_{n−m}). A linear substitution of det_n lies in its orbit closure because GL_N is dense in End(V) and substitution is a polynomial map. This proves the assertion for arbitrary dependencies among the linear forms. ∎

The full symbolic 3×3 permanent does not admit such an entry-sign conversion. Writing a sign as (−1)^{u_ij}, matching all six determinant terms would require

\[
\sum_i u_{i,\sigma(i)}=\operatorname{parity}(\sigma)\pmod2
\quad(\sigma\in S_3).
\]

Sum the six equations: each u_ij occurs twice, but three permutations are odd. This gives 0=1. Allowing a common overall sign adds six identical constants and does not change the contradiction.

**Consequence.** Evaluations or arcs lying wholly in any such zero-entry family can never certify padding rank greater than a valid determinant upper bound. Combining multiple such families does not help: their union remains inside X_det. Full support is necessary for this route, but is far from sufficient for a gap. A full-support arc may have a signable leading degeneration; its higher coefficients can still carry new information, so the lemma does not forbid those arcs.

A related exact control: det4 and z*per3 both degenerate to every product of four linear forms. Every binary quartic is such a product over C. By subspace inheritance, **all two-row cells have m_det=m_pad=a in every degree** for this pair. For example the computed d=5, λ=(16,4) cell has all three multiplicities equal to 2. Lower bounds obtained only from diagonal permanent degenerations cannot beat determinant: these degenerations are already inside its closure.

This lemma and the degree-one sign example are countertests of the strongest naive symmetry interpretation. They are elementary deductions, not claims of new results in the literature.

## 4. A concrete selector and an actual padding lower-bound route

Use the long-first-row family

\[
\lambda(n,d,\nu)=(nd-|\nu|,\nu),\quad
\ell(\nu)\le m^2,\quad |\nu|\le md,\quad nd-|\nu|\ge\nu_1.
\]

This includes every padding-eligible shape, but the following gates make it a selection algorithm rather than an unscreened census:

1. Apply proven exclusions and the degree/shape gates in §6. For the current pair discard all degrees ≤6 for the symmetry-only certificate, all two-row cells, and the closed Batch16 targets. Do not promote a multiplicity-free ambient cell as a genuinely non-occurrence multiplicity target: require a≥2 and, preferably, 1≤B<U. To establish that a resulting witness is strictly beyond occurrence, also prove m_det≥1 by an actual nonzero determinant evaluation; positivity of its upper bound B does not prove occurrence on the closure.
2. Compute a and the finite support-corrected U of (6). If U=0, stop. A generic ten-variable cubic is not the nine-variable core source.
3. Compute the connected bound g and then the exact transpose trace t. Set B by (5). Only U>B survives. Record separately how much of the improvement comes from transpose and how much from certified equations.
4. Order survivors by smallest required witness size B+1, then by largest U−B, then by estimated symbolic support. Return only the first affordable survivor. The affordability estimate must count actual coefficient terms and rows, not just a.
5. Build B+1 highest-weight polynomials of this single λ on actual padding. Stop as soon as an exact minor proves independence. If the chosen family loses a whole permanent entry, reject it by §3 before computing ranks.

For fixed small ν and d≥|ν|, one may replace a large connected character computation by

\[
g(\lambda(n,d,\nu),(d^n),(d^n))=
\dim S_\nu(\mathfrak{sl}_n)^{GL_n}.
\]

This is [Manivel, Theorem 1](https://arxiv.org/pdf/0907.3351). It stabilizes the **connected** bound. Do not assume it also identifies the transpose involution without proving compatibility; otherwise compute t at the actual finite degree.

### The lower bound must use the full permanent map

Let b and A_ij be linear forms on V and use the polynomial parameter map

\[
\Phi(b,A)=b^k\sum_{\sigma\in S_m}\prod_{i=1}^m A_{i,\sigma(i)}.
\]

Its image closure is X_pad: tuples with all m²+1 forms independent are restrictions of invertible changes of coordinates and are dense in the parameter space. Thus pullback of any nonzero function on X_pad is nonzero under this map. For degree d, the pullbacks have degree kd in b, degree d in each row of A and degree d in each column of A. Those exact margins, followed by row/column permutation averaging, are legitimate coefficient compression rules. Dividing a dimension by the group order is not.

An alternative that enforces actual orbit points from the outset is A(t)=A₀∏(I+t_jE_{u_jv_j}), with A₀ invertible and u_j≠v_j, and p_t(x)=p(A(t)x). Every specialized A(t) is invertible. This is a polynomial family of transforms of the exact padding; no generic cubic is introduced.

**Coefficient-minor lemma (proved).** Suppose F₁,…,F_r∈A_d are highest-weight vectors of the same λ. For a polynomial family p_t⊆X_pad, form

\[
C_{ij}=[t^{\beta_i}]F_j(p_t).
\]

If an r×r minor of C is nonzero, then m_pad(λ,d)≥r.

**Proof.** A linear dependence among the restricted F_j would pull back to a zero polynomial in t, so every coefficient row would annihilate the dependence. The nonzero minor rules this out. The highest-weight space of a λ-isotypic coordinate-ring component has dimension equal to its multiplicity. ∎

For a particularly short certificate, choose a monomial order and actual tableau polynomials whose nonzero leading monomials after pullback are pairwise distinct. Their ordered coefficient matrix is triangular. Contributions with identical exponents must first be combined with their Young-symmetrizer signs; “there is a matching” does not preclude cancellation. Another valid certificate is an exact evaluation minor at rational invertible substitutions. A modular minor also certifies characteristic-zero nonvanishing if it is a reduction of the explicitly identified rational/integer matrix and all denominators are invertible modulo that prime.

The success threshold is **r=s_λ+1** for the pure stabilizer method, or r=B+1 with additional equations. A complete ambient basis and the exact determinant rank are unnecessary for this sufficient certificate. The unresolved mathematical work is finding that many independent functions of the same λ on the full permanent map. No such minor is supplied here; source capacity U cannot fill the gap in the proof.

## 5. Fresh bounded calculation and what it says

The standard-library program [toy_character_screen.py](toy_character_screen.py) evaluates h_d[h_4], the exact character sum (4), and the nine-variable-core Pieri source (6). It uses integer Murnaghan–Nakayama characters and rational power-sum coefficients. It does not sample polynomial orbit points.

| d | Ambient types a>0 | Sum of ambient multiplicities | Types with s_λ<a | Types with U>min(a,s_λ) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 |
| 2 | 3 | 3 | 0 | 0 |
| 3 | 9 | 9 | 0 | 0 |
| 4 | 28 | 33 | 0 | 0 |
| 5 | 95 | 142 | 0 | 0 |
| 6 | 299 | 742 | 0 | 0 |

The exhaustive scope at each degree uses ℓ(λ)≤d, a necessary property of Sym^d(Sym^4V). Controls check symmetric-group character orthogonality through S₆, an explicit S₄ symmetric/exterior-square sign example, the decomposition of Sym²(Sym⁴), and the full GL₁₆ dimension identity

\[
\sum_\lambda a_\lambda\dim S_\lambda\mathbb C^{16}
=\binom{3876+d-1}{d}.
\]

The first run (d=1–4) took 0.1034 s; the second (d=5–6) took 6.0928 s, with peak aggregate committed memory 158,150,656 bytes in the larger run. Both used the inspected existing Windows Job Object wrapper with 60-second/512-MiB caps and one BLAS thread. All logs were written in this planning folder. The wrapper's inherited `batch15` metadata label does not denote a batch launch.

The output proves only that (3) is not small enough in these cells. Equality m_det=a is **not** inferred from s≥a. A boundary-extension mechanism could still produce equations that this orbit bound misses. No assertion of full determinant coordinate rank in this whole range is made.

The closed Batch16 values are even more decisive for their own cells: m_det=418 forces s≥418 in the stable tail, whereas U=288. No refinement using the **actual full** stabilizer can lower its valid upper bound below the already known rank. Additional rank-9 restrictions of the determinant equation space would concern kernel position, not repair this numerical deficit.

## 6. Primary-source regime checks and size-growth limits

* **LMR benchmark.** [Landsberg–Manivel–Ressayre, Theorem 1.0.1](https://arxiv.org/pdf/1004.4802) proves the quadratic border/orbit-closure bound n≥m²/2. The current m=3,n=4 noncontainment is inside its range. A lower equation degree at this same pair does not improve the growth of the determinant size.
* **A multiplicity exclusion inside BIP.** [Bürgisser–Ikenmeyer–Panova, Proposition 2.4 and its proof in §6(a)](https://arxiv.org/html/1604.06431v3) says every nonzero highest-weight vector survives determinant restriction when |bar λ|≤h d and h d²≤n for some positive integer h. Therefore m_det=a in that cell. For padding use h=m; more sharply use h=max(1,ceil(|bar λ|/d)). This excludes multiplicity obstructions, not merely occurrences, in that regime.
* **Connected bound only.** [Ikenmeyer–Panova, Corollary 1.9](https://arxiv.org/pdf/1512.03798) gives a_λ>g_λ and |bar λ|≤md ⇒ d>n/m. It is not stated for s_λ. Thus in the window sqrt(n/m)<d≤n/m, a symmetry certificate, if one exists, must exploit transpose rather than the connected bound. Boundary losses are a separate possibility.
* **Occurrence barrier.** BIP Theorem 1.4 uses n≥m²⁵, all d, and **internal padding X11^{n−m}per_m**. It proves occurrence inclusion, not multiplicity domination. Its printed length bound is m². Do not substitute it for the length-10 condition of independent z*per3. IP Appendix 7 gives a polynomial-size comparison between padding conventions for determinantal representations, not equality of their finite coordinate rings. This report does not assert an identical fixed-n cutoff for independent padding on the strength of that appendix.
* **Multiplicity can be stronger in another comparison.** [Dörfler–Ikenmeyer–Panova, Theorem 2.3](https://arxiv.org/html/1901.04576v1) concerns Chow varieties versus bounded border-Waring-rank varieties. Its family uses d=k=n+1 and λ=(n²−2,n,2); the finite (n,m,k,d)=(6,3,4,7) example has multiplicities 7<8. Absence of occurrence obstructions is proved in its two specified finite settings, not throughout that whole family. None of these multiplicities transfers to per3 versus det4.

There is a genuine route beyond the Hessian threshold: for a growing pair m,n, construct a family λ and actual coefficient minors with r(m,n)>B(m,n). These are global polynomial functions and the determinant bound comes from its full stabilizer, so this certificate is not intrinsically capped by Hessian rank 2n. But that is a route, not a growth estimate. To claim an improvement over the quadratic benchmark one must establish the inequality for n above m²/2 along an infinite family; a single diagnostic n=ceil(m²/2) is not enough. To claim a superpolynomial bound requires the corresponding exclusions for every fixed polynomial size scale. Neither follows from this report.

For mechanism 3, define the extension defect e_λ=s_λ−m_det≥0. A positive gap requires e_λ>s_λ−m_pad, and hence necessarily e_λ>s_λ−U. This prices how much boundary information must supplement the orbit bound. An ideal floor q_det gives e_λ≥s_λ−a+q_det, reproducing the test q_det+r>a; it does not make that test automatic. A shared-jet identity must first be globally polynomial, survive singular substitutions/closure, be independent of the equations already counted, and yield a padding minor satisfying (5). Multiplying the same Hessian-divisibility condition by more factors changes equation degree but adds no demonstrated size range. The reported negative quadratic 34-coordinate jet control remains a stopping condition for repeating that exact control.

## 7. Cheap falsification tests, stopping rules, and the next experiment

Before any candidate evaluation:

1. Check |λ|=nd, length, the padding first-row constraint, and the source support bound. Apply the two-row exclusion for n=4,m=3 and the literature degree gates.
2. Check actual projective characters and the transpose sign. At d=1 the expected answer is a=s=m_pad=m_det=1. A claimed sign-driven gap here falsifies the implementation.
3. Require U>B. If q_det is only a floor, record failure of that certificate rather than an exclusion of the cell. If exact m_det≥U is known, retire the cell entirely.
4. Reject a padding family with one permanent entry identically zero. Keep determinant, generic quartics, l*C with C of essential dimension≤9, and actual padding as distinct controls when maps are evaluated.
5. A plateau is not a rank upper bound. Prove the coefficient identity or stop with a lower bound. Do not sum ranks from different coefficient blocks unless independence across the blocks is certified.
6. Stop a symbolic proposal before execution if it cannot be priced inside the requested cap. A cap hit yields “uncomputed,” never a zero or an exclusion. Do not extend the search automatically after a negative result.

**Proposed smallest next experiment — one short-body degree-7 screen.** Fix n=4,m=3,d=7 and enumerate only λ=(28−|ν|,ν) with |ν|≤10, 2≤ℓ(ν)≤6, 28−|ν|≥ν₁, a≥2. Use an explicitly bounded, cache-controlled character preflight to compute (a,U,g,t,s). Return only the affordable cell minimizing B+1 among those with 1≤B<U, or report that none in this finite slice survives. Do not build any padding evaluation matrix until such a cell is found. If a survivor exists, the next separate experiment is exactly one (B+1)×(B+1) coefficient/evaluation minor using all nine permanent entries and an invertible substitution family.

This is a diagnostic slice, not evidence that short bodies are promising or a claim that the rest of degree 7 has been screened. If it fails, stop the short-body proposal and formulate one boundary-extension lemma before requesting more character work. The six nearby Batch16 cells remain in their previously reported uncomputed status; this session neither dispatched nor ranked them as new symmetry evidence.

## Delivery and review status

The saved [citation register](CITATIONS.md) identifies versions, theorem locations, and scope cautions. [TOY_CALCULATIONS.md](TOY_CALCULATIONS.md) records the two exact symbolic countertests and the computational recipe. Machine-readable rows are in [degrees 1–4](toy_character_screen.json) and [degrees 5–6](toy_character_screen_d5_d6.json), with resource receipts under `results/logs/`.

Proved here: the rank/character deductions, support-corrected ceiling derivation, sparse-probe lemma, sign counterexample, two-row control, and conditional coefficient-minor certificate. Fresh computation: the finite character tables. Inherited: all Batch16 ranks and equations. Unproved: any positive multiplicity gap, any full-padding minor above a determinant bound, any new shared-jet identity, and any improved determinant-size growth bound.
