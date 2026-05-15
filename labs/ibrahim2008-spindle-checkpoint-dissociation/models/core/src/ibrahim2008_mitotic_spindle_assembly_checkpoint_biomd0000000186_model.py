# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ibrahim2008 - Mitotic Spindle Assembly Checkpoint - Dissociation variant.

Source: biomodels_ebi:BIOMD0000000186
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000186
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlIbrahim2008MitoticSpindleAssemblyCheckpoint(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ibrahim2008 - Mitotic Spindle Assembly Checkpoint - Dissociation variant."""

    _SBML_ID = 'BIOMD0000000186'
    _TITLE = 'Ibrahim2008 - Mitotic Spindle Assembly Checkpoint - Dissociation variant'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Mad1_CMad2',
        'OMad2',
        'Mad1_CMad2_OMad2',
        'Cdc20',
        'Cdc20_CMad2',
        'Bub3_BubR1',
        'MCC',
        'Bub3_BubR1_Cdc20',
        'APC',
        'MCC_APC',
        'APC_Cdc20',
    ]
    _SPECIES_LABELS = {
        'Mad1_CMad2': 'Mad1:C Mad2',
        'OMad2': 'O Mad2',
        'Mad1_CMad2_OMad2': 'Mad1:C Mad2:O Mad2*',
        'Cdc20': 'Cdc20 APC/C activator',
        'Cdc20_CMad2': 'Cdc20:C Mad2',
        'Bub3_BubR1': 'Bub3:Bub Model state R1',
        'MCC': 'Mitotic checkpoint complex',
        'Bub3_BubR1_Cdc20': 'Bub3:Bub R1:Cdc20',
        'APC': 'APC/C/C',
        'MCC_APC': 'MCC:APC/C/C',
        'APC_Cdc20': 'APC/C/C:Cdc20',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'mad1_c_mad2': ('Mad1_CMad2', 'mole', 'Tracks Mad1:C Mad2. Maps to SBML symbol `Mad1_CMad2`.'),
        'o_mad2': ('OMad2', 'mole', 'Tracks O Mad2. Maps to SBML symbol `OMad2`.'),
        'mad1_c_mad2_o_mad2': ('Mad1_CMad2_OMad2', 'mole', 'Tracks Mad1:C Mad2:O Mad2*. Maps to SBML symbol `Mad1_CMad2_OMad2`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'mole', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'cdc20_c_mad2': ('Cdc20_CMad2', 'mole', 'Tracks Cdc20:C Mad2. Maps to SBML symbol `Cdc20_CMad2`.'),
        'bub3_bub_model_state_r1': ('Bub3_BubR1', 'mole', 'Tracks Bub3:Bub Model state R1. Maps to SBML symbol `Bub3_BubR1`.'),
        'mitotic_checkpoint_complex': ('MCC', 'mole', 'Tracks Mitotic checkpoint complex. Maps to SBML symbol `MCC`.'),
        'bub3_bub_r1_cdc20': ('Bub3_BubR1_Cdc20', 'mole', 'Tracks Bub3:Bub R1:Cdc20. Maps to SBML symbol `Bub3_BubR1_Cdc20`.'),
        'apc_c_c': ('APC', 'mole', 'Tracks APC/C/C. Maps to SBML symbol `APC`.'),
        'mcc_apc_c_c': ('MCC_APC', 'mole', 'Tracks MCC:APC/C/C. Maps to SBML symbol `MCC_APC`.'),
        'apc_c_c_cdc20': ('APC_Cdc20', 'mole', 'Tracks APC/C/C:Cdc20. Maps to SBML symbol `APC_Cdc20`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000186.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ibrahim2008MitoticSpindleAssemblyCheckpointBiomd0000000186Model = SbmlIbrahim2008MitoticSpindleAssemblyCheckpoint
