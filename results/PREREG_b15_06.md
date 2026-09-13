# B15-06 preregistration

Model for reasoning, implementation, and review: gpt-6-astra, xhigh, as assigned
to this native task. Banked B14-06 mathematics and code retain their Claude
Opus 5 attribution. No additional agents are used.

Readiness: native READINESS.md reports successful setup. Fresh Git reads match
base commit f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd, and annotated tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1. Work remains in the existing
B15-06 checkout on b15-06-fresh-tails. Setup runtime logs are preserved and
excluded from research staging. This file is the first research commit.

## Question and conventions

For n=4, r=7,8,9,10, t=3,5,...,21, count the stable multiplicity a_inf of
tail (t,2^(r-2)) in Sym(Sym^2+Sym^3+Sym^4)(Q^(r-1)). The conservative stable
coefficient degree is delta=|tail|; lambda=(4delta-|tail|,tail).
The ambient comparison is in sixteen variables, specialized to r variables
by polynomial-functor inheritance. D=m_pad-m_det=i_det-i_pad.
The stable points are characteristic coefficients of traceless 4-by-4 pencils
for DET, and normalized/depressed quartics for PAD/RED. PAD means independent
z*per3 pulled back by an explicit ten-by-r integer matrix, with rank ten
required for the r=10 full-support control. No nine-variable exclusion applies.

## Algorithms, bounds, and selection

Recompute exact stable dimensions using B14-04's rational power-sum exponential
recurrence and Murnaghan-Nakayama characters, extending through weight 37.
Validate small cases by explicit plethysm products and character orthogonality;
compare stable tails (17,2^7)=274 and (19,2^7)=392 with the banked exact values.
Retain reproducible recurrence and per-cycle signed sums. No modular count is
called exact without an integer bound; the primary census uses Q throughout.
Apply the scoped exclusion ledger and accepted transport overlay, inventory
historical full-rank witnesses and B13-06 components, and distinguish inherited
premises from fresh arithmetic. Record i_pad_lb and U_pad=min(a,h_pad_ub,
a-i_pad_lb,other proved upper bounds); unknown h is null, never zero.
Transport the three degree-13 equations only where a justified product reaches
the specified weight. Do not add overlapping product images.

Rank at most three unexcluded pilots, with a_inf<=533 and validated r, by
evidence for a determinant deficit relative to U_pad, then manageable source
size. The nine-row t=17,19 families are already closed in the overlay ranges;
nine-row t=21 is reserved to B15-05. Prefer an independently justified candidate
over the number of product channels. Record selection before geometry.

Use B14-06 integral/rational bracket constructions with two epsilon columns,
preserving factorials, signs, degree valences, and matrix orientation. Extend
the evaluator factorial list beyond 8! and replace hard-coded point dimensions
in a per-slot adapter, with explicit shape validation. Keep source bracket
indices, integer point parameters, interpolation seeds, primes and values.
Denominators are invertible at both house primes 2147483647 and 2147483629;
nonzero modular minors certify rational rank floors without source lifting.

## Controls and decisions

Before research geometry: compare direct epsilon contractions in small dimension;
test peaked-tail liveness at each r; compare traceless DET jets to normalized,
depressed shifted determinant quartics; test Euler identities and nonzero c;
verify full ten-variable padding by exact rank and direct polynomial values.
Alter signs, factorial normalization, source or point data and require the
corresponding check to detect a difference. Empty inputs fail.

For each pilot use independent generic and determinant batches, both primes,
and padded points when needed to judge the gap. Deficient sampled ranks remain
CANDIDATE. A stable full determinant rank implies i_det_inf=0, and by the ideal
filtration i_det(delta)=0 at every valid rung. A stable deficient floor gives
i_det(delta)<=a_inf-r_det; combine it with finite-rung padded ideal floors, not
with an unjustified transfer of coordinate multiplicities. Positive D needs
global i_det_lb plus padded rank r_pad with i_det_lb+r_pad>a at the same cell.
No positive claim follows from stable sampled kernels. Record zero ranks too.

