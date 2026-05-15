# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Hatzimanikatis1999-Regulation of the G1-S transition of the mammalian cell cycle..

Source: biomodels_ebi:MODEL2005070001
Original: https://www.ebi.ac.uk/biomodels/MODEL2005070001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlHatzimanikatis1999RegulationOfTheG1STransitionOfThe(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Hatzimanikatis1999-Regulation of the G1-S transition of the mammalian cell cycle.."""

    _SBML_ID = 'MODEL2005070001'
    _TITLE = 'Hatzimanikatis1999-Regulation of the G1-S transition of the mammalian cell cycle.'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'C',
        'K',
        'Rp',
    ]
    _SPECIES_LABELS = {
        'C': 'Model state C (C)',
        'K': 'Model state K',
        'Rp': 'Model state Rp',
    }
    _PARAMETER_INPUTS = {
        'model_state_e': ('E', 1.0, 'native SBML value', 'Controls Model state E. Maps to SBML symbol `E`.'),
        'model_state_kp': ('Kp', 1.0, 'native SBML value', 'Controls Model state Kp. Maps to SBML symbol `Kp`.'),
        'model_state_re': ('RE', 1.0, 'native SBML value', 'Controls Model state RE. Maps to SBML symbol `RE`.'),
    }
    _HEADLINE_OUTPUTS = {
        'model_state_c_c': ('C', 'native SBML value', 'Tracks Model state C (C). Maps to SBML symbol `C`.'),
        'model_state_k': ('K', 'native SBML value', 'Tracks Model state K. Maps to SBML symbol `K`.'),
        'model_state_rp': ('Rp', 'native SBML value', 'Tracks Model state Rp. Maps to SBML symbol `Rp`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2005070001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Hatzimanikatis1999RegulationOfTheG1STransiModel2005070001Model = SbmlHatzimanikatis1999RegulationOfTheG1STransitionOfThe
