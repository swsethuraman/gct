"""Read-only mathematical audit of supplied integer candidates; no harness execution."""
from pathlib import Path
import json,hashlib,tarfile,shutil
from flint import fmpz_mat
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SRC=Path('C:/Users/swami/Downloads')
names=['claude_sept13.txt','session_b15_padding_verdict.md','exact_ideals.json','b15_verdict_harness.tar.gz']
pins=[]
for n in names:
    raw=(SRC/n).read_bytes();(OUT/n).write_bytes(raw)
    pins.append(dict(name=n,sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
with tarfile.open(SRC/names[-1]) as t:
    for m in t.getmembers():
        p=Path(m.name)
        assert m.isfile() and len(p.parts)==1 and not p.is_absolute(),m.name
        d=OUT/'harness'/p;d.parent.mkdir(exist_ok=True);d.write_bytes(t.extractfile(m).read())
j=json.loads((OUT/'exact_ideals.json').read_text())
assert len(j['basis_bracket_indices'])==len(set(j['basis_bracket_indices']))==429
assert all(0<=x<1019 for x in j['basis_bracket_indices'])
A=j['I_red'];B=j['I_det'];assert all(len(r)==429 for r in A+B)
ra=fmpz_mat(A).rank();rb=fmpz_mat(B).rank();rab=fmpz_mat(A+B).rank()
result=dict(status='EXACT_CANDIDATE_LINEAR_ALGEBRA_ONLY',candidate_ranks={'RED':ra,'DET':rb,'joint':rab},candidate_span_intersection=ra+rb-rab,max_entries={'RED':max(abs(x) for r in A for x in r),'DET':max(abs(x) for r in B for x in r)},inputs=pins,scope='Exact integer row independence only. No global vanishing, geometry, modular-run reproduction, CRT uniqueness bound or full padded rank accepted. Original harness retained but not executed.')
(OUT/'arithmetic_review.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
