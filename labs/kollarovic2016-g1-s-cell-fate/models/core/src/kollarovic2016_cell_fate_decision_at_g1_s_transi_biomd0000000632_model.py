# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Kollarovic2016 - Cell fate decision at G1-S transition.

Source: biomodels_ebi:BIOMD0000000632
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000632
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlKollarovic2016CellFateDecisionAtG1STransition(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Kollarovic2016 - Cell fate decision at G1-S transition."""

    _SBML_ID = 'BIOMD0000000632'
    _TITLE = 'Kollarovic2016 - Cell fate decision at G1-S transition'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CycE',
        'Cdk2',
        'CycECdk2',
        'CycECdk2a',
        'p21',
        'DNADamageC',
        'DNADamageS',
        'p53',
    ]
    _SPECIES_LABELS = {
        'CycE': 'Cyclin E',
        'Cdk2': 'CDK2',
        'CycECdk2': 'Cyclin ECdk2',
        'CycECdk2a': 'Cyclin ECdk2a',
        'p21': 'P21',
        'DNADamageC': 'DNA damage Model state C',
        'DNADamageS': 'DNA damage S',
        'p53': 'p53 tumor suppressor',
    }
    _PARAMETER_INPUTS = {
        'ddr': ('DDR', 2.6669080000000003, 'native SBML value', 'Controls DDR. Maps to SBML symbol `DDR`.'),
        'dna_damagefoci_0': ('DNAdamagefoci_0', 0.0, 'dimensionless', 'Controls DNA damagefoci 0. Maps to SBML symbol `DNAdamagefoci_0`.'),
        'base_dna_damage': ('BaseDNAdamage', 2.16068, 'dimensionless', 'Controls Base DNA damage. Maps to SBML symbol `BaseDNAdamage`.'),
    }
    _HEADLINE_OUTPUTS = {
        'cyclin_e': ('CycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `CycE`.'),
        'cdk2': ('Cdk2', 'native SBML value', 'Tracks CDK2. Maps to SBML symbol `Cdk2`.'),
        'cyclin_ecdk2': ('CycECdk2', 'native SBML value', 'Tracks Cyclin ECdk2. Maps to SBML symbol `CycECdk2`.'),
        'cyclin_ecdk2a': ('CycECdk2a', 'native SBML value', 'Tracks Cyclin ECdk2a. Maps to SBML symbol `CycECdk2a`.'),
        'p21': ('p21', 'native SBML value', 'Tracks P21. Maps to SBML symbol `p21`.'),
        'dna_damage_model_state_c': ('DNADamageC', 'native SBML value', 'Tracks DNA damage Model state C. Maps to SBML symbol `DNADamageC`.'),
        'dna_damage_s': ('DNADamageS', 'native SBML value', 'Tracks DNA damage S. Maps to SBML symbol `DNADamageS`.'),
        'p53_tumor_suppressor': ('p53', 'native SBML value', 'Tracks p53 tumor suppressor. Maps to SBML symbol `p53`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000632.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Kollarovic2016CellFateDecisionAtG1STransiBiomd0000000632Model = SbmlKollarovic2016CellFateDecisionAtG1STransition
