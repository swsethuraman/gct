# A25-02 — Typed applicability of six exclusions

LOCAL COMPLETE — UNCOMMITTED / NOT RELEASED. Producer: Astra. Assessment timed from 2026-09-21T00:44:57Z; framework frozen by 2026-09-21T00:46:29Z. Final seal time and elapsed time are recorded by the administrative sealing script in the manifest. Outcome selection was completed before sealing, within the 45-minute bound. No mathematical pilots.

## Result and chosen outcome

**Outcome (1): a typed scope matrix, proved short implications, and a concrete survivor specification.** The six exclusions do not define six subsets of one construction universe. They concern source functions, coefficient constructions, invariant loci, threshold statistics and representation weights. A putative six-way intersection without maps between those objects is ill-typed. This is a framework finding, not a coverage/no-go theorem.

The strongest new certificate implication is elementary and exact: fix a finite coefficient space H with basis h_j, an exact pullback matrix Q for phi* restricted to H, and an actual-padding evaluation row p. Then

    H contains an equation nonzero at that padding point
    iff p is outside row(Q)
    iff rank([Q;p]) = rank Q + 1.

**PROVED, independent hand derivation**, in [IMPLICATIONS.md](../results/a25_02/IMPLICATIONS.md), Theorem A. A sampled version is valid only with a proved global rank ceiling saturated by an exact or good-prime rank floor. It is a specification of the missing certificate, not a produced equation or a novel algebraic algorithm.

Theorem B proves the source/coefficient distinction formally: if N is a necessary source test and E_H=phi*(H) lies in ker N, then N phi* is zero on every H, not just on its coefficient kernel. N can still bound dim E_H through dim ker N. The inherited five-block identity N_w=L_w C_arc therefore implies that stacking those tests cannot improve this ceiling or its ensuing exact-kernel certificate. Proposition C proves closure of padding-blind coefficient generators under polynomial/ideal combinations, only after the generators have actually landed in the same coefficient ring. These proofs supply the bridges used here; no bridge to a multiplicity gap or an asymptotic lower bound is claimed.

## What the matrix says

[SCOPE_MATRIX.md](../results/a25_02/SCOPE_MATRIX.md) gives the six entries with exact domain, quantifiers/actions, conclusion, dependencies, review lineage, candidate consequence and an explicitly labelled out-of-scope class. No out-of-scope class is offered as a verified viable mechanism.

- Lemma 1.3 excludes polynomial extraction through the stated r-minors at padding points with rank below r. It neither proves determinant vanishing nor covers arbitrary kernels or rational cancellation. It is separate from the (r+1)-minor threshold ideal.
- Lemma 1.4 excludes positive-degree SL5 invariants and the specified GL5 cubic covariant lift. Its general divisibility formula is retained; its cubic determinantal conclusion is not generalized to arbitrary targets.
- D2' is a single-witness consistency test from D2 alone. It says nothing against properties true at pure powers, and it does not forbid all closed weakenings of a failed orbit property.
- The tail theorem acts on weight vectors. Its c_(n e1) factorization is not GL-equivariant and supplies no equality of highest-weight multiplicities. No conjectural900 bound is moved to det4.
- Direction reversal needs a proved comparison for the actual statistic. The submatrix preserves elementary row-1 coverage at N=5..8, the separate N=16 premise chain, N5 higher-Koszul T2, the N6/7 versus N8 dependency split, and the unclosed intermediate and N16 ranges.
- Astra's theorem is restricted to the fixed five-block torus and the stipulated source symmetries. Transposition is essential for exact support. Its nine initial-form classes do not classify every degeneration.

The matrix uses explicit actual-padding closures. Equality with the closure of all products lC in five variables remains ADOPTED where mentioned; none of the negative proofs extends that equality above five variables. The final B24-10 rulings govern over earlier headlines. In particular, the cap is PROVED modulo the named adopted Kleiman/Dimca/Gulliksen–Negard inputs, whereas the upgraded row-1 kill at N=5..8 uses elementary premises. The cap status is at B24-10 section 11.5, row 5.10, correcting the launch prompt's section 11.5.8 pointer.

C45 is preserved as the unpadded n=3 control (degree12, lambda=(19,7,2^5), D=+1), PROVED modulo (star); (star)'s own status remains OPEN in B24-10. Its floor cites LMR Theorem 2.3.1 with sections 3.1–3.2 through B24-02b, never the misprinted Theorem 1.0.2. It is not a padded-det4 breakthrough. The old degree-five rectangle diagnostic was not reopened.

## Applications and usable survivor requirements

[APPLICATIONS.md](../results/a25_02/APPLICATIONS.md) contains exactly three applications:

