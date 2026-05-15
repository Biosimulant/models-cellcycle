# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Tyson1991 - Cell Cycle 6 var.

Source: biomodels_ebi:BIOMD0000000005
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000005
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlTyson1991CellCycle6Var(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Tyson1991 - Cell Cycle 6 var."""

    _SBML_ID = 'BIOMD0000000005'
    _TITLE = 'Tyson1991 - Cell Cycle 6 var'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'C2',
        'CP',
        'M',
        'pM',
        'Y',
        'YP',
    ]
    _SPECIES_LABELS = {
        'C2': 'Cdc2k',
        'CP': 'Cdc2k P',
        'M': 'Phosphorylated Cyclin Cdc2',
        'pM': 'Phosphorylated Cyclin Cdc2 P',
        'Y': 'Cyclin',
        'YP': 'Phosphorylated Cyclin',
    }
    _PARAMETER_INPUTS = {
        'total_cyclin': ('YT', 0.25, 'native SBML value', 'Controls Total Cyclin. Maps to SBML symbol `YT`.'),
        'total_cdc2': ('CT', 1.0, 'native SBML value', 'Controls Total Cdc2. Maps to SBML symbol `CT`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cdc2k': ('C2', 'native SBML value', 'Tracks Cdc2k. Maps to SBML symbol `C2`.'),
        'cdc2k_p': ('CP', 'native SBML value', 'Tracks Cdc2k P. Maps to SBML symbol `CP`.'),
        'phosphorylated_cyclin_cdc2': ('M', 'native SBML value', 'Tracks Phosphorylated Cyclin Cdc2. Maps to SBML symbol `M`.'),
        'phosphorylated_cyclin_cdc2_p': ('pM', 'native SBML value', 'Tracks Phosphorylated Cyclin Cdc2 P. Maps to SBML symbol `pM`.'),
        'cyclin': ('Y', 'native SBML value', 'Tracks Cyclin. Maps to SBML symbol `Y`.'),
        'phosphorylated_cyclin': ('YP', 'native SBML value', 'Tracks Phosphorylated Cyclin. Maps to SBML symbol `YP`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000005.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Tyson1991CellCycle6VarBiomd0000000005Model = SbmlTyson1991CellCycle6Var
