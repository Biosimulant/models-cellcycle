from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path
from typing import Any, Mapping

import yaml

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"

SHORT_NAME_RE = re.compile(r"^[a-z]{1,2}\d?$")
APPROVED_SHORT_PORTS = {
    "ap1",
    "atm",
    "atr",
    "dna",
    "e2f",
    "ip3",
    "mpf",
    "myc",
    "p21",
    "p27",
    "p53",
    "rb",
}
GERARD_FORBIDDEN_PORTS = {"cd", "mdi", "md", "ce", "ca", "cb", "p_rbp", "p_rbpp"}


def _ensure_paths(model_dir: Path | None = None) -> None:
    for candidate in (ROOT, ROOT.parent, *ROOT.parents):
        for src in (candidate / "biosim" / "src", candidate / "bsim-active" / "biosim" / "src"):
            if (src / "biosim").is_dir() and str(src) not in sys.path:
                sys.path.insert(0, str(src))
    if model_dir is not None and str(model_dir) not in sys.path:
        sys.path.insert(0, str(model_dir))


_ensure_paths()

from biosim import BioModule  # noqa: E402
from biosim.signals import RecordSignal  # noqa: E402


def _load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    assert isinstance(data, dict), f"{path} root must be a mapping"
    return data


def _split_entrypoint(entrypoint: str) -> tuple[str, str]:
    module_name, attr = entrypoint.split(":", 1) if ":" in entrypoint else entrypoint.rsplit(".", 1)
    return module_name, attr


def _public_ports(manifest: Mapping[str, Any]) -> list[str]:
    io = manifest.get("io") if isinstance(manifest.get("io"), Mapping) else {}
    ports: list[str] = []
    for direction in ("inputs", "outputs"):
        entries = io.get(direction) if isinstance(io.get(direction), list) else []
        ports.extend(str(item.get("name")) for item in entries if isinstance(item, Mapping) and item.get("name"))
    return ports


def _assert_user_facing_ports(path: Path, manifest: Mapping[str, Any]) -> None:
    for name in _public_ports(manifest):
        assert name == name.strip().lower(), f"{path}: public port is not lower-case snake_case: {name}"
        assert " " not in name and "-" not in name, f"{path}: public port is not snake_case: {name}"
        assert not (
            SHORT_NAME_RE.match(name) and name not in APPROVED_SHORT_PORTS
        ), f"{path}: abbreviated public port should be renamed or marked conservatively: {name}"


def test_all_public_ports_are_user_facing_and_gerard_ports_are_renamed() -> None:
    failures: list[str] = []
    for lab_dir in sorted(p for p in LABS.iterdir() if p.is_dir()):
        for manifest_path in (lab_dir / "lab.yaml", lab_dir / "models" / "core" / "model.yaml"):
            try:
                manifest = _load_yaml(manifest_path)
                _assert_user_facing_ports(manifest_path, manifest)
                if lab_dir.name == "gerard2009-integrated-mammalian-cell-cycle":
                    exposed = set(_public_ports(manifest))
                    forbidden = sorted(exposed & GERARD_FORBIDDEN_PORTS)
                    assert not forbidden, f"{manifest_path}: Gerard2009 still exposes {forbidden}"
            except AssertionError as exc:
                failures.append(str(exc))
    assert not failures, "\n".join(failures)


def test_visualisation_manifests_reference_model_ports_and_lab_specific_questions() -> None:
    failures: list[str] = []
    old_question = "Which variables carry the main cell-cycle activity in this SBML model?"
    for lab_dir in sorted(p for p in LABS.iterdir() if p.is_dir()):
        try:
            model_manifest = _load_yaml(lab_dir / "models" / "core" / "model.yaml")
            visual_manifest = _load_yaml(lab_dir / "models" / "visualisation" / "model.yaml")
            model_outputs = set(_public_ports(model_manifest))
            init_kwargs = visual_manifest["biosim"]["init_kwargs"]

            question = str(init_kwargs.get("question") or "")
            assert question and question != old_question, f"{lab_dir}: visual question is generic"
            assert not question.lower().startswith("which variables carry"), f"{lab_dir}: visual question is generic"

            sources = init_kwargs.get("sources")
            assert isinstance(sources, list) and sources, f"{lab_dir}: visual sources missing"
            for source in sources:
                for observable in source.get("observables", []) or []:
                    port = observable.get("port")
                    assert port in model_outputs, f"{lab_dir}: visual observable port {port!r} is not a model output"
                    label = str(observable.get("label") or "")
                    assert label and label != str(observable.get("id") or ""), (
                        f"{lab_dir}: visual observable {observable.get('id')!r} lacks a friendly label"
                    )
        except AssertionError as exc:
            failures.append(str(exc))
    assert not failures, "\n".join(failures)


