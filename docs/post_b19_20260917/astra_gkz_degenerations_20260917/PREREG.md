# GKZ-organized determinant degenerations

Session: 17 September 2026. Status: working report; proof developed below, final verification pending.

## Incremental decision, after reading B17-02

B17-02 section 4 already proves the entire native-entry diagonal negative theorem proposed in the skeleton. This is a duplicate, not new progress. The selected route is now the larger five-block diagonal family in the fixed adapted coordinates (a,r,c,S,v). Its determinant support projects to five points (1,2),(0,2),(0,1),(1,0),(0,0), whose convex hull is a rectangle. The claim to prove is that all normalized interval tests for this family together are exactly the old skew-degree cut C, on the full source in every degree. Thus the comparison with (C,T) can be settled without knowing their combined rank.

Weights (A,R,Cs,s,vw) on these five blocks give beta=R+Cs+2s, u=A-R-Cs+s, h=vw-s. On every source monomial of degree 4d the weight is d*beta+u*alpha+h*nu, where alpha is its a-degree and nu its skew degree. Stabilizer symmetry gives 0<=alpha<=d, and C=0 gives 0<=nu<=2d. The determinant weights are beta plus u*alpha+h*nu on the five displayed points. This proves the proposed interval redundancy once the monomial and action conventions are checked.

Concrete candidate (already an actual coordinate substitution, no coefficientwise-orbit assumption): B(t)=[[a/t,r],[t*c,A(v)+t*S]]. Its determinant is

    a v^T S v - t (rv)(v^T c)
      + t^2 (a det S + r A(Sv)c) - t^3 r adj(S)c.

The endpoint a v^T S v is reducible, whereas the old endpoint a v^T S v-(rv)(v^T c) is irreducible (primitive linear polynomial in a). It is consequently not the old endpoint up to an invertible coordinate change. It is nevertheless a further face degeneration of that old endpoint; a distinct endpoint does not imply an independent test. Candidate source weight is 3d-alpha-nu, so its negative-weight test is alpha+nu>3d, already prohibited by C together with alpha<=d.

Pilot plan now fixed: one exact sparse check of the displayed expansion, all five block degrees, primitive block-weight reduction, and small-degree support-sum controls including corrupted-sign and non-source controls. Estimate <5 seconds and <64 MiB; wrapper caps remain 60 seconds / 512 MiB. No source-vector evaluation. The proof, not finite checks, will certify all degrees.

## Verdict and scope

Investigate the restricted family of diagonal weights in native matrix-entry coordinates. First prove the bridge to determinant orbit points. Test whether the resulting pole/forbidden-weight conditions are already forced by left-right stabilizer symmetry. If so, close this family with a rigorous negative result rather than attempt a larger fan or carrier search.

No positive multiplicity obstruction is claimed. The current five-row diagnostic has dim M = 5, E = span(e), and a = m_det = 1. The user-supplied updated status is rank T = 3 and 2 <= rank C <= 4. Older handoff ranks must be reconciled with finalized source-vector packets.

## Definitions and theorem target

W = Mat_4(C), phi(Y) = det(sum x_i Y_i). For integral weights w_ij, scale every matrix entry (Y_k)_ij by t^(w_ij), and normalize by the minimum permutation weight m(w). This is a linear coordinate transformation of W for t != 0. The target is an exact necessary regularity condition on homogeneous degree-4d source polynomials transforming by (det A det B)^d under left-right multiplication.

Proposed negative theorem to verify: every monomial of such a source has row and column counts d; hence its w-weight is at least d*m(w). If established, normalized entry-weight pole projections vanish on all M, with no comparison computation required.

## Plan, pricing, and stopping rules

1. Read finalized project inputs and the Segal survey; pin used files.
2. Prove orbit membership, normalization, finite combinatorial organization, and source condition.
3. Give an explicit arc and distinguish the normal fan of the determinant support polytope from the secondary fan and from initial ideals of orbit closures.
4. Prove redundancy or identify one missing certificate.
5. Seal output hashes after final review.

No workers, carrier search, direct-arc-relation experiment, or incidence/resultant programme. No historical edits, Git changes, shared ledger writes, or publication.

Resource contract: at most three computational pilots, each at most 60 seconds and 512 MiB; at most 180 seconds total; one child process and one BLAS thread. Read and inspect the existing Windows Job Object wrapper before any pilot. Preserve failures and receipts. First process inspection found no python/julia/sage/magma/wsl/maple/mathematica jobs. Exact process snapshot will be saved before a pilot.

Provisional pilot: a single small standard-library exact arithmetic check of a 24-term determinant expansion and a constructive matching decomposition, if useful; estimate <5 seconds, <64 MiB. Controls must include a non-source monomial violating the bound. Do not run until the construction and proof target are written. No unpriced elimination or secondary-fan enumeration. Stop computational work once the proof is settled.

## Provenance and input pins

Pending: finalized handoff; routeA sign-filter report and manifest; arc-target-dimension report and manifest; B17-02/B18-02/B19-01 arc reports and relevant scripts; geometric background; project resource and delivery guidance. No unfinished direct-relation outputs will be read.

## Exact degeneration framework and candidate

Pending.

## Necessary-condition proof and comparison

Pending.

## Literature, dependencies, pilots, and controls

Primary reading: Ed Segal, A short guide to GKZ, arXiv:2412.14748. Literature stays outside the delivery tree. Any load-bearing result beyond the survey will be proved here or verified in its primary source with exact hypotheses.

## Smallest next step

Pending verdict. If entry weights are universally redundant, stop this family; do not fund an enumeration.
