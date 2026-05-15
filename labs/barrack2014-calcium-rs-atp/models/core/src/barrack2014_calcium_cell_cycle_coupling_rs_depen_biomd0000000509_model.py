# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Barrack2014 - Calcium/cell cycle coupling - Rs dependent ATP release.

Source: biomodels_ebi:BIOMD0000000509
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000509
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlBarrack2014CalciumCellCycleCouplingRsDependentAtp(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Barrack2014 - Calcium/cell cycle coupling - Rs dependent ATP release."""

    _SBML_ID = 'BIOMD0000000509'
    _TITLE = 'Barrack2014 - Calcium/cell cycle coupling - Rs dependent ATP release'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'd',
        'ad',
        'e',
        'r',
        'rs',
        'x',
        'ip3',
        'kg',
        'gstar',
        'ro',
        'ip3con',
        'rscon',
        'atp',
        'y',
        'delta',
        'ca',
    ]
    _SPECIES_LABELS = {
        'd': 'Model state D',
        'ad': 'Model state Ad',
        'e': 'Model state E',
        'r': 'Model state R (r)',
        'rs': 'Model state Rs',
        'x': 'Model state X (x)',
        'ip3': 'IP3',
        'kg': 'Model state Kg',
        'gstar': 'Gstar',
        'ro': 'Model state Ro',
        'ip3con': 'Ip3con',
        'rscon': 'Rscon',
        'atp': 'ATP',
        'y': 'Model state Y (y)',
        'delta': 'Delta',
        'ca': 'Calcium',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'model_state_d': ('d', 'native SBML value', 'Tracks Model state D. Maps to SBML symbol `d`.'),
        'model_state_ad': ('ad', 'native SBML value', 'Tracks Model state Ad. Maps to SBML symbol `ad`.'),
        'model_state_e': ('e', 'native SBML value', 'Tracks Model state E. Maps to SBML symbol `e`.'),
        'model_state_r_r': ('r', 'native SBML value', 'Tracks Model state R (r). Maps to SBML symbol `r`.'),
        'model_state_rs': ('rs', 'native SBML value', 'Tracks Model state Rs. Maps to SBML symbol `rs`.'),
        'model_state_x_x': ('x', 'native SBML value', 'Tracks Model state X (x). Maps to SBML symbol `x`.'),
        'ip3': ('ip3', 'native SBML value', 'Tracks IP3. Maps to SBML symbol `ip3`.'),
        'model_state_kg': ('kg', 'native SBML value', 'Tracks Model state Kg. Maps to SBML symbol `kg`.'),
        'gstar': ('gstar', 'native SBML value', 'Tracks Gstar. Maps to SBML symbol `gstar`.'),
        'model_state_ro': ('ro', 'native SBML value', 'Tracks Model state Ro. Maps to SBML symbol `ro`.'),
        'ip3con': ('ip3con', 'native SBML value', 'Tracks Ip3con. Maps to SBML symbol `ip3con`.'),
        'rscon': ('rscon', 'native SBML value', 'Tracks Rscon. Maps to SBML symbol `rscon`.'),
        'atp': ('atp', 'native SBML value', 'Tracks ATP. Maps to SBML symbol `atp`.'),
        'model_state_y_y': ('y', 'native SBML value', 'Tracks Model state Y (y). Maps to SBML symbol `y`.'),
        'delta': ('delta', 'native SBML value', 'Tracks Delta. Maps to SBML symbol `delta`.'),
        'calcium': ('ca', 'native SBML value', 'Tracks Calcium. Maps to SBML symbol `ca`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000509.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Barrack2014CalciumCellCycleCouplingRsDepenBiomd0000000509Model = SbmlBarrack2014CalciumCellCycleCouplingRsDependentAtp
