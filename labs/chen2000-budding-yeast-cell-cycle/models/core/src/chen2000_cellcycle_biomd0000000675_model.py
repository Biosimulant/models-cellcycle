# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Chen2000_CellCycle.

Source: biomodels_ebi:BIOMD0000000675
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000675
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlChen2000Cellcycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Chen2000_CellCycle."""

    _SBML_ID = 'BIOMD0000000675'
    _TITLE = 'Chen2000_CellCycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'Cln2',
        'Cdc20',
        'Cdc20_T',
        'Hct1',
        'Clb2_Sic1',
        'Sic1_T',
        'Clb5_Sic1',
        'Clb5_T',
        'Clb2_T',
        'mass',
        'ORI',
        'BUD',
        'SPN',
        'Bck2',
        'Clb2',
        'Clb5',
        'Cln3',
        'D',
        'MBF',
        'Mcm1',
        'SBF',
        'Sic1',
        'Swi5',
        'Va_sbf',
        'Vd2_c1',
        'Vd_b2',
        'Vd_b5',
        'Vi_20',
        'Vi_t1',
    ]
    _SPECIES_LABELS = {
        'Cln2': 'Cln2 G1 cyclin',
        'Cdc20': 'Cdc20 APC/C activator',
        'Cdc20_T': 'Cdc20 T',
        'Hct1': 'Hct1 APC/C activator',
        'Clb2_Sic1': 'Clb2 Sic1',
        'Sic1_T': 'Sic1 T',
        'Clb5_Sic1': 'Clb5 Sic1',
        'Clb5_T': 'Clb5 T',
        'Clb2_T': 'Clb2 T',
        'mass': 'Mass',
        'ORI': 'Replication origin state',
        'BUD': 'Budding index',
        'SPN': 'Spindle state',
        'Bck2': 'Bck2 G1 regulator',
        'Clb2': 'Clb2 mitotic cyclin',
        'Clb5': 'Clb5 S-phase cyclin',
        'Cln3': 'Cln3 Start cyclin',
        'D': 'Model state D',
        'MBF': 'MBF transcription factor',
        'Mcm1': 'Mcm1 transcription factor',
        'SBF': 'SBF transcription factor',
        'Sic1': 'Sic1 CDK inhibitor',
        'Swi5': 'Swi5 transcription factor',
        'Va_sbf': 'Va Sbf',
        'Vd2_c1': 'Vd2 Model state C1',
        'Vd_b2': 'Vd B2',
        'Vd_b5': 'Vd B5',
        'Vi_20': 'Vi 20',
        'Vi_t1': 'Vi T1',
    }
    _PARAMETER_INPUTS = {
        'hct1_t': ('Hct1_T', 1.0, 'native SBML value', 'Controls Hct1 T. Maps to SBML symbol `Hct1_T`.'),
        'bck2_0': ('Bck2_0', 0.0027, 'native SBML value', 'Controls Bck2 0. Maps to SBML symbol `Bck2_0`.'),
        'cln3_max': ('Cln3_max', 0.02, 'native SBML value', 'Controls Cln3 Max. Maps to SBML symbol `Cln3_max`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cln2_g1_cyclin': ('Cln2', 'native SBML value', 'Tracks Cln2 G1 cyclin. Maps to SBML symbol `Cln2`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'native SBML value', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'cdc20_t': ('Cdc20_T', 'native SBML value', 'Tracks Cdc20 T. Maps to SBML symbol `Cdc20_T`.'),
        'hct1_apc_c_activator': ('Hct1', 'native SBML value', 'Tracks Hct1 APC/C activator. Maps to SBML symbol `Hct1`.'),
        'clb2_sic1': ('Clb2_Sic1', 'native SBML value', 'Tracks Clb2 Sic1. Maps to SBML symbol `Clb2_Sic1`.'),
        'sic1_t': ('Sic1_T', 'native SBML value', 'Tracks Sic1 T. Maps to SBML symbol `Sic1_T`.'),
        'clb5_sic1': ('Clb5_Sic1', 'native SBML value', 'Tracks Clb5 Sic1. Maps to SBML symbol `Clb5_Sic1`.'),
        'clb5_t': ('Clb5_T', 'native SBML value', 'Tracks Clb5 T. Maps to SBML symbol `Clb5_T`.'),
        'clb2_t': ('Clb2_T', 'native SBML value', 'Tracks Clb2 T. Maps to SBML symbol `Clb2_T`.'),
        'mass': ('mass', 'dimensionless', 'Tracks Mass. Maps to SBML symbol `mass`.'),
        'replication_origin_state': ('ORI', 'dimensionless', 'Tracks Replication origin state. Maps to SBML symbol `ORI`.'),
        'budding_index': ('BUD', 'dimensionless', 'Tracks Budding index. Maps to SBML symbol `BUD`.'),
        'spindle_state': ('SPN', 'dimensionless', 'Tracks Spindle state. Maps to SBML symbol `SPN`.'),
        'bck2_g1_regulator': ('Bck2', 'native SBML value', 'Tracks Bck2 G1 regulator. Maps to SBML symbol `Bck2`.'),
        'clb2_mitotic_cyclin': ('Clb2', 'native SBML value', 'Tracks Clb2 mitotic cyclin. Maps to SBML symbol `Clb2`.'),
        'clb5_s_phase_cyclin': ('Clb5', 'native SBML value', 'Tracks Clb5 S-phase cyclin. Maps to SBML symbol `Clb5`.'),
        'cln3_start_cyclin': ('Cln3', 'native SBML value', 'Tracks Cln3 Start cyclin. Maps to SBML symbol `Cln3`.'),
        'model_state_d': ('D', 'dimensionless', 'Tracks Model state D. Maps to SBML symbol `D`.'),
        'mbf_transcription_factor': ('MBF', 'native SBML value', 'Tracks MBF transcription factor. Maps to SBML symbol `MBF`.'),
        'mcm1_transcription_factor': ('Mcm1', 'native SBML value', 'Tracks Mcm1 transcription factor. Maps to SBML symbol `Mcm1`.'),
        'sbf_transcription_factor': ('SBF', 'native SBML value', 'Tracks SBF transcription factor. Maps to SBML symbol `SBF`.'),
        'sic1_cdk_inhibitor': ('Sic1', 'native SBML value', 'Tracks Sic1 CDK inhibitor. Maps to SBML symbol `Sic1`.'),
        'swi5_transcription_factor': ('Swi5', 'native SBML value', 'Tracks Swi5 transcription factor. Maps to SBML symbol `Swi5`.'),
        'va_sbf': ('Va_sbf', 'dimensionless', 'Tracks Va Sbf. Maps to SBML symbol `Va_sbf`.'),
        'vd2_model_state_c1': ('Vd2_c1', 'dimensionless', 'Tracks Vd2 Model state C1. Maps to SBML symbol `Vd2_c1`.'),
        'vd_b2': ('Vd_b2', 'dimensionless', 'Tracks Vd B2. Maps to SBML symbol `Vd_b2`.'),
        'vd_b5': ('Vd_b5', 'dimensionless', 'Tracks Vd B5. Maps to SBML symbol `Vd_b5`.'),
        'vi_20': ('Vi_20', 'dimensionless', 'Tracks Vi 20. Maps to SBML symbol `Vi_20`.'),
        'vi_t1': ('Vi_t1', 'dimensionless', 'Tracks Vi T1. Maps to SBML symbol `Vi_t1`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000675.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Chen2000CellcycleBiomd0000000675Model = SbmlChen2000Cellcycle
