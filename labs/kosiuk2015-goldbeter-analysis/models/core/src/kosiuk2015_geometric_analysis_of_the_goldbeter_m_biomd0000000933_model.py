# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Kosiuk2015-Geometric analysis of the Goldbeter minimal model for the embryonic cell cycle.

Source: biomodels_ebi:BIOMD0000000933
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000933
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlKosiuk2015GeometricAnalysisOfTheGoldbeterMinimal(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Kosiuk2015-Geometric analysis of the Goldbeter minimal model for the embryonic cell cycle."""

    _SBML_ID = 'BIOMD0000000933'
    _TITLE = 'Kosiuk2015-Geometric analysis of the Goldbeter minimal model for the embryonic cell cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'C',
        'M',
        'X',
    ]
    _SPECIES_LABELS = {
        'C': 'Model state C (C)',
        'M': 'Model state M (M)',
        'X': 'Model state X (X)',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_c_c': ('C', 'native SBML value', 'Tracks Model state C (C). Maps to SBML symbol `C`.'),
        'model_state_m_m': ('M', 'native SBML value', 'Tracks Model state M (M). Maps to SBML symbol `M`.'),
        'model_state_x_x': ('X', 'native SBML value', 'Tracks Model state X (X). Maps to SBML symbol `X`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000933.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Kosiuk2015GeometricAnalysisOfTheGoldbeterMBiomd0000000933Model = SbmlKosiuk2015GeometricAnalysisOfTheGoldbeterMinimal
