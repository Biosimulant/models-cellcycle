# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Norel1990 - MPF and Cyclin Oscillations.

Source: biomodels_ebi:BIOMD0000000728
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000728
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNorel1990MpfAndCyclinOscillations(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Norel1990 - MPF and Cyclin Oscillations."""

    _SBML_ID = 'BIOMD0000000728'
    _TITLE = 'Norel1990 - MPF and Cyclin Oscillations'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'M',
        'C',
    ]
    _SPECIES_LABELS = {
        'M': 'Model state M (M)',
        'C': 'Model state C (C)',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_m_m': ('M', 'native SBML value', 'Tracks Model state M (M). Maps to SBML symbol `M`.'),
        'model_state_c_c': ('C', 'native SBML value', 'Tracks Model state C (C). Maps to SBML symbol `C`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000728.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Norel1990MpfAndCyclinOscillationsBiomd0000000728Model = SbmlNorel1990MpfAndCyclinOscillations
