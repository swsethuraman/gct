# Citation register

Primary texts inspected online on 13 September 2026. Links below are the sources actually checked; no external scripts were downloaded or executed. Mathematical scope and conventions are discussed in DREAM_REPORT.md. This is a targeted literature check, not a claim of exhaustive novelty review.

| Key | Primary source and version | Checked location |
|---|---|---|
| BLMW | Peter Bürgisser, J. M. Landsberg, Laurent Manivel, Jerzy Weyman, *An overview of mathematical issues arising in the geometric complexity theory approach to VP vs. VNP*, [arXiv:0907.2850v2](https://arxiv.org/pdf/0907.2850v2) | §4.1; §5.2, especially (5.2.1)–(5.2.7) and Proposition 5.2.1. |
| LMR | J. M. Landsberg, Laurent Manivel, Nicolas Ressayre, *Hypersurfaces with degenerate duals and the geometric complexity theory program*, [arXiv:1004.4802v1](https://arxiv.org/pdf/1004.4802) | Theorems 1.0.1–1.0.3. |
| KL | Harlan Kadish, J. M. Landsberg, *Padded polynomials, their cousins, and geometric complexity theory*, [arXiv:1204.4693v1](https://arxiv.org/pdf/1204.4693) | Theorems 1.2, 1.3, 1.7; Propositions 1.8, 1.12. |
| BIP | Peter Bürgisser, Christian Ikenmeyer, Greta Panova, *No occurrence obstructions in geometric complexity theory*, [arXiv:1604.06431v3](https://arxiv.org/html/1604.06431v3) | Definition (1.2), Theorem 1.4, Proposition 2.4 and its proof in §6(a). |
| IP | Christian Ikenmeyer, Greta Panova, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory*, [arXiv:1512.03798](https://arxiv.org/pdf/1512.03798) | Theorem 1.6; Corollary 1.9; Appendix 7, Claim 7.1. |
| M | Laurent Manivel, *On rectangular Kronecker coefficients*, [arXiv:0907.3351v1](https://arxiv.org/pdf/0907.3351) | Theorem 1 and its proof. |
| DIP | Julian Dörfler, Christian Ikenmeyer, Greta Panova, *On geometric complexity theory: Multiplicity obstructions are stronger than occurrence obstructions*, [arXiv:1901.04576v1](https://arxiv.org/html/1901.04576v1) | Theorem 2.3, including the distinction between its family and its two finite occurrence-free settings. |
| LR | J. M. Landsberg, Nicolas Ressayre, *Permanent v. determinant: an exponential lower bound assuming symmetry and a potential path towards Valiant's conjecture*, [author-hosted 22-page manuscript](https://people.tamu.edu/~jml/LRpermdet8-4.pdf) | Definitions 1.2–1.5, Theorems 2.1, 2.8, 2.13–2.14. |

## Scope reminders for reviewers

* BLMW uses a covariant space for forms in the cited section. Our report instead uses forms on V, so coordinate modules are S_λV and the orbit fixed space is (S_λV*)^H.
* BIP's displayed padded permanent uses X11, an internal variable. Its length bound is consequently m². Independent padding uses m²+1; an asymptotic comparison of complexity models is not a fixed-cell identification.
* IP's connected-Kronecker degree gate is distinct from a gate for symmetric Kronecker coefficients. The latter includes a separate transpose action.
* KL normalization/source descriptions must not be read as equality with the coordinate image of actual permanent padding.
* LR imposes symmetry on a determinantal realization. DIP compares different varieties. Neither supplies an unrestricted permanent-versus-determinant multiplicity witness here.

## Project inputs

Read in this order: `../COMMON_CONTEXT.md`, `../../../Batch16/STOCKTAKE.md`, `../../../Batch16/ROADMAP_AFTER_DREAM_CLAUDE.md`, and `../../../Batch16/claude_review/REVIEW.md` (paths relative to the Astra folder). All numerical Batch16 premises remain inherited. The planning report neither promotes sampled plateau claims nor reruns closed workers.

The input hashes and the inspected wrapper hash are saved in `REVIEW_MANIFEST.json`. Exact symbolic calculations and the reproducible local command are in `TOY_CALCULATIONS.md`.
