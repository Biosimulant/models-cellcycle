# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Novak1993 - Cell cycle M-phase control.

Source: biomodels_ebi:BIOMD0000000107
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000107
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNovak1993CellCycleMPhaseControl(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Novak1993 - Cell cycle M-phase control."""

    _SBML_ID = 'BIOMD0000000107'
    _TITLE = 'Novak1993 - Cell cycle M-phase control'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'cyclin',
        'dimer',
        'dimer_p',
        'p_dimer',
        'p_dimer_p',
        'cdc25_p',
        'wee1_p',
        'IE_p',
        'UbE_star',
    ]
    _SPECIES_LABELS = {
        'cyclin': 'Cyclin',
        'dimer': 'Cyclin Cdc2 Dimer',
        'dimer_p': 'Phosphorylated Dimer',
        'p_dimer': 'Tyr15 Phosphorylated Dimer',
        'p_dimer_p': 'Phosphorylated P Dimer',
        'cdc25_p': 'Phosphorylated Cdc25',
        'wee1_p': 'Phosphorylated Wee1',
        'IE_p': 'Phosphorylated IE',
        'UbE_star': 'Ubiquitin Conjugating Enzyme',
    }
    _PARAMETER_INPUTS = {
        'cdc2': ('cdc2', 100.0, 'native SBML value', 'Controls Cdc2. Maps to SBML symbol `cdc2`.'),
        'cdc25': ('cdc25', 1.0, 'native SBML value', 'Controls Cdc25. Maps to SBML symbol `cdc25`.'),
        'wee1': ('wee1', 1.0, 'native SBML value', 'Controls Wee1. Maps to SBML symbol `wee1`.'),
        'intermediary_enzyme': ('IE', 1.0, 'native SBML value', 'Controls Intermediary Enzyme. Maps to SBML symbol `IE`.'),
        'ubiquitin_conjugating_enzyme': ('UbE', 1.0, 'native SBML value', 'Controls Ubiquitin Conjugating Enzyme. Maps to SBML symbol `UbE`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cyclin': ('cyclin', 'native SBML value', 'Tracks Cyclin. Maps to SBML symbol `cyclin`.'),
        'cyclin_cdc2_dimer': ('dimer', 'native SBML value', 'Tracks Cyclin Cdc2 Dimer. Maps to SBML symbol `dimer`.'),
        'phosphorylated_dimer': ('dimer_p', 'native SBML value', 'Tracks Phosphorylated Dimer. Maps to SBML symbol `dimer_p`.'),
        'tyr15_phosphorylated_dimer': ('p_dimer', 'native SBML value', 'Tracks Tyr15 Phosphorylated Dimer. Maps to SBML symbol `p_dimer`.'),
        'phosphorylated_p_dimer': ('p_dimer_p', 'native SBML value', 'Tracks Phosphorylated P Dimer. Maps to SBML symbol `p_dimer_p`.'),
        'phosphorylated_cdc25': ('cdc25_p', 'native SBML value', 'Tracks Phosphorylated Cdc25. Maps to SBML symbol `cdc25_p`.'),
        'phosphorylated_wee1': ('wee1_p', 'native SBML value', 'Tracks Phosphorylated Wee1. Maps to SBML symbol `wee1_p`.'),
        'phosphorylated_ie': ('IE_p', 'native SBML value', 'Tracks Phosphorylated IE. Maps to SBML symbol `IE_p`.'),
        'ubiquitin_conjugating_enzyme': ('UbE_star', 'native SBML value', 'Tracks Ubiquitin Conjugating Enzyme. Maps to SBML symbol `UbE_star`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000107.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Novak1993CellCycleMPhaseControlBiomd0000000107Model = SbmlNovak1993CellCycleMPhaseControl
