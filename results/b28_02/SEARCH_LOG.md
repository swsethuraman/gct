# B28-02 search record

**READ (administrative):** the search was a bounded literature audit. Web search located sources; theorem-level claims use downloaded primary PDFs, with versions and raw hashes in [SOURCES.json](SOURCES.json). Local text search used `rg`; relevant sections were read in full around each cited statement. Formula-heavy pages in DW2000, LMR and H2017 were also rendered and visually inspected. No PDF, extracted text, or rendered page is committed.

**HAND (search limitation):** a negative verdict means no answer in the checked statements and searches, not exhaustive coverage of all literature or a nonexistence theorem. Search snippets, abstracts, bibliographies and third-party summaries remain UNREAD for the results they describe. Unrelated engine hits were discarded without opening and are not treated as mathematical sources.

## Queries issued

**READ (administrative):** queries below are the actual search strings, grouped by tool call. Searches had no recency cutoff unless the year strings appear explicitly. Most used the general index; the `site:arxiv.org` round explicitly narrowed the domain. Additional direct URL opens and reference-following are listed afterward.

1. Initial scope:
   - `matrix semi invariants subalgebra generated degree n determinants multiplicities Foulkes map`
   - `boundary determinant orbit closure first order limits adjugate singular matrices quartic`
   - `Derksen Makam polynomial degree bounds matrix semi invariants arxiv`
2. Named spanning and boundary literature:
   - `Huttenhain Lairez boundary orbit determinant polynomial 3 2016 arxiv`
   - `Landsberg Manivel Ressayre boundary determinant odd n adjugate 2013`
   - `Derksen Weyman semi-invariants quivers saturation Littlewood Richardson coefficients theorem 2000 pdf`
   - `Schofield van den Bergh semi invariants quivers 2001 pdf`
3. Image versus ambient ring:
   - `"Landsberg" "Manivel" "Ressayre" "boundary"`
   - `"Domokos" "Zubkov" "semi-invariants" pdf`
   - `"determinant" "Foulkes" "coordinate ring" multiplicities`
   - `"image" "multiplicities" "determinant" orbit closure algorithm`
4. Exact target terminology:
   - `"determinant orbit closure" "multiplicities" "algorithm"`
   - `"Foulkes" "determinant" map multiplicity coordinate`
   - `"singular cubic" "determinant" "boundary" quartic`
   - `"first order" "determinant" "orbit closure"`
5. Algorithms and maps:
   - `"determinant" "multiplicities" "Ikenmeyer" "algorithm" orbit`
   - `"Foulkes" "Howe" "Chow" "map" kernel algorithm`
   - `"On generating the ring" "1508.01554"`
   - `"Polynomial degree bounds for matrix semi-invariants" arxiv`
6. Follow-up titles and later work:
   - `"Symmetrizing Tableaux and the 5th case" arxiv`
   - `"determinant" "orbit closure" "quartic" boundary`
   - `"Geometric complexity theory" "Lie Algebraic Methods" arxiv`
   - `"determinant" "orbit closure" "computing" equations Ikenmeyer`
7. Primary copies and SAGBI literature:
   - `"Semi-invariants of quivers" "Derksen" "Weyman" filetype:pdf`
   - `"Semi-invariants of quivers as determinants" filetype:pdf`
   - `"Fundamental invariants of orbit closures" arxiv`
   - `"Quiver semi-invariants and SAGBI bases" arxiv`
8. Dissertation and generated subalgebra:
   - `"determinant" "orbit closures" "Hüttenhain" "multiplicities"`
   - `"determinant" "coordinate ring" "algorithm" "Ikenmeyer" -site:researchgate.net -site:slideplayer.com -site:scribd.com`
   - `"determinant" "subalgebra" "semi-invariants" -site:researchgate.net -site:wikipedia.org`
   - `"4" "boundary" "determinant orbit" -site:researchgate.net`
9. Domain-constrained cross-check:
   - `site:arxiv.org determinant orbit closure multiplicities computation`
   - `site:arxiv.org boundary determinant singular matrix spaces first order`
   - `site:arxiv.org matrix semi-invariants subalgebra lowest degree`
10. Original Domokos-Zubkov copy:
    - `"Domokos" "Zubkov" "Semi-invariants of quivers as determinants" pdf`
11. Parity, later boundary work and residual class:
    - `"Hypersurfaces with degenerate duals" arxiv`
    - `"Hüttenhain" "det4" boundary 2024 2025 2026`
    - `"determinant orbit closure" "singular cubic"`
    - `"lowest degree" "semi-invariants" subalgebra multiplicities`

## Source-by-source route