def test_visualisation_entrypoints_instantiate_biomodules_and_emit_renderable_payloads() -> None:
    failures: list[str] = []
    for lab_dir in sorted(p for p in LABS.iterdir() if p.is_dir()):
        model_dir = lab_dir / "models" / "visualisation"
        try:
            _ensure_paths(model_dir)
            manifest = _load_yaml(model_dir / "model.yaml")
            module_name, attr = _split_entrypoint(manifest["biosim"]["entrypoint"])
            for key in [k for k in sys.modules if k == module_name or k.startswith(f"{module_name}.")]:
                sys.modules.pop(key, None)
            importlib.invalidate_caches()
            module = importlib.import_module(module_name)
            cls = getattr(module, attr)
            visualisation = cls(**manifest["biosim"]["init_kwargs"])
            assert isinstance(visualisation, BioModule), f"{lab_dir}: visualisation is not a BioModule"

            visualisation.setup()
            source = manifest["biosim"]["init_kwargs"]["sources"][0]
            alias = source["alias"]
            observables = source["observables"][:4]
            assert observables, f"{lab_dir}: no configured visual observables"
            labels = {item["id"]: item["label"] for item in observables}
            state0 = {item["id"]: float(idx + 1) for idx, item in enumerate(observables)}
            state1 = {item["id"]: float(idx + 2) * 1.5 for idx, item in enumerate(observables)}
            summary = {
                "duration_simulated": 1.0,
                "observable_count": len(observables),
                "largest_change_observable": observables[0]["id"],
                "largest_change_magnitude": 1.0,
                "peak_observable": observables[-1]["id"],
                "peak_value": state1[observables[-1]["id"]],
            }
            visualisation.set_inputs({
                f"{alias}_state": RecordSignal("test", f"{alias}_state", state0, 0.0),
                f"{alias}_summary": RecordSignal("test", f"{alias}_summary", summary, 0.0),
                f"{alias}_species_labels": RecordSignal("test", f"{alias}_species_labels", labels, 0.0),
            })
            visualisation.advance_window(0.0, 0.0)
            visualisation.set_inputs({
                f"{alias}_state": RecordSignal("test", f"{alias}_state", state1, 1.0),
                f"{alias}_summary": RecordSignal("test", f"{alias}_summary", summary, 1.0),
                f"{alias}_species_labels": RecordSignal("test", f"{alias}_species_labels", labels, 1.0),
            })
            visualisation.advance_window(0.0, 1.0)
            visuals = visualisation.visualize()

            assert isinstance(visuals, list) and visuals, f"{lab_dir}: no visuals emitted"
            table_rows = []
            for visual in visuals:
                render = visual.get("render")
                data = visual.get("data")
                assert isinstance(data, Mapping), f"{lab_dir}: {render} visual lacks data mapping"
                if render == "bar":
                    assert data.get("items"), f"{lab_dir}: bar visual lacks desktop-compatible data.items"
                    assert "categories" not in data and "values" not in data, f"{lab_dir}: bar visual uses old schema"
                elif render == "timeseries":
                    assert data.get("series"), f"{lab_dir}: timeseries visual has no series"
                    assert all(series.get("points") for series in data["series"]), f"{lab_dir}: timeseries has empty series"
                elif render == "scatter":
                    assert data.get("points"), f"{lab_dir}: scatter visual has no points"
                elif render == "table":
                    rows = data.get("rows")
                    assert rows, f"{lab_dir}: table visual has no rows"
                    table_rows.extend(rows)
                else:
                    raise AssertionError(f"{lab_dir}: unsupported visual render type {render!r}")

            prompts = [row[0] for row in table_rows if isinstance(row, list) and row]
            assert "Observed answer" in prompts, f"{lab_dir}: Q/A table lacks an Observed answer row"
            assert "Question" not in prompts, f"{lab_dir}: Q/A table still uses Question -> question pattern"
        except AssertionError as exc:
            failures.append(str(exc))
        finally:
            if sys.path and sys.path[0] == str(model_dir):
                sys.path.pop(0)
    assert not failures, "\n".join(failures)
