"""Frozen-record reconciliation. No evaluator, point generator, or search is run.

An imported nonzero minor is ADOPTED until replayed. A sampled deficient rank
is only a rank floor. Neither an `exact` nor an `i_red` field in old prose is
trusted as a rational membership certificate.
"""
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PRIMES = (2147483647, 2147483629)
LMR = (65,17,2,2,2,2,2,2,2)
N3 = (19,7,2,2,2,2,2)


def partition(values):
    if isinstance(values,str):
        values = [int(x) for x in re.findall(r'\d+',values)]
    p = tuple(int(x) for x in values)
    if any(x < 0 for x in p) or any(a < b for a,b in zip(p,p[1:])):
        raise ValueError(f'not a partition: {values}')
    return tuple(x for x in p if x)


def cell_key(n,lam,delta):
    p = partition(lam); n,delta = int(n),int(delta)
    if not p or sum(p) != n*delta:
        raise ValueError(f'wrong cell size: {(n,p,delta)}')
    return n,p,delta


def cell_id(key):
    n,p,d = key
    return f'n{n}:d{d}:' + ','.join(map(str,p))


def json_file(path):
    with (ROOT/path).open(encoding='utf-8') as f: return json.load(f)


def json_rows(path):
    with (ROOT/path).open(encoding='utf-8') as f:
        for line,s in enumerate(f,1):
            if s.strip(): yield f'{path}:{line}',json.loads(s)


class Ledger:
    def __init__(self):
        self.cells = {}; self.inputs = set(); self.conflicts = []
        self.source_counts = Counter(); self.certificate_paths = set()

    def add(self,n,lam,delta,a,source,*,ranks=None,per_prime=None,cost=None,
            certificates=(),verification='reported_not_replayed',flags=()):
        key = cell_key(n,lam,delta); a = int(a) if a is not None else None
        if a is not None and a < 0: raise ValueError('negative dimension')
        path = source.split(':')[0]
        self.inputs.add(path); self.source_counts[path] += 1
        row = self.cells.setdefault(key,dict(id=cell_id(key),n=key[0],lam=list(key[1]),
            delta=key[2],a=a,tail=list(key[1][1:]),observations=[],flags=[]))
        if row['a'] is None and a is not None: row['a'] = a
        if a is not None and row['a'] != a:
            conflict = dict(cell=row['id'],field='a',values=[row['a'],a],source=source,
                            prior_sources=[o['source'] for o in row['observations']])
            self.conflicts.append(conflict)
            row['flags'].append('conflicting_ambient_dimensions')
        ranks = {s:int(v) for s,v in (ranks or {}).items() if v is not None}
        for side,v in ranks.items():
            if not 0 <= v <= a: raise ValueError(f'rank out of range at {source}: {side}={v}, a={a}')
        pp = {s:{str(p):int(v) for p,v in vs.items()} for s,vs in (per_prime or {}).items()}
        warnings = list(flags)
        for s,values in pp.items():
            if any(v < 0 or v > a for v in values.values()): raise ValueError(f'bad prime rank: {source}')
            if set(values) != set(map(str,PRIMES)): warnings.append(f'{s}:missing_house_prime')
            if len(set(values.values())) > 1: warnings.append(f'{s}:prime_ranks_differ')
            if s in ranks and values and ranks[s] not in set(values.values()):
                warnings.append(f'{s}:summary_prime_conflict')
        certs = [c[0] if isinstance(c,list) else c for c in certificates]
        self.certificate_paths.update(certs)
        missing = [c for c in certs if not (ROOT/c).is_file()]
        if missing: warnings.append('referenced_certificates_not_shipped')
        if ranks and not pp: warnings.append('per_prime_ranks_not_in_record')
        obs = dict(source=source,reported_a=a,ranks=ranks,per_prime=pp,verification=verification,
                   flags=sorted(set(warnings)))
        if cost: obs['resources'] = {k:v for k,v in cost.items() if v is not None}
        if certs:
            obs['certificates'] = certs
            obs['missing_certificates'] = missing
        row['observations'].append(obs)

    def finish(self):
        for key,row in self.cells.items():
            sides = sorted({s for o in row['observations'] for s in o['ranks']})
            row['sides'] = {}
            for s in sides:
                observations = [o for o in row['observations'] if s in o['ranks']]
                floor = max(o['ranks'][s] for o in observations)
                values = sorted({o['ranks'][s] for o in observations})
                full = floor == row['a']
                invalid = 'conflicting_ambient_dimensions' in row['flags'] or any(
                    'source_not_ok' in o['flags'] or f'{s}:summary_prime_conflict' in o['flags']
                    for o in observations)
                bound = dict(sampled_ranks=values,rank_floor=floor,
                    ideal_dimension_interval=[0,row['a']-floor],
                    status='ADOPTED' if full else 'MEASURED',
                    full_rank=full and not invalid,
                    independent_replay_this_run=False,
                    evidence=[o['source'] for o in observations],
                    interpretation='full_rank_certificate_claim' if full else 'finite_sample_floor_only')
                if len(values)>1: bound['flag']='different_sample_floors_retained'
                if full and not invalid: bound['exact_rank'] = row['a']
                if invalid: bound['status']='RECORDED'; bound['flag']='unresolved_record_conflict'
                row['sides'][s] = bound
            if key == (4,LMR,24):
                self._exact_det(row,273,'docs/batch13_board.md:LMR; docs/s74_final_review.md')
                row['D_interval'] = [-4,1]
                row['D_formula'] = 'D=mult_pad-mult_det=1-i_pad(24)'
                row['flags'] += ['epsilon_pad_rational_lift_unresolved',
                                 'sampled_pad_red_kernel_equality_is_not_ideal_equality']
            if key == (3,N3,12):
                self._exact_det(row,5,'docs/s63_report.md:3; LMR upper bound plus rank floor')
                row['sides']['pad'] = dict(status='PROVED',exact_rank=0,full_rank=False,
                    ideal_dimension_interval=[row['a'],row['a']],
                    interpretation='length 7 exceeds 5 essential variables of ell*per2')
                row['D_interval'] = [-5,-5]
            row['flags'] = sorted(set(row['flags']))
        return self

    @staticmethod
    def _exact_det(row,rank,dependency):
        side=row['sides']['det']
        if side['rank_floor'] > rank: raise ValueError('rank floor contradicts LMR')
        side.update(status='ADOPTED',exact_rank=rank,full_rank=(rank==row['a']),
                    ideal_dimension_interval=[row['a']-rank]*2,
                    upper_bound_dependency=dependency,interpretation='certified_floor_plus_LMR_upper_bound')


