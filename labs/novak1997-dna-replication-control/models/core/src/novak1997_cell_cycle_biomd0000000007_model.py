# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Novak1997 - Cell Cycle.

Source: biomodels_ebi:BIOMD0000000007
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000007
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNovak1997CellCycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Novak1997 - Cell Cycle."""

    _SBML_ID = 'BIOMD0000000007'
    _TITLE = 'Novak1997 - Cell Cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'UbE',
        'UbE2',
        'Wee1',
        'Cdc25',
        'G2K',
        'R',
        'G1K',
        'IE',
        'PG2',
        'G1R',
        'G2R',
        'PG2R',
        'SPF',
        'MPF',
        'Rum1Total',
        'Cdc13Total',
        'Cig2Total',
    ]
    _SPECIES_LABELS = {
        'UbE': 'Ubiquitin Protease1',
        'UbE2': 'Ubiquitin Protease2',
        'Wee1': 'Wee1 inhibitory kinase',
        'Cdc25': 'Cdc25 activating phosphatase',
        'G2K': 'Cdc13 Cdc2',
        'R': 'Free Rum1',
        'G1K': 'Cig2 Cdc2',
        'IE': 'Intermediary Enzyme',
        'PG2': 'Cdc13 P Cdc2',
        'G1R': 'Cig2 Cdc2 Rum1',
        'G2R': 'Cdc13 Cdc2 Rum1',
        'PG2R': 'Cdc13 P Cdc2 Rum1',
        'SPF': 'S Phase Promoting Factor',
        'MPF': 'Maturation-promoting factor',
        'Rum1Total': 'Total Rum1',
        'Cdc13Total': 'Total Cdc13',
        'Cig2Total': 'Total Cig2',
    }
    _PARAMETER_INPUTS = {
        'bound_intermediary_enzyme': ('IEB', 1.0, 'native SBML value', 'Controls Bound Intermediary Enzyme. Maps to SBML symbol `IEB`.'),
        'bound_ubiquitin_protease1': ('UbEB', 0.89, 'native SBML value', 'Controls Bound Ubiquitin Protease1. Maps to SBML symbol `UbEB`.'),
        'bound_ubiquitin_protease2': ('UbE2B', 1.0, 'native SBML value', 'Controls Bound Ubiquitin Protease2. Maps to SBML symbol `UbE2B`.'),
        'bound_wee1': ('Wee1B', 1.0, 'native SBML value', 'Controls Bound Wee1. Maps to SBML symbol `Wee1B`.'),
        'bound_cdc25': ('Cdc25B', 1.0, 'native SBML value', 'Controls Bound Cdc25. Maps to SBML symbol `Cdc25B`.'),
        'cell_mass': ('Mass', 0.49, 'dimensionless', 'Controls Cell mass. Maps to SBML symbol `Mass`.'),
    }
    _HEADLINE_OUTPUTS = {
        'ubiquitin_protease1': ('UbE', 'native SBML value', 'Tracks Ubiquitin Protease1. Maps to SBML symbol `UbE`.'),
        'ubiquitin_protease2': ('UbE2', 'native SBML value', 'Tracks Ubiquitin Protease2. Maps to SBML symbol `UbE2`.'),
        'wee1_inhibitory_kinase': ('Wee1', 'native SBML value', 'Tracks Wee1 inhibitory kinase. Maps to SBML symbol `Wee1`.'),
        'cdc25_activating_phosphatase': ('Cdc25', 'native SBML value', 'Tracks Cdc25 activating phosphatase. Maps to SBML symbol `Cdc25`.'),
        'cdc13_cdc2': ('G2K', 'native SBML value', 'Tracks Cdc13 Cdc2. Maps to SBML symbol `G2K`.'),
        'free_rum1': ('R', 'native SBML value', 'Tracks Free Rum1. Maps to SBML symbol `R`.'),
        'cig2_cdc2': ('G1K', 'native SBML value', 'Tracks Cig2 Cdc2. Maps to SBML symbol `G1K`.'),
        'intermediary_enzyme': ('IE', 'native SBML value', 'Tracks Intermediary Enzyme. Maps to SBML symbol `IE`.'),
        'cdc13_p_cdc2': ('PG2', 'native SBML value', 'Tracks Cdc13 P Cdc2. Maps to SBML symbol `PG2`.'),
        'cig2_cdc2_rum1': ('G1R', 'native SBML value', 'Tracks Cig2 Cdc2 Rum1. Maps to SBML symbol `G1R`.'),
        'cdc13_cdc2_rum1': ('G2R', 'native SBML value', 'Tracks Cdc13 Cdc2 Rum1. Maps to SBML symbol `G2R`.'),
        'cdc13_p_cdc2_rum1': ('PG2R', 'native SBML value', 'Tracks Cdc13 P Cdc2 Rum1. Maps to SBML symbol `PG2R`.'),
        's_phase_promoting_factor': ('SPF', 'native SBML value', 'Tracks S Phase Promoting Factor. Maps to SBML symbol `SPF`.'),
        'maturation_promoting_factor': ('MPF', 'native SBML value', 'Tracks Maturation-promoting factor. Maps to SBML symbol `MPF`.'),
        'total_rum1': ('Rum1Total', 'native SBML value', 'Tracks Total Rum1. Maps to SBML symbol `Rum1Total`.'),
        'total_cdc13': ('Cdc13Total', 'native SBML value', 'Tracks Total Cdc13. Maps to SBML symbol `Cdc13Total`.'),
        'total_cig2': ('Cig2Total', 'native SBML value', 'Tracks Total Cig2. Maps to SBML symbol `Cig2Total`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000007.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Novak1997CellCycleBiomd0000000007Model = SbmlNovak1997CellCycle
