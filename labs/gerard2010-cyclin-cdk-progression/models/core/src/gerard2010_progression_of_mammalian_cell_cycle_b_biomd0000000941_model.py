# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Gerard2010 - Progression of mammalian cell cycle by successive activation of various cyclin cdk complexes.

Source: biomodels_ebi:BIOMD0000000941
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000941
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlGerard2010ProgressionOfMammalianCellCycleBy(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Gerard2010 - Progression of mammalian cell cycle by successive activation of various cyclin cdk complexes."""

    _SBML_ID = 'BIOMD0000000941'
    _TITLE = 'Gerard2010 - Progression of mammalian cell cycle by successive activation of various cyclin cdk complexes'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'cyclin_D_Cdk4_6',
        'transcription_factor_E2F_active',
        'cyclin_E_Cdk2',
        'cyclin_A_Cdk2',
        'cyclin_B_Cdk1',
        'Cdc20_active',
        'E2F_total',
        'Cdc20_total',
    ]
    _SPECIES_LABELS = {
        'cyclin_D_Cdk4_6': 'Cyclin D CDK4 6',
        'transcription_factor_E2F_active': 'Transcription Factor E2F Active',
        'cyclin_E_Cdk2': 'Cyclin E CDK2',
        'cyclin_A_Cdk2': 'Cyclin Active CDK2',
        'cyclin_B_Cdk1': 'Cyclin B CDK1',
        'Cdc20_active': 'Cdc20 Active',
        'E2F_total': 'E2F Total',
        'Cdc20_total': 'Cdc20 Total',
    }
    _PARAMETER_INPUTS = {
        'growth_factor': ('GF', 1.0, 'dimensionless', 'Controls Growth Factor. Maps to SBML symbol `GF`.'),
        'kgf': ('Kgf', 0.1, 'dimensionless', 'Controls Kgf. Maps to SBML symbol `Kgf`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cyclin_d_cdk4_6': ('cyclin_D_Cdk4_6', 'native SBML value', 'Tracks Cyclin D CDK4 6. Maps to SBML symbol `cyclin_D_Cdk4_6`.'),
        'transcription_factor_e2f_active': ('transcription_factor_E2F_active', 'native SBML value', 'Tracks Transcription Factor E2F Active. Maps to SBML symbol `transcription_factor_E2F_active`.'),
        'cyclin_e_cdk2': ('cyclin_E_Cdk2', 'native SBML value', 'Tracks Cyclin E CDK2. Maps to SBML symbol `cyclin_E_Cdk2`.'),
        'cyclin_active_cdk2': ('cyclin_A_Cdk2', 'native SBML value', 'Tracks Cyclin Active CDK2. Maps to SBML symbol `cyclin_A_Cdk2`.'),
        'cyclin_b_cdk1': ('cyclin_B_Cdk1', 'native SBML value', 'Tracks Cyclin B CDK1. Maps to SBML symbol `cyclin_B_Cdk1`.'),
        'cdc20_active': ('Cdc20_active', 'native SBML value', 'Tracks Cdc20 Active. Maps to SBML symbol `Cdc20_active`.'),
        'e2f_total': ('E2F_total', 'native SBML value', 'Tracks E2F Total. Maps to SBML symbol `E2F_total`.'),
        'cdc20_total': ('Cdc20_total', 'native SBML value', 'Tracks Cdc20 Total. Maps to SBML symbol `Cdc20_total`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000941.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Gerard2010ProgressionOfMammalianCellCycleBBiomd0000000941Model = SbmlGerard2010ProgressionOfMammalianCellCycleBy
