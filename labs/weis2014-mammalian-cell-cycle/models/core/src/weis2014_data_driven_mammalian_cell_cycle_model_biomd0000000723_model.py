# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Weis2014 - Data driven Mammalian Cell Cycle Model.

Source: biomodels_ebi:BIOMD0000000723
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000723
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlWeis2014DataDrivenMammalianCellCycleModel(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Weis2014 - Data driven Mammalian Cell Cycle Model."""

    _SBML_ID = 'BIOMD0000000723'
    _TITLE = 'Weis2014 - Data driven Mammalian Cell Cycle Model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'ERG',
        'DRG',
        'ppRB',
        'E2F',
        'pE2F',
        'Rb',
        'E2FRB',
        'pE2FRB',
        'actCycD',
        'TriD',
        'actCycACdk1',
        'actCycACdk2',
        'actCycB',
        'actCycE',
        'cycA',
        'cycB',
        'cycE',
        'CKI',
        'Cdh1',
        'preMPF',
        'TriA',
        'APCP',
        'Cdc20A',
        'Cdc20T',
        'mass',
    ]
    _SPECIES_LABELS = {
        'ERG': 'Early response gene module',
        'DRG': 'Delayed response gene module',
        'ppRB': 'Hyperphosphorylated Rb',
        'E2F': 'E2F transcription factor',
        'pE2F': 'Phosphorylated E2F',
        'Rb': 'Rb tumor suppressor',
        'E2FRB': 'E2F-Rb complex',
        'pE2FRB': 'P E2FRB',
        'actCycD': 'Act Cyclin D',
        'TriD': 'Tri D',
        'actCycACdk1': 'Act Cyclin ACdk1',
        'actCycACdk2': 'Act Cyclin ACdk2',
        'actCycB': 'Act Cyclin B',
        'actCycE': 'Act Cyclin E',
        'cycA': 'Cyclin A',
        'cycB': 'Cyclin B',
        'cycE': 'Cyclin E',
        'CKI': 'Cyclin-dependent kinase inhibitor',
        'Cdh1': 'Cdh1 APC/C activator',
        'preMPF': 'Pre MPF',
        'TriA': 'Tri A',
        'APCP': 'Phosphorylated APC/C/C',
        'Cdc20A': 'Active Cdc20',
        'Cdc20T': 'Total Cdc20 APC/C activator',
        'mass': 'Mass',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'early_response_gene_module': ('ERG', 'native SBML value', 'Tracks Early response gene module. Maps to SBML symbol `ERG`.'),
        'delayed_response_gene_module': ('DRG', 'native SBML value', 'Tracks Delayed response gene module. Maps to SBML symbol `DRG`.'),
        'hyperphosphorylated_rb': ('ppRB', 'native SBML value', 'Tracks Hyperphosphorylated Rb. Maps to SBML symbol `ppRB`.'),
        'e2f_transcription_factor': ('E2F', 'native SBML value', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'phosphorylated_e2f': ('pE2F', 'native SBML value', 'Tracks Phosphorylated E2F. Maps to SBML symbol `pE2F`.'),
        'rb_tumor_suppressor': ('Rb', 'native SBML value', 'Tracks Rb tumor suppressor. Maps to SBML symbol `Rb`.'),
        'e2f_rb_complex': ('E2FRB', 'native SBML value', 'Tracks E2F-Rb complex. Maps to SBML symbol `E2FRB`.'),
        'p_e2frb': ('pE2FRB', 'native SBML value', 'Tracks P E2FRB. Maps to SBML symbol `pE2FRB`.'),
        'act_cyclin_d': ('actCycD', 'native SBML value', 'Tracks Act Cyclin D. Maps to SBML symbol `actCycD`.'),
        'tri_d': ('TriD', 'native SBML value', 'Tracks Tri D. Maps to SBML symbol `TriD`.'),
        'act_cyclin_acdk1': ('actCycACdk1', 'native SBML value', 'Tracks Act Cyclin ACdk1. Maps to SBML symbol `actCycACdk1`.'),
        'act_cyclin_acdk2': ('actCycACdk2', 'native SBML value', 'Tracks Act Cyclin ACdk2. Maps to SBML symbol `actCycACdk2`.'),
        'act_cyclin_b': ('actCycB', 'native SBML value', 'Tracks Act Cyclin B. Maps to SBML symbol `actCycB`.'),
        'act_cyclin_e': ('actCycE', 'native SBML value', 'Tracks Act Cyclin E. Maps to SBML symbol `actCycE`.'),
        'cyclin_a': ('cycA', 'native SBML value', 'Tracks Cyclin A. Maps to SBML symbol `cycA`.'),
        'cyclin_b': ('cycB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `cycB`.'),
        'cyclin_e': ('cycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `cycE`.'),
        'cyclin_dependent_kinase_inhibitor': ('CKI', 'native SBML value', 'Tracks Cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKI`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'pre_mpf': ('preMPF', 'native SBML value', 'Tracks Pre MPF. Maps to SBML symbol `preMPF`.'),
        'tri_a': ('TriA', 'native SBML value', 'Tracks Tri A. Maps to SBML symbol `TriA`.'),
        'phosphorylated_apc_c_c': ('APCP', 'native SBML value', 'Tracks Phosphorylated APC/C/C. Maps to SBML symbol `APCP`.'),
        'active_cdc20': ('Cdc20A', 'native SBML value', 'Tracks Active Cdc20. Maps to SBML symbol `Cdc20A`.'),
        'total_cdc20_apc_c_activator': ('Cdc20T', 'native SBML value', 'Tracks Total Cdc20 APC/C activator. Maps to SBML symbol `Cdc20T`.'),
        'mass': ('mass', 'native SBML value', 'Tracks Mass. Maps to SBML symbol `mass`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000723.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Weis2014DataDrivenMammalianCellCycleModelBiomd0000000723Model = SbmlWeis2014DataDrivenMammalianCellCycleModel
