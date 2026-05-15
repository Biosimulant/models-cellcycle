# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ciliberto2003 - CyclinE / Cdk2 timer in the cell cycle of Xenopus laevis embryo.

Source: biomodels_ebi:BIOMD0000000697
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000697
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlCiliberto2003CyclineCdk2TimerInTheCellCycleOf(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ciliberto2003 - CyclinE / Cdk2 timer in the cell cycle of Xenopus laevis embryo."""

    _SBML_ID = 'BIOMD0000000697'
    _TITLE = 'Ciliberto2003 - CyclinE / Cdk2 timer in the cell cycle of Xenopus laevis embryo'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'PCdk2_CycE',
        'Cdk2_CycE',
        'Wee1_a',
        'Cdk2_CycErem',
        'PCdk2_CycErem',
        'Deg_a',
        'Xic',
        'Xic_Cdk2_CycE',
        'Xic_PCdk2_CycE',
        'Xic_Cdk2_CycErem',
        'Xic_PCdk2_CycErem',
        'Xicrem',
        'Kin_a',
    ]
    _SPECIES_LABELS = {
        'PCdk2_CycE': 'PCdk2 Cyclin E',
        'Cdk2_CycE': 'CDK2 Cyclin E',
        'Wee1_a': 'Wee1 A',
        'Cdk2_CycErem': 'CDK2 Cyclin Erem',
        'PCdk2_CycErem': 'PCdk2 Cyclin Erem',
        'Deg_a': 'Oxygen-dependent degradation factor Cyclin E',
        'Xic': 'Xic CDK inhibitor',
        'Xic_Cdk2_CycE': 'Xic CDK2 Cyclin E',
        'Xic_PCdk2_CycE': 'Xic PCdk2 Cyclin E',
        'Xic_Cdk2_CycErem': 'Xic CDK2 Cyclin Erem',
        'Xic_PCdk2_CycErem': 'Xic PCdk2 Cyclin Erem',
        'Xicrem': 'Removed Xic inhibitor pool',
        'Kin_a': 'Kin A',
    }
    _PARAMETER_INPUTS = {
        'wee1_total': ('Wee1_total', 7.99999999999998, 'native SBML value', 'Controls Wee1 Total. Maps to SBML symbol `Wee1_total`.'),
        'cyclin_total': ('Cyc_total', 0.9999999999999999, 'native SBML value', 'Controls Cyclin Total. Maps to SBML symbol `Cyc_total`.'),
        'xic_total': ('Xic_total', 0.9999999999999933, 'native SBML value', 'Controls Xic Total. Maps to SBML symbol `Xic_total`.'),
    }
    _HEADLINE_OUTPUTS = {
        'pcdk2_cyclin_e': ('PCdk2_CycE', 'native SBML value', 'Tracks PCdk2 Cyclin E. Maps to SBML symbol `PCdk2_CycE`.'),
        'cdk2_cyclin_e': ('Cdk2_CycE', 'native SBML value', 'Tracks CDK2 Cyclin E. Maps to SBML symbol `Cdk2_CycE`.'),
        'wee1_a': ('Wee1_a', 'native SBML value', 'Tracks Wee1 A. Maps to SBML symbol `Wee1_a`.'),
        'cdk2_cyclin_erem': ('Cdk2_CycErem', 'native SBML value', 'Tracks CDK2 Cyclin Erem. Maps to SBML symbol `Cdk2_CycErem`.'),
        'pcdk2_cyclin_erem': ('PCdk2_CycErem', 'native SBML value', 'Tracks PCdk2 Cyclin Erem. Maps to SBML symbol `PCdk2_CycErem`.'),
        'oxygen_dependent_degradation_factor_cyclin_e': ('Deg_a', 'native SBML value', 'Tracks Oxygen-dependent degradation factor Cyclin E. Maps to SBML symbol `Deg_a`.'),
        'xic_cdk_inhibitor': ('Xic', 'native SBML value', 'Tracks Xic CDK inhibitor. Maps to SBML symbol `Xic`.'),
        'xic_cdk2_cyclin_e': ('Xic_Cdk2_CycE', 'native SBML value', 'Tracks Xic CDK2 Cyclin E. Maps to SBML symbol `Xic_Cdk2_CycE`.'),
        'xic_pcdk2_cyclin_e': ('Xic_PCdk2_CycE', 'native SBML value', 'Tracks Xic PCdk2 Cyclin E. Maps to SBML symbol `Xic_PCdk2_CycE`.'),
        'xic_cdk2_cyclin_erem': ('Xic_Cdk2_CycErem', 'native SBML value', 'Tracks Xic CDK2 Cyclin Erem. Maps to SBML symbol `Xic_Cdk2_CycErem`.'),
        'xic_pcdk2_cyclin_erem': ('Xic_PCdk2_CycErem', 'native SBML value', 'Tracks Xic PCdk2 Cyclin Erem. Maps to SBML symbol `Xic_PCdk2_CycErem`.'),
        'removed_xic_inhibitor_pool': ('Xicrem', 'native SBML value', 'Tracks Removed Xic inhibitor pool. Maps to SBML symbol `Xicrem`.'),
        'kin_a': ('Kin_a', 'native SBML value', 'Tracks Kin A. Maps to SBML symbol `Kin_a`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000697.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ciliberto2003CyclineCdk2TimerInTheCellCycBiomd0000000697Model = SbmlCiliberto2003CyclineCdk2TimerInTheCellCycleOf
