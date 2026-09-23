# B26-03 — source quotations and locators

**UNCOMMITTED / PRODUCER ONLY.** Every quotation below was read by this session (Claude Code,
Claude Opus 5.5 (1M context), 2026-09-22 UTC) in the bytes named. For arXiv items the quoted
text is taken from the authors' own TeX source (the e-print). The page number is the PDF page of
the arXiv PDF of the same version, located by `pdftotext` page breaks. The printed theorem numbers
were checked against that PDF's text layer, not inferred from the TeX counters. Quotes are short
and verbatim. `[...]` marks an omission, and TeX markup is kept as found. The thesis has no TeX
source. Its quotations come from `pdftotext` of the hashed PDF, which drops some glyphs. Where a
glyph was dropped, the reconstruction is given in ⟨angle brackets⟩ and labelled.

Fetch details (URL, retrieval UTC, SHA-256, bytes) are in `docs/b26_03_report.md` §3.

---

## Q1. Ikenmeyer–Kandasamy, arXiv:1911.03990v1 (e-print TeX `be587144…`, PDF `c3af3ef1…`)

**Lemma 5.2, PDF p. 9 (TeX l. 510–527), verbatim:**

> Let $\la \vdash_m dD$. If $D$ is even, let $e := d$ if $d\leq m$, $m + \lfloor \frac{d-m}{D-2} \rfloor$ if $d\geq m$.
> If $D$ is odd and ${{2(D-1)}\choose{D-1}} \geq 2(m-1)$, let $e := 2d$ if $d\leq m$, $2m + 2\lfloor \frac{d-m}{2(D-2)} \rfloor$ if $d\geq m$.
> In both cases we have $\mult_{(\la+(m \times e D))^*} \IC[\overline{Gp}] = \mult_{\la^*} \IC[G p] = \mult_{(\la+(m \times e D))^*} \IC[Gp]$.

(The `cases` environment is flattened onto one line here. The words are unchanged.)

**Standing definitions (§2, PDF p. 4, TeX l. 257; §3, PDF p. 6, TeX l. 335–338):**

> For $m \geq D$ let $p := x_1^D + x_2^D + \cdots + x_m^D$ and let $q := x_1 x_2 \cdots x_D$. Let $G := \GL_{m}$.  (§2, "Our contribution")

> We consider the power sum polynomial $p := x_1^D + \cdots + x_m^D \in \Sym^D \IC^m$. [...] For $D\geq 3$ these group elements generate the whole stabilizer of $p$ [...] Let $H := \stab p = \IZ_D^m \rtimes \aS_m \subseteq G$  (§3)

**Theorem 4.2 (Main technical theorem), on which Lemma 5.2's proof rests (TeX l. 390–404):**

> Let $m, d, D \in \IN$. If $D$ is odd, we assume that ${{2(D-1)}\choose{D-1}} \geq 2(m-1)$. [...] if $D$ is even, let $e_\varrho := \sum_{i=1}^{m} \lceil \frac{\varrho_i}{D-2} \rceil$.

**The tightness remark in the proof (TeX l. 539):**

> provides $e_\varrho = d$, so the bound is tight.

**§5, Prop. 5.3 proof (PDF p. 10; TeX l. 584–586): IK's attribution for the product of variables:**

> Kumar proved \cite{Kum:15} that $\mult_{(m)^*} \IC[\overline{G(x_1\cdots x_m)}] \geq 1$
> and that $\mult_{(m \times m)^*} \IC[\overline{G(x_1\cdots x_m)}] \geq 1$,
> provided that $m$ satisfies the Alon-Tarsi condition.

---

## Q2. Kumar, arXiv:1109.5996v2 (e-print TeX `8a091095…`, PDF `71078e23…`); journal-ref on the arXiv abstract page: *Compositio Math. 151 (2015) 292-312*

**Corollary 6.2, PDF p. 20 (TeX l. 1567–1576; source label `coro3.2`, printed "6.2 Corollary"), verbatim:**

