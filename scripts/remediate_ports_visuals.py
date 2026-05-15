#!/usr/bin/env python3
"""Remediate public cell-cycle ports and generated visualisation payloads.

This script is intentionally deterministic. It keeps SBML symbols untouched and
only changes Biosimulant-facing port IDs, labels, descriptions, and generated
visualisation payloads.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any, Mapping

import yaml


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"

COMPAT_OUTPUTS = {"state", "summary", "species_labels"}
COMMON_ALLOWED_SHORT = {
    "ap1",
    "atm",
    "atr",
    "bud",
    "dna",
    "e2f",
    "gf",
    "ip3",
    "mpf",
    "myc",
    "p21",
    "p27",
    "p53",
    "rb",
}

GERARD2009_SYMBOLS: dict[str, tuple[str, str, str]] = {
    "GF": ("growth_factor", "Growth factor", "External growth-factor stimulus."),
    "Kagf": ("growth_factor_activation_rate", "Growth factor activation rate", "Growth-factor activation parameter."),
    "pRB": ("phosphorylated_rb", "Phosphorylated Rb", "Rb phosphorylation state."),
    "pRBp": ("singly_phosphorylated_rb", "Singly phosphorylated Rb", "Intermediate phosphorylated Rb state."),
    "pRBpp": ("hyperphosphorylated_rb", "Hyperphosphorylated Rb", "Hyperphosphorylated Rb state."),
    "E2F": ("e2f", "E2F transcription factor", "E2F transcription-factor pool."),
    "E2Fp": ("phosphorylated_e2f", "Phosphorylated E2F", "Phosphorylated E2F pool."),
    "pRBc1": ("rb_e2f_complex", "Rb-E2F complex", "Rb-E2F inhibitory complex."),
    "pRBc2": ("phosphorylated_rb_e2f_complex", "Phosphorylated Rb-E2F complex", "Phosphorylated Rb-E2F complex."),
    "Cd": ("cyclin_d", "Cyclin D", "Cyclin D module species."),
    "Mdi": ("inactive_cyclin_d_cdk_complex", "Inactive Cyclin D-CDK4/6 complex", "Inactive Cyclin D-CDK4/6 module complex."),
    "Md": ("active_cyclin_d_cdk_complex", "Active Cyclin D-CDK4/6 complex", "Active Cyclin D-CDK4/6 module complex."),
    "Mdp27": ("cyclin_d_cdk_p27_complex", "Cyclin D-CDK4/6-p27 complex", "Cyclin D-CDK4/6 complex bound to p27."),
    "Ce": ("cyclin_e", "Cyclin E", "Cyclin E module species."),
    "Mei": ("inactive_cyclin_e_cdk2_complex", "Inactive Cyclin E-CDK2 complex", "Inactive Cyclin E-CDK2 module complex."),
    "Me": ("active_cyclin_e_cdk2_complex", "Active Cyclin E-CDK2 complex", "Active Cyclin E-CDK2 module complex."),
    "Skp2": ("skp2", "Skp2 ubiquitin-ligase adaptor", "Skp2 p27-degradation regulator."),
    "Mep27": ("cyclin_e_cdk2_p27_complex", "Cyclin E-CDK2-p27 complex", "Cyclin E-CDK2 complex bound to p27."),
    "Pei": ("inactive_cyclin_e_module_regulator", "Inactive Cyclin E module regulator", "Inactive regulator in the Cyclin E-CDK2 module."),
    "Pe": ("active_cyclin_e_module_regulator", "Active Cyclin E module regulator", "Active regulator in the Cyclin E-CDK2 module."),
    "Ca": ("cyclin_a", "Cyclin A", "Cyclin A module species."),
    "Mai": ("inactive_cyclin_a_cdk2_complex", "Inactive Cyclin A-CDK2 complex", "Inactive Cyclin A-CDK2 module complex."),
    "Ma": ("active_cyclin_a_cdk2_complex", "Active Cyclin A-CDK2 complex", "Active Cyclin A-CDK2 module complex."),
    "Map27": ("cyclin_a_cdk2_p27_complex", "Cyclin A-CDK2-p27 complex", "Cyclin A-CDK2 complex bound to p27."),
    "p27": ("p27", "p27 CDK inhibitor", "p27 CDK inhibitor pool."),
    "p27p": ("phosphorylated_p27", "Phosphorylated p27", "Phosphorylated p27 pool."),
    "Cdh1i": ("inactive_cdh1", "Inactive Cdh1", "Inactive Cdh1 APC/C regulator."),
    "Cdh1a": ("active_cdh1", "Active Cdh1", "Active Cdh1 APC/C regulator."),
    "Pai": ("inactive_cyclin_a_module_regulator", "Inactive Cyclin A module regulator", "Inactive regulator in the Cyclin A-CDK2 module."),
    "Pa": ("active_cyclin_a_module_regulator", "Active Cyclin A module regulator", "Active regulator in the Cyclin A-CDK2 module."),
    "Cb": ("cyclin_b", "Cyclin B", "Cyclin B module species."),
    "Mbi": ("inactive_cyclin_b_cdk1_complex", "Inactive Cyclin B-CDK1 complex", "Inactive Cyclin B-CDK1 module complex."),
    "Mb": ("active_cyclin_b_cdk1_complex", "Active Cyclin B-CDK1 complex", "Active Cyclin B-CDK1 module complex."),
    "Mbp27": ("cyclin_b_cdk1_p27_complex", "Cyclin B-CDK1-p27 complex", "Cyclin B-CDK1 complex bound to p27."),
    "Cdc20i": ("inactive_cdc20", "Inactive Cdc20", "Inactive Cdc20 APC/C regulator."),
    "Cdc20a": ("active_cdc20", "Active Cdc20", "Active Cdc20 APC/C regulator."),
    "Pbi": ("inactive_cyclin_b_module_regulator", "Inactive Cyclin B module regulator", "Inactive regulator in the Cyclin B-CDK1 module."),
    "Pb": ("active_cyclin_b_module_regulator", "Active Cyclin B module regulator", "Active regulator in the Cyclin B-CDK1 module."),
    "Wee1": ("wee1", "Wee1 inhibitory kinase", "Wee1 CDK inhibitory kinase."),
    "Wee1p": ("phosphorylated_wee1", "Phosphorylated Wee1", "Phosphorylated Wee1 pool."),
    "Pol": ("dna_polymerase", "DNA polymerase", "DNA polymerase replication marker."),
    "Cdc45": ("cdc45", "Cdc45 replication factor", "Cdc45 replication-initiation marker."),
    "Primer": ("replication_primer", "Replication primer", "DNA replication primer marker."),
    "Chk1": ("chk1", "Chk1 checkpoint kinase", "Chk1 checkpoint kinase."),
    "ATR": ("atr", "ATR checkpoint kinase", "ATR checkpoint kinase."),
    "AP1": ("ap1", "AP1 transcription factor", "AP1 growth-response transcription factor."),
    "Mw": ("wee1_module_regulator", "Wee1 module regulator", "Wee1-linked regulatory model state."),
}

SYMBOL_LABELS: dict[str, str] = {
    "AAE": "Aggregated APC/C enzyme state",
    "ACT": "Active regulatory state",
    "ACTt": "Total active regulatory state",
    "Agg": "Protein aggregate burden",
    "AP1": "AP1 transcription factor",
    "APCC": "APC/C complex",
    "ATM": "ATM checkpoint kinase",
    "ATR": "ATR checkpoint kinase",
    "BCC": "BubR1-Cdc20 checkpoint complex",
    "Bck2": "Bck2 G1 regulator",
    "BCK2": "Bck2 G1 regulator",
    "BCKI": "B-type cyclin CDK inhibitor",
    "Bfa1": "Bfa1 spindle checkpoint GAP",
    "Bfa1P4": "Bfa1 phosphorylated state P4",
    "Bfa1P5": "Bfa1 phosphorylated state P5",
    "BUD": "Budding index",
    "CDC14": "Cdc14 phosphatase",
    "CDC14T": "Total Cdc14 phosphatase",
    "CDC15": "Cdc15 mitotic exit kinase",
    "Cdc20": "Cdc20 APC/C activator",
    "Cdc20t": "Total Cdc20 APC/C activator",
    "Cdc20T": "Total Cdc20 APC/C activator",
    "Cdc25": "Cdc25 activating phosphatase",
    "Cdc45": "Cdc45 replication factor",
    "CDC6": "Cdc6 replication licensing factor",
    "CDC6T": "Total Cdc6 replication licensing factor",
    "Cdh1": "Cdh1 APC/C activator",
    "CDH1": "Cdh1 APC/C activator",
    "Cdh1p": "Phosphorylated Cdh1",
    "CDK": "Cyclin-dependent kinase activity",
    "Chk1": "Chk1 checkpoint kinase",
    "CKI": "Cyclin-dependent kinase inhibitor",
    "CKIT": "Total cyclin-dependent kinase inhibitor",
    "CKIt": "Total cyclin-dependent kinase inhibitor",
    "Clb2": "Clb2 mitotic cyclin",
    "CLB2": "Clb2 mitotic cyclin",
    "CLB2T": "Total Clb2 mitotic cyclin",
    "Clb5": "Clb5 S-phase cyclin",
    "CLB5": "Clb5 S-phase cyclin",
    "CLB5T": "Total Clb5 S-phase cyclin",
    "Cln": "G1 cyclin pool",
    "Cln2": "Cln2 G1 cyclin",
    "CLN2": "Cln2 G1 cyclin",
    "Cln3": "Cln3 Start cyclin",
    "CLN3": "Cln3 Start cyclin",
    "Cln3F": "Folded Cln3 Start cyclin",
    "Cln3U": "Unfolded Cln3 Start cyclin",
    "Count": "Division event counter",
    "CtrA": "CtrA cell-cycle regulator",
    "Cyclin": "Cyclin pool",
    "DivK": "DivK polarity regulator",
    "DNA": "DNA replication state",
    "DnaA": "DnaA replication initiator",
    "DRG": "Delayed response gene module",
    "E2F": "E2F transcription factor",
    "E2F1": "E2F1 transcription factor",
    "E2Fm": "E2F mRNA",
    "E2FRB": "E2F-Rb complex",
    "Effectoract": "Active checkpoint effector",
    "Effectorina": "Inactive checkpoint effector",
    "Elong": "Cell elongation state",
    "Emi1": "Emi1 APC/C inhibitor",
    "Emi1Cdh1": "Emi1-Cdh1 complex",
    "Emi1Cdh1p": "Emi1-phosphorylated Cdh1 complex",
    "ERG": "Early response gene module",
    "ESP1": "Esp1 separase",
    "Fts": "FtsZ division marker",
    "GcrA": "GcrA transcriptional regulator",
    "Hct1": "Hct1 APC/C activator",
    "Ini": "Replication initiation state",
    "Kip1": "Kip1 CDK inhibitor",
    "Let7TOT": "Total let-7 microRNA",
    "LTE1": "Lte1 mitotic exit regulator",
    "Mad": "Mad spindle checkpoint signal",
    "MAD2": "Mad2 spindle checkpoint protein",
    "MASS": "Cell mass",
    "Mass": "Cell mass",
    "MBF": "MBF transcription factor",
    "MCC": "Mitotic checkpoint complex",
    "Mcm": "MCM replication licensing complex",
    "Mcm1": "Mcm1 transcription factor",
    "Mih1": "Mih1 activating phosphatase",
    "Mih1a": "Active Mih1 phosphatase",
    "Mik1": "Mik1 inhibitory kinase",
    "MPF": "Maturation-promoting factor",
    "Myc": "Myc transcription factor",
    "NET1": "Net1 nucleolar Cdc14 anchor",
    "NET1T": "Total Net1 nucleolar Cdc14 anchor",
    "NFY": "NF-Y transcription factor",
    "NHEJ": "Non-homologous end joining repair state",
    "Oli": "Oligomerized proteostasis species",
    "ORI": "Replication origin state",
    "P27": "p27 CDK inhibitor",
    "p27": "p27 CDK inhibitor",
    "p53": "p53 tumor suppressor",
    "PClb2": "Phosphorylated Clb2",
    "PDS1": "Pds1 securin",
    "PPX": "PPX phosphatase",
    "Prot": "Protein load",
    "PSwe1": "Phosphorylated Swe1",
    "PSwe1M": "Membrane-associated phosphorylated Swe1",
    "PTrim": "Phosphorylated trimer complex",
    "Rb": "Rb tumor suppressor",
    "RENT": "RENT Cdc14 sequestration complex",
    "Rum1": "Rum1 CDK inhibitor",
    "SBF": "SBF transcription factor",
    "SCF": "SCF ubiquitin ligase",
    "Securin": "Securin separase inhibitor",
    "Sic1": "Sic1 CDK inhibitor",
    "SIC1T": "Total Sic1 CDK inhibitor",
    "Skp2": "Skp2 ubiquitin-ligase adaptor",
    "SPN": "Spindle state",
    "Swe1": "Swe1 inhibitory kinase",
    "Swe1M": "Membrane-associated Swe1",
    "Swi5": "Swi5 transcription factor",
    "SWI5": "Swi5 transcription factor",
    "Timeract": "Active timer state",
    "Timerinact": "Inactive timer state",
    "TRI": "Trimer complex",
    "Trim": "Trimer complex",
    "Trimer": "Trimer complex",
    "Wee1": "Wee1 inhibitory kinase",
    "Whi5": "Whi5 Start inhibitor",
    "Whi5i": "Inactive Whi5 Start inhibitor",
    "Xic": "Xic CDK inhibitor",
    "Xicrem": "Removed Xic inhibitor pool",
    "Ydj1": "Ydj1 chaperone",
    "YOAgg": "Ydj1-oligomer aggregate complex",
}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def dump_yaml(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=110), encoding="utf-8")


def slugify(text: str) -> str:
    text = text.replace("α", " alpha ").replace("β", " beta ")
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    text = re.sub(r"_+", "_", text)
    if not text:
        return "model_state"
    if text[0].isdigit():
        text = f"observable_{text}"
    return text


def clean_label(label: str, *, symbol: str, lab_name: str, title: str) -> str:
    if lab_name == "gerard2009-integrated-mammalian-cell-cycle" and symbol in GERARD2009_SYMBOLS:
        return GERARD2009_SYMBOLS[symbol][1]
    if symbol in SYMBOL_LABELS:
        return SYMBOL_LABELS[symbol]
    if re.fullmatch(r"Cdk[1246]Y[0-9]+", symbol):
        kinase = symbol.split("Y", 1)[0].replace("Cdk", "CDK")
        state = symbol.split("Y", 1)[1]
        return f"{kinase} phosphorylation state {state}"
    if re.fullmatch(r"APCCYCdk[12]Y[0-9]+YCdk[12]Y[0-9]+YInt", symbol):
        return f"APC/C-CDK interaction state {symbol}"
    if re.fullmatch(r"APCCY[A-Za-z0-9]+", symbol):
        partner = symbol.removeprefix("APCCY")
        return f"APC/C-bound {partner} state"

    text = str(label or symbol or "").strip()
    text = text.replace("Model variable", "Model state")
    replacements = [
        (r"\bCyc\s*D\b", "Cyclin D"),
        (r"\bCyc\s*E\b", "Cyclin E"),
        (r"\bCyc\s*A\b", "Cyclin A"),
        (r"\bCyc\s*B\b", "Cyclin B"),
        (r"\bCyc\b", "Cyclin"),
        (r"\bCdk\b", "CDK"),
        (r"\bCdk([1246])\b", r"CDK\1"),
        (r"\bP\s+Rb\b", "Phosphorylated Rb"),
        (r"\bP\s+RB\b", "Phosphorylated Rb"),
        (r"\bPp\s+Rb\b", "Hyperphosphorylated Rb"),
        (r"\bE2Fp\b", "Phosphorylated E2F"),
        (r"\bP27p\b", "Phosphorylated p27"),
        (r"\bCdh1i\b", "Inactive Cdh1"),
        (r"\bCdh1a\b", "Active Cdh1"),
        (r"\bCdc20i\b", "Inactive Cdc20"),
        (r"\bCdc20a\b", "Active Cdc20"),
        (r"\bWee1p\b", "Phosphorylated Wee1"),
        (r"\b14\s+3\s+3\b", "14-3-3"),
        (r"\bM\s+RNA\b", "mRNA"),
        (r"\bDna\s*A\b", "DnaA"),
        (r"\bCtr\s*A\b", "CtrA"),
        (r"\bGcr\s*A\b", "GcrA"),
        (r"\bDiv\s*K\b", "DivK"),
        (r"\bFts\s*Z\b", "FtsZ"),
        (r"\bZring\b", "Z-ring"),
        (r"\bHiF\b", "HIF"),
        (r"\bHif\b", "HIF"),
        (r"\bDNA[Dd]amage\b", "DNA damage"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    if text in {"D", "E", "C", "M", "X", "Y", "Z", "U", "V", "R", "T", "B", "I", "K"}:
        text = f"Model state {text}"
    if text == "Ca":
        text = "Calcium" if "calcium" in f"{lab_name} {title}".lower() else "Model state Ca"
    if text == "RS":
        text = "Restriction-point signal"
    if re.fullmatch(r"[A-Za-z]{1,2}\d?", text) and slugify(text) not in COMMON_ALLOWED_SHORT:
        text = f"Model state {text}"
    return re.sub(r"\s+", " ", text).strip()


def port_name_for(label: str, *, symbol: str, lab_name: str) -> str:
    if lab_name == "gerard2009-integrated-mammalian-cell-cycle" and symbol in GERARD2009_SYMBOLS:
        return GERARD2009_SYMBOLS[symbol][0]
    name = slugify(label)
    if len(name) <= 2 and name not in COMMON_ALLOWED_SHORT:
        name = f"model_state_{name}"
    if re.fullmatch(r"[a-z]{1,2}\d?", name) and name not in COMMON_ALLOWED_SHORT:
        name = f"model_state_{name}"
    return name


def make_unique(name: str, used: set[str]) -> str:
    if name not in used:
        used.add(name)
        return name
    base = name
    index = 2
    while f"{base}_{index}" in used:
        index += 1
    unique = f"{base}_{index}"
    used.add(unique)
    return unique


def group_for(label: str, port: str, lab_name: str, title: str) -> str:
    text = f"{label} {port} {lab_name} {title}".lower()
    if any(key in text for key in ("calcium", " ip3", "atp", "gstar")):
        return "calcium"
    if any(key in text for key in ("hsp", "ydj", "proteostasis", "agg", "aggregate", "cln3", "whi5")):
        return "proteostasis"
    if any(key in text for key in ("dna damage", "checkpoint", "p53", "p21", "chk", "atm", "atr", "mad", "bub", "mcc", "securin", "hif", "oxygen", "ddr", "rad")):
        return "checkpoint"
    if any(key in text for key in ("e2f", " rb", "cyclin d", "cyclin e", "cdk2", "p27", "kip", "restriction", "g1", "s transition", "start")):
        return "g1s"
    if any(key in text for key in ("cdk1", "cdc2", "mpf", "cyclin b", "apc", "cdc20", "cdh1", "cdc25", "wee1", "plk", "mitotic", "m-phase")):
        return "mitosis"
    if any(key in text for key in ("mass", "size", "dna", "ori", "bud", "spn", "fts", "z-ring", "caulobacter", "ctra", "gcra", "dnaa", "divk", "elong")):
        return "replication"
    return "core"


def question_for(lab_name: str, title: str) -> tuple[str, str]:
    text = f"{lab_name} {title}".lower()
    if lab_name == "gerard2009-integrated-mammalian-cell-cycle":
        return (
            "Does growth-factor signaling drive the mammalian Rb/E2F and cyclin-CDK program toward cell-cycle progression?",
            "The answer is based on Rb phosphorylation, E2F activity, and sequential Cyclin D/E/A/B-CDK module responses.",
        )
    if "hypoxia" in text or "hif" in text:
        return ("Does hypoxia signaling reshape cell-cycle commitment?", "The answer is based on HIF, Myc, Rb/E2F, and cyclin commitment markers.")
    if any(key in text for key in ("damage", "checkpoint", "arrest", "ddr")):
        return ("Does checkpoint signaling suppress or redirect cell-cycle progression?", "The answer is based on DNA damage, p53/p21, checkpoint kinases, and CDK activity.")
    if "calcium" in text:
        return ("Does calcium-linked signaling couple to cell-cycle control?", "The answer is based on ATP/IP3/calcium signals and cell-cycle response variables.")
    if any(key in text for key in ("g1", "restriction", "e2f")):
        return ("Does the G1/S commitment gate open during this simulation?", "The answer is based on Rb/E2F, Cyclin D/E, CDK2, and inhibitor variables.")
    if "caulobacter" in text:
        return ("Are bacterial replication and division regulators coordinated?", "The answer is based on DnaA, CtrA, GcrA, DivK, DNA, and division markers.")
    if any(key in text for key in ("proteostasis", "critical-size", "critical size")):
        return ("Does proteostasis pressure influence Start or G1 arrest?", "The answer is based on chaperone, aggregate, Cln3, and Whi5-linked markers.")
    if any(key in text for key in ("cdc2", "cdk1", "mitotic", "m-phase", "xenopus")):
        return ("Does the mitotic switch activate and reset?", "The answer is based on CDK1/Cdc2, Cyclin B, APC/C, Cdc25, Wee1, and Plk outputs.")
    if "yeast" in text:
        return ("Does the yeast model progress through its cell-cycle phase program?", "The answer is based on cyclins, inhibitors, APC/C regulators, mass, and phase markers.")
    return ("Which model variables show measurable cell-cycle activity in this run?", "The answer is based on module-specific trajectories and ranked changes from the SBML simulation.")


VISUALISATION_CODE = r'''# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
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
'''


VIS_TEST_CODE = r'''from __future__ import annotations

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
'''


def rewrite_python_dict_keys(
    path: Path,
    input_renames: Mapping[str, str],
    output_renames: Mapping[str, str],
    label_by_symbol: Mapping[str, str],
    input_description_by_symbol: Mapping[str, str],
    output_description_by_symbol: Mapping[str, str],
) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in input_renames.items():
        text = re.sub(rf"(?m)^(\s*)'{re.escape(old)}': \(", rf"\1'{new}': (", text)
    for old, new in output_renames.items():
        text = re.sub(rf"(?m)^(\s*)'{re.escape(old)}': \(", rf"\1'{new}': (", text)
    for symbol, label in label_by_symbol.items():
        text = re.sub(rf"(?m)^(\s*)'{re.escape(symbol)}': '.*?',", rf"\1'{symbol}': {label!r},", text)
    for symbol, description in input_description_by_symbol.items():
        text = re.sub(
            rf"(?m)^(\s*'[^']+': \('{re.escape(symbol)}', [^,]+, '[^']+', )'[^']*'(\),)",
            rf"\1{description!r}\2",
            text,
        )
    for symbol, description in output_description_by_symbol.items():
        text = re.sub(
            rf"(?m)^(\s*'[^']+': \('{re.escape(symbol)}', '[^']+', )'[^']*'(\),)",
            rf"\1{description!r}\2",
            text,
        )
    path.write_text(text, encoding="utf-8")


def remediate_lab(lab: Path) -> None:
    model_yaml = lab / "models" / "core" / "model.yaml"
    lab_yaml = lab / "lab.yaml"
    if not model_yaml.exists() or not lab_yaml.exists():
        return
    model = load_yaml(model_yaml)
    lab_manifest = load_yaml(lab_yaml)
    title = str(model.get("title") or lab_manifest.get("title") or lab.name)
    alias = str((lab_manifest.get("models") or [{}])[0].get("alias") or lab.name.replace("-", "_"))

    input_renames: dict[str, str] = {}
    output_renames: dict[str, str] = {}
    label_by_symbol: dict[str, str] = {}
    input_description_by_symbol: dict[str, str] = {}
    output_description_by_symbol: dict[str, str] = {}
    used_inputs: set[str] = set()
    used_outputs: set[str] = set()

    for item in model.get("io", {}).get("inputs", []) or []:
        old_name = str(item.get("name"))
        symbol = str(item.get("maps_to") or old_name)
        label = clean_label(str(item.get("label") or old_name), symbol=symbol, lab_name=lab.name, title=title)
        base = port_name_for(label, symbol=symbol, lab_name=lab.name)
        new_name = make_unique(base, used_inputs)
        input_renames[old_name] = new_name
        item["name"] = new_name
        item["label"] = label
        detail = GERARD2009_SYMBOLS.get(symbol, ("", "", f"Controls {label}."))[2] if lab.name == "gerard2009-integrated-mammalian-cell-cycle" else f"Controls {label}."
        item["description"] = f"{detail} Maps to SBML symbol `{symbol}`."
        input_description_by_symbol[symbol] = item["description"]

    for item in model.get("io", {}).get("outputs", []) or []:
        old_name = str(item.get("name"))
        if old_name in COMPAT_OUTPUTS:
            used_outputs.add(old_name)
            continue
        symbol = str(item.get("maps_to") or old_name)
        label = clean_label(str(item.get("label") or old_name), symbol=symbol, lab_name=lab.name, title=title)
        base = port_name_for(label, symbol=symbol, lab_name=lab.name)
        new_name = make_unique(base, used_outputs)
        output_renames[old_name] = new_name
        label_by_symbol[symbol] = label
        item["name"] = new_name
        item["label"] = label
        detail = GERARD2009_SYMBOLS.get(symbol, ("", "", f"Tracks {label}."))[2] if lab.name == "gerard2009-integrated-mammalian-cell-cycle" else f"Tracks {label}."
        item["description"] = f"{detail} Maps to SBML symbol `{symbol}`."
        output_description_by_symbol[symbol] = item["description"]

    lab_io = lab_manifest.setdefault("io", {})
    for item in lab_io.get("inputs", []) or []:
        old_name = str(item.get("name"))
        if old_name in input_renames:
            item["name"] = input_renames[old_name]
            item["maps_to"] = f"{alias}.{input_renames[old_name]}"
        model_item = next((entry for entry in model.get("io", {}).get("inputs", []) or [] if entry.get("name") == item.get("name")), None)
        if model_item:
            item["label"] = model_item.get("label")
            item["description"] = f"Controls {model_item.get('label')} in the lab model via `{item['maps_to']}`."
    for item in lab_io.get("outputs", []) or []:
        old_name = str(item.get("name"))
        if old_name in output_renames:
            item["name"] = output_renames[old_name]
            item["maps_to"] = f"{alias}.{output_renames[old_name]}"
        model_item = next((entry for entry in model.get("io", {}).get("outputs", []) or [] if entry.get("name") == item.get("name")), None)
        if model_item and item.get("name") not in COMPAT_OUTPUTS:
            item["label"] = model_item.get("label")
            item["description"] = f"Tracks {model_item.get('label')} in the lab model via `{item['maps_to']}`."

    vis_dir = lab / "models" / "visualisation"
    vis_model_yaml = vis_dir / "model.yaml"
    if vis_model_yaml.exists():
        vis = load_yaml(vis_model_yaml)
        question, answer_focus = question_for(lab.name, title)
        init_kwargs = vis.setdefault("biosim", {}).setdefault("init_kwargs", {})
        init_kwargs["question"] = question
        init_kwargs["answer_focus"] = answer_focus
        sources = init_kwargs.get("sources") or []
        if sources:
            source = sources[0]
            observables = []
            for output in model.get("io", {}).get("outputs", []) or []:
                if output.get("name") in COMPAT_OUTPUTS:
                    continue
                symbol = str(output.get("maps_to") or output.get("name"))
                label = str(output.get("label") or output.get("name"))
                observables.append(
                    {
                        "id": symbol,
                        "port": str(output.get("name")),
                        "label": label,
                        "group": group_for(label, str(output.get("name")), lab.name, title),
                    }
                )
            source["observables"] = observables
        dump_yaml(vis_model_yaml, vis)
        (vis_dir / "src" / "cellcycle_visualisation.py").write_text(VISUALISATION_CODE, encoding="utf-8")
        (vis_dir / "tests" / "test_cellcycle_visualisation.py").write_text(VIS_TEST_CODE, encoding="utf-8")

    src_files = list((lab / "models" / "core" / "src").glob("*.py"))
    if src_files:
        rewrite_python_dict_keys(
            src_files[0],
            input_renames,
            output_renames,
            label_by_symbol,
            input_description_by_symbol,
            output_description_by_symbol,
        )
    dump_yaml(model_yaml, model)
    dump_yaml(lab_yaml, lab_manifest)


def is_bad_port(name: str) -> bool:
    if name in COMPAT_OUTPUTS or name in COMMON_ALLOWED_SHORT:
        return False
    return bool(re.fullmatch(r"[a-z]{1,2}\d?", name))


def audit() -> list[str]:
    errors: list[str] = []
    forbidden_gerard = {"cd", "mdi", "md", "ce", "ca", "cb", "p_rbp", "p_rbpp"}
    for lab in sorted(p for p in LABS.iterdir() if p.is_dir()):
        for manifest_path in (lab / "models" / "core" / "model.yaml", lab / "lab.yaml"):
            if not manifest_path.exists():
                continue
            manifest = load_yaml(manifest_path)
            for section in ("inputs", "outputs"):
                for item in manifest.get("io", {}).get(section, []) or []:
                    name = str(item.get("name") or "")
                    if is_bad_port(name):
                        errors.append(f"{manifest_path}: non-friendly port name `{name}`")
                    if lab.name == "gerard2009-integrated-mammalian-cell-cycle" and name in forbidden_gerard:
                        errors.append(f"{manifest_path}: forbidden Gerard2009 port `{name}`")
        vis_manifest = lab / "models" / "visualisation" / "model.yaml"
        if vis_manifest.exists():
            vis = load_yaml(vis_manifest)
            question = str(vis.get("biosim", {}).get("init_kwargs", {}).get("question") or "")
            if question.startswith("Which variables carry the main"):
                errors.append(f"{vis_manifest}: generic question remains")
    return errors


def main() -> int:
    for lab in sorted(p for p in LABS.iterdir() if p.is_dir()):
        remediate_lab(lab)
    errors = audit()
    if errors:
        print("Remediation audit failed:")
        for error in errors[:80]:
            print(f" - {error}")
        if len(errors) > 80:
            print(f" - ... {len(errors) - 80} more")
        return 1
    print("Remediated 59 cell-cycle labs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
