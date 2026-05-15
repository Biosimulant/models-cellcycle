# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Model of budding yeast critical cell size dependence on growth rate with parameter set 3114.

Source: biomodels_ebi:MODEL1808310001
Original: https://www.ebi.ac.uk/biomodels/MODEL1808310001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlModelOfBuddingYeastCriticalCellSizeDependenceOn(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Model of budding yeast critical cell size dependence on growth rate with parameter set 3114."""

    _SBML_ID = 'MODEL1808310001'
    _TITLE = 'Model of budding yeast critical cell size dependence on growth rate with parameter set 3114'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Cln3F',
        'Cln3U',
        'Ydj1',
        'YP',
        'YC',
        'ProtU',
        'ProtF',
    ]
    _SPECIES_LABELS = {
        'Cln3F': 'Folded Cln3 Start cyclin',
        'Cln3U': 'Unfolded Cln3 Start cyclin',
        'Ydj1': 'Ydj1 chaperone',
        'YP': 'Model state YP',
        'YC': 'Model state YC',
        'ProtU': 'Prot Model state U',
        'ProtF': 'Prot F',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'folded_cln3_start_cyclin': ('Cln3F', 'native SBML value', 'Tracks Folded Cln3 Start cyclin. Maps to SBML symbol `Cln3F`.'),
        'unfolded_cln3_start_cyclin': ('Cln3U', 'native SBML value', 'Tracks Unfolded Cln3 Start cyclin. Maps to SBML symbol `Cln3U`.'),
        'ydj1_chaperone': ('Ydj1', 'native SBML value', 'Tracks Ydj1 chaperone. Maps to SBML symbol `Ydj1`.'),
        'model_state_yp': ('YP', 'native SBML value', 'Tracks Model state YP. Maps to SBML symbol `YP`.'),
        'model_state_yc': ('YC', 'native SBML value', 'Tracks Model state YC. Maps to SBML symbol `YC`.'),
        'prot_model_state_u': ('ProtU', 'native SBML value', 'Tracks Prot Model state U. Maps to SBML symbol `ProtU`.'),
        'prot_f': ('ProtF', 'native SBML value', 'Tracks Prot F. Maps to SBML symbol `ProtF`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1808310001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
ModelOfBuddingYeastCriticalCellSizeDependModel1808310001Model = SbmlModelOfBuddingYeastCriticalCellSizeDependenceOn