## Resources and delivery

Use exactly C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06/.venv/python.exe.
The native bounded runtime control is inherited setup evidence. Small research
controls/counts initially have a 60-second, 512-MiB aggregate envelope through
analysis/b15_bound.py; one process and one BLAS thread. Check free RAM at launch.
If counting exceeds that envelope, retain the partial output and request a lease.
No heavy lease is held: LEASES.json lists 01 and 02. Request one in this task
after code, sizing, and small controls. Heavy pilot: <=900 seconds and 1536 MiB;
extend only from measured cost with integrator authorization, <=5400 seconds.

Stop on a failed convention control, cap, scope conflict, or unresolved extension;
deliver the exact census and validated small extension control independently.
Save return codes, elapsed time, aggregate memory, replay commands, hashes and
all outcomes in docs/b15_06_report.md, docs/b15_06_proved.md and results/b15_06/.
Propose exclusions only in results/b15_06/proposed_exclusions.json. Commit only
intended per-slot files with model attribution; run the Batch15 delivery check
and package helper into a fresh delivery/b15_06_final directory. No push.

## Input hashes

The following SHA-256 values normalize CRLF to LF for UTF-8 text and preserve
binary files exactly. They are appended before this preregistration is committed.

| Input | SHA-256 |
|---|---|
| docs/batch15/WORKER_PREAMBLE.md | b41ab684785ad4be1fa91ec491c25c10fa463c0bdf2d5bb69b3e59e2abf6797d |
| docs/batch15/ACCEPTED_STATE.md | 97b07d5f50c21fc6a3a6bba267339ba385dcda0b6bad7a067c5905b1351352df |
| docs/batch15/briefs/B15-06.md | df220ad684c15cce9774d358163c342b477c15c17b3344ceb67b7014fdc859bc |
| docs/brief_wording.md | f5ca5b747543254bca82f74daf0088e443400922c9a216768175be399218e0b8 |
| docs/s57_report.md | 8a685ba2f5423863c5d9db6b2f7f1216b20468b87b1af6b6697ca052f4ac35c9 |
| analysis/b14_04/recount.py | 884586a57411c53ff2e3f8992642be85976bf7907f33acd05ea5cf405394e0b3 |
| analysis/b14_06_bracket.py | bb5e8a2d5f5c9550c560695eb17b4da5875a3cb8fbe5e4eb0b0df8b937467eea |
| analysis/b14_06_points.py | 78fbacf60394ecd8696d7e38a8cfbdcef92c662524e487ef23b46be084bb9398 |
| results/b15_prep/transport_overlay.json | e8f2d129c60eaf36e0ec6644b5e9f706a6c540cc85a8329f17bcdc0c8ba6c007 |
| results/integrate/inherited_exclusions.json | bfdf6bf971e192723bb48c9c9be4cf00f32ecb0f05647f4df790858145edb338 |
| tools/integrate/exclusion_predicates.py | e5addf6e749ce129db4bb8308d72aadb0984852e64d12957a92f131b0b76776f |
| results/b13_06/components.json | 7c3da281675271a34404db5b61a60a660c61b405fb8606357544aed137077a3b |
| results/s57_cells/stable_a.jsonl | 499e8c626d0b96955ab990f7aeda494fa61066b082c3fdd6d305f1f0266f119d |
| results/b14_04/stable_summary.json | 692ff9711b04fd29efa1a6305ab8515b2234a72ff6c1bd3c01e74271aff91e1d |
| analysis/wk8_s30_pleth.py | 55ae352881aa9447a9b29e89300105530764ca251c8e571602bc55186f547f41 |
| analysis/b15_bound.py | 1f73ad8de393238165443862d028057a2dd75e4b5753afd6bf3192a71b7d5df2 |
