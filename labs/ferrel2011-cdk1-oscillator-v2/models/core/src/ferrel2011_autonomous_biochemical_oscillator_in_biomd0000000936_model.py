# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2.

Source: biomodels_ebi:BIOMD0000000936
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000936
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlFerrel2011AutonomousBiochemicalOscillatorInCellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2."""

    _SBML_ID = 'BIOMD0000000936'
    _TITLE = 'ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDK1_active',
    ]
    _SPECIES_LABELS = {
        'CDK1_active': 'CDK1 Active',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cdk1_active': ('CDK1_active', 'native SBML value', 'Tracks CDK1 Active. Maps to SBML symbol `CDK1_active`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000936.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ferrel2011AutonomousBiochemicalOscillatorInBiomd0000000936Model = SbmlFerrel2011AutonomousBiochemicalOscillatorInCellCycle
