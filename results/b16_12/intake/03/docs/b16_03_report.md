# B16-03 delivery

**PASS:** exported and independently certified the degree-23 determinant
equation `c^23 S7`, highest weight `(61,15,2^8)`, with explicit polynomial
pole clearing and a fresh full-support padding nonzero
`-26743148924112014067635076791795712`.

The 10-by-10 integer padding map has determinant -248434 and c=2. Two fresh
Hessian calculations agree on the full polynomial. The exported recurrence
has only 194 terms across its binary-coefficient intermediates. Global
vanishing, polynomiality, and highest weight have universal proofs in
`docs/b16_03_proof.md`; sampled zeros are only controls.

**Finite comparison:** slot02's independently accepted a23=189, padding upper158,
and stable determinant ideal upper11 gives `D23<=-20`. Thus this finite cell
cannot give a positive gap under those inputs. The count is inherited here,
not independently recounted. The fresh equation gives q>=1 and padding r>=1;
equation separation alone is not a multiplicity obstruction.

Successful production/replay: 0.753/0.749 seconds, about 20 MiB peak Job
memory, exit0, under enforced60s/512MiB caps and one numerical thread.
The final portable receiver also passed in0.687seconds, peak Job19,832,832bytes.
Two initial fixture failures from a singular leading determinant matrix are
documented and their receipts preserved. No heavy lease held; all owned
numerical processes exited. Frozen worktree head unchanged; no Git mutation.

Deliverables: executable `analysis/b16_03_receiver.py` with
`analysis/b16_03_equation.py`; exact `results/b16_03/certificate.json`; proof,
input hashes, finite comparison, resource/release receipts, and a portable
receiver package under `delivery/b16_03/`.

Slot02's finite count has been independently accepted; this cell is excluded.
Any positive-gap search must use another nonexcluded finite cell and actual
global equation and padding image floors q,r satisfying q+r>a. No minimum
lift-degree or broader LMR novelty claim is made.
