# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Novak1998 - Mathematical model of fission yeast cell cycle.

Source: biomodels_ebi:MODEL2003190004
Original: https://www.ebi.ac.uk/biomodels/MODEL2003190004
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNovak1998MathematicalModelOfFissionYeastCellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Novak1998 - Mathematical model of fission yeast cell cycle."""

    _SBML_ID = 'MODEL2003190004'
    _TITLE = 'Novak1998 - Mathematical model of fission yeast cell cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'AAE',
        'Cdc13_Cdc2',
        'Mik1',
        'AAE_total',
        'Wee1',
        'Rum1',
        'mass',
        'Cdc13_P_Cdc2',
        'Rum1_Cdc13_Cdc2',
        'APC',
        'Cdc25P',
        'Cdc13_total',
        'MPF',
        'Rum1_total',
        'k2',
        'k25r',
        'k2c',
        'k4',
        'kai',
        'kcdc25',
        'kmr',
        'ks',
        'kwee',
        'kwr',
    ]
    _SPECIES_LABELS = {
        'AAE': 'Aggregated APC/C enzyme state',
        'Cdc13_Cdc2': 'Cdc13 Cdc2',
        'Mik1': 'Mik1 inhibitory kinase',
        'AAE_total': 'AAE Total',
        'Wee1': 'Wee1 inhibitory kinase',
        'Rum1': 'Rum1 CDK inhibitor',
        'mass': 'Mass',
        'Cdc13_P_Cdc2': 'Cdc13 P Cdc2',
        'Rum1_Cdc13_Cdc2': 'Rum1 Cdc13 Cdc2',
        'APC': 'APC/C/C',
        'Cdc25P': 'Phosphorylated Cdc25',
        'Cdc13_total': 'Cdc13 Total',
        'MPF': 'Maturation-promoting factor',
        'Rum1_total': 'Rum1 Total',
        'k2': 'Model state K2',
        'k25r': 'K25r',
        'k2c': 'K2c',
        'k4': 'Model state K4',
        'kai': 'Kai',
        'kcdc25': 'Kcdc25',
        'kmr': 'Kmr',
        'ks': 'Model state Ks',
        'kwee': 'Kwee',
        'kwr': 'Kwr',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'aggregated_apc_c_enzyme_state': ('AAE', 'unit_1', 'Tracks Aggregated APC/C enzyme state. Maps to SBML symbol `AAE`.'),
        'cdc13_cdc2': ('Cdc13_Cdc2', 'unit_1', 'Tracks Cdc13 Cdc2. Maps to SBML symbol `Cdc13_Cdc2`.'),
        'mik1_inhibitory_kinase': ('Mik1', 'unit_1', 'Tracks Mik1 inhibitory kinase. Maps to SBML symbol `Mik1`.'),
        'aae_total': ('AAE_total', 'unit_1', 'Tracks AAE Total. Maps to SBML symbol `AAE_total`.'),
        'wee1_inhibitory_kinase': ('Wee1', 'unit_1', 'Tracks Wee1 inhibitory kinase. Maps to SBML symbol `Wee1`.'),
        'rum1_cdk_inhibitor': ('Rum1', 'unit_1', 'Tracks Rum1 CDK inhibitor. Maps to SBML symbol `Rum1`.'),
        'mass': ('mass', 'unit_1', 'Tracks Mass. Maps to SBML symbol `mass`.'),
        'cdc13_p_cdc2': ('Cdc13_P_Cdc2', 'unit_1', 'Tracks Cdc13 P Cdc2. Maps to SBML symbol `Cdc13_P_Cdc2`.'),
        'rum1_cdc13_cdc2': ('Rum1_Cdc13_Cdc2', 'unit_1', 'Tracks Rum1 Cdc13 Cdc2. Maps to SBML symbol `Rum1_Cdc13_Cdc2`.'),
        'apc_c_c': ('APC', 'unit_1', 'Tracks APC/C/C. Maps to SBML symbol `APC`.'),
        'phosphorylated_cdc25': ('Cdc25P', 'unit_1', 'Tracks Phosphorylated Cdc25. Maps to SBML symbol `Cdc25P`.'),
        'cdc13_total': ('Cdc13_total', 'dimensionless', 'Tracks Cdc13 Total. Maps to SBML symbol `Cdc13_total`.'),
        'maturation_promoting_factor': ('MPF', 'unit_1', 'Tracks Maturation-promoting factor. Maps to SBML symbol `MPF`.'),
        'rum1_total': ('Rum1_total', 'dimensionless', 'Tracks Rum1 Total. Maps to SBML symbol `Rum1_total`.'),
        'model_state_k2': ('k2', 'unit_0', 'Tracks Model state K2. Maps to SBML symbol `k2`.'),
        'k25r': ('k25r', 'unit_0', 'Tracks K25r. Maps to SBML symbol `k25r`.'),
        'k2c': ('k2c', 'unit_0', 'Tracks K2c. Maps to SBML symbol `k2c`.'),
        'model_state_k4': ('k4', 'unit_0', 'Tracks Model state K4. Maps to SBML symbol `k4`.'),
        'kai': ('kai', 'unit_0', 'Tracks Kai. Maps to SBML symbol `kai`.'),
        'kcdc25': ('kcdc25', 'unit_0', 'Tracks Kcdc25. Maps to SBML symbol `kcdc25`.'),
        'kmr': ('kmr', 'unit_0', 'Tracks Kmr. Maps to SBML symbol `kmr`.'),
        'model_state_ks': ('ks', 'unit_0', 'Tracks Model state Ks. Maps to SBML symbol `ks`.'),
        'kwee': ('kwee', 'unit_0', 'Tracks Kwee. Maps to SBML symbol `kwee`.'),
        'kwr': ('kwr', 'unit_0', 'Tracks Kwr. Maps to SBML symbol `kwr`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2003190004.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Novak1998MathematicalModelOfFissionYeastCeModel2003190004Model = SbmlNovak1998MathematicalModelOfFissionYeastCellCycle
