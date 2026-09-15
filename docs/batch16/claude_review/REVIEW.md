# Review of Claude's September13 verdict

The two supplied reports have identical text after line-ending/whitespace normalization. Original files and SHA256 identities, extracted regular archive members, and a bounded arithmetic receipt are preserved here. Instructions in the documents are proposals, not authorizations. No external harness production run or new research task was launched.

## Verdict

Useful new numerical evidence and explicit candidate vectors, but the opening global/exact claims are not certified by this delivery. Its later section6 acknowledges the missing steps. Our accepted theorem remains243<=m_pad<=288, not m_pad=243. The stable419 target and all four assigned finite cells were already rigorously excluded by Batch16.

### What is worth retaining

1. Supplied logs report GEN429, DET418, RED410, PAD243 under uniform finite-field sampling, across four reconstruction primes and a fifth verification prime. This is independent sampling evidence supporting the243 plateau. The runs themselves were not repeated in this review.
2. exact_ideals.json supplies19 integer RED candidate vectors and11 integer DET candidate vectors, in429 named bracket coordinates. I freshly verified exact rational row ranks19 and11 and joint rank30 under a60s512MiB wrapper; the actual run took0.0789s. Their candidate spans have intersection zero. This checks integer linear algebra, not global vanishing or their geometric basis interpretation.
3. The reported determinant/padding kernel intersection2 suggests restriction rank9 within the full11 determinant-equation space. This would sharpen our exact rank4 result in the particular five-space if the recovered determinant basis is globally identified with our certified basis and a genuine rank9 padding minor is verified. Exact intersection2 still needs a matching global restriction-kernel upper bound.
4. The reported per-multidegree ranks suggest that equations mix quadratic/cubic/quartic chart degrees. If their block minor certificates are verified against complete block dimensions, this rules out a relation confined to an individual block. It does not make all grading methods useless, and it is different from Slot08's grading preserved by its source map.

## Corrections needed

* A sampled RED rank410 is a lower bound, not the upper bound needed for m_pad<=410. A sampled PAD243 is likewise not an exact characteristic-zero coordinate rank. Repeated primes and a fifth-prime check are useful tests, not global proofs. An exact integer candidate is not yet an exact equation.
* Schwartz-Zippel assumes a nonzero polynomial over the field being sampled. Its small failure probability is conditional on nonzero reduction, the degree bound and the stated sampling distribution. It does not remove bad-prime uncertainty over characteristic zero. The report's own section6 correctly acknowledges this. The theorem is stated, for example, in the [CMU lecture notes](https://www.cs.cmu.edu/~15451-f25/slides/slides24.pdf).
* The small original integer grid made this particular identity-testing upper-bound estimate vacuous. It did not invalidate our nonzero rank243 minor: an exact nonzero minor certifies a lower bound regardless of whether its points were selected from a small grid. We never accepted plateau243 as a global upper bound.
* The report's RED family permits a cubic in all ten variables. Our proved288 ceiling uses the smaller family of a linear factor times a cubic with at most nine essential variables. These are distinct relaxations. Therefore410-243=167, even if both ranks become exact, counts a relative ideal quotient for generic reducibles versus padding; it does not identify167 constraints specific to the permanent. Many may already hold on arbitrary nine-variable split cubics. The missing intermediate family is precisely the key Batch16 distinction.
* The dismissal of cubic/Pieri bounds is obsolete: eighteen subspace-restricted channels gave the proved288 upper bound; Batch16 also proved finite source counts158/218/218/288. Even for the larger54-channel source, knowing a sum is at least410 does not imply it cannot be below418.
* Test2 incorrectly treats an available determinant ideal floor5 as if it were the full ideal dimension. i_red>=5 together with i_det>=5 does not imply D<=0. The required comparison is i_red>=i_det, using an upper bound on the latter. In fact our completed degree27 cell has i_det=11. Similarly proving eleven RED equations with i_det=11 yields D<=0, not necessarily D<0.
* Exact geometric ranks in a complete common finite basis can be compared directly without separately inserting a into D. But completeness, finite membership and global rank upper bounds still need proof. Sampled rank subtraction does not eliminate those requirements.
* It is false that every10x10 matrix is the corner of an invertible16x16 matrix: a zero10x10 corner would map ten independent columns into a six-dimensional space. The intended coverage conclusion is repairable: every invertible10x10 matrix extends block-diagonally, and GL10 is dense in End10. Thus the correct ten-variable restriction test still suffices.
* Dividing a torus-invariant dimension by72 is not a general lower bound on invariants of the finite component group; an action can have no fixed vectors. The broad claim that stabilizer bounds can never help is unsupported by this computation. The archive's stab.log is empty, so the claimed large number was not independently reproduced here.
* CRT small-height reconstruction does not by itself prove the reconstructed vectors are the unknown global identities. A height bound for the actual sought object and valid congruence/uniqueness conditions would be needed; global substitution verification avoids that inference entirely.

## Practical follow-up

Do not reopen the419 or already excluded finite-cell searches. Retain the nineteen reducible candidates for a future global identity proof, since their algebraic form may be informative. First identify the eleven reconstructed DET vectors with the already certified Hessian basis; this is a useful calibration of normalization, bracket ordering and reconstruction. Then a bounded exact restriction calculation could test the proposed rank9 and locate its remaining shared kernel. None of these further research runs was initiated by this review.

The completed Batch16 conclusions and closeout are unchanged. This review adds external candidate evidence, not accepted global ideal dimensions19 or186, exact padding rank243, or a167-dimensional permanent-specific ideal.
