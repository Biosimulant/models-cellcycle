# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Dong2018 - E2F dynamics in G1 phase.

Source: biomodels_ebi:MODEL1811050001
Original: https://www.ebi.ac.uk/biomodels/MODEL1811050001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlDong2018E2fDynamicsInG1Phase(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Dong2018 - E2F dynamics in G1 phase."""

    _SBML_ID = 'MODEL1811050001'
    _TITLE = 'Dong2018 - E2F dynamics in G1 phase'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'MYC',
        'S',
        'E2Fp',
        'E2Fm',
        'RB',
        'RE',
        'R',
        'CD',
        'CE',
        'RP',
    ]
    _SPECIES_LABELS = {
        'MYC': 'Myc',
        'S': 'Model state S',
        'E2Fp': 'Phosphorylated E2F',
        'E2Fm': 'E2F mRNA',
        'RB': 'Rb',
        'RE': 'Model state RE',
        'R': 'Model state R (R)',
        'CD': 'Model state CD',
        'CE': 'Model state CE',
        'RP': 'Model state RP',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'myc': ('MYC', 'native SBML value', 'Tracks Myc. Maps to SBML symbol `MYC`.'),
        'model_state_s': ('S', 'native SBML value', 'Tracks Model state S. Maps to SBML symbol `S`.'),
        'phosphorylated_e2f': ('E2Fp', 'native SBML value', 'Tracks Phosphorylated E2F. Maps to SBML symbol `E2Fp`.'),
        'e2f_m_rna': ('E2Fm', 'native SBML value', 'Tracks E2F mRNA. Maps to SBML symbol `E2Fm`.'),
        'rb': ('RB', 'native SBML value', 'Tracks Rb. Maps to SBML symbol `RB`.'),
        'model_state_re': ('RE', 'native SBML value', 'Tracks Model state RE. Maps to SBML symbol `RE`.'),
        'model_state_r_r': ('R', 'native SBML value', 'Tracks Model state R (R). Maps to SBML symbol `R`.'),
        'model_state_cd': ('CD', 'native SBML value', 'Tracks Model state CD. Maps to SBML symbol `CD`.'),
        'model_state_ce': ('CE', 'native SBML value', 'Tracks Model state CE. Maps to SBML symbol `CE`.'),
        'model_state_rp': ('RP', 'native SBML value', 'Tracks Model state RP. Maps to SBML symbol `RP`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1811050001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Dong2018E2fDynamicsInG1PhaseModel1811050001Model = SbmlDong2018E2fDynamicsInG1Phase
