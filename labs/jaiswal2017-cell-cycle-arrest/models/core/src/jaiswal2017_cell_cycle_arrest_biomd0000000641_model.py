# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Jaiswal2017 - Cell cycle arrest.

Source: biomodels_ebi:BIOMD0000000641
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000641
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlJaiswal2017CellCycleArrest(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Jaiswal2017 - Cell cycle arrest."""

    _SBML_ID = 'BIOMD0000000641'
    _TITLE = 'Jaiswal2017 - Cell cycle arrest'
    _TIME_UNIT = 'time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'Timeract',
        'CellCact',
        'Effectoract',
        'HR',
        'NHEJ',
        'CellCina',
        'Damage',
        'Effectorina',
        'Timerinact',
    ]
    _SPECIES_LABELS = {
        'Timeract': 'Active timer state',
        'CellCact': 'Cell Cact',
        'Effectoract': 'Active checkpoint effector',
        'HR': 'Model state HR',
        'NHEJ': 'Non-homologous end joining repair state',
        'CellCina': 'Cell Cina',
        'Damage': 'DNA Damage',
        'Effectorina': 'Inactive checkpoint effector',
        'Timerinact': 'Inactive timer state',
    }
    _PARAMETER_INPUTS = {
        'cell_cycletot': ('CellCycletot', 10.0, 'substance', 'Controls Cell Cycletot. Maps to SBML symbol `CellCycletot`.'),
        'effectortot': ('Effectortot', 10.0, 'substance', 'Controls Effectortot. Maps to SBML symbol `Effectortot`.'),
        'timertot': ('Timertot', 10.0, 'substance', 'Controls Timertot. Maps to SBML symbol `Timertot`.'),
    }
    _HEADLINE_OUTPUTS = {
        'active_timer_state': ('Timeract', 'substance', 'Tracks Active timer state. Maps to SBML symbol `Timeract`.'),
        'cell_cact': ('CellCact', 'substance', 'Tracks Cell Cact. Maps to SBML symbol `CellCact`.'),
        'active_checkpoint_effector': ('Effectoract', 'substance', 'Tracks Active checkpoint effector. Maps to SBML symbol `Effectoract`.'),
        'model_state_hr': ('HR', 'substance', 'Tracks Model state HR. Maps to SBML symbol `HR`.'),
        'non_homologous_end_joining_repair_state': ('NHEJ', 'substance', 'Tracks Non-homologous end joining repair state. Maps to SBML symbol `NHEJ`.'),
        'cell_cina': ('CellCina', 'substance', 'Tracks Cell Cina. Maps to SBML symbol `CellCina`.'),
        'dna_damage': ('Damage', 'substance', 'Tracks DNA Damage. Maps to SBML symbol `Damage`.'),
        'inactive_checkpoint_effector': ('Effectorina', 'substance', 'Tracks Inactive checkpoint effector. Maps to SBML symbol `Effectorina`.'),
        'inactive_timer_state': ('Timerinact', 'substance', 'Tracks Inactive timer state. Maps to SBML symbol `Timerinact`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000641.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Jaiswal2017CellCycleArrestBiomd0000000641Model = SbmlJaiswal2017CellCycleArrest
