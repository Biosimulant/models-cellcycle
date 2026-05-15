# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Li2008 - Caulobacter Cell Cycle.

Source: biomodels_ebi:BIOMD0000000718
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000718
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlLi2008CaulobacterCellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Li2008 - Caulobacter Cell Cycle."""

    _SBML_ID = 'BIOMD0000000718'
    _TITLE = 'Li2008 - Caulobacter Cell Cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CtrA',
        'GcrA',
        'DnaA',
        'Fts',
        'Zring',
        'DivK',
        'DivK_P',
        'I',
        'CcrM',
        'hcori',
        'hctrA',
        'hccrM',
        'hfts',
        'Ini',
        'Elong',
        'DNA',
    ]
    _SPECIES_LABELS = {
        'CtrA': 'CtrA cell-cycle regulator',
        'GcrA': 'GcrA transcriptional regulator',
        'DnaA': 'DnaA replication initiator',
        'Fts': 'FtsZ division marker',
        'Zring': 'Z-ring',
        'DivK': 'DivK polarity regulator',
        'DivK_P': 'Phosphorylated DivK',
        'I': 'Model state I',
        'CcrM': 'Ccr Model state M',
        'hcori': 'Hcori',
        'hctrA': 'Hctr A',
        'hccrM': 'Hccr Model state M',
        'hfts': 'Hfts',
        'Ini': 'Replication initiation state',
        'Elong': 'Cell elongation state',
        'DNA': 'DNA replication state',
    }
    _PARAMETER_INPUTS = {
        'ks_dna_a': ('ks_DnaA', 0.0165, 'unit_0', 'Controls Ks,DnaA. Maps to SBML symbol `ks_DnaA`.'),
        'kd_dna_a': ('kd_DnaA', 0.007, 'unit_0', 'Controls Kd,DnaA. Maps to SBML symbol `kd_DnaA`.'),
        'ja_dna_active_ctr_a': ('Ja_DnaA_CtrA', 0.3, 'unit_1', 'Controls Ja,DNA Active CtrA. Maps to SBML symbol `Ja_DnaA_CtrA`.'),
        'theta_dna_a': ('thetaDnaA', 0.6, 'unit_1', 'Controls Theta DnaA. Maps to SBML symbol `thetaDnaA`.'),
        'ji_dna_active_gcr_a': ('Ji_DnaA_GcrA', 0.5, 'unit_1', 'Controls Ji,DNA Active GcrA. Maps to SBML symbol `Ji_DnaA_GcrA`.'),
    }
    _HEADLINE_OUTPUTS = {
        'ctr_a_cell_cycle_regulator': ('CtrA', 'native SBML value', 'Tracks CtrA cell-cycle regulator. Maps to SBML symbol `CtrA`.'),
        'gcr_a_transcriptional_regulator': ('GcrA', 'native SBML value', 'Tracks GcrA transcriptional regulator. Maps to SBML symbol `GcrA`.'),
        'dna_a_replication_initiator': ('DnaA', 'native SBML value', 'Tracks DnaA replication initiator. Maps to SBML symbol `DnaA`.'),
        'fts_z_division_marker': ('Fts', 'native SBML value', 'Tracks FtsZ division marker. Maps to SBML symbol `Fts`.'),
        'z_ring': ('Zring', 'native SBML value', 'Tracks Z-ring. Maps to SBML symbol `Zring`.'),
        'div_k_polarity_regulator': ('DivK', 'native SBML value', 'Tracks DivK polarity regulator. Maps to SBML symbol `DivK`.'),
        'phosphorylated_div_k': ('DivK_P', 'native SBML value', 'Tracks Phosphorylated DivK. Maps to SBML symbol `DivK_P`.'),
        'model_state_i': ('I', 'native SBML value', 'Tracks Model state I. Maps to SBML symbol `I`.'),
        'ccr_model_state_m': ('CcrM', 'native SBML value', 'Tracks Ccr Model state M. Maps to SBML symbol `CcrM`.'),
        'hcori': ('hcori', 'native SBML value', 'Tracks Hcori. Maps to SBML symbol `hcori`.'),
        'hctr_a': ('hctrA', 'native SBML value', 'Tracks Hctr A. Maps to SBML symbol `hctrA`.'),
        'hccr_model_state_m': ('hccrM', 'native SBML value', 'Tracks Hccr Model state M. Maps to SBML symbol `hccrM`.'),
        'hfts': ('hfts', 'native SBML value', 'Tracks Hfts. Maps to SBML symbol `hfts`.'),
        'replication_initiation_state': ('Ini', 'native SBML value', 'Tracks Replication initiation state. Maps to SBML symbol `Ini`.'),
        'cell_elongation_state': ('Elong', 'native SBML value', 'Tracks Cell elongation state. Maps to SBML symbol `Elong`.'),
        'dna_replication_state': ('DNA', 'native SBML value', 'Tracks DNA replication state. Maps to SBML symbol `DNA`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000718.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Li2008CaulobacterCellCycleBiomd0000000718Model = SbmlLi2008CaulobacterCellCycle
