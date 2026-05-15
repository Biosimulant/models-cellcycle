# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ciliberto2003_Morphogenesis_Checkpoint.

Source: biomodels_ebi:BIOMD0000000297
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000297
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlCiliberto2003MorphogenesisCheckpoint(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ciliberto2003_Morphogenesis_Checkpoint."""

    _SBML_ID = 'BIOMD0000000297'
    _TITLE = 'Ciliberto2003_Morphogenesis_Checkpoint'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Trim',
        'Clb',
        'Sic',
        'PTrim',
        'PClb',
        'SBF',
        'IE',
        'Cdc20a',
        'Cdc20',
        'Cdh1',
        'Swe1',
        'Swe1M',
        'PSwe1',
        'PSwe1M',
        'Mih1a',
        'Mcm',
        'BE',
        'Cln',
        'mass',
    ]
    _SPECIES_LABELS = {
        'Trim': 'Trimer complex',
        'Clb': 'Clb2',
        'Sic': 'Sic1',
        'PTrim': 'Phosphorylated trimer complex',
        'PClb': 'Phosphorylated Clb2',
        'SBF': 'SBF transcription factor',
        'IE': 'Intermediary Enzyme',
        'Cdc20a': 'Cdc20 Activated',
        'Cdc20': 'Cdc20 APC/C activator',
        'Cdh1': 'Cdh1 APC/C activator',
        'Swe1': 'Swe1 inhibitory kinase',
        'Swe1M': 'Membrane-associated Swe1',
        'PSwe1': 'Phosphorylated Swe1',
        'PSwe1M': 'Membrane-associated phosphorylated Swe1',
        'Mih1a': 'Active Mih1 phosphatase',
        'Mcm': 'MCM replication licensing complex',
        'BE': 'Model state BE',
        'Cln': 'G1 cyclin pool',
        'mass': 'Mass',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'trimer_complex': ('Trim', 'native SBML value', 'Tracks Trimer complex. Maps to SBML symbol `Trim`.'),
        'clb2': ('Clb', 'native SBML value', 'Tracks Clb2. Maps to SBML symbol `Clb`.'),
        'sic1': ('Sic', 'native SBML value', 'Tracks Sic1. Maps to SBML symbol `Sic`.'),
        'phosphorylated_trimer_complex': ('PTrim', 'native SBML value', 'Tracks Phosphorylated trimer complex. Maps to SBML symbol `PTrim`.'),
        'phosphorylated_clb2': ('PClb', 'native SBML value', 'Tracks Phosphorylated Clb2. Maps to SBML symbol `PClb`.'),
        'sbf_transcription_factor': ('SBF', 'native SBML value', 'Tracks SBF transcription factor. Maps to SBML symbol `SBF`.'),
        'intermediary_enzyme': ('IE', 'native SBML value', 'Tracks Intermediary Enzyme. Maps to SBML symbol `IE`.'),
        'cdc20_activated': ('Cdc20a', 'native SBML value', 'Tracks Cdc20 Activated. Maps to SBML symbol `Cdc20a`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'native SBML value', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'swe1_inhibitory_kinase': ('Swe1', 'native SBML value', 'Tracks Swe1 inhibitory kinase. Maps to SBML symbol `Swe1`.'),
        'membrane_associated_swe1': ('Swe1M', 'native SBML value', 'Tracks Membrane-associated Swe1. Maps to SBML symbol `Swe1M`.'),
        'phosphorylated_swe1': ('PSwe1', 'native SBML value', 'Tracks Phosphorylated Swe1. Maps to SBML symbol `PSwe1`.'),
        'membrane_associated_phosphorylated_swe1': ('PSwe1M', 'native SBML value', 'Tracks Membrane-associated phosphorylated Swe1. Maps to SBML symbol `PSwe1M`.'),
        'active_mih1_phosphatase': ('Mih1a', 'native SBML value', 'Tracks Active Mih1 phosphatase. Maps to SBML symbol `Mih1a`.'),
        'mcm_replication_licensing_complex': ('Mcm', 'native SBML value', 'Tracks MCM replication licensing complex. Maps to SBML symbol `Mcm`.'),
        'model_state_be': ('BE', 'native SBML value', 'Tracks Model state BE. Maps to SBML symbol `BE`.'),
        'g1_cyclin_pool': ('Cln', 'native SBML value', 'Tracks G1 cyclin pool. Maps to SBML symbol `Cln`.'),
        'mass': ('mass', 'native SBML value', 'Tracks Mass. Maps to SBML symbol `mass`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000297.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ciliberto2003MorphogenesisCheckpointBiomd0000000297Model = SbmlCiliberto2003MorphogenesisCheckpoint
