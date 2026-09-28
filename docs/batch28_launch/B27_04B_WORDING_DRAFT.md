# B27-04b — proposed exact wording (DRAFT for the author's approval)

Drafted by the integrator on 2026-09-24 from the committed after-states:
- Paper 2: `b28-04-p2`, based on `b24-06-paper2` @ `f8326974`; `paper/det4-onset.tex` is CRLF.
- Paper 3: `b28-04-p3`, based on `b23-04-paper3` @ `4c5a5450`.

Each item gives a FIND string (quoted in its LF rendering) and its REPLACE text. B28-04 applies
them verbatim, preserving each file's line endings. **Once approved, nothing here may be
reworded.** For each item, answer **approve / change / drop**.

Two items rest on results accepted since the Batch 27 close:
- **B28-03** (`e0a8041b`) accepted R27-K4's any-degree lemma. Item 2 is therefore a *citation of
  the accepted argument*, not the narrowing note R27-K4 first proposed.
- **C1** (the smooth-cubic exclusion, closed by the author's ruling on 2026-09-23) **answers
  Paper 3's named open question (Question 6.5) in the negative.** Item 3 restates the question for
  what remains open: singular cubic factors outside `D₃₅ ∪ Σ_Π`, which is B27-01's class (iii).

---

## Item 1 — the "35" gloss (Paper 2, Remark 6.3(iv))

Source: B26-05 §4.2. The fixed-factor 35 (`dim W`) and Paper 3's varying-factor 35 are different
numbers.

**FIND** (`paper/det4-onset.tex`):
```
($31$) \cite{Companion3}.  With every enumerated exceptional component at most $31$ as well,
```
**REPLACE:**
```
($31$) \cite{Companion3}.  (These are fixed-factor dimensions; letting the linear factor vary
adds $5-1=4$, giving families $\{\ell\cdot C\}$ of affine dimensions $33$ and $35$, and the
latter $35$ is not the $35=\dim W$ used here.)  With every enumerated exceptional component at
most $31$ as well,
```

## Item 2 — the cap-proof clause (Paper 2, L712–713 at `f8326974`, formerly L705–706)

This supersedes R27-K4's "scope note, n = 4 only". B28-03 accepted the lemma in every form degree
`d ≥ 1`, for `1 ≤ r ≤ N`. Here `d = n`, `N = n²` and `r = 5 ≤ n²` for `n ≥ 3`. The case `n = 2` is
treated separately at L671–675. The proof ingredients are those Paper 2 already lists at L1068–1071.
**No new citation is needed.**

**FIND:**
```
Fitting construction makes the span $\GL_5$-stable, and \eqref{eq:lengthred}
carries it into $I(\cO)$.
```
**REPLACE:**
```
Fitting construction makes the span $\GL_5$-stable, and the length-restriction
lemma carries it into the ideal of $\overline{\GL_{n^{2}}\cdot\det_n}$: its proof
(coefficient weights are non-negative, the raising operators beyond the first
five coordinates kill every restricted coefficient, injective substitutions are
dense, and complete reducibility holds in characteristic zero) uses nothing about
the form degree, so it applies verbatim with $(d,N,r)=(n,n^{2},5)$ for every
$n\ge3$, each highest-weight vector pulling back to a nonzero one.
```

## Item 3 — the smooth-cubic statements (Paper 3: abstract, Question 6.5, GAPS G-33)

### 3a. Abstract (L123–126)

**FIND** (`papers/det4-blindness/det4-blindness.tex`):
```
that part. Whether it survives on the boundary --- a point of $\Dff\cap\Pf$ that is a limit of
determinants without being one, with smooth cubic factor --- is this paper's named open
question.
```
**REPLACE:**
```
that part. A boundary point with smooth cubic factor would have destroyed it, and there is none:
$\ell\cdot C\notin\Dff$ for every smooth cubic $C$ and every $\ell\ne0$ \cite{Paper2}. Whether
it survives on the remaining boundary --- limits of determinants $\ell\cdot C$ with $C$ singular,
not determinantal and containing no plane --- is this paper's named open question.
```

### 3b. Question 6.5 and the paragraph after it

**FIND:**
```
Theorem~\ref{thm:classify} classifies $\overline{\Dff^\circ\cap\Pf}$. Is there a point of
$\Dff\cap\Pf$ outside $T_1\cup T_2$ --- necessarily a limit of determinants that is not itself a
determinant --- of the form $\ell\cdot C^*$ with $C^*$ smooth?
\end{question}
\noindent If there is, the right-way corner is gone: a smooth cubic would lie in the lift's
projection, and no Macaulay-rank threshold could separate. Nothing on the record excludes such a
point. Two natural invariants fail to exclude it.
```
**REPLACE:**
```
Theorem~\ref{thm:classify} classifies $\overline{\Dff^\circ\cap\Pf}$. Is there a point of
$\Dff\cap\Pf$ outside $T_1\cup T_2$ --- necessarily a limit of determinants that is not itself a
determinant --- of the form $\ell\cdot C$ with $C$ singular, $C\notin D_{35}$ and $C$ containing
no plane?
\end{question}
\noindent As first posed, with $C$ smooth, the question is answered: there is no such point,
since $\ell\cdot C\notin\Dff$ for every smooth cubic $C$ and every $\ell\ne0$ \cite{Paper2}. So
the right-way corner cannot be lost at a smooth cubic factor. A reducible $C$ contains a
hyperplane and lies in $\Sigma_\Pi$, so the singular irreducible case above is what remains.
Nothing on the record excludes such a point, and whether the cap minors vanish at one is not
known. Two natural invariants fail to exclude it.
```

### 3c. The provenance line of Question 6.5 (the `\prov{OPEN. …}` block)

**FIND:**
```
B17-01-C excludes one specific $F^*$, not a family}
```
**REPLACE:**
```
The smooth form of the question is CLOSED: B17-01's general smooth-cubic exclusion @ \cm{01c49022}, reviewed by B26-01 @ \cm{901b0fe6} and cross-lineage by A26-02R @ \cm{b0d2d2e8}, closed by the author's ruling of 2026-09-23. The singular form stated above stays OPEN; B27-01 @ \cm{01f78eb2}, reviewed by R27-01 @ \cm{51f9d17e}, shows that in the padding parameters it is a $49$-dimensional class excluded from literal determinants, with closure membership undecided}
```

### 3d. GAPS G-33

**FIND** (`papers/det4-blindness/GAPS.md`):
```
**Nothing on the record excludes such a point of the form `l·C*` with `C*` smooth**, and if one exists the right-way corner is gone: a smooth cubic would lie in the lift's projection and no Macaulay-rank threshold could separate.
```
**REPLACE:**
```
**⟳ 2026-09-24: the smooth case is CLOSED.** `l·C ∉ D45` for every smooth cubic `C` and every `l ≠ 0` (B17-01 @ `01c49022`; B26-01 @ `901b0fe6`; A26-02R @ `b0d2d2e8`; author's ruling 2026-09-23), so no boundary point has a smooth cubic factor and the right-way corner cannot be lost there. **What stays open is a boundary point `l·C` with `C` singular, `C ∉ D35`, `C` containing no plane** (reducible `C` lies in `Σ_Π`). B27-01 @ `01f78eb2` (R27-01 @ `51f9d17e`) shows this class is 49-dimensional in the padding parameters and excluded from literal determinants; its closure membership is undecided. (Historical wording: nothing on the record excluded such a point with `C*` smooth.)
```

**FIND** (same row):
```
B17-01-C excludes one specific `F*`, not a family.
```
**REPLACE:**
```
B17-01-C excluded one specific `F*`; the general smooth-cubic exclusion is now accepted (above).
```

## Item 4 — the cap-theorem inputs at `n = 3` (Paper 3, abstract (iv) and L896–898)

This matches the C34 wording already applied by B27-04 (Paper 1 Prop. 4.23).

**FIND** (abstract):
```
conditional on the cap theorem (PROVED modulo Kleiman, Dimca and Gulliksen--Neg\aa rd, all
three ADOPTED inputs).
```
**REPLACE:**
```
conditional on the cap theorem, which at $n=3$ is PROVED modulo Kleiman and Dimca, both ADOPTED
inputs (Gulliksen--Neg\aa rd is not needed at $n=3$ \cite[Prop.~4.23]{Paper1}).
```

**FIND** (§6):
```
(Proposition~\ref{prop:capplane}), the $D_{35}$ half carrying the cap theorem's own label,
PROVED modulo three named ADOPTED inputs (Theorem~\ref{thm:cap}) --- and they are nonzero at
```
**REPLACE:**
```
(Proposition~\ref{prop:capplane}), the $D_{35}$ half carrying the cap theorem's label at $n=3$,
PROVED modulo Kleiman and Dimca, both ADOPTED (Theorem~\ref{thm:cap}; Gulliksen--Neg\aa rd is
not needed at $n=3$ \cite[Prop.~4.23]{Paper1}) --- and they are nonzero at
```

## Item 5 — `PAPER2_GAPS.md`: G-P2-18 and G-P2-19

**APPEND** at the end of the file:
```

## Part V — B27-04 and B28-04 (2026-09-23/24)

- **G-P2-18 — CLOSED.** The smooth-cubic result is stated in general in the TeX (B27-04 @ `f8326974`): `ℓ·C ∉ D₄,₅` for every smooth cubic `C` and every `ℓ ≠ 0`, cited through `Companion2`, scope geometric non-containment only. C1 was closed by the author's ruling of 2026-09-23 on B17-01 @ `01c49022`, B26-01 @ `901b0fe6` and A26-02R @ `b0d2d2e8`. Singular and reducible cubic factors stay open (G-A1).
- **G-P2-19 — CLOSED.** The `r = 9` flag was removed by B27-04. The quartic `16 → 9` transfer was accepted cross-lineage (B26-04 @ `65736d9f`, B26-10A @ `21816b3c`); the general degree-4 statement by R27-K4 @ `53206b43`; and the any-degree form by B28-03 @ `e0a8041b`. The cap-proof clause now uses the any-degree form (B28-04 item 2). This clears the transfer step only: the LMR copy and the other cap-theorem inputs rest on their own evidence.
- **Remark 6.3(iv)** gains the fixed/varying-factor gloss on "35" (B26-05 §4.2; B28-04 item 1).
```

## Item 6 — the "PROPOSED, UNCOMMITTED" labels on the B26-05 appends

**FIND** (`PAPER2_CLAIMS.md`):
```
## N. B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only)
```
**REPLACE:**
```
## N. B26-05 current-state amendment (2026-09-22; proposed by B26-05, applied verbatim by B27-04 @ `f8326974`)
```

**FIND** (`PAPER2_READINESS.md`):
```
**B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only; the B24-06
```
**REPLACE:**
```
**B26-05 current-state amendment (2026-09-22; proposed by B26-05, applied verbatim by B27-04 @ `f8326974`; the B24-06
```

**FIND** (`PAPER2_READINESS.md`):
```
(1) The `n = 4` sixteen-to-nine transfer **stays flagged** (G-P2-19). B26-04 is checking it, and
```
**REPLACE:**
```
(1) [⟳ 2026-09-24: superseded. The flag was removed by B27-04 and the transfer is accepted; see
PAPER2_GAPS Part V.] The `n = 4` sixteen-to-nine transfer **stays flagged** (G-P2-19). B26-04 is checking it, and
```

---

## Checks B28-04 must run

- Every FIND occurs **exactly once**; otherwise stop that item.
- Paper 2's CRLF bytes are preserved.
- Static checks as in B27-04: brace balance, `$` parity, every `\ref` and `\cite` defined, no new
  slot labels in Paper 2's TeX, and "Claude" only in the acknowledgement.
- Paper 3 may carry slot labels in its `\prov` blocks, as it already does. It adds no new
  bibitems: `Paper1` and `Paper2` already exist.
- The integrator compiles both after-states.
