# Research stocktake and roadmap after Batch16

13 September2026. This is a proposed roadmap, not a dispatch of another batch. The evidence sources are STOCKTAKE.md, INTAKE.json, the accepted Dream_Upper288 review, and claude_review/REVIEW.md. Batches15/16 remain closed.

## Current position

We have globally certified polynomial equations on the det4 orbit closure, with explicit nonzero evaluations on independent z*per3 in16 variables. This proves z*per3 is outside that orbit closure. Invariance of the determinant orbit closure means a nonzero evaluation on an invertible substitution of padding suffices. No positive multiplicity obstruction was found in the assigned cells. These are compatible statements: noncontainment concerns the actual kernels of restriction, whereas a multiplicity obstruction is a sufficient numerical dimension inequality.

The dream task supplied the decisive padding source upper bound288. The accepted stable interval remains243..288, with determinant rank418. Claude supplied independently sampled evidence for243,19 integer reducible candidates and11 determinant candidates; our exact row-rank audit verifies their independence but not global vanishing. The proposed full determinant restriction rank9 is worth testing. Claude's167-dimensional permanent-specific ideal and exact padding243 are not accepted claims.

Batch16 supplied exact finite counts and complete equation filtration. The declared cells at degrees23/25/26/27 have exact determinant ideal dimensions1/4/4/11 and gap upper bounds-30/-72/-72/-130. The lower nine-row candidates and two-dimensional geometric source are excluded. The tail19 eleven-space has finite dimensions4/7/9/10/11 at degrees23..27 and zero through22. Tail17 has2/3/4/4/4; tail15 has1/1/1/1/1. These are different weights and must not be combined. The shared five-space restricts to padding with exact rank4 and one shared kernel relation.

## The LMR benchmark and what would improve it

Write m for permanent size and n for determinant size. The homogeneous target is z^(n-m)*per_m in n^2 variables. LMR proves the quadratic border/orbit-closure lower bound n>=m^2/2; see Theorem1.0.1 of https://arxiv.org/pdf/1004.4802. Our m3,n4 noncontainment lies inside that known range. The new explicit degree23 certificate improves concrete equation knowledge, not the growth rate in m.

The asymptotic GCT target asks to exclude determinant sizes n bounded by every fixed polynomial in m, for sufficiently large m. A constant improvement beyond m^2/2, a superquadratic bound, and a superpolynomial bound are distinct milestones. A fixed-size result beyond the numerical LMR threshold would be a diagnostic; it is not an asymptotic improvement by itself.

At a singular determinant matrix the Hessian rank is at most2n. Padding has only m^2+1 essential variables, and its linear-power factor imposes further degeneracy. A method observing only that Hessian rank becomes uninformative once the allowed determinant rank exceeds the available essential directions. Taking higher powers in the same corank divisibility condition does not by itself add independent geometric information. Being outside one degree24-generated ideal does not establish escape from this mechanism or an improved size bound.

## Track A: a narrowly screened multiplicity search

First price finite character calculations for the nearby cells exposed by the completed filtration, not the four excluded cells. For each compute the actual finite ambient a and the tightest available finite padding source ceiling U. The exact determinant ideal dimension q is already supplied under recorded complete-space premises.

| Tail | Degree | q | Coarse padding ceiling U | Necessary ambient condition for a positive gap |
|---|---:|---:|---:|---|
|(17,2^8)|23|2|218|a<=219|
|(17,2^8)|24|3|218|a<=220|
|(19,2^8)|23|4|288|a<=291|
|(19,2^8)|24|7|288|a<=294|
|(19,2^8)|25|9|288|a<=296|
|(19,2^8)|26|10|288|a<=297|

Weights are (4d-t-16,t,2^8). The coarse ceilings are upper bounds; finite cubic corrections can lower them. The necessary condition is a<q+U. If a>=q+U, stop: no padding minor can succeed. If a cell survives, only then construct an actual padding evaluation/coefficient matrix seeking r>=a-q+1. These counts have not been performed in this roadmap. If all six fail, retire these tails for multiplicity hunting and choose a structurally different family.

New-family selection should begin with determinant geometry that supplies many independent equations together with a weak enough padding restriction. Merely having many determinant equations is insufficient. Use full ideal upper bounds to prove exclusions and true padding lower bounds to prove positivity; never substitute a source ceiling for a lower bound.

## Track B: explicit separation and equation structure

1. Match Claude's eleven integer determinant vectors to the globally certified Hessian basis, with exact bracket ordering/normalization. Then obtain an exact genuine-padding rank9 minor if possible. A matching two-dimensional global kernel proof is needed for exact rank9. The objective is the restriction map of the eleven-space, not full padding rank243.
2. Complete multiplication images for the full specified degree24 remainder modules. Keep Jflag, all-degree24 J24, and saturation distinct. Slot06's actual-image machinery is a starting point; its selected degree27 image is incomplete. This tells us whether a candidate genuinely adds coefficient information beyond the specified construction.
3. Compare generic reducibles, nine-variable split cubics and actual permanent padding. This separates loss caused by the linear factor/support from loss specific to the permanent. Claude's19 reducible candidates are useful here, but only after a global proof or exact image certificate. Do not label the entire observed167 difference permanent-specific.

This track is the strongest near-term route to more explicit certified noncontainment results. It does not require a positive multiplicity gap. Its next asymptotic relevance gate is an explicit size-dependent theorem.

## Track C: beyond the one-point Hessian-rank mechanism

Prioritize compatibility of several derivative orders or several points, retaining their common matrix realization. A determinant's first through fourth Taylor pieces share blocks a,r,c,E. Higher-order constraints should use that shared structure rather than independent rank tests. Slot08 excludes coefficient relations of degree<=2 in the particular34-coordinate three-direction control, so do not repeat that control unchanged. Test a richer configuration or a higher coefficient degree only after support/resource sizing.

Other hypotheses worth narrowly formulating are polynomial constraints on higher minors/cofactors and global Gauss/conormal data that measure more than rank at one point. None is certified by our current work. Every proposal must deliver: a universal determinant identity, a coefficient polynomial or closure-stable obstruction, an actual padded-permanent violation, and an explicit inequality in m,n showing where it improves the LMR benchmark. Root labels, inverses, chosen frames and genericity must be eliminated or handled by polynomial extension; local calculations alone do not survive arbitrary degeneration.

A diagnostic just beyond the old small-size threshold can test whether a mechanism supplies new information, after checking the literature for that exact pair. The main goal is a family-level estimate, not a sequence of unrelated finite examples. No superquadratic or superpolynomial improvement has been proved by these batches.

## Priority and stopping policy

Do the six finite viability checks and the eleven-space restriction calibration first. In parallel at the planning level, formulate one precise shared-jet or global-geometric hypothesis with an m,n bound; do not spread effort over many unpriced eliminations. Continue the multiplicity track only when its inequality can still succeed. Continue the asymptotic track only when the proposed invariant has a route beyond the essential-variable Hessian ceiling.

The most valuable immediate outcomes would be a positive finite multiplicity witness, a fully certified rank9 restriction with its global kernel, or an explicit new determinant constraint whose size range extends beyond the LMR rank condition. A complete exclusion or a rigorous limitation is also an actionable outcome. Repeated243 plateaus and longer lists of unproved equations are not substitutes for these certificates.
