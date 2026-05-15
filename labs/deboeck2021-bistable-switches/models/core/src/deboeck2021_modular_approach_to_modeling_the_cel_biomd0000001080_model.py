# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for DeBoeck2021 - Modular approach to modeling the cell cycle, 5 ODE model with 3 bistable switches.

Source: biomodels_ebi:BIOMD0000001080
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000001080
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlDeboeck2021ModularApproachToModelingTheCellCycle5(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: DeBoeck2021 - Modular approach to modeling the cell cycle, 5 ODE model with 3 bistable switches."""

    _SBML_ID = 'BIOMD0000001080'
    _TITLE = 'DeBoeck2021 - Modular approach to modeling the cell cycle, 5 ODE model with 3 bistable switches'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CycD',
        'CycB',
    ]
    _SPECIES_LABELS = {
        'CycD': 'Cyclin D',
        'CycB': 'Cyclin B',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin_d': ('CycD', 'native SBML value', 'Tracks Cyclin D. Maps to SBML symbol `CycD`.'),
        'cyclin_b': ('CycB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `CycB`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000001080.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Deboeck2021ModularApproachToModelingTheCelBiomd0000001080Model = SbmlDeboeck2021ModularApproachToModelingTheCellCycle5
