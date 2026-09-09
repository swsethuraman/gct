"""Join only frozen candidates and records; no numerical queue is launched."""
import ast
from collections import Counter,defaultdict
import json
from pathlib import Path
import sys
from b13_11_ledger import (ROOT,PRIMES,partition,cell_key,cell_id,load_record,
                           stable_record,json_file,json_rows,resources)
from b13_11_reconcile import save,parts,OUT


def inherited_gap_exclusion(n,lam):
    """This is an exclusion for the padded gap, not a determinant ideal claim."""
    if n==4 and len(partition(lam))<=4:
        return dict(rule='padded_containment_length_le_4',status='ADOPTED',
                    dependency='docs/n4_gate.md section 1',conclusion='D<=0')
    return None


def main():
    bank=load_record(); candidates={}; input_paths=set(bank.inputs)
    def add(n,r,path,index,lamfield='lam'):
        key=cell_key(n,r[lamfield],r['delta'])
        c=candidates.setdefault(key,dict(id=cell_id(key),n=n,lam=list(key[1]),delta=key[2],
              a=r.get('a'),provenance=[],resources=[]))
        if c['a'] is not None and r.get('a') is not None and c['a']!=r['a']:
            raise ValueError(f'candidate dimension conflict: {key}: {c["a"]} vs {r["a"]}')
        if c['a'] is None: c['a']=r.get('a')
        c['provenance'].append(f'{path}:{index}')
        cost=resources(r)
        if cost: c['resources'].append(dict(source=path,**cost))
        input_paths.add(path)
    for key,r in bank.cells.items():
        candidates[key]=dict(id=r['id'],n=r['n'],lam=r['lam'],delta=r['delta'],a=r['a'],
                            provenance=[o['source'] for o in r['observations']],
                            resources=[dict(source=o['source'],**o['resources']) for o in r['observations'] if o.get('resources')])
    for path in ('results/s60_closing_cells.json','results/s71_queue.json',
                 'results/s79_queue.json','results/s79_queue2.json'):
        for i,r in enumerate(json_file(path)): add(4,r,path,i)
    path='results/s79_per6_queue.json'
    for d,rows in json_file(path).items():
        for i,r in enumerate(rows): add(3,r,path,f'{d}/{i}',lamfield='mu')

    dims={}; dim_sources=defaultdict(list)
    def dimension(tail,value,source):
        if value is None:return
        tail=partition(tail); value=int(value)
        if tail in dims and dims[tail]!=value: raise ValueError(f'stable dimension conflict: {tail}')
        dims[tail]=value; dim_sources[tail].append(source)
    for src,r in json_rows('results/s57_cells/stable_a.jsonl'):
        dimension(r['tail'],r['a_inf'],src)
    input_paths.add('results/s57_cells/stable_a.jsonl')
    for i,r in enumerate(json_file('results/s60_tail_census.json')):
        dimension(r['tail'],r['a_inf'],f'results/s60_tail_census.json:{i}')
    input_paths.add('results/s60_tail_census.json')
    for i,r in enumerate(json_file('results/s79_queue.json')):
        dimension(r['lam'][1:],r.get('a_inf'),f'results/s79_queue.json:{i}')
    census=json_file('results/b13_11/weight13_census.json')
    for t,value in census['a_inf_by_shape'].items():
        dimension(ast.literal_eval(t),value,'results/b13_11/weight13_census.json')
    stable=stable_record()
    replay=json_file('results/b13_11/stable_replay.json')
    if len(replay['checks'])!=192 or any(not c['ok'] for c in replay['checks']):
        raise ValueError('incomplete stable replay')
    full_by_tail=defaultdict(list)
    for (n,lam,d),r in bank.cells.items():
        if n==4 and r['sides'].get('det',{}).get('full_rank'):
            full_by_tail[partition(lam[1:])].append(r)
    closures={}
    for t,a in dims.items():
        witnesses=[r for r in full_by_tail[t] if r['a']==a]
        reasons=[]
        if a==0: reasons.append(dict(rule='stable_ambient_zero',status='ADOPTED',sources=dim_sources[t]))
        if witnesses:
            reasons.append(dict(rule='Prop_S_full_rank_at_stable_dimension',status='ADOPTED',
                witness_cells=[r['id'] for r in witnesses],dimension_sources=dim_sources[t],
                verification='imported_full_rank_claims; see cell certificate and replay flags'))
        if t in stable and stable[t]['full_rank']:
            reasons.append(dict(rule='stable_determinant_full_rank',status='CERTIFIED',
                source=stable[t]['evidence'],independent_replay='results/b13_11/stable_replay.json'))
        if reasons: closures[t]=reasons
    for key,c in candidates.items():
        n,lam,d=key; t=partition(lam[1:]); r=bank.cells.get(key); why=[]; flags=[]
        if r:
            flags.extend(r['flags'])
            for o in r['observations']:flags.extend(o['flags'])
        if n==4:
            inherited=inherited_gap_exclusion(n,lam)
            if inherited:why.append(inherited)
            if c['a']==0:
                why.append(dict(rule='ambient_dimension_zero',status='ADOPTED',conclusion='D=0'))
            if t in closures:
                why.append(dict(rule='whole_tail_determinant_exclusion',tail=list(t),
                    status='CERTIFIED' if any(x['status']=='CERTIFIED' for x in closures[t]) else 'ADOPTED',
                    conclusion='i_det=0;D<=0'))
            if r and r['sides'].get('det',{}).get('full_rank'):
                why.append(dict(rule='direct_full_rank_determinant',status='ADOPTED',conclusion='i_det=0;D<=0'))
            if not why:
                witnesses=[x for x in full_by_tail[t] if d<=x['delta'] or c['a']==x['a']]
                if witnesses:
                    why.append(dict(rule='Lemma_L_downward_or_equal_dimension_transport',status='ADOPTED',
                                    witness_cells=[x['id'] for x in witnesses],conclusion='i_det=0;D<=0'))
            c['closed_for_positive_padded_gap']=bool(why)
            c['open_on_all_instruments']=not why
            c['objective']='D=mult_pad-mult_det>0'
            if lam==(65,17,2,2,2,2,2,2,2) and d==24:
                c['D_interval']=[-4,1];c['D_formula']='1-i_pad(24)'
        else:
            # Cubic per3 screen is a different objective. Its emptiness is not
            # an exclusion for a quartic padded multiplicity obstruction.
            full=r and r['sides'].get('per3',{}).get('full_rank')
            if len(lam)<=5: why.append(dict(rule='cubic_per3_dominance_length_le_5',
                status='ADOPTED',dependency='docs/washout_lemma.md Theorem 2 and restriction lemma',
                conclusion='i_per3=0'))
            if full:why.append(dict(rule='direct_cubic_per3_full_rank',status='ADOPTED',conclusion='i_per3=0'))
            c['objective']='cubic_per3_ideal_screen; separate from padded gap'
            c['open_on_all_instruments']=not why
            if r and 'det' in r['sides']:
                c['objective']='n3_determinant_control'
                c['open_on_all_instruments']=False
        c['closures']=why
        c['verification_flags']=sorted(set(flags+(['resource_estimate_unavailable'] if not c['resources'] else [])))
        # Give a transparent work proxy, never an uncalibrated wall-time prediction.
        ns=next((v['N_S'] for v in c['resources'] if v.get('N_S') is not None),None)
        if ns is not None:
            c['work_proxy_NS_delta']=ns*d
            c['recorded_builder_wall_exceeded']=ns*d>=147_000_000
        if n==4 and t in dims:
            c['a_inf_adopted']=dims[t]
            c['stable_dimension_sources']=dim_sources[t]
    closure_rows=[dict(n=4,tail=list(t),a_inf=dims[t],reasons=reasons)
                  for t,reasons in sorted(closures.items())]
    cp=parts('candidate_inventory',[candidates[k] for k in sorted(candidates)])
    tp=parts('inherited_tail_closures',closure_rows)
    # Explicit inventory of the 57 exact census tails, with rank-record versus
    # inherited-containment openness separated.
    w13=[]
    for t,value in census['a_inf_by_shape'].items():
        tail=partition(ast.literal_eval(t)); reasons=closures.get(tail,[])
        containment=len(tail)+1<=4
        prices=[dict(cell=c['id'],resources=c['resources'],work_proxy=c.get('work_proxy_NS_delta'))
                for k,c in candidates.items() if k[0]==4 and partition(k[1][1:])==tail and c['resources']]
        w13.append(dict(tail=list(tail),a_inf=value,status='CERTIFIED',
                       a_inf_method='exact_integer_counting',rank_record_closed=bool(reasons),
                       inherited_containment=containment,
                       open_for_D_positive=value>0 and not reasons and not containment,
                       closure_reasons=reasons,banked_prices=prices))
    wp=parts('weight13_inventory',w13)
    cube10=[c for (n,lam,d),c in candidates.items() if n==3 and d==10 and len(lam)==6]
    open_cube10=[c for c in cube10 if c['open_on_all_instruments']]
    q1=json_file('results/s79_queue.json'); q2=json_file('results/s79_queue2.json')
    qcounts={}
    for name,queue in [('Q1',q1),('Q2',q2)]:
        vals=[candidates[cell_key(4,r['lam'],r['delta'])] for r in queue]
        qcounts[name]=dict(cells=len(vals),open_on_all_instruments=sum(c['open_on_all_instruments'] for c in vals),
                          closed=sum(not c['open_on_all_instruments'] for c in vals))
    summary=dict(board_numbering='batch13',session_id='B13-11',candidate_parts=cp,
        inherited_tail_parts=tp,weight13_parts=wp,scope='explicit frozen records and s60/s71/s79 queues; no new search or ranking',
        candidate_cells=len(candidates),quartic_candidate_cells=sum(k[0]==4 for k in candidates),
        quartic_open=sum(c['n']==4 and c['open_on_all_instruments'] for c in candidates.values()),
        whole_tail_closures=len(closures),nonzero_whole_tail_closures=sum(dims[t]>0 for t in closures),
        weight13=dict(shapes=len(w13),nonempty=sum(r['a_inf']>0 for r in w13),
            closed_on_rank_records=sum(r['a_inf']>0 and r['rank_record_closed'] for r in w13),
            open_on_two_rank_records=sum(r['a_inf']>0 and not r['rank_record_closed'] for r in w13),
            open_after_inherited_containment=sum(r['open_for_D_positive'] for r in w13)),
        s79_queues=qcounts,cubic_degree10=dict(candidates=len(cube10),open=len(open_cube10),
            open_NS_below_10m=sum(c['work_proxy_NS_delta']<100_000_000 for c in open_cube10),
            open_NS_at_least_10m=sum(c['work_proxy_NS_delta']>=100_000_000 for c in open_cube10)),
        inputs=sorted(input_paths))
    save('inventory_summary.json',summary)
    save('inherited_rules.json',dict(board_numbering='batch13',session_id='B13-11',rules=[
        dict(rule='coordinate_ring_surjection',status='PROVED',formula='P subset D implies mult_pad<=mult_det',source='docs/brief_wording.md section 7'),
        dict(rule='full_rank_floor',status='PROVED',formula='rank_p<=rank_Q<=a; full rank implies i=0'),
        dict(rule='deficient_sample',status='PROVED',formula='sampled rank k gives i<=a-k, never i>=a-k'),
        dict(rule='Lemma_L_and_Prop_S',status='ADOPTED',source='docs/s57_report.md sections 2 and 3'),
        dict(rule='length_le_4_padded_containment',status='ADOPTED',source='docs/n4_gate.md section 1'),
        dict(rule='length_le_5_cubic_per3_dominance',status='ADOPTED',source='docs/washout_lemma.md Theorems 2 and 3(1)'),
        dict(rule='degree9_cubic_complete',status='ADOPTED',source='docs/batch13_corrections.md section 2',
             dependency='210 six-row full-rank claims plus inherited 365 shorter constituents',
             conclusion='padded/reducible equality in that degree; does not exclude D>0 alone')]))
    print(json.dumps(summary),flush=True)


if __name__=='__main__':main()