> With the notation and assumptions as in the last theorem (in particular,
> assuming the validity of the column Latin
> $(m,m)$-square conjecture), for any
> dominant integral weight $\lambda$ for $GL(E)$ of the form
> $\lambda=\sum^{m}_{i=1} n_i\delta_{i}$, $n_{i}\in \mathbb{Z}_{+}$, the
> irreducible $GL(E)$-module $V_{E}(m\lambda)$ occurs in
> $\mathbb{C}[\mathcal{X}]$ with nonzero multiplicity.

**Theorem 6.1, PDF p. 20 (TeX l. 1524–1537):**

> Assume, as above, that $m$ is even. Assume further that the column Latin
> $(m,m)$-square conjecture \ref{conj16} is true. [...] Moreover, by Corollary \ref{coro2.4},
> $V_{E}(d\delta_{i})$, for any $d<m$ and any $1\leq i\leq m^{2}$, does
> not occur in $S^{\bigdot}(S^{m}(E))$

**Setting of §6 (TeX l. 1486–1492):** $E:=\End \mathfrak{v}$ with $\dim\mathfrak v = m$,
$Q:=\mathcal{P}^m (E)$, "Let $\mathcal{X}$ be the $G$-orbit closure of $\mathscr{D}$ inside $Q$",
where $G=GL(E)$ and $\mathscr D$ is the determinant.

**Standing parity assumption, PDF p. 4 (TeX l. 320):** "{\it From now on, $m$ is an even positive integer.}"

**Howe's vanishing (Prop. 2.3, PDF p. 3; TeX l. 290–302):** "We recall the following result from
\cite[Proposition 4.3]{H}. [...] (b) $[S^{\ell}(S^{m}(E))]^{SL(E)}\simeq (0)$ if $m$ is odd,
$\mathbb{C}$ if $m$ is even."

**Remark 4.5, PDF p. 13 (TeX l. 997–999):** "As proved by Huang-Rota [HR, \S 3], their column Latin
$(m,m)$-square conjecture is equivalent to the (full) Latin $(m,m)$-square conjecture given by
Alon-Tarsi [AT]."

**Theorem 5.6, last clause, PDF p. 18 (TeX l. 1434–1435; printed "5.6 Theorem"):**

> For $i=m$, $U_m\cap \mathcal{I}_{m\delta_{m}} \neq (0)$ if and only if
> the column Latin $(m,m)$-square conjecture is true.

**§3 (TeX l. 518, PDF p. 6):** $A\in\End E$ with "$Ae_{j}=\sum^{m}_{p=1}a^{j}_{p}e_{p}$, $1\leq j\leq i$",
where $e_1,\dots,e_m$ are the diagonal units $v_p\otimes v_p^*$. The map is $\theta(A)=(\mathscr D\odot A)_{|E_i}$.

---

## Q3. Kumar–Landsberg, arXiv:1410.8585v1 (e-print TeX `5c4eb18b…`, PDF `8397138d…`)

**Definition of the Chow variety, PDF p. 2 (TeX l. 185–188):**

> $\Ch_n(V^*):=\{ P\in S^nV^*\mid P=\ell_1\cdots \ell_n {\rm{\ for \ some \ } }\ell_j\in V^*\}.$

**Lemma 1.5, PDF p. 2 (TeX l. 198–204):**

> (Hadamard [...]) The kernel of the $\GL(V)$-module map
> $\oplus h_{d,n}:\Sym(S^nV):=\oplus_d S^d(S^n V)\ra \oplus_d S^n(S^dV)$ is the ideal of the Chow variety.

**Conjecture 1.6 (TeX l. 230–232):** "\cite{kumarcoordring} For all $d$ and $n$, $S_{(d^n)}V$ is not in
the kernel of $h_{d,n}$", where `kumarcoordring` = Kumar, *A study of the representations supported
by the orbit closure of the determinant*, arXiv:1109.5996.

**Theorem 1.9, PDF p. 4 (TeX l. 340–348):**

> Fix $n$ even. [...] The following are equivalent:
> (a) The Alon-Tarsi conjecture for $n$.
> (b) Conjecture \ref{kumarconj} for $n$ with $d=n$.

**§3, PDF p. 6:** "This proves the equivalence of (a) and (b) by Lemma 1.5."

---

## Q4. Kumar, arXiv:1007.1695v1 (e-print TeX `8209e0d1…`, PDF `3c6b70d7…`): the CMH 2013 paper

