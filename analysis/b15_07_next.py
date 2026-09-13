"""Exact next-channel sizing and scoped ledger application; no large carrier."""
import hashlib
import json
from math import comb
from pathlib import Path
import sys
import flint
import numpy
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_07'
sys.path.insert(0,str(ROOT/'tools/integrate'))
from exclusion_predicates import conclusions_for
from b13_06_decompose import horizontal, schur_dim


def main():
    lam=(65,17)+(2,)*7; nu=(68,17,3)+(2,)*6
    rows=json.loads((ROOT/'results/b13_06/components.json').read_text())['rows']
    entry=next(r for r in rows if r['degree']==25 and tuple(r['partition'])==nu)
    strips=horizontal(lam,4)
    assert len(strips)==31 and nu in strips and entry['tensor_multiplicity']==1
    ledger=json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    overlay=json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())['targets']
    cell=dict(n=4,ell=len(nu),delta=25,**{'lambda':list(nu)})
    applied=conclusions_for(ledger,cell,'quartic_padded_gap')
    transport=next(r for r in overlay if r['degree']==25 and tuple(r['lam'])==nu)
    assert not applied and transport['status']=='OPEN'
    # The four-term HW tensor is checked symbolically for arbitrary HW lambda.
    a,b,n=s.symbols('a b n', positive=True)
    x=-1/b; y=-n/(a+b+1); z=n/(b*(a+b+1))
    assert s.simplify(1+b*x)==0 and s.simplify(y+b*z)==0
    assert s.simplify(n*x-y+(a+1)*z)==0
    coefficients=[s.Rational(1),x.subs(b,15),y.subs({n:4,a:48,b:15}),z.subs({n:4,a:48,b:15})]
    c2=lambda p: sum(v*(v+15-2*i) for i,v in enumerate(p))
    collision=[p for p in strips if p!=nu and c2(p)==c2(nu)]
    # Counting full ordinary coefficient carriers is enough to reject them.
    # No signed Burnside carrier is replaced by a stabilizer quotient.
    counts=[]
    for r in (9,10,16):
        letters=comb(r+3,4)
        counts.append(dict(ambient_variables=r,quartic_coefficient_variables=letters,
            source_module_dimension=schur_dim(lam,r),
            tensor_module_dimension=schur_dim(lam,r)*letters,
            output_irrep_dimension=schur_dim(nu,r),
            full_A25_monomials=comb(letters+24,25),
            method='Weyl dimension product and stars-and-bars; exact integer counts only'))
    record=dict(status='EXACT',purpose='costed next question, not a geometric run',
        n=4,degree=25,ambient_variables_for_full_geometry=16,partition=list(nu),
        source_degree=24,source_partition=list(lam),multiplier_partition=[4],
        tensor_multiplicity=1,image_hw_rank_lb=0,image_hw_rank_ub=1,
        a=None,i_det_lb=None,i_pad_lb=None,m_det_ub=None,m_pad_lb=None,h_pad_ub=None,
        inherited_channel_entry=entry,scoped_ledger=applied,accepted_transport_overlay=transport,
        independent_pieri_count=len(strips),casimir_eigenvalue=c2(nu),
        same_eigenvalue_other_domain_channels=[list(p) for p in collision],
        formula='T(F)=F*c_301 -(E32 F)*c_310/15 -(E31 F)*c_400/16 +(E21 E32 F)*c_400/240',
        indices='Only first three coordinates are displayed; other coefficient exponents are zero. E21 E32 means E32 first.',
        normalization='coefficient of F tensor c_301 is 1 before multiplication',
        formula_coefficients=list(map(str,coefficients)),
        symbolic_raising_equations=['1+15*(-1/15)=0','-1/16+15*(1/240)=0','4*(-1/15)-(-1/16)+49*(1/240)=0'],
        full_carrier_counts=counts,
        compact_cost=dict(method='five simultaneous derivation values per arithmetic circuit node',
            slots=['F','E21 F','E32 F','E31 F','E21 E32 F'],
            construction='Reuse the complete rational source circuit; extend each coefficient leaf by its exact root values.',
            multiplication_node_field_multiplications_ub=11,multiplication_node_field_additions_ub=6,
            addition_node_field_additions=5,live_field_elements='5 times the original circuit live-node count',
            final_linear_combination_field_multiplications_ub=7,final_linear_combination_field_additions_ub=3,
            reduction='One candidate HW column. Test exact coefficient nonzeroness or a nonzero rational evaluation. No full Schur module or carrier.',
            evaluation='For s points and a circuit with M product nodes and A sum nodes: at most s*(11M+7) field multiplications and s*(6M+5A+3) field additions, plus leaf construction. Bit complexity depends on source/point heights.',
            wall_time_estimate=None,reason='No complete source circuit cost or point height measured here; not inferred from small controls.'),
        next_sufficient_witness='A complete rational LMR HW circuit F with its global determinant-ideal provenance, and an exact nonzero T(F) value. This proves one product equation only. A positive gap would additionally need padded rank a, or stronger independently proved determinant and padded bounds.',
        padded_point_family='z*per3 in ten independent essential variables, with GL16 substitutions for full geometry',
        resource_decision='No heavy job; no lease requested or acquired. Production remains subject to integrator lease and measured pilot.',
        no_full_padded_ideal_inference=True)
    (OUT/'next_channel.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    paths=[]
    pre=(ROOT/'results/PREREG_b15_07.md').read_text()
    for line in pre.splitlines():
        if line.startswith('| ') and ' | ' in line:
            path=line.split('|')[1].strip()
            if (ROOT/path).is_file():
                paths.append(path)
    paths+=['analysis/b15_bound.py','analysis/b15_resource_smoke.py',
            'tools/integrate/exclusion_predicates.py','tools/delivery/check_batch15.py',
            'tools/delivery/package_batch15.py']
    hashes=[]
    for path in paths:
        raw=(ROOT/path).read_bytes()
        hashes.append(dict(path=path,bytes=len(raw),sha256_exact=hashlib.sha256(raw).hexdigest(),
            sha256_normalized_lf=hashlib.sha256(raw.replace(b'\r\n',b'\n')).hexdigest()))
    (OUT/'input_manifest.json').write_text(json.dumps(dict(status='RECORDED',files=hashes,
        runtime=dict(python=sys.executable,numpy=numpy.__version__,python_flint=flint.__version__,sympy=s.__version__)),indent=2)+'\n',encoding='utf-8')
    (OUT/'proposed_exclusions.json').write_text(json.dumps(dict(status='EXACT',exclusions=[],
        reason='Operator construction and exact controls do not compare determinant and padded multiplicities.'),indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='PASS',next_partition=list(nu),ledger_matches=len(applied),
                         overlay_status=transport['status'],coefficients=list(map(str,coefficients)))))


if __name__=='__main__':
    main()
