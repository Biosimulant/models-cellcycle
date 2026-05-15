# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Deineko2003_CellCycle.

Source: biomodels_ebi:BIOMD0000000208
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000208
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlDeineko2003Cellcycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Deineko2003_CellCycle."""

    _SBML_ID = 'BIOMD0000000208'
    _TITLE = 'Deineko2003_CellCycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'y1',
        'y2',
        'y3',
        'y4',
        'y5',
        'y6',
    ]
    _SPECIES_LABELS = {
        'y1': 'E2F',
        'y2': 'Phosphorylated Rb',
        'y3': 'Phosphorylated Phosphorylated Rb',
        'y4': 'Inactive Cyclin E CDK2',
        'y5': 'Active Cyclin E CDK2',
        'y6': 'AP 1',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'e2f': ('y1', 'native SBML value', 'Tracks E2F. Maps to SBML symbol `y1`.'),
        'phosphorylated_rb': ('y2', 'native SBML value', 'Tracks Phosphorylated Rb. Maps to SBML symbol `y2`.'),
        'phosphorylated_phosphorylated_rb': ('y3', 'native SBML value', 'Tracks Phosphorylated Phosphorylated Rb. Maps to SBML symbol `y3`.'),
        'inactive_cyclin_e_cdk2': ('y4', 'native SBML value', 'Tracks Inactive Cyclin E CDK2. Maps to SBML symbol `y4`.'),
        'active_cyclin_e_cdk2': ('y5', 'native SBML value', 'Tracks Active Cyclin E CDK2. Maps to SBML symbol `y5`.'),
        'ap_1': ('y6', 'native SBML value', 'Tracks AP 1. Maps to SBML symbol `y6`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000208.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Deineko2003CellcycleBiomd0000000208Model = SbmlDeineko2003Cellcycle
