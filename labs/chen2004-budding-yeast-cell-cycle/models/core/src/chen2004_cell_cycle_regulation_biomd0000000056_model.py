# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Chen2004 - Cell Cycle Regulation.

Source: biomodels_ebi:BIOMD0000000056
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000056
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlChen2004CellCycleRegulation(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Chen2004 - Cell Cycle Regulation."""

    _SBML_ID = 'BIOMD0000000056'
    _TITLE = 'Chen2004 - Cell Cycle Regulation'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'BUB2',
        'BUD',
        'C2',
        'C2P',
        'C5',
        'C5P',
        'CDC14',
        'CDC15',
        'CDC20',
        'CDC20i',
        'CDC6',
        'CDC6P',
        'CDH1',
        'CDH1i',
        'CLB2',
        'CLB5',
        'CLN2',
        'ESP1',
        'F2',
        'F2P',
        'F5',
        'F5P',
        'IEP',
        'LTE1',
        'MAD2',
        'MASS',
        'NET1',
        'NET1P',
        'ORI',
        'PDS1',
        'PPX',
        'RENT',
        'RENTP',
        'SIC1',
        'SIC1P',
        'SPN',
        'SWI5',
        'SWI5P',
        'TEM1GTP',
        'BCK2',
        'CDC14T',
        'CDC6T',
        'CKIT',
        'CLB2T',
        'CLB5T',
        'CLN3',
        'MCM1',
        'NET1T',
        'SBF',
        'SIC1T',
    ]
    _SPECIES_LABELS = {
        'BUB2': 'Bub2',
        'BUD': 'Budding index',
        'C2': 'Model state C2 (C2)',
        'C2P': 'Phosphorylated Model state C2',
        'C5': 'Model state C5 (C5)',
        'C5P': 'Phosphorylated Model state C5',
        'CDC14': 'Cdc14 phosphatase',
        'CDC15': 'Cdc15 mitotic exit kinase',
        'CDC20': 'Cdc20',
        'CDC20i': 'Inactive Cdc20',
        'CDC6': 'Cdc6 replication licensing factor',
        'CDC6P': 'Phosphorylated CDC6',
        'CDH1': 'Cdh1 APC/C activator',
        'CDH1i': 'Inactive Cdh1',
        'CLB2': 'Clb2 mitotic cyclin',
        'CLB5': 'Clb5 S-phase cyclin',
        'CLN2': 'Cln2 G1 cyclin',
        'ESP1': 'Esp1 separase',
        'F2': 'Model state F2',
        'F2P': 'Phosphorylated F2',
        'F5': 'Model state F5',
        'F5P': 'Phosphorylated F5',
        'IEP': 'Phosphorylated IE',
        'LTE1': 'Lte1 mitotic exit regulator',
        'MAD2': 'Mad2 spindle checkpoint protein',
        'MASS': 'Cell mass',
        'NET1': 'Net1 nucleolar Cdc14 anchor',
        'NET1P': 'Phosphorylated NET1',
        'ORI': 'Replication origin state',
        'PDS1': 'Pds1 securin',
        'PPX': 'PPX phosphatase',
        'RENT': 'RENT Cdc14 sequestration complex',
        'RENTP': 'Phosphorylated RENT',
        'SIC1': 'Sic1',
        'SIC1P': 'Phosphorylated Sic1',
        'SPN': 'Spindle state',
        'SWI5': 'Swi5 transcription factor',
        'SWI5P': 'Phosphorylated SWI5',
        'TEM1GTP': 'Phosphorylated TEM1GT',
        'BCK2': 'Bck2 G1 regulator',
        'CDC14T': 'Total Cdc14 phosphatase',
        'CDC6T': 'Total Cdc6 replication licensing factor',
        'CKIT': 'Total cyclin-dependent kinase inhibitor',
        'CLB2T': 'Total Clb2 mitotic cyclin',
        'CLB5T': 'Total Clb5 S-phase cyclin',
        'CLN3': 'Cln3 Start cyclin',
        'MCM1': 'Mcm1',
        'NET1T': 'Total Net1 nucleolar Cdc14 anchor',
        'SBF': 'SBF transcription factor',
        'SIC1T': 'Total Sic1 CDK inhibitor',
    }
    _PARAMETER_INPUTS = {
        'cdc15i': ('CDC15i', 0.34346699999999997, 'native SBML value', 'Controls CDC15i. Maps to SBML symbol `CDC15i`.'),
        'model_state_ie': ('IE', 0.8985, 'native SBML value', 'Controls Model state IE. Maps to SBML symbol `IE`.'),
        'model_state_pe': ('PE', 0.6986870000000001, 'native SBML value', 'Controls Model state PE. Maps to SBML symbol `PE`.'),
        'phosphorylated_tem1gd': ('TEM1GDP', 0.09999999999999998, 'native SBML value', 'Controls Phosphorylated TEM1GD. Maps to SBML symbol `TEM1GDP`.'),
    }
    _HEADLINE_OUTPUTS = {
        'bub2': ('BUB2', 'native SBML value', 'Tracks Bub2. Maps to SBML symbol `BUB2`.'),
        'budding_index': ('BUD', 'native SBML value', 'Tracks Budding index. Maps to SBML symbol `BUD`.'),
        'model_state_c2_c2': ('C2', 'native SBML value', 'Tracks Model state C2 (C2). Maps to SBML symbol `C2`.'),
        'phosphorylated_model_state_c2': ('C2P', 'native SBML value', 'Tracks Phosphorylated Model state C2. Maps to SBML symbol `C2P`.'),
        'model_state_c5_c5': ('C5', 'native SBML value', 'Tracks Model state C5 (C5). Maps to SBML symbol `C5`.'),
        'phosphorylated_model_state_c5': ('C5P', 'native SBML value', 'Tracks Phosphorylated Model state C5. Maps to SBML symbol `C5P`.'),
        'cdc14_phosphatase': ('CDC14', 'native SBML value', 'Tracks Cdc14 phosphatase. Maps to SBML symbol `CDC14`.'),
        'cdc15_mitotic_exit_kinase': ('CDC15', 'native SBML value', 'Tracks Cdc15 mitotic exit kinase. Maps to SBML symbol `CDC15`.'),
        'cdc20': ('CDC20', 'native SBML value', 'Tracks Cdc20. Maps to SBML symbol `CDC20`.'),
        'inactive_cdc20': ('CDC20i', 'native SBML value', 'Tracks Inactive Cdc20. Maps to SBML symbol `CDC20i`.'),
        'cdc6_replication_licensing_factor': ('CDC6', 'native SBML value', 'Tracks Cdc6 replication licensing factor. Maps to SBML symbol `CDC6`.'),
        'phosphorylated_cdc6': ('CDC6P', 'native SBML value', 'Tracks Phosphorylated CDC6. Maps to SBML symbol `CDC6P`.'),
        'cdh1_apc_c_activator': ('CDH1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `CDH1`.'),
        'inactive_cdh1': ('CDH1i', 'native SBML value', 'Tracks Inactive Cdh1. Maps to SBML symbol `CDH1i`.'),
        'clb2_mitotic_cyclin': ('CLB2', 'native SBML value', 'Tracks Clb2 mitotic cyclin. Maps to SBML symbol `CLB2`.'),
        'clb5_s_phase_cyclin': ('CLB5', 'native SBML value', 'Tracks Clb5 S-phase cyclin. Maps to SBML symbol `CLB5`.'),
        'cln2_g1_cyclin': ('CLN2', 'native SBML value', 'Tracks Cln2 G1 cyclin. Maps to SBML symbol `CLN2`.'),
        'esp1_separase': ('ESP1', 'native SBML value', 'Tracks Esp1 separase. Maps to SBML symbol `ESP1`.'),
        'model_state_f2': ('F2', 'native SBML value', 'Tracks Model state F2. Maps to SBML symbol `F2`.'),
        'phosphorylated_f2': ('F2P', 'native SBML value', 'Tracks Phosphorylated F2. Maps to SBML symbol `F2P`.'),
        'model_state_f5': ('F5', 'native SBML value', 'Tracks Model state F5. Maps to SBML symbol `F5`.'),
        'phosphorylated_f5': ('F5P', 'native SBML value', 'Tracks Phosphorylated F5. Maps to SBML symbol `F5P`.'),
        'phosphorylated_ie': ('IEP', 'native SBML value', 'Tracks Phosphorylated IE. Maps to SBML symbol `IEP`.'),
        'lte1_mitotic_exit_regulator': ('LTE1', 'native SBML value', 'Tracks Lte1 mitotic exit regulator. Maps to SBML symbol `LTE1`.'),
        'mad2_spindle_checkpoint_protein': ('MAD2', 'native SBML value', 'Tracks Mad2 spindle checkpoint protein. Maps to SBML symbol `MAD2`.'),
        'cell_mass': ('MASS', 'native SBML value', 'Tracks Cell mass. Maps to SBML symbol `MASS`.'),
        'net1_nucleolar_cdc14_anchor': ('NET1', 'native SBML value', 'Tracks Net1 nucleolar Cdc14 anchor. Maps to SBML symbol `NET1`.'),
        'phosphorylated_net1': ('NET1P', 'native SBML value', 'Tracks Phosphorylated NET1. Maps to SBML symbol `NET1P`.'),
        'replication_origin_state': ('ORI', 'native SBML value', 'Tracks Replication origin state. Maps to SBML symbol `ORI`.'),
        'pds1_securin': ('PDS1', 'native SBML value', 'Tracks Pds1 securin. Maps to SBML symbol `PDS1`.'),
        'ppx_phosphatase': ('PPX', 'native SBML value', 'Tracks PPX phosphatase. Maps to SBML symbol `PPX`.'),
        'rent_cdc14_sequestration_complex': ('RENT', 'native SBML value', 'Tracks RENT Cdc14 sequestration complex. Maps to SBML symbol `RENT`.'),
        'phosphorylated_rent': ('RENTP', 'native SBML value', 'Tracks Phosphorylated RENT. Maps to SBML symbol `RENTP`.'),
        'sic1': ('SIC1', 'native SBML value', 'Tracks Sic1. Maps to SBML symbol `SIC1`.'),
        'phosphorylated_sic1': ('SIC1P', 'native SBML value', 'Tracks Phosphorylated Sic1. Maps to SBML symbol `SIC1P`.'),
        'spindle_state': ('SPN', 'native SBML value', 'Tracks Spindle state. Maps to SBML symbol `SPN`.'),
        'swi5_transcription_factor': ('SWI5', 'native SBML value', 'Tracks Swi5 transcription factor. Maps to SBML symbol `SWI5`.'),
        'phosphorylated_swi5': ('SWI5P', 'native SBML value', 'Tracks Phosphorylated SWI5. Maps to SBML symbol `SWI5P`.'),
        'phosphorylated_tem1gt': ('TEM1GTP', 'native SBML value', 'Tracks Phosphorylated TEM1GT. Maps to SBML symbol `TEM1GTP`.'),
        'bck2_g1_regulator': ('BCK2', 'native SBML value', 'Tracks Bck2 G1 regulator. Maps to SBML symbol `BCK2`.'),
        'total_cdc14_phosphatase': ('CDC14T', 'native SBML value', 'Tracks Total Cdc14 phosphatase. Maps to SBML symbol `CDC14T`.'),
        'total_cdc6_replication_licensing_factor': ('CDC6T', 'native SBML value', 'Tracks Total Cdc6 replication licensing factor. Maps to SBML symbol `CDC6T`.'),
        'total_cyclin_dependent_kinase_inhibitor': ('CKIT', 'native SBML value', 'Tracks Total cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKIT`.'),
        'total_clb2_mitotic_cyclin': ('CLB2T', 'native SBML value', 'Tracks Total Clb2 mitotic cyclin. Maps to SBML symbol `CLB2T`.'),
        'total_clb5_s_phase_cyclin': ('CLB5T', 'native SBML value', 'Tracks Total Clb5 S-phase cyclin. Maps to SBML symbol `CLB5T`.'),
        'cln3_start_cyclin': ('CLN3', 'native SBML value', 'Tracks Cln3 Start cyclin. Maps to SBML symbol `CLN3`.'),
        'mcm1': ('MCM1', 'native SBML value', 'Tracks Mcm1. Maps to SBML symbol `MCM1`.'),
        'total_net1_nucleolar_cdc14_anchor': ('NET1T', 'native SBML value', 'Tracks Total Net1 nucleolar Cdc14 anchor. Maps to SBML symbol `NET1T`.'),
        'sbf_transcription_factor': ('SBF', 'native SBML value', 'Tracks SBF transcription factor. Maps to SBML symbol `SBF`.'),
        'total_sic1_cdk_inhibitor': ('SIC1T', 'native SBML value', 'Tracks Total Sic1 CDK inhibitor. Maps to SBML symbol `SIC1T`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000056.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Chen2004CellCycleRegulationBiomd0000000056Model = SbmlChen2004CellCycleRegulation
