from pathlib import Path
import json,hashlib,shutil
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/'Batch16'
ledger=json.loads((B/'INTAKE.json').read_text());now=datetime.now(timezone.utc).isoformat()
rows=[
('01','Exact finite cubic source dimensions158/218/218/288; explicit finite ideal injections into degree35 upper11. These do not give exact padding image ranks.','Integrator proof review and fresh bounded receiver:235 direct controls, dual character computations,4 mutations;2.0792s. Transport replay0.0431s.23 delivery hashes verified.','Accepted degree35 ideal upper11 and product/subspace geometry.'),
('03','Global polynomial c^23 S7, degree23 HW(61,15,2^8), genuine full-support padding value -26743148924112014067635076791795712. D23<=-20 from accepted02.','Integrator reviewed recurrence, degree/HW and corank/density proof in12 supplement. Assigned independent reviewer12 verified23 delivery and86 input hashes and replayed two fresh full Hessian implementations,0.7784s. No second integrator rerun claimed.','Determinant rank<=8 normal-form lemma and accepted02 finite counts/source ceiling.'),
('07','At degree14 weight(21,21,2^7) and degree15(25,21,2^7), i_det=0; D14<=0,D15<=-3.','Integrator reviewed necessary-degree specialization argument and invertible primitive4x4 minor -5639493386240000. Reviewer12 independently reconstructed actual quartic/Hessian/depression, checked15 delivery and23 input hashes, replayed in3.0620s.','Complete stable four-space from accepted533/529/global4; CI73 padded floor3 and q44 multiplication forD15.'),
('09','At d19 weight(57,4,3,2^6), a=m_det=2,i_det=0,D<=0; same for higher degrees in stated stable range.','Integrator reviewed polynomial lift/frame/source-evaluation proof. Fresh receiver0.2554s reconstructs genuine determinant pencils, exact rational minor166461230261179373415548625/256, two modular minors and289-term ambient sum;16 delivery hashes.','B15-08 highest-weight source proof, inherited character algorithm and S57 stable identification; no exact padding rank.'),
('10','Actual padding arc coefficient rank floors1/2/2/3 at degrees23/25/26/27; excluded cells unchanged.','Integrator reviewed coefficient-functional independence and ideal-transport proof.50 delivery hashes verified, portable receiver freshly replayed0.5318s, full source Hessian controls and4 mutations.','Hessian source global/finite membership; accepted02 counts and source ceilings. Floor3 does not improve accepted243 atd27.'),
('11','Frozen launch evidence audit and portable metadata/conditional arithmetic receiver PASS; no new mathematical equation or gap.','Integrator verified124 delivery hashes and freshly replayed108-input relocated receiver in0.3773s. Read report and scope boundaries.','All historical mathematical computations and Git source bindings are inherited from named receipts; integrator did not repeat11 Git audit.')]
for slot,claim,fresh,inherited in rows:
    r={'slot':slot,'status':'ACCEPTED_SCOPED_REVIEW','checked_utc':now,'claim':claim,'fresh':fresh,'inherited':inherited,'resources':'All new numerical replays sequential,60s512MiB enforced Job Object, one process/BLAS thread, exit0. No heavy lease.','delivery_scope':'Filesystem hash binding, no new Git commit asserted.'}
    out=B/'reviews'/slot;out.mkdir(exist_ok=True)
    if slot in ('03','07'):
        src=ROOT/'work/batch15_workers/B15-12/docs/b16_12_receive03_07.md';shutil.copy2(src,out/'adversarial_proof_review.md')
        r['review_proof_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
        for name in ('intake_'+slot+'.json','replay_'+slot+'_integrity.json'):
            p=ROOT/'work/batch15_workers/B15-12/results/b16_12'/name
            if p.exists():shutil.copy2(p,out/name)
    (out/'integrator_review.json').write_text(json.dumps(r,indent=2)+'\n')
    ledger['entries']=[e for e in ledger['entries'] if e.get('slot')!=slot]+[r]
ledger['entries'].sort(key=lambda x:x['slot']);ledger['status']='ACCEPTED_01_02_03_07_09_10_11_PENDING_04_05_06_08_AND_FINAL12'
(B/'INTAKE.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(ledger['status'])