def resources(row):
    keys=('N_S','N_S_status','n_chi','nchi_est','NS_delta','secs','hwm_gb',
          'build_secs','build_hwm_gb','pred_mem_bytes','pred_mem_x_bytes','pred_cost_s','pred_secs')
    return {k:row[k] for k in keys if k in row}


def load_record():
    """Explicit frozen-file adapters; missing/malformed inputs raise, never disappear."""
    from wk9_s57_lib import _cells_from_md
    bank=Ledger()
    specs=[('s36_ledger.md',1,2,4,10),('s36_aone.md',2,1,3,6),
           ('s41_ledger.md',1,0,2,9),('s43_ledger.md',1,0,2,9),
           ('s45_ledger.md',1,0,4,13),('s46_ledger.md',1,0,4,14)]
    for name,*cols in specs:
        path='results/'+name
        for index,(lam,d,a,md) in enumerate(_cells_from_md(path,*cols)):
            bank.add(4,lam,d,a,f'{path}:parsed_row_{index}',ranks={'det':md},
                     flags=['legacy_markdown_rank_claim'])
    paths=['results/s52_ledger.jsonl']+[f'results/s54_cells_d{d}.jsonl' for d in (6,7,8,9)]
    paths += ['results/'+name for name in ('s60_cells.jsonl','s60_calibration.jsonl',
               's60_recheck.jsonl','s60_scan_dense.jsonl','s60_scan_sparse.jsonl',
               's71_sweep.jsonl','s71_calibration.jsonl','s79_cells.jsonl','s79_calibration6.jsonl')]
    for path in paths:
        for source,r in json_rows(path):
            ranks={s:r.get('mult_'+s) for s in ('det','pad','red','red_star','red_pts','per4')}
            pp={}
            for s,side in r.get('sides',{}).items():
                if side.get('per_prime'):
                    pp[s]={p:(v if not isinstance(v,dict) else
                              v['mult'] if 'mult' in v else r['a']-v['nullity'])
                           for p,v in side['per_prime'].items()}
            if not pp:
                for p,v in r.get('per_prime',{}).items():
                    for s,side in v.get('sides',{}).items():
                        if side.get('mult') is not None: pp.setdefault(s,{})[p]=side['mult']
                    for s in ranks:
                        if v.get('mult_'+s) is not None: pp.setdefault(s,{})[p]=v['mult_'+s]
            certs=list(r.get('certs',[]))
            for v in r.get('per_prime',{}).values(): certs.extend(v.get('certs',[]))
            bank.add(4,r['lam'],r['delta'],r['a'],source,ranks=ranks,per_prime=pp,
                     cost=resources(r),certificates=certs,
                     verification=('integrator_record_consistency_only' if 's79_' in path else 'reported_not_replayed'),
                     flags=['source_not_ok'] if r.get('ok') is False else [])
    # s57 and s63 contain dimensions/prices, not additional quartic rank measurements.
    for name in ('bank_aprofile.jsonl','bank_below_l6.jsonl'):
        for source,r in json_rows('results/s57_cells/'+name):
            bank.add(4,r['lam'],r['delta'],r['a'],source,cost=resources(r),
                     verification='dimension_or_cost_only')
    for source,r in json_rows('results/s57_cells/bank_families.jsonl'):
        if r['col'] in ('a_weyl','a_engine'):
            bank.add(4,r['lam'],r['delta'],r['value'],source,verification='dimension_only')
    for name in ('s63_anchor.json','s63_aladder.json'):
        for i,r in enumerate(json_file('results/'+name)['rows']):
            bank.add(4,r['lam'],r['delta'],r.get('a',r.get('a_amb')),
                     f'results/{name}:rows/{i}',verification='dimension_only')
    for i,r in enumerate(json_file('results/s63_n3ladder.json')['ladder']):
        bank.add(3,r['lam'],r['delta'],r['a'],f'results/s63_n3ladder.json:ladder/{i}',
                 ranks={'det':r['mult_det_P1']},per_prime={'det':dict(zip(PRIMES,[r['mult_det_P1'],r['mult_det_P2']]))},
                 flags=['LMR_required_for_deficient_rank_upper_bound'] if r['delta']==12 else [])
    n3=json_file('results/astra/S4/artifacts/n3_control.json')
    for family,side in [('det','det'),('unpadded_per3','per3')]:
        rr=[r for r in n3['results'] if r['family']==family]
        bank.add(3,N3,12,6,f'results/astra/S4/artifacts/n3_control.json:{family}',
                 ranks={side:rr[0]['minor']['rank']},
                 per_prime={side:{r['prime']:r['minor']['rank'] for r in rr}},
                 verification='banked_small_matrix; arithmetic replay in results/b13_11/n3_control.json',
                 certificates=['results/astra/S4/artifacts/n3_control.json'],
                 flags=['native_source_evaluations_inherited'])
    # s74's rows are native values transported by msym_u^(delta-rung).
    ladder=json_file('results/s74/ladder_ranks.json')
    if set(ladder) != set(map(str,PRIMES)): raise ValueError('s74 missing prime')
    p1={r['delta']:r for r in ladder[str(PRIMES[0])]}
    p2={r['delta']:r for r in ladder[str(PRIMES[1])]}
    if p1.keys()!=p2.keys(): raise ValueError('s74 ladder prime coverage differs')
    for d,r in p1.items():
        if r['a']!=p2[d]['a']: raise ValueError('s74 dimensions disagree')
        sides=('det','pad','red','per4','gen')
        bank.add(4,[4*d-31,17]+[2]*7,d,r['a'],f'results/s74/ladder_ranks.json:delta/{d}',
            ranks={s:r['rank_'+s] for s in sides},
            per_prime={s:{PRIMES[0]:r['rank_'+s],PRIMES[1]:p2[d]['rank_'+s]} for s in sides},
            verification='independent_integrator_matrix_replay_banked',
            certificates=['results/s74/certified.json','results/wk12_int_s74_final.json'],
            flags=['values_are_native_times_msym_u_power_at_read'])
    for source,r in json_rows('results/s79_per6.jsonl'):
        bank.add(3,r['mu'],r['delta'],r['a'],source,ranks={'per3':r['mult']},
            per_prime={'per3':{p:v['mult'] for p,v in r['per_prime'].items()}},
            cost=resources(r),certificates=r.get('certs',[]),verification='integrator_record_consistency_only')
    return bank.finish()


