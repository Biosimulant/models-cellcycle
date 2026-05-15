# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Bedessem2014 - HiF-1 a -mediated response to hypoxia on the G1/S transition.

Source: biomodels_ebi:MODEL1812040001
Original: https://www.ebi.ac.uk/biomodels/MODEL1812040001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlBedessem2014Hif1AMediatedResponseToHypoxiaOnTheG1(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Bedessem2014 - HiF-1 a -mediated response to hypoxia on the G1/S transition."""

    _SBML_ID = 'MODEL1812040001'
    _TITLE = 'Bedessem2014 - HiF-1 a -mediated response to hypoxia on the G1/S transition'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'm',
        'cycD',
        'Rb',
        'cycE',
        'SCF',
        'E2F',
        'E2F_A',
        'E2F_Rb',
    ]
    _SPECIES_LABELS = {
        'm': 'Model state M (m)',
        'cycD': 'Cyclin D',
        'Rb': 'Rb tumor suppressor',
        'cycE': 'Cyclin E',
        'SCF': 'SCF ubiquitin ligase',
        'E2F': 'E2F transcription factor',
        'E2F_A': 'E2F A',
        'E2F_Rb': 'E2F Rb',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_m_m': ('m', 'native SBML value', 'Tracks Model state M (m). Maps to SBML symbol `m`.'),
        'cyclin_d': ('cycD', 'native SBML value', 'Tracks Cyclin D. Maps to SBML symbol `cycD`.'),
        'rb_tumor_suppressor': ('Rb', 'native SBML value', 'Tracks Rb tumor suppressor. Maps to SBML symbol `Rb`.'),
        'cyclin_e': ('cycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `cycE`.'),
        'scf_ubiquitin_ligase': ('SCF', 'native SBML value', 'Tracks SCF ubiquitin ligase. Maps to SBML symbol `SCF`.'),
        'e2f_transcription_factor': ('E2F', 'native SBML value', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'e2f_a': ('E2F_A', 'dimensionless', 'Tracks E2F A. Maps to SBML symbol `E2F_A`.'),
        'e2f_rb': ('E2F_Rb', 'dimensionless', 'Tracks E2F Rb. Maps to SBML symbol `E2F_Rb`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1812040001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Bedessem2014Hif1AMediatedResponseToHypoxiModel1812040001Model = SbmlBedessem2014Hif1AMediatedResponseToHypoxiaOnTheG1
