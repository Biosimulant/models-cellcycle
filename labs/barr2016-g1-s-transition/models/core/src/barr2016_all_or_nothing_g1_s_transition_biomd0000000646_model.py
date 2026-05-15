# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Barr2016 - All-or-nothing G1/S transition.

Source: biomodels_ebi:BIOMD0000000646
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000646
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlBarr2016AllOrNothingG1STransition(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Barr2016 - All-or-nothing G1/S transition."""

    _SBML_ID = 'BIOMD0000000646'
    _TITLE = 'Barr2016 - All-or-nothing G1/S transition'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CycE',
        'CycA',
        'CycEp27',
        'CycAp27',
        'Skp2',
        'Cdh1p',
        'Emi1',
        'p27',
        'Cdh1',
        'Emi1Cdh1',
        'Emi1Cdh1p',
    ]
    _SPECIES_LABELS = {
        'CycE': 'Cyclin E',
        'CycA': 'Cyclin A',
        'CycEp27': 'Cyclin Ep27',
        'CycAp27': 'Cyclin Ap27',
        'Skp2': 'Skp2 ubiquitin-ligase adaptor',
        'Cdh1p': 'Phosphorylated Cdh1',
        'Emi1': 'Emi1 APC/C inhibitor',
        'p27': 'p27 CDK inhibitor',
        'Cdh1': 'Cdh1 APC/C activator',
        'Emi1Cdh1': 'Emi1-Cdh1 complex',
        'Emi1Cdh1p': 'Emi1-phosphorylated Cdh1 complex',
    }
    _PARAMETER_INPUTS = {
        'cyclin_et': ('CycET', 0.0, 'native SBML value', 'Controls Cyclin ET. Maps to SBML symbol `CycET`.'),
        'cyclin_at': ('CycAT', 0.0, 'native SBML value', 'Controls Cyclin AT. Maps to SBML symbol `CycAT`.'),
        'p27t': ('p27T', 0.0, 'native SBML value', 'Controls P27T. Maps to SBML symbol `p27T`.'),
        'emi_model_state_c': ('EmiC', 0.0, 'native SBML value', 'Controls Emi Model state C. Maps to SBML symbol `EmiC`.'),
        'emi1t': ('Emi1T', 0.0, 'native SBML value', 'Controls Emi1T. Maps to SBML symbol `Emi1T`.'),
        'cdh1dp': ('Cdh1dp', 1.0, 'native SBML value', 'Controls Cdh1dp. Maps to SBML symbol `Cdh1dp`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cyclin_e': ('CycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `CycE`.'),
        'cyclin_a': ('CycA', 'native SBML value', 'Tracks Cyclin A. Maps to SBML symbol `CycA`.'),
        'cyclin_ep27': ('CycEp27', 'native SBML value', 'Tracks Cyclin Ep27. Maps to SBML symbol `CycEp27`.'),
        'cyclin_ap27': ('CycAp27', 'native SBML value', 'Tracks Cyclin Ap27. Maps to SBML symbol `CycAp27`.'),
        'skp2_ubiquitin_ligase_adaptor': ('Skp2', 'native SBML value', 'Tracks Skp2 ubiquitin-ligase adaptor. Maps to SBML symbol `Skp2`.'),
        'phosphorylated_cdh1': ('Cdh1p', 'native SBML value', 'Tracks Phosphorylated Cdh1. Maps to SBML symbol `Cdh1p`.'),
        'emi1_apc_c_inhibitor': ('Emi1', 'native SBML value', 'Tracks Emi1 APC/C inhibitor. Maps to SBML symbol `Emi1`.'),
        'p27_cdk_inhibitor': ('p27', 'native SBML value', 'Tracks p27 CDK inhibitor. Maps to SBML symbol `p27`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'emi1_cdh1_complex': ('Emi1Cdh1', 'native SBML value', 'Tracks Emi1-Cdh1 complex. Maps to SBML symbol `Emi1Cdh1`.'),
        'emi1_phosphorylated_cdh1_complex': ('Emi1Cdh1p', 'native SBML value', 'Tracks Emi1-phosphorylated Cdh1 complex. Maps to SBML symbol `Emi1Cdh1p`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000646.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Barr2016AllOrNothingG1STransitionBiomd0000000646Model = SbmlBarr2016AllOrNothingG1STransition
