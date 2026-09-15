"""B15-11: scoped evidence joins; external observations are never authority.

All public queries fail closed. EXACT labels exact deduction from explicitly
named inherited premises, not a fresh replay of those premises. The only native
certificate replay currently supported is b14-10-catalecticant/1.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import itertools
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.integrate.exclusion_predicates import matches, validate_cell

CONVENTION = "polynomial_GL_covariant_Schur_label"
STATES = {"EXACT", "REPLAYED_RANK_FLOOR", "RECORDED", "CANDIDATE", "RESOURCE_STOP"}


def digest(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def canonical_digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def key(c):
    return c["n"], c["delta"], tuple(c.get("lambda", c.get("lam", [])))


def cell(n, delta, lam, context=None):
    return dict(n=n, delta=delta, ell=len(lam), **{"lambda": list(lam)},
                ambient_variables=n*n, representation=CONVENTION,
                geometry="orbit_closure", context=context or
                ("quartic_padded_gap" if n == 4 else "cubic_per3_ideal"),
                point_family=("det4_vs_independent_z_per3" if n == 4 else "per3"))


def validate(c):
    validate_cell(c)
    if set(c) != {"n", "delta", "ell", "lambda", "ambient_variables", "representation", "geometry", "context", "point_family"}:
        raise ValueError("cell fields differ from b15-evidence/1")
    if c.get("ambient_variables") != c["n"]**2:
        raise ValueError("unsupported ambient: require full matrix-variable ambient, not partition length")
    if c.get("representation") != CONVENTION or c.get("geometry") != "orbit_closure":
        raise ValueError("unsupported representation or orbit/closure convention")
    expected = {"quartic_padded_gap": (4, "det4_vs_independent_z_per3"),
                "cubic_per3_ideal": (3, "per3")}
    if expected.get(c.get("context")) != (c["n"], c.get("point_family")):
        raise ValueError("unsupported point family or comparison context")
    if c["ell"] > c["ambient_variables"]:
        raise ValueError("partition exceeds ambient variable count")


class Memory:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        self.pins = json.loads((self.root / "results/b15_11/trusted_inputs.json").read_text(encoding="utf-8"))
        self.cache = {}

    def read(self, path):
        # Pins are the reviewer's trust root, versioned with this consumer.
        if path not in self.pins:
            raise ValueError("unregistered dependency: " + path)
        raw = (self.root / path).read_bytes()
        if digest(raw) != self.pins[path]:
            raise ValueError("dependency digest mismatch: " + path)
        if path not in self.cache:
            self.cache[path] = json.loads(raw) if path.endswith(".json") else raw.decode("utf-8")
        return copy.deepcopy(self.cache[path])

    def query(self, c, observations=(), certificates=()):
        try:
            validate(c)
            return self._query(c, observations, certificates)
        except (ValueError, KeyError, TypeError, AssertionError, OSError) as exc:
            return dict(cell=c, status="RECORDED", decision="UNRESOLVED", bounds={},
                        exclusion_reason=None, inherited_premises=[], rejected=[str(exc)],
                        next_sufficient_witness="Repair the key, scope or dependency and replay.")

    def _query(self, c, observations, certificates):
        self.read("tools/integrate/exclusion_predicates.py")
        bounds = {}
        inherited, replayed, recorded, reasons = [], [], [], []

        def put(name, value):
            if type(value) is not int or (name != "D_lb" and name != "D_ub" and value < 0):
                raise ValueError("invalid integer bound " + name)
            if not name.endswith(("_lb", "_ub")):
                raise ValueError("untyped bound " + name)
            if name not in bounds:
                bounds[name] = value
            else:
                bounds[name] = (max if name.endswith("_lb") else min)(bounds[name], value)

        def exact(name, value):
            put(name + "_lb", value)
            put(name + "_ub", value)

        def premise(identifier, source):
            self.read(source)
            entry = dict(id=identifier, source=source, scope="inherited; no native evaluation replay here")
            if entry not in inherited:
                inherited.append(entry)

        for ring in (("det", "pad") if c["n"] == 4 else ("per3",)):
            put("m_" + ring + "_lb", 0)
            put("i_" + ring + "_lb", 0)
        put("a_lb", 0)
        index = self.read("results/integrate/inherited_exclusions.json")
        contracts = index["application_contract"]["conclusions_by_id"]
        # Do not let the legacy matcher's global cache bypass a pin check.
        for rule in index["exclusions"]:
            cat = rule["predicate"].get("explicit_cell_keys")
            if cat:
                self.read(cat)
            if not matches(rule["predicate"], c, c["context"]):
                continue
            conclusion = contracts[rule["id"]].get(c["context"])
            if not conclusion:
                continue
            premise(rule["id"], "results/integrate/inherited_exclusions.json")
            if "D<=0" in conclusion:
                put("D_ub", 0)
                reasons.append(rule["id"])
            if "mult_pad=0" in conclusion:
                exact("m_pad", 0)
            if conclusion == "i_per3=0":
                exact("i_per3", 0)
            if rule["id"] == "peaked_quartic_ladders":
                exact("a", 1)
                exact("m_det", 1)
            if rule["id"] == "b14_10_four_cubic_top_replacements":
                exact("a", 1)

        if c["n"] == 4:
            if not hasattr(self, "queue"):
                self.queue = {key(r): r for r in self.read("results/b14_11/cost_queue.json")}
            row = self.queue.get(key(c))
            if row:
                premise("reviewed_exact_census", "docs/b14_11_review.md")
                exact("a", row["a"])
                put("h_pad_ub", row["h_pad"])
            self.read("docs/batch15/ACCEPTED_STATE.md")
            if key(c) == (4, 24, (65, 17) + (2,)*7):
                premise("accepted_LMR", "docs/batch15/ACCEPTED_STATE.md")
                exact("a", 274)
                exact("m_det", 273)
                put("m_pad_lb", 269)
                put("i_pad_lb", 3)
            overlay = self.read("results/b15_prep/transport_overlay.json")
            for family in overlay["family_extensions"]:
                if c["delta"] >= family["from_degree"] and c["lambda"][1:] == family["tail"]:
                    premise("reviewed_tail_transport", "results/b15_prep/transport_overlay.json")
                    put("D_ub", family["D_upper"])
                    put("i_pad_lb", 3)
                    put("i_det_ub", 3 + family["D_upper"])
                    reasons.append("reviewed_tail_transport")
            for row in overlay["targets"]:
                if c["delta"] == row["degree"] and c["lambda"] == row["lam"]:
                    if row["padded_ideal_floor"]:
                        premise("reviewed_ideal_products", "results/b15_prep/transport_overlay.json")
                        put("i_pad_lb", row["padded_ideal_floor"])
                    if row["determinant_ideal_upper"] is not None:
                        premise("reviewed_finite_ideal_upper", "results/b15_prep/transport_overlay.json")
                        put("i_det_ub", row["determinant_ideal_upper"])
            if c["lambda"][1:] == [21] + [2]*7 and c["delta"] >= 15:
                premise("accepted_tail21_transport", "docs/batch15/ACCEPTED_STATE.md")
                put("i_pad_lb", 3)
                if c["delta"] == 26:
                    exact("a", 531)
            if key(c) == (4, 8, (12, 4, 4, 4, 4, 4)):
                premise("Q1_recount_hpad", "results/b15_prep/Q1_combined_bound.json")
                exact("a", 4)
                put("h_pad_ub", 1)
            # The operational accepted closure remains visible, without treating
            # delivered geometric outcomes as a native witness in this consumer.
            if not hasattr(self, "q1"):
                self.q1 = {key(r): r for r in self.read("results/b15_prep/Q1_coverage.json")["cells"]}
            row = self.q1.get(key(c))
            if row:
                recorded.append(dict(kind="accepted_Q1_record_closure", record=row,
                                     native_witness_replayed=False))

        for observation in observations:
            validate_record(observation)
            if observation.get("cell") != c:
                raise ValueError("observation cell/context mismatch")
            recorded.append(dict(kind="external_record_only", record=observation,
                                 usable_for_bounds=False))
        for cert in certificates:
            self.read("analysis/b14_10/recover.py")
            result = verify_native(cert)
            cc = cert["cell"]
            if key(cc) != key(c) or c["context"] != "cubic_per3_ideal":
                raise ValueError("native certificate cell/context mismatch")
            put("m_per3_lb", 1)
            replayed.append(result)

        close_intervals(bounds)
        if bounds.get("D_ub", 1) <= 0:
            decision = "EXCLUDED_D_POSITIVE"
            if not reasons:
                reasons.append("valid_m_det_lb_ge_U_pad")
        elif bounds.get("D_lb", 0) > 0:
            decision = "POSITIVE_D"
        elif c["context"] == "cubic_per3_ideal" and bounds.get("i_per3_ub") == 0:
            decision = "IDEAL_ZERO"
        else:
            decision = "UNRESOLVED"
        nxt = ("No positive-gap witness is possible under the listed premises."
               if decision in ("EXCLUDED_D_POSITIVE", "IDEAL_ZERO") else
               "Supply a native determinant rank floor at least U_pad, or a global determinant ideal floor q and native padded rank r with q+r>a.")
        if key(c) == (4, 24, (65, 17)+(2,)*7):
            nxt = "To obtain D=-4, prove two further independent global padded equations, raising i_pad_lb from 3 to 5."
        if c["n"] == 4 and c["lambda"][1:] == [21]+[2]*7:
            nxt = "Stable determinant rank floor 530 with native witness and stable ambient 533 excludes every rung from degree 15; at degree 26, native rank 528 suffices with a=531 and i_pad_lb=3."
        return dict(cell=c, bounds=bounds, decision=decision,
                    status=("REPLAYED_RANK_FLOOR" if replayed else "RECORDED" if recorded and decision == "UNRESOLVED" else "EXACT" if decision != "UNRESOLVED" else "CANDIDATE"),
                    exclusion_reason=reasons or None, inherited_premises=inherited,
                    replayed=replayed, recorded=recorded, rejected=[], next_sufficient_witness=nxt)


def close_intervals(b):
    """Exact integer interval closure. Inputs must already be authorized facts."""
    def put(k, v):
        if k not in b:
            b[k] = v
        else:
            b[k] = (max if k.endswith("_lb") else min)(b[k], v)
    for _ in range(8):
        old = b.copy()
        if b.get("a_lb") == b.get("a_ub") and "a_ub" in b:
            a = b["a_ub"]
            for ring in ("det", "pad", "per3"):
                m, i = "m_"+ring, "i_"+ring
                if m+"_lb" not in b:
                    continue
                put(m+"_ub", a); put(i+"_ub", a)
                for src, dst in ((m, i), (i, m)):
                    for end, other in (("lb", "ub"), ("ub", "lb")):
                        if src+"_"+end in b:
                            put(dst+"_"+other, a-b[src+"_"+end])
        if "h_pad_ub" in b:
            put("m_pad_ub", b["h_pad_ub"])
        if "m_pad_ub" in b and "m_det_lb" in b:
            put("D_ub", b["m_pad_ub"]-b["m_det_lb"])
        if "m_pad_lb" in b and "m_det_ub" in b:
            put("D_lb", b["m_pad_lb"]-b["m_det_ub"])
        if "i_det_ub" in b and "i_pad_lb" in b:
            put("D_ub", b["i_det_ub"]-b["i_pad_lb"])
        if "i_det_lb" in b and "i_pad_ub" in b:
            put("D_lb", b["i_det_lb"]-b["i_pad_ub"])
        if old == b:
            break
    if "m_pad_ub" in b:
        b["U_pad_ub"] = b["m_pad_ub"]
    for k, v in b.items():
        if not k.startswith("D_") and v < 0:
            raise ValueError("inconsistent negative multiplicity bound")
        if k.endswith("_lb") and k[:-3]+"_ub" in b and v > b[k[:-3]+"_ub"]:
            raise ValueError("inconsistent bounds for " + k[:-3])


def verify_native(cert):
    if not __debug__:
        raise ValueError("native verifier requires assertions enabled; do not use python -O")
    if cert.get("format") != "b14-10-catalecticant/1":
        raise ValueError("unsupported native format; retain RECORDED")
    spec = importlib.util.spec_from_file_location("b15_11_recover", ROOT/"analysis/b14_10/recover.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.verify(cert, check_hwv=True)
    return dict(status="REPLAYED_RANK_FLOOR", m_per3_lb=1,
                source_integral=True, fresh="per3 pencil, coefficient matrix, integer HWV and nonzero determinant",
                inherited="top_cells_catalecticant ambient dimension theorem")


def normalize_record(raw, model, c, source):
    """Astra/Claude provenance is orthogonal to mathematical admissibility."""
    if model not in ("gpt-6-astra", "claude-opus-5"):
        raise ValueError("unregistered model attribution")
    validate(c)
    return dict(schema="b15-evidence/1", cell=c, producer_model=model,
                source=source, status="RECORDED", raw=copy.deepcopy(raw),
                raw_sha256=canonical_digest(raw), usable_for_bounds=False)


def validate_record(record):
    fields = {"schema", "cell", "producer_model", "source", "status", "raw", "raw_sha256", "usable_for_bounds"}
    if not isinstance(record, dict) or set(record) != fields:
        raise ValueError("observation fields differ from b15-evidence/1")
    validate(record["cell"])
    if record["schema"] != "b15-evidence/1" or record["producer_model"] not in ("gpt-6-astra", "claude-opus-5"):
        raise ValueError("invalid schema or model attribution")
    if record["status"] != "RECORDED" or record["usable_for_bounds"] is not False:
        raise ValueError("record cannot self-authorize mathematical bounds")
    if not isinstance(record["source"], str) or not record["source"] or record["raw_sha256"] != canonical_digest(record["raw"]):
        raise ValueError("record source or content digest invalid")


def coordinate_transport(*, ring, irreducibility_proof, multiplier_witness,
                         source_floor_lb, evaluated_multiplier):
    """Low-level checked implication, never automatically authorized by query.

    The caller must supply a validated witness on this same variety. A bool or
    ambient nonzero assertion is deliberately insufficient.
    """
    if ring not in ("det", "pad", "per3") or irreducibility_proof != "GL_orbit_closure_irreducible":
        raise ValueError("irreducible variety proof required")
    if not isinstance(multiplier_witness, dict) or multiplier_witness.get("ring") != ring:
        raise ValueError("multiplier witness must lie on the same variety")
    # u=n! times the leading coefficient. These integer matrices construct an
    # actual point of the indicated orbit closure; no membership flag is read.
    matrix = multiplier_witness.get("first_variable_matrix")
    size = 4 if ring == "det" else 3
    if not isinstance(matrix, list) or len(matrix) != size or any(not isinstance(r, list) or len(r) != size or any(type(x) is not int for x in r) for r in matrix):
        raise ValueError("native first-variable matrix required")
    total = 0
    for perm in itertools.permutations(range(size)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(size) for j in range(i+1, size)) if ring == "det" else 1
        total += sign*math.prod(matrix[i][perm[i]] for i in range(size))
    if ring == "pad":
        z = multiplier_witness.get("independent_linear_first_coefficient")
        if type(z) is not int:
            raise ValueError("independent padding linear form required")
        total *= z
    total *= math.factorial(3 if ring == "per3" else 4)
    if type(evaluated_multiplier) is not int or total != evaluated_multiplier or total == 0:
        raise ValueError("native nonzero multiplier evaluation required")
    if type(source_floor_lb) is not int or source_floor_lb < 0:
        raise ValueError("invalid rank floor")
    return source_floor_lb


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cell", required=True, help="JSON file with complete b15-evidence/1 cell")
    p.add_argument("--certificate", action="append", default=[])
    p.add_argument("--record", action="append", default=[])
    a = p.parse_args()
    read = lambda f: json.loads(Path(f).read_text(encoding="utf-8"))
    print(json.dumps(Memory().query(read(a.cell), [read(x) for x in a.record],
                                   [read(x) for x in a.certificate]), indent=2))


if __name__ == "__main__":
    main()
