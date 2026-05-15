# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Henze2017 - A Dynamical Model for Activating and Silencing the Mitotic Checkpoint.

Source: biomodels_ebi:MODEL1812210002
Original: https://www.ebi.ac.uk/biomodels/MODEL1812210002
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlHenze2017ADynamicalModelForActivatingAndSilencing(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Henze2017 - A Dynamical Model for Activating and Silencing the Mitotic Checkpoint."""

    _SBML_ID = 'MODEL1812210002'
    _TITLE = 'Henze2017 - A Dynamical Model for Activating and Silencing the Mitotic Checkpoint'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'KinA',
        'KinU',
        'APCC_Cdc20',
        'Securin',
        'APCC',
        'Cdc20',
        'CyclinB',
        'APCC_MCC',
        'MCC',
        'C_Mad2',
        'O_Mad2',
        'Cdc20_C_Mad2',
        'BubR1_Bub3',
        'Mad1_Mad2',
        'Mad1_Mad2_C_Mad2',
        'BCC',
        'APCC_Cdc20_C_Mad2',
        'APCC_BCC',
        'APCC_Cdc20_MCC',
    ]
    _SPECIES_LABELS = {
        'KinA': 'Kin A',
        'KinU': 'Kin Model state U',
        'APCC_Cdc20': 'APCC Cdc20',
        'Securin': 'Securin separase inhibitor',
        'APCC': 'APC/C complex',
        'Cdc20': 'Cdc20 APC/C activator',
        'CyclinB': 'Cyclin B',
        'APCC_MCC': 'APCC MCC',
        'MCC': 'Mitotic checkpoint complex',
        'C_Mad2': 'Model state C Mad2',
        'O_Mad2': 'O Mad2',
        'Cdc20_C_Mad2': 'Cdc20 Model state C Mad2',
        'BubR1_Bub3': 'Bub Model state R1 Bub3',
        'Mad1_Mad2': 'Mad1 Mad2',
        'Mad1_Mad2_C_Mad2': 'Mad1 Mad2 Model state C Mad2',
        'BCC': 'BubR1-Cdc20 checkpoint complex',
        'APCC_Cdc20_C_Mad2': 'APCC Cdc20 Model state C Mad2',
        'APCC_BCC': 'APCC BCC',
        'APCC_Cdc20_MCC': 'APCC Cdc20 MCC',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'kin_a': ('KinA', 'native SBML value', 'Tracks Kin A. Maps to SBML symbol `KinA`.'),
        'kin_model_state_u': ('KinU', 'native SBML value', 'Tracks Kin Model state U. Maps to SBML symbol `KinU`.'),
        'apcc_cdc20': ('APCC_Cdc20', 'native SBML value', 'Tracks APCC Cdc20. Maps to SBML symbol `APCC_Cdc20`.'),
        'securin_separase_inhibitor': ('Securin', 'native SBML value', 'Tracks Securin separase inhibitor. Maps to SBML symbol `Securin`.'),
        'apc_c_complex': ('APCC', 'native SBML value', 'Tracks APC/C complex. Maps to SBML symbol `APCC`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'native SBML value', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'cyclin_b': ('CyclinB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `CyclinB`.'),
        'apcc_mcc': ('APCC_MCC', 'native SBML value', 'Tracks APCC MCC. Maps to SBML symbol `APCC_MCC`.'),
        'mitotic_checkpoint_complex': ('MCC', 'native SBML value', 'Tracks Mitotic checkpoint complex. Maps to SBML symbol `MCC`.'),
        'model_state_c_mad2': ('C_Mad2', 'native SBML value', 'Tracks Model state C Mad2. Maps to SBML symbol `C_Mad2`.'),
        'o_mad2': ('O_Mad2', 'native SBML value', 'Tracks O Mad2. Maps to SBML symbol `O_Mad2`.'),
        'cdc20_model_state_c_mad2': ('Cdc20_C_Mad2', 'native SBML value', 'Tracks Cdc20 Model state C Mad2. Maps to SBML symbol `Cdc20_C_Mad2`.'),
        'bub_model_state_r1_bub3': ('BubR1_Bub3', 'native SBML value', 'Tracks Bub Model state R1 Bub3. Maps to SBML symbol `BubR1_Bub3`.'),
        'mad1_mad2': ('Mad1_Mad2', 'native SBML value', 'Tracks Mad1 Mad2. Maps to SBML symbol `Mad1_Mad2`.'),
        'mad1_mad2_model_state_c_mad2': ('Mad1_Mad2_C_Mad2', 'native SBML value', 'Tracks Mad1 Mad2 Model state C Mad2. Maps to SBML symbol `Mad1_Mad2_C_Mad2`.'),
        'bub_r1_cdc20_checkpoint_complex': ('BCC', 'native SBML value', 'Tracks BubR1-Cdc20 checkpoint complex. Maps to SBML symbol `BCC`.'),
        'apcc_cdc20_model_state_c_mad2': ('APCC_Cdc20_C_Mad2', 'native SBML value', 'Tracks APCC Cdc20 Model state C Mad2. Maps to SBML symbol `APCC_Cdc20_C_Mad2`.'),
        'apcc_bcc': ('APCC_BCC', 'native SBML value', 'Tracks APCC BCC. Maps to SBML symbol `APCC_BCC`.'),
        'apcc_cdc20_mcc': ('APCC_Cdc20_MCC', 'native SBML value', 'Tracks APCC Cdc20 MCC. Maps to SBML symbol `APCC_Cdc20_MCC`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1812210002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Henze2017ADynamicalModelForActivatingAndSModel1812210002Model = SbmlHenze2017ADynamicalModelForActivatingAndSilencing
