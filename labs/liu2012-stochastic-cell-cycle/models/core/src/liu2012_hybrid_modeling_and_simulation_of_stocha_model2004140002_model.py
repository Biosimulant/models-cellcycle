# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Liu2012-Hybrid modeling and simulation of stochastic effects on progression through the eukaryotic cell cycle..

Source: biomodels_ebi:MODEL2004140002
Original: https://www.ebi.ac.uk/biomodels/MODEL2004140002
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlLiu2012HybridModelingAndSimulationOfStochastic(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Liu2012-Hybrid modeling and simulation of stochastic effects on progression through the eukaryotic cell cycle.."""

    _SBML_ID = 'MODEL2004140002'
    _TITLE = 'Liu2012-Hybrid modeling and simulation of stochastic effects on progression through the eukaryotic cell cycle.'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'X',
        'V',
        'Y',
        'Z',
        'YT',
        'Mx',
        'My',
        'Mz',
    ]
    _SPECIES_LABELS = {
        'X': 'Model state X (X)',
        'V': 'Model state V (V)',
        'Y': 'Model state Y (Y)',
        'Z': 'Model state Z (Z)',
        'YT': 'Model state YT',
        'Mx': 'Model state Mx',
        'My': 'Model state My',
        'Mz': 'Model state Mz',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_x_x': ('X', 'native SBML value', 'Tracks Model state X (X). Maps to SBML symbol `X`.'),
        'model_state_v_v': ('V', 'native SBML value', 'Tracks Model state V (V). Maps to SBML symbol `V`.'),
        'model_state_y_y': ('Y', 'native SBML value', 'Tracks Model state Y (Y). Maps to SBML symbol `Y`.'),
        'model_state_z_z': ('Z', 'native SBML value', 'Tracks Model state Z (Z). Maps to SBML symbol `Z`.'),
        'model_state_yt': ('YT', 'native SBML value', 'Tracks Model state YT. Maps to SBML symbol `YT`.'),
        'model_state_mx': ('Mx', 'native SBML value', 'Tracks Model state Mx. Maps to SBML symbol `Mx`.'),
        'model_state_my': ('My', 'native SBML value', 'Tracks Model state My. Maps to SBML symbol `My`.'),
        'model_state_mz': ('Mz', 'native SBML value', 'Tracks Model state Mz. Maps to SBML symbol `Mz`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2004140002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Liu2012HybridModelingAndSimulationOfStochaModel2004140002Model = SbmlLiu2012HybridModelingAndSimulationOfStochastic
