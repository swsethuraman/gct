# BIB — bibliography by read-status (the record's labels)

Slot B23-04; brought current by slot B24-03 on 2026-09-20. Categories follow gate G14 as refined
by G14′ (B21-10 §7, `f7727cb7`):

- **PRIMARY**: the record says the primary text was read, and names the file and hash.
- **SECONDARY**: quoted through a programme note or another text. Not read in the primary.
- **UNREAD-CLASSICAL**: stated in three or more standard sources. The claim is ADOPTED-classical,
  and the citation number is a convenience.
- **UNREAD-SPECIALIST**: unread. Any claim resting on it is CONDITIONAL.

The draft prints each item's status at every point of citation, through `\lit{key}{status}`. The
bibliography inside `det4-blindness.tex` is grouped under the same four headings. Nothing is cited
"quietly". Bibliographic fields are only those the record carries. Missing fields are listed in
GAPS G-25 and are not filled from memory.

**One item now carries three different read-statuses at three different points of use.** That is
not an inconsistency: LMR is cited for three distinct statements, one of which has been read at
the source and two of which have not, and G14′ attaches read-status to the *use*, not to the
paper. The LMR row below prints all three, and the draft prints the relevant one at each point of
citation. **A reader who takes "LMR is PRIMARY" from one point of use and carries it to another
will over-read the record**, which is exactly the failure this file exists to prevent.

**Changes in the 2026-09-20 pass:** Landsberg arXiv:1305.7387 added under PRIMARY (it is now
load-bearing in two places); the LMR row rewritten to separate its three uses; the Kleiman row's
"used in" column updated for the enlarged scope of row 1; Hilbert--Burch/Eagon--Northcott and the
classical inputs of the `D45 ∩ P5` classification added under UNREAD-CLASSICAL.

**Changes in the 2026-09-21 pass (slot B25-01):** LMR use (iii) now PRIMARY, on B24-02b's
committed reading, with the Thm. 1.0.2 warning and the (★) qualifier; the cap theorem's three
inputs (Dimca, Gulliksen–Negård, Kleiman) re-described as ADOPTED inputs of a theorem that is
PROVED modulo them, their own read-statuses unchanged; Kleiman removed from row 1 of the kill
table. No new source was read by this slot.

## PRIMARY

