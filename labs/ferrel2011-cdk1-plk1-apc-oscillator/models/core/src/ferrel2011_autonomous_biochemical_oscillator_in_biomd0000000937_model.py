# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ferrel2011 - Autonomous biochemical oscillator in regulation of CDK1, Plk1, and APC in Xenopus Laevis cell cycle.

Source: biomodels_ebi:BIOMD0000000937
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000937
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlFerrel2011AutonomousBiochemicalOscillatorInRegulation(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ferrel2011 - Autonomous biochemical oscillator in regulation of CDK1, Plk1, and APC in Xenopus Laevis cell cycle."""

    _SBML_ID = 'BIOMD0000000937'
    _TITLE = 'Ferrel2011 - Autonomous biochemical oscillator in regulation of CDK1, Plk1, and APC in Xenopus Laevis cell cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDK1_active',
        'APC_active',
        'Plk1_active',
    ]
    _SPECIES_LABELS = {
        'CDK1_active': 'CDK1 Active',
        'APC_active': 'APC/C/C Active',
        'Plk1_active': 'Plk1 Active',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cdk1_active': ('CDK1_active', 'native SBML value', 'Tracks CDK1 Active. Maps to SBML symbol `CDK1_active`.'),
        'apc_c_c_active': ('APC_active', 'native SBML value', 'Tracks APC/C/C Active. Maps to SBML symbol `APC_active`.'),
        'plk1_active': ('Plk1_active', 'native SBML value', 'Tracks Plk1 Active. Maps to SBML symbol `Plk1_active`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000937.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ferrel2011AutonomousBiochemicalOscillatorInBiomd0000000937Model = SbmlFerrel2011AutonomousBiochemicalOscillatorInRegulation
