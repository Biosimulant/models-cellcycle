# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ferrel2011 - Cdk1 and APC regulation in cell cycle in Xenopus laevis.

Source: biomodels_ebi:BIOMD0000000935
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000935
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlFerrel2011Cdk1AndApcRegulationInCellCycleInXenopus(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ferrel2011 - Cdk1 and APC regulation in cell cycle in Xenopus laevis."""

    _SBML_ID = 'BIOMD0000000935'
    _TITLE = 'Ferrel2011 - Cdk1 and APC regulation in cell cycle in Xenopus laevis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDK1_active',
        'APC_active',
    ]
    _SPECIES_LABELS = {
        'CDK1_active': 'CDK1 Active',
        'APC_active': 'APC/C/C Active',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cdk1_active': ('CDK1_active', 'native SBML value', 'Tracks CDK1 Active. Maps to SBML symbol `CDK1_active`.'),
        'apc_c_c_active': ('APC_active', 'native SBML value', 'Tracks APC/C/C Active. Maps to SBML symbol `APC_active`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000935.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ferrel2011Cdk1AndApcRegulationInCellCycleBiomd0000000935Model = SbmlFerrel2011Cdk1AndApcRegulationInCellCycleInXenopus
