# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model.

Source: biomodels_ebi:BIOMD0000001079
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000001079
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlDeboeck2021ModularApproachToModelingTheCellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model."""

    _SBML_ID = 'BIOMD0000001079'
    _TITLE = 'DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CycCdk',
    ]
    _SPECIES_LABELS = {
        'CycCdk': 'Cyclin CDK',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin_cdk': ('CycCdk', 'native SBML value', 'Tracks Cyclin CDK. Maps to SBML symbol `CycCdk`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000001079.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Deboeck2021ModularApproachToModelingTheCelBiomd0000001079Model = SbmlDeboeck2021ModularApproachToModelingTheCellCycle