This is a **negative finding**, not a quotation. Case-insensitive searches of the full TeX source
found no occurrence of `Alon`, `Tarsi`, `Latin`, `Chow`, `Hadamard`, `Foulkes`, `product of`, or
any `x_1\cdots x` / `x_1x_2` / `x_1\dots x` monomial: zero hits. arXiv lists a single version
(v1) for 1007.1695.

---

## Q5. Bürgisser–Ikenmeyer, arXiv:1511.02927v2 (e-print TeX `fb1cec08…`, PDF `a4138fc3…`)

Read **only** to settle G-P4's attribution: the paper cites BI in the same sentence.

**Proposition 3.25 and the sentence before it, PDF p. 16 (TeX l. 1408–1414):**

> The following observation is due to Kumar~\cite{Kum:15}
> and Kumar and Landsberg~\cite{kumar-landsberg:15}.
>
> Let $m$ be even. Then $e(X_1\ldots X_m) \ge m$ and equality holds
> iff the Alon-Tarsi conjecture is true for $m$.

BI's bibliography (TeX l. 3170–3179): `Kum:15` = Kumar, *A study of the representations supported
by the orbit closure of the determinant*. `kumar-landsberg:15` = Kumar and Landsberg,
*Connections between conjectures of Alon-Tarsi, Hadamard-Howe, and integrals over the special
unitary group*.

The printed PDF numbers for BI's Theorem 3.14 (Howe), Problem 3.23 and Proposition 3.28 match the
locators the paper already uses.

---

## Q6. Hüttenhain, PhD thesis, TU Berlin 2017, doi:10.14279/depositonce-6032 (PDF `ccf1a13e…`)

Printed page numbers are the thesis's own. PDF pages are given in brackets.

**Chapter 8 opening, p. 89 [PDF p. 99]:** "In this chapter we give a description of the boundary of
the orbit of the 3 × 3 determinant. These results have been previously published in [HL16]." The
same page continues: "Our main result is a description of ⟨∂⟩(det3) that answers a question of
Landsberg [Lan15, Problem 5.4]". **Theorem 8.0.1:** "The boundary ⟨∂⟩(det3) has exactly two
irreducible components". The components are Q1, the determinant of the generic traceless matrix,
and Q2 = x4·x1² + x5·x2² + x6·x3² + x7·x1x2 + x8·x2x3 + x9·x1x3.

**§8.1, Lemma 8.1.3 and its proof, pp. 90–91 [PDF pp. 100–101]:**

> Let ⟨b⟩ := [[0, x1, −x2], [−x1, 0, x3], [x2, −x3, 0]] and ⟨a⟩ := [[2x6, x8, x9], [x8, 2x5, x7], [x9, x7, 2x4]].
> [...] b pro-jecting onto the space of antisymmetric matrices and a projecting onto its orthogonal
> complement of symmetric matrices. [...] To show that Q2 ∈ ⟨∂⟩(det3), we will use the approximation
> path b + at as outlined. [...] The coefficient of t in det(b + ta) is equal to tr(b⟨^♯⟩a) by Jacobi's
> formula, where b⟨^♯⟩ is the adjugate matrix of b. Furthermore, we have b⟨^♯⟩ = u⟨^t⟩u with
> u = (x3, x2, x1). Since tr(b⟨^♯⟩a) = u a u⟨^t⟩ = 2Q2, [...]

The matrices were laid out by `pdftotext` and have been re-set in row notation here. The adjugate
and transpose marks were dropped, and the reconstruction relies on "where b… is the adjugate
matrix of b".

**§8.3, Corollary 8.3.2, p. 96 [PDF p. 106]:**

> The orbit closure of the traceless determinant is an irreducible component of ⟨∂⟩(det_d), for all d ≥ 3.

In the section's own wording it is proved "for all d ≥ 3". Its proof uses Theorem 8.3.1, which
gives dim G_P = d² − 1, and Lemma 8.3.3, and reaches "dim(Q) = dim(det_d) − 1".

⟨∂⟩ is the boundary operator. The glyph is dropped by `pdftotext`, and its meaning is fixed by the
phrase "The boundary ⟨∂⟩(det3)" in Theorem 8.0.1.
