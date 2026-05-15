# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Tsai2014 - Cell cycle duration control by oscillatory Dynamics in Early Xenopus laevis Embryos.

Source: biomodels_ebi:BIOMD0000000719
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000719
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlTsai2014CellCycleDurationControlByOscillatory(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Tsai2014 - Cell cycle duration control by oscillatory Dynamics in Early Xenopus laevis Embryos."""

    _SBML_ID = 'BIOMD0000000719'
    _TITLE = 'Tsai2014 - Cell cycle duration control by oscillatory Dynamics in Early Xenopus laevis Embryos'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Cyclin_B1_Cdk1_complex_phosphorylated',
        'Cyclin_B1_Cdk1_complex_unphosphorylated',
        'Plx1_active',
        'APC_C_active',
        'APC_C_total',
    ]
    _SPECIES_LABELS = {
        'Cyclin_B1_Cdk1_complex_phosphorylated': 'Cyclin B1 CDK1 Complex Phosphorylated',
        'Cyclin_B1_Cdk1_complex_unphosphorylated': 'Cyclin B1 CDK1 Complex Unphosphorylated',
        'Plx1_active': 'Plx1 Active',
        'APC_C_active': 'APC/C/C Model state C Active',
        'APC_C_total': 'APC/C/C Model state C Total',
    }
    _PARAMETER_INPUTS = {
        'plx1_total': ('Plx1_total', 1.0, 'native SBML value', 'Controls Plx1 Total. Maps to SBML symbol `Plx1_total`.'),
        'cyclin_b1_cdk1_complex_total': ('Cyclin_B1_Cdk1_complex_total', 60.0, 'native SBML value', 'Controls Cyclin B1 CDK1 Complex Total. Maps to SBML symbol `Cyclin_B1_Cdk1_complex_total`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cyclin_b1_cdk1_complex_phosphorylated': ('Cyclin_B1_Cdk1_complex_phosphorylated', 'native SBML value', 'Tracks Cyclin B1 CDK1 Complex Phosphorylated. Maps to SBML symbol `Cyclin_B1_Cdk1_complex_phosphorylated`.'),
        'cyclin_b1_cdk1_complex_unphosphorylated': ('Cyclin_B1_Cdk1_complex_unphosphorylated', 'native SBML value', 'Tracks Cyclin B1 CDK1 Complex Unphosphorylated. Maps to SBML symbol `Cyclin_B1_Cdk1_complex_unphosphorylated`.'),
        'plx1_active': ('Plx1_active', 'native SBML value', 'Tracks Plx1 Active. Maps to SBML symbol `Plx1_active`.'),
        'apc_c_c_model_state_c_active': ('APC_C_active', 'native SBML value', 'Tracks APC/C/C Model state C Active. Maps to SBML symbol `APC_C_active`.'),
        'apc_c_c_model_state_c_total': ('APC_C_total', 'native SBML value', 'Tracks APC/C/C Model state C Total. Maps to SBML symbol `APC_C_total`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000719.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Tsai2014CellCycleDurationControlByOscillatBiomd0000000719Model = SbmlTsai2014CellCycleDurationControlByOscillatory
