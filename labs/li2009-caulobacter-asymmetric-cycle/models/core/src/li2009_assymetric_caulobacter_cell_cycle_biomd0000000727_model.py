# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Li2009- Assymetric Caulobacter cell cycle.

Source: biomodels_ebi:BIOMD0000000727
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000727
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlLi2009AssymetricCaulobacterCellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Li2009- Assymetric Caulobacter cell cycle."""

    _SBML_ID = 'BIOMD0000000727'
    _TITLE = 'Li2009- Assymetric Caulobacter cell cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'DnaA',
        'GcrA',
        'CtrA',
        'CtrA_P',
        'DivK',
        'DivK_P',
        'I',
        'CcrM',
        'hcori',
        'hctrA',
        'hccrM',
        'hftsZ',
        'Ini',
        'DNA',
        'Count',
        'PodJL',
        'PerP',
        'DivJ',
        'CckA_P',
        'CpdR',
        'RcdA',
        'ParAADP',
        'FtsZ',
        'Zring',
        'CckA_tot',
        'CpdR_tot',
        'ParA_tot',
        'Elong',
        'Z',
        'FtsQ',
    ]
    _SPECIES_LABELS = {
        'DnaA': 'DnaA replication initiator',
        'GcrA': 'GcrA transcriptional regulator',
        'CtrA': 'CtrA cell-cycle regulator',
        'CtrA_P': 'Phosphorylated CtrA',
        'DivK': 'DivK polarity regulator',
        'DivK_P': 'Phosphorylated DivK',
        'I': 'Model state I',
        'CcrM': 'Ccr Model state M',
        'hcori': 'Hcori',
        'hctrA': 'Hctr A',
        'hccrM': 'Hccr Model state M',
        'hftsZ': 'Hfts Model state Z',
        'Ini': 'Replication initiation state',
        'DNA': 'DNA replication state',
        'Count': 'Division event counter',
        'PodJL': 'Pod JL',
        'PerP': 'Phosphorylated Per',
        'DivJ': 'Div J',
        'CckA_P': 'Phosphorylated Cck A',
        'CpdR': 'Cpd Model state R',
        'RcdA': 'Rcd A',
        'ParAADP': 'Phosphorylated Par AAD',
        'FtsZ': 'Fts Model state Z',
        'Zring': 'Z-ring',
        'CckA_tot': 'Cck Active Tot',
        'CpdR_tot': 'Cpd Model state R Tot',
        'ParA_tot': 'Par Active Tot',
        'Elong': 'Cell elongation state',
        'Z': 'Model state Z (Z)',
        'FtsQ': 'Fts Q',
    }
    _PARAMETER_INPUTS = {
        'ks_dna_a1': ('ks_DnaA1', 0.0031, 'dimensionless', 'Controls Ks,DNA A1. Maps to SBML symbol `ks_DnaA1`.'),
        'ks_dna_a2': ('ks_DnaA2', 0.0022, 'dimensionless', 'Controls Ks,DNA A2. Maps to SBML symbol `ks_DnaA2`.'),
        'kd_dna_a': ('kd_DnaA', 0.007, 'dimensionless', 'Controls Kd,DnaA. Maps to SBML symbol `kd_DnaA`.'),
        'ji_dna_active_gcr_a': ('JiDnaA_GcrA', 0.6, 'dimensionless', 'Controls Ji DNA Active GcrA. Maps to SBML symbol `JiDnaA_GcrA`.'),
        'phosphorylated_ja_dna_ctr_a': ('Ja_Dna_CtrA_P', 0.3, 'dimensionless', 'Controls Phosphorylated Ja DNA CtrA. Maps to SBML symbol `Ja_Dna_CtrA_P`.'),
        'ja_fts_q_dna': ('Ja_FtsQ_DNA', 0.05, 'dimensionless', 'Controls Ja,Fts Q,DNA. Maps to SBML symbol `Ja_FtsQ_DNA`.'),
    }
    _HEADLINE_OUTPUTS = {
        'dna_a_replication_initiator': ('DnaA', 'native SBML value', 'Tracks DnaA replication initiator. Maps to SBML symbol `DnaA`.'),
        'gcr_a_transcriptional_regulator': ('GcrA', 'native SBML value', 'Tracks GcrA transcriptional regulator. Maps to SBML symbol `GcrA`.'),
        'ctr_a_cell_cycle_regulator': ('CtrA', 'native SBML value', 'Tracks CtrA cell-cycle regulator. Maps to SBML symbol `CtrA`.'),
        'phosphorylated_ctr_a': ('CtrA_P', 'native SBML value', 'Tracks Phosphorylated CtrA. Maps to SBML symbol `CtrA_P`.'),
        'div_k_polarity_regulator': ('DivK', 'native SBML value', 'Tracks DivK polarity regulator. Maps to SBML symbol `DivK`.'),
        'phosphorylated_div_k': ('DivK_P', 'native SBML value', 'Tracks Phosphorylated DivK. Maps to SBML symbol `DivK_P`.'),
        'model_state_i': ('I', 'native SBML value', 'Tracks Model state I. Maps to SBML symbol `I`.'),
        'ccr_model_state_m': ('CcrM', 'native SBML value', 'Tracks Ccr Model state M. Maps to SBML symbol `CcrM`.'),
        'hcori': ('hcori', 'native SBML value', 'Tracks Hcori. Maps to SBML symbol `hcori`.'),
        'hctr_a': ('hctrA', 'native SBML value', 'Tracks Hctr A. Maps to SBML symbol `hctrA`.'),
        'hccr_model_state_m': ('hccrM', 'native SBML value', 'Tracks Hccr Model state M. Maps to SBML symbol `hccrM`.'),
        'hfts_model_state_z': ('hftsZ', 'native SBML value', 'Tracks Hfts Model state Z. Maps to SBML symbol `hftsZ`.'),
        'replication_initiation_state': ('Ini', 'native SBML value', 'Tracks Replication initiation state. Maps to SBML symbol `Ini`.'),
        'dna_replication_state': ('DNA', 'native SBML value', 'Tracks DNA replication state. Maps to SBML symbol `DNA`.'),
        'division_event_counter': ('Count', 'native SBML value', 'Tracks Division event counter. Maps to SBML symbol `Count`.'),
        'pod_jl': ('PodJL', 'native SBML value', 'Tracks Pod JL. Maps to SBML symbol `PodJL`.'),
        'phosphorylated_per': ('PerP', 'native SBML value', 'Tracks Phosphorylated Per. Maps to SBML symbol `PerP`.'),
        'div_j': ('DivJ', 'native SBML value', 'Tracks Div J. Maps to SBML symbol `DivJ`.'),
        'phosphorylated_cck_a': ('CckA_P', 'native SBML value', 'Tracks Phosphorylated Cck A. Maps to SBML symbol `CckA_P`.'),
        'cpd_model_state_r': ('CpdR', 'native SBML value', 'Tracks Cpd Model state R. Maps to SBML symbol `CpdR`.'),
        'rcd_a': ('RcdA', 'native SBML value', 'Tracks Rcd A. Maps to SBML symbol `RcdA`.'),
        'phosphorylated_par_aad': ('ParAADP', 'native SBML value', 'Tracks Phosphorylated Par AAD. Maps to SBML symbol `ParAADP`.'),
        'fts_model_state_z': ('FtsZ', 'native SBML value', 'Tracks Fts Model state Z. Maps to SBML symbol `FtsZ`.'),
        'z_ring': ('Zring', 'native SBML value', 'Tracks Z-ring. Maps to SBML symbol `Zring`.'),
        'cck_active_tot': ('CckA_tot', 'native SBML value', 'Tracks Cck Active Tot. Maps to SBML symbol `CckA_tot`.'),
        'cpd_model_state_r_tot': ('CpdR_tot', 'native SBML value', 'Tracks Cpd Model state R Tot. Maps to SBML symbol `CpdR_tot`.'),
        'par_active_tot': ('ParA_tot', 'native SBML value', 'Tracks Par Active Tot. Maps to SBML symbol `ParA_tot`.'),
        'cell_elongation_state': ('Elong', 'native SBML value', 'Tracks Cell elongation state. Maps to SBML symbol `Elong`.'),
        'model_state_z_z': ('Z', 'native SBML value', 'Tracks Model state Z (Z). Maps to SBML symbol `Z`.'),
        'fts_q': ('FtsQ', 'native SBML value', 'Tracks Fts Q. Maps to SBML symbol `FtsQ`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000727.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Li2009AssymetricCaulobacterCellCycleBiomd0000000727Model = SbmlLi2009AssymetricCaulobacterCellCycle
