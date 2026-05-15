# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Dedicated visualisation model for cell-cycle SBML labs."""
from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec


_GROUP_TITLES = {
    "checkpoint": ("Checkpoint and stress response", "Checkpoint and stress-response variables over time."),
    "g1s": ("G1/S commitment gate", "Rb/E2F, Cyclin D/E, CDK2, and inhibitor markers over time."),
    "mitosis": ("Mitotic switch and exit", "CDK, APC/C, Cdc20/Cdh1, Wee1, Cdc25, and Plk markers over time."),
    "replication": ("Growth, DNA, and division markers", "Mass, DNA replication, budding, and division markers over time."),
    "calcium": ("Calcium and second-messenger response", "ATP, IP3, calcium, and linked signalling variables over time."),
    "proteostasis": ("Proteostasis and aging stress", "Chaperone, aggregate, and proteostasis-linked cell-cycle variables over time."),
    "core": ("Core model states", "Conservative trace of source-defined model states that do not map cleanly to a named module."),
}


def _signal_value(signal: BioSignal | None) -> Any:
    if signal is None:
        return None
    value = getattr(signal, "value", signal)
    if isinstance(value, Mapping) and set(value.keys()) == {"payload"}:
        return value["payload"]
    return value


def _float_or_none(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def _safe_title(value: Any, fallback: str) -> str:
    text = str(value or "").strip()
    return text or fallback


class CellCycleVisualisationModel(BioModule):
    """Render active, lab-specific visual summaries from cell-cycle model signals."""

    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = str(lab_title)
        self.question = str(question)
        self.answer_focus = str(answer_focus)
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._time = 0.0
        self._history: dict[str, list[dict[str, float]]] = {}
        self._latest_summary: dict[str, Mapping[str, Any]] = {}
        self._latest_labels: dict[str, dict[str, str]] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        summary_schema = {
            "duration_simulated": "float",
            "observable_count": "int",
            "largest_change_observable": "str",
            "largest_change_magnitude": "float",
            "peak_observable": "str",
            "peak_value": "float",
        }
        for source in self.sources:
            alias = str(source["alias"])
            observables = [
                str(item.get("id"))
                for item in source.get("observables", []) or []
                if isinstance(item, Mapping) and item.get("id")
            ]
            state_schema = {name: "float" for name in observables} or {"payload": "json"}
            label_schema = {name: "str" for name in observables} or {"payload": "json"}
            specs[f"{alias}_state"] = SignalSpec.record(
                schema=state_schema,
                description=f"Full state feed from {_safe_title(source.get('title'), alias)}.",
            )
            specs[f"{alias}_summary"] = SignalSpec.record(
                schema=summary_schema,
                description=f"Run summary feed from {_safe_title(source.get('title'), alias)}.",
            )
            specs[f"{alias}_species_labels"] = SignalSpec.record(
                schema=label_schema,
                description=f"Display label feed from {_safe_title(source.get('title'), alias)}.",
            )
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self.reset()

    def reset(self) -> None:
        self._inputs = {}
        self._time = 0.0
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._latest_summary = {}
        self._latest_labels = {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        self._time = float(end)
        for source in self.sources:
            self._capture_source(str(source["alias"]), self._time)

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            history = self._history.get(alias) or []
            if not history:
                continue
            visuals.append(self._question_answer_visual(alias, source, history))
            visuals.extend(self._grouped_timeseries_visuals(alias, source, history))
            excursion = self._largest_excursions_visual(alias, source, history)
            if excursion is not None:
                visuals.append(excursion)
            endpoint = self._endpoint_snapshot_visual(alias, source, history)
            if endpoint is not None:
                visuals.append(endpoint)
            portrait = self._phase_portrait_visual(alias, source, history)
            if portrait is not None:
                visuals.append(portrait)
        return visuals or None

    def _capture_source(self, alias: str, emitted_at: float) -> None:
        state = _signal_value(self._inputs.get(f"{alias}_state"))
        if isinstance(state, Mapping):
            row: dict[str, float] = {"t": float(getattr(self._inputs.get(f"{alias}_state"), "emitted_at", emitted_at))}
            for key, value in state.items():
                number = _float_or_none(value)
                if number is not None:
                    row[str(key)] = number
            history = self._history.setdefault(alias, [])
            if len(row) > 1 and (not history or abs(row["t"] - history[-1].get("t", -1.0)) > 1e-12):
                history.append(row)

        summary = _signal_value(self._inputs.get(f"{alias}_summary"))
        if isinstance(summary, Mapping):
            self._latest_summary[alias] = dict(summary)

        labels = _signal_value(self._inputs.get(f"{alias}_species_labels"))
        if isinstance(labels, Mapping):
            self._latest_labels[alias] = {str(k): str(v) for k, v in labels.items()}

    def _observables_for_source(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> list[dict[str, str]]:
        latest = history[-1]
        configured = []
        for item in source.get("observables", []) or []:
            if not isinstance(item, Mapping):
                continue
            obs_id = str(item.get("id") or "")
            if obs_id and obs_id in latest:
                configured.append({
                    "id": obs_id,
                    "label": str(item.get("label") or self._latest_labels.get(alias, {}).get(obs_id) or obs_id),
                    "group": str(item.get("group") or "core"),
                })
        if configured:
            return configured
        return [
            {"id": key, "label": self._latest_labels.get(alias, {}).get(key, key), "group": "core"}
            for key in latest
            if key != "t"
        ]

    def _question_answer_visual(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> dict[str, Any]:
        observables = self._observables_for_source(alias, source, history)
        summary = self._latest_summary.get(alias, {})
        label_by_id = {item["id"]: item["label"] for item in observables}
        largest = str(summary.get("largest_change_observable") or "")
        peak = str(summary.get("peak_observable") or "")
        duration = float(history[-1].get("t", 0.0)) - float(history[0].get("t", 0.0))
        largest_answer = label_by_id.get(largest, largest or "No dominant mover detected")
        peak_answer = label_by_id.get(peak, peak or "No peak detected")
        change = _float_or_none(summary.get("largest_change_magnitude"))
        active_groups = self._active_groups(observables, history)
        if change is None or abs(change) < 1e-12:
            answer = "No meaningful dynamic excursion was detected under the current baseline inputs."
            evidence = "The state values stayed near their initial levels across the sampled run window."
        else:
            answer = f"Yes, the run shows measurable activity led by {largest_answer}."
            evidence = f"{largest_answer} had the largest excursion ({change:.4g}); the largest peak was {peak_answer}."
        caveat = "Values are native SBML quantities; interpretation preserves the bundled model and does not re-fit or rewrite equations."
        rows = [
            ["Scientific question", self.question],
            ["Observed answer", answer],
            ["Evidence", evidence],
            ["Dominant module", active_groups or "No single module dominated the baseline run."],
            ["Caveat", caveat],
        ]
        return {
            "render": "table",
            "description": "Direct scientific answer for this lab run.",
            "data": {"title": f"{self.lab_title} - run interpretation", "columns": ["Prompt", "Answer"], "rows": rows},
        }

    def _grouped_timeseries_visuals(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> list[dict[str, Any]]:
        observables = self._observables_for_source(alias, source, history)
        by_group: dict[str, list[dict[str, str]]] = {}
        for item in observables:
            by_group.setdefault(item["group"], []).append(item)
        visuals: list[dict[str, Any]] = []
        for group in ("checkpoint", "g1s", "mitosis", "replication", "calcium", "proteostasis", "core"):
            items = by_group.get(group) or []
            ranked = [item for item in sorted(items, key=lambda item: self._range(history, item["id"]), reverse=True) if self._has_points(history, item["id"])][:8]
            if not ranked:
                continue
            title, description = _GROUP_TITLES.get(group, _GROUP_TITLES["core"])
            series = [
                {
                    "name": item["label"],
                    "points": [[point["t"], point[item["id"]]] for point in history if item["id"] in point],
                }
                for item in ranked
            ]
            series = [entry for entry in series if entry["points"]]
            if not series:
                continue
            visuals.append({
                "render": "timeseries",
                "description": description,
                "data": {
                    "title": f"{_safe_title(source.get('title'), alias)} - {title}",
                    "x_label": "Model time",
                    "y_label": "Native SBML value",
                    "series": series,
                },
            })
            if len(visuals) >= 4:
                break
        return visuals

    def _largest_excursions_visual(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> dict[str, Any] | None:
        observables = self._observables_for_source(alias, source, history)
        ranked = sorted(observables, key=lambda item: self._range(history, item["id"]), reverse=True)[:10]
        items = [{"label": item["label"], "value": self._range(history, item["id"])} for item in ranked if self._range(history, item["id"]) > 0]
        if not items:
            return None
        return {
            "render": "bar",
            "description": "Variables ranked by within-run excursion.",
            "data": {
                "title": f"{_safe_title(source.get('title'), alias)} - largest activity ranges",
                "items": items,
                "x_label": "Model variable",
                "y_label": "Max-min range",
            },
        }

    def _endpoint_snapshot_visual(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> dict[str, Any] | None:
        observables = self._observables_for_source(alias, source, history)
        latest = history[-1]
        ranked = sorted(
            [item for item in observables if item["id"] in latest],
            key=lambda item: abs(float(latest.get(item["id"], 0.0))),
            reverse=True,
        )[:10]
        items = [{"label": item["label"], "value": float(latest.get(item["id"], 0.0))} for item in ranked if abs(float(latest.get(item["id"], 0.0))) > 0]
        if not items:
            return None
        return {
            "render": "bar",
            "description": "Final-state composition view for the most abundant tracked variables.",
            "data": {
                "title": f"{_safe_title(source.get('title'), alias)} - final state snapshot",
                "items": items,
                "x_label": "Model variable",
                "y_label": "Final native SBML value",
            },
        }

    def _phase_portrait_visual(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> dict[str, Any] | None:
        observables = sorted(
            self._observables_for_source(alias, source, history),
            key=lambda item: self._range(history, item["id"]),
            reverse=True,
        )
        if len(observables) < 2:
            return None
        x_item, y_item = observables[0], observables[1]
        if self._range(history, x_item["id"]) <= 0 or self._range(history, y_item["id"]) <= 0:
            return None
        points = [
            {"x": point[x_item["id"]], "y": point[y_item["id"]], "series": "trajectory"}
            for point in history
            if x_item["id"] in point and y_item["id"] in point
        ]
        if not points:
            return None
        return {
            "render": "scatter",
            "description": "Phase portrait connecting the two most active observables during this run.",
            "data": {
                "title": f"{_safe_title(source.get('title'), alias)} - activity phase portrait",
                "x_label": x_item["label"],
                "y_label": y_item["label"],
                "connect_points": True,
                "points": points,
            },
        }

    def _active_groups(self, observables: list[dict[str, str]], history: list[dict[str, float]]) -> str:
        ranges: dict[str, float] = {}
        for item in observables:
            ranges[item["group"]] = ranges.get(item["group"], 0.0) + self._range(history, item["id"])
        ranked = [group for group, value in sorted(ranges.items(), key=lambda pair: pair[1], reverse=True) if value > 0]
        labels = [_GROUP_TITLES.get(group, _GROUP_TITLES["core"])[0] for group in ranked[:3]]
        return ", ".join(labels)

    @staticmethod
    def _has_points(history: list[dict[str, float]], key: str) -> bool:
        return any(key in point for point in history)

    @staticmethod
    def _range(history: list[dict[str, float]], key: str) -> float:
        values = [float(point[key]) for point in history if key in point]
        if not values:
            return 0.0
        return max(values) - min(values)