| Source / status | How it was searched and checked |
|---|---|
| **PRIMARY DW2000** | Rounds 2 and 7; read author's publication index after two failed copies; followed its link to `A.I.a.6.pdf`. Read Theorem 1, definitions and surrounding context; visually checked p.470. |
| **PRIMARY SVB1999** | Round 2; arXiv full PDF. Searched `Theorem 2.3`, read the definition of determinantal semi-invariants and characteristic-zero assumption. |
| **PRIMARY IQS2015** | Rounds 1, 3, 5 and 9 plus committed s56 reference. Searched `kernel`, `Proposition`, `Fact 4`, `diagonal`; read the actual multilinear map, relation theorem and generation criterion. |
| **PRIMARY DM2017** | Rounds 1 and 5; author's publisher-formatted PDF. Searched numbered theorems and read §§1.1-1.4, including grading, matrix-size convention and field assumptions. |
| **PRIMARY M2015** | Rounds 1, 9 and 11; followed arXiv full PDF. Searched `Kronecker`, `Lemma 1.14` and `Hilbert series`; read the full-ring module formula and proof. |
| **PRIMARY HK2025** | Rounds 3 and 7 located the later SAGBI paper. Read v3's Theorems 1.1-1.3, dimension-vector assumptions and linked-tableau conventions; sampled neither bases nor ranks. |
| **PRIMARY CIM2015** | Rounds 5 and 6; full arXiv PDF. Read the map, Theorem 6, Chow identification and exact-evaluation algorithm; searched runtime discussion and read §§4-5. |
| **PRIMARY BI2015** | Rounds 5 and 7; full arXiv PDF. Searched `normal`, `Theorem`, `Proposition`, `determinant`; read Proposition 3.9 and Corollary 3.29 in context. |
| **PRIMARY DM2020** | Round 3 found publisher PDF; checked Theorem 1.17 and §5A rather than treating an abstract's polynomial-time assertion as an image algorithm. |
| **PRIMARY HL2016** | Rounds 1-2; full arXiv PDF. Read Theorem 1, Lemma 5, Jacobi formula and the start of the blowup argument; followed its LMR reference. |
| **PRIMARY LMR** | Rounds 2-3 and 11; author-hosted full PDF. Read Proposition 3.5.1 with its preceding odd-size restriction and proof; visually checked page 9. |
| **PRIMARY H2017** | Round 1 located deposited dissertation; round 8 pursued it. Searched `adjugate`, `first-order`, `normalization`, `boundary`, `n = 4`. Read Theorem 6.2.3 for the normalization distinction, then §8.3's theorem/corollary and §8.4's actual first-order constructions and open question. Visually checked printed p.103. |
| **PRIMARY ASS2022** | Rounds 4 and 6; full arXiv PDF. Read §3.1, Assumption 3.1 and Theorem 3.13. The source requires a family and transversality; its abstract alone was not used. |
| **UNREAD DZ2001** | Rounds 3, 7 and 10; opened publisher's DOI page, which exposes an abstract and subscription preview. Author-upload ResearchGate listing also found; original theorem PDF not obtained. |
| **UNREAD Kadish-Landsberg** | Round 5 search excerpt mentioning a generalized Foulkes map. Original PDF not read; no theorem used. |
| **UNREAD Landsberg survey** | Rounds 5 and 11 and references in HL/H2017. Search snippets only. Historical claims attributed to other authors were instead checked in primary papers. |
| **UNREAD EH1988 and FLR1985** | Bibliographic pointers inside H2017 §8.4. Original bounded-rank classifications were not read. The report relies on H2017's own Proposition 8.4.1, not on a claimed independent classification audit. |
| **UNREAD BIP / no occurrence obstructions** | Round 4 search abstract. Not imported into a multiplicity or small-size statement. |
| **UNREAD BIH / not via saturations** | Round 5 listing, round 8 search pointer and CIM bibliography. Not used for a multiplicity claim. |
| **UNREAD Cheung-Mkrtchyan, Hermite-Hadamard-Howe map report** | Round 5 excerpt; superseded for this audit by reading CIM2015's map and algorithm. |
| **UNREAD Domokos, Characteristic free description of semi-invariants of 2 x 2 matrices** | Repeated search hit in rounds 1, 3, 5, 8 and 10; original theorem not read. No size-two result transferred to size four. |
| **UNREAD Derksen-Weyman, On the Littlewood-Richardson polynomials** | Round 3 primary-PDF search excerpt; not read or used as a theorem. |
| **UNREAD The separating variety for matrix semi-invariants** | Round 5 search listing; not read. |

## Access and version notes

**READ (administrative):** the first sandboxed PDF download failed because sockets were denied. A narrowly scoped network escalation for the authorized temporary PDF downloads succeeded. No installation or persistent permission/configuration change was made.

**READ (administrative):** the Weyman-hosted DW2000 URL returned 404; the AMS PDF returned 403. The web-tool attempt to read Derksen's publication index returned 502, but a direct read of the same author page succeeded and yielded the usable PDF link. These are access failures, not missing mathematical statements. The DZ publisher page explicitly exposed subscription-only full text; no access-control workaround was attempted.

**READ (version control):** PDF banners were used to identify arXiv versions, rather than assuming the query result's date was the version date. SVB's regenerated PDF has an internal date different from its arXiv banner; both are recorded. LMR's author copy is identified as an undated eleven-page version by its hash. It is not silently equated with either arXiv or the journal typesetting.

**HAND (coverage):** the search includes a later SAGBI version and a later projective-limit paper, not only classical invariant theory. It does not certify that every later preprint, thesis or private construction was indexed. No theorem establishing a residual class-(iii) specialization was located. No novel specialization, contraction, search mechanism, rank experiment or proposed research programme was added.
