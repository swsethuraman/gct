---
board_numbering: batch13
session_id: B13-06
model: gpt-6-astra
reasoning_effort: xhigh
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-06
registered_at: 2026-09-09T11:13:00-04:00
---

# B13-06 preregistration: products of the LMR equation module

This is the single authorized run. Work and commands stay in the prepared
isolated checkout. The `main` ref is absent; the user-specified frozen base is
the recorded base instead. The automation configuration records the actual
session model `gpt-6-astra`, effort `xhigh`.

## Question and scope

Let A=Sym(Sym^4 V), E=S_(65,17,2^7)V be the one-copy LMR equation module
in I(det_4)_24, and J=(E). Enumerate the possible components of J_25 and
J_26 by the multiplication maps E tensor A_k -> A_(24+k), k=1,2.
Use stable polynomial representations (V of dimension 16); report separately
length 9, length 10, and length greater than 10. Nine-variable specialization
retains only length <=9; full padding has ten essential variables.

Success is the board's finite, justified list with explicit image-rank and
membership questions, including any rigorously closed components. A tensor
constituent is not assumed to survive polynomial multiplication. We will not
claim a positive gap without the full board verification protocol.

## Inputs read and controlling corrections

- Required five documents: worker preamble, controlling board, corrections,
  stocktake_batch12, brief_wording.
- docs/lmr_cell.md, docs/compact_circuit.md, docs/s74_final_review.md,
  docs/sparse_det_route.md; transport failures in stocktake_batch10 section 2
  and stocktake_batch11 section 5.
- results/s74/source.json; columns_det, columns_pad, columns_red at both house
  primes; decision files; certified.json; results/s63_aladder.json.
- analysis/wk12_int_s74_final.py and wk12_s74_decide.py for stored-value
  interpretation; their overstatements about rational kernel containment are
  explicitly NOT adopted.

The source is integral bracket fillings. Values at degree d are native values
times msym_u^(d-rung), with msym_u=24*c_(4,0,...,0). Keep original point data
and u-values with any transported certificate. Preserve rank(det)=273 exactly,
rank(pad)>=269, D=mult_pad-mult_det=1-i_pad(24), and [-4,+1]. Neither the
measured reducible nullity five nor modular birth-coordinate vanishing is a
rational membership statement.

The board names conceptual inputs rather than exact paths or ambient variable
count. The paths above resolve that ambiguity from the existing repository;
the stable/9/10-variable split makes the chosen scope explicit.

## Computation registered before execution

1. Exact horizontal-strip enumeration for E tensor S_4. For degree two use
   Sym^2(Sym^4)=S_8+S_(6,2)+S_(4,4) and Jacobi--Trudi/Pieri differences.
   Independently verify all resulting coefficients by LR skew-tableau
   enumeration (at most eight new boxes), and Weyl dimension identities at
   r=9,10,11,16. Retain zero channels in the audit, not in the live list.
2. Validate the symmetric-square identity by direct degree-two monomial
   characters. Give explicit coefficient HWVs of weights (8),(6,2),(4,4),
   verify their raising derivatives over Z, and nonzero evaluations. Complete
   a small multiplication control that exhibits both surviving components and
   syzygies (Sym^4 tensor Sym^4 -> Sym^2 Sym^4).
3. Prove the Cartan u and u^2 transport limitation using saturation
   a_24=a_infinity=274 and the integral-domain coordinate rings. Audit the
   banked saturation inputs. Do not assume i_pad(23)=i_pad(24).
4. Replay stored LMR determinant/padded/reducible minors at both house primes
   if python-flint becomes available. Recompute every u from its integer point,
   and degree-25/26 transported minors. Independently combine determinant
   columns with padded/reducible columns to test intersection zero without
   pretending to rationally reconstruct the determinant vector. If the mandated
   rank dependency is unavailable, preserve these checks as ADOPTED inputs and
   deliver exact decomposition/proofs instead; do not relabel a missing import
   as a mathematical negative.
5. Price every support cell using exact dimensions and explicit matrix-shape
   formulas; no full A_25/A_26 basis or huge Schur module is materialized.
   Formulate product image B, structural restriction S, and padded restriction
   T and their rank thresholds. Degree-25/26 non-Cartan ranks remain open
   unless actually computed. No new determinant size or replication operator.

Any additional measurement requires a dated committed addendum. The exact
finite enumeration, controls, proofs, and per-component rank questions are the
primary board success; full non-Cartan rank measurements are beyond this run.

## Resources and stopping rules

Windows, Python 3.12.14 from bundled runtime. numpy installed; python-flint,
sympy, scipy, psutil absent; Singular and msolve not on PATH. Local pip install
attempts for python-flint and sympy/scipy returned no matching distribution;
none installed. No shared runtime changes. Pure Python integers/Fraction suffice
for the registered combinatorics and exact polynomial controls.

GlobalMemoryStatusEx: total physical 33,752,997,888 bytes; available
7,429,640,192 bytes at preflight. CIM memory query was denied; native API worked.
Use at most one numerical worker; OPENBLAS_NUM_THREADS, MKL_NUM_THREADS,
OMP_NUM_THREADS, NUMEXPR_NUM_THREADS all 1. Each computation is launched with
a Windows Job Object memory ceiling of 768 MiB and a watchdog wall bound
(maximum 1,200 seconds per unit). Record PID and resource outcome in
results/logs/b13_06_<unit>.*. A failed memory/wall bound is a cost boundary,
not evidence about ideals. Exact combinatorics should be far below this cap.

Bank preregistration first, then each completed object/unit. No file over 5 MB
is committed. Deliver report, manifest, replay scripts, bundle against the
frozen base and part00-based whole/part checksums under Batch13_Results/B13-06.
No pushes, publication, or further schedules. Aim to finish well before 20:30
America/New_York on 2026-09-09.
