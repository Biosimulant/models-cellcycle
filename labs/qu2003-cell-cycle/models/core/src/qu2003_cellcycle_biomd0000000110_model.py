# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Qu2003_CellCycle.

Source: biomodels_ebi:BIOMD0000000110
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000110
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlQu2003Cellcycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Qu2003_CellCycle."""

    _SBML_ID = 'BIOMD0000000110'
    _TITLE = 'Qu2003_CellCycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'x1',
        'x',
        'c0',
        'z0',
        'z1',
        'z2',
        'w0',
        'w1',
        'u',
        'i',
        'ix',
        'ixp',
        'y',
        'c',
        'totalCyclin',
    ]
    _SPECIES_LABELS = {
        'x1': 'Inactive Cyclin:CDK Complex',
        'x': 'Active Cyclin:CDK Complex',
        'c0': 'Total CDK',
        'z0': 'Unphosphorylated Cdc25',
        'z1': 'One Site Phosphorylated Cdc25',
        'z2': 'Two Site Phosphorylated Cdc25',
        'w0': 'Unphosphorylated Wee1',
        'w1': 'Phosphorylated Wee1',
        'u': 'Active SKP2 Or APC/C/C',
        'i': 'Free CKI',
        'ix': 'Cyclin:CDK:CKI Complex With CKI Unphosphorylated',
        'ixp': 'Cyclin:CDK:CKI Complex With CKI Phosphorylated',
        'y': 'Free Cyclin',
        'c': 'Free CDK',
        'totalCyclin': 'Total Cyclin',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'inactive_cyclin_cdk_complex': ('x1', 'native SBML value', 'Tracks Inactive Cyclin:CDK Complex. Maps to SBML symbol `x1`.'),
        'active_cyclin_cdk_complex': ('x', 'native SBML value', 'Tracks Active Cyclin:CDK Complex. Maps to SBML symbol `x`.'),
        'total_cdk': ('c0', 'native SBML value', 'Tracks Total CDK. Maps to SBML symbol `c0`.'),
        'unphosphorylated_cdc25': ('z0', 'native SBML value', 'Tracks Unphosphorylated Cdc25. Maps to SBML symbol `z0`.'),
        'one_site_phosphorylated_cdc25': ('z1', 'native SBML value', 'Tracks One Site Phosphorylated Cdc25. Maps to SBML symbol `z1`.'),
        'two_site_phosphorylated_cdc25': ('z2', 'native SBML value', 'Tracks Two Site Phosphorylated Cdc25. Maps to SBML symbol `z2`.'),
        'unphosphorylated_wee1': ('w0', 'native SBML value', 'Tracks Unphosphorylated Wee1. Maps to SBML symbol `w0`.'),
        'phosphorylated_wee1': ('w1', 'native SBML value', 'Tracks Phosphorylated Wee1. Maps to SBML symbol `w1`.'),
        'active_skp2_or_apc_c_c': ('u', 'native SBML value', 'Tracks Active SKP2 Or APC/C/C. Maps to SBML symbol `u`.'),
        'free_cki': ('i', 'native SBML value', 'Tracks Free CKI. Maps to SBML symbol `i`.'),
        'cyclin_cdk_cki_complex_with_cki_unphosphorylated': ('ix', 'native SBML value', 'Tracks Cyclin:CDK:CKI Complex With CKI Unphosphorylated. Maps to SBML symbol `ix`.'),
        'cyclin_cdk_cki_complex_with_cki_phosphorylated': ('ixp', 'native SBML value', 'Tracks Cyclin:CDK:CKI Complex With CKI Phosphorylated. Maps to SBML symbol `ixp`.'),
        'free_cyclin': ('y', 'native SBML value', 'Tracks Free Cyclin. Maps to SBML symbol `y`.'),
        'free_cdk': ('c', 'native SBML value', 'Tracks Free CDK. Maps to SBML symbol `c`.'),
        'total_cyclin': ('totalCyclin', 'native SBML value', 'Tracks Total Cyclin. Maps to SBML symbol `totalCyclin`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000110.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Qu2003CellcycleBiomd0000000110Model = SbmlQu2003Cellcycle
