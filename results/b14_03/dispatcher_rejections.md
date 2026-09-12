# Verifier report

4 certificate file(s); verifier tools/verify at 2026-09-12 03:51:12 UTC
PASS 0, RECORDED 0, FAIL 1, UNPARSEABLE 3, ERROR 0

## FAIL — `results\b14_03\corrupted_entry_control.json`

*Complete h=1 interpolation with mixed source basis*  (5.1s)

- [x] strict required inputs and profile — {}
- [x] complete source over Q — {"weight_dimension": 561, "raising_rows": 1056, "ranks_mod_p": [559, 559], "dimension_Q": 2, "independent_exact_HWs": 2}
- [x] target dimension, bracket membership and full minor — {"upper_bound_proof": [{"nu": [8, 8, 2], "weight_dimension": 38, "raising_rows": 54, "ranks_mod_p": [37, 37]}], "dimension_Q": 1, "polynomial_terms": 1720, "minor_determinant": 209952, "entries": [[209952, 1143072]]}
- [ ] source_entries — integer source entry differs from exact polynomial evaluation

## UNPARSEABLE — `results\b14_03\missing_input_control.json`

*Complete h=1 interpolation with mixed source basis*  (0.0s)

- [ ] schema — certificate: missing=['points'], unknown=[]

## UNPARSEABLE — `results\b14_03\duplicate_key_control.json`

- [ ] CI input — duplicate JSON key: kind

## UNPARSEABLE — `results\b14_03\nonexistent_control.json`

- [ ] read/parse JSON — [Errno 2] No such file or directory: 'results/b14_03/nonexistent_control.json'
