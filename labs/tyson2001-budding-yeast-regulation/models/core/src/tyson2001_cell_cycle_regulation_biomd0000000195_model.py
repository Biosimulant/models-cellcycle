# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Tyson2001_Cell_Cycle_Regulation.

Source: biomodels_ebi:BIOMD0000000195
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000195
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlTyson2001CellCycleRegulation(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Tyson2001_Cell_Cycle_Regulation."""

    _SBML_ID = 'BIOMD0000000195'
    _TITLE = 'Tyson2001_Cell_Cycle_Regulation'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CycBt',
        'Cdc20a',
        'Cdh1',
        'm',
        'Cdc20t',
        'IEP',
        'CKIt',
        'SK',
        'CycB',
        'Trimer',
        'Mad',
    ]
    _SPECIES_LABELS = {
        'CycBt': 'Cyclin Bt',
        'Cdc20a': 'Active Cdc20',
        'Cdh1': 'Cdh1 APC/C activator',
        'm': 'Model state M (m)',
        'Cdc20t': 'Total Cdc20 APC/C activator',
        'IEP': 'Phosphorylated IE',
        'CKIt': 'Total cyclin-dependent kinase inhibitor',
        'SK': 'Model state SK',
        'CycB': 'Cyclin B',
        'Trimer': 'Trimer complex',
        'Mad': 'Mad spindle checkpoint signal',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin_bt': ('CycBt', 'native SBML value', 'Tracks Cyclin Bt. Maps to SBML symbol `CycBt`.'),
        'active_cdc20': ('Cdc20a', 'native SBML value', 'Tracks Active Cdc20. Maps to SBML symbol `Cdc20a`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'model_state_m_m': ('m', 'native SBML value', 'Tracks Model state M (m). Maps to SBML symbol `m`.'),
        'total_cdc20_apc_c_activator': ('Cdc20t', 'native SBML value', 'Tracks Total Cdc20 APC/C activator. Maps to SBML symbol `Cdc20t`.'),
        'phosphorylated_ie': ('IEP', 'native SBML value', 'Tracks Phosphorylated IE. Maps to SBML symbol `IEP`.'),
        'total_cyclin_dependent_kinase_inhibitor': ('CKIt', 'native SBML value', 'Tracks Total cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKIt`.'),
        'model_state_sk': ('SK', 'native SBML value', 'Tracks Model state SK. Maps to SBML symbol `SK`.'),
        'cyclin_b': ('CycB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `CycB`.'),
        'trimer_complex': ('Trimer', 'native SBML value', 'Tracks Trimer complex. Maps to SBML symbol `Trimer`.'),
        'mad_spindle_checkpoint_signal': ('Mad', 'native SBML value', 'Tracks Mad spindle checkpoint signal. Maps to SBML symbol `Mad`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000195.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Tyson2001CellCycleRegulationBiomd0000000195Model = SbmlTyson2001CellCycleRegulation
