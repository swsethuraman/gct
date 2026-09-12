# B14-11 — protected-file audit for the integrator

**RECORDED / NEEDS INTEGRATOR EDIT.** The packet reserves these files for the
integrator. B14-11 has not changed them. The line numbers below refer to frozen
base `9898e56941a7665f231873481dae956f08509995`. These findings are part of the
audit, so the delivery does not claim that every historical sentence is repaired.

1. **`paper/det4-onset.tex:692`**, theorem `thm:slab`, and its introductory
   summary at line 197. The theorem states that the determinant multiplicity
   equals the ambient plethysm at length at most four **in every degree**.
   Its proof immediately acknowledges the length-four hypersurface and then
   refers only to the degrees computed. This does not prove the universal
   assertion and is inconsistent with the nonempty hypersurface ideal.
   Replace the all-degree conclusion by `mult_pad<=mult_det` from
   `n4_gate_containment`; restrict any ambient-equality claim to explicitly
   certified degrees and labels. This is the most consequential pending edit.
2. **`paper/det4-onset.tex:774`**, the unpadded positive-control discussion.
   Its reason that BIP closes occurrence obstructions in the padded regime
   needs the explicit range `n>=m^25`. The cited unpadded `n=3` control and
   the project's `(4,3)` padded comparison are outside that theorem's regime.
   Keep the correct positive multiplicities; remove the small-parameter BIP
   justification. The gate remark at lines 729–736 already makes the correct
   distinction and should be the wording used throughout.
3. **`paper/det4-onset.tex:715`**, the no-arithmetic-obstruction conclusion:
   append “in the enumerated range.” A silent stabiliser upper-bound screen
   does not settle all degrees or prove nonvanishing on determinant closures.
4. **`paper/det4-onset.tex:77` and `:203`** describe numerical agreement as
   extending the BIP phenomenon to small parameters. Label it as measured
   agreement on the stated finite region, not an extension of the theorem.
5. **`docs/boundary_deficit.html:115`–`:116`** uses an unqualified “no occurrence
   obstructions” slogan in a conceptual analogy. Add the asymptotic BIP range
   if this is retained as programme guidance. This is no machine exclusion.
6. **`paper/det3-conductor.tex:100`–`:101`** discusses BIP as background for
   the asymptotic GCT programme. No concrete A1 exclusion is applied there;
   an explicit asymptotic-range qualification would prevent re-use at `(4,3)`.

**REVIEWED, no correction requested.** `PROJECT_NOTES.md:145` describes the
unpadded example as a multiplicity obstruction with both multiplicities
positive; it supplies no BIP-based A1 exclusion. The bibliography references
in the protected files are ordinary source citations. None was altered.
