# B16-12 receipt of accepted slot02 finite census

Delivered by the integrator at `Batch16/reviews/02`; received after the initial B16-12 proof review. All earlier statements that a23/a25/a26/a27 were unknown are superseded by this receipt. Slots03–08 remain undelivered.

**Verdict: the finite-character proof and exclusion deductions pass independent mathematical review.** Slot12 inherits the numeric counts from slot02 and its integrator's independent regeneration; slot12 does not run another count production. The executable B16-12 receiver checks every delivery artifact hash, the finite correction carriers, all four degree/weight identities and exclusion arithmetic, and records fresh/inherited boundaries.

## Independent check of the finite-stability proof

Let tau have size n. Extract the first-variable weight in Sym^d(Sym^4(V)). Separate the weight-zero generator, tail-linear generators, and b factors of tail degrees2,3,4 whose combined tail weight is m. Write their Schur-positive character as G_(b,m). The first-variable roots in the Weyl denominator contribute sum_k (-1)^k e_k x0^-k. This requires L-k tail-linear factors where L=n-m, and the finite factor bound is L-k<=D=d-b. The remaining multiplier is therefore

    H_(L,D)=sum_(0<=k<=L, L-k<=D) (-1)^k e_k h_(L-k).

The sign follows directly from product(1-y_i/x0); it is not the opposite Borel denominator. Complete cancellation gives H=0 for 0<L<=D. For L>D>=0, the hook identity gives

    H=(-1)^(L-D) s_(D+1,1^(L-D-1)).

For example, L=D+1 gives -h_L, confirming the material boundary sign. In finite residual dimension an overly tall hook is zero, which only removes corrections. A nonzero correction requires m>=2b and n-m>d-b, so b<=n-d-1. Its first row therefore satisfies d-b+1>=2d-n+2. If this exceeds tau_1, every Schur constituent of G times the hook is too wide to equal tau, by containment in the Littlewood–Richardson rule. All finite corrections vanish. The remaining L=0 terms are exactly the stable symmetric algebra in degrees2,3,4; the stated inequality also puts all relevant b within the finite factor allowance.

The hypothesis holds in all four requested cells. The minimum possible correction first rows are17,19,21,21 against tail first rows15,17,17,19. The receiver enumerates the small correction carrier list (b,m,L,D,first row,height), retaining it as arithmetic, but imports or executes neither slot02 count producer nor receiver.

## Geometric transfer and exclusion

Equal dimensions alone would not transfer ideals between unrelated vector spaces. Here the required additional premise is the inherited compatible chart inclusion A_d subset A_inf with I_X(d)=A_d intersect K_X, for both varieties. Under that premise, equality of the ambient dimensions implies A_d=A_inf and transfers all the relevant ideal/coordinate multiplicities. This is the point to retain in any use of the degree27 eleven-space conclusion. It gives existence of polynomial lifts at that degree but does not construct them.

For lower tails the full ideal upper11 is inherited via injective multiplication by the nonzero same-row s2 multiplier into tail19. It is an upper bound on the entire determinant ideal, not merely the known eleven-space. The padding ceilings come from the ring-map/chart proof reviewed independently by slot12. Hence

    i_pad>=a-h,  i_det<=11,  D<=11+h-a.

| degree | weight | exact ambient a | padding coordinate ceiling h | D upper |
|---:|---|---:|---:|---:|
|23|(61,15,2^8)|189|158|-20|
|25|(67,17,2^8)|294|218|-65|
|26|(71,17,2^8)|294|218|-65|
|27|(73,19,2^8)|429|288|-130|

These are genuine exclusions under named inherited premises. They do not follow just from q+r<=a. No positive certificate compatible with those premises can occur in these cells. At degree27 the full inherited stable interval transfers: i_det=11, m_det=418, 243<=m_pad<=288, -175<=D<=-130. Additional explicit finite lifts remain useful certificates; rank hunting in these excluded cells is not warranted.

## Snapshot provenance qualification

The integrator ran the slot02 receiver inside the snapshot. Its inspected source writes `results/b16_02/receiver.json`, and the wrapper writes the same-named resource receipt. Thus these two paths may contain the integrator's fresh replay bytes rather than the original bytes in INPUT_DELIVERY_MANIFEST.json. The B16-12 receiver treats only those two paths as refreshable, verifies the original worker copies against the manifest, and checks that the receiver's only payload change is elapsed_seconds. It checks the new resource receipt's integrator label, successful exit, single worker/thread, Job Object and caps. Every other mismatch is fatal. The output binds actual bytes for all versions read and lists every discrepancy; it does not say that all current snapshot bytes match the original delivery manifest.

This provenance qualification does not change the mathematical counts. No files in the slot02 snapshot or worktree were modified. The remaining inputs03–08 need their own exact delivered versions and scoped review.
