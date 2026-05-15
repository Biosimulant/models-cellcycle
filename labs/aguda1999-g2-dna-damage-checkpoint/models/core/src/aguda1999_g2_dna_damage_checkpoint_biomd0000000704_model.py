# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Aguda1999 - G2 DNA damage checkpoint.

Source: biomodels_ebi:BIOMD0000000704
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000704
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlAguda1999G2DnaDamageCheckpoint(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Aguda1999 - G2 DNA damage checkpoint."""

    _SBML_ID = 'BIOMD0000000704'
    _TITLE = 'Aguda1999 - G2 DNA damage checkpoint'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Cdc25_active',
        'Cdc25Ps216_active',
        'Cdc25_inactive',
        'Cdc25Ps216_inactive',
        'Chk1P',
        'protein_14_3_3',
        'Cdc25Ps216_14_3_3_inactive',
        'p53',
        'p21',
        'MPF',
        'p21_MPF',
        'preMPF',
        'Wee1',
        'Chk1',
        'Rad3_ATM',
        'Wee1_phosphorylated',
    ]
    _SPECIES_LABELS = {
        'Cdc25_active': 'Cdc25 Active',
        'Cdc25Ps216_active': 'Cdc25Ps216 Active',
        'Cdc25_inactive': 'Cdc25 Inactive',
        'Cdc25Ps216_inactive': 'Cdc25Ps216 Inactive',
        'Chk1P': 'Phosphorylated Chk1',
        'protein_14_3_3': 'Protein 14-3-3',
        'Cdc25Ps216_14_3_3_inactive': 'Cdc25Ps216 14-3-3 Inactive',
        'p53': 'p53 tumor suppressor',
        'p21': 'P21',
        'MPF': 'Maturation-promoting factor',
        'p21_MPF': 'P21 MPF',
        'preMPF': 'Pre MPF',
        'Wee1': 'Wee1 inhibitory kinase',
        'Chk1': 'Chk1 checkpoint kinase',
        'Rad3_ATM': 'Rad3 ATM',
        'Wee1_phosphorylated': 'Wee1 Phosphorylated',
    }
    _PARAMETER_INPUTS = {
        'cdc25_active_total': ('Cdc25_active_total', 1e-06, 'native SBML value', 'Controls Cdc25 Active Total. Maps to SBML symbol `Cdc25_active_total`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cdc25_active': ('Cdc25_active', 'native SBML value', 'Tracks Cdc25 Active. Maps to SBML symbol `Cdc25_active`.'),
        'cdc25ps216_active': ('Cdc25Ps216_active', 'native SBML value', 'Tracks Cdc25Ps216 Active. Maps to SBML symbol `Cdc25Ps216_active`.'),
        'cdc25_inactive': ('Cdc25_inactive', 'native SBML value', 'Tracks Cdc25 Inactive. Maps to SBML symbol `Cdc25_inactive`.'),
        'cdc25ps216_inactive': ('Cdc25Ps216_inactive', 'native SBML value', 'Tracks Cdc25Ps216 Inactive. Maps to SBML symbol `Cdc25Ps216_inactive`.'),
        'phosphorylated_chk1': ('Chk1P', 'native SBML value', 'Tracks Phosphorylated Chk1. Maps to SBML symbol `Chk1P`.'),
        'protein_14_3_3': ('protein_14_3_3', 'native SBML value', 'Tracks Protein 14-3-3. Maps to SBML symbol `protein_14_3_3`.'),
        'cdc25ps216_14_3_3_inactive': ('Cdc25Ps216_14_3_3_inactive', 'native SBML value', 'Tracks Cdc25Ps216 14-3-3 Inactive. Maps to SBML symbol `Cdc25Ps216_14_3_3_inactive`.'),
        'p53_tumor_suppressor': ('p53', 'native SBML value', 'Tracks p53 tumor suppressor. Maps to SBML symbol `p53`.'),
        'p21': ('p21', 'native SBML value', 'Tracks P21. Maps to SBML symbol `p21`.'),
        'maturation_promoting_factor': ('MPF', 'native SBML value', 'Tracks Maturation-promoting factor. Maps to SBML symbol `MPF`.'),
        'p21_mpf': ('p21_MPF', 'native SBML value', 'Tracks P21 MPF. Maps to SBML symbol `p21_MPF`.'),
        'pre_mpf': ('preMPF', 'native SBML value', 'Tracks Pre MPF. Maps to SBML symbol `preMPF`.'),
        'wee1_inhibitory_kinase': ('Wee1', 'native SBML value', 'Tracks Wee1 inhibitory kinase. Maps to SBML symbol `Wee1`.'),
        'chk1_checkpoint_kinase': ('Chk1', 'native SBML value', 'Tracks Chk1 checkpoint kinase. Maps to SBML symbol `Chk1`.'),
        'rad3_atm': ('Rad3_ATM', 'native SBML value', 'Tracks Rad3 ATM. Maps to SBML symbol `Rad3_ATM`.'),
        'wee1_phosphorylated': ('Wee1_phosphorylated', 'native SBML value', 'Tracks Wee1 Phosphorylated. Maps to SBML symbol `Wee1_phosphorylated`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000704.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Aguda1999G2DnaDamageCheckpointBiomd0000000704Model = SbmlAguda1999G2DnaDamageCheckpoint
