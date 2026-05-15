from __future__ import annotations

import importlib
import sys
from pathlib import Path

import yaml

from biosim import BioModule
from biosim.signals import RecordSignal


_MODEL_DIR = Path(__file__).resolve().parents[1]


def _ensure_paths() -> None:
    model_dir = str(_MODEL_DIR)
    if model_dir not in sys.path:
        sys.path.insert(0, model_dir)
    for parent in [_MODEL_DIR, *_MODEL_DIR.parents]:
        for candidate in (parent / "biosim" / "src", parent / "bsim-active" / "biosim" / "src"):
            if (candidate / "biosim").is_dir() and str(candidate) not in sys.path:
                sys.path.insert(0, str(candidate))
                return


def test_cellcycle_visualisation_renders_multiple_activity_views() -> None:
    _ensure_paths()
    manifest = yaml.safe_load((_MODEL_DIR / "model.yaml").read_text())
    module_name, attr = manifest["biosim"]["entrypoint"].split(":", 1)
    module = importlib.import_module(module_name)
    cls = getattr(module, attr)
    visualisation = cls(**manifest["biosim"]["init_kwargs"])
    assert isinstance(visualisation, BioModule)
    visualisation.setup()
    alias = manifest["biosim"]["init_kwargs"]["sources"][0]["alias"]
    observables = manifest["biosim"]["init_kwargs"]["sources"][0]["observables"][:4]
    state0 = {item["id"]: float(idx + 1) for idx, item in enumerate(observables)}
    state1 = {item["id"]: float(idx + 2) * 1.5 for idx, item in enumerate(observables)}
    labels = {item["id"]: item["label"] for item in observables}
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
    assert isinstance(visuals, list)
    assert len(visuals) >= 3
    renders = {visual["render"] for visual in visuals}
    assert {"table", "timeseries", "bar"}.issubset(renders)
    for visual in visuals:
        if visual["render"] == "bar":
            assert visual["data"].get("items")
            assert "categories" not in visual["data"]
            assert "values" not in visual["data"]
        if visual["render"] == "table":
            rows = visual["data"].get("rows", [])
            prompts = [row[0] for row in rows if isinstance(row, list) and row]
            assert "Observed answer" in prompts
            assert "Question" not in prompts
