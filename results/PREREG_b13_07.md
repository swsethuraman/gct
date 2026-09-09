---
board_numbering: batch13
session_id: B13-07
model: gpt-6-astra
base_commit: 00495110c62acfbbbc951e82cc218ed091563b3f
---

# Independent S79 audit — preregistration

RECORDED, 2026-09-09, before audit computations. Work exclusively on branch
`b13-07` in the prepared B13-07 checkout. `HEAD` is the frozen base above;
this isolated checkout has no `main` ref. The user's frozen-base instruction
supersedes the preamble's fresh-clone and `main` instructions. No other session
is a dependency. No publication, push, or new schedule.

## Question and ordered objects

1. Reconstruct the five-variable permanent Jacobian at the s37 integer point
   (seed `20260902*1000+5`, box +/-1000000). Independently expand derivatives
   as the corresponding 2-by-2 permanents times a coordinate. Reproduce rank
   35 at both house primes and ship the integer point, Jacobian, pivot minor
   indices and residues. Cross-check by exact finite differences of cubic
   substitution. Prove shorter-weight inheritance explicitly; do not compute
   365 redundant restriction ranks.
2. Inventory the final S79 merged artefacts and manifest; check all shipped
   hashes and distinguish missing original transport bundle from present merged
   contents. Re-enumerate degree-nine plethysm by the exact symmetric-character
   route and verify the 331 length-six candidates, 210 positive weights, and
   shorter-weight count. Check every per-prime record, including the hybrid
   dimension/verification fields, separately from actual certificate replay.
   Replay all available degree-nine full-rank certificates, smallest first,
   checking every polynomial's weight, all raising images, and evaluations
   from integer pencils with no dropped terms. If full certificates are absent,
   list those requiring regeneration and do not call metadata replay an
   independent rank verification.
3. Audit all sixteen weight-13 stable blocks (five new plus eleven controls):
   re-enumerate source monomials, derive ambient multiplicities, rebuild raising
   images, evaluate actual traceless pencils by determinant expansion, and
   check ranks at both primes. Check a wrong-weight or deliberately altered
   vector fails. Explicitly justify characteristic-zero lifting using the
   degree-smaller-than-prime polynomial-representation argument, or leave that
   dependency unresolved. Audit Proposition S from the frozen proof.
4. Check every one of the 682 quartic records at both primes; separate full
   determinant ranks, full padded/reducible ranks, and sampled deficiencies.
   Inventory replay coverage and avoid promoting the 59 sampled drops to
   rational ideal membership. Keep D=mult_pad-mult_det.
5. Audit the epsilon_pad claim: inspect s74's integral source and transported
   values, reproduce the modular birth-coordinate statement if bounded, and
   decide whether an exact rational argument follows. A two-prime vanishing
   coefficient is insufficient. Seek a proof or give an explicit integer
   linear-algebra counterexample to that inference and the precise missing
   certificate. Preserve exact determinant rank 273, padded rank floor 269,
   and the unconditional formula D=1-i_pad(24), in [-4,+1].

## Bounds, controls, and stopping rules

One numerical worker, all BLAS/OpenMP thread counts set to one. Windows native
GlobalMemoryStatusEx preflight reports total physical memory 33752997888 bytes,
available 7445483520 bytes (about 6.93 GiB) at 15:07 UTC; measure again at every
launch. Use a Windows Job Object cap of 1.5 GiB per job, and do not start a
numerical job with less than 2 GiB available. Every launch writes its PID and
has a supervisor wall limit: dominance/inventory 300 s, census 1800 s, each
certificate 180 s, each stable block 900 s, epsilon matrix replay 600 s.
Whole run bounded by 2026-09-09 20:15 America/New_York to leave delivery time.
Bank completed units; output filenames all start b13_07 or are in
results/b13_07. No file over 5 MB will be committed.

Negative audit outcomes are a failed control, a hash mismatch, a missing
certificate, a timed/resource-limited replay, or a logical implication not
justified over Q. These are not evidence of a new ideal or obstruction.
At a potential positive obstruction or nonzero cubic ideal, stop broad work
and apply the board's full independent verification protocol before claiming it.

## Environment and fallback

RECORDED: bundled CPython exists at
`C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
NumPy is installed; python-flint, SymPy, SciPy, psutil, Singular, and msolve
were not found in the initial checks. A local-target pip installation of
python-flint/SymPy/SciPy/psutil was attempted and failed because host socket
access to PyPI is forbidden (WinError 10013). No approval escalation is
available. No global environment was changed. Bounded exact integer and
finite-field audit arithmetic will use the existing independent stdlib/NumPy
checkers or transparent stdlib arithmetic; this is a declared implementation
deviation from the preamble's python-flint preference, not a downgrade to
floating point or sampled membership. Large engine regeneration requiring the
unavailable dependencies will be priced and left as an explicit fallback.

Success is a claim-by-claim verified ledger with exact inherited dependencies.
Fallback is a verified prefix, a complete record/certificate inventory, and
specific certificates needing regeneration. The epsilon equality may remain
conditional. Delivery: report, manifest, banked commits, bundle against the
frozen base, part00 onward and whole/per-part MD5 and SHA256, with user copies
in `C:/Users/swami/Projects/gct-gpt/Batch13_Results/B13-07`.
