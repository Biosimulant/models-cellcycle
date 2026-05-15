# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Chiorino2002 - G1/S transition model.

Source: biomodels_ebi:MODEL2003180003
Original: https://www.ebi.ac.uk/biomodels/MODEL2003180003
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlChiorino2002G1STransitionModel(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Chiorino2002 - G1/S transition model."""

    _SBML_ID = 'MODEL2003180003'
    _TITLE = 'Chiorino2002 - G1/S transition model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'pRb',
        'pRbE2F',
        'Cdk2',
        'cycE',
        'cycE_Cdk2',
        'cycE_Cdk2_pRbE2F',
        'pRb_P',
        'cycE_P',
        'cycE_Cdk2_p27',
        'p27',
        'cycE_Cdk2_cycE_Cdk2_p27',
        'p27_P',
        'mRNA_cyclinE',
        'E2F',
        'mRNA_E2F',
    ]
    _SPECIES_LABELS = {
        'pRb': 'Phosphorylated Rb',
        'pRbE2F': 'Phosphorylated Rb E2F',
        'Cdk2': 'CDK2',
        'cycE': 'Cyclin E',
        'cycE_Cdk2': 'Cyclin E CDK2',
        'cycE_Cdk2_pRbE2F': 'Cyclin E CDK2 Phosphorylated Rb E2F',
        'pRb_P': 'Phosphorylated Phosphorylated Rb',
        'cycE_P': 'Phosphorylated Cyclin E',
        'cycE_Cdk2_p27': 'Cyclin E CDK2 P27',
        'p27': 'p27 CDK inhibitor',
        'cycE_Cdk2_cycE_Cdk2_p27': 'Cyclin E CDK2 Cyclin E CDK2 P27',
        'p27_P': 'Phosphorylated P27',
        'mRNA_cyclinE': 'Model state mRNA Cyclin E',
        'E2F': 'E2F transcription factor',
        'mRNA_E2F': 'Model state mRNA E2F',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'phosphorylated_rb': ('pRb', 'native SBML value', 'Tracks Phosphorylated Rb. Maps to SBML symbol `pRb`.'),
        'phosphorylated_rb_e2f': ('pRbE2F', 'native SBML value', 'Tracks Phosphorylated Rb E2F. Maps to SBML symbol `pRbE2F`.'),
        'cdk2': ('Cdk2', 'native SBML value', 'Tracks CDK2. Maps to SBML symbol `Cdk2`.'),
        'cyclin_e': ('cycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `cycE`.'),
        'cyclin_e_cdk2': ('cycE_Cdk2', 'native SBML value', 'Tracks Cyclin E CDK2. Maps to SBML symbol `cycE_Cdk2`.'),
        'cyclin_e_cdk2_phosphorylated_rb_e2f': ('cycE_Cdk2_pRbE2F', 'native SBML value', 'Tracks Cyclin E CDK2 Phosphorylated Rb E2F. Maps to SBML symbol `cycE_Cdk2_pRbE2F`.'),
        'phosphorylated_phosphorylated_rb': ('pRb_P', 'native SBML value', 'Tracks Phosphorylated Phosphorylated Rb. Maps to SBML symbol `pRb_P`.'),
        'phosphorylated_cyclin_e': ('cycE_P', 'native SBML value', 'Tracks Phosphorylated Cyclin E. Maps to SBML symbol `cycE_P`.'),
        'cyclin_e_cdk2_p27': ('cycE_Cdk2_p27', 'native SBML value', 'Tracks Cyclin E CDK2 P27. Maps to SBML symbol `cycE_Cdk2_p27`.'),
        'p27_cdk_inhibitor': ('p27', 'native SBML value', 'Tracks p27 CDK inhibitor. Maps to SBML symbol `p27`.'),
        'cyclin_e_cdk2_cyclin_e_cdk2_p27': ('cycE_Cdk2_cycE_Cdk2_p27', 'native SBML value', 'Tracks Cyclin E CDK2 Cyclin E CDK2 P27. Maps to SBML symbol `cycE_Cdk2_cycE_Cdk2_p27`.'),
        'phosphorylated_p27': ('p27_P', 'native SBML value', 'Tracks Phosphorylated P27. Maps to SBML symbol `p27_P`.'),
        'model_state_m_rna_cyclin_e': ('mRNA_cyclinE', 'native SBML value', 'Tracks Model state mRNA Cyclin E. Maps to SBML symbol `mRNA_cyclinE`.'),
        'e2f_transcription_factor': ('E2F', 'native SBML value', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'model_state_m_rna_e2f': ('mRNA_E2F', 'native SBML value', 'Tracks Model state mRNA E2F. Maps to SBML symbol `mRNA_E2F`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2003180003.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Chiorino2002G1STransitionModelModel2003180003Model = SbmlChiorino2002G1STransitionModel
