---
board_numbering: batch13
session_id: B13-02
model: gpt-6-astra
base: 00495110c62acfbbbc951e82cc218ed091563b3f
---

# Structural restriction preregistration

Recorded 2026-09-09, before mathematical measurements. This single execution
uses only the prepared branch b13-02. `main` is absent in this isolated checkout;
HEAD is the authorized frozen base above. No clone or other session is needed.

Question: can the integral 274-row s74 source yield an exact reducible
restriction rank at most 273? Adopt the certified determinant rank 273 and
padded floor 269; preserve D=mult_pad-mult_det=1-i_pad(24). No sampled kernel
or modular rank drop establishes rational ideal membership.

Inputs read: batch13_worker_preamble, batch13_board (B13-02 controls),
batch13_corrections, stocktake_batch12, brief_wording; batch11_plan C3;
s74_final_review (subject to corrections); s74/source.json;
S4/S4_report.md, its src/s4.py and src/calibrate.py, exact control artifacts;
docs/s_split.md and the coefficient/circuit implementations they identify.
The S4 archive omits its inputs directory and run.ps1: its replay command is
not directly runnable here. Use its retained mathematical artifacts directly.

Instrument: ordinary coefficient pullback c_alpha -> sum_i y_i d_(alpha-e_i),
or house symbols m4_alpha -> sum_i alpha_i y_i m3_(alpha-e_i). On highest-weight
vectors use the kernel-equivalent fixed factor x1: c_alpha -> d_(alpha-e1)
if alpha1>0, zero otherwise. Resolve exponent indices from explicit orderings.
Construct the literal transported 274-source restriction as an exact contraction
circuit and extract actual integer coefficient matrices, with exact monomial
keys and no hash merging. This is S in an injective codomain realization on its
image, not a claimed numeric 521-coordinate Pieri conversion.

Units and gates, banked as completed:

1. Audit all source filling incidences, degrees, and u transport. Recompute
   ranks/minors from inherited value data only if python-flint becomes available;
   otherwise retain them as adopted independently verified evidence.
2. Exact small controls: full symbolic pullback and fixed-factor restriction for
   S4's (8,8,8),d6 two-vector source; also a tiny literal bracket source and a
   full-rank control. Check all raising equations over Z and compare coefficients
   to the general pullback. No characteristic-zero conclusion from modular zeros.
3. Verify the 48 Pieri indices and attempt a fresh exact cubic multiplicity count
   (521 is not assumed verified). Permit 600 seconds/768 MiB for initial count;
   continue only with a priced, committed addendum if needed.
4. LMR pilot: exact coefficient extraction after x1 fixation, first on the two
   rung-12 rows and then representative native rows at rungs 13,14,24, extending
   to all 274 only if controls and cost gates permit. Deterministic coefficient
   choices, selected before inspecting their values, may be chosen from valid
   weight monomials with small support; the choices and seeds are retained.
   Cap each coefficient job at 120 seconds and 250,000 stored states; cap each
   completed symbolic polynomial at 200,000 terms. Total pilot at most 40 minutes.
   Retain exact partial matrices and resumable unfinished objects.
5. If a kernel candidate is found, only an exact zero of the complete pullback
   plus a nonzero rational source witness counts as an identity. An upper bound
   below 269 is an instrument failure. No Q stage is planned; if Q is used,
   first reproduce s74's 144/144 S4 cross-check at both house primes.

Success: exact rank S<=273 and hence D<=0, consistent with 269<=rank S<=274
and rank S<=521. Stretch: exact rank S=269. Negative/fallback: exact controls,
the actual full-source restriction circuit, completed coefficient submatrices,
supported candidate coordinates if available, and the smallest unresolved
symbolic calculation priced from the pilot. A partial matrix supplies only a
rank floor. Do not identify degree-23 and degree-24 padded nullities.

Runtime: Windows; actual model gpt-6-astra (Astra), no delegated agents. One
numerical worker, OPENBLAS/OMP/MKL/NUMEXPR threads=1. Initial physical memory
33,752,997,888 bytes, available 7,561,863,168 bytes. Use a Windows Job Object
process memory cap 768 MiB and an external parent timeout with recorded child
PID; no name-based process selection. A failed cap setup prevents computation.

Python 3.12.14 and NumPy are available. flint, sympy, scipy, psutil, Singular,
msolve and a PATH C compiler were not initially available. Attempted isolated
pip install of python-flint/sympy/scipy/psutil failed: PyPI socket access denied
(WinError 10013). No local wheel was found. Do exact polynomial arithmetic
with Python integers; do not replace the required flint rank engine with an
unreported substitute. Explicit tiny determinants may serve as replay witnesses.

Deliver report, manifest, own-branch commits and bundle against the frozen base.
Parts start part00; whole and per-part MD5 and SHA256 use bare filenames.
User-facing copies: Batch13_Results/B13-02. End before 20:30 America/New_York.
