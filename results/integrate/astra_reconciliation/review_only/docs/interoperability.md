# Astra / Claude interoperability contract

Use the same integration commit and repository-relative inputs. Model identity belongs in provenance, never in the mathematical API. Resolve Python through configuration/PATH; do not copy a producer's absolute Linux or Windows path. Record Python, NumPy, SciPy, python-flint and compiler versions. Linux shell wrappers and Windows Job Object wrappers are host-specific; mathematical modules should remain portable.

Shared interface requirements:

- Cell key: polynomial degree n, coefficient degree delta, descending partition with trailing zero padding removed. Validate sum(lambda)=n*delta. Ambient variable count is separate metadata.
- Record actual exponent tuples and their ordering. Do not exchange anonymous coefficient arrays. Ordinary coefficients c_alpha and factorial coefficients m_alpha=alpha!c_alpha require explicit conversion.
- Each evaluation records family, integer point recipe, prime, source basis identity, and native versus transported values. S74 transport uses (24*c_(4,0,...))^(target_degree-native_degree).
- Retain rational identities, modular rank floors, producer full-rank claims, independent replay status, missing certificates and inherited theorems as distinct fields. A deficient sample never supplies a rational ideal-dimension lower bound.
- A compact operator has narrower storage dtypes. Its consumer must explicitly support those dtypes; return-shape compatibility alone is insufficient.

Reusable modules now present:

| Function | Module | Acceptance boundary |
|---|---|---|
| Exact expanded-polynomial membership | analysis/b13_03_exact.py | Small exact controls; target circuit conversion missing |
| Retained structural restriction | analysis/b13_02* | Check exact entry point and conventions in its report |
| Lean raising operator / safe consumer | analysis/wk13_b10_lean.py | 20 producer comparison cells; large pilot |
| Wide modular multiplication | analysis/wk13_b08_per6_lean.py | Above-guard producer controls; integrate with lean consumer |
| Higher-length cubic driver | analysis/b13_09_per_r.py | Higher-length controls and run records |
| Frozen legacy ledger | analysis/b13_11_ledger.py | Preserve legacy API and immutable baseline tests |

Production integration gate: run one small exact operator comparison, one known deficient control, one length-7/8 positive cell, one product exceeding the 2^21 arithmetic guard, and one a=0 complete-cover control. Check all generated raising targets, kernel verification and identical evaluations. Measure peak memory for the combined path. These tests have NOT yet been run as one combined production implementation.

Do not overwrite frozen certificates or resource logs during replay. Use isolated output directories. Never have two workers write the same result file or Git index concurrently. Preserve explicit failed/interrupted states. Export compact certificates where possible; record regeneration requirements otherwise.
