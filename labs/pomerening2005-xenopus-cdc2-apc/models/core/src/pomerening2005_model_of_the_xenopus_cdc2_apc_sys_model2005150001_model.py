# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Pomerening2005- Model of the Xenopus Cdc2/APC System.

Source: biomodels_ebi:MODEL2005150001
Original: https://www.ebi.ac.uk/biomodels/MODEL2005150001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlPomerening2005ModelOfTheXenopusCdc2ApcSystem(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Pomerening2005- Model of the Xenopus Cdc2/APC System."""

    _SBML_ID = 'MODEL2005150001'
    _TITLE = 'Pomerening2005- Model of the Xenopus Cdc2/APC System'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Cyclin',
        'cdc2cyclin',
        'cdc2cyclinyp',
        'cdc2cyclinyptp',
        'cdc2cyclintp',
        'cdc2',
        'cdc2afcyclin',
        'cdc2afcyclintp',
        'cdc2af',
        'cdc25act',
        'wee1act',
        'plxact',
        'apcstar',
    ]
    _SPECIES_LABELS = {
        'Cyclin': 'Cyclin pool',
        'cdc2cyclin': 'Cdc2cyclin',
        'cdc2cyclinyp': 'Cdc2cyclinyp',
        'cdc2cyclinyptp': 'Cdc2cyclinyptp',
        'cdc2cyclintp': 'Cdc2cyclintp',
        'cdc2': 'Cdc2',
        'cdc2afcyclin': 'Cdc2afcyclin',
        'cdc2afcyclintp': 'Cdc2afcyclintp',
        'cdc2af': 'Cdc2af',
        'cdc25act': 'Cdc25act',
        'wee1act': 'Wee1act',
        'plxact': 'Plxact',
        'apcstar': 'Apcstar',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin_pool': ('Cyclin', 'native SBML value', 'Tracks Cyclin pool. Maps to SBML symbol `Cyclin`.'),
        'cdc2cyclin': ('cdc2cyclin', 'native SBML value', 'Tracks Cdc2cyclin. Maps to SBML symbol `cdc2cyclin`.'),
        'cdc2cyclinyp': ('cdc2cyclinyp', 'native SBML value', 'Tracks Cdc2cyclinyp. Maps to SBML symbol `cdc2cyclinyp`.'),
        'cdc2cyclinyptp': ('cdc2cyclinyptp', 'native SBML value', 'Tracks Cdc2cyclinyptp. Maps to SBML symbol `cdc2cyclinyptp`.'),
        'cdc2cyclintp': ('cdc2cyclintp', 'native SBML value', 'Tracks Cdc2cyclintp. Maps to SBML symbol `cdc2cyclintp`.'),
        'cdc2': ('cdc2', 'native SBML value', 'Tracks Cdc2. Maps to SBML symbol `cdc2`.'),
        'cdc2afcyclin': ('cdc2afcyclin', 'native SBML value', 'Tracks Cdc2afcyclin. Maps to SBML symbol `cdc2afcyclin`.'),
        'cdc2afcyclintp': ('cdc2afcyclintp', 'native SBML value', 'Tracks Cdc2afcyclintp. Maps to SBML symbol `cdc2afcyclintp`.'),
        'cdc2af': ('cdc2af', 'native SBML value', 'Tracks Cdc2af. Maps to SBML symbol `cdc2af`.'),
        'cdc25act': ('cdc25act', 'native SBML value', 'Tracks Cdc25act. Maps to SBML symbol `cdc25act`.'),
        'wee1act': ('wee1act', 'native SBML value', 'Tracks Wee1act. Maps to SBML symbol `wee1act`.'),
        'plxact': ('plxact', 'native SBML value', 'Tracks Plxact. Maps to SBML symbol `plxact`.'),
        'apcstar': ('apcstar', 'native SBML value', 'Tracks Apcstar. Maps to SBML symbol `apcstar`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2005150001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Pomerening2005ModelOfTheXenopusCdc2ApcSysModel2005150001Model = SbmlPomerening2005ModelOfTheXenopusCdc2ApcSystem
