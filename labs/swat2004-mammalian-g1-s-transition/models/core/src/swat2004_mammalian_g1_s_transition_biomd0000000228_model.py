# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Swat2004_Mammalian_G1_S_Transition.

Source: biomodels_ebi:BIOMD0000000228
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000228
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlSwat2004MammalianG1STransition(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Swat2004_Mammalian_G1_S_Transition."""

    _SBML_ID = 'BIOMD0000000228'
    _TITLE = 'Swat2004_Mammalian_G1_S_Transition'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'pRB',
        'pRBp',
        'E2F1',
        'CycDi',
        'CycDa',
        'AP1',
        'pRBpp',
        'CycEi',
        'CycEa',
    ]
    _SPECIES_LABELS = {
        'pRB': 'Phosphorylated Rb',
        'pRBp': 'P RBp',
        'E2F1': 'E2F1 transcription factor',
        'CycDi': 'Cyclin D CDK4,6(i)',
        'CycDa': 'Cyclin D CDK4,6(a)',
        'AP1': 'AP1 transcription factor',
        'pRBpp': 'P RBpp',
        'CycEi': 'Cyclin E CDK2(i)',
        'CycEa': 'Cyclin Ea CDK2(a)',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'phosphorylated_rb': ('pRB', 'native SBML value', 'Tracks Phosphorylated Rb. Maps to SBML symbol `pRB`.'),
        'p_rbp': ('pRBp', 'native SBML value', 'Tracks P RBp. Maps to SBML symbol `pRBp`.'),
        'e2f1_transcription_factor': ('E2F1', 'native SBML value', 'Tracks E2F1 transcription factor. Maps to SBML symbol `E2F1`.'),
        'cyclin_d_cdk4_6_i': ('CycDi', 'native SBML value', 'Tracks Cyclin D CDK4,6(i). Maps to SBML symbol `CycDi`.'),
        'cyclin_d_cdk4_6_a': ('CycDa', 'native SBML value', 'Tracks Cyclin D CDK4,6(a). Maps to SBML symbol `CycDa`.'),
        'ap1_transcription_factor': ('AP1', 'native SBML value', 'Tracks AP1 transcription factor. Maps to SBML symbol `AP1`.'),
        'p_rbpp': ('pRBpp', 'native SBML value', 'Tracks P RBpp. Maps to SBML symbol `pRBpp`.'),
        'cyclin_e_cdk2_i': ('CycEi', 'native SBML value', 'Tracks Cyclin E CDK2(i). Maps to SBML symbol `CycEi`.'),
        'cyclin_ea_cdk2_a': ('CycEa', 'native SBML value', 'Tracks Cyclin Ea CDK2(a). Maps to SBML symbol `CycEa`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000228.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Swat2004MammalianG1STransitionBiomd0000000228Model = SbmlSwat2004MammalianG1STransition