def negative_record():
    """Compatibility view: only full-rank quartic determinant cells, not LMR.

    This API historically feeds code which treats *every* key as closed.
    Complete deficient and n=3 records live in load_record().
    """
    out={}
    for (n,lam,d),row in load_record().cells.items():
        det=row['sides'].get('det',{})
        if n==4 and det.get('full_rank'):
            srcs=sorted({o['source'].split(':')[0] for o in row['observations'] if 'det' in o['ranks']})
            out[lam,d]=(row['a'],row['a'],';'.join(srcs))
    return out


def stable_record():
    """All sixteen banked stable blocks; flags retain independent-review scope."""
    out={}
    paths=sorted((ROOT/'results/s79_stable').glob('**/*_summary.json'))
    for p in paths:
        r=json.loads(p.read_text()); tail=partition(r['rho']); a=int(r['a_inf'])
        pp=r['per_prime']
        full=set(pp)==set(map(str,PRIMES)) and all(v['mult_det_inf']==a for v in pp.values())
        out[tail]=dict(a_inf=a,full_rank=full,status='ADOPTED',
                      evidence=p.relative_to(ROOT).as_posix(),
                      independent_review=('docs/s79_review.md:60/60' if a==4 else None),
                      flags=[] if a==4 else ['calibration_source_not_independently_replayed_this_run'])
    if len(out)!=16: raise ValueError(f'expected sixteen stable blocks, found {len(out)}')
    return out


def quartic_closed_tails(vals,record=None):
    """Preserve caller keys, normalize only for matching (including zero tails)."""
    rec=negative_record() if record is None else record
    keys={partition(k):k for k in vals}
    out=set()
    for (lam,d),(a,md,*_) in rec.items():
        tail=partition(lam[1:])
        if tail in keys and a==md==vals[keys[tail]]:
            out.add(keys[tail])
    return out


def stable_closed_tails(vals):
    bank=stable_record()
    return {k for k,v in vals.items() if partition(k) in bank
            and bank[partition(k)]['a_inf']==v and bank[partition(k)]['full_rank']}
