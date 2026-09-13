"""Assemble a per-slot report from checked outputs; no numerical research."""
from pathlib import Path
import json
import hashlib
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_06'


def read(path):return json.loads(path.read_text(encoding='utf-8'))


def main():
    census=read(OUT/'census.json');selection=read(OUT/'selection.json')
    selected={(x['r'],x['t']):x['rank'] for x in selection['selected']}
    candidates=[]
    for row in census['rows']:
        x=dict(row)
        x['pilot_priority']=selected.get((x['r'],x['t']))
        if x['overlay_exclusions']:x['queue_status']='INHERITED_EXCLUSION'
        elif x['reserved']:x['queue_status']='RESERVED_05'
        elif x['a_inf']>533:x['queue_status']='OVER_CAP'
        else:x['queue_status']='OPEN'
        candidates.append(x)
    ordered=sorted(candidates,key=lambda x:(x['queue_status']!='OPEN',x['pilot_priority'] or 100,
                                            -x['a_inf'],-x['r'],-x['t']))
    report=['# B15-06: fresh stable families', '',
        'Model for all new work: gpt-6-astra, xhigh. Banked B14-06 code and mathematics retain Claude Opus 5 attribution.', '',
        'The exact census covers all 40 requested families. A fresh recomputation using the same character methods agrees on all 80 ambient/normalization counts. The dimension-explicit evaluator passes both-prime controls at r=7,8,9,10, including full ten-variable independent padding. No positive multiplicity gap is claimed.', '',
        '## Exact census', '',
        'Each entry below is a_inf for tail (t,2^(r-2)). Use n=4, comparison ambient dimension16, stable coefficient degree delta=t+2(r-2), and lambda=(3delta,t,2^(r-2)). S57 Proposition S is inherited; the rational character arithmetic is newly computed.', '',
        '| t | r=7 | r=8 | r=9 | r=10 |','|---|---:|---:|---:|---:|']
    for t in range(3,22,2):
        report.append('| '+str(t)+' | '+' | '.join(str(next(x['a_inf'] for x in candidates if (x['r'],x['t'])==(r,t))) for r in range(7,11))+' |')
    report += ['',
        'The accepted overlay excludes nine-row t=17 from degree13 and t=19 from degree15, with D<=-2 and D<=-1. These are inherited exclusions and were skipped. Nine-row t=21 remains reserved to B15-05. Ten-row t=21 has a_inf=594 and exceeds the533 cap. Thus36 families remain within this slot\'s eligible census before pilot outcomes.', '',
        'For each stable family the census records i_pad_lb and m_pad_ub=min(a_inf,h_pad_ub,a_inf-i_pad_lb). The exact h_pad_ub is the multiplicity in Sym(V\'+Sym^2 V\'+Sym^3 V\'), derived from the reducible parametrization in proof C2. All40 values exceed a_inf; this bound adds no ideal floor. Only the accepted nine-row t=17/19/21 transport supplies L_pad=3. Unknown additional ideal floors are not inferred from sampled ranks.', '',
        'The historical record audit found no previously full stable determinant witness among the other requested families. It retains finite-rung nine-row t=17 observations separately; the stable-ambient upper bound is never substituted for a finite ambient dimension. B13-06 tensor components are inventoried in census.json, with tensor multiplicities distinguished from image ranks.', '',
        '## Selected pilots', '',
        'selection.json was written before geometry: (r,t)=(10,19),(8,21),(7,21), with ambient multiplicities429,460,378. The ten-row family has an inherited LMR structural motivation (k=7, degree27); the seven/eight-row comparison at t=21 probes lengths where that mechanism is absent. Other open rows are ranked by source size as a resource order, without assigning a probability of positive D.', '',
        '| r | t | a_inf | GEN rank_lb | DET rank_lb | PAD rank_lb | Interpretation |',
        '|---|---|---:|---:|---:|---:|---|']
    exclusions=[];completed=0
    for cell in selection['selected']:
        r,t=cell['r'],cell['t'];a=cell['a_inf']
        path=OUT/f'pilot_r{r}_t{t}_summary.json'
        if not path.exists() or not read(path)['complete']:
            report.append(f'| {r} | {t} | {a} | pending | pending | pending | Heavy lease requested |')
            continue
        data=read(path);ranks={}
        for fam in ('GEN','DET','PAD'):
            records=[v for v in data['records'] if v['family']==fam]
            assert len(records)==2
            assert len({v['rank_lb'] for v in records})==1
            ranks[fam]=records[0]['rank_lb']
        replay=read(OUT/f'geometric_replay_r{r}_t{t}.json')
        assert replay['complete'] and all(v['fresh_geometric_replay'] for v in replay['checks'])
        completed+=1
        if ranks['DET']==a:
            interpretation='EXACT family exclusion, via full rank and C4'
            exclusions.append({'id':f'b15_06_r{r}_t{t}_stable_full', 'status':'EXACT',
                'claim':'i_det=0 at every valid rung; D<=0',
                'n':4,'r':r,'tail':[t]+[2]*(r-2),'degree_scope':'every valid rung',
                'a_inf':a,'m_det_stable_lb':ranks['DET'],
                'inherited_premises':['S57 Proposition S ideal filtration','polynomial-functor inheritance'],
                'fresh_evidence':[f'results/b15_06/pilot_r{r}_t{t}_summary.json',
                                  f'results/b15_06/geometric_replay_r{r}_t{t}.json'],
                'proof':'docs/b15_06_proved.md C3/C4; exact ambient count plus nonzero determinant minor'})
        else:
            interpretation=f'CANDIDATE; i_det_inf<={a-ranks["DET"]}'
        report.append(f'| {r} | {t} | {a} | {ranks["GEN"]} | {ranks["DET"]} | {ranks["PAD"]} | {interpretation} |')
        row=next(x for x in ordered if (x['r'],x['t'])==(r,t))
        row['pilot_ranks_lb']=ranks
        row['i_det_inf_ub']=a-ranks['DET']
        if ranks['DET']==a:row['queue_status']='NEW_FAMILY_EXCLUSION'
        else:
            row['i_pad_inf_ub']=a-ranks['PAD']
            row['D_stable_lb']=ranks['PAD']-a
            row['D_stable_ub']=a-ranks['DET']
            row['next_sufficient_negative_witness']=f"global padded ideal floor {a-ranks['DET']} at a stated stable rung"
    report += ['',
        'All ranks, when present, agree at2147483647 and2147483629 and are backed by explicit nonzero square minors. The replay reconstructs jets from integer pencils or independent padded linear forms, reevaluates the selected source brackets, and checks every entry of the minor before recomputing its determinant. This is a fresh geometric replay, not stored-matrix elimination. Generic source matrices attaining a_inf also certify source completeness without a separate spanning premise.', '',
        'A deficient DET rank is a floor, and bounds the ideal from above. A deficient PAD sample cannot produce an ideal lower bound. For a remaining candidate, the next sufficient positive witness is a global determinant ideal floor q and a padded minor r_pad satisfying q+r_pad>a at one fixed cell. A sufficient negative witness is a padded ideal floor at least a_inf-r_det, combined with the stable ideal filtration. No finite degree27 ambient value is asserted from the stable ten-row count429.', '',
        '## Validation and resource decisions', '',
        'The frozen commit f365568d80d5f66fea2dd9342ff1998e1d866915, tree aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd and annotated tag object80209c13e9ae33bad8933cb47413bf7710c96cb1 matched before work. Preregistration commit:5cded1760b25641074ddbf2795554c1dd14b6672. Original setup runtime logs were preserved and excluded from research staging.', '',
        'The original B14-06 point module fixes NV=8 and AMB=9, and the evaluator factorial table ends at8!. The per-slot extension makes all point dimensions explicit, validates array shapes, and extends factorials through col!. Reused Jet/contraction/normalization helpers retain their banked attribution. Small controls compare direct epsilon contractions, shifted DET/DETQ, covariance and torus weights, and known peaked liveness. Altered point, Euler, sign, factorial, dimension and source serialization checks detect defects. Full ten-variable padding has exact derivative rank10 and a nonsingular integer ten-by-ten substitution. NumPy2.4.6 and python-flint0.9.0 ran successfully.', '',
        '| Run | Exit | Wall seconds | Peak aggregate MiB | Cap seconds / MiB |',
        '|---|---:|---:|---:|---|']
    logs=[]
    for path in sorted((ROOT/'results/logs').glob('b15_06_*_resources.json')):
        if 'runtime_native' in path.name:continue
        meta=read(path);logs.append(str(path.relative_to(ROOT)))
        report.append(f'| {path.stem} | {meta.get("exit_code","unfinished")} | {meta.get("wall_seconds",0):.3f} | {meta.get("job_memory",{}).get("peak_job_memory",0)/1024**2:.2f} | {meta["wall_cap_seconds"]} / {meta["memory_cap_mb"]} |')
    if completed==3:
        phase='The selected pilots are complete. Heavy process exit and lease release are recorded for the integrator.'
    elif completed:
        phase='Completed runs have exited. The integrator granted the first selected family; later families await a measured-cost checkpoint and extension authorization.'
    else:
        phase='The initial lease request is recorded in lease_request.json. Independent census and extension work is complete.'
    report += ['',f'Completed pilot/replay pairs: {completed}/3. '+phase, '',
        'One process and one BLAS thread were used under the native Windows Job Object wrapper. Four-point timing controls price construction, point generation and evaluation separately; extrapolations are labeled estimates and exclude matrix reduction/replay. No weight carrier or stabilizer quotient was allocated. Every tracked artifact is checked below5,000,000 bytes; large delivery bundles are split by the supplied helper.', '',
        '## Replay and delivery', '',
        'All commands run from C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06. A concise exact-count replay is:', '',
        "```powershell\n& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06/.venv/python.exe' analysis/b15_bound.py --slot 06 --name b15_06_receiver_counts --seconds 60 --memory-mb 512 analysis/b15_06_verify.py counts\n```", '',
        'Use the same executable and wrapper for the following entry points, with unique run names:', '',
        '- analysis/b15_06_census.py: regenerate the40-row census (60seconds,512MiB).',
        '- analysis/b15_06_verify.py counts: independently recompute and compare80 certificates (60seconds,512MiB).',
        '- analysis/b15_06_geometry.py controls: dimension and liveness controls (60seconds,512MiB).',
        '- analysis/b15_06_heavy.py --rank K: one selected production and native geometric replay, requiring an integrator lease for that family (900seconds,1536MiB).',
        '- analysis/b15_06_verify.py geometry --r R --t T: replay saved native minors under a lease.', '',
        'Input hashes are in preregistration and input_hashes.json. Source constructions, integer points, primes, interpolation seed, bracket-by-point orientation, minors, and resource logs are retained. The chart uses ordinary c=[s0^4]F, with c=1 for DET; it does not silently substitute the historical factorial symbol u=24c.', '',
        'Final packaging, after the last commit: tools/delivery/check_batch15.py --branch b15-06-fresh-tails --base f365568d80d5f66fea2dd9342ff1998e1d866915 --slot 06, then tools/delivery/package_batch15.py --branch b15-06-fresh-tails --slot 06 --model gpt-6-astra --output delivery/b15_06_final. The external manifest carries head/tree and bundle checksums without self-reference. A packaging PASS is not mathematical verification.', '']
    prose='\n'.join(report)
    for old,new in [('all40','all 40'),('All40','All 40'),('the40','the 40'),('compare80','compare 80'),
                    ('degree13','degree 13'),('degree15','degree 15'),('degree27','degree 27'),
                    ('the533','the 533'),('Thus36','Thus 36'),('multiplicities429','multiplicities 429'),
                    ('at2147483647','at 2147483647'),('and2147483629','and 2147483629'),
                    ('count429','count 429'),('object80209','object 80209'),('commit:5c','commit: 5c'),
                    ('at8!','at 8!'),('rank10','rank 10'),('NumPy2.4.6','NumPy 2.4.6'),
                    ('python-flint0.9.0','python-flint 0.9.0'),('below5,','below 5,'),
                    ('60seconds','60 seconds'),('512MiB','512 MiB'),('900seconds','900 seconds'),
                    ('1536MiB','1536 MiB')]:
        prose=prose.replace(old,new)
    (ROOT/'docs/b15_06_report.md').write_text(prose,encoding='utf-8')
    (OUT/'ranked_census.json').write_text(json.dumps({'status':'EXACT','rows':ordered},indent=2)+'\n',encoding='utf-8')
    (OUT/'proposed_exclusions.json').write_text(json.dumps({'slot':'06','single_writer':'integrator',
        'proposals':exclusions,'no_shared_index_written':True},indent=2)+'\n',encoding='utf-8')
    sources=['docs/s57_report.md','analysis/b14_04/recount.py','analysis/b14_06_bracket.py',
        'analysis/b14_06_points.py','analysis/wk8_s30_pleth.py','analysis/b13_11_ledger.py',
        'results/b15_prep/transport_overlay.json','results/integrate/inherited_exclusions.json',
        'results/b13_06/components.json','results/s57_cells/stable_a.jsonl','docs/s55_report.md',
        'tools/integrate/exclusion_predicates.py','analysis/b15_bound.py']
    hashes={p:hashlib.sha256((ROOT/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest() for p in sources}
    (OUT/'input_hashes.json').write_text(json.dumps({'convention':'SHA256; CRLF normalized to LF for UTF-8 text',
                                                 'files':hashes},indent=2)+'\n',encoding='utf-8')
    print('REPORT',completed,'pilots;',len(exclusions),'new family exclusions')


if __name__=='__main__':main()
