# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Tyson1991 - Cell Cycle 2 var.

Source: biomodels_ebi:BIOMD0000000006
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000006
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlTyson1991CellCycle2Var(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Tyson1991 - Cell Cycle 2 var."""

    _SBML_ID = 'BIOMD0000000006'
    _TITLE = 'Tyson1991 - Cell Cycle 2 var'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'u',
        'v',
        'alpha',
        'z',
    ]
    _SPECIES_LABELS = {
        'u': 'Model state U (u)',
        'v': 'Model state V (v)',
        'alpha': 'Alpha',
        'z': 'Model state Z (z)',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_u_u': ('u', 'native SBML value', 'Tracks Model state U (u). Maps to SBML symbol `u`.'),
        'model_state_v_v': ('v', 'native SBML value', 'Tracks Model state V (v). Maps to SBML symbol `v`.'),
        'alpha': ('alpha', 'dimensionless', 'Tracks Alpha. Maps to SBML symbol `alpha`.'),
        'model_state_z_z': ('z', 'native SBML value', 'Tracks Model state Z (z). Maps to SBML symbol `z`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000006.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Tyson1991CellCycle2VarBiomd0000000006Model = SbmlTyson1991CellCycle2Var