| key | item | read-status evidence | used in draft | load-bearing? |
|---|---|---|---|---|
| `Dimca13` | A. Dimca, *Syzygies of Jacobian ideals and defects of linear systems*, Bull. Math. Soc. Sci. Math. Roumanie 56(104) (2013), 191–203; arXiv:1210.1795v4 | PDF sha256 `20b96f5830291574…`, re-fetched byte-identical by B21-10 (R17). Remarks 3.5–3.6 read through the arXiv HTML rendering. **PRIMARY at statement level.** Theorem 3.1 used by B22-10 S18 | C11 (cap theorem's Dimca input), C34 (re-derivation of the `n = 3` instance) | Yes, as one of the cap theorem's three named ADOPTED inputs (the theorem is PROVED modulo them, B24-10 11.5.10 @ `ab2f8a40`; ⟳ 2026-09-21, was "for the cap theorem as ADOPTED"). For C34's instance it is the reviewer's second derivation. |
| `EH` | Eisenbud, Harris, *Vector spaces of matrices of low rank*, Adv. Math. 70 (1988), 135–155 | Scan sha256 `6b10d8fea80396a7c833…`, pp. 135–141 transcribed from page images (singular-locus REPORT §1). **PRIMARY at statement level. The proofs in EH §3 are unread by anyone** (B20-10 R11, honest negative 2) | C28 (condition C1) | Yes. `ρ_Z = 0` is CONDITIONAL on it. |
| `LLV` | "LLV", arXiv:2303.09028v3 (authors and title not on the record, G-25) | PDF sha256 `67b1701f761d4336…`. Theorem 2 (five prime divisors; `deg F1 = 320112`; others 136512, 38475, 2508, 320), Cor. 3.1, Prop. 1.1 and the table row `F1 (5,5,5,5)(6,6,6,6)` read in the text extraction (B20-10 R13). CONDITIONAL lifted | C07, C08, C25 | Yes (C08, C25). |
| `Landsberg13` | J. M. Landsberg, *Geometric complexity theory: an introduction for geometers*, arXiv:1305.7387v3 | **PRIMARY**, via the ar5iv rendering. Read by B23-06 (PDF v3 sha256 `cdcaaab95e9e4053…`) and **independently re-fetched and re-read by B23-10** (§5.3, hash in its manifest); the two fetches of the rendering agree. §2 read for "it is known … that `5 <= dc̄(per_3) <= dc(per_3) <= 7`" and "Problem 2.4. Determine `dc̄(per_3)`", and for the polynomials `P_{Λ,m}` with `dc̄(P_{Λ,m}) = m < dc(P_{Λ,m})` | C50 (the `dc`/`dc̄` distinction behind the LMR frontier); the boundary question G-33 (limits of determinantal expressions that are not determinantal) | **Yes, in two places.** It is why `(3,5)` and `(3,6)` are open *at the orbit-closure level* rather than settled, and why "`D45°` is closed" is not to be assumed. Honest negative carried from B23-10: the rendering was read, not the PDF bytes; the PDF hash pins the version only |
| `Segal` | E. Segal, *A short guide to GKZ*, arXiv:2412.14748v1 (19 Dec 2024) | PDF sha256 `8c8d9d058c878e77…`, read in full by the GKZ and Astra packets (B20-10 §4) | C24 (context only) | No: "a dependency map, not an invocation of unverified machinery". |

## SECONDARY

| key | item | route | used in draft | load-bearing? |
|---|---|---|---|---|
| `Fulton` | W. Fulton, refined Bézout inequality: *Introduction to Intersection Theory in Algebraic Geometry*, CBMS 54 (AMS, 1984), Prop. 2.3; also cited as *Intersection Theory*, 2nd ed. (Springer, 1998), Ex. 8.4.6 | Secondary only, through the quotation in Sharir–Solomon arXiv:1411.0777v2 Thm. 2.2 (hashed `0741e2d2…4589`, B18-01 R2). The Ex. 8.4.6 numbering is **not confirmed** (B18-01 R2; B20-10 R14) | C06, C07 | Yes, for the upper end `4^49` only. CONDITIONAL. |
| `GN` | T. H. Gulliksen, O. G. Negård, *Un complexe résolvant pour certains idéaux déterminantiels*, C. R. Acad. Sci. Paris 274 (1972), 16–18 | "ADOPTED exactly as in `onset_conjecture.md` §2 (not re-fetched)" (B20-10 R15) | C11, C19 | Yes: cap theorem (PROVED modulo this and two other named ADOPTED inputs; ⟳ 2026-09-21); GKZ Thm. A. |
| `Kleiman` | S. L. Kleiman, *The transversality of a general translate*, Compositio Math. 28 (1974), 287–297 | Same secondary route (B20-10 R15) | C11; **C18 and C48 (`N = 5`, `k >= 7` only)** | Yes: the cap theorem (PROVED modulo this and two other named ADOPTED inputs; ⟳ 2026-09-21); GKZ Thm. B at `k >= 7`, whose own label is unchanged. **⟳ 2026-09-21: no longer an input to row 1 of the kill table anywhere**: B24-02.1 @ `f8273c3b` proves the `N = 5` rank inequality on elementary premises (C48). *The 2026-09-20 text follows.* It was then the **only** adopted input anywhere in row 1 of the kill table. **⟳ 2026-09-20:** row 1's kill at `N = 6, 7, 8` (C47) is proved **without** Kleiman, so its load has shrunk to the single point `N = 5`, `k >= 7`; the GKZ corrigendum C2's wording is "Kleiman remains the only adopted input for `k >= 7`". An uncommitted Batch-24 pilot reports even that discharged (GAPS G-30) — since committed and applied. Kleiman is also ADOPTED for the `j >= N−3` zero-ideal statement at `N = 6, 7` (C23) |
| `Teissier` | Teissier, class formula for hypersurfaces with isolated singularities (reference not on the record, G-25) | B22-02 L9: "SECONDARY/UNREAD, illustrative"; B20-02 §4: "SECONDARY, UNREAD; illustrative only" | C29 (class 68) | No. Row 4's kill is stated "given the two class values". |

## UNREAD-CLASSICAL

| key | item | label source | used in draft |
|---|---|---|---|
| `BH` (Cor. 2.1.4) | Bruns, Herzog, *Cohen–Macaulay Rings*, CUP 1993 (Cambridge Stud. Adv. Math. 39): **(T2)** grade = height in a Cohen–Macaulay ring | B21-10 R15: UNREAD-CLASSICAL, condition KEPT, exposure nil | C20 (Thm. 6.4 CONDITIONAL on it alone) |
| `BH` (Prop. 1.5.12) | same book: an ideal of grade `g` generated by forms of one degree contains a regular sequence of `g` general linear combinations | B21-10 R16: UNREAD-CLASSICAL; **the fact is proved independently** in B21-10 §3.2, Step 1 | C18 (GKZ Thm. B(iii)) |
| — | Hilbert–Mumford criterion; Bertini; Cramer's rule and Plücker coordinates; the plethysm/Kostka row bound (`h_4^e` has constituents of length `<= e`) | B22-02 §5 literature paragraph; B22-10 §5 table | C15, C16, C17 |
| — | Cauchy decomposition; Plücker generation (FFT for `SL_5`); complete reducibility of `L × T_ad` in characteristic 0; FFT for `SL_3`; Jacobi–Trudi; the Weyl character formula for `GL_3` | B22-10 §2.4 table ("UNREAD-CLASSICAL, label affirmed") | C41 (Theorem M) |
| — | **Hilbert–Burch, in the Eagon–Northcott form for a `3 × 4` matrix** (the complex is exact exactly when `grade I_3(B) = 2`); `grade = height` in a Cohen–Macaulay ring; Lefschetz for divisors on a smooth cubic threefold; upper semicontinuity of fibre dimension | B23-02 §1.1, §5 literature paragraph @ `68866e6d`; reviewer B23-10 §5.4 | C49 (row 10 restated as `ker φ*`) |
| — | **Jacobi's formula** `d(det) = tr(adj · dA)`; **Gauss's lemma** (rank-one factorisation over a UFD); Koszul relations of a regular pair; intersection numbers on `P^1 × P^1`; "a generic line meets a quadric in two points"; lower semicontinuity of rank; closedness of images of projective morphisms; Bézout for two plane conics; **Hilbert functions of zero-dimensional schemes** (length `L` imposes `L` conditions in degree `>= L − 1`) **and of curves**; the affine dimension inequality for intersections | B23-03 §5 literature paragraph @ `3bcad666`; reviewer B23-10 §3.4 (READ, affirmed) | C36 (the classification), C37 (Prop. 2.5), G-33's dimension floor `>= 19`. The two Hilbert-function facts are used **only** in the proof that `T1 ⊄ T2`, and B23-03 flags them as such |

## UNREAD-SPECIALIST

| key | item | record status | used in draft | effect |
|---|---|---|---|---|
| `Ballico` | Ballico, *Vector spaces of matrices of low rank and vector bundles on projective spaces: An addendum to a paper by Eisenbud and Harris*, Beitr. Algebra Geom. 36 (1995), 119–122 (Zbl 0828.14009) | **UNREAD by anyone.** Three fetch routes failed (B20-10 §4.2, R12). Classified UNREAD-SPECIALIST by B21-10 G14′ | C28 (condition C3) | `ρ_Z = 0` is CONDITIONAL. |
| `BH16` | Bruns, Herzog, *op. cit.*: Thm. 1.6.16 (cited by Dimca Remark 3.6) and Thm. 1.6.17 (T1), in particular its **nonvanishing half** | Unread. The numbers are unreconciled and neither is verified (B21-10 R17). The vanishing half of (T1) is LIFTED by B21-10's own proof (R14). Two corroborating sources fall short of G14′'s three, so the item is placed here conservatively | C21 (the "strictly more homology" sentence only) | That sentence is CONDITIONAL. |
| `LMR` | J. M. Landsberg, L. Manivel, N. Ressayre, *Hypersurfaces with degenerate duals and the geometric complexity theory program*, Comment. Math. Helv. 88 (2013), 469–484; arXiv:1004.4802v1 | **Three uses, three statuses. (i) Thm. 1.0.1**, `dc̄(per_m) >= m²/2`: **PRIMARY** (B23-06, via ar5iv; PDF v1 sha256 `cfc28275a8c6b27f…`). **(ii) The dual-defect statistic:** UNREAD-SPECIALIST and *not* load-bearing, since C31 is self-contained (B22-02 §5). **(iii) The base-rung floor `i_det((19,7,2⁵),12) >= 1`: ⟳ 2026-09-21 PRIMARY** (B24-02b @ `5a97317e`: PDF v1 re-fetched, sha256 `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79`, identical to `results/b23_06/MANIFEST.json` @ `feed104e`; v1 the only version; text read via ar5iv, sha256 `fb5844ad…`; Thm. 2.3.1, §3.1 with Thm. 3.1.1, and §3.2 with its printed `n = 3` instance read; **proofs not audited**; passages quoted in `results/b24_02b/lmr_quotes.md`). *Was: no read-status anywhere on the committed record.* This slot did not itself re-fetch or re-read the PDF; it consumed B24-02b's committed quotations | (i) C50; (ii) C29, C31; (iii) **C45** | **(i) Yes**, for the frontier `n <= m²/2` and its boundary precision. **(ii) No.** **(iii) Yes, decisively** — it carries the *sign* of the programme's only positive result, not a refinement. **Cite Thm. 2.3.1 with §§3.1–3.2, never Thm. 1.0.2** (printed `ω_1` coefficient and degree both halved and mutually inconsistent; it gives `(13,7,2⁵)` at degree 6). Only the **floor** is taken from LMR; the ceiling is the record's own nullity, and LMR's "only one copy" (asserted without printed proof) is not used. The `C⁹ → C⁷` transfer is the record's length-restriction lemma (formerly "(★)"), not LMR's. **⟳ 2026-09-22:** that lemma is **PROVED** (B25-05 Lemma R @ `2688efd1`, reviewed B25-10 §2.4 @ `42e7f4ba`; GAPS G-37 CLOSED), so C45 is **PROVED**, with LMR Thm. 2.3.1 + §3.1 its one PRIMARY external input; LMR is still not cited for "only one copy". *The 2026-09-20 text said this was reported by an uncommitted half-slot and not cited; that is now history (GAPS G-31, disposition).* |
| `CG` | Clemens, Griffiths: intermediate Jacobian of the cubic threefold (reference not on the record) | B22-02 §5: UNREAD-SPECIALIST, a non-candidate, not load-bearing | C30 caption | None. |
| `Paper1` | S. Sethuraman, *Conductors of orbit closures, and the fundamental invariant of the 3×3 determinant* (paper 1 of this programme; `paper/det3-conductor.tex`) | B22-12 §3: the `δ_0` bracket's source "paper 1" is **UNREAD** (ADOPTED record-internal) | C12 | The `δ_0` bracket stays ADOPTED. Placed here because the record marks it unread, not because it is specialist. |

## On the record but not cited in the draft

These are listed so that no reader thinks they were overlooked. The draft makes no claim that
rests on them.

| item | record status | why not cited |
|---|---|---|
| Atkinson, *Primitive spaces of matrices of bounded rank II*, J. Austral. Math. Soc. 34 (1983) | UNREAD/POINTER, corroborative only (B20-10 §4). This predates G14′, so it has no CLASSICAL/SPECIALIST split | The draft follows the brief and says nothing about the classification of `D45 ∩ P5` beyond "OPEN". |
| Huang–Landsberg, *On linear spaces of matrices of bounded rank*, arXiv:2306.14428v1 | read through arXiv HTML, not hashed; "no result of this paper is load-bearing" | Not needed. |
| Domokos–Zubkov / Derksen–Weyman / Schofield–Van den Bergh (FFT for `SL_4 × SL_4` on `(Mat_4)^5`) | SECONDARY (B20-10 §4) | Used only in a check the singular-locus theorem does not need. |
| HMSV Lemma 6.6 | UNREAD/POINTER; the fact is the classical `O_n` odd-part rule (B20-10 §4) | The 2+2 partial-transpose family is not cited. |
| Marcus–May / Botta (stabiliser of `per_3`) | ADOPTED (`PROVED.md` `orbit_stabiliser_silent`) | Not needed. |
| Bürgisser–Ikenmeyer–Panova; Kadish–Landsberg | in `paper/det4-onset.tex`; no label in the Batch 20–22 record | Not needed. |
