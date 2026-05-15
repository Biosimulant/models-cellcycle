# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Gardner1998 - Cell Cycle Goldbeter.

Source: biomodels_ebi:BIOMD0000000008
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000008
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlGardner1998CellCycleGoldbeter(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Gardner1998 - Cell Cycle Goldbeter."""

    _SBML_ID = 'BIOMD0000000008'
    _TITLE = 'Gardner1998 - Cell Cycle Goldbeter'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'C',
        'X',
        'M',
        'Y',
        'Z',
    ]
    _SPECIES_LABELS = {
        'C': 'Cyclin',
        'X': 'Protease',
        'M': 'Cdc2k',
        'Y': 'Cyclin Inhibitor',
        'Z': 'Complex Inhibitor Cyclin',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin': ('C', 'substance', 'Tracks Cyclin. Maps to SBML symbol `C`.'),
        'protease': ('X', 'substance', 'Tracks Protease. Maps to SBML symbol `X`.'),
        'cdc2k': ('M', 'substance', 'Tracks Cdc2k. Maps to SBML symbol `M`.'),
        'cyclin_inhibitor': ('Y', 'substance', 'Tracks Cyclin Inhibitor. Maps to SBML symbol `Y`.'),
        'complex_inhibitor_cyclin': ('Z', 'substance', 'Tracks Complex Inhibitor Cyclin. Maps to SBML symbol `Z`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000008.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Gardner1998CellCycleGoldbeterBiomd0000000008Model = SbmlGardner1998CellCycleGoldbeter
