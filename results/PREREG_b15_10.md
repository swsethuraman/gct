# B15-10 preregistration

Model for proof, code, numerical controls, and delivery: gpt-6-astra; requested
reasoning xhigh. No additional agents. Existing branch b15-10-portable-witness,
existing checkout work/batch15_workers/B15-10. HEAD and annotated base resolve to
f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd; tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1. All three matched before work.
Native READINESS.md was read. Existing runtime PID/resource records are setup
provenance and will remain separate from the research commits.

## Question and conventions

For n=4, coefficient degree delta=8, ambient space of quartics in 16 variables,
and lambda=(12,4,4,4,4,4), construct rational/integral highest-weight polynomials
that evaluate nontrivially on explicit integer det4 pencils. Six-variable
restrictions are points in the orbit closure; coordinate-ring multiplicities
use Sym^8(Sym^4 V), with covariant coefficient-function weights. Polynomial
coefficients are ordinary coefficients c_alpha unless a factorial conversion
is explicitly written. No modular kernel vector is presumed to lift.

Inherited bounds are a=4 and h_pad=1 from the accepted Q1 record. Here a is
ambient multiplicity, i_X ideal multiplicity, m_X=a-i_X coordinate
multiplicity, and h_pad is the pullback upper bound. Thus U_pad=1. A freshly
checked r_det>=1 suffices for D=m_pad-m_det<=0; four independent determinant
evaluations plus one independent padded evaluation would give D=-3. Stable
sample deficiencies never give global ideal lower bounds. True padded points
are substitutions into z*per3 with ten independently available source
variables. The scoped exclusion ledger and accepted overlay already close Q1;
this task improves the evidence rather than opening a new cell.

## Method and controls

First replay a small banked integral highest-weight witness in a compact
format. Then seek direct symbolic brackets with four columns of height six
and eight singleton boxes, eight quartic letters of valence four. A particularly
small candidate is the six-letter fourth-power determinant bracket times
c_(4,0,0,0,0,0)^2. Its weight is (12,4^5). Prove the symbolic construction is
highest weight over Q before using residues, preserving the exact polarization
factors. Sparse determinant pencils, including skew-symmetric pencils whose
determinants are squares of quadratic forms, are valid candidate points.

Use subset dynamic programming or sparse contraction, count states and
transitions before allocation, and impose explicit expansion bounds. Broaden
to other column-incidence patterns only after the first candidate is checked.
Do not rebuild the 753,614,285-byte operator to establish rank one. If a full
four-direction source remains too costly, deliver the exclusion with the full
rank result explicitly RECORDED and identify the remaining witness.

Positive controls: a separate known nonzero polynomial/family; independently
expanded small examples; agreement of direct permutation and optimized
contractions where affordable; exact determinant coefficients from explicit
integer points. Negative controls: zero/diagonal degenerate points, changed
normalization, changed source/sign data, changed point or claimed minor, and
corrupted certificate rejection. The research evaluation itself may be zero.
Receiver replay must regenerate polynomials/values from source and points,
not merely eliminate a stored matrix. No cleanup of caller output directories.

## Resources and decisions

The lease record was read: holders 01 and 02; slot10 has no heavy lease.
Proof, code, sizing and small controls may proceed. Small controls use the
tested b15_bound.py runner, at most 60 seconds and 512 MiB, one process and one
BLAS thread. Any heavy pilot requires an integrator lease before launch; its
maximum is 900 seconds and 1536 MiB. A measured pilot may justify a production
attempt at most 5400 seconds under the same aggregate cap. Use only the local
absolute .venv/python.exe. A missing dependency triggers an explicit alternate
method decision, not a false mathematical conclusion.

Return EXACT for an integral identity/nonzero integer; REPLAYED_RANK_FLOOR for
a valid source evaluated modulo a justified prime; RECORDED for inherited
outcomes; CANDIDATE for unresolved evidence; RESOURCE_STOP for bounded stops.
Store native source constructions, explicit points, normalization, input
hashes, replay command, return code, wall time, and aggregate peak memory.
Every tracked file stays below 5,000,000 bytes. Shared records remain untouched.

## Input SHA-256 (exact working-file bytes, including line endings)

| Path | SHA-256 |
|---|---|
| docs/batch15/WORKER_PREAMBLE.md | 9946cbeba95c3b53e0da6322b92b874c3e69ab8c5314d98c27d70a7285778703 |
| docs/batch15/ACCEPTED_STATE.md | 9805ecc550bae5dbdfe845e280f42a0c2b03e0b6989e819e5a3d93e62f59148c |
| docs/batch15/briefs/B15-10.md | e9b0af4bce2573636e5eb42de53326cf003065bb6f89cbd9206aed5ff88076bf |
| docs/brief_wording.md | 0f3c6dbb15920aa25d52676cb638004d7bc989c22f9d88fe584ff36a5317cf5a |
| analysis/b14_12_cell.py | 87270f2417fd40cabab9e64ff6e272b3a44ca21c333d49a23122affb1f9c783f |
| analysis/b14_12_families.py | fa2a8c229ea61440ad57d0a451546c26b0483dce220dec70f8518317770cd1c4 |
| results/b14_12/b14_12.json | 47c876deaf5b7f2851f49d07d1f61a64d4b25a69c40da1f823e0c7ceb3e7f06b |
| results/b15_prep/Q1_combined_bound.json | 3d1fa35e56869fd614fa4193b67a9a46a17226f091a1f6a7fcce27f2a4c6e8c8 |
| results/b14_10/replacement_map.json | 0eab1448538dc53654d9bf494a92b1dbfa694e82fd6c81f1912f161557214347 |
| analysis/b14_06_bracket.py | d67a78c39694b1d4229970fd1bec46213913935030afcfae5165d2697d68b493 |
| results/integrate/inherited_exclusions.json | b71469d2d3db97e4d16f6b9b4be6f77ac1cfc00ea286b2e9cedefcec43b1458b |
| results/b15_prep/transport_overlay.json | b594dcdae7b4b448039d705d6f15f319e245a0d2cf3636f8b08b15cbfc42b4df |

The source conventions and tiny formats in the named banked files retain their
original attribution, including Claude's bracket code. New implementation and
proof will identify which premises are inherited and which are checked here.
