# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Morris2002_CellCycle_CDK2Cyclin.

Source: biomodels_ebi:BIOMD0000000150
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000150
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlMorris2002CellcycleCdk2cyclin(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Morris2002_CellCycle_CDK2Cyclin."""

    _SBML_ID = 'BIOMD0000000150'
    _TITLE = 'Morris2002_CellCycle_CDK2Cyclin'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDK2cycA',
        'CyclinA',
        'Cdk2',
        'CDK2cycA_star_',
    ]
    _SPECIES_LABELS = {
        'CDK2cycA': 'CDK2cyc A',
        'CyclinA': 'Cyclin A',
        'Cdk2': 'CDK2',
        'CDK2cycA_star_': 'CDK2cyc Active Star',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cdk2cyc_a': ('CDK2cycA', 'native SBML value', 'Tracks CDK2cyc A. Maps to SBML symbol `CDK2cycA`.'),
        'cyclin_a': ('CyclinA', 'native SBML value', 'Tracks Cyclin A. Maps to SBML symbol `CyclinA`.'),
        'cdk2': ('Cdk2', 'native SBML value', 'Tracks CDK2. Maps to SBML symbol `Cdk2`.'),
        'cdk2cyc_active_star': ('CDK2cycA_star_', 'native SBML value', 'Tracks CDK2cyc Active Star. Maps to SBML symbol `CDK2cycA_star_`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000150.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Morris2002CellcycleCdk2cyclinBiomd0000000150Model = SbmlMorris2002CellcycleCdk2cyclin
