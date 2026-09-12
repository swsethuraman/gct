# B14-04 preregistration

Committed before new mathematical measurements. UTC date: 2026-09-12.
board_numbering: batch14. Actual model: gpt-6-astra (Codex); launch requests xhigh reasoning. No model change or delegated agent is used.
Branch: b14-04-astra. Frozen base: 9898e56941a7665f231873481dae956f08509995.
Frozen tree: cb688cd3fe454d638f3202e759e2eaa0c629739f.
Both git log -1 --format=%H batch14-base and git log -1 --format=%T batch14-base match. Initial HEAD equals base, working tree clean. No applicable AGENTS.md found in the worktree or ancestor paths.

## Question, prior observations, objects

Formalise and control the already observed character recounts dim N13=73 and dim N14=159, then independently compute a_inf(19,2^7)=392 and a_inf(21,2^7)=533 by symmetric-group characters, not Weyl weight counting. 73/159 are OBSERVED PILOTS, never blind predictions. 392/533 are RECORDED expectations from the scratch Weyl route; no new independent stable measurements yet. Control a_inf(17,2^7)=274 and small banked stable tails (6,3,3,1)=4 and (5,2,2,2,2)=4 when within budget.

Inputs are hashed in results/b14_04/input_manifest.json using frozen Git blobs (authoritative across line endings) and working-file SHA256. Complete mandatory board, index, wording, reconciliation, memo, s57 proof and assignment inputs read. Scratch scripts inspected as historical evidence only; none will be imported or run. No a_weyl or amb calls.

## Instrument and conventions

Work over Q with arbitrary-precision integers and fractions. h_d=sum_{rho|-d} p_rho/z_rho; <p_rho,s_lambda>=chi_lambda(rho). p_r[h_j]=sum_{sigma|-j} p_{r sigma}/z_sigma, so cubic coefficients are 1/6,1/2,1/3. Use banked wk8_s30_pleth.pleth_p and chi after controls. Enumerate horizontal strips freshly via lambda_i >= mu_i >= lambda_(i+1), sum(mu)=3d. N_d is the weight-lambda HWV multiplicity of Sym^d(V) tensor Sym^d(Sym^3(V)), V of dimension >=9. This is a normalization target dimension, not padded coordinate-ring multiplicity or source rank.

Stable F(t)=exp(L(t)), L=sum_{j in {2,3,4},r>=1} t^(jr) p_r[h_j]/r. Compute F_0=1 and n F_n=sum_{m=1}^n m L_m F_(n-m) sparsely; pair F_33,F_35 with the length-eight tails. This is a genuinely different method from the scratch weight-space DP and Weyl alternation. Save each requested complete power-sum expansion with exact coefficients and character values. Save signed subtotal decomposition by cycle length as a resumable fallback. Optionally refine by generator multidegree only if core finishes cheaply; preregister later refinements before measuring.

values_are: exact power-sum coefficients and unscaled integer symmetric-group character values; scalar products are exact multiplicities. No evaluation matrices: matrix orientation is not applicable. Downstream source vectors would be rows, points columns and relations columns of K satisfying A^T K=0. Natural common integral model: polynomial symmetric powers over Z, symmetric functions embedded in Q[p_1,p_2,...]. Check all denominator primes before using either house prime 2147483647 or 2147483629. No rank or modular kernel conclusion is drawn here.

## Validation and falsifiers

1. Check MN identity character against hook-length dimensions; orthogonality over all partitions at small n (through 7), trivial/sign characters and conjugation.
2. Check h_2[h_2]=s_4+s_22 and h_2[h_3]=s_6+s_42; reject intentionally altered cubic normalization. Validate stable low degrees against independent finite product of pleth_p factors, plus the small banked stable values.
3. Require every strip key exactly once; compare all 15/27 pilot channels partition by partition and degree13 against B13-01. Empty/missing/duplicate/altered channel input MUST be rejected. Mutation tests must execute failing assertions, not report vacuous success.
4. Stable expansions must have homogeneous degree, nonnegative rational coefficients, denominator dividing n!, z_rho times coefficient integral and nonnegative, and exact integral/nonnegative final scalar product. Check identity-cycle value against counts of set partitions into blocks of sizes 2,3,4. Recompute generating-function coefficients at both house primes with separately implemented modular arithmetic and compare all saved rational coefficients after denominator checks. Corrupt coefficient/character/value and incomplete artifacts must fail verifier.
5. Record completed vs partial explicitly. Never PASS a missing input. If control fails, halt dependent arithmetic and diagnose; any changed measurement plan requires a committed dated addendum.

## Resources and stopping rules

Windows 11 build 26200, Python 3.12.14 at C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe; numpy 2.3.5 present, not needed by new arithmetic. No dependencies installed; psutil absent. Win32 GlobalMemoryStatusEx measured RAM 33,752,997,888 bytes, available 12,873,416,704 bytes; os.cpu_count()=20. CIM queries denied; Win32 query succeeded.

One computation worker at once, OMP/OPENBLAS/MKL/NUMEXPR threads=1, no parallel agents. Enforce 1024 MiB process commit memory at launch using a Windows Job Object, and wall-clock timeout via supervisor; logs and recorded PIDs under results/logs/b14_04_*. Cooperative checkpoints precede expensive stages. Controls 120s, each hpad 180s, stable generation+three tails 600s, verifier 600s. If a hard cap is reached, retain completed outputs and report RESOURCE_STOPPED with precise completed degree/remaining cycle classes. Never relaunch the same failed budget unbounded. Plan at most 30 minutes of heavy computation total including an optional improved bounded attempt after an addendum.

Before stable expansion, estimate p(n), number of recurrence multiply-adds and conservative sparse-storage cost through n=35. If estimated memory exceeds the cap, use degree/channel partial results. A completed scalar product is PROVED/CERTIFIED by its exact replay only after validation. Timings are MEASURED. Identification with stable ambient dimensions uses s57 Proposition S (proof reviewed, not a new geometry result).

## Decision table and delivery

All controls and all terms agree: certify normalization dimensions and stable symmetric-function multiplicities, retaining original lineage labels. Disagreement: record exact discrepancies, do not choose the expected value. Resource limit: exact partial decomposition and costed remaining bottleneck. No computations of 390/391/532 or finite rung28 are funded. No equation, ideal upper bound, i_red value, or new D conclusion follows from these dimensions alone: frozen a24=274, det rank273, padded rank>=269, D in [-4,+1] remains.

Deliver docs/b14_04_report.md, reproducible scripts, exact compressed certificates, validation/resource logs and replay instructions. Append only proved/certified appropriately scoped entries if justified. Preserve all four protected files and repository configuration. Commit only session outputs with Co-Authored-By: GPT-6 Astra <noreply@openai.com>. Run delivery checker before and after a NAMED b14-04-astra bundle against the captured base; deliver report, replay, manifest, verification logs and whole/part MD5+SHA256 bare-filename sidecars to C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04. No push, integration merge, other-session writes or recurring work.
