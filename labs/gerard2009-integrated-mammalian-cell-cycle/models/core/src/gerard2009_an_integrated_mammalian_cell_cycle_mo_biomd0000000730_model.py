# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Gerard2009 - An Integrated Mammalian Cell Cycle Model.

Source: biomodels_ebi:BIOMD0000000730
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000730
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlGerard2009AnIntegratedMammalianCellCycleModel(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Gerard2009 - An Integrated Mammalian Cell Cycle Model."""

    _SBML_ID = 'BIOMD0000000730'
    _TITLE = 'Gerard2009 - An Integrated Mammalian Cell Cycle Model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'pRB',
        'pRBp',
        'pRBpp',
        'E2F',
        'E2Fp',
        'pRBc1',
        'pRBc2',
        'Cd',
        'Mdi',
        'Md',
        'Mdp27',
        'Ce',
        'Mei',
        'Me',
        'Skp2',
        'Mep27',
        'Pei',
        'Pe',
        'Ca',
        'Mai',
        'Ma',
        'Map27',
        'p27',
        'p27p',
        'Cdh1i',
        'Cdh1a',
        'Pai',
        'Pa',
        'Cb',
        'Mbi',
        'Mb',
        'Mbp27',
        'Cdc20i',
        'Cdc20a',
        'Pbi',
        'Pb',
        'Wee1',
        'Wee1p',
        'Pol',
        'Cdc45',
        'Primer',
        'Chk1',
        'ATR',
        'AP1',
        'Mw',
    ]
    _SPECIES_LABELS = {
        'pRB': 'Phosphorylated Rb',
        'pRBp': 'Singly phosphorylated Rb',
        'pRBpp': 'Hyperphosphorylated Rb',
        'E2F': 'E2F transcription factor',
        'E2Fp': 'Phosphorylated E2F',
        'pRBc1': 'Rb-E2F complex',
        'pRBc2': 'Phosphorylated Rb-E2F complex',
        'Cd': 'Cyclin D',
        'Mdi': 'Inactive Cyclin D-CDK4/6 complex',
        'Md': 'Active Cyclin D-CDK4/6 complex',
        'Mdp27': 'Cyclin D-CDK4/6-p27 complex',
        'Ce': 'Cyclin E',
        'Mei': 'Inactive Cyclin E-CDK2 complex',
        'Me': 'Active Cyclin E-CDK2 complex',
        'Skp2': 'Skp2 ubiquitin-ligase adaptor',
        'Mep27': 'Cyclin E-CDK2-p27 complex',
        'Pei': 'Inactive Cyclin E module regulator',
        'Pe': 'Active Cyclin E module regulator',
        'Ca': 'Cyclin A',
        'Mai': 'Inactive Cyclin A-CDK2 complex',
        'Ma': 'Active Cyclin A-CDK2 complex',
        'Map27': 'Cyclin A-CDK2-p27 complex',
        'p27': 'p27 CDK inhibitor',
        'p27p': 'Phosphorylated p27',
        'Cdh1i': 'Inactive Cdh1',
        'Cdh1a': 'Active Cdh1',
        'Pai': 'Inactive Cyclin A module regulator',
        'Pa': 'Active Cyclin A module regulator',
        'Cb': 'Cyclin B',
        'Mbi': 'Inactive Cyclin B-CDK1 complex',
        'Mb': 'Active Cyclin B-CDK1 complex',
        'Mbp27': 'Cyclin B-CDK1-p27 complex',
        'Cdc20i': 'Inactive Cdc20',
        'Cdc20a': 'Active Cdc20',
        'Pbi': 'Inactive Cyclin B module regulator',
        'Pb': 'Active Cyclin B module regulator',
        'Wee1': 'Wee1 inhibitory kinase',
        'Wee1p': 'Phosphorylated Wee1',
        'Pol': 'DNA polymerase',
        'Cdc45': 'Cdc45 replication factor',
        'Primer': 'Replication primer',
        'Chk1': 'Chk1 checkpoint kinase',
        'ATR': 'ATR checkpoint kinase',
        'AP1': 'AP1 transcription factor',
        'Mw': 'Wee1 module regulator',
    }
    _PARAMETER_INPUTS = {
        'growth_factor': ('GF', 1.0, 'dimensionless', 'External growth-factor stimulus. Maps to SBML symbol `GF`.'),
        'growth_factor_activation_rate': ('Kagf', 0.1, 'dimensionless', 'Growth-factor activation parameter. Maps to SBML symbol `Kagf`.'),
    }
    _HEADLINE_OUTPUTS = {
        'phosphorylated_rb': ('pRB', 'native SBML value', 'Rb phosphorylation state. Maps to SBML symbol `pRB`.'),
        'singly_phosphorylated_rb': ('pRBp', 'native SBML value', 'Intermediate phosphorylated Rb state. Maps to SBML symbol `pRBp`.'),
        'hyperphosphorylated_rb': ('pRBpp', 'native SBML value', 'Hyperphosphorylated Rb state. Maps to SBML symbol `pRBpp`.'),
        'e2f': ('E2F', 'native SBML value', 'E2F transcription-factor pool. Maps to SBML symbol `E2F`.'),
        'phosphorylated_e2f': ('E2Fp', 'native SBML value', 'Phosphorylated E2F pool. Maps to SBML symbol `E2Fp`.'),
        'rb_e2f_complex': ('pRBc1', 'native SBML value', 'Rb-E2F inhibitory complex. Maps to SBML symbol `pRBc1`.'),
        'phosphorylated_rb_e2f_complex': ('pRBc2', 'native SBML value', 'Phosphorylated Rb-E2F complex. Maps to SBML symbol `pRBc2`.'),
        'cyclin_d': ('Cd', 'native SBML value', 'Cyclin D module species. Maps to SBML symbol `Cd`.'),
        'inactive_cyclin_d_cdk_complex': ('Mdi', 'native SBML value', 'Inactive Cyclin D-CDK4/6 module complex. Maps to SBML symbol `Mdi`.'),
        'active_cyclin_d_cdk_complex': ('Md', 'native SBML value', 'Active Cyclin D-CDK4/6 module complex. Maps to SBML symbol `Md`.'),
        'cyclin_d_cdk_p27_complex': ('Mdp27', 'native SBML value', 'Cyclin D-CDK4/6 complex bound to p27. Maps to SBML symbol `Mdp27`.'),
        'cyclin_e': ('Ce', 'native SBML value', 'Cyclin E module species. Maps to SBML symbol `Ce`.'),
        'inactive_cyclin_e_cdk2_complex': ('Mei', 'native SBML value', 'Inactive Cyclin E-CDK2 module complex. Maps to SBML symbol `Mei`.'),
        'active_cyclin_e_cdk2_complex': ('Me', 'native SBML value', 'Active Cyclin E-CDK2 module complex. Maps to SBML symbol `Me`.'),
        'skp2': ('Skp2', 'native SBML value', 'Skp2 p27-degradation regulator. Maps to SBML symbol `Skp2`.'),
        'cyclin_e_cdk2_p27_complex': ('Mep27', 'native SBML value', 'Cyclin E-CDK2 complex bound to p27. Maps to SBML symbol `Mep27`.'),
        'inactive_cyclin_e_module_regulator': ('Pei', 'native SBML value', 'Inactive regulator in the Cyclin E-CDK2 module. Maps to SBML symbol `Pei`.'),
        'active_cyclin_e_module_regulator': ('Pe', 'native SBML value', 'Active regulator in the Cyclin E-CDK2 module. Maps to SBML symbol `Pe`.'),
        'cyclin_a': ('Ca', 'native SBML value', 'Cyclin A module species. Maps to SBML symbol `Ca`.'),
        'inactive_cyclin_a_cdk2_complex': ('Mai', 'native SBML value', 'Inactive Cyclin A-CDK2 module complex. Maps to SBML symbol `Mai`.'),
        'active_cyclin_a_cdk2_complex': ('Ma', 'native SBML value', 'Active Cyclin A-CDK2 module complex. Maps to SBML symbol `Ma`.'),
        'cyclin_a_cdk2_p27_complex': ('Map27', 'native SBML value', 'Cyclin A-CDK2 complex bound to p27. Maps to SBML symbol `Map27`.'),
        'p27': ('p27', 'native SBML value', 'p27 CDK inhibitor pool. Maps to SBML symbol `p27`.'),
        'phosphorylated_p27': ('p27p', 'native SBML value', 'Phosphorylated p27 pool. Maps to SBML symbol `p27p`.'),
        'inactive_cdh1': ('Cdh1i', 'native SBML value', 'Inactive Cdh1 APC/C regulator. Maps to SBML symbol `Cdh1i`.'),
        'active_cdh1': ('Cdh1a', 'native SBML value', 'Active Cdh1 APC/C regulator. Maps to SBML symbol `Cdh1a`.'),
        'inactive_cyclin_a_module_regulator': ('Pai', 'native SBML value', 'Inactive regulator in the Cyclin A-CDK2 module. Maps to SBML symbol `Pai`.'),
        'active_cyclin_a_module_regulator': ('Pa', 'native SBML value', 'Active regulator in the Cyclin A-CDK2 module. Maps to SBML symbol `Pa`.'),
        'cyclin_b': ('Cb', 'native SBML value', 'Cyclin B module species. Maps to SBML symbol `Cb`.'),
        'inactive_cyclin_b_cdk1_complex': ('Mbi', 'native SBML value', 'Inactive Cyclin B-CDK1 module complex. Maps to SBML symbol `Mbi`.'),
        'active_cyclin_b_cdk1_complex': ('Mb', 'native SBML value', 'Active Cyclin B-CDK1 module complex. Maps to SBML symbol `Mb`.'),
        'cyclin_b_cdk1_p27_complex': ('Mbp27', 'native SBML value', 'Cyclin B-CDK1 complex bound to p27. Maps to SBML symbol `Mbp27`.'),
        'inactive_cdc20': ('Cdc20i', 'native SBML value', 'Inactive Cdc20 APC/C regulator. Maps to SBML symbol `Cdc20i`.'),
        'active_cdc20': ('Cdc20a', 'native SBML value', 'Active Cdc20 APC/C regulator. Maps to SBML symbol `Cdc20a`.'),
        'inactive_cyclin_b_module_regulator': ('Pbi', 'native SBML value', 'Inactive regulator in the Cyclin B-CDK1 module. Maps to SBML symbol `Pbi`.'),
        'active_cyclin_b_module_regulator': ('Pb', 'native SBML value', 'Active regulator in the Cyclin B-CDK1 module. Maps to SBML symbol `Pb`.'),
        'wee1': ('Wee1', 'native SBML value', 'Wee1 CDK inhibitory kinase. Maps to SBML symbol `Wee1`.'),
        'phosphorylated_wee1': ('Wee1p', 'native SBML value', 'Phosphorylated Wee1 pool. Maps to SBML symbol `Wee1p`.'),
        'dna_polymerase': ('Pol', 'native SBML value', 'DNA polymerase replication marker. Maps to SBML symbol `Pol`.'),
        'cdc45': ('Cdc45', 'native SBML value', 'Cdc45 replication-initiation marker. Maps to SBML symbol `Cdc45`.'),
        'replication_primer': ('Primer', 'native SBML value', 'DNA replication primer marker. Maps to SBML symbol `Primer`.'),
        'chk1': ('Chk1', 'native SBML value', 'Chk1 checkpoint kinase. Maps to SBML symbol `Chk1`.'),
        'atr': ('ATR', 'native SBML value', 'ATR checkpoint kinase. Maps to SBML symbol `ATR`.'),
        'ap1': ('AP1', 'native SBML value', 'AP1 growth-response transcription factor. Maps to SBML symbol `AP1`.'),
        'wee1_module_regulator': ('Mw', 'native SBML value', 'Wee1-linked regulatory model state. Maps to SBML symbol `Mw`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000730.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Gerard2009AnIntegratedMammalianCellCycleMoBiomd0000000730Model = SbmlGerard2009AnIntegratedMammalianCellCycleModel
