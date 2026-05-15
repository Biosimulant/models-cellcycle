# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Bai2003_G1phaseRegulation.

Source: biomodels_ebi:BIOMD0000000242
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000242
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlBai2003G1phaseregulation(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Bai2003_G1phaseRegulation."""

    _SBML_ID = 'BIOMD0000000242'
    _TITLE = 'Bai2003_G1phaseRegulation'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'D_1',
        'E_1',
        'R_1',
        'RS_1',
        'theta_1',
        'X_1',
    ]
    _SPECIES_LABELS = {
        'D_1': 'Model state D',
        'E_1': 'Model state E',
        'R_1': 'Model state R (R_1)',
        'RS_1': 'Restriction-point signal',
        'theta_1': 'Theta',
        'X_1': 'Model state X (X_1)',
    }
    _PARAMETER_INPUTS = {
        'growth_factor': ('GF_1', 6.3, 'dimensionless', 'Controls Growth Factor. Maps to SBML symbol `GF_1`.'),
    }
    _HEADLINE_OUTPUTS = {
        'model_state_d': ('D_1', 'native SBML value', 'Tracks Model state D. Maps to SBML symbol `D_1`.'),
        'model_state_e': ('E_1', 'native SBML value', 'Tracks Model state E. Maps to SBML symbol `E_1`.'),
        'model_state_r_r_1': ('R_1', 'native SBML value', 'Tracks Model state R (R_1). Maps to SBML symbol `R_1`.'),
        'restriction_point_signal': ('RS_1', 'native SBML value', 'Tracks Restriction-point signal. Maps to SBML symbol `RS_1`.'),
        'theta': ('theta_1', 'native SBML value', 'Tracks Theta. Maps to SBML symbol `theta_1`.'),
        'model_state_x_x_1': ('X_1', 'native SBML value', 'Tracks Model state X (X_1). Maps to SBML symbol `X_1`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000242.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Bai2003G1phaseregulationBiomd0000000242Model = SbmlBai2003G1phaseregulation