| application | disposition |
|---|---|
| Recorded row12 / coefficient-kernel bridge | ELIGIBLE IN PRINCIPLE as an exact membership framework; UNDERSPECIFIED as a feasible construction. “Find h in K” passes the pure-power test tautologically but gives no coefficient vector, degree, witness or price. Scheme-theoretic row10 merges into the same kernel mechanism under its named premises. |
| Non-rank smaller-minor relations, row3 | UNDERSPECIFIED. No exact matrix/minor-family/identity triple in the assessed inputs. Missing global determinant identity and separate actual-padding test are stated; no search begun. |
| Large-minor polynomial extraction from M_7 | EXCLUDED on all P5. The uniform padding ceiling245 is below a certified determinant floor299. Every polynomial in the r-minors without constant term, r=max_D rank>=299, is padding-blind; so is the entire fixed299-minor ideal. No exact generic-rank299 or cap premise is needed for that conclusion. |

[SURVIVOR_SPEC.md](../results/a25_02/SURVIVOR_SPEC.md) requires an exact h/map or certified source-to-coefficient bridge; a global identity h(phi(B))=0; a separately checkable actual-padding model and nonzero evaluation; explicit representation/closure conventions; a mechanism-by-mechanism hypothesis audit; and a finite certificate with dimensions, sparsity, bit growth and memory/time price. It distinguishes logical separation requirements from this programme's feasibility requirements. It gives symbolic operation/storage bounds, not unsupported runtime estimates.

**One next certificate, not launched:** a single explicit rational pair (h,T), with finite coefficient/circuit description, global pullback identity, exact nonzero actual-padding value, and size/bit/memory price. The matrix criterion is an alternative form of that same certificate. No particular cell, reserve session or new numerical job is nominated.

Existence of a supplied affordable instance is **OPEN**; exhaustive coverage is **NOT ESTABLISHED**. This does not withdraw abstract existence under the record's adopted noncontainment premises. A25-02 neither re-certifies those premises nor exhibits a separator. It proves no positive multiplicity gap and no asymptotic lower bound.

## Evidence, provenance and delivery

Method: **READ of committed packets plus independent hand derivations**; no REPLAY or INDEPENDENT EVALUATOR run. [SOURCE_BINDINGS.json](../results/a25_02/SOURCE_BINDINGS.json) records fresh raw-byte checks of 34 committed source blobs, including supplied manifests. Hash verification is provenance, not mathematical acceptance. The draft input audit was used only as a locator and expected-digest list; every used pin was resolved afresh through the shared Git object database.

Principal content read: B19-02 sections1–3/7; B22-02 sections1/4 and rows3/10–12; B22-10 sections5–6/S17–S21; Astra archive sections1/3/7–8; B24-02 sections3–4; B24-04 section2.2 and evaluator-scope statements; B24-05 section1.2 via the governing B24-10 derivation; GKZ corrected scope table and its underlying definitions; B20-02 sections1–2/6/8 and B20-02b sections1–4; B21-10 T1/T2 rulings and gates; B23-03 section3; B23-10 sections3.2–3.4/5.4; B23-02 Proposition1.1/R1–R3; cap Theorem1; B24-10 sections1–3/6.4/9 and governing section11; B24 ledger section8.14. B24-02b, CLAIMS and GAPS were provenance-bound for correction context; no fresh PRIMARY external-literature reading or numerical acceptance is inferred from their hashes. External literature used through reports remains SECONDARY here, regardless of a historical producer's PRIMARY label.

[INTAKE.md](../results/a25_02/INTAKE.md) records authorization, outcome registration, the initial Git state and the timestamp correction. Only A25-02 paths were written; A25-01 output was neither read nor used. No agents, extra tasks, tool memories, commits, pushes or publications were created. All source tips observed at intake match the pinned local baseline; no fetch or review of subsequently unfinished B25 work occurred.

[RESOURCE_RECEIPTS.md](../results/a25_02/RESOURCE_RECEIPTS.md): **0 pilots, 0 mathematical computational seconds**. [LIMITATIONS.md](../results/a25_02/LIMITATIONS.md) records the evidence boundaries. [MANIFEST.json](../results/a25_02/MANIFEST.json) binds this report and the local packet; it does not hash itself. [DELIVERY_NOTE.md](../results/a25_02/DELIVERY_NOTE.md) and [ADD_LIST.txt](../results/a25_02/ADD_LIST.txt) prepare the exact later delivery footprint.

**Provenance gate still open: G29 downstream delivery and independent review.** The local packet is complete but UNCOMMITTED / NOT RELEASED. There is no delivery commit. Raw-versus-filtered Git bytes differ for the report; ADMIN_VERIFICATION.json records all comparisons. A separately authorized delivery pass must resolve byte preservation with an explicit rules proposal or a newly reviewed normalization, commit only its approved paths, compare committed blobs to reviewed hashes and record the resulting commit/manifest binding separately. Historical seals and other producers' files must remain untouched.

