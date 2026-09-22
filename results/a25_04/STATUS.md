# A25-04 status

UNCOMMITTED / NOT RELEASED. Producer-only. No delivery commit.

- Start checkpoint: 2026-09-21T03:27:11Z. Theory selection began with required-input reading.
- Mechanism frozen by: 2026-09-21T03:29:36Z, under 3 minutes after that checkpoint.
- Fixed object: N=5, j=1, k=3; M=d_1^(3): C^5 -> S_3, 35 by 5. Ten bordered 2-minors m_ij from rows x1^3,x1^2*x_(i+1), columns 1,j+1, 1<=i<=j<=4; use symmetry to form a 4 by 4 matrix m.
- Fixed mechanism: the determinant trace-pairing factorization of these minors, testing h0=det(m) and polynomial relations in the ten generators. Proposed closure: a polynomial section makes their determinant image all A^10, so no nonzero relation exists. No other matrix or mechanism will be pursued after closure.
- Initial proof direction: m_ij(phi(B))=-4 tr(W_i W_j), where W_i=adj(B1)B_(i+1)-(tr(adj(B1)B_(i+1))/4)I4. Four arbitrary Gram vectors in sl4 do not have a forced dependence; four explicit hyperbolic pairs give a section.
- Preregistered controls: a determinant with m=-4I4; actual padding from z=x1 and permanent of [[x1+x5,x2,x3],[x2,x1-x5,x4],[x3,x4,x1]], with m=diag(8,8,8,-8); pure power m=0. All will be hand derived, not run.
- Source integrity: prior 15+14 payload hashes checked against their manifests; A25-01/02 remain provisional. Committed source bindings freshly resolved through the shared object store. SOURCE_BINDINGS.json records exact bytes and states.
- Pilots: 0. No shared lease acquired or modified. No mathematical program, agent, extra task, Git mutation, paper edit, publication, or tool memory.
- State at initial write: proof and packet preparation in progress.
- Outcome fixed by 2026-09-21T03:33:27Z: outcome (3), a scoped no-go. The polynomial section is proved; h0 has exact determinant value 256 and actual-padding value -4096, so its padding nonvanishing is not separation. No different mechanism was pursued.
- Final local state: COMPLETE / UNCOMMITTED / NOT RELEASED. Full proof, six-exclusion audit, source records, zero-pilot receipt and exact delivery list prepared. Administrative seal time and payload hashes are in MANIFEST.json. Independent review and G29 delivery remain open; no scientific premise is left conditional in the producer proof.
